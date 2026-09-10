from textual.app import App
from textual.widgets import *

class TextualApp(App):
    def compose(self):
        
        yield Static("Hello")

app = TextualApp()
app.run()
