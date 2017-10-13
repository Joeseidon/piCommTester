import wx
import os

class ExamplePane(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self,parent)
        self.quote = wx.StaticText(self, label="Your quote :", pos=(20,30))

        self.logger = wx.TextCtrl(self, pos=(300,20), size=(200,300), style=wx.TE_MULTILINE | wx.TE_READONLY)

        #Button test
        self.button = wx.Button(self, label="Save", pos=(200,325))
        self.Bind(wx.EVT_BUTTON, self.OnClick, self.button)

        #Text Control test
        self.lblname = wx.StaticText(self, label="Your name :", pos=(20,60))
        self.editname = wx.TextCtrl(self, value="Enter your name here:", pos=(150,60), size=(140,-1))
        self.Bind(wx.EVT_TEXT, self.EvtText, self.editname)
        self.Bind(wx.EVT_CHAR, self.EvtChar, self.editname)


        #ComboBox test
        self.sampleList = ['friends', 'advertising', 'web search', 'yellow pages']
        self.lblhear = wx.StaticText(self, label="How did you hear from us ?", pos=(20,90))
        self.edithear = wx.ComboBox(self, pos=(180,90), size=(95, -1), choices = self.sampleList, style = wx.CB_DROPDOWN)
        self.Bind(wx.EVT_COMBOBOX, self.EvtComboBox, self.edithear)
        self.Bind(wx.EVT_TEXT, self.EvtText, self.edithear)


        #Checkbox test
        self.insure = wx.CheckBox(self, label="Do you want Insured Shipment ?", pos=(20,180))
        self.Bind(wx.EVT_CHECKBOX, self.EvtCheckBox, self.insure)

        #Radio Boxes test
        radioList = ['blue', 'red', 'yellow', 'orange', 'green', 'purple','navy']
        self.rb = wx.RadioBox(self, label="What color whould you like ?", pos=(20,210), choices=radioList, majorDimension=3, style = wx.RA_SPECIFY_COLS)
        self.Bind(wx.EVT_RADIOBOX, self.EvtRadioBox, self.rb)
        self.Bind(wx.EVT_RADIOBOX, self.EvtText, self.rb)

    def EvtRadioBox(self, event):
        self.logger.AppendText('EvtRadioBox: %d\n' %event.GetInt())
    def EvtComboBox(self, event):
        self.logger.AppendText('EvtComboBox: %s\n' %event.GetString())
    def OnClick(self, event):
        self.logger.AppendText("Clicked on object with Id %d\n" %event.getInt())
    def EvtText(self,event):
        self.logger.AppendText("EvtText: %s\n" %event.GetString())
    def EvtChar(self, event):
        self.logger.AppendText("EvtChar: %d\n" %event.GetKeyCode())
    def EvtCheckBox(self,event):
        self.logger.AppendText("EvtCheckBox: %d\n" %event.IsChecked())

if __name__ == '__main__':
    app = wx.App(False)
    frame = wx.Frame(None,title="Widget Test", size=(550,400))
    panel = ExamplePane(frame)
    frame.Show()
    app.MainLoop()
