from datetime import datetime
from blessings import Terminal
t = Terminal()


class Native(object):

    name = "native"

    def __init__(self, vm, vm_type):

        super(Native, self).__init__()
        self.vm = vm
        self.vm_type = vm_type

    def run(self):

        """
        Search native method usage
        """

        if self.vm_type == "apks":
            _vm = self.vm.get_vm()
            _native_methods = list()
            # Re-implementation of the Androguard code in order to handle the returned data
            for method in _vm.get_methods():
                if method.get_access_flags() & 0x100:
                    _native_methods.append((method.get_class_name(), method.get_name()))
            if _native_methods:
                print(t.green("[{0}] ".format(datetime.now()) + "------"))
                for n in _native_methods:
                    print(t.green("[{0}] ".format(datetime.now()) + t.yellow("Found: ") + "{0}".format(n[1])))
                    print(t.green("[{0}] ".format(datetime.now()) + t.yellow("Class: ") + "{0}".format(n[0])))
                    print(t.green("[{0}] ".format(datetime.now()) + t.yellow("------")))
        elif self.vm_type == "dex":
            _native_methods = list()
            for method in self.vm.get_methods():
                if method.get_access_flags() & 0x100:
                    _native_methods.append((method.get_class_name(), method.get_name()))
            if _native_methods:
                print(t.green("[{0}] ".format(datetime.now()) + "------"))
                for n in _native_methods:
                    print(t.green("[{0}] ".format(datetime.now()) + t.yellow("Found: ") + "{0}".format(n[1])))
                    print(t.green("[{0}] ".format(datetime.now()) + t.yellow("Class: ") + "{0}".format(n[0])))
                    print(t.green("[{0}] ".format(datetime.now()) + t.yellow("------")))

