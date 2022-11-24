from Repositories.AspirantRepository import AspirantRepository
from Repositories.PartyRepository import PartyRepository
from Models.Aspirant import Aspirant
from Models.Party import Party

class AspirantController():
    def __init__(self):
        self.RepositoryAspirant = AspirantRepository()
        self.RepositoryParty = PartyRepository()

    def index(self):
        return self.RepositoryAspirant.findAll()

    def create(self, infoAspirant):
        nuevoAspirant = Aspirant(infoAspirant)
        return self.RepositoryAspirant.save(nuevoAspirant)
    def show(self, id):
        elAspirant = Aspirant(self.RepositoryAspirant.findById(id))
        return elAspirant.__dict__

    def update(self, id, infoAspirant):
        elAspirant = Aspirant(self.RepositoryAspirant.findById(id))
        elAspirant.cedula = infoAspirant["cedula"]
        elAspirant.numero_resolucion = infoAspirant["numero_resolucion"]
        elAspirant.nombre = infoAspirant["nombre"]
        elAspirant.apellido = infoAspirant["apellido"]
        return self.RepositoryAspirant.save(elAspirant)

    def delete(self, id):
        return self.RepositoryAspirant.delete(id)
    
    def asignarAspirant(self, id, id_Party):
        AspirantActual = Aspirant(self.RepositoryAspirant.findById(id))
        PartyActual = Party(self.RepositoryParty.findById(id_Party))
        AspirantActual.Party = PartyActual
        return self.RepositoryAspirant.save(AspirantActual)

