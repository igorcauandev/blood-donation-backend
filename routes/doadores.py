from flask import Blueprint, jsonify, request
import json
import dados

doadores_bp = Blueprint("doadores", __name__)

@doadores_bp.get("/doadores")
def listar_doadores():
    if not dados.pessoas:
        return jsonify({"mensagem": "Nenhum doador encontrado"}), 400
    return jsonify(dados.pessoas), 200


@doadores_bp.post("/doadores")
def criar_doador():

    novo = request.json

    if not novo:
        return jsonify({"erro": "JSON inválido"}), 400

    # Valida se o campo 'id' existe e é do tipo int
    if "id" not in novo:
        return jsonify({"erro": "Campo 'id' é obrigatório"}), 400

    if not isinstance(novo["id"], int):
        return jsonify({"erro": "Campo 'id' deve ser um número inteiro"}), 400

    # Valida se o campo 'nome' existe e é do tipo str
    if "nome" not in novo:
        return jsonify({"erro": "Campo 'nome' é obrigatório"}), 400
    
    if not isinstance(novo["nome"], str):
        return jsonify({"erro": "Campo 'nome' deve ser texto"}), 422

    # Valida se o campo 'tipoSanguineo' existe e é do tipo str
    if "tipoSanguineo" not in novo:
        return jsonify({"erro": "Campo 'tipoSanguineo' é obrigatório"}), 400
    
    if not isinstance(novo["tipoSanguineo"], str):
        return jsonify({"erro": "Campo 'tipoSanguineo' deve ser texto"}), 422
    
    # Valida se o campo 'genero' existe e é do tipo str
    if "genero" not in novo:
        return jsonify({"erro": "Campo 'genero' é obrigatório"}), 400
    
    if not isinstance(novo["genero"], str):
        return jsonify({"erro": "Campo 'genero' deve ser texto"}), 422

    # Valida se o campo 'idade' existe e é do tipo int
    if "idade" not in novo:
        return jsonify({"erro": "Campo 'idade' é obrigatório"}), 400
    
    if not isinstance(novo["idade"], int):
        return jsonify({"erro": "Campo 'idade' deve ser um número inteiro"}), 422

    if "peso" not in novo or not isinstance(novo["peso"], (int, float)):
        return jsonify({"erro": "Campo 'peso' é obrigatório e deve ser número"}), 400

    dados.pessoas.append(novo)
    dados.salvar("doadores.json", dados.pessoas)  # persiste no arquivo

    return jsonify({
        "mensagem": "Doador cadastrado",
        "doador": novo
    }), 201


@doadores_bp.get("/doadores/<int:id>")
def buscar_doador(id):

    if id < len(dados.pessoas):
        return jsonify(dados.pessoas[id]), 200

    return jsonify({"erro": "Doador não encontrado"}), 400