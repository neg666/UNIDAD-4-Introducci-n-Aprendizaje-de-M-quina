import pandas as pd 
df = pd.read_csv('Productos_farmaceuticos_vigentes_venta_directa.csv',encoding = 'latin1',delimiter=';')
print(df.columns)
print("Frecuencias sin truncar")
print(df['Nombre Producto'].value_counts().head(n=15))
def trunc5(x):
	return x[0:5]
def trunc7(x):
	return x[0:7]
def trunc10(x):
	return x[0:10]
t5 = df['Nombre Producto'].apply(trunc5)
t7 = df['Nombre Producto'].apply(trunc7)
t10 = df['Nombre Producto'].apply(trunc10)
print(t5.value_counts().head(n=15))
print(t7.value_counts().head(n=15))
print(t10.value_counts().head(n=15))