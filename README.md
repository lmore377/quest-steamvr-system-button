# quest-system-button-steamvr
Maps the Quest system button to the SteamVR dashboard. For use with [OculusKiller](https://github.com/LibreQuest/OculusKiller) 

Don't use this without killer installed. You'll run into weird issues with both the steamvr and oculus dashboard trying to open at the same time.

Right now this just opens the dashboard with a short press. 

The provided exe was created using [PyInstaller](https://pyinstaller.org/en/stable/operating-mode.html). It *shoud* be fine since it's just the .py file in this repo packaged together with python itself and any required libraries but Windows Defender and other antivirus software might freak out. If you don't trust it just [manually install python](#Slightly-less-easy-setup)

# Easy Setup
1. Install [OculusKiller](https://github.com/LibreQuest/OculusKiller) 
2. Setup ADB on your PC. You can either do this manually or use something like SideQuest or [Meta Quest Developer Hub](https://developer.oculus.com/documentation/unity/ts-odh/). You don't need to do this if you already use one of those programs.
3. Connect your headset to your computer with a USB cable then start adb using whatever software you chose.
4. (Only required if using Air Link) Setup adb to connect over WiFi. If you're using SideQuest or Quest Developer Hub there's a button that sets it up for you. If you manually installed adb, do [this](https://gist.github.com/blixt/1e57de3739a669b8a58395ca07ec5ad0#connecting-quest-to-computer).
5. Download oculus-button-watcher.exe and launch it. You should see the serial number or IP address of your headset and when you press the oculus button it should say `Home Down` / `Home Up`
6. Now just connect to Link / Air Link. When SteamVR completely loads, try pressing the oculus button to see if the dashboard opens and closes.

# Slightly less easy setup
1. At the top of this repo, click Code then Download ZIP. Extract the contents of the zip file to a safe place like your desktop
2. Install python. You can find instructions for that [here.](https://www.digitalocean.com/community/tutorials/install-python-windows-10)
3. Open the folder you extracted from the zip file, click the address bar at the top, type cmd and press enter.
4. Type `python --version` and make sure you see an output similar to this: `Python 3.x.x`  If you get something else like command not found you didn't install python properly.
5. If the last step worked fine, type `pip install -r requirements.txt` and hit enter. It'll take a few seconds to install everything it needs.
6. If the last command finished with no errors, do steps 1-4 from the Easy Setup section.
7. In the terminal window, type `python oculus-button-watcher.py` and press enter. You should see the serial number or IP address of your headset and when you press the oculus button it should say `Home Down` / `Home Up`
8. Now just connect to Link / Air Link. When SteamVR completely loads, try pressing the oculus button to see if the dashboard opens and closes.

# Remapping the Menu button on the left controller
1. Install [OVR Advanced Settings](https://store.steampowered.com/app/1009850/OVR_Advanced_Settings/) if you don't have it installed.
2. Go into VR, open OVRAS, go to the SteamVR tab, enable system button binding then hit Restart SteamVR.
3. Open up the legacy binding UI, select VR Dashboard, Edit, System Actions then set the left controller binding to look like this:
![image](https://user-images.githubusercontent.com/24685455/222074073-e4f31565-8cbb-48fc-94a6-52b10a348d21.png)

You should now be able to bind the menu button to whatever you want.
