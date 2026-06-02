import psycopg2

def exibir_painel_eficiencia():
    print("\n==================================================")
    print("       📊 ART-TECH: PAINEL DE EFICIÊNCIA          ")
    print("==================================================")
    
    id_bolsa = 2  # Sua nova bolsa de Fio Náutico
    meta_horas = 20.0
    
    try:
        # Conecta ao banco de dados utilizando suas credenciais
        conexao = psycopg2.connect(
            host="localhost",
            database="art_tech_db",
            user="postgres",
            password="vania"
        )
        cursor = conexao.cursor()
        
        # Busca os dados reais da peça em produção
        query = """
            SELECT nome_modelo, horas_trabalhadas, data_inicio 
            FROM producao_bolsas 
            WHERE id = %s;
        """
        cursor.execute(query, (id_bolsa,))
        resultado = cursor.fetchone()
        
        if not resultado:
            print("❌ Erro: Bolsa com ID 2 não foi encontrada no banco.")
            return
            
        nome_modelo, horas_gastas, data_inicio = resultado
        horas_gastas = float(horas_gastas)
        
        # Lógica matemática do Burndown e Progresso
        horas_restantes = meta_horas - horas_gastas
        percentual_concluido = (horas_gastas / meta_horas) * 100
        
        # Garante que o mostrador não fique negativo caso você passe um pouco das 20h
        if horas_restantes < 0:
            horas_restantes = 0.0
            
        # Exibe os dados de forma escaneável e limpa
        print(f"👜 Modelo: {nome_modelo}")
        print(f"📅 Início da Jornada: {data_inicio}")
        print(f"🎯 Meta Estipulada: {meta_horas} horas")
        print("--------------------------------------------------")
        print(f"⏱️  Horas já investidas: {horas_gastas:.2f}h")
        print(f"📉 Orçamento de tempo restante: {horas_restantes:.2f}h")
        print(f"📈 Progresso do Método de Ensino: {percentual_concluido:.2f}%")
        print("==================================================")
        
        # Barra de progresso visual no terminal
        blocos = int(percentual_concluido // 5)
        barra = "▓" * blocos + "░" * (20 - blocos)
        print(f"|{barra}| {percentual_concluido:.1f}%\n")
        
        cursor.close()
        conexao.close()
        
    except Exception as erro:
        print(f"❌ Erro ao ler dados do painel: {erro}")

if __name__ == "__main__":
    exibir_painel_eficiencia()