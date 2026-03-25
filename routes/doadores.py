from flask import jsonify, request
import dados


def rota_doadores(app):

    # DOADORES

    @app.get("/doadores")
    def listar_doadores():
        return jsonify(dados.pessoas)


    @app.post("/doadores")
    def criar_doador():

        novo = request.json
        dados.pessoas.append(novo)

        return jsonify({
            "mensagem": "Doador cadastrado",
            "doador": novo
        })


    @app.get("/doadores/<int:id>")
    def buscar_doador(id):

        if id < len(dados.pessoas):
            return jsonify(dados.pessoas[id])

        return jsonify({"erro": "Doador não encontrado"})