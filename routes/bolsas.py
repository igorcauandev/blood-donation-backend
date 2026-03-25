from flask import jsonify, request
import dados


def rota_bolsas(app):

    # BOLSAS DE SANGUE

    @app.post("/bolsas")
    def criar_bolsa():

        bolsa = request.json

        if not bolsa:
            return jsonify({"erro": "JSON inválido"}), 400

        with open("bolsa.json", "a") as arquivo:
            arquivo.write(str(bolsa))

        dados.bolsas.append(bolsa)

        return jsonify({
            "mensagem": "Bolsa registrada"
        }), 201

    @app.get("/bolsas")
    def listar_bolsas():

        return jsonify(dados.bolsas)
    
    # BUSCAR POR TIPO SANGUINEO

    @app.get("/bolsas/tipo/<tipo>")
    def buscar_tipo(tipo):

        resultado = []

        for bolsa in dados.bolsas:
            if bolsa["tipoSanguineo"] == tipo:
                resultado.append(bolsa)

        return jsonify(resultado)
