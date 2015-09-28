import sys
import time
import datetime

import AnswerLogger
import ErrorLogger
sys.path.insert(0, './Problems')

#TODO: Figure out how to import python modules dynamically.
import Problem1;
import Problem2;
import Problem4;
import Problem5;
import Problem6;
import Problem25;
import Problem48;


ProblemModules = [Problem1, Problem2, Problem4, Problem5, Problem6, Problem25]
textLogPath = "./AnswerLog.txt"
errorLogPath = "./ErrorLog.txt"


def GetProblem():
    print("Enter Problem #: ")
    input = sys.stdin.readline()
    return input.replace('\n', '')

def Solve():
    problem = GetProblem()
    try:

        textLog = AnswerLogger.AnswerLogger(textLogPath)
        errorLog = ErrorLogger.ErrorLogger(errorLogPath)
        for problemModule in ProblemModules:
            problemString = str(problemModule)
            if(problemString.find(problem) >= 0 or problem == '0'):
                start = time.clock()
                answer = problemModule.Solve()
                                
                end = time.clock()
                timeDelta = end - start
                timeVal = datetime.timedelta(seconds = timeDelta);
                textLog.AddAnswer(str(timeVal), problemString, answer)
                textLog.Save()
        

    except Exception as e:
        print(e)
        errorLog.AddError(e)

Solve()