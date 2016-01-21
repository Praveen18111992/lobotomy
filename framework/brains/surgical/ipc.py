from framework.brains.colorize.console import ColorizeConsole
from androguard.core.analysis import analysis
from androguard.decompiler.dad import decompile
from datetime import datetime
from blessings import Terminal
console = ColorizeConsole()
t = Terminal()


class IPCEnum(object):

    values = {

        "android.app.Activity":

            [

                "onCreate",
                "onNewIntent",
                "getIntent",
                "startActivities",
                "startActivity",
                "startActivityForResult",
                "startActivityFromChild",
                "startActivityFromFragment",
                "startActivityIfNeeded",
                "startIntentSender",
                "startIntentSenderForResult",
                "startIntentSenderFromChild",

            ],

        "android.content.Intent":

            [

                "parseUri",
                "parseIntent",
                "addCategory",
                "addFlags",
                "getAction",
                "getBooleanArrayExtra",
                "getBooleanExtra",
                "getBundleExtra",
                "getByteArrayExtra",
                "getByteExtra",
                "getCategories",
                "getCharArrayExtra",
                "getCharExtra",
                "getCharSequenceArrayExtra",
                "getCharSequenceArrayListExtra",
                "getComponent",
                "getDataString",
                "getDoubleExtra",
                "getDoubleString",
                "getExtras",
                "getFlags",
                "getIntent",
                "getIntExtra",
                "getIntArrayExtra",
                "getPackage",
                "getParceableArrayExtra",
                "getScheme",
                "getSelector",
                "getSerializableExtra"
                "putExtra",
                "readFromParcel",
                "setData",
                "setFlags",
                "setSelector",
                "setPackage"

            ],

        "android.content.BroadcastReceiver":

            [

                "onReceive"

            ],

        "android.content.Context":

            [

                "startIntentSender",
                "startService",
                "stopService",
                "startActivities",
                "sendStickyOrderedBroadcast",
                "sendStickyOrderedBroadcastAsUser",
                "sendStickyBroadcast",
                "sendStickyOrderedBroadcast",
                "sendStickyOrderedBroadcastAsUser",
                "sendBroadCast",
                "bindService"

            ],

        "android.app.Service":

            [

                "onBind",
                "onRebind",
                "onStart",
                "onStartCommand",
                "onCreate"

            ]

    }


class IPC(object):

    name = "ipc"

    def __init__(self, vm, vm_type):

        super(IPC, self).__init__()
        self.vm = vm
        self.vm_type = vm_type
        self.enum = IPCEnum()

    def run(self):

        """
        Search for IPC API usage within target class and methods
        """

        if self.vm_type == "apks":

            x = analysis.uVMAnalysis(self.vm.get_vm())
            _vm = self.vm.get_vm()

            selections = [

                "activity",
                "intent",
                "receiver",
                "context",
                "service"

            ]

            print(t.green("[{0}] ".format(datetime.now()) +
                          t.yellow("Available selections: ")))

            for s in selections:
                print(t.green("[{0}] ".format(datetime.now())) + "{0}".format(s))

            selection = raw_input(t.green("[{0}] ".format(datetime.now()) + t.yellow("Enter selection: ")))

            _structure = list()

            for a, b in self.enum.values.items():
                if selection in a.lower():
                    for c in b:
                        paths = x.get_tainted_packages().search_methods("{0}".format(a), "{0}".format(c), ".")
                        if paths:
                            for p in paths:
                                for method in self.vm.get_methods():
                                    if method.get_name() == p.get_src(_vm.get_class_manager())[1]:
                                        if method.get_class_name() == p.get_src(_vm.get_class_manager())[0]:
                                            mx = x.get_method(method)
                                            d = decompile.DvMethod(mx)
                                            d.process()
                                            _structure.append((c, method, d))

            methods = [s[0] for s in _structure]
            methods_set = set(methods)

            for m in methods_set:
                print(t.green("[{0}] ".format(datetime.now()) +
                              t.yellow("Available {0} methods: ".format(selection)) + "{0}".format(m)))

            print(t.green("[{0}] ".format(datetime.now()) +
                          t.yellow("Enter \'back\' to exit")))

            print(t.green("[{0}] ".format(datetime.now()) +
                          t.yellow("Enter \'list\' to show available methods")))

            while True:

                method = raw_input(t.green("[{0}] ".format(datetime.now()) + t.yellow("Enter method selection: ")))

                for s in _structure:
                    if method == s[0]:
                        print(t.green("[{0}] ".format(datetime.now()) +
                                      t.yellow("Found: ") +
                                      "{0}".format(s[0])))
                        print(t.green("[{0}] ".format(datetime.now()) +
                                      t.yellow("Class: ") +
                                      "{0}".format(s[1].get_class_name())))
                        print(t.green("[{0}] ".format(datetime.now()) +
                                      t.yellow("Method: ") +
                                      "{0}".format(s[1].get_name())))
                        print(s[1].show())
                        console.colorize_decompiled_method(str(s[2].get_source()))

                if method == "back":
                    break
                elif method == "list":
                    for m in methods_set:
                        print(t.green("[{0}] ".format(datetime.now()) +
                              t.yellow("Available {0} methods: ".format(selection)) + "{0}".format(m)))

        elif self.vm_type == "dex":

            x = analysis.uVMAnalysis(self.vm)
            _vm = self.vm
            _structure = list()

            selections = [

                "activity",
                "intent",
                "receiver",
                "context",
                "service"

            ]

            print(t.green("[{0}] ".format(datetime.now()) +
                          t.yellow("Available ipc selections: ")))

            for s in selections:
                print(t.green("[{0}] ".format(datetime.now())) + "{0}".format(s))

            selection = raw_input(t.green("[{0}] ".format(datetime.now()) + t.yellow("Enter selection: ")))

            for a, b in self.enum.values.items():
                if selection in a.lower():
                    for c in b:
                        paths = x.get_tainted_packages().search_methods("{0}".format(a), "{0}".format(c), ".")
                        if paths:
                            for p in paths:
                                for method in self.vm.get_methods():
                                    if method.get_name() == p.get_src(_vm.get_class_manager())[1]:
                                        if method.get_class_name() == p.get_src(_vm.get_class_manager())[0]:
                                            mx = x.get_method(method)
                                            d = decompile.DvMethod(mx)
                                            d.process()
                                            _structure.append((c, method, d))

            methods = [s[0] for s in _structure]
            methods_set = set(methods)

            for m in methods_set:
                print(t.green("[{0}] ".format(datetime.now()) +
                              t.yellow("Available {0} methods: ".format(selection)) + "{0}".format(m)))

            print(t.green("[{0}] ".format(datetime.now()) +
                          t.yellow("Enter \'back\' to exit")))

            print(t.green("[{0}] ".format(datetime.now()) +
                          t.yellow("Enter \'list\' to show available methods")))

            while True:

                method = raw_input(t.green("[{0}] ".format(datetime.now()) + t.yellow("Enter method selection: ")))

                for s in _structure:
                    if method == s[0]:
                        print(t.green("[{0}] ".format(datetime.now()) +
                                      t.yellow("Found: ") +
                                      "{0}".format(s[0])))
                        print(t.green("[{0}] ".format(datetime.now()) +
                                      t.yellow("Class: ") +
                                      "{0}".format(s[1].get_class_name())))
                        print(t.green("[{0}] ".format(datetime.now()) +
                                      t.yellow("Method: ") +
                                      "{0}".format(s[1].get_name())))
                        print(s[1].show())
                        console.colorize_decompiled_method(str(s[2].get_source()))

                if method == "back":
                    break
                elif method == "list":
                    for m in methods_set:
                        print(t.green("[{0}] ".format(datetime.now()) +
                              t.yellow("Available {0} methods: ".format(selection)) + "{0}".format(m)))