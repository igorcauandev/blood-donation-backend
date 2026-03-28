from flask import Blueprint, jsonify, request
import dados

homocentro_bp = Blueprint("homocentro", __name__)


@homocentro_bp.get("/homocentros")
def listar_homocentros():
    return jsonify(dados.homocentros), 200

@homocentro_bp.get("/homocentros/<int:id>")
def buscar_homocentro(id):
    if id < len(dados.homocentros):
        return jsonify(dados.homocentros[id]), 200

    return jsonify({"erro": "Homocentro não encontrado"}), 400

@homocentro_bp.post("/homocentros")
def criar_homocentro():

    homocentro = request.json

    if not homocentro:
        return jsonify({"erro": "JSON inválido"}), 400

    if "id" not in homocentro or not isinstance(homocentro["id"], int) or isinstance(homocentro["id"], bool):
        return jsonify({"erro": "Campo 'id' é obrigatório e deve ser número inteiro"}), 400

    if "nome" not in homocentro or not isinstance(homocentro["nome"], str):
        return jsonify({"erro": "Campo 'nome' é obrigatório e deve ser texto"}), 400

    if "endereco" not in homocentro or not isinstance(homocentro["endereco"], str):
        return jsonify({"erro": "Campo 'endereco' é obrigatório e deve ser texto"}), 400

    if "telefone" not in homocentro or not isinstance(homocentro["telefone"], str):
        return jsonify({"erro": "Campo 'telefone' é obrigatório e deve ser texto"}), 400

    dados.homocentros.append(homocentro)
    dados.salvar("homocentros.json", dados.homocentros)

    return jsonify({
        "mensagem": "Homocentro registrado",
        "homocentro": homocentro
    }), 201