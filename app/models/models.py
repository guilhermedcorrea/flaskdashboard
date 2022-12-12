from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
def configure(app):
    db.init_app(app)
    app.db = db


class Produtos(db.Model):
    __tablename__ = "produto"
    __bind_key__ = "appweb"
    __table_args__ = {"schema": "produtos"}
    idproduto = db.Column(db.Integer, primary_key=True)
    sku = db.Column(db.String)
    nomeproduto = db.Column(db.String)
    marca = db.Column(db.String)
    ean = db.Column(db.String)
    atributos = db.Column(db.String)
    preco = db.Column(db.Float)



class MonitoramentoPrecos(db.Model):
    __tablename__ = "monitoramentoprecos"
    __bind_key__ = "appweb"
    __table_args__ = {"schema": "produtos"}
    idprecos = db.Column(db.Integer, primary_key=True)
    marca = db.Column(db.String)
    seller = db.Column(db.String)
    preco = db.Column(db.Float)
    urlgoogle = db.Column(db.String)
    urlanuncio = db.Column(db.String)
    ean = db.Column(db.String)
    nomeproduto = db.Column(db.String)
    dataatualizacao = db.Column(db.DateTime)
 
class Precificacao(db.Model):
    __tablename__ = "precificacao"
    __bind_key__ = "appweb"
    __table_args__ = {"schema": "produtos"}
    idprecos = db.Column(db.Integer, primary_key=True)
    urlanuncio = db.Column(db.String)
    sku = db.Column(db.String)
    marca = db.Column(db.String)
    precoproduto = db.Column(db.Float)
    precoselelr = db.Column(db.Float)
    diferenca = db.Column(db.Float)
    statuspreco = db.Column(db.String)
    novopreco = db.Column(db.Float)
    dataalteracao = db.Column(db.DateTime)


class Pedidos(db.Model):
    __tablename__ = "pedidos"
    __bind_key__ = "appweb"
    __table_args__ = {"schema": "produtos"}
    idpedido = db.Column(db.Integer, primary_key=True)
    numeropedido = db.Column(db.Integer)
    valorpedido = db.Column(db.Float)
    idproduto = db.Column(db.Integer)
    sku = db.Column(db.String)
    marca = db.Column(db.String)
    quantidade = db.Column(db.Float)
    cidade = db.Column(db.String)
    statuspedido = db.Column(db.String)
    datapedido = db.Column(db.DateTime)









