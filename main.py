import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
import webview

kivy.require('1.11.1')


class WebBrowserApp(App):
    def build(self):
        layout = BoxLayout(orientation="vertical")
        webview.create_window("Web Browser", "https://www.google.com", width=800, height=600)
        return layout

if __name__ == "__main__":
    WebBrowserApp().run()
