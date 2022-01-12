# flake8: noqa
import math

class Renko:
    """Renko initialization class
    """
    def __init__(self, brick_size, data):
        self.brick_size = brick_size
        self.data = data
        self.bricks = []
        self.wick = 0


    def create_renko(self):
        """Creating renko bricks using the provided price data
        """
        for i, d in enumerate(self.data):
            if i == 0:
                self.bricks.append({"type":"first", "open":float(d), "close":float(d), "low":float(d), "high":float(d)})
            else:
                if self.bricks[-1]["type"] == "up":
                    if d > self.bricks[-1]["close"]:
                        delta = d - self.bricks[-1]["close"]
                        fcount = math.floor(delta / self.brick_size)
                        if fcount != 0:
                            # low - high values will be added according to self.wick
                            self.add_bricks("up", fcount, self.brick_size)
                        else:
                            if delta > self.brick_size:
                                self.wick = self.bricks[-1]["close"] + self.brick_size
                    elif d < self.bricks[-1]["open"]:
                        delta = self.bricks[-1]["open"] - d
                        fcount = math.floor(delta / self.brick_size)
                        if fcount != 0:
                            self.add_bricks("down", fcount, self.brick_size) 
                elif self.bricks[-1]["type"] == "down":
                    if d < self.bricks[-1]["close"]:
                        delta = self.bricks[-1]["close"] - d
                        fcount = math.floor(delta / self.brick_size)
                        if fcount != 0:
                            self.add_bricks("down", fcount, self.brick_size)
                    elif d > self.bricks[-1]["open"]:
                        delta = d - self.bricks[-1]["open"]
                        fcount = math.floor(delta / self.brick_size)
                        if fcount != 0:
                            self.add_bricks("up", fcount, self.brick_size)
                else:
                    if d > self.bricks[-1]["close"]:
                        delta = d - self.bricks[-1]["close"]
                        fcount = math.floor(delta / self.brick_size)
                        if fcount != 0:
                            self.add_bricks("up", fcount, self.brick_size)
                    if d < self.bricks[-1]["close"]:
                        delta = self.bricks[-1]["close"] - d
                        fcount = math.floor(delta / self.brick_size)
                        if fcount != 0:
                            self.add_bricks("down", fcount, self.brick_size)


    def add_bricks(self, type, count, brick_size):
        """Adds brick(s) to the bricks list

        :param type: type of brick (up or down)
        :type type: string
        :param count: number of bricks to add
        :type count: int
        :param brick_size: brick size
        :type brick_size: float
        """
        for i in range(count):
            if type == "up":
                if self.bricks[-1]["type"] == "up" or self.bricks[-1]["type"] == "first":
                    self.bricks.append({"type": type, "open": self.bricks[-1]["close"], "close": self.bricks[-1]["close"] + brick_size})
                elif self.bricks[-1]["type"] == "down":
                    self.bricks.append({"type": type, "open": self.bricks[-1]["open"], "close": self.bricks[-1]["open"] + brick_size})
            elif type == "down":
                if self.bricks[-1]["type"] == "up":
                    self.bricks.append({"type": type, "open": self.bricks[-1]["open"], "close": self.bricks[-1]["open"] - brick_size})
                elif self.bricks[-1]["type"] == "down" or self.bricks[-1]["type"] == "first":
                    self.bricks.append({"type": type, "open": self.bricks[-1]["close"], "close": self.bricks[-1]["close"] - brick_size})


    def check_new_price(self, price):
        """Checks new price. If price change is big enough to create a new birck or bricks, the bricks list will be updated accordingly.

        :param price: last price value
        :type price: float
        """
        if self.bricks[-1]["type"] == "up":
            if price > self.bricks[-1]["close"]:
                delta = price - self.bricks[-1]["close"]
                fcount = math.floor(delta / self.brick_size)
                if fcount != 0:
                    self.add_bricks("up", fcount, self.brick_size)
            elif price < self.bricks[-1]["close"] - self.brick_size:
                delta = (self.bricks[-1]["close"] - self.brick_size) - price
                fcount = math.floor(delta / self.brick_size)
                if fcount != 0:
                    self.add_bricks("down", fcount, self.brick_size)
        elif self.bricks[-1]["type"] == "down":
            if price < self.bricks[-1]["close"]:
                delta = self.bricks[-1]["close"] - price
                fcount = math.floor(delta / self.brick_size)
                if fcount != 0:
                    self.add_bricks("down", fcount, self.brick_size)
            elif price > self.bricks[-1]["close"] + self.brick_size:
                delta = price - (self.bricks[-1]["close"] + self.brick_size)
                fcount = math.floor(delta / self.brick_size)
                if fcount != 0:
                    self.add_bricks("up", fcount, self.brick_size)
        else:
            if price > self.bricks[-1]["close"]:
                delta = price - self.bricks[-1]["close"]
                fcount = math.floor(delta / self.brick_size)
                if fcount != 0:
                    self.add_bricks("up", fcount, self.brick_size)
            if price < self.bricks[-1]["close"]:
                delta = self.bricks[-1]["close"] - price
                fcount = math.floor(delta / self.brick_size)
                if fcount != 0:
                    self.add_bricks("down", fcount, self.brick_size)


    def add_single_custom_brick(self, type, open, close):
        """Mainly used for adding the first brick in live strategies.

        :param type: type of brick, up or down
        :type type: string
        :param open: open price of the brick
        :type open: float
        :param close: close price of the brick
        :type close: float
        """
        self.bricks.append({"type": type, "open": open, "close": close})