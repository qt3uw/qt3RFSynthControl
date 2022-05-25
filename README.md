# Controller for Windfreak SynthHD v2 RF Generator

Helper code to control [Windfreak's SynthHD RF generator](https://windfreaktech.com/product/microwave-signal-generator-synthhd/).


## Installation

```
git clone https://github.com/gadamc/qt3rfsynthcontrol
cd qt3rfsynthcontrol
python -m pip install .
#python -m pip install -e . #-e flag facitlitates development
```

## Usage

### Determine the port


```python
import qt3rfsynthcontrol
qt3rfsynthcontrol.discover_devices()
```

Will return a list of ports and information about devices connected to those ports.
For example

```python
[['COM3',
  'Intel(R) Active Management Technology - SOL (COM3)',
  'PCI\\VEN_8086&DEV_43E3&SUBSYS_0A541028&REV_11\\3&11583659&1&B3'],
 ['COM5',
  'USB Serial Device (COM5)',
  'USB VID:PID=0483:A3E5 SER=206A36705430 LOCATION=1-2:x.0'],
 ['COM6',
  'USB Serial Device (COM6)',
  'USB VID:PID=04D8:000A SER= LOCATION=1-8:x.0'],
 ['COM7',
  'USB Serial Device (COM7)',
  'USB VID:PID=239A:8014 SER=3B0D07C25831555020312E341A3214FF LOCATION=1-6:x.0']]
```

It is certainly not obvious to which USB port the Windfreak is connected. However,
using the Windows Task Manager, as well as trial and error, should eventually
reveal the correct serial port to use.

### Connection to SynthHD

```python
my_pulser = qt3rfsynthcontrol.Pulser('COM5')
```

### Communication


### System Settings

Two methods exist to report on global and channel settings

##### Global Settings

```python
import pprint
pp = pprint.PrettyPrinter(indent=4)

pp.pprint(my_pulser.report_global_settings())
```

##### Channel Settings

```python
for channel in range(1,5):
    pp.pprint(f'channel {channel}')
    pp.pprint(my_pulser.report_channel_settings(channel))
```


### Debugging

If you hit an error, especially when trying to use the property-like calls,
the last string written to the Serial port is found in the
`.last_write_command` attribute of the pulser object.

```python
my_pulser.pulse1.width(25e-6)
print(my_pulser.last_write_command)
# ':PULSE1:WIDTH 2.5e-05'
```

Additionally, you can see the recent command history of the object (last 1000 commands)

```python
for command in my_pulser.command_history():
  print(command)
```

# LICENSE

[LICENCE](LICENSE)

##### Acknowledgments

The `Property` class of this code was taken from `easy-scpi`: https://github.com/bicarlsen/easy-scpi
and modified.
