import os
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, Integer, String

#confirgurando uma string de conexão 
engine = create_engine("sqlite:///database.db")

#configurando seesão
Session = sessionmaker(engine)

#criando tabela
Base = declarative_base()

class Usuario(Base):
    __tablename__ = "usuarios"
    id = Column(Integer, primary_key=True)
    nome = Column(String, nullable=False)
    tipo = Column(String, nullable=False)

def insert_usuario(nome_usuario, tipo_usuario):
    session = Session()
    try:
        if all([nome_usuario, tipo_usuario]):
            usuario = Usuario(nome=nome_usuario, tipo=tipo_usuario)
            session.add(usuario)
            session.commit()
            print(f"Usuário {nome_usuario} adicionado com sucesso")
        else:
            print("Preencha todos os campos, por favor?")
    except Exception as e:
        session.rollback()
        print(f'Ocorreu um erro ao tentar criar usuário {nome_usuario}: {e}')
    finally:
        session.close()

def select_usuarios(nome_usuario = ''):
    session = Session()
    try:
        if nome_usuario:
            dados = session.query(Usuario).filter(Usuario.nome == nome_usuario).all()
        else:
            dados = session.query(Usuario).all()
        for i in dados:
            print(f'Usuario: {i.nome}  - Tipo: {i.tipo}')
        
    except Exception as e:
        print(f'Ocorreu um erro ao consultar os usuários')

    finally:
        session.close()

def update_nome_usuario(id_usuario, nome_usuario):
    session = Session()
    try:
        if all([id_usuario, nome_usuario]):
            usuario = session.query(Usuario).filter(Usuario.id == id_usuario).first()
            usuario.nome = nome_usuario
            session.commit()
            print(f'Usuário {id_usuario} atualizado com sucesso')
        else:    
            print("obrigatório id e nome que quer atualizar.")
    except Exception as e:
        session.rollback()
        print(f'Ocorreu um erro ao tentar atualizar o usuário {id}: {e}')
    finally:
        session.close()

    #Deletar um usuário:

def delete_usuario(id_usuario):
    session = Session()
    try:
        if id_usuario:
            usuario = session.query(Usuario).filter(Usuario.id == id_usuario).first()
            session.delete(usuario)
            session.commit()
            print(f'Usuário {id_usuario} deletado com sucesso')
        else:
                print('É obrigatório informar o id do usuário')
    except Exception as e:
                session.rollback()
                print(f'Ocorreu um erro ao tentar deletar o usuário {id_usuario}: {e}')
    finally:
            session.close()

        

if __name__ == "__main__":
    os.system('cls')
    Base.metadata.create_all(engine)
    # insert_usuario('Lucas', 'Consultor')
    
    #Select usuário:
    # select_usuarios('Lucas')

    #Atualizar usuário:
    # update_nome_usuario(3, 'Maria Antonieta')
    
    #Deletar usuário
    delete_usuario(3)




  

  





