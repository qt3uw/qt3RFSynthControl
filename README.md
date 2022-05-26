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
rf_synth = qt3rfsynthcontrol.Pulser('COM5')
```

### Hardware Info

```python
rf_synth.hw_info()
```

### Current Signal Status

```python
rf_synth.current_status()
```

### Set Fixed Frequency

```python
channel_A = 0
channel_B = 1
rf_synth.set_channel_fixed_output(channel_A, power = -5.0, frequency = 2870e6)
```

### Set Up For Frequency Scan

Frequency scan can either be triggered externally (using the Quantum Composer
  Sapphire pulser, or other), or can run independent of any external control.

```python
channel_A = 0
channel_B = 1
rf_synth.set_frequency_sweep(channel_A, power = -5.0, frequency_low = 2820e6,
                            frequency_high = 2920e6, n_steps = 101,
                            trigger_mode = 'single frequency step',
                            frequency_sample_time = 0.100)
```

See the function's documentation for further details

```python
help(rf_synth.set_frequency_sweep)
```

### Turn RF ON/OFF

The RF generation can be turned on and off with

```python
channel_A = 0
channel_B = 1
rf_synth.rf_on(channel_A)
rf_sythh.rf_off(channel_A)
```

# LICENSE

[LICENCE](LICENSE)
