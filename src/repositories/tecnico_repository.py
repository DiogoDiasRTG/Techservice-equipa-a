from src.database.conexao import conectar
from src.models.tecnico import Tecnico


def inserir(tecnico):
    conexao = conectar()
    cursor = conexao.cursor()

    sql = """INSERT INTO tecnicos (nome, telefone, email, especialidade)
             VALUES (%s, %s, %s, %s)"""
    valores = (tecnico.nome, tecnico.telefone, tecnico.email,
               tecnico.especialidade)

    cursor.execute(sql, valores)
    conexao.commit()

    tecnico.id_tecnico = cursor.lastrowid

    cursor.close()
    conexao.close()

    return tecnico


def procurar_por_id(id_tecnico):
    conexao = conectar()
    cursor = conexao.cursor(dictionary=True)

    sql = "SELECT * FROM tecnicos WHERE id_tecnico = %s"
    cursor.execute(sql, (id_tecnico,))
    linha = cursor.fetchone()

    cursor.close()
    conexao.close()

    if linha is None:
        return None

    return linha_para_tecnico(linha)


def listar():
    conexao = conectar()
    cursor = conexao.cursor(dictionary=True)

    cursor.execute("SELECT * FROM tecnicos WHERE ativo = 1")
    linhas = cursor.fetchall()

    cursor.close()
    conexao.close()

    return linhas


def atualizar(tecnico):
    conexao = conectar()
    cursor = conexao.cursor()

    sql = """UPDATE tecnicos
             SET nome = %s, telefone = %s, email = %s,
                 especialidade = %s, ativo = %s
             WHERE id_tecnico = %s"""
    valores = (tecnico.nome, tecnico.telefone, tecnico.email,
               tecnico.especialidade, tecnico.status, tecnico.id_tecnico)

    cursor.execute(sql, valores)
    conexao.commit()

    cursor.close()
    conexao.close()


def remover(id_tecnico):
    conexao = conectar()
    cursor = conexao.cursor()

    sql = "DELETE FROM tecnicos WHERE id_tecnico = %s"
    cursor.execute(sql, (id_tecnico,))
    conexao.commit()

    cursor.close()
    conexao.close()


def linha_para_tecnico(linha):
    return Tecnico(
        id_tecnico=linha["id_tecnico"],
        nome=linha["nome"],
        telefone=linha["telefone"],
        email=linha["email"],
        especialidade=linha["especialidade"],
        status=linha["ativo"]
    )
