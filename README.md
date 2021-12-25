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
	{'type': 'first', 'open': 53041.32, 'close': 53041.32},
	{'type': 'down', 'open': 53041.32, 'close': 52041.32},
	{'type': 'down', 'open': 52041.32, 'close': 51041.32}, 
	{'type': 'down', 'open': 51041.32, 'close': 50041.32}, 
	{'type': 'down', 'open': 50041.32, 'close': 49041.32}, 
	{'type': 'down', 'open': 49041.32, 'close': 48041.32}, 
	{'type': 'down', 'open': 48041.32, 'close': 47041.32}, 
	{'type': 'up', 'open': 48041.32, 'close': 49041.32}, 
	{'type': 'up', 'open': 49041.32, 'close': 50041.32}, 
	{'type': 'up', 'open': 50041.32, 'close': 51041.32}, 
	{'type': 'down', 'open': 50041.32, 'close': 49041.32}, 
	{'type': 'down', 'open': 49041.32, 'close': 48041.32},
	{'type': 'up', 'open': 49041.32, 'close': 50041.32}, 
	{'type': 'down', 'open': 49041.32, 'close': 48041.32}, 
	{'type': 'down', 'open': 48041.32, 'close': 47041.32}, 
	{'type': 'up', 'open': 48041.32, 'close': 49041.32}, 
	{'type': 'down', 'open': 48041.32, 'close': 47041.32}, 
	{'type': 'down', 'open': 47041.32, 'close': 46041.32}, 
	{'type': 'up', 'open': 47041.32, 'close': 48041.32}, 
	{'type': 'up', 'open': 48041.32, 'close': 49041.32}, 
	{'type': 'up', 'open': 49041.32, 'close': 50041.32}, 
	{'type': 'up', 'open': 50041.32, 'close': 51041.32}
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