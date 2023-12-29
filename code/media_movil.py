
def calcular_estocastico(data, periodo=14, n1=3, n2=3):
    '''
    Función que recibe un dataframe con la información OLHC y calcula los indicadores estocásticos, que los devuelve en
    nuevas columnas del dataframe
    '''
    data['maximo'] = data['high'].rolling(window=periodo).max()
    data['minimo'] = data['low'].rolling(window=periodo).min()

    # Calcular el %K estocástico
    data['K'] = ((data['close'] - data['minimo']) / (data['maximo'] - data['minimo'])) * 100

    # Calcular el %D estocástico (media móvil del %K)
    data['SK'] = data['K'].rolling(window=n1).mean()
    data['SD'] = data['SK'].rolling(window=n2).mean()
    return data


