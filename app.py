from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        nome = request.form.get('nome', 'Visitante')
        return render_template('index.html', nome=nome)
    return render_template('index.html', nome='Visitante')

if __name__ == '__main__':
    app.run(debug=True)