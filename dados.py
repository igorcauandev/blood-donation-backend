import json
import os

def carregar(arquivo, padrao):
    if os.path.exists(arquivo):
        with open(arquivo, "r", encoding="utf-8") as f:
            return json.load(f)
    return padrao

def salvar(arquivo, lista):
    with open(arquivo, "w", encoding="utf-8") as f:
        json.dump(lista, f, ensure_ascii=False, indent=2)

pessoas = carregar("doadores.json", [
    {
        "id": 1,
        "quantidade": "100ml",
        "dataColeta": "2024-06-01",
        "dataValidade": "2024-12-01",
        "dataSaida": "2024-12-01",
        "localArmazenamento": "Banco de Sangue Central",
        "tipoSanguineo": "O+",
        "doador": "Igor"
    },
])

bolsas = carregar("bolsa.json", [
    {
        "id": 2, 
        "quantidade": "103ml", 
        "dataColeta": "2024-06-01", 
        "dataValidade": "2024-12-01", 
        "dataSaida": "2024-12-01", 
        "localArmazenamento": "Banco de Sangue Central", 
        "tipoSanguineo": "O+", 
        "doador": "Igor"
    },
])

estoque = carregar("estoque.json", [
    {
        "A+": 10, 
        "A-": 5, 
        "B+": 8, 
        "B-": 3, 
        "AB+": 4, 
        "AB-": 2, 
        "O+": 15, 
        "O-": 7
    }
])

homocentros = carregar("homocentros.json", [
    {
        "id": 1, 
        "nome": "Banco de Sangue Central",
        "endereco": "Rua Principal, 123",
        "telefone": "(11) 1234-5678"
    }
])

triagens = carregar("triagens.json", [
    {
        "id": 1, 
        "doadorId": 1, 
        "dataTriagem": "2024-06-01", 
        "resultado": "Apto"
    }
])

solicitacoes = carregar("solicitacoes.json", [])