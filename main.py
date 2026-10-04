import asyncio
from bleak import BleakClient

ADDRESS = "56C16398-53FC-C0E4-8746-F547ED01D422"

async def main():
    async with BleakClient(ADDRESS) as client:
        print("Connected:", client.is_connected)

        for service in client.services:
            for char in service.characteristics:
                if "notify" in char.properties:
                    # await client.start_notify(
                    #     char.uuid,
                    #     lambda sender, data: print(sender, data)
                    # )
                    print(f"Service: {service.uuid}, Char: {char.uuid}, Desc: {char.description}")
                    try:
                        await client.start_notify(char.uuid, lambda sender, data: print(sender, data))
                        await asyncio.sleep(0.1)  # small delay between subscriptions
                    except Exception as e:
                        print(f"Skipping {char.uuid}: {e}")

        print("Listening...")
        await asyncio.sleep(9999)

asyncio.run(main())

volume = 'DA6D0FA2-0d18-442c-babe-f85b5baa6f11'
# DA6D0FA2-0D18-442C-BABE-F85B5BAA6F11