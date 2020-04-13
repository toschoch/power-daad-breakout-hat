# Compile and install on RPi
1. Install sshfs `sudo apt install sshfs`
2. Make dir and mount this directory to that dir `mkdir power-daad-breakout-hat && sudo sshfs -o allow_other,default_permissions tobi@192.168.0.15:Projects/RamanInsight/PowerAnalogHAT/power-daad-breakout-hat /home/pi/power-daad-breakout-hat`
3. Use the device-tree-compile to compile the file go to `pi/home`
   `dtc -@ -I dts -O dtb -o pdaad.dtbo power-daad-breakout-hat/pdaadhat-device-tree/pdaad.dts`
4. copy to boot overlays `sudo mv pdaad.dtbo /boot/overlays/` (ignore warning)
5. edit `/boot/config.txt`
