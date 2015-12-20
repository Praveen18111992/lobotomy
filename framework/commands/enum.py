
class CommandEnum(object):

    # Enum type for
    # commands
    # ---------
    APK = "apk"
    APKS = "apks"
    DEX = "dex"
    # ---------------------------------
    ARGUMENTS = "Not enough arguments!"
    # ----------------------------------------------
    IMPORT_ERROR_LOADER = "Unable to import Loader!"
    IMPORT_ERROR_DECOMPILE = "Unable to import decompile module!"
    IMPORT_ERROR_PROFILER = "Unable to import profiler module!"
    IMPORT_ERROR_PERMISSIONS = "Unable to import permissions module!"
    IMPORT_ERROR_COMPONENTS = "Unable to import components module!"
    IMPORT_ERROR_DEBUGGABLE = "Unable to import debuggable module!"
    IMPORT_ERROR_ATTACKSURFACE = "Unable to import attacksurface module"
    IMPORT_ERROR_D2J = "Unable to import d2j module!"
    IMPORT_ERROR_EXPLOIT = "Unable to import the exploitAPI!"
    IMPORT_ERROR_SURGICAL = "Unable to import the surgicalAPI"
    IMPORT_ERROR_FRIDA = "Unable to import frida module!"
    IMPORT_ERROR_LOGCAT = "Unable to import the logcat module!"
    IMPORT_ERROR_SCALPEL = "Unable to import the scalpel module!"
    # ----------------------------------------------
    STRING_INDEX_ERROR = "string index out of range"
    LIST_INDEX_ERROR = "list index out of range"
    # -------------------------------------------
    MODULE_UNAVAILABLE = "Module not available!"
    # -----------------------------------------------------------------------------------
    DECOMPILE_USAGE = "Usage: decompile <name_of_output_directory> && \"</path/to/apk>\""
    DEBUGGABLE_USAGE = "Usage debuggable <name_of_output_directory> && \"</path/to/apk\""
    LOADER_USAGE = "Usage: loader </path/to/apk> - Load APK which includes classes.dex"
    D2J_USAGE = "Usage: d2j <directory_name> </path/to/apk>"
    # ---------------------------------------------------------------------------------
    PROFILER_MODULE_MESSAGE = "You cannot run the profiler module without a loaded APK"
    PERMISSIONS_LIST_MODULE_MESSAGE = "You cannot list permissions with out a loaded APK"
    PERMISSIONS_MAP_MODULE_MESSAGE = "You cannot map permissions with out an executable or APK"
    COMPONENTS_MODULE_MESSAGE = "You cannot run the components module without a loaded APK"
    ATTACKSURFACE_MODULE_MESSAGE = "You cannot run the attacksurface module without a loaded APK"
    SURGICAL_MODULE_MESSAGE = "You cannot run the surgical module without a target executable"
    FRIDA_MODULE_MESSAGE = "You cannot run the frida module without a loaded APK"
    # ------------------------------------------------
    SCAlPEL_BANNER = "[Vulnerability Analysis Engine]"
    SCAlPEL_SERVER = "Scalpel server starting ... "
    SCALPEL_ARGS_START_SERVER = "start server"

