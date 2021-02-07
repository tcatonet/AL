from Projet.Modele.FileManager import FileManager
class CreateBacthFileCommandHandler:
    def __init__(self, FileManager):
        self.FileManager = FileManager

    def addBacthFiletoFileManager(self, bacthFileToSend):
        self.FileManager.batchFileStandBy.append(bacthFileToSend.BatchFileStandBy)
