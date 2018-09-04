import pandas as pd 
df = pd.read_csv('bd.csv')
print(df.columns)


def extract_names( dff ):
   df1 = dff[['Nombre','Apellido']]
   d = {'id' : range(1,len(dff)+1)}
   df1['id'] = pd.DataFrame(d);
   return df1

df1 = extract_names(df)
print(df1)

def anonimize_csv(dff):
	local = extract_names(dff)
	dff = dff.drop('Nombre',1)
	dff = dff.drop('Apellido',1)
	dff['id'] = local['id']
	return dff

extract_names(df).to_csv('bd_local.csv')
anonimize_csv(df).to_csv('bd_export.csv')