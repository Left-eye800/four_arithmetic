"""
学习九九乘法表

the statistics of this file:
lines(count)    understand_level(h/m/l)    classes(count)    functions(count)    fields(count)
000000000141    ----------------------l    00000000000000    0000000000000002    ~~~~~~~~~~~~~
"""

import wx

__author__ = '与C同行'


def multiplication_table_layout(self, first_page):
    """ 九九乘法表布局 """
    def find_index():
        first_equation_str = self.label_4.GetLabelText()
        current_index = int(first_equation_str[0])
        return current_index

    def previous_handle(event):
        current_index = find_index() - 1
        if current_index == 1:
            self.button_previous.Hide()
        else:
            self.button_previous.Show()
        self.button_next.Show()
        previous_page = self.multiplication_table[current_index - 1]
        for i in range(9):
            self.labels[i].SetLabelText(previous_page[i])
        self.Layout()

    def next_handle(event):
        current_index = find_index() - 1
        if current_index == 7:
            self.button_next.Hide()
        else:
            self.button_next.Show()
        self.button_previous.Show()
        next_page = self.multiplication_table[current_index+1]
        for i in range(9):
            self.labels[i].SetLabelText(next_page[i])
        self.Layout()

    self.button_previous = wx.Button(self.panel, wx.ID_ANY, u"← 上一页")
    self.button_next = wx.Button(self.panel, wx.ID_ANY, u"下一页 →")
    self.Bind(wx.EVT_BUTTON, previous_handle, self.button_previous)
    self.Bind(wx.EVT_BUTTON, next_handle, self.button_next)
    sizer_panel = wx.BoxSizer(wx.HORIZONTAL)
    sizer_widgets = wx.BoxSizer(wx.VERTICAL)
    sizer_control = wx.BoxSizer(wx.HORIZONTAL)
    sizer_numbers = wx.BoxSizer(wx.VERTICAL)
    sizer_9 = wx.BoxSizer(wx.HORIZONTAL)
    sizer_8 = wx.BoxSizer(wx.HORIZONTAL)
    sizer_7 = wx.BoxSizer(wx.HORIZONTAL)
    sizer_6 = wx.BoxSizer(wx.HORIZONTAL)
    sizer_5 = wx.BoxSizer(wx.HORIZONTAL)
    sizer_4 = wx.BoxSizer(wx.HORIZONTAL)
    sizer_3 = wx.BoxSizer(wx.HORIZONTAL)
    sizer_2 = wx.BoxSizer(wx.HORIZONTAL)
    sizer_1 = wx.BoxSizer(wx.HORIZONTAL)
    sizer_1.Add((300, 20), 0, 0, 0)

    self.label_1 = wx.StaticText(self.panel, wx.ID_ANY, first_page[0])
    self.label_1.SetForegroundColour(wx.Colour(255, 0, 0))
    self.label_1.SetFont(wx.Font(30, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, 0, ""))
    sizer_1.Add(self.label_1, 0, wx.ALIGN_CENTER, 0)
    sizer_numbers.Add(sizer_1, 1, wx.EXPAND, 0)
    sizer_2.Add((300, 20), 0, 0, 0)
    self.label_2 = wx.StaticText(self.panel, wx.ID_ANY, first_page[1])
    self.label_2.SetForegroundColour(wx.Colour(255, 0, 0))
    self.label_2.SetFont(wx.Font(30, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, 0, ""))
    sizer_2.Add(self.label_2, 0, 0, 0)
    sizer_numbers.Add(sizer_2, 1, wx.EXPAND, 0)
    sizer_3.Add((300, 20), 0, 0, 0)
    self.label_3 = wx.StaticText(self.panel, wx.ID_ANY, first_page[2])
    self.label_3.SetForegroundColour(wx.Colour(255, 0, 0))
    self.label_3.SetFont(wx.Font(30, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, 0, ""))
    sizer_3.Add(self.label_3, 0, 0, 0)
    sizer_numbers.Add(sizer_3, 1, wx.EXPAND, 0)
    sizer_4.Add((300, 20), 0, 0, 0)
    self.label_4 = wx.StaticText(self.panel, wx.ID_ANY, first_page[3])
    self.label_4.SetForegroundColour(wx.Colour(255, 0, 0))
    self.label_4.SetFont(wx.Font(30, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, 0, ""))
    sizer_4.Add(self.label_4, 0, 0, 0)
    sizer_numbers.Add(sizer_4, 1, wx.EXPAND, 0)
    sizer_5.Add((300, 20), 0, 0, 0)
    self.label_5 = wx.StaticText(self.panel, wx.ID_ANY, first_page[4])
    self.label_5.SetForegroundColour(wx.Colour(255, 0, 0))
    self.label_5.SetFont(wx.Font(30, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, 0, ""))
    sizer_5.Add(self.label_5, 0, 0, 0)
    sizer_numbers.Add(sizer_5, 1, wx.EXPAND, 0)
    sizer_6.Add((300, 20), 0, 0, 0)
    self.label_6 = wx.StaticText(self.panel, wx.ID_ANY, first_page[5])
    self.label_6.SetForegroundColour(wx.Colour(255, 0, 0))
    self.label_6.SetFont(wx.Font(30, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, 0, ""))
    sizer_6.Add(self.label_6, 0, 0, 0)
    sizer_numbers.Add(sizer_6, 1, wx.EXPAND, 0)
    sizer_7.Add((300, 20), 0, 0, 0)
    self.label_7 = wx.StaticText(self.panel, wx.ID_ANY, first_page[6])
    self.label_7.SetForegroundColour(wx.Colour(255, 0, 0))
    self.label_7.SetFont(wx.Font(30, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, 0, ""))
    sizer_7.Add(self.label_7, 0, 0, 0)
    sizer_numbers.Add(sizer_7, 1, wx.EXPAND, 0)
    sizer_8.Add((300, 20), 0, 0, 0)
    self.label_8 = wx.StaticText(self.panel, wx.ID_ANY, first_page[7])
    self.label_8.SetForegroundColour(wx.Colour(255, 0, 0))
    self.label_8.SetFont(wx.Font(30, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, 0, ""))
    sizer_8.Add(self.label_8, 0, 0, 0)
    sizer_numbers.Add(sizer_8, 1, wx.EXPAND, 0)
    sizer_9.Add((300, 20), 0, 0, 0)
    self.label_9 = wx.StaticText(self.panel, wx.ID_ANY, first_page[8])
    self.label_9.SetForegroundColour(wx.Colour(255, 0, 0))
    self.label_9.SetFont(wx.Font(30, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, 0, ""))
    sizer_9.Add(self.label_9, 0, 0, 0)
    sizer_numbers.Add(sizer_9, 1, wx.EXPAND, 0)
    sizer_widgets.Add(sizer_numbers, 1, wx.ALIGN_CENTER | wx.EXPAND, 0)
    sizer_control.Add((20, 20), 1, wx.ALIGN_CENTER, 0)
    sizer_control.Add(self.button_previous, 0, wx.ALIGN_CENTER | wx.ALL, 40)
    sizer_control.Add(self.button_next, 0, wx.ALIGN_CENTER | wx.ALL, 40)
    sizer_widgets.Add(sizer_control, 0, wx.EXPAND, 0)
    self.panel.SetSizer(sizer_widgets)
    sizer_panel.Add(self.panel, 1, wx.EXPAND, 0)
    self.SetSizer(sizer_panel)
    self.Layout()
    self.button_previous.Hide()
    self.labels = [self.label_1, self.label_2, self.label_3, self.label_4, self.label_5,
                   self.label_6, self.label_7, self.label_8, self.label_9]


def multiplication_table_func(self, event):
    """ 打印九九乘法表 """
    self.panel.DestroyChildren()
    self.multiplication_table = []
    for i in range(1, 10):
        temp_list = []
        for j in range(1, 10):
            multiplication_outcome = i * j
            temp_list.append(str(i) + ' × ' + str(j) + ' = ' + str(multiplication_outcome))
        self.multiplication_table.append(temp_list)
    self.multiplication_table_layout(self.multiplication_table[0])
