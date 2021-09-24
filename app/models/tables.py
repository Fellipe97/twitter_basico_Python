from enum import unique
from app import db


# db.Model = classe do SQLAlchemy que tras um modelo de banco de dados padrão
class User(db.Model):      #Primeira tabela
    __tablename__= "users"  #o nome da tabela do banco de dados

    id = db.Column(db.Integer, primary_key=True)  #criando a coluna e o que ela suporta; db.Integer = recebe numero inteiro;  primary_key = chave primaria; unique =  evitar repetição (ser único)
    usernane = db.Column(db.String, unique=True)
    password = db.Column(db.String)
    name = db.Column(db.String)
    email = db.Column(db.String, unique=True)

    #construtor que inicializa todos os campos (campos obrigatorios)
    def __init__(self, username, password, name, email):
        self.username = username
        self.password = password
        self.name = name
        self.email = email
    
    # representação, vai ser utilizado para bnusca no banco de dados
    def __repr__(self):
        return "<User %r>" % self.username


class Post(db.Model):
    __tablename__= "posts"

    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))  # id do usuario; referencia ao banco de dados: Users ( db.ForeignKey('users.id')

    user = db.relationship('User', foreign_keys=user_id)  # quando buscar o post, vai vê no campo user não só o id mas tb todas as informações do usuario

    def __init__ (self,content,user_id):
        self.content = content
        self.user_id = user_id
    
    def __repr__(self):
        return "<Post %r>" % self.id


class Follow(db.Model):
    __tablename__ = "follow"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    follower_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    user = db.relationship('User', foreign_keys=user_id)
    follower = db.relationship('User', foreign_keys=follower_id) 



