#The below code is simple and works fine but has a big delay
'''
    import pywemo
    devices = pywemo.discover_devices()
    print(devices)
    #[<WeMo Insight "AC Insight">]
    
    devices[0].toggle()
    
    '''

#The address of the device can be found in the app as:
#More => Setting & About => Hardware Info => Select the device
#The change the addresses in the code below

import pywemo
address = "192.168.1.149"
address1 = "192.168.1.165"
port = pywemo.ouimeaux_device.probe_wemo(address)
port1 = pywemo.ouimeaux_device.probe_wemo(address1)
url = 'http://%s:%i/setup.xml' % (address, port)
url1 = 'http://%s:%i/setup.xml' % (address1, port1)
device = pywemo.discovery.device_from_description(url, None)
device1 = pywemo.discovery.device_from_description(url1, None)

while True:
    userInput = input("Press 1 to heat the water\nPress 2 to toggle the light\nPress 0 to quit\n")
    if(userInput == 1):
        device.toggle()
    if(userInput == 2):
        device1.toggle()
    if(userInput == 0):
        break

print(device)
#<WeMo Insight "AC Insight">
