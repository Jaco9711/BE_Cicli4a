from Repositories.ResultRepository import ResultRepository
from Repositories.TableRepository import TableRepository
from Repositories.AspirantRepository import AspirantRepository

from Models.Result import Result
from Models.Aspirant import Aspirant
from Models.Table import Table

class ResultController():
    def __init__(self):
        self.RepositoryResult = ResultRepository()
        self.RepositoryAspirant = AspirantRepository()
        self.RepositoryTable = TableRepository()

    def index(self): 
        return self.RepositoryResult.findAll()

    def create(self, infoResult, id_Table, id_Aspirant):
        nuevoResult = Result(infoResult)
        laTable = Table(self.RepositoryTable.findById(id_Table))
        elAspirant = Aspirant(self.RepositoryAspirant.findById(id_Aspirant))
        nuevoResult.Table = laTable
        nuevoResult.Aspirant = elAspirant
        return self.RepositoryResult.save(nuevoResult)

    def show(self, id):
        elResult = Result(self.RepositoryResult.findById(id))
        return elResult.__dict__

    def update(self, id, infoResult, id_Table, id_Aspirant):
        elResult = Result(self.RepositoryResult.findById(id))
        laTable = Table(self.RepositoryTable.findById(id_Table))
        elAspirant = Aspirant(self.RepositoryAspirant.findById(id_Aspirant))
        elResult.Table = laTable
        elResult.Aspirant = elAspirant
        return self.RepositoryResult.save(elResult)

    def delete(self, id):
        return self.RepositoryResult.delete(id)

    def getListarAspirantsTable(self, id_Table):
        return self.RepositoryResult.getListadoAspirantsInscritosTable(id_Table)

    def getListarTablesDeInscritoAspirant(self, id_Aspirant):
        return self.RepositoryResult.getListadoTablesAspirantInscrito(id_Aspirant)

    def getMayorCedula(self):
        return self.RepositoryResult.getNumeroCedulaMayorAspirant()