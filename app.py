from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres-aula.cuebxlhckhcy.us-east-1.rds.amazonaws.com:5432'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
db = SQLAlchemy(app)

class Leitor(db.Model):
    _tablename_= 'leitor'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nomelivro = db.Column(db.String(100), nullable=False)
    nomeautor = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    mensagem = db.Column(db.Text, nullable=False)
    receber_informacoes = db.Column(db.Boolean, nullable=False)
    
with app.app_context():
    db.create_all()

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/contato', request['GET', 'POST'])
def contato():
    if request.method == 'POST':
        nomelivro = request.form.get['nome_livro']
        nomeautor = request.form.get['nome_autor']
        email = request.form.get['email']
        mensagem = request.form.get['mensagem']
        receber_informacoes = receber_informacoes in request.form

        novo_leitor = Leitor(
            nomelivro=nomelivro,
            nomeautor=nomeautor,
            email=email,
            mensagem=mensagem,
            receber_informacoes=receber_informacoes
    )
        
        db.session.add(novo_leitor)
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('contato.html')

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)