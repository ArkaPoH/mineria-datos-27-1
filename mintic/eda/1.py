import pandas as pd
import numpy as np

url = "D:\\Documentos\\proyect unite\\mineria-datos-27-1\\data\\IMDb_Top_700_Movies_2026.csv"
df = pd.read_csv(url)
print(df.head())


#la idea es rellenar lo valores faltantes de un dataframe con la media, mediana o moda de las columnas especificadas.
#como saber si usar la media, mediana o moda? depende del tipo de dato de la columna, si es numerica se puede usar la media o mediana,
# si es categorica se puede usar la moda.
def impute_missing(data, strategy="mean", columns=None):    
	if not isinstance(data, pd.DataFrame):
		raise TypeError("data debe ser un pandas.DataFrame")

	valid_strategies = {"mean", "median", "mode"}
	if strategy not in valid_strategies:
		raise ValueError("strategy debe ser 'mean', 'median' o 'mode'")

	selected_columns = list(data.columns) if columns is None else list(columns)
	missing_columns = [column for column in selected_columns if column not in data.columns]
	if missing_columns:
		raise KeyError(f"Columnas no encontradas: {missing_columns}")

	result = data.copy()
	for column in selected_columns:
		values = result[column]
		if strategy in {"mean", "median"}:
			if not pd.api.types.is_numeric_dtype(values):
				raise TypeError(
					f"La estrategia '{strategy}' requiere una columna numérica: {column}"
				)
			replacement = getattr(values, strategy)()
		else:
			modes = values.mode(dropna=True)
			replacement = modes.iloc[0] if not modes.empty else pd.NA

		result[column] = values.fillna(replacement)

	return result


