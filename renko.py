# flake8: noqa
import math

class Renko:
    """Renko initialization class
    """
    def __init__(self, brick_size, data):
        self.brick_size = brick_size
        self.data = data
        self.bricks = []


    def create_renko(self):
        for i, d in enumerate(self.data):
            if i == 0:
                self.bricks.append({"type":"first", "open":float(d), "close":float(d)})
            else:
                if self.bricks[-1]["type"] == "up":
                    if d > self.bricks[-1]["close"]:
                        delta = d - self.bricks[-1]["close"]
                        fcount = math.floor(delta / self.brick_size)
                        if fcount != 0:
                            self.add_bricks("up", fcount, self.brick_size)
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