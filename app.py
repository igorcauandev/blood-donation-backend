from flask import Flask
from rotas import registrar_rotas
from routes.bolsas import rota_bolsas
from routes.doadores import rota_doadores

app = Flask(__name__)

registrar_rotas(app)
rota_bolsas(app)
rota_doadores(app)

app.run(debug=True)