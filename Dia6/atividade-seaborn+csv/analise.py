import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd


df = pd.read_csv("Dia6/atividade-seaborn+csv/dadosParaAnalise.csv")

media_vendas = df['Vendas'].mean()
print("medias vendas",media_vendas)

maior_venda= df.loc[df["Vendas"].idxmax()]
print("maior venda", maior_venda)


menor_venda= df.loc[df["Vendas"].idxmin()]
print("menor venda", menor_venda)

plt.figure(figsize=(10,7))
sns.lineplot(x = "Mes",y= "Vendas",data=df,marker = 'o',linewidth=1.5)

plt.title("analise de vendas", fontsize = 15, pad = 20)
plt.xlabel("meses de venda", fontsize= 12)
plt.ylabel("Vendas", fontsize=12)
plt.grid(True,linestyle =":",alpha = 0.7)


for i, row in df.iterrows():
    plt.text(row['Meses'], row['Vendas'], f'R${ row['Vendas'] }',
        ha = 'center', va = 'top', bbox = dict(facecolor = 'black', alpha = 0.5), fontsize = 15, color = 'yellow')

plt.tight_layout()

plt.xticks(rotation = 30)



plt.show()