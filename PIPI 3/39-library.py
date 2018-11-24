#0752 225 542 
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button


class LoginScreen(GridLayout):
    def __init__(self, **kwargs):
        super(LoginScreen, self).__init__(**kwargs)
        self.cols = 2
        self.row_force_default = True
        self.row_default_height = 40
        self.add_widget(Label(
            text='User Name',
            size_hint_x=None,
            width=100))
        self.username = TextInput(multiline=False, password=False, width=200, size_hint_x=None)
        self.add_widget(self.username)
        self.add_widget(Label(
            text='password',
            size_hint_x=None,
            width=100
        ))
        self.password = TextInput(password=False, multiline=False, width=200, size_hint_x=None)
        self.add_widget(self.password)
        self.add_widget(Label(text='', size_hint_x=None, width=100))
        self.login_button = Button(text='Login', size_hint_x=None, width=100)
        self.add_widget(self.login_button)
        self.login_button.bind(on_press=self.button_pressed)

    def button_pressed(self, *args):
        # MODUL INDICATIV DE ACI
        # Mod indicativ timp perfect compus
        if self.username.text[0:2] == "am" or self.username.text[0:2] == "ai" or self.username.text [0:1] == "a" or self.username.text[0:3] == "ati" or self.username.text [0:2] == "au":
            my_label = Label(text=self.username.text + " este la modul indicativ timp perfect compus")
            self.add_widget(my_label)
    # Mod indicativ timp imperfect

        elif self.username.text[-2:] == "am" or self.username.text[-2:] == "ai" or self.username.text[-1:] == "a" or self.username.text[-3:] == "ati" or self.username.text[-2:] == "au":
            my_label2 = Label(text=self.username.text + " este la modul indicativ timp imperfect")
            self.add_widget(my_label2)
# Mod indicativ timp perfect simplu
        elif self.username.text[-2:] == "ui" or self.username.text[-3:] == "uși" or self.username.text[-1:] == "u" or self.username.text[-4:] == "urăm" or self.username.text[-5:] == "urăți" or self.username.text[-3:] == "ură":
            my_label3 = Label(text=self.username.text + " este la modul indicativ timp perfect simplu")
            self.add_widget(my_label3)
# Mod indicativ timp perfect simplu 2
        elif self.username.text[-3:] == "sei" or self.username.text[-4:] == """avem o buba aici""" "seşi" or self.username.text[-2:] == "se" or self.username.text[-5:] == "serăm" or self.username.text[-6:] == "serăţi" or self.username.text[-4:] == "seră":
            my_label4 = Label(text=self.username.text + " este la modul indicativ timp perfect simplu")
            self.add_widget(my_label4)
# Mod indicativ timp Mai Mult CA Perfectul
        elif self.username.text[-3:] == "sem" or self.username.text[-4:] == "seşi" or self.username.text[-2:] == "se" or self.username.text[-5:] == "serăm" or self.username.text[-6:] == "serăţi" or self.username.text[-4:] == "seră":
            my_label5 = Label(text=self.username.text + " este la modul indicativ timp mai mult ca  perfect.Formele de Plural la persoana I-II-a sunt la fel ca la perfect simplu")
            self.add_widget(my_label5)
# Viitor anterior
        elif self.username.text[0:6] == "voi fi" or self.username.text[0:6] == "vei fi" or self.username.text[
                                                                                   0:5] == "va fi" or self.username.text[
                                                                                                      0:6] == "vom fi" or self.username.text[
                                                                                                                          0:7] == "veți fi" or self.username.text[
                                                                                                                                               0:6] == "vor fi":
            my_label6 = Label(text=self.username.text + " este la modul indicativ timp viitor anterior")
            self.add_widget(my_label6)
# Viitor 1
        elif self.username.text[0:3] == "voi" or self.username.text[0:3] == "vei" or self.username.text[
                                                                             0:2] == "va" or self.username.text[
                                                                                             0:3] == "vom" or self.username.text[
                                                                                                              0:4] == "veți" or self.username.text[
                                                                                                                                0:3] == "vor":
            my_label7 = Label(text=self.username.text + " este la modul indicativ timp viitor")
            self.add_widget(my_label7)
# Viitor 2
        elif self.username.text[0:4] == "o să":
            my_label8 = Label(text=self.username.text + " este la modul indicativ timp viitor")
            self.add_widget(my_label8)
# Viitor popular
        elif self.username.text[0:2] == "oi" or self.username.text[0:2] == "îi" or self.username.text[
                                                                           0:1] == "o" or self.username.text[
                                                                                          0:2] == "om" or self.username.text[
                                                                                                          0:3] == "oți" or self.username.text[
                                                                                                                           0:2] == "or":
            my_label9 = Label(text=self.username.text + " este la modul indicativ timp viitor popular ")
            self.add_widget(my_label9)
# SI PANA ACI DE REVENIT!!!!!!
        elif self.username.text[0:1] == "să":
            my_label10 = Label(text=self.username.text + " este la modul conjunctiv timp prezent")
            self.add_widget(my_label10)


class Layout(BoxLayout):
    def __init__(self, **kwargs):
        super(Layout, self).__init__(**kwargs)
        self.cols = 1
        self.orientation = "vertical"

        self.add_widget(Label(text="Welcome", size_hint_x=None, width=100))
        self.add_widget(LoginScreen())


class MyApp(App):
    def build(self):
        return Layout()


if __name__ == '__main__':
    MyApp().run()
