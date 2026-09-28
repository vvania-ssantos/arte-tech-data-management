import os
import pandas as pd
import psycopg2


def exportar_banco_para_excel_csv():
  try:
    conn = psycopg2.connect(
        dbname="art_tech_db",
        user="postgres",
        password="vania",  # Substitua pela sua senha do Postgres
        host="localhost",
        port="5432",
    )

    query = "SELECT * FROM producao_bolsas ORDER BY id ASC;"
    df = pd.read_sql_query(query, conn)
    conn.close()

    pasta_saida = "dados_exportados"
    os.makedirs(pasta_saida, exist_ok=True)

    caminho_csv = os.path.join(pasta_saida, "acervo_arte_tech.csv")
    caminho_excel = os.path.join(pasta_saida, "acervo_arte_tech.xlsx")

    df.to_csv(caminho_csv, index=False, encoding="utf-8-sig")
    df.to_excel(caminho_excel, index=False, engine="openpyxl")

    print("==================================================")
    print("✅ DADOS EXPORTADOS COM SUCESSO!")
    print("==================================================")
    print(f"📊 Total de peças registradas: {len(df)}")
    print(f"📁 Arquivo CSV salvo em: {caminho_csv}")
    print(f"📗 Arquivo Excel salvo em: {caminho_excel}")
    print("==================================================")

  except Exception as e:
    print(f"❌ Erro ao exportar dados: {e}")


if __name__ == "__main__":
  exportar_banco_para_excel_csv()