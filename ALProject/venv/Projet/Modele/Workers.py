from Projet.Modele.Worker import Worker

class Workers:
    def __init__(self,fileManager):
        self.workers = []
        self.fileManager = fileManager

    def initWorker(self):
        self.workers = [Worker("W1",self.fileManager), Worker("W2",self.fileManager), Worker("W3",self.fileManager)]

        for worker in self.workers:
            worker.start()

        print("init")