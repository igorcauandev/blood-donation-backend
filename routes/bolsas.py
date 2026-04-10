from flask import Blueprint, jsonify, request
import dados


bolsas_bp = Blueprint("bolsas", __name__)


@bolsas_bp.post("/bolsas")
def criar_bolsa():

    bolsa = request.json

    if not bolsa:
        return jsonify({"erro": "JSON inválido"}), 400

    # Valida se o campo 'id' existe e é do tipo int
    if "id" not in bolsa:
        return jsonify({"erro": "Campo 'id' é obrigatório"}), 400

    if not isinstance(bolsa["id"], int):
        return jsonify({"erro": "Campo 'id' deve ser um número inteiro"}), 422

    # Valida se o campo 'quantidade' existe e é do tipo str
    if "quantidade" not in bolsa:
        return jsonify({"erro": "Campo 'quantidade' é obrigatório"}), 400

    if not isinstance(bolsa["quantidade"], str):
        return jsonify({"erro": "Campo 'quantidade' deve ser texto (ex: '100ml')"}), 422

    # Valida se o campo 'dataColeta' existe e é do tipo str
    if "dataColeta" not in bolsa:
        return jsonify({"erro": "Campo 'dataColeta' é obrigatório"}), 400

    if not isinstance(bolsa["dataColeta"], str):
        return jsonify({"erro": "Campo 'dataColeta' deve ser texto (ex: '2024-06-01')"}), 422

    # Valida se o campo 'dataValidade' existe e é do tipo str
    if "dataValidade" not in bolsa:
        return jsonify({"erro": "Campo 'dataValidade' é obrigatório"}), 400

    if not isinstance(bolsa["dataValidade"], str):
        return jsonify({"erro": "Campo 'dataValidade' deve ser texto (ex: '2024-12-01')"}), 422

    # Valida se o campo 'dataSaida' existe e é do tipo str
    if "dataSaida" not in bolsa:
        return jsonify({"erro": "Campo 'dataSaida' é obrigatório"}), 400

    if not isinstance(bolsa["dataSaida"], str):
        return jsonify({"erro": "Campo 'dataSaida' deve ser texto (ex: '2024-12-01')"}), 422

    # Valida se o campo 'localArmazenamento' existe e é do tipo str
    if "localArmazenamento" not in bolsa:
        return jsonify({"erro": "Campo 'localArmazenamento' é obrigatório"}), 400

    if not isinstance(bolsa["localArmazenamento"], str):
        return jsonify({"erro": "Campo 'localArmazenamento' deve ser texto"}), 422

    # Valida se o campo 'tipoSanguineo' existe e é do tipo str
    if "tipoSanguineo" not in bolsa:
        return jsonify({"erro": "Campo 'tipoSanguineo' é obrigatório"}), 400

    if not isinstance(bolsa["tipoSanguineo"], str):
        return jsonify({"erro": "Campo 'tipoSanguineo' deve ser texto (ex: 'O+')"}), 422

    # Valida se o campo 'doador' existe e é do tipo str
    if "doador" not in bolsa:
        return jsonify({"erro": "Campo 'doador' é obrigatório"}), 400

    if not isinstance(bolsa["doador"], str):
        return jsonify({"erro": "Campo 'doador' deve ser texto"}), 422

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
