from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer



my_bot = ChatBot(name='DetectAndDeter', read_only=True,
                 logic_adapters=['chatterbot.logic.MathematicalEvaluation',
                                 'chatterbot.logic.BestMatch'])
while True:
    print(my_bot.get_response(input("> ")))
# corpus_trainer = ChatterBotCorpusTrainer(my_bot)
# corpus_trainer.train('chatterbot.corpus.english')

