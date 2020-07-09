"""0到10的减法

1。0到10的减法
2.10到0的减法
3.0到10的乱序减法

the statistics of this file:
lines(count)    understand_level(h/m/l)    classes(count)    functions(count)    fields(count)
000000000037    ----------------------l    00000000000000    0000000000000003    ~~~~~~~~~~~~~
"""

import random

__author__ = '与C同行'


def subtract_order(self, event):
    """ 0到10的正序减法 """
    self.panel.DestroyChildren()
    self.both_side_list = [[i+j, j] for i in range(11) for j in range(11)]
    self.asmd_layout(self.both_side_list[0], '-')


def subtract_antiorder(self, event):
    """ 0到10的倒序减法 """
    self.panel.DestroyChildren()
    self.both_side_list = [[i+j, j] for i in range(11) for j in range(11)]
    self.both_side_list.reverse()
    self.asmd_layout(self.both_side_list[0], '-')


def subtract_random(self, event):
    """ 0到10的乱序减法 """
    self.panel.DestroyChildren()
    self.both_side_list = [[i+j, j] for i in range(11) for j in range(11)]
    self.both_side_list = random.choices(self.both_side_list, k=len(self.both_side_list))
    self.asmd_layout(self.both_side_list[0], '-')
