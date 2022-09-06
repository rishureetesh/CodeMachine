import sys
import json
import logging
import uuid

PATH = "C:\\Workspace\\CodeMachine\\Leetcode\\template\\"

class UtilityTemplate():

    logging.basicConfig(
        filename=f'{PATH}graveyard.log',
        filemode='a',
        format='%(asctime)s | %(name)s | %(levelname)s | %(message)s',
        datefmt='%d-%m-%Y %H:%M:%S',
        level=logging.DEBUG
    )

    def __init__(self, QuestionID, QuestionName):
        self.inputList = []
        self.success = False
        self.QuestionID = QuestionID
        self.QuestionName = QuestionName
        self.TotalTime = None
        self.retries = 1
        self.Output = None
        self.Outcome = []

        #Logging Configuration
        self.logger = logging.getLogger(__name__)

        #File import
        self.input = open(f'{PATH}stockyard.txt', 'r')
        self.output = open(f'{PATH}dumpyard.json', 'w')
    
    def __del__(self):
        self.input.close()
        self.output.close()
        print("Object Deleted!!!")
    
    #Taking Input
    def stockyard(self, numberOfLines):
        internalList = []
        for index, line in enumerate(self.input.readlines()):
            internalList.append(line.strip())
            if (index+1) % numberOfLines == 0:
                self.inputList.append(internalList)
                internalList = []


    #Printing Output
    def dumpyard(self):
        self.output.write(json.dumps(
            {
                "Unique ID":uuid.uuid4().hex,
                "Question ID":self.QuestionID,
                "Question Name":self.QuestionName,
                "Input List": self.inputList,
                "Output List":self.Output,
                "Success":self.success,
                "Retries" : self.retries,
                "Total Time Taken":self.TotalTime
            }
        ))

    #Logger Implememtation
    def graveyard(self):
        self.logger.info(json.dumps(
            {
                "Unique ID":uuid.uuid4().hex,
                "Question ID":self.QuestionID,
                "Question Name":self.QuestionName,
                "Input List": self.inputList,
                "Output List":self.Output,
                "Success":self.success,
                "Retries" : self.retries,
                "Total Time Taken":self.TotalTime
            }
        ))

    #Stress Testing
    def showtime(self, firstOponent, secondOponent):
        self.actualResult, self.TotalTime = firstOponent()
        self.expectedResult = secondOponent()
        if self.actualResult == self.expectedResult:
            self.Outcome += "Passed"
        else:
            self.Outcome += "Failed"
        self.graveyard()