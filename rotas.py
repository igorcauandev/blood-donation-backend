from flask import jsonify, request
import dados


def registrar_rotas(app):

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


    # TRIAGEM

    @app.post("/triagens")
    def criar_triagem():

        triagem = request.json
        dados.triagens.append(triagem)

        return jsonify({
            "mensagem": "Triagem registrada"
        })


    @app.get("/triagens")
    def listar_triagens():

        return jsonify(dados.triagens)


    # SOLICITAÇÃO DE HOSPITAL

    @app.post("/solicitacoes")
    def criar_solicitacao():

        solicitacao = request.json
        dados.solicitacoes.append(solicitacao)

        return jsonify({
            "mensagem": "Solicitação registrada"
        })


    @app.get("/solicitacoes")
    def listar_solicitacoes():

        return jsonify(dados.solicitacoes)