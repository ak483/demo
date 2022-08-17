# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Jun 17 2015)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc


###########################################################################
## Class MyFrame1
###########################################################################

class MyFrame1(wx.Frame):

    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=wx.EmptyString, pos=wx.DefaultPosition,
                          size=wx.Size(284, 299), style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

        self.SetSizeHintsSz(wx.DefaultSize, wx.DefaultSize)
        self.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_WINDOW))
        self.SetTitle('Pywinauto')
        bSizer1 = wx.BoxSizer(wx.VERTICAL)

        bSizer2 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_staticText1 = wx.StaticText(self, wx.ID_ANY, u"姓名", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText1.Wrap(-1)
        self.m_staticText1.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_WINDOWTEXT))

        bSizer2.Add(self.m_staticText1, 0, wx.ALIGN_CENTER_HORIZONTAL | wx.ALL, 5)

        self.m_textCtrl1 = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer2.Add(self.m_textCtrl1, 0, wx.ALIGN_CENTER_HORIZONTAL | wx.ALL, 5)

        bSizer1.Add(bSizer2, 1, wx.ALIGN_CENTER_HORIZONTAL | wx.EXPAND, 5)

        bSizer3 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_staticText2 = wx.StaticText(self, wx.ID_ANY, u"性别", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText2.Wrap(-1)
        self.m_staticText2.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_WINDOWTEXT))

        bSizer3.Add(self.m_staticText2, 0, wx.ALIGN_CENTER_HORIZONTAL | wx.ALL, 5)

        self.m_radioBtn1 = wx.RadioButton(self, wx.ID_ANY, u"男", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer3.Add(self.m_radioBtn1, 0, wx.ALL, 5)

        self.m_radioBtn2 = wx.RadioButton(self, wx.ID_ANY, u"女", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer3.Add(self.m_radioBtn2, 0, wx.ALL, 5)

        bSizer1.Add(bSizer3, 1, wx.ALIGN_CENTER_HORIZONTAL | wx.EXPAND, 5)

        bSizer4 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_staticText3 = wx.StaticText(self, wx.ID_ANY, u"所在省份", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText3.Wrap(-1)
        self.m_staticText3.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_WINDOWTEXT))

        bSizer4.Add(self.m_staticText3, 0, wx.ALIGN_CENTER_HORIZONTAL | wx.ALL, 5)

        m_choice1Choices = [u"广东省", u"湖北省", u"湖南省", u"浙江省"]
        self.m_choice1 = wx.Choice(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_choice1Choices, 0)
        self.m_choice1.SetSelection(2)
        bSizer4.Add(self.m_choice1, 0, wx.ALIGN_CENTER_HORIZONTAL | wx.ALL, 5)

        bSizer1.Add(bSizer4, 1, wx.ALIGN_CENTER_HORIZONTAL | wx.EXPAND, 5)

        bSizer5 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_staticText4 = wx.StaticText(self, wx.ID_ANY, u"所在城市", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText4.Wrap(-1)
        self.m_staticText4.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_WINDOWTEXT))

        bSizer5.Add(self.m_staticText4, 0, wx.ALIGN_CENTER_HORIZONTAL | wx.ALL, 5)

        m_comboBox1Choices = [u"广州市", u"武汉市", u"杭州市", u"衡阳市", u"佛山市"]
        self.m_comboBox1 = wx.ComboBox(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize,
                                       m_comboBox1Choices, 0)
        self.m_comboBox1.SetSelection(0)
        bSizer5.Add(self.m_comboBox1, 0, wx.ALL, 5)

        bSizer1.Add(bSizer5, 1, wx.ALIGN_CENTER_HORIZONTAL | wx.EXPAND, 5)

        bSizer6 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_staticText5 = wx.StaticText(self, wx.ID_ANY, u"注册须知", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText5.Wrap(-1)
        self.m_staticText5.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_WINDOWTEXT))

        bSizer6.Add(self.m_staticText5, 0, wx.ALIGN_CENTER_HORIZONTAL | wx.ALL, 5)

        self.m_checkBox1 = wx.CheckBox(self, wx.ID_ANY, u"我已阅读有关事项", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_checkBox1.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_WINDOWTEXT))

        bSizer6.Add(self.m_checkBox1, 0, wx.ALIGN_CENTER_HORIZONTAL | wx.ALL, 5)

        bSizer1.Add(bSizer6, 1, wx.ALIGN_CENTER_HORIZONTAL | wx.EXPAND, 5)

        bSizer7 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_button1 = wx.Button(self, wx.ID_ANY, u"注册", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer7.Add(self.m_button1, 0, wx.ALIGN_CENTER_HORIZONTAL | wx.ALL, 5)
        self.m_button1.Bind(event=wx.EVT_BUTTON, handler=self.printBtn)

        self.m_button2 = wx.Button(self, wx.ID_ANY, u"取消", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_button2.Enable(False)
        bSizer7.Add(self.m_button2, 0, wx.ALIGN_CENTER_HORIZONTAL | wx.ALL, 5)

        bSizer1.Add(bSizer7, 1, wx.ALIGN_CENTER_HORIZONTAL | wx.EXPAND, 5)

        self.SetSizer(bSizer1)
        self.Layout()

        self.Centre(wx.BOTH)

    def __del__(self):
        pass

    def printBtn(self, event):
        dlg = wx.MessageDialog(None, "你已成功注册！", "注册成功", wx.YES_NO | wx.ICON_QUESTION)
        if dlg.ShowModal() == wx.ID_YES:
            pass
        dlg.Destroy()

if __name__ == '__main__':
    app = wx.App()
    frame = MyFrame1(None)
    frame.Show()
    app.MainLoop()