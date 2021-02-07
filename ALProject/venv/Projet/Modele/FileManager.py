from Projet.Modele.Worker import Worker
import threading
import time
import copy

class FileManager(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.batchFileStandBy = []
        self.limitAction=100
        self.blockAcess = False


    def getbatchFileStandBy(self):
        return self.batchFileStandBy

    def getFirstbatchFileStandBy(self):
        res = copy.copy(self.batchFileStandBy[0])
        del self.batchFileStandBy[0]
        return res


    def getLenstbatchFileStandBy(self):
        return len(self.batchFileStandBy)


    def getBlockAcess(self):
        return self.blockAcess

    def setBlockAcess(self ,val):
        self.blockAcess = val

    def run(self):
        while True:
           # print("batchFileStandBy")
            print(len(self.batchFileStandBy))
            time.sleep(0.5)

