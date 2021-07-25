import base64
import json
import time
from urllib.parse import urlencode


class AirtableForm:
    def __init__(self, form_id: str, redirect_url: str):
        self.form_id = form_id
        self.redirect_url = redirect_url
        self.answers = {}
        self.events = []
        self.add_event('init')
    
    def add_event(self, event: str) -> None:
        self.events.append({'event': event, 'ts': time.time()})

    def add_answer(self, question: str, answer: str) -> None:
        self.answers[question] = answer
        self.add_event(f"answered {question}")
        
    def url(self) -> str:
        self.add_event('url generated')
        data = json.dumps({
            'form_id': self.form_id,
            'answers': self.answers, 
            'events': self.events})
        params = {'data': base64.b64encode(data.encode()).decode()}
        url = f"{self.redirect_url}?{urlencode(params)}"
        return url
