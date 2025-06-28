
import matplotlib.pyplot as plt
import random



vendas  =[1,2,6,9,12,45,89,10,45,78,8] # EIXO  y 
meses  =['jan','fev','mar','abr','mai','jun','jul','ago','set','out','nov'] # EIXO x


plt.xlabel(' MESES')
plt.ylabel('VENDAS')
plt.title('ACUMULO DE VENDAS SEMESTRAIS')
plt.grid(True)

# LINHA***
# plt.plot(meses, vendas,  color='red')
# BARRA***
# plt.bar(meses, vendas,  color='red')
# DISPERSÃO***
plt.scatter(meses, vendas, color='red')
# PIZZA***
# plt.pie(vendas, labels=mes, autopct='%.1f%%')


plt.show()
