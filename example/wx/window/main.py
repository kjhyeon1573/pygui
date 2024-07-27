import wx

# Create the application object
app = wx.App(False)

# Create the main window
frame = wx.Frame(None, wx.ID_ANY, "My First Window", size=(400, 300))

# Create a panel in the frame
panel = wx.Panel(frame, wx.ID_ANY)

# Add a label
label = wx.StaticText(panel, label="Hello, World!", pos=(150, 100))

# Add a button to close the window
button = wx.Button(panel, label="Close", pos=(150, 150))
button.Bind(wx.EVT_BUTTON, lambda event: frame.Close())

# Show the window
frame.Show(True)

# Run the application
app.MainLoop()