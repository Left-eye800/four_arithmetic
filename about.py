""" 关于

功能简单介绍

the statistics of this file:
lines(count)    understand_level(h/m/l)    classes(count)    functions(count)    fields(count)
000000000037    ----------------------l    00000000000000    0000000000000002    ~~~~~~~~~~~~~
"""

import wx

__author__ = '与C同行'


def about_layout(self):
    self.text_ctrl_about = wx.TextCtrl(self.panel, wx.ID_ANY,
                                       u"儿童四则运算第一版\n"
                                       u"1.认识0到100；\n"
                                       u"2.学习10以内的加法；\n"
                                       u"3.学习10以内的减法；\n"
                                       u"4.学习10以内的乘法；\n"
                                       u"5.学习10以内的除法；\n"
                                       u"6.学习九九乘法表。",
                                       style=wx.TE_READONLY|wx.TE_MULTILINE)
    self.text_ctrl_about.SetFont(wx.Font(12, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, 0, ""))
    sizer_panel = wx.BoxSizer(wx.HORIZONTAL)
    sizer_about = wx.BoxSizer(wx.HORIZONTAL)
    sizer_about.Add(self.text_ctrl_about, 1, wx.ALL | wx.EXPAND, 0)
    self.panel.SetSizer(sizer_about)
    sizer_panel.Add(self.panel, 1, wx.EXPAND, 0)
    self.SetSizer(sizer_panel)
    self.Layout()


def about_handle(self, event):
    self.panel.DestroyChildren()
    self.about_layout()
