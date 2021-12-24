from renko import Renko
import requests

BINANCE_URL = "https://api.binance.com/api/v3/klines"
SYMBOL = "BTCUSDT"
INTERVAL = "1h"
PARAMS = {"symbol": SYMBOL, "interval": INTERVAL}


def test_createrenko():
    response = requests.get(url=BINANCE_URL, params=PARAMS)
    data = response.json()
    close = [float(c[4]) for c in data]

    rnk = Renko(1000, close)
    rnk.create_renko()

    print(rnk.bricks)
