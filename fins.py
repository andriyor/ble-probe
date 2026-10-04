import asyncio
from bleak import BleakScanner

async def main():
    # use_bdaddr: real MAC instead of macOS per-host UUID (undocumented IOBluetooth API)
    found = await BleakScanner.discover(timeout=10, return_adv=True, cb={"use_bdaddr": True})
    for d, adv in sorted(found.values(), key=lambda x: -x[1].rssi):
        mfr = {f"0x{k:04X}": v.hex() for k, v in adv.manufacturer_data.items()}
        print(adv.rssi, d.address, d.name, adv.local_name, mfr, adv.service_uuids)

asyncio.run(main())
