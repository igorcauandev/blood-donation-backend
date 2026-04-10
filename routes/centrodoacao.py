from flask import Blueprint, jsonify, request
import dados

homocentro_bp = Blueprint("homocentro", __name__)


@homocentro_bp.get("/hemocentros")
def listar_homocentros():
    return jsonify(dados.hemocentros), 200

@homocentro_bp.get("/hemocentros/<int:id>")
def buscar_homocentro(id):
    if id < len(dados.hemocentros):
        return jsonify(dados.hemocentros[id]), 200

    return jsonify({"erro": "Hemocentro não encontrado"}), 400

@homocentro_bp.post("/hemocentros")
def criar_homocentro():

    hemocentro = request.json

    if not hemocentro:
        return jsonify({"erro": "JSON inválido"}), 400

    # Valida se o campo 'id' existe e é do tipo int
    if "id" not in hemocentro:
        return jsonify({"erro": "Campo 'id' é obrigatório"}), 400
    
    if not isinstance(hemocentro["id"], int):
        return jsonify({"erro": "Campo 'id' deve ser um número inteiro"}), 422

    # Valida se o campo 'nome' existe e é do tipo str
    if "nome" not in hemocentro:
        return jsonify({"erro": "Campo 'nome' é obrigatório"}), 400

    if not isinstance(hemocentro["nome"], str):
        return jsonify({"erro": "Campo 'nome' deve ser texto"}), 422

    # Valida se o campo 'endereco' existe e é do tipo str
    if "endereco" not in hemocentro:
        return jsonify({"erro": "Campo 'endereco' é obrigatório"}), 400

    if not isinstance(hemocentro["endereco"], str):
        return jsonify({"erro": "Campo 'endereco' deve ser texto"}), 422

    # Valida se o campo 'telefone' existe e é do tipo str
    if "telefone" not in hemocentro:
        return jsonify({"erro": "Campo 'telefone' é obrigatório"}), 400

    if not isinstance(hemocentro["telefone"], str):
        return jsonify({"erro": "Campo 'telefone' deve ser texto"}), 422

    dados.hemocentros.append(hemocentro)
    dados.salvar("hemocentros.json", dados.hemocentros)

    return jsonify({
        "mensagem": "Hemocentro registrado",
        "hemocentro": hemocentro
    }), 201