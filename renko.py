# flake8: noqa
import math
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
import numpy as np

class Renko:
    """Renko initialization class
    """
    def __init__(self, brick_size, data):
        self.brick_size = brick_size
        self.data = data
        self.bricks = []
        self.low_wick = 0
        self.high_wick = 0


    def create_renko(self):
        """Creating renko bricks using the provided price data
        """
        for i, d in enumerate(self.data):
            if i == 0:
                if len(self.bricks) == 0:
                    self.bricks.append({"type":"first", "open":float(d), "close":float(d)})
            else:
                if self.bricks[-1]["type"] == "up":
                    if d > self.bricks[-1]["close"]:
                        delta = d - self.bricks[-1]["close"]
                        fcount = math.floor(delta / self.brick_size)
                        if fcount != 0:
                            if self.low_wick == 0:
                                self.add_bricks("up", fcount, self.brick_size)
                            else:
                                self.add_bricks("up", fcount, self.brick_size, self.low_wick)
                            self.low_wick = 0
                            self.high_wick = 0
                        else:
                            if d > self.high_wick:
                                self.high_wick = d
                    elif d < self.bricks[-1]["open"]:
                        delta = self.bricks[-1]["open"] - d
                        fcount = math.floor(delta / self.brick_size)
                        if fcount != 0:
                            if self.high_wick == 0:
                                self.add_bricks("down", fcount, self.brick_size)
                            else:
                                self.add_bricks("down", fcount, self.brick_size, self.high_wick)
                            self.high_wick = 0
                            self.low_wick = 0
                        else:
                            if self.low_wick == 0 or d < self.low_wick:
                                self.low_wick = d

                elif self.bricks[-1]["type"] == "down":
                    if d < self.bricks[-1]["close"]:
                        delta = self.bricks[-1]["close"] - d
                        fcount = math.floor(delta / self.brick_size)
                        if fcount != 0:
                            if self.high_wick == 0:
                                self.add_bricks("down", fcount, self.brick_size)
                            else:
                                self.add_bricks("down", fcount, self.brick_size, self.high_wick)
                            self.high_wick = 0
                            self.low_wick = 0
                        else:
                            if self.low_wick == 0 or d < self.low_wick:
                                self.low_wick = d
                    elif d > self.bricks[-1]["open"]:
                        delta = d - self.bricks[-1]["open"]
                        fcount = math.floor(delta / self.brick_size)
                        if fcount != 0:
                            if self.low_wick == 0:
                                self.add_bricks("up", fcount, self.brick_size)
                            else:
                                self.add_bricks("up", fcount, self.brick_size, self.low_wick)
                            self.low_wick = 0
                            self.high_wick = 0
                        else:
                            if d > self.high_wick:
                                self.high_wick = d
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


    def add_bricks(self, type, count, brick_size, wick=0):
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
                    if wick == 0:
                        self.bricks.append({"type": type, "open": self.bricks[-1]["close"], "close": (self.bricks[-1]["close"] + brick_size)})
                    else:
                        if i == 0:
                            self.bricks.append({"type": type, "open": self.bricks[-1]["close"], "close": (self.bricks[-1]["close"] + brick_size), "low": wick})
                        else:
                            self.bricks.append({"type": type, "open": self.bricks[-1]["close"], "close": (self.bricks[-1]["close"] + brick_size)})
                elif self.bricks[-1]["type"] == "down":
                    if wick == 0:
                        self.bricks.append({"type": type, "open": self.bricks[-1]["open"], "close": (self.bricks[-1]["open"] + brick_size)})
                    else:
                        if i == 0:
                            self.bricks.append({"type": type, "open": self.bricks[-1]["open"], "close": (self.bricks[-1]["open"] + brick_size), "low": wick})
                        else:
                            self.bricks.append({"type": type, "open": self.bricks[-1]["open"], "close": (self.bricks[-1]["open"] + brick_size)})
            elif type == "down":
                if self.bricks[-1]["type"] == "up":
                    if wick == 0:
                        self.bricks.append({"type": type, "open": self.bricks[-1]["open"], "close": (self.bricks[-1]["open"] - brick_size)})
                    else:
                        if i == 0:
                            self.bricks.append({"type": type, "open": self.bricks[-1]["open"], "close": (self.bricks[-1]["open"] - brick_size), "high": wick})
                        else:
                            self.bricks.append({"type": type, "open": self.bricks[-1]["open"], "close": (self.bricks[-1]["open"] - brick_size)})
                elif self.bricks[-1]["type"] == "down" or self.bricks[-1]["type"] == "first":
                    if wick == 0:
                        self.bricks.append({"type": type, "open": self.bricks[-1]["close"], "close": (self.bricks[-1]["close"] - brick_size)})
                    else:
                        if i == 0:
                            self.bricks.append({"type": type, "open": self.bricks[-1]["close"], "close": (self.bricks[-1]["close"] - brick_size), "high": wick})
                        else:
                            self.bricks.append({"type": type, "open": self.bricks[-1]["close"], "close": (self.bricks[-1]["close"] - brick_size)})


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


    def draw_chart(self):
        brick_width = self.brick_size / 2
        y_max = 0
        fig, ax = plt.subplots()

        count = 1
        for b in self.bricks:
            y = 0
            color = ""
            if b["type"] == "up":
                y = b["open"]
                color = "green"
            elif b["type"] == "down":
                y = b["close"]
                color = "red"
            else:
                color = "gray"
                y = b["close"]

            if y > y_max:
                y_max = y

            r = Rectangle((count * brick_width, y), brick_width, self.brick_size)
            r.set_color(color)

            ax.add_patch(r)
            count = count + 1

        ax.set_xlim(0, count * brick_width)
        ax.set_ylim(0, y_max + (y_max * 0.1))
        ax.set_axisbelow(True)
        ax.get_xaxis().set_visible(False)

        ticks = np.arange(0, y_max + (y_max * 0.1), self.brick_size)
        plt.yticks(ticks)
        plt.grid(linestyle='--', color="#ccd8c0")
        plt.show()