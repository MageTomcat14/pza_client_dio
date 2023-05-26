######################################################
#
#          SCRIPT USED TO TEST PICO FIRMWARE
#
######################################################




from pymodbus.client import ModbusSerialClient
from pymodbus.transaction import ModbusRtuFramer
import time
import logging

FORMAT = ('%(message)-15s')
logging.basicConfig(format=FORMAT)
log = logging.getLogger()
log.setLevel(logging.DEBUG)

master = ModbusSerialClient(framer=ModbusRtuFramer, port = '/dev/ttyACM0', stopbits=1, bytesize=8, parity='N', baudrate=115200)



# getting value of output in input test
addrW = 64  # apply offset of 64 to write and read coil
addrR = 65
print("\033[92m-------------------writing IO 0----------------------\033[0m")
testWrite = master.write_coil(address = 0, value = True, slave = 0x01) 
testWrite = master.write_coil(address = addrW, value = True, slave = 0x01)
print(testWrite.__dict__)

# print("\033[92m-------------------reading----------------------\033[0m")
# testReceive = master.read_discrete_inputs(address = 1, count = 1, slave = 0x01)
# print(testReceive.bits)



# # push button test
# testWrite = master.write_coil(address = 16, value = False, slave = 0x01) 
testReceive = master.read_discrete_inputs(address = 17,count = 1,slave = 0x01)
print(testReceive.bits)
