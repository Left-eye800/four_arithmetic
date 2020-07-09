"""0到10的除法

1。0到10的除法
2.10到0的除法
3.0到10的乱序除法

the statistics of this file:
lines(count)    understand_level(h/m/l)    classes(count)    functions(count)    fields(count)
000000000037    ----------------------l    00000000000000    0000000000000003    ~~~~~~~~~~~~~
"""

import random

__author__ = '与C同行'


def division_order(self, event):
    """ 1到10的正序除法 """
    self.panel.DestroyChildren()
    self.both_side_list = [[i*j, j] for i in range(1, 11) for j in range(1, 11)]
    self.asmd_layout(self.both_side_list[0], '÷')


def division_antiorder(self, event):
    """ 1到10的倒序除法 """
    self.panel.DestroyChildren()
    self.both_side_list = [[i*j, j] for i in range(1, 11) for j in range(1, 11)]
    self.both_side_list.reverse()
    self.asmd_layout(self.both_side_list[0], '÷')


def division_random(self, event):
    """ 1到10的乱序除法 """
    self.panel.DestroyChildren()
    self.both_side_list = [[i*j, j] for i in range(1, 11) for j in range(1, 11)]
    self.both_side_list = random.choices(self.both_side_list, k=len(self.both_side_list))
    self.asmd_layout(self.both_side_list[0], '÷')
