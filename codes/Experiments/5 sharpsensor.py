import spidev #spi library to control spi devices
import RPi.GPIO as GPIO  #To control Pi GPIO channels
from time import sleep # time library to include sleep function


spi=spidev.SpiDev()# Open SPI bus  to create spi object
spi.open(0,0)# opened in bus 0 device 0


# Function to read SPI data from MCP3008 chip
# Channel must be an integer 0-7
# Function name :getADC
# Input : channel
# Output : analog data converted to digital in 10 bit resolution
# Example call: getADC(channel)
def getADC(channel):
    if(channel>7) or (channel<0):
        return -1
    r=spi.xfer([1,(8+channel) << 4,0])
    adc_out=((r[1]&3) << 8) + r[2]
    voltage=(adc_out*3.3)/1024 #converted into voltage level for distance calculation 
    
    #distance calculation corresponding to the voltage level
    distance= 27.86*pow(voltage,-1.15)
    print("adc output:{0:4d} distance output:{1:}".format(adc_out,distance)) # for printing the values

# Loop for printing the corresponding values continuously 
while 1:
    getADC(0)
    print("---------------------------------------------------------")
    sleep(0.1)
