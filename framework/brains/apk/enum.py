
class APKEnum(object):

    # Enum type for
    # the apk package
    #
    # ---------
    apk = "apk"
    apks = "apks"
    dex = "dex"
    # ---------------------------------------------------------------------
    FILE_TYPE_ERROR = "The application does not contain an executable file!"
    APK_ONLY_ERROR = "Please load the application as an APK only!"
    NOT_AN_APK = "This is not an APK!"
    NOT_A_DEX = "This is not a Dalvik executable!"
    # ------------------------------------------------------
    ADDING_DEBUGGABLE = "Adding android:debuggable=\"true\""
    DEBUGGABLE_PROCESS_EXCEPTION = "Process exception, check the logs!"
    DEBUGGABLE_IO_EXCEPTION = "IO exception, check the logs!"
    DEBUGGABLE_XML_EXCEPTION = "XML exception, check the logs!"
    DEBUGGABLE_BUILDING_APK = "Building APK : "
    DEBUGGABLE_BUILD_COMPLETE = "Building completed"
    DEBUGGABLE_APK_SIGNING = "APK signing process initiated"
