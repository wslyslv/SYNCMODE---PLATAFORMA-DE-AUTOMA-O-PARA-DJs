from flask import Flask, render_template, request, jsonify
from modules.organizer import scan_music_folder
import os

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/organizar', methods=['POST'])
def organizar():
    data= request.get_json()
    source_folder = data.get('source')
    target_folder=data.get('target')
    # validação simples (espera-se caminhos absolutos ou relativos válidos)
    if not source_folder or not os.path.exists(source_folder):
        return jsonify({'error': 'Pasta de origem inválida.'}), 400

    # target_folder é opcional na implementação atual — a função aceita None
    if target_folder and not os.path.exists(target_folder):
        return jsonify({'error': 'Pasta de destino inválida.'}), 400

    logs = scan_music_folder(source_folder, target_folder)
    return jsonify({'result': logs})

@app.route("/scan", methods=["GET"])
def scan():
    # usa caminho absoluto baseado na raiz do app para evitar problemas de path
    folder = os.path.join(app.root_path, 'static', 'musics')
    musics = scan_music_folder(folder)
    return jsonify(musics)

if __name__=='__main__':
    app.run(debug=True)