from flask import Flask
from routes.bolsas import bolsas_bp
from routes.doadores import doadores_bp
from routes.centrodoacao import homocentro_bp
from routes.triagem import triagem_bp

app = Flask(__name__)

app.register_blueprint(bolsas_bp)
app.register_blueprint(doadores_bp)
app.register_blueprint(homocentro_bp)
app.register_blueprint(triagem_bp)

app.run(debug=True)