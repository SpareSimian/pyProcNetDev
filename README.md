**pyProcNetDev** is an APACHE licensed library written in Python designed to provide a simple and pythonic way to parse the _/proc/net/dev_ file on LINUX based systems.

Based on hazelnut by Martin Simon, a library for parsing /proc/meminfo. He did the heavy lifting. Any bugs are mine.

## Installation:

From source use

		$ python setup.py install

or install from PyPi

		$ pip install pyProcNetDev

## Documentation:

- Basic use:

```python
>>> from pyProcNetDev import ProcNetDev
>>> procNetDev = ProcNetDev()
>>> procNetDev

Inter-|   Receive                                                |  Transmit
 face |bytes    packets errs drop fifo frame compressed multicast|bytes    packets errs drop fifo colls carrier compressed
    lo: 26217676  125468    0    0    0     0          0         0 26217676  125468    0    0    0     0       0          0
  eth0: 9023440606 54510507 2197 2197    0     0          0   7239942 79739514172 73835543    0    0    0     0       0          0
  eth1: 77537968700 73231803    0    0    0     0          0         0 7362247385 43427153    0    0    0     0       0          0
 wlan0:       0       0    0    0    0     0          0         0        0       0    0    0    0     0       0          0
```

- Return output as dict:

```python
>>> procNetDev.dict()
{
 'lo': {'Receive': {'bytes': 29862036,
                    'compressed': 0,
                    'drop': 0,
                    'errs': 0,
                    'fifo': 0,
                    'frame': 0,
                    'multicast': 0,
                    'packets': 130960},
        'Transmit': {'bytes': 29862036,
                     'carrier': 0,
                     'colls': 0,
                     'compressed': 0,
                     'drop': 0,
                     'errs': 0,
                     'fifo': 0,
                     'packets': 130960}},
 # ...
}
```

- Search (is case insensitive):

```python
>>> procNetDev.search('.*eth')
['  eth0: 9026331702 54528520 2197 2197    0     0          0   7243285 '
 '79745499387 73851068    0    0    0     0       0          0\n',
 '  eth1: 77539038290 73238913    0    0    0     0          0         0 '
 '7363537535 43434382    0    0    0     0       0          0\n']
```

## License:

```
Copyright 2023 SpareSimian

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

   http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.

```
