import os
from framework.logging.logger import Logger
from subprocess import Popen, CalledProcessError
from datetime import datetime
from blessings import Terminal
t = Terminal()


class Decompile(object):

    def __init__(self, directory, apk):
        super(Decompile, self).__init__()
        self.apk = apk
        self.directory = directory

    def run_decompile(self):

        """
        Decompiles target APK with apktool.jar
        """

        print(t.green("[{0}] ".format(datetime.now())) + t.yellow("Decompiling : ") + self.apk)

        try:
            Popen("java -jar {0} d {1} -f -o output/{2}".format("".join([os.getcwd(), "/bin/apktool.jar"]),
                                                                self.apk,
                                                                self.directory), shell=True).wait()
            print(t.green("[{0}] ".format(datetime.now())) + t.yellow("Finished!"))
        # Exception handler
        # for process issues
        #
        except CalledProcessError as e:
            print(t.red("[{0}] ".format(datetime.now)) + e.returncode)
            Logger.run_logger(e.message)
