from flask import Flask, jsonify, request
import json

app = Flask(__name__)

desenvolvedores = [
    {'nome': 'Rodrigo',
     'ID': 0,
     'habilidades': ['Python', 'Rust', 'Flask']
     },
    {'nome': 'Arnaldinho',
     'ID': 1,
     'habilidades': ['Java', 'Golang', 'Django']}
]

# Recupera, Altera ou Deleta um determinado desenvolvedor pelo ID
@app.route('/dev/<int:id>/', methods=['GET', 'PUT', 'DELETE'])
def desenvolvedor(id):
    if request.method == 'GET':
        try:
            response = desenvolvedores[id]
        except IndexError:
            mensagem = 'Desenvolvedor ID:{} inexistente!'.format(id)
            response = {'status':'erro', 'mensagem': mensagem}
        except Exception:
            mensagem = 'Erro desconhecido. Consulte o administrador da API'
            response = {'status': 'erro', 'mensagem': mensagem}
        return jsonify(response)
    elif request.method == 'PUT':
        dados = json.loads(request.data)
        desenvolvedores[id] = dados
        return jsonify(dados)
    elif request.method == 'DELETE':
        desenvolvedores.pop(id)
        return jsonify({'status': 'sucesso', 'mensagem': 'registro deletado!'})

# Adiciona ou lista os desenvolvedores cadastrados
@app.route('/dev/', methods=['POST', 'GET'])
def lista_desenvoledores():
    if request.method == 'POST':
        dados = json.loads(request.data)
        pos = len(desenvolvedores)
        dados['ID'] = pos
        desenvolvedores.append(dados)
        mensagem = 'Registro adicionado'
        return jsonify({'mensagem': mensagem,
                        'desenvolvedor adicionado na posição': pos,
                        'dev': desenvolvedores[pos]})
    elif request.method == 'GET':
        return jsonify(desenvolvedores)


if __name__ == '__main__':
    app.run(debug=True)
