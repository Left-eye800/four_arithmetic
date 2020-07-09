"""
加减乘除通用布局模板

the statistics of this file:
lines(count)    understand_level(h/m/l)    classes(count)    functions(count)    fields(count)
000000000124    ----------------------h    00000000000000    0000000000000001    ~~~~~~~~~~~~~
"""

import random

import wx

__author__ = '与C同行'


def asmd_layout(self, frist_double, operator):
    """ 加减乘除通用布局 """
    def get_current_numbers():
        first_number = int(self.label_first_number.GetLabelText())
        second_number = int(self.label_second_number.GetLabelText())
        return [first_number, second_number]

    def question_outcome_handle(event):
        bothside = get_current_numbers()
        if self.operator == '+':
            outcome_number = int(bothside[0]) + int(bothside[1])
        elif self.operator == '-':
            outcome_number = int(bothside[0]) - int(bothside[1])
        elif self.operator == '×':
            outcome_number = int(bothside[0]) * int(bothside[1])
        elif self.operator == '÷':
            outcome_number = int(bothside[0]) / int(bothside[1])
        else:
            pass
        outcome_number = int(outcome_number)
        self.label_outcome.SetLabelText(str(outcome_number))
        self.Layout()

    def previous_question_handle(event):
        bothside = get_current_numbers()
        current_index = self.both_side_list.index(bothside)
        if current_index == 1:
            self.button_previous.Hide()
        else:
            self.button_previous.Show()
        self.button_next.Show()
        previous_side_number = self.both_side_list[current_index - 1]
        self.label_first_number.SetLabelText(str(previous_side_number[0]))
        self.label_first_number.SetForegroundColour(random.choice(self.colors))
        self.label_operator.SetForegroundColour(random.choice(self.colors))
        self.label_second_number.SetLabelText(str(previous_side_number[1]))
        self.label_second_number.SetForegroundColour(random.choice(self.colors))
        self.label_equal.SetForegroundColour(random.choice(self.colors))
        self.label_outcome.SetLabelText('?')
        self.label_outcome.SetForegroundColour(random.choice(self.colors))
        self.Layout()

    def next_question_handle(event):
        bothside = get_current_numbers()
        current_index = self.both_side_list.index(bothside)
        if current_index == (len(self.both_side_list)-2):
            self.button_next.Hide()
        else:
            self.button_next.Show()
        self.button_previous.Show()
        next_side_number = self.both_side_list[current_index+1]
        self.label_first_number.SetLabelText(str(next_side_number[0]))
        self.label_first_number.SetForegroundColour(random.choice(self.colors))
        self.label_operator.SetForegroundColour(random.choice(self.colors))
        self.label_second_number.SetLabelText(str(next_side_number[1]))
        self.label_second_number.SetForegroundColour(random.choice(self.colors))
        self.label_equal.SetForegroundColour(random.choice(self.colors))
        self.label_outcome.SetLabelText('?')
        self.label_outcome.SetForegroundColour(random.choice(self.colors))
        self.Layout()

    self.button_outcome = wx.Button(self.panel, wx.ID_ANY, u"答案")
    self.button_previous = wx.Button(self.panel, wx.ID_ANY, u"←上一题")
    self.button_next = wx.Button(self.panel, wx.ID_ANY, u"下一题→")
    self.Bind(wx.EVT_BUTTON, question_outcome_handle, self.button_outcome)
    self.Bind(wx.EVT_BUTTON, previous_question_handle, self.button_previous)
    self.Bind(wx.EVT_BUTTON, next_question_handle, self.button_next)
    sizer_panel = wx.BoxSizer(wx.VERTICAL)
    sizer_body = wx.BoxSizer(wx.VERTICAL)
    sizer_navigation = wx.BoxSizer(wx.HORIZONTAL)
    sizer_show_labels = wx.BoxSizer(wx.HORIZONTAL)
    sizer_show_labels.Add((40, 20), 1, wx.ALIGN_CENTER, 0)
    self.label_first_number = wx.StaticText(self.panel, wx.ID_ANY, str(frist_double[0]), style=wx.ALIGN_CENTER)
    self.label_first_number.SetForegroundColour(random.choice(self.colors))
    self.label_first_number.SetFont(self.font)
    sizer_show_labels.Add(self.label_first_number, 0, wx.ALIGN_CENTER, 0)
    sizer_show_labels.Add((20, 40), 0, wx.ALIGN_CENTER, 0)
    self.label_operator = wx.StaticText(self.panel, wx.ID_ANY, operator, style=wx.ALIGN_CENTER)
    self.label_operator.SetForegroundColour(random.choice(self.colors))
    self.label_operator.SetFont(self.font)
    sizer_show_labels.Add(self.label_operator, 0, wx.ALIGN_CENTER, 0)
    sizer_show_labels.Add((20, 40), 0, wx.ALIGN_CENTER, 0)
    self.label_second_number = wx.StaticText(self.panel, wx.ID_ANY, str(frist_double[1]), style=wx.ALIGN_CENTER)
    self.label_second_number.SetForegroundColour(random.choice(self.colors))
    self.label_second_number.SetFont(self.font)
    sizer_show_labels.Add(self.label_second_number, 0, wx.ALIGN_CENTER, 0)
    sizer_show_labels.Add((20, 40), 0, wx.ALIGN_CENTER, 0)
    self.label_equal = wx.StaticText(self.panel, wx.ID_ANY, "=", style=wx.ALIGN_CENTER)
    self.label_equal.SetForegroundColour(random.choice(self.colors))
    self.label_equal.SetFont(self.font)
    sizer_show_labels.Add(self.label_equal, 0, wx.ALIGN_CENTER, 0)
    sizer_show_labels.Add((20, 40), 0, wx.ALIGN_CENTER, 0)
    self.operator = operator
    self.label_outcome = wx.StaticText(self.panel, wx.ID_ANY, '?', style=wx.ALIGN_CENTER)
    self.label_outcome.SetForegroundColour(random.choice(self.colors))
    self.label_outcome.SetFont(self.font)
    sizer_show_labels.Add(self.label_outcome, 0, wx.ALIGN_CENTER, 0)
    sizer_show_labels.Add((40, 20), 1, wx.ALIGN_CENTER, 0)
    sizer_body.Add(sizer_show_labels, 6, wx.EXPAND, 0)
    sizer_body.Add(self.button_outcome, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALIGN_RIGHT | wx.RIGHT, 100)
    sizer_navigation.Add((20, 20), 1, wx.ALIGN_CENTER, 0)
    sizer_navigation.Add(self.button_previous, 0, wx.ALIGN_CENTER | wx.ALL, 40)
    sizer_navigation.Add(self.button_next, 0, wx.ALIGN_CENTER | wx.RIGHT, 40)
    sizer_body.Add(sizer_navigation, 1, wx.EXPAND, 0)
    self.panel.SetSizer(sizer_body)
    sizer_panel.Add(self.panel, 1, wx.EXPAND, 0)
    self.SetSizer(sizer_panel)
    self.Layout()
    self.button_previous.Hide()
