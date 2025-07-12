import pandas as pd
import sqlite3



data = {
    'Vendas': [2000, 2000300, 30000, 3000],
    'Vendedor': ['a', 'b', 'c', 'd'],
    'Cidade': ['São Paulo', 'Rio de Janeiro', 'Belo Horizonte', 'Curitiba']
}
df = pd.DataFrame(data)
print("DataFrame original:")
print(df)



conexao = sqlite3.connect('vendas.db')
df.to_sql('tabela_vendas', conexao, if_exists='replace', index=False)



df_db = pd.read_sql('SELECT * FROM tabela_vendas', conexao)
print("\nDados salvos e lidos do banco:")
print(df_db)



print("\nApenas a coluna de Vendas:")
print(df_db['Vendas'])

print("\nLinha com índice 1:")
print(df_db.loc[1])

print("\nLinhas de 1 a 2:")
print(df_db.iloc[1:3])



filtro = df_db[df_db['Vendas'] > 5000]
print("\nFiltrando vendas acima de 5000:")
print(filtro)



df_db['Comissão'] = df_db['Vendas'] * 0.1


df_db.loc[0, 'Vendas'] = 9999


df_db.drop('Cidade', axis=1, inplace=True)

print("\nDataFrame final após manipulação:")
print(df_db)



conexao.close()
