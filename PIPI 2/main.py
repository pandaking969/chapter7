from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import NumericProperty

from kivy.clock import Clock

class RootWidget(BoxLayout):
    counter = NumericProperty(0)

    def on_counter(self, a, b):
        print("degismis")

    def startCounter(self):
        Clock.schedule_interval(self.saniyeGuncelle, 1)
        return "Started"

    def pauseCounter(self):
        Clock.unschedule(self.saniyeGuncelle)
        return "Paused"

    def resetCounter(self):
        self.saniyeSifirla()
        return "Stopped"

    def saniyeGuncelle(self, dt):
        print(self.counter)
        self.counter += 1

    def saniyeSifirla(self):
        self.counter = 0


class etiketApp(App):
    def build(self):
        return RootWidget()


if __name__ == "__main__":
    etiketApp().run()

