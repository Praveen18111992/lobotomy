from datetime import datetime
import sys
import struct
from androguard.core.bytecodes.apk import APK
from androguard.core.androgen import AndroguardS
from androguard.core.bytecodes import dvm
from androguard.util import read
from blessings import Terminal

t = Terminal()


class Loader(object):

    def __init__(self, args):
        super(Loader, self).__init__()
        self.args = args.split()

    def run_loader(self):

        """
        Load the target APK and return
        the loaded instance, which will
        be stored as a global
        """

        if self.args[0] == "apk":
            print(t.green("[{0}] ".format(datetime.now()) + t.yellow("Loading : ") + "{0}".format(self.args[1])))
            try:
                apk = APK(self.args[1])
                return apk
            except IOError as e:
                raise e

        elif self.args[0] == "dex":
            print(t.green("[{0}] ".format(datetime.now()) + t.yellow("Loading : ") + "{0}".format(self.args[1])))
            try:
                d = dvm.DalvikVMFormat(read(self.args[1], binary=False))
                return d
            except IOError as e:
                raise e

        else:
            print(t.green("[{0}] ".format(datetime.now()) + t.yellow("Loading : ") + "{0}".format(self.args[0])))
            try:
                apk = APK(self.args[0])
                apks = AndroguardS(self.args[0])
                return apk, apks
            except struct.error:
                print(t.red("[{0}] ".format(datetime.now())) +
                      t.white("The application does not contain an executable file"))
                print(t.red("[{0}] ".format(datetime.now())) +
                      t.white("Please load the application as an APK only"))
                sys.exit(1)

