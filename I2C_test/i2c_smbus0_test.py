from smbus import SMBus
import time

def main():
	i2cbus = SMBus(0)
	i2caddress = 0x4C
	a=i2cbus.read_byte_data(i2caddress, 0x05)
	print(a)
	time.sleep(1)
if __name__ == "__main__":
    main()

