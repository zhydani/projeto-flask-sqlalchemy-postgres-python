from . import db

class Empenho(db.Model):
    """Model for user accounts."""

    __tablename__ = 'empenho'
    _id = db.Column(db.Integer, primary_key=True)
    dt_emissao = db.Column(db.String(120), unique=False)
    dt_create = db.Column(db.String(120), unique=False)
    numero = db.Column(db.String(120), unique=False)
    valor = db.Column(db.String(120), unique=False)
    existencia_relatorio = db.Column(db.String(120), unique=False)
    id_municipio = db.Column(db.Integer, unique=False)
    servico_produto = db.Column(db.String(120), unique=False)
    id_classificacao_orcamentaria = db.Column(db.Integer, unique=False)
    id_fornecedor_credor = db.Column(db.Integer, unique=False)

    def __repr__(self):
        return '<Empenho {}>'.format(self.numero)

class Fornecedor_credor(db.Model):
    __tablename__ = 'fornecedor_credor'
    _id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(120), unique=False)
    validar_cpf_cnpj = db.Column(db.String(120), unique=False)
    cpf_cnpj = db.Column(db.String(120), unique=False)

    def __repr__(self):
        return '<Fornecedor_credor {}>'.format(self.cpf_cnpj)