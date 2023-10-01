import pandas as pd
from fastapi import FastAPI 
from pydantic import BaseModel

# Cambiar las rutas de archivo a la carpeta de datos
reviews = pd.read_csv("data/Merge_reviews_items.csv")
sentiment = pd.read_csv("data/sentiment.csv")
UserNot = pd.read_csv("data/UserNot.csv")
PlayTimeGenero=pd.read_parquet("data/PlayTimeGenre.parquet")
UserForGenero=pd.read_csv("data/UserForGenero.csv")

app = FastAPI()

@app.get("/playtime_genre/{genero}")
async def playtime_genre(genero: str):
    try:
        filtered_df = PlayTimeGenero[PlayTimeGenero['genres'].str.contains(genero, case=False, na=False)]

        if filtered_df.empty:
            return {"mensaje": f"No se encontraron registros para el género '{genero}'"}

        max_playtime_year = filtered_df.groupby('release_date')['playtime_forever'].sum().idxmax()

        result = {
            f"Año de lanzamiento con más horas jugadas para el género {genero}": int(max_playtime_year)
        }

        return result
    except Exception as e:
        # Registro de errores
        print(f"Error en la función playtime_genre: {e}")
        return {"mensaje": "Ocurrió un error interno en el servidor"}
    
    
 # UserForGenre
@app.post("/user_for_genre/")
async def user_for_genre(genero: str):
    # Filtrar el DataFrame por el género deseado
    df_genero_filtrado = UserForGenero[UserForGenero['genres'].str.contains(genero, case=False)]
    
    if df_genero_filtrado.empty:
        return {"message": f"No se encontraron registros para el género '{genero}'"}
    
    # Agrupar por usuario, año y sumar las horas jugadas
    df_agrupado = df_genero_filtrado.groupby(['user_id', 'posted'])['playtime_forever'].sum().reset_index()
    
    # Agrupar por año y sumar las horas para el mismo año
    df_agrupado_anio = df_agrupado.groupby('posted')['playtime_forever'].sum().reset_index()
    
    # Encontrar al usuario con más horas jugadas para el género
    max_user = df_agrupado.loc[df_agrupado.groupby(['user_id', 'posted'])['playtime_forever'].idxmax()]
    
    # Crear la lista de acumulación de horas jugadas por año
    horas_por_anio = [{"Año": año, "Horas": horas} for año, horas in zip(df_agrupado_anio['posted'], df_agrupado_anio['playtime_forever'])]
    
    return {
        "Usuario con más horas jugadas para Género " + genero: max_user['user_id'].values[0],
        "Horas jugadas por año": horas_por_anio
    }


# UserReccomend
@app.get("/users_recommend/{year}")
async def users_recommend(year: int):
    # Filtrar el DataFrame por el año y las condiciones de recomendación y sentimiento
    filtro = (reviews['posted'] == year) & (reviews['recommend'] == True) & (reviews['sentiment_analysis'] >= 0)
    juegos_recomendados = reviews[filtro]

    # Verificar si hay datos para el año especificado
    if juegos_recomendados.empty:
        return {"mensaje": "Año no encontrado"}

    # Contar la cantidad de reseñas por juego
    juegos_count = juegos_recomendados['app_name'].value_counts()

    # Obtener los tres juegos más recomendados
    top_3_juegos = juegos_count.head(3)

    # Crear una lista de resultados en el formato deseado
    resultado = []
    for puesto, juego in enumerate(top_3_juegos.index, 1):
        resultado.append({f"Puesto {puesto}": juego})

    return resultado

# UserNotRecommended
@app.get("/users_not_recommend/{year}")
async def users_not_recommend(year: int):
    # Obtiene los años únicos disponibles en la columna 'posted'
    años_disponibles = UserNot['posted'].unique()

    # Verifica si el año proporcionado está en la lista de años disponibles
    if year not in años_disponibles:
        return {"mensaje": "Año no encontrado"}

    # Filtrar el DataFrame para el año dado y donde 'recommend' es False
    filtered_df = UserNot[(UserNot['posted'] == year) & (UserNot['recommend'] == False)]

    # Contar la cantidad de juegos menos recomendados para cada juego
    game_counts = filtered_df['app_name'].value_counts()

    # Tomar los 3 juegos menos recomendados
    top_3_least_recommended = game_counts.tail(3)

    # Crear una lista de diccionarios en el formato deseado
    result = [{"Puesto {}".format(i + 1): game} for i, (game, count) in enumerate(top_3_least_recommended.items())]

    return result

# sentimentAnalysis
@app.get("/sentiment-analysis/{year}")
async def analyze_sentiment(year: int):
    # Verificar si el año está presente en el DataFrame
    if year not in sentiment['posted'].astype(int).unique():
        return {"mensaje": "Año no encontrado"}
    
    # Convertir la columna 'posted' a tipo int64 para la comparación
    sentiment['posted'] = sentiment['posted'].astype(int)
    
    # Filtrar el DataFrame para obtener las filas correspondientes al año dado
    year_df = sentiment[sentiment['posted'] == year]
    
    # Calcular la cantidad de registros para cada categoría de sentimiento
    sentiment_counts = year_df['sentiment_analysis'].value_counts().to_dict()
    
    # Crear el diccionario de respuesta
    respuesta = {
        'Negative': sentiment_counts.get(0, 0),  # 0 representa 'Negative'
        'Neutral': sentiment_counts.get(1, 0),   # 1 representa 'Neutral'
        'Positive': sentiment_counts.get(2, 0)   # 2 representa 'Positive'
    }
    
    return respuesta