import psycopg2


def cadastrar_bolsa_tela():
  try:
    conn = psycopg2.connect(
        dbname="art_tech_db",
        user="postgres",
        password="vania",  # Coloque a senha do seu Postgres local
        host="localhost",
        port="5432",
    )
    cursor = conn.cursor()

    # Dados da Bolsa em Tela (Clutch Bege)
    nome_modelo = "Clutch Bege Tela Plástica"
    tamanho = "M"  # P, M ou G (conforme a constraint CHECK)
    fio_principal_cor = "Fio Náutico NYBC 3mm Bege"
    horas_trabalhadas = 15.00  # 5 dias x 3h/dia
    custo_materiais_calculado = (
        22.69 + 8.00 + 6.00 + 12.00
    )  # Fio + Tela + Forro + Ferragens (R$ 48,69)
    preco_venda_sugerido = 285.00

    query = """
        INSERT INTO producao_bolsas (
            nome_modelo, 
            tamanho, 
            fio_principal_cor, 
            horas_trabalhadas, 
            custo_materiais_calculado, 
            preco_venda_sugerido
        ) VALUES (%s, %s, %s, %s, %s, %s)
        RETURNING id;
        """

    cursor.execute(
        query,
        (
            nome_modelo,
            tamanho,
            fio_principal_cor,
            horas_trabalhadas,
            custo_materiais_calculado,
            preco_venda_sugerido,
        ),
    )

    bolsa_id = cursor.fetchone()[0]
    conn.commit()

    lucro_bruto = preco_venda_sugerido - custo_materiais_calculado
    valor_hora_real = lucro_bruto / horas_trabalhadas

    print("==================================================")
    print(f"✅ BOLSA CADASTRADA COM SUCESSO NO BANCO! (ID: {bolsa_id})")
    print("==================================================")
    print(f"Modelo: {nome_modelo}")
    print(f"Tamanho: {tamanho}")
    print(f"Fio: {fio_principal_cor}")
    print(f"Custo de Materiais: R$ {custo_materiais_calculado:.2f}")
    print(f"Preço Sugerido: R$ {preco_venda_sugerido:.2f}")
    print(f"Lucro Bruto: R$ {lucro_bruto:.2f}")
    print(f"Valor Real da Hora: R$ {valor_hora_real:.2f}/h")
    print("==================================================")

    cursor.close()
    conn.close()

  except Exception as e:
    print(f"❌ Erro ao conectar ou inserir no banco: {e}")


if __name__ == "__main__":
  cadastrar_bolsa_tela()