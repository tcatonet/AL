import time
import threading
from Projet.Modele.File import File
#from Projet.Infrastructure.DatabaseSimulation import DatabaseSimulation
#from Projet.Infrastructure.DatabaseAccess import DatabaseAccess


class Worker(threading.Thread):
    def __init__(self, name, fileManager):
        threading.Thread.__init__(self)
        self.name = name
        self.bacthFileProcessing =  []
        self.fileManager = fileManager
        self.limitAction = 100

    def IWantToWork(self):

        if self.checkFileManager():

         #   try:
            self.bacthFileProcessing = self.fileManager.getFirstbatchFileStandBy()
          #  except:
            print("check true"+self.name)
            print(self.bacthFileProcessing)

            self.fileManager.setBlockAcess(False)

    def checkFileManager(self):

        if self.fileManager.getLenstbatchFileStandBy() > 0 and self.fileManager.getBlockAcess() == False:
            self.fileManager.setBlockAcess(True)
            return True
        else:
            return False

    def process(self):

        del self.bacthFileProcessing[0]
        time.sleep(1)


    def checkRemainingWork(self):
        if len(self.bacthFileProcessing) > 0:
            return True
        else :
            return False


    def run(self):
        while True:

            if self.checkRemainingWork():
                self.process()
            else:
                self.IWantToWork()

