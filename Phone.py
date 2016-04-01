# -*- coding: utf-8 -*-
import wx
from wx import Height, Width
from unittest import case

telefon=['RursusPhone',0,0,0]
class ExamplePanel(wx.Panel):
    def __init__(self, parent, title):
        wx.Panel.__init__(self, parent)
        self.SetInitialSize((500,400))
        self.quote = wx.StaticText(self, label="TELEFONKALKYLATORN :", pos=(20, 30))
        
        
        # A "-1" in the size parameter instructs wxWidgets to use the default size.
        # In this case, we select 200px width and the default height.
        #wx.Frame.__init__(self, parent, title=title, size=(200,-1))
        #self.control = wx.TextCtrl(self, style=wx.TE_MULTILINE)
        #self.CreateStatusBar() # A Statusbar in the bottom of the window

        # A multiline TextCtrl - This is here to show how the events work in this program, don't pay too much attention to it
        self.logger = wx.TextCtrl(self, pos=(10,230), size=(370,200), style=wx.TE_MULTILINE | wx.TE_READONLY)

        # A button
        self.button =wx.Button(self, label="Nästa", pos=(305, 199))
        self.Bind(wx.EVT_BUTTON, self.OnClick,self.button)

        # the edit control - one line version.
        self.lblname = wx.StaticText(self, label="Hur länge har du haft din telefon? :", pos=(20,60))
        self.editname = wx.TextCtrl(self, value="Svar i antal år", pos=(250, 55), size=(100,-1))
        self.Bind(wx.EVT_TEXT, self.EvtText, self.editname)
        self.Bind(wx.EVT_CHAR, self.EvtChar, self.editname)

        # the combobox Control
        self.sampleList = ['Samsung GS4', 'Samsung GS5', 'Samsung GS6', 'Samsung GS7' , 'iPhone 4', 'iPhone 4s', 'iPhone 5', 'iPhone 5s', 'iPhone 6', 'iPhone 6s', 'LG G2', 'LG G3', 'LG G4', 'LG G5', 'OnePlus 1', 'Oneplus 2']
        self.lblhear = wx.StaticText(self, label="Välj din telefon i listan", pos=(20, 90))
        self.edithear = wx.ComboBox(self, pos=(175, 85), size=(200, -1), choices=self.sampleList, style=wx.CB_DROPDOWN)
        self.Bind(wx.EVT_COMBOBOX, self.EvtComboBox, self.edithear)
        self.Bind(wx.EVT_TEXT, self.EvtMarke,self.edithear)

        # Checkbox
        self.insure = wx.CheckBox(self, label="Jag säljer inte stöldgods", pos=(5,120))
        self.Bind(wx.EVT_CHECKBOX, self.EvtCheckBox, self.insure)

        # Radio Boxes
        radioList = ['16Gb', '32Gb', '64Gb','128Gb']
        rb = wx.RadioBox(self, label="Hur mycket inbyggd lagringskapacitet i telefonen har du ?", pos=(10, 143), choices=radioList,  majorDimension=3,
                         style=wx.RA_SPECIFY_COLS)
        self.Bind(wx.EVT_RADIOBOX, self.EvtRadioBox, rb)

    def EvtRadioBox(self, event):
        val=event.GetInt()
        self.logger.AppendText('EvtRadioBox: %d\n' % val)
        gb=[16,32,64,128][val]
        self.logger.AppendText('  => gb: %d\n' % gb)
        telefon[1]=gb
    def EvtComboBox(self, event):
        self.logger.AppendText('EvtComboBox: %s\n' % event.GetString())
    def OnClick(self,event):
        self.logger.AppendText('Click on object with Id %d\n' % event.GetId())
    def EvtText(self, event):
        self.logger.AppendText('EvtMarke: %s\n' % event.GetString())
    def EvtMarke(self, event):
        marke=event.GetString()
        self.logger.AppendText('EvtMarke: %s\n' % event.GetString())
        telefon[0]=marke
    def EvtChar(self, event):
        self.logger.AppendText('EvtChar: %d\n' % event.GetKeyCode())
        event.Skip()
    def EvtCheckBox(self, event):
        self.logger.AppendText('EvtCheckBox: %d\n' % event.Checked())


app = wx.App(False)
frame = wx.Frame(None)
panel = ExamplePanel(frame,"gösta")
frame.Show()
app.MainLoop()
print telefon