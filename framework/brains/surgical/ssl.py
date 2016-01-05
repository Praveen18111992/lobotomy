from framework.brains.colorize.console import ColorizeConsole
from androguard.core.analysis import analysis
from androguard.decompiler.dad import decompile
from datetime import datetime
from blessings import Terminal
console = ColorizeConsole()
t = Terminal()


class SSLEnum(object):

    values = {

        "java.net.ssl.SSLSocketFactory": [

            "createSocket",
            "getDefault",
            "getDefaultCipherSuites",
            "getSupportCipherSuites"

        ],

        "android.net.ssl.SSLCertificateSocketFactory": [

            "createSocket",
            "getDefault",
            "getDefaultCipherSuites",
            "getInsecure",
            "getSupportedCipherSuites",
            "setHostname",
            "setKeyManagers",
            "setUseSessionTickets"

        ],

        "javax.net.ssl.SSLSocket": [

            "addHandshakeCompletedListener",
            "getEnableSessionCreation",
            "getEnabledCipherSuites",
            "getEnabledProtocols",
            "getNeedClientAuth",
            "getSSLParameters",
            "getSession",
            "getSupportedCipherSuites",
            "getSupportedProtocols",
            "getUseClientMode",
            "getWantClientAuth",
            "removeHandshakeCompletedListener",
            "setEnableSessionCreation",
            "setEnabledProtocols",
            "setEnabledCipherSuites",
            "setNeedClientAuth",
            "setSSLParameters",
            "setUseClientMode",
            "setWantClientAuth",
            "shutdownInput",
            "shutdownOutput",
            "startHandshake"

        ],

        "javax.net.ssl.TrustManagerFactory": [

            "getAlgorithm",
            "getDefaultAlgorithm"
            "getInstance",
            "getProvider",
            "getTrustManagers",
            "init"
        ]


    }


class SSL(object):

    name = "ssl"

    def __init__(self, vm, vm_type):

        super(SSL, self).__init__()
        # The vm_type argument is always determined through the loader
        self.vm = vm
        self.vm_type = vm_type
        self.enum = SSLEnum()

    def run(self):

        """
        Search for SSLSocket and TrustManager API usage within target class and methods
        """

        if self.vm_type == "apks":
            # Get the DVM analysis object from Androguard
            x = analysis.uVMAnalysis(self.vm.get_vm())
            _vm = self.vm.get_vm()
            _structure = list()

            if x:
                print(t.green("[{0}] ".format(datetime.now()) + t.yellow("Performing surgery ...")))
                for a, b in self.enum.values.items():
                    for c in b:
                        paths = x.get_tainted_packages().search_methods("{0}".format(a), "{0}".format(c), ".")
                        if paths:
                            for p in paths:
                                for method in self.vm.get_methods():
                                    if method.get_name() == p.get_src(_vm.get_class_manager())[1]:
                                        if method.get_class_name() == p.get_src(_vm.get_class_manager())[0]:
                                            # Start decompilation process for each method
                                            mx = x.get_method(method)
                                            d = decompile.DvMethod(mx)
                                            d.process()
                                            _structure.append((c, method, d))
            # Iterate through the generated methods and
            # create a unique set
            methods = [s[0] for s in _structure]
            methods_set = set(methods)

            for m in methods_set:
                print(t.green("[{0}] ".format(datetime.now()) +
                              t.yellow("Available ssl methods: ") + "{0}".format(m)))

            print(t.green("[{0}] ".format(datetime.now()) +
                          t.yellow("Enter \'back\' to exit")))

            print(t.green("[{0}] ".format(datetime.now()) +
                          t.yellow("Enter \'list\' to show available functions")))

            while True:
                # Selected target method
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
                        print(s[2].get_source())
                        console.colorize_decompiled_method(str(s[2].get_source()))

                if method == "back":
                    break
                elif method == "list":
                    for m in methods_set:
                        print(t.green("[{0}] ".format(datetime.now()) +
                              t.yellow("Available ssl methods: ") + "{0}".format(m)))

        elif self.vm_type == "dex":

            x = analysis.uVMAnalysis(self.vm)
            _vm = self.vm
            _structure = list()

            if x:
                print(t.green("[{0}] ".format(datetime.now()) + t.yellow("Performing surgery ...")))
                for a, b in self.enum.values.items():
                    for c in b:
                        paths = x.get_tainted_packages().search_methods("{0}".format(a), "{0}".format(c), ".")
                        if paths:
                            for p in paths:
                                for method in self.vm.get_methods():
                                    if method.get_name() == p.get_src(_vm.get_class_manager())[1]:
                                        if method.get_class_name() == p.get_src(_vm.get_class_manager())[0]:
                                            # Start decompilation process for each method
                                            mx = x.get_method(method)
                                            d = decompile.DvMethod(mx)
                                            d.process()
                                            _structure.append((c, method, d))
            # Iterate through the generated methods and
            # create a unique set
            methods = [s[0] for s in _structure]
            methods_set = set(methods)

            for m in methods_set:
                print(t.green("[{0}] ".format(datetime.now()) +
                              t.yellow("Available ssl methods: ") + "{0}".format(m)))

            print(t.green("[{0}] ".format(datetime.now()) +
                          t.yellow("Enter \'back\' to exit")))

            print(t.green("[{0}] ".format(datetime.now()) +
                          t.yellow("Enter \'list\' to show available functions")))

            while True:
                # Selected target method
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
                              t.yellow("Available ssl methods: ") + "{0}".format(m)))
