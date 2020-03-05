from smbus import SMBus

b = SMBus(1)  # 1 indicates /dev/i2c-1

dev_addr1 = 0x10
dev_addr2 = 0x11

general_purpose_register = 0x03
dac_pin_config_register = 0x05
dac_out0_register = 0x10

# set I/O0 of dev 0 to dac output
b.write_word_data(dev_addr1, dac_pin_config_register, 0x0001)

# set I/O0 to 1000/4095 -> 0x3e8
b.write_word_data(dev_addr1, dac_out0_register, 0x83e8)

print("{:x}".format(b.read_word_data(dev_addr1, general_purpose_register)))
