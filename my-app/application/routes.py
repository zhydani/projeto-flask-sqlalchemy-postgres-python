from flask import request, render_template, make_response
from datetime import datetime as dt
from flask import current_app as app
from .models import db, Empenho


@app.route('/', methods=['POST'])
def create_empenho():
    data = request.get_json()
    dt_emissao = data['dt_emissao']
    dt_create = data['dt_create']
    numero = data['numero']
    valor = data['valor']
    existencia_relatorio = data['existencia_relatorio']
    id_municipio = data['id_municipio']
    servico_produto = data['servico_produto']
    id_classificacao_orcamentaria = data['id_classificacao_orcamentaria']

    #Verificar se o fornecedor existe e se ele nao existir, ele será inserido na tabela fornecedor_credor
    cpf_cnpj = data.get("fornecedor").get("cpf_cnpj")
    nome = data.get("fornecedor").get("nome")
    if fornecedor:
        existing_fornecedor = Fornecedor.query.filter(.cpf_cnpj == cpf_cnpj).first()
        if existing:
            return make_response(f'{cpf_cnpj} ({nome}) Este fornecedor ja existe!')
        new_fornecedor = Fornecedor(nome=nome,
                        validar_cpf_cnpj=validar_cpf_cnpj,
                        cpf_cnpj=cpf_cnpj)  
        db.session.add(new_fornecedor)  
        db.session.commit()
        
    print(make_response(f"{new_fornecedor} Fornecedor criado!"))
    result = db.execute('select id from fornecedor_credor where cpf_cnpj = "{}"'.format(cpf_cnpj)).fetchall()
        for select in result:
            for registro in select:
                id_fornecedor_credor = registro
                print(id_fornecedor_credor)

    new_empenho = Empenho(dt_emissao=dt_emissao,
                        dt_create=dt_create,
                        numero=numero,
                        valor=valor,
                        existencia_relatorio=existencia_relatorio,
                        id_municipio=id_municipio,
                        servico_produto=servico_produto,
                        id_classificacao_orcamentaria=id_classificacao_orcamentaria,
                        id_fornecedor_credor=id_fornecedor_credor)  # Create an instance of the User class
    db.session.add(new_empenho)  # Adds new User record to database
    db.session.commit()  # Commits all changes
    return make_response(f"{new_empenho} successfully created!")