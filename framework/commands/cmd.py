from datetime import datetime
from cmd2 import Cmd as Lobotomy
from blessings import Terminal
from framework.logging.logger import Logger
from framework.commands.enum import CommandEnum as enum
t = Terminal()


class Run(Lobotomy):

    def __init__(self):

        Lobotomy.__init__(self)

    # APK related commands
    # --------------------
    # loader, decompile, debuggable,
    # profiler, permissions, components
    #

    @staticmethod
    def do_loader(args):
        """
        Description: Load target APK or classes.dex for analysis

        Requirements: APK or Dalvik Executable

        Usage: loader </path/to/apk> - Load APK which includes classes.dex
        Usage: loader apk </path/to/apk> - Load APK which does not include classes.dex
        Usage: loader dex </path/to/classes.dex> - Load classes.dex
        """
        try:
            from framework.brains.apk.loader import Loader
            # Pass arguments to the loader module
            loader = Loader(args)
            # Define global variables
            global apk, apks, dex
            # Begin to check command line arguments for the loader module
            if args:
                # APK only
                if args.split()[0] == enum.APK:
                    apk, apks = loader.run_loader(), None
                # DEX only
                elif args.split()[0] == enum.DEX:
                    dex, apk, apks = loader.run_loader(), None, None
                else:
                    apk, apks = loader.run_loader()
            else:
                print(t.red("[{0}] ".format(datetime.now()) + t.white(enum.ARGUMENTS)))
        except Exception as e:
            if e.message == enum.STRING_INDEX_ERROR or e.message == enum.LIST_INDEX_ERROR:
                print(t.red("[{0}] ".format(datetime.now()) + t.white(enum.ARGUMENTS)))
                print(t.red("[{0}] ".format(datetime.now()) + t.white(enum.LOADER_USAGE)))
        except ImportError as e:
            print(t.red("[{0}] ".format(datetime.now()) + enum.IMPORT_ERROR_LOADER))
            Logger.run_logger(e.message)

    @staticmethod
    def do_decompile(args):
        """
        Description: Decompile target APK with apktool.jar

        Requirements: Target APK

        Usage: decompile <name_of_output_directory> && </path/to/apk>
        """
        try:
            from framework.brains.apk.decompile import Decompile
            if args[0] and args[1]:
                decompile = Decompile(args.split()[0], args.split()[1])
                decompile.run_decompile()
            else:
                print(t.red("[{0}] ".format(datetime.now()) +
                            t.white(enum.ARGUMENTS)))
        except Exception as e:
            if e.message == enum.STRING_INDEX_ERROR or e.message == enum.LIST_INDEX_ERROR:
                print(t.red("[{0}] ".format(datetime.now()) +
                            t.white(enum.ARGUMENTS)))
                print(t.red("[{0}] ".format(datetime.now()) +
                            t.white(enum.DECOMPILE_USAGE)))
        except ImportError as e:
            print(t.red("[{0}] ".format(datetime.now()) +
                        t.white(enum.IMPORT_ERROR_DECOMPILE)))
            Logger.run_logger(e.message)

    @staticmethod
    def do_profiler(args):
        """
        Description: Run profiling on the target APK loaded

        Requirements: Loaded APK

        Usage: profiler
        """
        try:
            from framework.brains.apk.enumeration.profiler import Profiler
            if globals()["apk"] is not None:
                p = Profiler(globals()["apk"])
                p.run_profiler()
            else:
                print(t.red("[{0}] ".format(datetime.now())) +
                      t.white(enum.MODULE_UNAVAILABLE))
                print(t.red("[{0}] ".format(datetime.now())) +
                      t.white(enum.PROFILER_MODULE_MESSAGE))
        except ImportError as e:
            print(t.red("[{0}] ".format(datetime.now()) + enum.IMPORT_ERROR_LOADER))
            Logger.run_logger(e.message)

    @staticmethod
    def do_permissions(args):
        """
        Description: List enumeration and api mappings from target APK

        Requirements: Loaded APK

        Usage: permissions <list> || <map>
        """
        try:
            from framework.brains.apk.enumeration.permissions import PermissionsList, PermissionsMap
            if args:
                if args == "list":
                    if globals()["apk"] is not None:
                        # Instantiate permissions
                        # module
                        #
                        p = PermissionsList(globals()["apk"])
                        p.run_list_permissions()
                    else:
                        print(t.red("[{0}] ".format(datetime.now())) +
                              t.white(enum.MODULE_UNAVAILABLE))
                        print(t.red("[{0}] ".format(datetime.now())) +
                              t.white(enum.PERMISSIONS_LIST_MODULE_MESSAGE))
                if args == "map":
                    if globals()["apk"] is not None and globals()["apks"] is not None:
                        # Instantiate permissions
                        # module
                        p = PermissionsMap(globals()["apk"], globals()["apks"])
                        p.run_map_permissions()
                    else:
                        print(t.red("[{0}] ".format(datetime.now())) +
                              t.white(enum.MODULE_UNAVAILABLE))
                        print(t.red("[{0}] ".format(datetime.now())) +
                              t.white(enum.PERMISSIONS_MAP_MODULE_MESSAGE))
            else:
                print(t.red("[{0}] ".format(datetime.now()) +
                            t.white(enum.ARGUMENTS)))
        except Exception as e:
            if e.message == enum.STRING_INDEX_ERROR or e.message == enum.LIST_INDEX_ERROR:
                print(t.red("[{0}] ".format(datetime.now()) +
                            t.white(enum.ARGUMENTS)))
                print(t.red("[{0}] ".format(datetime.now()) +
                            t.white(enum.DECOMPILE_USAGE)))
        except ImportError as e:
            print(t.red("[{0}] ".format(datetime.now()) + enum.IMPORT_ERROR_PERMISSIONS))
            Logger.run_logger(e.message)

    @staticmethod
    def do_components(args):
        """
        Description: Enumerate components for target APK

        Requirements: Loaded APK

        Usage: components
        """
        try:
            from framework.brains.apk.enumeration.components import Components
            if globals()["apk"] is not None:
                # Instantiate components
                # module
                #
                c = Components(globals()["apk"])
                c.enum_component()
            else:
                print(t.red("[{0}] ".format(datetime.now())) +
                      t.white(enum.MODULE_UNAVAILABLE))
                print(t.red("[{0}] ".format(datetime.now())) +
                      t.white(enum.COMPONENTS_MODULE_MESSAGE))
        except ImportError as e:
            print(t.red("[{0}] ".format(datetime.now()) + enum.IMPORT_ERROR_COMPONENTS))
            Logger.run_logger(e.message)

    @staticmethod
    def do_attacksurface(args):
        """
        Description: Enumerates attacksurface for target APK

        Requirements: Loaded APK

        Usage: attacksurface
        """
        try:
            from framework.brains.apk.enumeration.attack_surface import AttackSurface
            if globals()["apk"] is not None:
                # Instantiate attacksurface
                # module
                #
                c = AttackSurface(globals()["apk"])
                c.run_enum_attack_surface()
            else:
                print(t.red("[{0}] ".format(datetime.now())) +
                      t.white(enum.MODULE_UNAVAILABLE))
                print(t.red("[{0}] ".format(datetime.now())) +
                      t.white(enum.ATTACKSURFACE_MODULE_MESSAGE))
        except ImportError as e:
            print(t.red("[{0}] ".format(datetime.now()) + enum.IMPORT_ERROR_ATTACKSURFACE))
            Logger.run_logger(e.message)

    @staticmethod
    def do_debuggable(args):
        """
        Description: Make target APK debuggable

        Requirements: Target APK

        Usage: debuggable <name_of_output_directory> && </path/to/apk>
        """
        try:
            from framework.brains.apk.debuggable import Debuggable
            # Instantiate debuggable
            # module
            #
            d = Debuggable(args.split()[0], args.split()[1])
            d.run_debuggable()
        except ImportError as e:
            print(t.red("[{0}] ".format(datetime.now()) + enum.IMPORT_ERROR_DEBUGGABLE))
            Logger.run_logger(e.message)
        except Exception as e:
            if e.message == enum.STRING_INDEX_ERROR or e.message == enum.LIST_INDEX_ERROR:
                print(t.red("[{0}] ".format(datetime.now()) +
                            t.white(enum.ARGUMENTS)))
                print(t.red("[{0}] ".format(datetime.now()) +
                            t.white(enum.DEBUGGABLE_USAGE)))

    # dex2jar
    # --------------------
    # d2j
    #

    @staticmethod
    def do_d2j(args):
        """
        Description: Runs d2j-dex2jar.sh on the target APK

        Requirements: Target APK

        Usage: d2j <directory_name> </path/to/apk>
        """
        try:
            from framework.brains.dex2jar.d2j import D2J
            # Instantiate d2j
            # module
            #
            d = D2J(args.split()[0], args.split()[1])
            d.run_d2j()
        except ImportError as e:
            print(t.red("[{0}] ".format(datetime.now()) + enum.IMPORT_ERROR_D2J))
            Logger.run_logger(e.message)
        except Exception as e:
            if e.message == enum.STRING_INDEX_ERROR or e.message == enum.LIST_INDEX_ERROR:
                print(t.red("[{0}] ".format(datetime.now()) +
                            t.white(enum.ARGUMENTS)))
                print(t.red("[{0}] ".format(datetime.now()) +
                            t.white(enum.D2J_USAGE)))

    # Dynamic
    # -----------------------
    # logcat, instrumentation
    #

    @staticmethod
    def do_logcat(args):
        """
        Description: Runs logcat against the target APK and sends the output
                     to its RESTFul service handler

        Requirements: Loaded APK

        Usage: logcat
        """
        try:
            from framework.brains.dynamic.logcat import Logcat
            # Instantiate logcat
            # module
            #
            l = Logcat()
            l.run_logcat()
        except ImportError as e:
            print(t.red("[{0}] ".format(datetime.now()) + enum.IMPORT_ERROR_LOGCAT))
            Logger.run_logger(e.message)

    @staticmethod
    def do_frida(args):
        """
        Description: Runs the Frida instrumentation toolkit against a target process

        Requirements: Loaded APK

        Usage: frida
        """
        try:
            from framework.brains.dynamic.frida.instrumentation import Frida
            if globals()["apk"] is not None:
                # Instantiate frida
                # module
                #
                i = Frida(globals()["apk"])
                i.run_frida()
            else:
                print(t.red("[{0}] ".format(datetime.now())) +
                      t.white("Module not available"))
                print(t.red("[{0}] ".format(datetime.now())) +
                      t.white(enum.FRIDA_MODULE_MESSAGE))
        except ImportError as e:
            print(t.red("[{0}] ".format(datetime.now()) + enum.IMPORT_ERROR_FRIDA))
            Logger.run_logger(e.message)

    # Surgical
    # --------------------
    # This module is designed to find android API implementations
    # in the target APK
    #

    @staticmethod
    def do_surgical(args):
        """
        Description: Instantiates the SurgicalAPI with available functions and operations

        Requirements: Loaded APK

        Usage: surgical
        """
        try:
            from framework.brains.surgical.api import SurgicalAPI
            if globals()["apks"] is not None:
                # Instantiate surgicalAPI
                #
                s = SurgicalAPI(globals()["apks"], "apks")
                s.run_surgical()
            elif globals()["dex"] is not None:
                s = SurgicalAPI(globals()["dex"], "dex")
                s.run_surgical()
            else:
                print(t.red("[{0}] ".format(datetime.now())) +
                      t.white(enum.MODULE_UNAVAILABLE))
                print(t.red("[{0}] ".format(datetime.now())) +
                      t.white(enum.SURGICAL_MODULE_MESSAGE))
        except ImportError as e:
            print(t.red("[{0}] ".format(datetime.now()) + enum.IMPORT_ERROR_SURGICAL))
            Logger.run_logger(e.message)

    # Exploits
    # --------------------
    # Collection of available exploits
    #
    #

    @staticmethod
    def do_exploit(args):
        """
        Description: Instantiates the ExploitAPI with available exploits

        Requirements: Loaded APK

        Usage: [exploit] & [type] & [name] [module] - Example: exploit browser mercury wfm
        """
        try:
            from framework.brains.exploits.api import ExploitAPI
            if args.split()[0] and args.split()[1] and args.split()[2]:
                # Instantiate exploitAPI
                #
                ExploitAPI(exploit=args.split()[0], name=args.split()[1], module=args.split()[2])
            else:
                print(t.red("[{0}] ".format(datetime.now()) + enum.ARGUMENTS))
        except ImportError as e:
            print(t.red("[{0}] ".format(datetime.now()) + enum.IMPORT_ERROR_EXPLOIT))
            Logger.run_logger(e.message)

    # Scalpel - Vulnerability Analysis (BETA)
    # --------------------------------

    @staticmethod
    def do_scalpel(args):
        """
        Description:
        Requirements:
        Usage:
        """
        if args:
            if args == enum.SCALPEL_ARGS_START_SERVER:
                print(t.green("[{0}] ".format(datetime.now()) +
                              t.red(enum.SCAlPEL_BANNER) +
                              t.yellow(enum.SCAlPEL_SERVER)))
                try:
                    from framework.brains.scalpel.server.scalpel_server import ScalpelServer
                    global scalpel
                    # Instantiate the ScalpelServer
                    #
                    scalpel = ScalpelServer()
                    scalpel.run()
                except ImportError as e:
                    print(t.red("[{0}] ".format(datetime.now()) + enum.IMPORT_ERROR_SCALPEL))
                    Logger.run_logger(e.message)
        else:
            print(t.red("[{0}] ".format(datetime.now()) + enum.ARGUMENTS))


