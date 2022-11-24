from Repositories.PartyRepository import PartyRepository
from Models.Party import Party

class PartyController():
    
    def __init__(self):
        self.RepositoryParty = PartyRepository()
    
    def index(self):
        return self.RepositoryParty.findAll()
    
    def create(self, infoParty):
        nuevoParty = Party(infoParty)
        return self.RepositoryParty.save(nuevoParty)
    
    def show(self, id):
        elParty = Party(self.RepositoryParty.findById(id))
        return elParty.__dict__
    
    def update(self, id, infoParty):
        PartyActual = Party(self.RepositoryParty.findById(id))
        PartyActual.nombre = infoParty["nombre"]
        PartyActual.lema = infoParty["lema"]
        return self.RepositoryParty.save(PartyActual)
    
    def delete(self, id):
        return self.RepositoryParty.delete(id)
