# ble-probe

Small [bleak](https://github.com/hbldh/bleak) scripts for poking at Bluetooth LE devices. Used to check the Klipsch The Fives protocol for [KlipschControl](https://github.com/andriyor/KlipschControl): which characteristics exist and which bytes change when you turn the knob or use the remote.

## Run

Needs [uv](https://docs.astral.sh/uv/) (Python 3.9+).

```sh
uv run fins.py   # scan for 10 s and list nearby devices
uv run main.py   # connect to ADDRESS and print every notification
```

## fins.py

Scans for 10 seconds and prints each device, strongest signal first: RSSI, address, name, manufacturer data and advertised service UUIDs.

It passes `use_bdaddr` so macOS shows the real MAC address instead of its per-host UUID (an undocumented IOBluetooth option).

## main.py

Connects to `ADDRESS`, lists every characteristic that supports notifications, subscribes to all of them and prints each value as it changes. Turn the knob or press the remote and watch which characteristic and byte move.

Set `ADDRESS` at the top first. On macOS, bleak connects by the per-host UUID, not the MAC, so take it from a scan without `use_bdaddr` (remove that option in `fins.py` and run it again).

Klipsch characteristics end in `-0D18-442C-BABE-F85B5BAA6F11`; for example volume is `DA6D0FA2-0D18-442C-BABE-F85B5BAA6F11`.
