from Projet.Application.BacthFile.CreateBacthFileCommand import CreateBacthFileCommand
from Projet.Application.BacthFile.CreateBacthFileCommandHandler import CreateBacthFileCommandHandler
from Projet.Modele.FileManager import FileManager
from Projet.Modele.Workers import Workers
#from Projet.Infrastructure.DatabaseSimulation import DatabaseSimulation
#from Projet.Infrastructure.DatabaseAccess import DatabaseAccess



class APIfileManager:
    def __init__(self):
        self.fileManager = FileManager()


    def addBacthFile(self, listFile):
        bacthFileToSend = CreateBacthFileCommand(listFile)
        commandHandler = CreateBacthFileCommandHandler(self.fileManager)
        commandHandler.addBacthFiletoFileManager(bacthFileToSend)


    def init(self):
#        databaseSimulation = DatabaseSimulation()
       # databaseAccess = DatabaseAccess(databaseSimulation.TABLE_MESSAGE,databaseSimulation.TABLE_INFO)
        self.fileManager = FileManager()
        workers = Workers( self.fileManager)
        workers.initWorker()


