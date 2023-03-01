from ppadb.client import Client as AdbClient
from pymem import Pymem
import pymem
import os

#Setup ADB stuff and connect to headset
client = AdbClient(host="127.0.0.1", port=5037) # Connect to adbd
devices = client.devices() # Get list of devices
deviceSerial = devices[0].serial #Get serial of the first device
print("Device Serial/IP: " + deviceSerial) #Print serial
device = client.device(deviceSerial)

def dump_logcat(connection): #Watches for home button up/down events
    while True:
        data = connection.read(1024)
        if not data:
            break
        if "SetHomeButtonDownState" in data.decode('utf-8'):
            try:
                pm = Pymem('vrdashboard.exe') #Test if steamvr dash is running
                print("Home Down")
            except:
                print("Home Down (SteamVR not running)")
                
        if "SetHomeButtonUpState" in data.decode('utf-8'):
            try:
                pm = Pymem('vrdashboard.exe') #Test if steamvr dash is running
                print("Home Up")
                os.system("start \"\" vrmonitor://debugcommands/system_dashboard_toggle")

            except:
                print("Home Up (SteamVR not running)")

    connection.close()

device.shell("logcat -c && logcat -e 'system button' -b main", handler=dump_logcat) # Run logcat and have dump_logcat handle the output