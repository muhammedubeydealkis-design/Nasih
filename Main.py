import json
import threading
import urllib.request
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.clock import Clock

API_URL = "https://text.pollinations.ai/"

SYSTEM_INSTRUCTION = (
    "Sen 'Nasih' adında, kullanıcının en yakın dostu, samimi ve güvenilir bir yoldaşısın. "
    "İslami ilimlere vakıf, ahlaklı ve hikmetli öğütler veren, asla resmi olmayan, sıcak ve kucaklayıcı bir asistansın. "
    "Konuşurken asla soğuk olma; sanki can dostunla konuşuyormuş gibi samimi bir dil kullan. "
    "Dini ve ahlaki konuları Kur'an-ı Kerim ve sahih sünnet ışığında, yapıcı bir dille açıkla."
)

class NasihApp(App):
    def build(self):
        self.title = "Nasih - İslami Dostane Rehber"
        
        root = BoxLayout(orientation='vertical', padding=10, spacing=10)
        
        scroll = ScrollView(size_hint=(1, 0.82))
        
        self.chat_history = Label(
            text="[b]Nasih:[/b] Aleykümselam dostum! Hoş geldin, nasılsın?\n\n",
            markup=True,
            size_hint_y=None,
            halign='left',
            valign='top'
        )
        
        scroll.bind(width=lambda *x: setattr(self.chat_history, 'text_size', (scroll.width - 20, None)))
        self.chat_history.bind(texture_size=self.chat_history.setter('size'))
        
        scroll.add_widget(self.chat_history)
        root.add_widget(scroll)
        
        input_layout = BoxLayout(size_hint=(1, 0.15), spacing=5)
        
        self.text_input = TextInput(
            hint_text="Mesajını yaz dostum...",
            multiline=False
        )
        self.text_input.bind(on_text_validate=self.send_message)
        input_layout.add_widget(self.text_input)
        
        send_btn = Button(text="Gönder", size_hint_x=0.3, background_color=(0.1, 0.5, 0.3, 1))
        send_btn.bind(on_press=self.send_message)
        input_layout.add_widget(send_btn)
        
        root.add_widget(input_layout)
        
        self.messages = [{"role": "system", "content": SYSTEM_INSTRUCTION}]
        return root

    def send_message(self, instance):
        user_text = self.text_input.text.strip()
        if not user_text:
            return
        
        self.chat_history.text += f"[b]Sen:[/b] {user_text}\n\n"
        self.text_input.text = ""
        
        self.messages.append({"role": "user", "content": user_text})
        threading.Thread(target=self.fetch_ai_response).start()

    def fetch_ai_response(self):
        payload = {
            "messages": self.messages,
            "model": "openai",
            "json": False
        }
        try:
            data = json.dumps(payload).encode('utf-8')
            req = urllib.request.Request(
                API_URL, 
                data=data, 
                headers={'Content-Type': 'application/json'},
                method='POST'
            )
            with urllib.request.urlopen(req, timeout=20) as response:
                ai_response = response.read().decode('utf-8').strip()
                self.messages.append({"role": "assistant", "content": ai_response})
                Clock.schedule_once(lambda dt: self.update_chat(ai_response))
        except Exception as e:
            error_msg = f"Bağlantı hatası oldu dostum: {e}"
            Clock.schedule_once(lambda dt: self.update_chat(error_msg))

    def update_chat(self, text):
        self.chat_history.text += f"[b]Nasih:[/b] {text}\n\n"

if __name__ == '__main__':
    NasihApp().run()
      
