import psycopg2

def precificar_com_realidade():
    print("--- 💸 ARTE-TECH: PRECIFICAÇÃO REALISTA DE MERCADO ---")
    
    id_bolsa = 1
    
    try:
        # 1. Conecta ao banco para buscar as horas reais gastas
        conexao = psycopg2.connect(
            host="localhost", database="art_tech_db", user="postgres", password="vania"
        )
        cursor = conexao.cursor()
        
        cursor.execute("SELECT nome_modelo, horas_trabalhadas FROM producao_bolsas WHERE id = %s;", (id_bolsa,))
        bolsa = cursor.fetchone()
        nome_modelo, horas_reais = bolsa[0], float(bolsa[1])
        
        print(f"Bolsa selecionada: {nome_modelo}")
        print(f"Tempo real gasto: {horas_reais} horas\n")
        
        # 2. Inputs da realidade do negócio
        custo_materiais = float(input("Qual o custo total dos materiais (linha, tela, alça, forro) em R$? "))
        preco_venda_alvo = float(input("Por quanto você quer vender essa bolsa no mercado atual (R$)? "))
        
        # 3. Engenharia Reversa dos Dados
        lucro_bruto_total = preco_venda_alvo - custo_materiais
        
        # Quanto sobrou para pagar a sua hora de trabalho neste cenário de mercado?
        valor_hora_real = lucro_bruto_total / horas_reais if horas_reais > 0 else 0
        
        print("\n--- 📊 RELATÓRIO DE VIABILIDADE FINANCEIRA ---")
        print(f"Preço de Venda Definido: R$ {preco_venda_alvo:.2f}")
        print(f"Custo de Materiais: R$ {custo_materiais:.2f}")
        print(f"Lucro Bruto que fica na empresa: R$ {lucro_bruto_total:.2f}")
        print(f"Valor real pago por hora de trabalho: R$ {valor_hora_real:.2f}/h")
        print("---------------------------------------------")
        
        # 4. Grava os dados finais no PostgreSQL para seu portfólio e histórico
        sql_update = """
            UPDATE producao_bolsas 
            SET custo_materiais_calculado = %s,
                preco_venda_sugerido = %s
            WHERE id = %s;
        """
        cursor.execute(sql_update, (custo_materiais, preco_venda_alvo, id_bolsa))
        conexao.commit()
        
        print("✅ Dados salvos com sucesso no art_tech_db!")
        
        cursor.close()
        conexao.close()
        
    except Exception as erro:
        print(f"❌ Erro no sistema: {erro}")

if __name__ == "__main__":
    precificar_com_realidade();