import wpf

from System.Windows import Application, Window

class MyWindow(Window):
    def __init__(self):
        wpf.LoadComponent(self, 'winform_python_2.xaml')
        #self._button.Content = "My Button1"
        #self._button.Click += self.OnClickButton
        #self._textBox.Text = "My Text1"
        self.button = self.FindName('button')
        self.button.Click += self.OnClickButton
        self.textBox = self.FindName('textBox')
               
    #def get_button(self):
    #    return self._button

    #def set_button(self, value):
    #    self._button = value

    #button = property(get_button, set_button)    

    #def get_text(self):
    #    return self._textBox

    #def set_text(self, value):
    #    self._textBox = value

    #textBox = property(get_text, set_text)

    def OnClickButton(self, sender, args):
        self.textBox.Text = "clicked!"
    

if __name__ == '__main__':
    Application().Run(MyWindow())
