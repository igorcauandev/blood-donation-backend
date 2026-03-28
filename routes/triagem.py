from flask import Blueprint, jsonify, request
import dados

triagem_bp = Blueprint("triagem", __name__)

@triagem_bp.post("/triagem")
def criar_triagem():

    triagem = request.json

    if not triagem:
        return jsonify({"erro": "JSON inválido"}), 400

    if "id" not in triagem or not isinstance(triagem["id"], int) or isinstance(triagem["id"], bool):
        return jsonify({"erro": "Campo 'id' é obrigatório e deve ser número inteiro"}), 400

    if "doadorId" not in triagem or not isinstance(triagem["doadorId"], int) or isinstance(triagem["doadorId"], bool):
        return jsonify({"erro": "Campo 'doadorId' é obrigatório e deve ser número inteiro"}), 400

    if "dataTriagem" not in triagem or not isinstance(triagem["dataTriagem"], str):
        return jsonify({"erro": "Campo 'dataTriagem' é obrigatório e deve ser texto"}), 400

    if "resultado" not in triagem or not isinstance(triagem["resultado"], str):
        return jsonify({"erro": "Campo 'resultado' é obrigatório e deve ser texto"}), 400

    dados.triagens.append(triagem)
    dados.salvar("triagens.json", dados.triagens)

    return jsonify({
        "mensagem": "Triagem registrada",
        "triagem": triagem
    }), 201
    
@triagem_bp.get("/triagens")
def listar_triagens():
    if not dados.triagens:
        return jsonify({"mensagem": "Nenhuma triagem encontrada"}), 400
    return jsonify(dados.triagens), 200