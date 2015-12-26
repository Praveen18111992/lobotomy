from framework.brains.surgical.storage import InsecureStorage
from framework.brains.surgical.crypto import Crypto
from framework.brains.surgical.logging import Logging
from framework.brains.surgical.ipc import IPC
from framework.brains.surgical.zip import Zip
from framework.brains.surgical.native import Native
from framework.brains.surgical.socket import Socket
from framework.brains.surgical.ssl import SSL
from framework.brains.surgical.certkey import CertKey
from datetime import datetime
from blessings import Terminal
t = Terminal()


class SurgicalAPI(object):

    def __init__(self, vm, vm_type):

        super(SurgicalAPI, self).__init__()

        if vm_type == "apks":
            self.apks = vm
            self.storage = InsecureStorage(self.apks, vm_type)
            self.crypto = Crypto(self.apks, vm_type)
            self.logging = Logging(self.apks, vm_type)
            self.ipc = IPC(self.apks, vm_type)
            self.zip = Zip(self.apks, vm_type)
            self.native = Native(self.apks, vm_type)
            self.socket = Socket(self.apks, vm_type)
            self.ssl = SSL(self.apks, vm_type)
            self.certkey = CertKey(self.apks, vm_type)
            self.functions = [f for f in self.storage,
                              self.crypto,
                              self.logging,
                              self.ipc,
                              self.zip,
                              self.native,
                              self.socket,
                              self.ssl,
                              self.certkey]

        elif vm_type == "dex":
            self.dex = vm
            self.storage = InsecureStorage(self.dex, vm_type)
            self.crypto = Crypto(self.dex, vm_type)
            self.logging = Logging(self.dex, vm_type)
            self.ipc = IPC(self.dex, vm_type)
            self.zip = Zip(self.dex, vm_type)
            self.native = Native(self.dex, vm_type)
            self.socket = Socket(self.dex, vm_type)
            self.ssl = SSL(self.dex, vm_type)
            self.certkey = CertKey(self.dex, vm_type)
            self.functions = [f for f in self.storage,
                              self.crypto,
                              self.logging,
                              self.ipc,
                              self.zip,
                              self.native,
                              self.socket,
                              self.ssl,
                              self.certkey]

    def run_surgical(self):

        """
        Helper function for API
        """

        print(t.green("[{0}] ".format(datetime.now()) +
                      t.yellow("Available functions: ")))

        for f in self.functions:
            print(t.green("[{0}] ".format(datetime.now())) +
                  f.__getattribute__("name"))

        print(t.green("[{0}] ".format(datetime.now()) +
                      t.yellow("Enter \'quit\' to exit")))

        print(t.green("[{0}] ".format(datetime.now()) +
                      t.yellow("Enter \'list\' to show available functions")))

        while True:
            # Assign target API
            # function
            #
            function = raw_input(t.green("[{0}] ".format(datetime.now()) + t.yellow("Enter function: ")))

            if function == "list":
                for f in self.functions:
                    print(t.green("[{0}] ".format(datetime.now())) +
                          f.__getattribute__("name"))
            if function == "quit":
                break
            # Match on Class attribute
            # and call run() function
            # of target class
            #
            for f in self.functions:
                if function == f.__getattribute__("name"):
                    f.run()
