<h1 align="center"> LABS01-HENRY </h1>
   
![Logo Henry](https://github.com/JLaurencioAJimenez/Proyecto_Final/assets/135534222/fe44e9fe-5dcb-46f1-9812-fd89422e053e)

Link para el deploy de FastAPI: [Ver el deploy](https://proyecto-individual-nz5f.onrender.com/docs)

Puedes encontrar los dataset originales de tipo JSON en este link: [DATASETS](https://drive.google.com/drive/u/1/folders/1h7qqbyEVPYAIcrYumqzSBEzxpRqid_NB)

Puedes encontrar los dataset de tipo CSV o PARQUET creados por mi en este link: [DATASETS](https://drive.google.com/drive/u/1/folders/1i0DYV_MLcuU88pQIa2jLOsVPcLYCG6Om)

Puede encontrar el video aqui: [VIDEO](https://drive.google.com/drive/u/1/folders/1qC5XfTT7slo_V2LQuNdYYCT2aHpR0K7u)

## PASOS REALIZADOS

<h1 align="center"> PASO 1 ETL </h1>

En la carpeta [Limpieza de datos](https://github.com/JLaurencioAJimenez/Proyecto_Final/tree/main/Limpeza%20de%20datos) se puede mirar mas detalladamente como hice la limpieza de datos,
Yo pienso que las funciones usen un dataframe para cada funcion por eso en el archivo [DATASETS](https://drive.google.com/drive/u/1/folders/1i0DYV_MLcuU88pQIa2jLOsVPcLYCG6Om) hay tantos archivos 
creados
Los pasos a realizar fueron

- Abrir cada archivo JSON original
- Filtrar los datos necesarios y eliminar las columnas inecesarias y datos NaN
  - Por que filtre los datos NaN?
  - Ya que mi computadora al no ser muy potente preferia trabajar con datos que fueran utiles
  
- Los datasets estan tanto en repositorio como en [DATASETS](https://drive.google.com/drive/u/1/folders/1i0DYV_MLcuU88pQIa2jLOsVPcLYCG6Om)
- Luego de terminar de filtrar datos y crear cada archivo para cada funcion solicitada en la descripcion del proyecto

  Continue con el paso 2 

<h1 align="center"> PASO 2 EDA </h1>

Consiste en un análisis descriptivo para ver que variables incluir en el sistema de recomendación

para mas informacion sobre el EDA pulsa este [LINK](https://github.com/JLaurencioAJimenez/Proyecto_Final/blob/main/EDA/EDA.ipynb)

- Yo trabaje con un archivo llamado [EDA](https://github.com/JLaurencioAJimenez/Proyecto_Final/blob/main/EDA/EDA.csv)
- Aca se puede observar un resumen estadistico usando .describe

|              | sentiment_analysis | playtime_forever | price  |
|--------------|--------------------|------------------|--------|
| count        | 43,402             | 43,402           | 43,402 |
| mean         | 1.336              | 2,455.331        | 14.620 |
| std          | 0.761              | 6,243.369        | 13.362 |
| min          | 0                  | 0                | 0      |
| 25%          | 1                  | 46               | 9.990  |
| 50%          | 2                  | 229              | 14.620 |
| 75%          | 2                  | 1,005            | 19.990 |
| max          | 2                  | 141,766          | 771.710|

Luego realize algunas tablas pidiendo ciertas caracteristicas como:

-Informacion de barras usando el análisis sentimiento en reviews
![Sentimiento](https://github.com/JLaurencioAJimenez/Proyecto_Final/assets/135534222/af27233f-78ad-4ff6-b0cb-55aa0d1dfa12)

-Tambien cree un grafico de barras donde muestra el precio mas comun en los juegos
![Precio](https://github.com/JLaurencioAJimenez/Proyecto_Final/assets/135534222/034a945c-8d3f-4a32-b39d-57756e93f252)

-Y al final cree una comparativa de barras del genero mas popular
![Genero](https://github.com/JLaurencioAJimenez/Proyecto_Final/assets/135534222/fa873a97-889a-4996-a989-7002295051ca)

Una vez terminado el EDA comenze a realizar el deplpoy de FastAPI

<h1 align="center"> PASO 3 FASTAPI </h1>

Para aprender a usar FastAPI usa el siguiente [link](https://github.com/JLaurencioAJimenez/Proyecto_Final/blob/main/ComoUsarFastAPI.txt)

<h1 align="center"> PASO 4 DEPLOY DE LA API</h1>

Para el deploy de la API necesitamos los documentos que se encuentran en [DATA](https://github.com/JLaurencioAJimenez/Proyecto_Final/tree/main/FastApi/data), tambien necesitaremos a [main.py](https://github.com/JLaurencioAJimenez/Proyecto_Final/blob/main/FastApi/main.py) y a [requirements](https://github.com/JLaurencioAJimenez/Proyecto_Final/blob/main/FastApi/requirements.txt)

Y de esta forma se ve el [deploy](https://proyecto-individual-nz5f.onrender.com/docs)
![image](https://github.com/JLaurencioAJimenez/Proyecto_Final/assets/135534222/4a19182e-4b35-4101-ad6e-e9e22f15e42e)
