<p align=center><img src=https://d31uz8lwfmyn8g.cloudfront.net/Assets/logo-henry-white-lg.png><p>

# <h1 align=center> **PROYECTO INDIVIDUAL Nº1** </h1>

# <h1 align=center>**`Data Engineering`**</h1>

<p align="center">
<img src="https://blog.indicium.tech/content/images/2020/12/etl-processo.png"  height=300>
</p>



<hr>  



Mi nombre es Angel Zavaleta, este es mi primer proyecto de ETL para SoyHenry.



## **Propuesta de trabajo**

El proyecto consiste en realizar una ingesta de datos desde diversas fuentes, posteriormente aplicar las transformaciones que se consideren pertinentes, y luego disponibilizar los datos limpios para su consulta a través de una API. Esta API se construirá en un entorno virtual dockerizado.

Los datos fueron provistos en archivos de diferentes extensiones, como csv o json. Se espera un EDA para cada dataset y se corrijan los tipos de datos, valores nulos y duplicados, entre otras tareas. Posteriormente, se relacionan los datasets y así poder acceder a su información por medio de consultas a la API.

## **Tecnologias usadas**

+ Python

+ Mysql
  
+ FastApi

+ Docker
 

<p align="center">
<img src="https://blog.logrocket.com/wp-content/uploads/2022/10/fast-api-docker-containers.png"  height=400>  
</p>  
  


Se genera una conexion con MySQL para hacer consultas y se traen de vuelta a VisutalStudioCode (VSC). Así se dockerizan e importan a fastAPI.
En main.py se generan la conexiones con uvicorn y otros archivos.
En config.py se genera la conexion con MySQL. 
En model.py se TIENE que igualar la informacion con MySQL(WorkBench).
en router.py se hacen las consultas.


## **Conclusión.** 

El EDA (ETL) tiene como base el criterio de la persona que analiza la informacion entregada y poder hacer uso de herramientas (pandas, sqlalchemy, etc...) para optimizar la limpieza de los archivos(datos),y al fin y al cabo, poder realizar un analisis de calidad.


<p align="center">
<img src="https://media.tenor.com/W9_8dfFmyr0AAAAM/pixel-game.gif"  height=400>  
</p># ETL_PI01_AngelZavaleta
