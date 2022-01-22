# Renko

Renko chart creator.

[![Publish Python 🐍 distributions 📦 to PyPI and TestPyPI](https://github.com/aticio/renko/actions/workflows/publish-to-test-pypi.yml/badge.svg?branch=main)](https://github.com/aticio/renko/actions/workflows/publish-to-test-pypi.yml)

## Example Usage
```python
from renko import Renko

...

    # Create new renko instance. Give brick size and list of close prices as parameters
    rnk = Renko(1000, close)
    rnk.create_renko()

    print(rnk.bricks)
...

# The output will be like:
[
	{'type': 'first', 'open': 10336.87, 'close': 10336.87}
	{'type': 'up', 'open': 10336.87, 'close': 11084.87}
	{'type': 'up', 'open': 11084.87, 'close': 11832.87}
	{'type': 'up', 'open': 11832.87, 'close': 12580.87}
	{'type': 'up', 'open': 12580.87, 'close': 13328.87}
	{'type': 'up', 'open': 13328.87, 'close': 14076.87}
	{'type': 'up', 'open': 14076.87, 'close': 14824.87}
	{'type': 'up', 'open': 14824.87, 'close': 15572.87}
	{'type': 'up', 'open': 15572.87, 'close': 16320.87, 'low': 14818.3}
	{'type': 'up', 'open': 16320.87, 'close': 17068.87}
	{'type': 'up', 'open': 17068.87, 'close': 17816.87}
	{'type': 'up', 'open': 17816.87, 'close': 18564.87}
	{'type': 'up', 'open': 18564.87, 'close': 19312.87, 'low': 17139.52}
	{'type': 'up', 'open': 19312.87, 'close': 20060.87, 'low': 18036.53}
	{'type': 'up', 'open': 20060.87, 'close': 20808.87}
	{'type': 'up', 'open': 20808.87, 'close': 21556.87}
	{'type': 'up', 'open': 21556.87, 'close': 22304.87}
	{'type': 'up', 'open': 22304.87, 'close': 23052.87}
	{'type': 'up', 'open': 23052.87, 'close': 23800.87}
	{'type': 'up', 'open': 23800.87, 'close': 24548.87, 'low': 22719.71}
	{'type': 'up', 'open': 24548.87, 'close': 25296.87}
	{'type': 'up', 'open': 25296.87, 'close': 26044.87}

	...
	...
	...

	{'type': 'up', 'open': 48484.87, 'close': 49232.87}
	{'type': 'up', 'open': 49232.87, 'close': 49980.87}
	{'type': 'up', 'open': 49980.87, 'close': 50728.87}
	{'type': 'down', 'open': 49980.87, 'close': 49232.87, 'high': 50820.0}
	{'type': 'down', 'open': 49232.87, 'close': 48484.87}
	{'type': 'down', 'open': 48484.87, 'close': 47736.87}
	{'type': 'down', 'open': 47736.87, 'close': 46988.87}
	{'type': 'down', 'open': 46988.87, 'close': 46240.87}
	{'type': 'down', 'open': 46240.87, 'close': 45492.87, 'high': 47722.65}
	{'type': 'down', 'open': 45492.87, 'close': 44744.87}
	{'type': 'down', 'open': 44744.87, 'close': 43996.87}
	{'type': 'down', 'open': 43996.87, 'close': 43248.87}
	{'type': 'down', 'open': 43248.87, 'close': 42500.87}
	{'type': 'down', 'open': 42500.87, 'close': 41752.87}
	{'type': 'up', 'open': 42500.87, 'close': 43248.87, 'low': 41679.74}
	{'type': 'down', 'open': 42500.87, 'close': 41752.87}
	{'type': 'down', 'open': 41752.87, 'close': 41004.87}
	{'type': 'down', 'open': 41004.87, 'close': 40256.87}
	{'type': 'down', 'open': 40256.87, 'close': 39508.87}
	{'type': 'down', 'open': 39508.87, 'close': 38760.87}
	{'type': 'down', 'open': 38760.87, 'close': 38012.87}
	{'type': 'down', 'open': 38012.87, 'close': 37264.87}
	{'type': 'down', 'open': 37264.87, 'close': 36516.87}
	{'type': 'down', 'open': 36516.87, 'close': 35768.87}
	{'type': 'down', 'open': 35768.87, 'close': 35020.87}
]
```

```python
from renko import Renko

...

    # If you use it live in your strategies, pass the current price to check_new_price() function. 
    # If new price change is big enough to create a new birck or bricks, 
    # the bricks list will be updated accordingly.
    rnk = Renko(1000, close)
    rnk.create_renko()

    print(rnk.bricks)

...

    rnk.check_new_price(100000)

    print("Bricks after new price added-------------")
    print(rnk.bricks)

```

## Installation

Run the following to install:

```python
pip install renko
```