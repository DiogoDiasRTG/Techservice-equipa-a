import os

import mysql.connector
from dotenv import load_dotenv


load_dotenv()


def conectar():
    return mysql.connector.connect(
        host=os.getenv("DB_HOST", "162.240.171.8"),
        port=int(os.getenv("DB_PORT","3306")),
        user=os.getenv("DB_USER", "techservice"),
        password=os.getenv("DB_PASSWORD", "TechService@2026!"),
        database=os.getenv("DB_NAME", "techservice_equipa1")
    )


# --- Teste de conexão logo abaixo ---
if __name__ == "__main__":
    try:
        conexao = conectar()
        if conexao.is_connected():
            db_info = conexao.get_server_info()
            print(f"Sucesso! Conectado ao servidor MySQL versão: {db_info}")
            
            cursor = conexao.cursor()
            cursor.execute("SELECT DATABASE();")
            nome_bd = cursor.fetchone()
            print(f"Banco de dados atual: {nome_bd[0]}")
            
            cursor.close()
            conexao.close()
            print("Conexão fechada com sucesso.")
    except Exception as e:
        print(f"Erro ao conectar ao banco de dados: {e}")