from flask import Flask, render_template, request
from models.tarefa import Tarefa

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html', titulo='Home')

@app.route('/agenda', methods=['GET', 'POST'])
def agenda():
    tarefa = None

    if request.method == 'POST':
        titulo_tarefa = request.form.get('titulo_tarefa')
        data_conclusao = request.form.get('data_conclusao')
        tarefa = Tarefa(titulo_tarefa, data_conclusao)
        tarefa.salvar_tarefa()

    tarefas = Tarefa.obter_tarefas()
    return render_template(
        'agenda.html',
        titulo='Agenda',
        tarefa=tarefa
    )

@app.route('delete/<int:idTarefa>')
def delete(idTarefa):
    tarefa = Tarefa.id(idTarefa)
    tarefa.excluir_tarefa()

@app.route('/ola')
def ola_mundo():
    return "Olá, Mundo!"

if __name__ == "__main__":
    app.run(debug=True)
