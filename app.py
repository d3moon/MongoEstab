from flask import Flask, render_template, request, redirect, url_for, flash
from pymongo import MongoClient
from bson.objectid import ObjectId
from validator import is_valid_cnpj, is_valid_cep, is_valid_telephone, is_valid_email
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
client = MongoClient(os.getenv('MONGO_URI'))
db = client['desafio1']
collection = db['estabelecimentos9']


@app.route('/')
def index():
    estabelecimentos = collection.find()
    return render_template('index.html', estabelecimentos=estabelecimentos)


@app.route('/add', methods=['GET', 'POST'])
def add():
     
    if request.method == 'POST':
        cnpj = request.form['cnpj']
        nome = request.form['nome']
        cep = request.form['cep']
        telefone = request.form['telefone']
        email = request.form['email']
        if not is_valid_cnpj(cnpj):
            flash('CNPJ inválido.')
            return redirect(url_for('add'))
        if not is_valid_cep(cep):
            flash('CEP inválido.')
            return redirect(url_for('add'))
        if not is_valid_telephone(telefone):
            flash('Telefone inválido.')
            return redirect(url_for('add'))
        if not is_valid_email(email):
            flash('Email inválido.')
            return redirect(url_for('add'))
        collection.insert_one({
            'CNPJ': cnpj,
            'Nome': nome,
            'CEP': cep,
            'Telefone': telefone,
            'Email': email
        })
        flash('Estabelecimento adicionado com sucesso.')
        return redirect(url_for('index'))
    return render_template('add.html')


@app.route('/edit/<id>', methods=['GET', 'POST'])
def edit(id):
    estabelecimento = collection.find_one({'_id': ObjectId(id)})
    if not estabelecimento:
        return redirect(url_for('page_not_found'))
    if request.method == 'POST':
        cnpj = request.form['cnpj']
        nome = request.form['nome']
        cep = request.form['cep']
        telefone = request.form['telefone']
        email = request.form['email']
        if not is_valid_cnpj(cnpj):
            flash('CNPJ inválido.')
            return redirect(url_for('edit', id=id))
        if not is_valid_cep(cep):
            flash('CEP inválido.')
            return redirect(url_for('edit', id=id))
        if not is_valid_telephone(telefone):
            flash('Telefone inválido.')
            return redirect(url_for('edit', id=id))
        if not is_valid_email(email):
            flash('Email inválido.')
            return redirect(url_for('edit', id=id))

        collection.update_one({'_id': ObjectId(id)}, {'$set': {
            'CNPJ': cnpj,
            'Nome': nome,
            'CEP': cep,
            'Telefone': telefone,
            'Email': email
        }})
        flash('Estabelecimento atualizado com sucesso.')
        return redirect(url_for('index'))

    return render_template('edit.html', estabelecimento=estabelecimento)


      
@app.route('/delete/<id>', methods=['POST'])
def delete(id):
    collection.delete_one({'_id': ObjectId(id)})
    flash('Estabelecimento removido com sucesso.')
    return redirect(url_for('index'))


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
