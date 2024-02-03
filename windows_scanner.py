import usb.core
import usb.util

# Find the RFID reader device
device = usb.core.find(idVendor="1A86", idProduct="DD01")

if device is None:
    raise ValueError('Device not found')

# On Windows, you might not need to detach the kernel driver. If you do, use device.detach_kernel_driver(0) as shown in the Mac example.

# Set the active configuration
device.set_configuration()

# Assuming the first endpoint is our target
endpoint = device[0][(0,0)][0]

# Attempt to read data from the device
try:
    data = device.read(endpoint.bEndpointAddress, endpoint.wMaxPacketSize, timeout=1000)
    print('Data read from the device:', data)
except usb.core.USBError as e:
    print("Could not read data: %s" % str(e))
