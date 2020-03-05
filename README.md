# Power Digital/Analog - Analog/Digital Hat

## Compile the Analog ad5593r Kernel Driver
Analog devices provide a Linux/Raspbian Kernel driver
https://wiki.analog.com/resources/tools-software/linux-drivers/iio-dac/ad5593r

This driver is necessary for the PDAAD-Hat device tree. To compile it
the following steps are needed:
1. Download the Raspbian kernel source for the installed kernel
version.
    Use `rpi-source` https://github.com/notro/rpi-source/wiki
    ```shell script
   sudo apt-get install git bc bison flex libssl-dev libncurses5-dev
   sudo wget https://raw.githubusercontent.com/notro/rpi-source/master/rpi-source -O /usr/local/bin/rpi-source && sudo chmod +x /usr/local/bin/rpi-source && /usr/local/bin/rpi-source -q --tag-update
   rpi-source
    ```
   the kernel sources are installed in the `linux` subdirectory
2. Configure only the `ad5593r` module for compilation
    1. Set `export KERNEL=kernel7` environment variable
    2. Start with default configuration `make bcm2709_defconfig`
    3. Use `make menuconfig` and select 
    
        `Device Drivers > Industrial I/O > DAC > <M> AD5593r `
       
       for compilation
    4. Compile
        ```shell script
         make prepare
         make modules_prepare
         make SUBDIRS=scripts/mod
         make SUBDIRS=drivers/iio/dac modules
         sudo make SUBDIRS=drivers/iio/dac modules_install
        ``` 
    5. Use `sudo depmod` to update module index
    
3. Test installation with `iio_info` see https://wiki.analog.com/resources/tools-software/linux-drivers/iio-dac/ad5593r
