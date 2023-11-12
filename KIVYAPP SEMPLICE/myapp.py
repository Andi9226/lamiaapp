from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.core.window import Window
from kivy.uix.image import Image
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.network.urlrequest import UrlRequest


class TrovaTemperatura(App):
    def build(self):
        self.window = GridLayout()
        self.window.cols=1   #cols=colonna
        self.window.size_hint=(0.8,0.9)
        self.window.pos_hint={"center_x":0.5,"center_y":0.5}
        Window.size=(360,640)
        self.window.add_widget(Image(source="C:/Users/UTENTE/Desktop/_ef066e8c-b575-4815-b8e3-a0bf3799b3cf.jpg"))
        self.input_testo=TextInput(
            size_hint=(1,0.2),
            font_size="20sp",
            padding_y="12sp",
            halign="center")
        self.window.add_widget(self.input_testo)
        self.bottone=Button(
            text="Via",
            size_hint=(1,0.2),
            bold=True,          #bold=grassetto
            background_color="#0099ff" #blu
        )
        self.window.add_widget(self.bottone)
        self.bottone.bind(on_press=self.trova_temp)#premi il buttone e ti trova il tempo
        self.etichetta=Label(
            text="Cerca una città\n\n\n\n\n\n\n\nAndi",
            font_size="20sp",
            color="#ffcc00"# giallo
            )
        self.window.add_widget(self.etichetta)
        return self.window
    def trova_temp(self,instance):
        def edit_label(request,result):
            temp=result["main"]["temp"]
            self.etichetta.text=f"Oggi a {self.input_testo.text} ci sono {temp} gradi"
        link=f"https://api.openweathermap.org/data/2.5/weather?q={self.input_testo.text}&appid=31cc021853cd5b171ffdd51418b822d0&units=metric"
        UrlRequest(link,edit_label)

TrovaTemperatura().run()
