import frida
import sys
from framework.logging.logger import Logger
from subprocess import Popen
from datetime import datetime
from blessings import Terminal
t = Terminal()


class Frida(object):

    def __init__(self, apk):
        super(Frida, self).__init__()
        self.apk = apk

    @staticmethod
    def on_message(message, data):
        try:
            if message:
                print(t.green("[{0}] ".format(datetime.now())) + message["payload"])
        except Exception as e:
            print(message)
            print(e)

    @staticmethod
    def do_inputStream():

        """
        Instrument calls made to InputStream functionality
        """

        inputStream = """

        Dalvik.perform(function () {

            var InputStream = Dalvik.use("java.io.InputStream");

            InputStream.read.overload("java.lang.Byte","java.lang.Integer","java.lang.Integer").implementation = function (b, i, i) {

                send("read()");

                this.read.overload("java.lang.Byte", "java.lang.Integer", "java.lang.Integer").call(this, b, i, i);

            };

        });

        """

        return inputStream

    @staticmethod
    def do_webview():

        """
        Instrument calls made to WebViews - loadUrl(), addJavascriptInterface()
        """

        web_view = """

        Dalvik.perform(function () {

            var WebView = Dalvik.use("android.webkit.WebView");

            WebView.loadUrl.overload("java.lang.String").implementation = function (s) {

                send("loadUrl()");

                this.loadUrl.overload("java.lang.String").call(this, s);

            };

        });

        """

        return web_view

    @staticmethod
    def do_activities():

        """
        Instrument calls made to activities - onCreate(), onNewIntent()
        """

        activities = """

        Dalvik.perform(function () {

            var Activity = Dalvik.use("android.app.Activity");

            Activity.onCreate.implementation = function (b) {

                currentActivity = this.getComponentName();

                send("onCreate()");
                send(currentActivity.toString());

                this.onCreate(b);
            };

        });

        """

        return activities

    def run_frida(self):

        """
        Select and run instrumentation function using the
        Frida instrumentation toolkit
        """

        while True:
            print(t.green("[{0}] ".format(datetime.now()) +
                          t.cyan("Enter 'quit' to exit Frida module!")))

            print(t.green("[{0}] ".format(datetime.now()) +
                          t.yellow("Available Frida functions: ") +
                          "activities, webview, inputStream"))

            function = raw_input(t.green("[{0}] ".format(datetime.now())
                                         + t.yellow("Enter Frida function: ")))

            if function == "quit":
                break
            try:
                if function == "activities":
                    Popen("adb forward tcp:27042 tcp:27042", shell=True).wait()
                    process = frida.get_device_manager().enumerate_devices()[-1].attach(self.apk.get_package())
                    script = process.create_script(self.do_activities())
                    script.on('message', self.on_message)
                    script.load()
                    sys.stdin.read()
                elif function == "webview":
                    Popen("adb forward tcp:27042 tcp:27042", shell=True).wait()
                    process = frida.get_device_manager().enumerate_devices()[-1].attach(self.apk.get_package())
                    script = process.create_script(self.do_webview())
                    script.on('message', self.on_message)
                    script.load()
                    sys.stdin.read()
                elif function == "inputStream":
                    Popen("adb forward tcp:27042 tcp:27042", shell=True).wait()
                    process = frida.get_device_manager().enumerate_devices()[-1].attach(self.apk.get_package())
                    script = process.create_script(self.do_inputStream())
                    script.on('message', self.on_message)
                    script.load()
                    sys.stdin.read()
            except frida.ProcessNotFoundError as e:
                print(t.red("[{0}] ".format(datetime.now()) +
                            "Could not connect to target process!"))
                Logger.run_logger(e.message)
            except frida.ServerNotRunningError as e:
                print(t.red("[{0}] ".format(datetime.now()) +
                            "The frida-server is not running!"))
                Logger.run_logger(e.message)
            except frida.TransportError as e:
                print(t.red("[{0}] ".format(datetime.now()) +
                            "Connection was closed!"))
                Logger.run_logger(e.message)
            except KeyboardInterrupt:
                pass
