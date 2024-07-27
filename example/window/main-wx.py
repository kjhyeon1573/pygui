import wx

class MyFrame(wx.Frame):
    def __init__(self, *args, **kw):
        super(MyFrame, self).__init__(*args, **kw)

        panel = wx.Panel(self)

        label = wx.StaticText(panel, label="Hello, World!", pos=(150, 100))
        button = wx.Button(panel, label="Close", pos=(150, 150))

        button.Bind(wx.EVT_BUTTON, self.on_close)

    def on_close(self, event):
        self.Close()

class MyApp(wx.App):
    def OnInit(self):
        frame = MyFrame(None, title="My First Window", size=(400, 300))
        frame.Show(True)
        return True

if __name__ == "__main__":
    app = MyApp()
    app.MainLoop()