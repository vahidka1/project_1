import backend
import wx

app=wx.App()
frame=wx.Frame(parent=None,title='Dictionary')
panel=wx.Panel(frame)
sizer=wx.GridBagSizer()
def press_button(event):
    word = str(input_box.GetValue())
    mean = backend.search(word)
    result.SetLabel(str(mean))

#difine widget
input_label= wx.StaticText(panel,label='word: ' )
input_box=wx.TextCtrl(panel)
result_label = wx.StaticText(panel, label='mean: ')
result =  text = wx.TextCtrl(panel,size=(1080,250), style=wx.TE_READONLY | wx.TE_MULTILINE)
button = wx.Button(panel, label='search')
button.Bind(wx.EVT_BUTTON,press_button)

#difine layout
sizer.Add(input_label,(0,0))
sizer.Add(input_box,(0,1))
sizer.Add(result_label,(2,0))
sizer.Add(result,(2,1))
sizer.Add(button,(3,1))

panel.SetSizerAndFit(sizer)
frame.SetSizerAndFit(sizer)

frame.Show()
app.MainLoop()