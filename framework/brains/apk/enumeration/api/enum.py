class APIMappings(object):

    mappings = {

        "install_shortcut":

            {
                "permission": "com.android.launcher.permission.INSTALL_SHORTCUT",

                "class":

                    {

                        "android.content.Intent.ShortcutIconResource":

                            {
                                "method": "fromContext"

                            }

                    },

                "method": "fromContext"

            },

        "read_phone_state":

            {
                "permission": "android.permission.READ_PHONE_STATE",

                "classes":

                    {

                        "android.telephony.PhoneStateListener":

                            {
                                "methods":

                                    [

                                        "onCallForwardingIndicatorChanged", "onCallStateChanged",
                                        "onCellInfoChanged", "onCellLocationChanged", "onDataActivity",
                                        "onDataConnectionStateChanged", "onMessageWaitingIndicatorChanged",
                                        "onServiceStateChanged", "onSignalStrengthChanged",
                                        "onSignalStrengthsChanged"

                                    ]

                            },

                        "android.telephony.ServiceState":

                            {

                                "methods":

                                    [

                                        "getlsManualSelection", "getOperatorAlphaLong",
                                        "getOperatorAlphaShort", "getOperatorNumeric", "getRoaming", "getState",
                                        "setlsManualSelection", "setOperatorName", "setRoaming", "setState",
                                        "SetStateOutofService"

                                    ]

                            }

                    },

            },

        "access_coarse_location":

            {
                "permission": "android.permission.ACCESS_COARSE_LOCATION",

                "classes":

                    {

                        "android.location.LocationManager":

                            {
                                "methods":

                                    [

                                        "requestLocationUpdates", "getProviders", "requestSingleUpdate",
                                        "getProvider", "getLastKnownLocation", "isProviderEnabled",
                                        "addProximityAlert", "requestLocationUpdates", "getBestProvider",
                                        "sendExtraCommand"

                                    ]

                            },

                        "android.telephony.TelephonyManager":

                            {

                                "methods":

                                    [

                                        "getNeighboingCellInfo", "getCellLocation", "listen"

                                    ]

                            }

                    },

            },

        "access_fine_location":

            {
                "permission": "android.permission.ACCESS_FINE_LOCATION",

                "classes":

                    {

                        "android.location.LocationManager":

                            {
                                "methods":

                                    [

                                        "requestLocationUpdates", "getProviders", "requestSingleUpdate",
                                        "getProvider", "getLastKnownLocation", "isProviderEnabled",
                                        "addProximityAlert", "requestLocationUpdates", "getBestProvider",
                                        "sendExtraCommand", "addNmeaListner", "addGpsStatusListener"

                                    ]

                            },

                        "android.telephony.TelephonyManager":

                            {

                                "methods":

                                    [

                                        "getNeighboingCellInfo", "getCellLocation"

                                    ]

                            }

                    },

            },

        "access_network_state":

            {
                "permission": "android.permission.ACCESS_NETWORK_STATE",

                "class":

                    {

                        "android.net.ConnectivityManager":

                            {
                                "methods":

                                    [

                                        "getNetworkInfo", "isActiveNetworkMetered", "getNetworkPreferences",
                                        "getActiveNetworkInfo", "getAllNetworkInfo", "stopUsingNetworkFeature",
                                        "startUsingNetworkFeature"

                                    ]

                            }

                    },

            },

        "set_debug_app":

            {

                "permission": "android.permission.SET_DEBUG_APP",

                "class":

                    {
                        "android.os.Debug":

                            {
                                "methods":

                                    [

                                        "changeDebugPort", "dumpHprofData", "dumpService", "waitForDebugger",
                                        "waitingForDebugger", "isDebuggerConnected"

                                    ]

                            }

                    },

            },


        "bluetooth":

            {

                "permission": "android.permission.BLUETOOTH_ADMIN",

                "classes":

                    {


                        "android.bluetooth.BluetoothAdapter":

                            {

                                "methods":

                                    [
                                        "enable", "startDiscovery", "setName", "cancelDiscovery"

                                    ]
                            },

                        "android.bluetooth.BluetoothA2dp":

                            {

                                "methods":

                                    [
                                        "isA2dpPlaying", "disconnect", "setPriority", "connect"
                                    ]
                            },

                        "android.bluetooth.BluetoothHeadset":
                            {

                                "methods":

                                    [

                                        "setPriority", "stopVoiceRecognition", "getPriority",
                                        "connect",

                                    ]
                            }

                    }


            }
    }