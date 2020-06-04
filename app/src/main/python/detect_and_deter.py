from queue import Queue
from threading import Event, Thread
from time import sleep

from ai import AI
from watson2 import WatsonRecognizer
from chatbot import get_response


class DetectAndDeter:
    def __init__(self):
        self.ai = AI.load_learner()
        self.watson = WatsonRecognizer()
        self.chatbot = get_response
        self.caller_speech = self.watson.transcription_q
        self.predictions = []
        self.responses = Queue()
        self.stop_event = Event()

        self.response_thread = Thread(target=self.generate_response)
        self.prediction_thread = Thread(target=self.generate_prediction)
        self.handler_thread = Thread(target=self.handler)

    def start(self):
        self.handler_thread.start()

    def stop(self):
        self.stop_event.set()

    def reset(self):
        self.predictions.clear()
        while not self.caller_speech.empty():
            self.caller_speech.get()

        while not self.responses.empty():
            self.responses.get()

    def close(self):
        self.watson.close()

    def generate_response(self):
        self.responses.put(self.chatbot(self.caller_speech.get(block=False)))

    def generate_prediction(self):
        self.predictions.append(self.ai.predict_text(self.caller_speech.get(False)))

    def handler(self):
        try:
            self.watson.start()
            while not self.stop_event.is_set():
                if not self.caller_speech.empty():
                    self.prediction_thread.start()
                    self.response_thread.start()

                    self.prediction_thread.join()
                    self.response_thread.join()
        finally:
            print("stopping")
            self.watson.stop()


if __name__ == '__main__':
    dad = DetectAndDeter()
    last_pred_size = 0
    try:

        dad.start()

        while True:
            sleep(.1)
            if len(dad.predictions) > last_pred_size:
                print(dad.predictions)
            if not dad.responses.empty():
                print(dad.responses.get())

    finally:
        dad.stop()


