from framework.brains.surgical.storage import InsecureStorage
from framework.brains.surgical.crypto import Crypto
from framework.brains.surgical.logging import Logging
from framework.brains.surgical.ipc import IPC
from framework.brains.surgical.zip import Zip
from framework.brains.surgical.native import Native
from framework.brains.surgical.socket import Socket
from datetime import datetime
from blessings import Terminal
t = Terminal()


class SurgicalAPI(object):

    def __init__(self, apks):

        super(SurgicalAPI, self).__init__()
        self.apk = apks
        self.storage = InsecureStorage(apks)
        self.crypto = Crypto(apks)
        self.logging = Logging(apks)
        self.ipc = IPC(apks)
        self.zip = Zip(apks)
        self.native = Native(apks)
        self.socket = Socket(apks)
        self.functions = [f for f in self.storage,
                          self.crypto,
                          self.logging,
                          self.ipc,
                          self.zip,
                          self.native,
                          self.socket]

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
