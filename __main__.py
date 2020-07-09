""" 儿童四则运算关于

1.10以内的加减乘除
2.认识0到100
3.认识九九乘法表

the statistics of this file:
lines(count)    understand_level(h/m/l)    classes(count)    functions(count)    fields(count)
000000000079    ----------------------h    00000000000002    0000000000000000    ~~~~~~~~~~~~~
"""

import wx

from base_window import BaseFrame
from konw_100 import learn100_layout, learn100_order_handle, learn100_antiorder_handle, learn100_random_handle
from asmd_layout import asmd_layout
from add_learn import add_order, add_antiorder, add_random
from subtract_learn import subtract_order, subtract_antiorder, subtract_random
from multiplication_learn import multiplication_order, multiplication_antiorder, multiplication_random
from division_learn import division_order, division_antiorder, division_random
from multiplication_table import multiplication_table_func, multiplication_table_layout
from about import about_layout, about_handle

__author__ = '与C同行'


class MainFrame(BaseFrame):
    colors = [wx.Colour(255, 0, 0),
              wx.Colour(255, 100, 0),
              wx.Colour(0, 255, 255),
              # wx.Colour(255, 255, 0),
              wx.Colour(255, 127, 0),
              wx.Colour(255, 0, 127),
              wx.Colour(176, 0, 255),
              ]


# 认识0到100
MainFrame.learn100_layout = learn100_layout
MainFrame.learn100_order_handle = learn100_order_handle
MainFrame.learn100_antiorder_handle = learn100_antiorder_handle
MainFrame.learn100_random_handle = learn100_random_handle
# 添加加减乘除的通用布局
MainFrame.asmd_layout = asmd_layout
# 0到10的加法
MainFrame.add_order_handle = add_order
MainFrame.add_antiorder_handle = add_antiorder
MainFrame.add_random_handle = add_random
# 0到10的减法
MainFrame.subtract_order_handle = subtract_order
MainFrame.subtract_antiorder_handle = subtract_antiorder
MainFrame.subtract_random_handle = subtract_random
# 0到10的乘法
MainFrame.multiplication_order_handle = multiplication_order
MainFrame.multiplication_antiorder_handle = multiplication_antiorder
MainFrame.multiplication_random_handle = multiplication_random
# 0到10的除法
MainFrame.division_order_handle = division_order
MainFrame.division_antiorder_handle = division_antiorder
MainFrame.division_random_handle = division_random
# 九九乘法表
MainFrame.multiplication_table_layout = multiplication_table_layout
MainFrame.multiplication_table_handle = multiplication_table_func
# 关于
MainFrame.about_layout = about_layout
MainFrame.about_handle = about_handle


class MainApp(wx.App):
    def OnInit(self):
        self.frame = MainFrame(None, wx.ID_ANY, "")
        self.SetTopWindow(self.frame)
        self.frame.Show()
        return True


if __name__ == '__main__':
    app = MainApp(0)
    app.MainLoop()
