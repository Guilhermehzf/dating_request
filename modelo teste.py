from sqlalchemy import create_engine, asc
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.automap import automap_base
from prettytable import PrettyTable

# ----- CONEXAO GLOBAL ------------------------------------

# Ligação com o esquema de banco de dados
engine = create_engine("mysql+mysqlconnector://root:uniceub@localhost/brasil?charset=utf8mb4")

# Mapeamento Objeto Relacional com o SQLAlchemy
DB = automap_base()
DB.prepare(autoload_with=engine)
estados_brasil= DB.classes.estados_brasil
municipio_brasil = DB.classes.municipio_brasil


# Trabalho com sessões da base agora Objeto-Relacional com SQLAlchemy
session_factory = sessionmaker(bind=engine)
ses = session_factory()

def lista_estados():
   pt = PrettyTable(["Identificador", "Estado"])
   lst = ses.query(estados_brasil).order_by(asc(estados_brasil.Estado))
   if lst.first():
       for obj in lst:
           pt.add_row([obj.id_estado, obj.Estado])
           pt.add_row(["", ""])
       print(pt)
   return



def lista_municipios():
   nome = input('nome: ')
   pt = PrettyTable(["Identificador", "Município"])
   lst = ses.query(municipio_brasil).order_by(asc(municipio_brasil.Município)).filter(municipio_brasil.Município.ilike('%' + nome + '%'))
   if lst.first():
       for obj in lst:
           pt.add_row([obj.id_municipio, obj.Município])
           pt.add_row(["", ""])
       print(pt)
   return


def main():
 sair = False
 while not sair:
     print('''
     MENU DE OPÇÔES
     1 - lista_estados
     2 - listas municípos pelo nome
     3 - sair
     ''')
     opc = input("Qual a opção? ")
     print("\n" * 2)
     if opc == "1":
         lista_estados()
     elif opc == "2":
         lista_municipios()
     elif opc == "3":
         sair = True
         print("Fim de Programa")
 return


if __name__ == "__main__":
    main()
