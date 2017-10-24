"""
you should catch all exceptions except NotImplementedError
"""


class BaseBot():
    def __init__(self):
        pass

    def answer(self, question):
        raise NotImplementedError


class SampleBot(BaseBot):
    def answer(self, question):
        return 'your answer: {}'.format(question)
