import psycopg2

def registrar_horas():
    print("--- ⏱️ ART-TECH: REGISTRO DE FLUXO DE TRABALHO ---")
    
    # 1. Solicita ao usuário a quantidade de horas trabalhadas na sessão
    try:
        horas_sessao = float(input("Quantas horas você trabalhou nessa sessão? (Ex: 1.5 para 1h30min): "))
    except ValueError:
        print("❌ Erro: Por favor, digite um número válido usando ponto (Ex: 2 ou 1.5).")
        return

    try:
        # 2. Conecta ao banco de dados com a sua credencial personalizada
        conexao = psycopg2.connect(
            host="localhost",
            database="art_tech_db",
            user="postgres",
            password="vania"
        )
        cursor = conexao.cursor()
        
        # 3. Executa o UPDATE somando as novas horas ao valor atual (id = 1 para a bolsa Alpha)
        id_bolsa = 1
        sql_update = """
            UPDATE producao_bolsas 
            SET horas_trabalhadas = horas_trabalhadas + %s 
            WHERE id = %s;
        """
        
        cursor.execute(sql_update, (horas_sessao, id_bolsa))
        conexao.commit()  # Confirma a alteração no banco
        
        # 4. Busca o valor atualizado para dar o feedback na tela
        cursor.execute("SELECT nome_modelo, horas_trabalhadas FROM producao_bolsas WHERE id = %s;", (id_bolsa,))
        resultado = cursor.fetchone()
        
        print("\n✅ Dados atualizados com sucesso!")
        print(f"👜 Bolsa: {resultado[0]}")
        print(f"⏱️ Total acumulado de tempo investido: {resultado[1]} horas.")
        print("--------------------------------------------------\n")
        
        # 5. Fecha as conexões
        cursor.close()
        conexao.close()
        
    except Exception as erro:
        print(f"❌ Erro ao conectar ou atualizar o banco de dados: {erro}")

if __name__ == "__main__":
    registrar_horas()