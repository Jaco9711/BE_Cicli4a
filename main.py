from flask import Flask, request, Response
from flask import jsonify
from flask_cors import CORS

from Controllers.PartyController import PartyController
from Controllers.AspirantController import AspirantController
from Controllers.TableController import TableController
from Controllers.ResultController import ResultController
 
app = Flask(__name__)
cors = CORS(app)

##############################
##     VARIABLES GLOBALES   ##
##############################
MyControllerParty = PartyController()
MyControllerAspirant = AspirantController()
MyControllerTable = TableController()
MyControllerResult = ResultController()

####################################
##    PROBAR EL SERVICIO          ##
####################################
@app.route("/", methods=["GET"])
def test():
    json = {}
    json["message"] = "Server running ..."
    return jsonify(json)

#####################################
##      ENDPOINT Parties          ##
#####################################
@app.route("/Parties", methods=["GET"])
def getParties():
    json = MyControllerParty.index()
    return jsonify(json)

@app.route("/Parties", methods=["POST"])
def crearParty():
    data = request.get_json()
    json = MyControllerParty.create(data)
    return jsonify(json)

@app.route("/Parties/<string:id>", methods=["GET"])
def getParty(id):
    json = MyControllerParty.show(id)
    return jsonify(json)

@app.route("/Parties/<string:id>", methods=["PUT"])
def modificarParty(id):
    data = request.get_json()
    json = MyControllerParty.update(id, data)
    return jsonify(json)

@app.route("/Parties/<string:id>", methods=["DELETE"])
def eliMynarParty(id):
    json = MyControllerParty.delete(id)
    return jsonify(json)

#####################################
##      ENDPOINT Aspirants        ##
#####################################
@app.route("/Aspirants", methods = ["GET"])
def getAspirants():
    json = MyControllerAspirant.index()
    return jsonify(json)

@app.route("/Aspirants", methods =["POST"])
def crearAspirant():
    data = request.get_json()
    json = MyControllerAspirant.create(data)
    return jsonify(json)

@app.route("/Aspirants/<string:id_Aspirant>", methods = ["GET"])
def getAspirant(id_Aspirant):
    json = MyControllerAspirant.show(id_Aspirant)
    return jsonify(json)

@app.route("/Aspirants/<string:id_Aspirant>", methods = ["PUT"])
def modificarAspirant(id_Aspirant):
    data = request.get_json()
    json = MyControllerAspirant.update(id_Aspirant, data)
    return jsonify(json)

@app.route("/Aspirants/<string:id_Aspirant>", methods = ["DELETE"])
def eliMynarAspirant(id_Aspirant):
    json = MyControllerAspirant.delete(id_Aspirant)
    return jsonify(json)

@app.route("/Aspirants/<string:id_Aspirant>/Party/<string:id_Party>", methods=["PUT"])
def asignarPartyAspirant(id_Aspirant, id_Party):
    json = MyControllerAspirant.asignarAspirant(id_Aspirant, id_Party)
    return jsonify(json)

#####################################
##           ENDPOINT Tables        ##
#####################################

@app.route("/Tables", methods=["GET"])
def getTables():
    json = MyControllerTable.index()
    return jsonify(json)

@app.route("/Tables", methods=["POST"])
def crearTable():
    data = request.get_json()
    json = MyControllerTable.create(data)
    return jsonify(json)

@app.route("/Tables/<string:id>", methods=["GET"])
def getTable(id):
    json = MyControllerTable.show(id)
    return jsonify(json)

@app.route("/Tables/<string:id>", methods=["PUT"])
def modificarTable(id):
    data = request.get_json()
    json = MyControllerTable.update(id, data)
    return jsonify(json)

@app.route("/Tables/<string:id>", methods=["DELETE"])
def eliMynarTable(id):
    json = MyControllerTable.delete(id)
    return jsonify(json)

#####################################
##       ENDPOINT Result        ##
#####################################
#Obtener todos los Results
@app.route("/Results", methods = ["GET"])
def getResults():
    json = MyControllerResult.index()
    return jsonify(json)


#Añadir un Result a una Table
@app.route("/Results/Table/<string:id_Table>/Aspirant/<string:id_Aspirant>", methods =["POST"])
def crearResult(id_Table, id_Aspirant):
    data = request.get_json()
    json = MyControllerResult.create(data, id_Table, id_Aspirant)
    return jsonify(json)


#Obtener Result especifico
@app.route("/Results/<string:id>", methods=["GET"])
def getResult(id):
    json = MyControllerResult.show(id)
    return jsonify(json)

#Modificar un Result
@app.route("/Results/<string:id_Result>/Table/<string:id_Table>/Aspirant/<string:id_Aspirant>", methods=["PUT"])
def modificarResult(id_Result, id_Table, id_Aspirant):
    data={}
    json = MyControllerResult.update(id_Result, data, id_Table, id_Aspirant)
    return jsonify(json)

#EliMynar Result
@app.route("/Results/<string:id>", methods=["DELETE"])
def borrarResult(id):
    json = MyControllerResult.delete(id)
    return jsonify(json)

#Buscar los Aspirants votados en una Table
@app.route("/Results/Table/<string:id_Table>", methods=["GET"])
def inscritosTable(id_Table):
    json = MyControllerResult.getListarAspirantsTable(id_Table)
    return jsonify(json)

#Buscar el Aspirant en las Tables
@app.route("/Results/Tables/<string:id_Aspirant>", methods=["GET"])
def inscritoEnTables(id_Aspirant):
    json = MyControllerResult.getListarTablesDeInscritoAspirant(id_Aspirant)
    return jsonify(json)
def getMaxDocument():
    json = MyControllerResult.getMayorCedula()
    return jsonify(json)

if __name__ == "__main__":
    app.run(debug=False, port=9000)