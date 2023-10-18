from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        data = request.get_json()
        resposta = data.get('resposta')

        if resposta == 'sim':
            # Lógica para lidar com a resposta "Sim"
            print("Você escolheu Sim!")
        else:
            # Lógica para lidar com a resposta "Não"
            print("Você escolheu Não!")

    return render_template('index.html')

if __name__ == '__main__':
    app.run()
