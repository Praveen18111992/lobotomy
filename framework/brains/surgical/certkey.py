from framework.brains.colorize.console import ColorizeConsole
from androguard.core.analysis import analysis
from androguard.decompiler.dad import decompile
from datetime import datetime
from blessings import Terminal
console = ColorizeConsole()
t = Terminal()


class CertKeyEnum(object):

    values = {

        "java.security.cert.CertStore": [

            "getCRLs",
            "getCertStoreParameters",
            "getCertificates",
            "getDefaultType",
            "getInstances",
            "getProvider",
            "getType"

        ],

        "android.security.keystore.KeyGenParameterSpec": [

            "getAlgorithmParameterSpec",
            "getBlockModes",
            "getCertificateNotAfter",
            "getCertificateNotBefore",
            "getCertificateSerialNumber",
            "getCertificateSubject",
            "getDigests",
            "getEncryptionPaddings",
            "getKeySize",
            "getKeyValidityForConsumptionEnd",
            "getKeyValidityForOriginationEnd",
            "getKeyValidityStart",
            "getKeystoreAlias",
            "getPurposes",
            "getSignaturePaddings",
            "getUserAuthenticationValidtyDurationSeconds",
            "isDigestsSpecified",
            "isRandomizedEncryptionRequired",
            "isUserAuthenticationRequired"

        ],

        "java.security.KeyStore": [

            "aliases",
            "containsAlias",
            "deleteEntry",
            "entryInstanceOf",
            "getCertificate",
            "getCertificateAlias",
            "getCertificateChain",
            "getCreationDate",
            "getDefaultType",
            "getEntry",
            "getInstance",
            "getProvider",
            "getType",
            "isCertificateEntry",
            "isKeyEntry",
            "load",
            "setCertificateEntry",
            "setEntry",
            "setKeyEntry",
            "size",
            "store"

        ],

        "java.security.KeyStore.Builder": [

            "getKeyStore",
            "getProtectionParameter",
            "newInstance",

        ],

        "java.security.KeyStore.LoadStoreParameter": [

            "getProtectionParameter"
        ],

        "java.security.KeyStore.PasswordProtection": [

            "destroy",
            "getPassword",
            "isDestroyed"

        ],

        "java.security.KeyStore.PrivateKeyEntry": [

            "getCertificate",
            "getCertificateChain",
            "getPrivateKey"
        ],

        "java.security.KeyStore.SecretKeyEntry": [

            "getSecretKey"
        ],

        "java.security.KeyStore.TrustedCertificateEntry": [

            "getTrustedCertificate"
        ]

    }


class CertKey(object):

    name = "certkey"

    def __init__(self, vm, vm_type):
        super(CertKey, self).__init__()
        self.vm = vm
        self.vm_type = vm_type
        self.enum = CertKeyEnum()

    def run(self):

        """
        Search for CertificateManager and Keystore API usage within target class and methods
        """

        if self.vm_type == "apks":

            _x = analysis.uVMAnalysis(self.vm.get_vm())
            _vm = self.vm.get_vm()
            _structure = list()

            if _x:
                print(t.green("[{0}] ".format(datetime.now()) + t.yellow("Performing surgery ...")))
                for a, b in self.enum.values.items():
                    for c in b:
                        paths = _x.get_tainted_packages().search_methods("{0}".format(a), "{0}".format(c), ".")
                        if paths:
                            for p in paths:
                                for method in self.vm.get_methods():
                                    if method.get_name() == p.get_src(_vm.get_class_manager())[1]:
                                        if method.get_class_name() == p.get_src(_vm.get_class_manager())[0]:
                                            mx = _x.get_method(method)
                                            d = decompile.DvMethod(mx)
                                            d.process()
                                            _structure.append((c, method, d))

            methods = [s[0] for s in _structure]
            methods_set = set(methods)

            for m in methods_set:
                print(t.green("[{0}] ".format(datetime.now()) +
                              t.yellow("Available certkey method: ") + "{0}".format(m)))

            print(t.green("[{0}] ".format(datetime.now()) + t.yellow("Enter \'back\' to exit")))
            print(t.green("[{0}] ".format(datetime.now()) + t.yellow("Enter \'list\' to show available methods")))

            while True:
                method = raw_input(t.green("[{0}] ".format(datetime.now()) + t.yellow("Enter method selection: ")))

                for s in _structure:
                    if method == s[0]:
                        print(t.green("[{0}] ".format(datetime.now()) + t.yellow("Found: ") +
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
                              t.yellow("Available certkey method: ") + "{0}".format(m)))

        elif self.vm_type == "dex":

            _x = analysis.uVMAnalysis(self.vm)
            _vm = self.vm
            _structure = list()

            if _x:
                print(t.green("[{0}] ".format(datetime.now()) + t.yellow("Performing surgery ...")))
                for a, b in self.enum.values.items():
                    for c in b:
                        paths = _x.get_tainted_packages().search_methods("{0}".format(a), "{0}".format(c), ".")
                        if paths:
                            for p in paths:
                                for method in self.vm.get_methods():
                                    if method.get_name() == p.get_src(_vm.get_class_manager())[1]:
                                        if method.get_class_name() == p.get_src(_vm.get_class_manager())[0]:
                                            mx = _x.get_method(method)
                                            d = decompile.DvMethod(mx)
                                            d.process()
                                            _structure.append((c, method, d))

            methods = [s[0] for s in _structure]
            methods_set = set(methods)

            for m in methods_set:
                print(t.green("[{0}] ".format(datetime.now()) +
                              t.yellow("Available certkey method: ") + "{0}".format(m)))

            print(t.green("[{0}] ".format(datetime.now()) + t.yellow("Enter \'back\' to exit")))
            print(t.green("[{0}] ".format(datetime.now()) + t.yellow("Enter \'list\' to show available methods")))

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
                              t.yellow("Available certkey method: ") + "{0}".format(m)))
