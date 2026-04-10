from flask import Blueprint, jsonify, request
import dados

triagem_bp = Blueprint("triagem", __name__)

@triagem_bp.get("/triagens")
def listar_triagens():
    if not dados.triagens:
        return jsonify({"mensagem": "Nenhuma triagem encontrada"}), 400
    return jsonify(dados.triagens), 200

@triagem_bp.post("/triagem")
def criar_triagem():

    triagem = request.json

    if not triagem:
        return jsonify({"erro": "JSON inválido"}), 400

    # Valida se o campo 'id' existe e é do tipo int
    if "id" not in triagem:
        return jsonify({"erro": "Campo 'id' é obrigatório"}), 400
    
    if not isinstance(triagem["id"], int) or isinstance(triagem["id"], bool):
        return jsonify({"erro": "Campo 'id' deve ser um número inteiro"}), 422

    # Valida se o campo 'doadorId' existe e é do tipo int
    if "doadorId" not in triagem:
        return jsonify({"erro": "Campo 'doadorId' é obrigatório"}), 400
    
    if not isinstance(triagem["doadorId"], int) or isinstance(triagem["doadorId"], bool):
        return jsonify({"erro": "Campo 'doadorId' deve ser um número inteiro"}), 422

    # Valida se o campo 'dataTriagem' existe e é do tipo str
    if "dataTriagem" not in triagem:
        return jsonify({"erro": "Campo 'dataTriagem' é obrigatório"}), 400

    if not isinstance(triagem["dataTriagem"], str):
        return jsonify({"erro": "Campo 'dataTriagem' deve ser texto (ex: '2024-06-01')"}), 422
    
    # Valida se o campo 'resultado' existe e é do tipo str
    if "resultado" not in triagem:
        return jsonify({"erro": "Campo 'resultado' é obrigatório"}), 400
    
    if not isinstance(triagem["resultado"], str):
        return jsonify({"erro": "Campo 'resultado' deve ser texto (ex: 'Apto' ou 'Inapto')"}), 422

    dados.triagens.append(triagem)
    dados.salvar("triagens.json", dados.triagens)

    return jsonify({
        "mensagem": "Triagem registrada",
        "triagem": triagem
    }), 201
    