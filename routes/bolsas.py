from flask import Blueprint, jsonify, request
import dados


bolsas_bp = Blueprint("bolsas", __name__)


@bolsas_bp.post("/bolsas")
def criar_bolsa():

    bolsa = request.json

    if not bolsa:
        return jsonify({"erro": "JSON inválido"}), 400

    if "id" not in bolsa or not isinstance(bolsa["id"], int) or isinstance(bolsa["id"], bool):
        return jsonify({"erro": "Campo 'id' é obrigatório e deve ser número inteiro"}), 400

    if "quantidade" not in bolsa or not isinstance(bolsa["quantidade"], str):
        return jsonify({"erro": "Campo 'quantidade' é obrigatório e deve ser texto"}), 400

    if "dataColeta" not in bolsa or not isinstance(bolsa["dataColeta"], str):
        return jsonify({"erro": "Campo 'dataColeta' é obrigatório e deve ser texto"}), 400

    if "dataValidade" not in bolsa or not isinstance(bolsa["dataValidade"], str):
        return jsonify({"erro": "Campo 'dataValidade' é obrigatório e deve ser texto"}), 400

    if "tipoSanguineo" not in bolsa or not isinstance(bolsa["tipoSanguineo"], str):
        return jsonify({"erro": "Campo 'tipoSanguineo' é obrigatório e deve ser texto"}), 400

    if "doador" not in bolsa or not isinstance(bolsa["doador"], str):
        return jsonify({"erro": "Campo 'doador' é obrigatório e deve ser texto"}), 400

    dados.bolsas.append(bolsa)
    dados.salvar("bolsas.json", dados.bolsas)

    return jsonify({
        "mensagem": "Bolsa registrada",
        "bolsa": bolsa
    }), 201
    

@bolsas_bp.get("/bolsas")
def listar_bolsas():

    return jsonify(dados.bolsas), 200


@bolsas_bp.get("/bolsas/tipo/<tipo>")
def buscar_tipo(tipo):

    resultado = []

    for bolsa in dados.bolsas:
        if bolsa["tipoSanguineo"] == tipo:
            resultado.append(bolsa)

    return jsonify(resultado), 200
