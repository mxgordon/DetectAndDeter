import warnings

from fastai.text import load_learner, RNNLearner

from timer import Timer

# model = load_learner('models', )

timer = Timer()

warnings.filterwarnings('ignore')


class AI(RNNLearner):
    @staticmethod
    def load_learner(path='models', file='finalv1.model') -> "AI":
        nlp_model: RNNLearner = load_learner(path=path, file=file)
        nlp_model.__class__ = AI
        return nlp_model

    def predict_text(self, text: str, replace: bool = True):
        if replace:
            text.replace(" %HESITATION", "")
        return self.predict(text)[0]


# if __name__ == '__main__':
#     while True:
#         user_input = input("> ")
#         timer.reset()
#         prediction = predict_text(user_input)
#         time_seconds = timer.get()
#         print(prediction, end=' ')
#         print(time_seconds, "s", sep="")
