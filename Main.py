from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class NasihApp(App):
    def build(self):
        self.title = "Nasih AI"
        
        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        
        self.chat_history = Label(
            text="Nasih AI Asistanına Hoş Geldiniz!\nSorunuzu aşağıya yazın...",
            halign='left',
            valign='top',
            size_hint_y=0.7
        )
        self.chat_history.bind(size=self.chat_history.setter('text_size'))
        
        self.user_input = TextInput(
            text='',
            hint_text='Buraya yazın...',
            size_hint_y=0.15,
            multiline=False
        )
        
        submit_btn = Button(
            text='Gönder',
            size_hint_y=0.15,
            background_color=(0.1, 0.5, 0.8, 1)
        )
        submit_btn.bind(on_press=self.send_message)
        
        layout.add_widget(self.chat_history)
        layout.add_widget(self.user_input)
        layout.add_widget(submit_btn)
        
        return layout

    def send_message(self, instance):
        text = self.user_input.text.strip()
        if text:
            self.chat_history.text = f"\nSiz: {text}"
            self.user_input.text = ""

if __name__ == '__main__':
    NasihApp().run()
    
