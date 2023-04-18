from flask import Flask, jsonify

app = Flask(__name__)

dados = {
    "1": {"nome": "João", "idade": 25},
    "2": {"nome": "Maria", "idade": 30},
    "3": {"nome": "Pedro", "idade": 35}
}

@app.route('/dados/<string:id>', methods=['GET'])
def buscar_dado(id):
    if id in dados:
        return jsonify(dados[id]), 200
    else:
        return "Dado não encontrado", 404

if __name__ == '__main__':
    app.run()
