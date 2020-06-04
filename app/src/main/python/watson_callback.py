import sys
from queue import Queue

from ibm_watson.websocket import RecognizeCallback

import ai


class WatsonCallback(RecognizeCallback):
    def __init__(self, transcript_q: Queue = Queue(), prints=False):
        RecognizeCallback.__init__(self)
        self.last = ''
        self.transcript_q = transcript_q
        self.prints = prints
        self.ai = ai.AI.load_learner()

    def on_transcription(self, transcript):
        self.last = transcript[0]['transcript'].strip()
        self.transcript_q.put(self.last)  # Adds it twice because two different threads need it
        self.transcript_q.put(self.last)
        if self.prints:
            print("\r--> ", self.last, "-- ",  self.ai.predict_text(self.last))

    def on_connected(self):
        if self.prints:
            print('Connection was successful')

    def on_error(self, error):
        if self.prints:
            print(f'Error received: {error}')

    def on_inactivity_timeout(self, error):
        if self.prints:
            print(f'Inactivity timeout: {error}')

    def on_listening(self):
        if self.prints:
            print('Service is listening')

    def on_hypothesis(self, hypothesis):
        if self.prints:
            if hypothesis.strip() != self.last:
                print('\r', hypothesis, sep='', end='')
                sys.stdout.flush()

    def on_close(self):
        if self.prints:
            print("Connection closed")