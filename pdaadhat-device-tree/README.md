# Compile and install on RPi
1. Install sshfs `sudo apt install sshfs`
2. Make dir and mount this directory to that dir `mkdir power-daad-breakout-hat && sudo sshfs -o allow_other,default_permissions tobi@192.168.0.15:/home/Tobi/Projects/RamanInsight/PowerAnalogHAT/power-daad-breakout-hat /home/pi/power-daad-breakout-hat`
