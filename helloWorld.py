import wx
import os

class MainWindow(wx.Frame):
    def __init__(self, parent, title):
        self.dirname=''
        wx.Frame.__init__(self, parent, title=title, size=(200,-1))
        self.control = wx.TextCtrl(self, style=wx.TE_MULTILINE)
        self.CreateStatusBar()  #A Statusbar in the bottom of the window

        #Setting up the menu
        filemenu = wx.Menu()
        menuOpen = filemenu.Append(wx.ID_OPEN, "&Open", "Open a file to edit")
        menuAbout = filemenu.Append(wx.ID_ABOUT, "&About","Information about this program")
        menuExit = filemenu.Append(wx.ID_EXIT,"E&xit","Terminate the program")

        #Create the menu bar
        menuBar = wx.MenuBar()
        menuBar.Append(filemenu, "&File")
        self.SetMenuBar(menuBar)

        self.Bind(wx.EVT_MENU, self.OnAbout, menuAbout)
        self.Bind(wx.EVT_MENU, self.OnExit, menuExit)
        self.Bind(wx.EVT_MENU, self.OnOpen, menuOpen)

        self.sizer2 = wx.BoxSizer(wx.HORIZONTAL)
        self.buttons = []
        for i in range(0,6):
            self.buttons.append(wx.Button(self, -1, "Button &"+str(i)))
            self.sizer2.Add(self.buttons[i], 1, wx.EXPAND)
        for btn in self.buttons:
            btn.Bind(wx.EVT_BUTTON, self.OnClick)

        #Sizers set layout options
        self.sizer = wx.BoxSizer(wx.VERTICAL)
        self.sizer.Add(self.control, 1, wx.EXPAND)
        self.sizer.Add(self.sizer2, 0, wx.EXPAND)

        self.SetSizer(self.sizer)
        self.SetAutoLayout(1)
        self.sizer.Fit(self)
        self.Show(True)

    def OnClick(self, event):
        btn = event.GetEventObject().GetLabel()
        print "Label of pressed button = ", btn
        dlq = wx.MessageDialog(self, "Label of pressed button = " + btn, "Button Click", wx.OK)
        dlq.ShowModal()
        dlg.Destroy() #finally destroy it when finished

    def OnAbout(self, event):
        dlq = wx.MessageDialog(self, "A small text editor", "About Sample Editor", wx.OK)
        dlq.ShowModal()
        dlg.Destroy() #finally destroy it when finished

    def OnExit(self, event):
        self.Close(True)

    def OnOpen(self,e):
        print("Should be open")
        self.dirname = ''
        dlg = wx.FileDialog(self, "Choose a file", self.dirname, "", "*.*", wx.FD_OPEN)
        if dlg.ShowModal() == wx.ID_OK:
            self.filename = dlg.GetFilename()
            self.dirname = dlg.GetDirectory()
            f = open(os.path.join(self.dirname, self.filename), 'r')
            self.control.SetValue(f.read())
            f.close()
        dlg.Destroy()

if __name__ == '__main__':
    print("Started")
    app = wx.App(False)
    print("App created")
    frame = MainWindow(None, title="Sample editor")
    app.MainLoop()
