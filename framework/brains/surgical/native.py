from datetime import datetime
from blessings import Terminal
t = Terminal()


class Native(object):

    name = "native"

    def __init__(self, apks):

        super(Native, self).__init__()
        self.apks = apks

    def run(self):

        """
        Search dynamic code usage
        """

        vm = self.apks.get_vm()
        native_methods = []

        # Re-implementation of the Androguard
        # code in order to handle the returned
        # data
        #
        for method in vm.get_methods():
            if method.get_access_flags() & 0x100:
                native_methods.append((method.get_class_name(), method.get_name()))
        if native_methods:
            print(t.green("[{0}] ".format(datetime.now())
                          + "------"))
            for n in native_methods:
                print(t.green("[{0}] ".format(datetime.now()) +
                              t.yellow("Found: ") + "{0}".format(n[1])))
                print(t.green("[{0}] ".format(datetime.now()) +
                              t.yellow("Class: ") +
                              "{0}".format(n[0])))
                print(t.green("[{0}] ".format(datetime.now()) +
                              t.yellow("------")))
