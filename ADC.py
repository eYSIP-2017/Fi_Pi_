import spidev
from time import sleep
spi=spidev.SpiDev()
spi.open(0,0)
def getAdc(channel):
	if ((channel>8) or (channel<0)):
		return -1
	r=spi.xfer([1,(8+channel)<<4,0])
	adcout=((r[1]&3)<<8)+r[2]
	print ("ADC output: {0:4d}".format(adcout))
	sleep(0.1)
while 1:
	getAdc(0)
