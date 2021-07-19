import json
import time
from urllib.parse import urlencode


BASE_AIRTABLE_URL = 'https://airtable.com/embed/'


class AirtableForm:
    def __init__(self, form_id: str):
        self.form_id = form_id
        self.answers = []
        self.events = []
        self.add_event('init')
    
    def add_event(self, event: str) -> None:
        self.events.append({'event': event, 'ts': time.time()})

    def add_answer(self, answer: str) -> None:
        self.answers.append(answer)
        self.add_event('answer')
        
    def url(self) -> str:
        self.add_event('url generated')
        params = {f"prefill_q{i+1:d}": a for i, a in enumerate(self.answers)}
        params['events'] = json.dumps(self.events)
        url = f"{BASE_AIRTABLE_URL}{self.form_id}?{urlencode(params)}"
        return url
