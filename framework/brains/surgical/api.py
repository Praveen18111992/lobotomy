from framework.brains.surgical.storage import InsecureStorage
from framework.brains.surgical.crypto import Crypto
from framework.brains.surgical.logging import Logging
from framework.brains.surgical.ipc import IPC
from framework.brains.surgical.zip import Zip
from framework.brains.surgical.native import Native
from framework.brains.surgical.socket import Socket
from framework.brains.surgical.ssl import SSL
from framework.brains.surgical.certkey import CertKey
from framework.brains.surgical.clipboard import ClipBoard
from framework.brains.surgical.bowser import Bowser
from framework.brains.surgical.hash import Hash
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
            self.clipboard = ClipBoard(self.apks, vm_type)
            self.bowser = Bowser(self.apks, vm_type)
            self.hash = Hash(self.apks, vm_type)
            self.modules = [f for f in self.storage,
                            self.crypto,
                            self.logging,
                            self.ipc,
                            self.zip,
                            self.native,
                            self.socket,
                            self.ssl,
                            self.certkey,
                            self.clipboard,
                            self.bowser,
                            self.hash
                            ]

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
            self.clipboard = ClipBoard(self.dex, vm_type)
            self.bowser = Bowser(self.dex, vm_type)
            self.hash = Hash(self.dex, vm_type)
            self.modules = [f for f in self.storage,
                            self.crypto,
                            self.logging,
                            self.ipc,
                            self.zip,
                            self.native,
                            self.socket,
                            self.ssl,
                            self.certkey,
                            self.clipboard,
                            self.bowser,
                            self.hash
                            ]

    def run_surgical(self):

        """
        Helper function for the surgicalAPI
        """

        print(t.green("[{0}] ".format(datetime.now()) + t.yellow("Available modules: ")))

        for m in self.modules:
            print(t.green("[{0}] ".format(datetime.now())) +
                  m.__getattribute__("name"))

        print(t.green("[{0}] ".format(datetime.now()) + t.yellow("Enter \'quit\' to exit")))
        print(t.green("[{0}] ".format(datetime.now()) + t.yellow("Enter \'list\' to show available modules")))

        while True:
            # Assign target API function
            module = raw_input(t.green("[{0}] ".format(datetime.now()) + t.yellow("Enter module: ")))
            # List available surgical modules
            if module == "list":
                for m in self.modules:
                    print(t.green("[{0}] ".format(datetime.now())) +
                          m.__getattribute__("name"))
            if module == "quit":
                break
            # Match on Class attribute and call run() function of target class
            for m in self.modules:
                if module == m.__getattribute__("name"):
                    # Run target module
                    m.run()
