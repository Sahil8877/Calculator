from kivy.clock import Clock
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from functools import partial

class boxlayout(BoxLayout):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.button()
        print("init")

    
    def button(self):
        print("in")
        button = Button(text="Long Press Me")
        self.add_widget(button)
        def on_press(self, touch):
            print("Pressed")
            if Clock.schedule_once(lambda dt: no_args_func(), 5) == True:
                print("Long Press Detected")
        
        def no_args_func():
            pass
        button.bind(on_touch_down=on_press)
    
    
class MainApp(App):
    def build(self):
        return boxlayout()

MainApp().run()
