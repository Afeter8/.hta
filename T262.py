from flask import Flask, jsonify
import protección  # tu archivo protección.py con funciones autónomas

app = Flask(__name__)

@app.route('/api/proteccion')
def api_proteccion():
    protección.verificar_integridad()
    protección.reparar_sistema()
    return jsonify({"status": "ok", "timestamp": str(datetime.now())})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
