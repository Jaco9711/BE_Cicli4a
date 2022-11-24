from Repositories.TableRepository import TableRepository
from Models.Table import Table

class TableController():
    
    def __init__(self):
        self.RepositoryTable = TableRepository()
    
    def index(self):
        return self.RepositoryTable.findAll()
    
    def create(self, infoTable):
        nuevaTable = Table(infoTable)
        return self.RepositoryTable.save(nuevaTable)
    
    def show(self, id):
        laTable = Table(self.RepositoryTable.findById(id))
        return laTable.__dict__
    
    def update(self, id, infoTable):
        TableActual = Table(self.RepositoryTable.findById(id))
        TableActual.numero = infoTable["numero"]
        TableActual.cantidad_inscritos = infoTable["cantidad_inscritos"]
        return self.RepositoryTable.save(TableActual)
    
    def delete(self, id):
        return self.RepositoryTable.delete(id)
