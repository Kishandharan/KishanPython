from textual.app import App
from textual.widgets import *

class TextualApp(App):
    def compose(self):
        self.static1 =  Static("[red italic]Hello world[/red italic]")
        self.label1 = Label("[yellow italic]Boom[/yellow italic]")
        yield self.static1
        yield self.label1

    def on_mount(self):
       self.static1.background = "yellow" 
       self.label1.background = "red" 

TextualApp().run()
