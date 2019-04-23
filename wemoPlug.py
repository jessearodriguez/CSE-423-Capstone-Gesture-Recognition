import pywemo

devices = pywemo.discover_devices()

#[<WeMo Insight "AC Insight">]

devices[0].toggle()
print(len(devices))

if not devices:
    print("no device found")