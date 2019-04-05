import pywemo
devices = pywemo.discover_devices()
print(devices)
#[<WeMo Insight "AC Insight">]

devices[0].toggle()