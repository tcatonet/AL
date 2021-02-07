class RetrieveBacthFileQueryHandler:
    def __init__(self,managerFile):
        self.managerFile = managerFile

    def handle(self):
        retrieveBacthFileQuery = RetrieveBacthFileQuery(managerFile)
        return retrieveBacthFileQuery



