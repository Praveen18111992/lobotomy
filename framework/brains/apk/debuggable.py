import os
from framework.logging.logger import Logger
from subprocess import Popen
from datetime import datetime
from xml.dom import DOMException
from xml.dom import minidom
from framework.brains.apk.enum import APKEnum as enum
from blessings import Terminal
t = Terminal()


class Debuggable(object):

    def __init__(self, directory, apk):
        super(Debuggable, self).__init__()
        self.directory = directory
        self.apk = apk

    def run_debuggable(self):

        """
        This will take a target APK decompile with with the apktool.jar and add the attribute
        android:debuggable to the <application/> tag

        It will the rebuild the APK from the output directory and sign it with a JKS key so it can be deployed back
        to the target device
        """

        print(t.green("[{0}] ".format(datetime.now())) + t.yellow("Decompiling : ") + self.apk)

        try:
            Popen(
                ["java -jar {0} d {1} -f -o output/{2}".format("".join([os.getcwd(), "/bin/apktool.jar"]),
                                                               self.apk,
                                                               self.directory)], shell=True).wait()

            print(t.green("[{0}] ".format(datetime.now())) + t.yellow(enum.ADDING_DEBUGGABLE))

            with open("output/{0}/AndroidManifest.xml".format(self.directory), "r+") as manifest:
                # Read in the AndroidManifest.xml
                #
                xml = minidom.parseString(manifest.read())
                # Get the <application/> tag element
                #
                application = xml.getElementsByTagName("application")
                # Set the debuggable attribute within the
                # application tag element
                #
                application[0].setAttribute("android:debuggable", "true")
                # Write and close the modified XML
                #
                manifest.seek(0)
                xml.writexml(manifest)
                manifest.truncate()
                manifest.close()
        # Exception handlers
        # for I/O, OS, and DOM issues
        #
        except OSError as e:
            print(t.red("[{0}]".format(datetime.now()) + enum.DEBUGGABLE_PROCESS_EXCEPTION))
            Logger.run_logger(e.message)
        except IOError as e:
            print(t.red("[{0}]".format(datetime.now()) + enum.DEBUGGABLE_IO_EXCEPTION))
            Logger.run_logger(e.message)
        except DOMException as e:
            print(t.red("[{0}]".format(datetime.now()) + enum.DEBUGGABLE_XML_EXCEPTION))
            Logger.run_logger(e.message)

        try:
            print(t.green("[{0}] ".format(datetime.now())) +
                  t.yellow(enum.DEBUGGABLE_BUILDING_APK) +
                  self.directory)

            Popen(["java -jar {0} b output/{1} -o output/{1}/{1}.apk".format("".join([os.getcwd(), "/bin/apktool.jar"]),
                                                                             self.directory)], shell=True).wait()

            print(t.green("[{0}] ".format(datetime.now())) + t.yellow(enum.DEBUGGABLE_BUILD_COMPLETE))
            print(t.green("[{0}] ".format(datetime.now())) + t.yellow(enum.DEBUGGABLE_APK_SIGNING))

            Popen(["keytool -genkey -v -keystore lobotomy-key.keystore "
                   "-alias lobotomy -keyalg RSA -keysize 2048 -validity 10000"],
                  shell=True).wait()

            Popen(["jarsigner -verbose -sigalg SHA1withRSA -digestalg SHA1 "
                   "-keystore lobotomy-key.keystore output/{0}/{0}.apk lobotomy".format(self.directory)],
                  shell=True).wait()

            print(t.green("[{0}] ".format(datetime.now())) + t.yellow("Freshly signed APK is located at : ") +
                  "output/{0}/{0}.apk".format(self.directory))

            # We want to create a fresh keystore
            # every time we build and sign a new APK
            #
            Popen(["rm lobotomy-key.keystore"], shell=True).wait()
        # Exception handler
        # for process exception
        # issues
        #
        except OSError as e:
            print(t.red("[{0}]".format(datetime.now()) + enum.DEBUGGABLE_PROCESS_EXCEPTION))
            Logger.run_logger(e.message)
