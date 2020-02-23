# Power DA/AD Breakout (PDAAD) HAT EEPROM image.

## Usage
1. create tools with `make`

	Tools available:

	  * `eepmake`: Parses EEPROM text file and creates binary .eep file

	  * `eepdump`: Dumps a binary .eep file as human readable text (for debug)

	  * `eepflash.sh`: Write or read .eep binary image to/from HAT EEPROM
2. Edit eeprom_setting.txt
3. run `./eepmake eeprom_settings.txt pdaad.eep` to create the eep binary

#### On the raspberry pi
1. Disable EEPROM write protection (GPIO25 -> low)
	```bash
		sudo bash
		#   Exports pin to userspace
		echo "25" > /sys/class/gpio/export                  

		# Sets pin 25 as an output
		echo "out" > /sys/class/gpio/gpio25/direction

		# Sets pin 25 to low
		echo "0" > /sys/class/gpio/gpio25/value
		exit
	```
2. Make sure you can talk to the EEPROM
	* enable i2c in `sudo raspi-config`, `/etc/modules` and `/boot/config.txt` (see https://developer-blog.net/raspberry-pi-i2c-aktivieren/)
	* install i2cdetec `sudo apt install i2c-tools`
	* check with `sudo i2cdetect -y 0` (should be at adress 50)
3. Flash eep file `sudo ./eepflash.sh -w -t=24c32 -f=pdaad.eep -d=0 -a=50`
4. Enable EEPROM write protection (GPIO25 -> low)
	```bash
		sudo bash
		# Sets pin 25 to high
		echo "1" > /sys/class/gpio/gpio25/value
		exit
	``` 

