import psycopg2

def testar_conexao():
    try:
        # 1. Estabelece a conexão com o banco real da Art-tech
        conexao = psycopg2.connect(
    host="localhost",
    database="art_tech_db",
    user="postgres",
    password="vania"
)
        
        
        # 2. Cria o cursor para executar comandos
        cursor = conexao.cursor()
        
        # 3. Executa a nossa query de verificação
        cursor.execute("SELECT id, nome_modelo, fio_principal_cor, status_venda FROM producao_bolsas WHERE status_venda = 'Em produção';")
        
        bolsas = cursor.fetchall()
        
        print("\n--- 👜 ARTE-TECH: BOLSAS EM PRODUÇÃO ---")
        for bolsa in bolsas:
            print(f"ID: {bolsa[0]} | Modelo: {bolsa[1]} | Linha: {bolsa[2]} | Status: {bolsa[3]}")
        print("---------------------------------------\n")
        
        # 4. Fecha as conexões de forma segura
        cursor.close()
        conexao.close()
        
    except Exception as erro:
        print(f"Erro ao conectar ao banco de dados: {erro}")

if __name__ == "__main__":
    testar_conexao()