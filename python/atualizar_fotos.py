import psycopg2


def atualizar_caminho_fotos():
  try:
    conn = psycopg2.connect(
        dbname="art_tech_db",
        user="postgres",
        password="SUA_SENHA_AQUI",  # Substitua pela sua senha local do Postgres
        host="localhost",
        port="5432",
    )
    cursor = conn.cursor()

    # Atualizando a Clutch Bege (ID 3) com o caminho da foto na pasta images/
    sql_update = """
        UPDATE producao_bolsas 
        SET foto_url = %s 
        WHERE id = %s;
        """

    # Exemplo: definindo o caminho local ou relativo da imagem da Clutch
    cursor.execute(sql_update, ("images/clutch_bege_tela.jpg", 3))

    conn.commit()
    print("==================================================")
    print("✅ FOTO ATUALIZADA COM SUCESSO NO BANCO!")
    print("==================================================")

    cursor.close()
    conn.close()

  except Exception as e:
    print(f"❌ Erro ao atualizar foto no banco: {e}")


if __name__ == "__main__":
  atualizar_caminho_fotos()