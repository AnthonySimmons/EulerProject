import sys

class AnswerLogger(object):
    """description of class"""
    _filepath = ''
    _answers = []


    def __init__(self, filepath):
        self._filepath = filepath

    def Save(self):
        file = open(self._filepath, 'w')
        file.writelines(self._answers)

    def AddAnswer(self, time, problem, answer):
        self._answers.append(str(time) + ", " + str(problem) + ", " + str(answer) + "\n")