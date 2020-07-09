""" 学习0到100的数字

1.从0到100开始学习
2.从100到0开始学习
3.0到100之间乱序学习

the statistics of this file:
lines(count)    understand_level(h/m/l)    classes(count)    functions(count)    fields(count)
000000000141    ----------------------m    00000000000000    0000000000000004    ~~~~~~~~~~~~~
"""

import random

import wx

__author__ = '与C同行'


def learn100_layout(self, first_str):
    """ 认识0到100数字的布局 """
    self.button_previous = wx.Button(self.panel, wx.ID_ANY, u"← 上一个")
    self.button_next = wx.Button(self.panel, wx.ID_ANY, u"下一个 →")
    sizer_panel = wx.BoxSizer(wx.HORIZONTAL)
    sizer_widgets = wx.BoxSizer(wx.VERTICAL)
    sizer_control = wx.BoxSizer(wx.HORIZONTAL)
    sizer_number = wx.BoxSizer(wx.HORIZONTAL)
    sizer_number.Add((20, 20), 1, wx.ALIGN_CENTER, 0)
    self.label_number = wx.StaticText(self.panel, wx.ID_ANY, first_str, style=wx.ALIGN_CENTER)
    self.label_number.SetForegroundColour(random.choice(self.colors))
    self.label_number.SetFont(self.font)
    sizer_number.Add(self.label_number, 0, wx.ALIGN_CENTER, 0)
    sizer_number.Add((20, 20), 1, wx.ALIGN_CENTER, 0)
    sizer_widgets.Add(sizer_number, 1, wx.ALIGN_CENTER | wx.EXPAND, 0)
    sizer_control.Add((20, 20), 1, wx.ALIGN_CENTER, 0)
    sizer_control.Add(self.button_previous, 0, wx.ALIGN_CENTER | wx.BOTTOM | wx.LEFT | wx.TOP, 40)
    sizer_control.Add(self.button_next, 0, wx.ALIGN_CENTER | wx.ALL, 40)
    sizer_widgets.Add(sizer_control, 0, wx.EXPAND, 0)
    self.panel.SetSizer(sizer_widgets)
    sizer_panel.Add(self.panel, 1, wx.EXPAND, 0)
    self.SetSizer(sizer_panel)
    self.Layout()
    self.button_previous.Hide()


def learn100_order_handle(self, event):
    """ 从0认识到100 """
    def previous_handle(event):
        text = self.label_number.GetLabelText()
        current_number = int(text)
        previous_number = current_number - 1
        self.button_next.Show()
        if previous_number == 0:
            self.button_previous.Hide()
        self.label_number.SetLabelText(str(previous_number))
        self.label_number.SetForegroundColour(random.choice(self.colors))

    def next_handle(event):
        text = self.label_number.GetLabelText()
        current_number = int(text)
        next_number = current_number + 1
        self.button_previous.Show()
        if next_number == 100:
            self.button_next.Hide()
        self.label_number.SetLabelText(str(next_number))
        self.label_number.SetForegroundColour(random.choice(self.colors))

    self.panel.DestroyChildren()
    self.learn100_layout('0')
    self.Bind(wx.EVT_BUTTON, previous_handle, self.button_previous)
    self.Bind(wx.EVT_BUTTON, next_handle, self.button_next)


def learn100_antiorder_handle(self, event):
    """ 从100认识到0 """
    def previous_handle(event):
        text = self.label_number.GetLabelText()
        current_number = int(text)
        previous_number = current_number + 1
        self.button_next.Show()
        if previous_number == 100:
            self.button_previous.Hide()
        self.label_number.SetLabelText(str(previous_number))
        self.label_number.SetForegroundColour(random.choice(self.colors))

    def next_handle(event):
        text = self.label_number.GetLabelText()
        current_number = int(text)
        next_number = current_number - 1
        self.button_previous.Show()
        if next_number == 0:
            self.button_next.Hide()
        self.label_number.SetLabelText(str(next_number))
        self.label_number.SetForegroundColour(random.choice(self.colors))

    self.panel.DestroyChildren()
    self.learn100_layout('100')
    self.Bind(wx.EVT_BUTTON, previous_handle, self.button_previous)
    self.Bind(wx.EVT_BUTTON, next_handle, self.button_next)


def learn100_random_handle(self, event):
    """ 随机认识0到100 """
    def previous_handle(event):
        text = self.label_number.GetLabelText()
        current_number = int(text)
        current_random_index = self.random_numbers_100.index(current_number)
        if current_random_index == 1:
            self.button_previous.Hide()
        else:
            self.button_previous.Show()
        previous_number = self.random_numbers_100[current_random_index-1]
        self.button_next.Show()
        self.label_number.SetLabelText(str(previous_number))
        self.label_number.SetForegroundColour(random.choice(self.colors))

    def next_handle(event):
        text = self.label_number.GetLabelText()
        current_number = int(text)
        if current_number == self.random_numbers_100[-1]:
            next_number = random.choice(self.numbers_100)
            self.numbers_100.remove(next_number)
            self.random_numbers_100.append(next_number)
        else:
            current_random_index = self.random_numbers_100.index(current_number)
            next_number = self.random_numbers_100[current_random_index+1]
        self.button_previous.Show()
        if (len(self.random_numbers_100) == 101 and
                next_number ==self.random_numbers_100[-1]):
            self.button_next.Hide()
        self.label_number.SetLabelText(str(next_number))
        self.label_number.SetForegroundColour(random.choice(self.colors))

    self.panel.DestroyChildren()
    self.numbers_100 = [i for i in range(101)]
    self.random_numbers_100 = []
    first_number = random.choice(self.numbers_100)
    self.numbers_100.remove(first_number)
    self.random_numbers_100.append(first_number)
    self.learn100_layout(str(first_number))
    self.Bind(wx.EVT_BUTTON, previous_handle, self.button_previous)
    self.Bind(wx.EVT_BUTTON, next_handle, self.button_next)
