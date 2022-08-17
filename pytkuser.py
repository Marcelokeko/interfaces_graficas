import pymysql

conn = pymysql.connect(db='aula1',user='root',passwd='frederico')

class Tabela_cadastro():
    def __init__(self,id=0,nome='',sobrenome='',cpf=''):
        self.id = id
        self.nome_cliente = nome
        self.sobrenome = sobrenome
        self.cpf = cpf
        
# Criar as açoes de crud no banco

    def insere_user(self):
        cursor = conn.cursor()
        cursor.execute("insert into clientes(Nome_cliente,sobrenome,cpf) values('"+self.Nome_cliente+"','"+self.sobrenome+"','"+self.cpf+"')")
        conn.commit()
        cursor.close()
        
    def selectusuario(self,id):
        
        cursor = conn.cursor()
        cursor.execute("select * from clientes where id ="+id+"")
        
        for regs in cursor:
            self.id = regs[0]
            self.Nome_cliente = regs[1]
            self.sobrenome = regs[2]
            self.cpf = regs[3]
            
        cursor.close()
        