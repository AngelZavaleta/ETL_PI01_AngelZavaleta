from fastapi import APIRouter
from config import engine
from model import stream_t, genre_t, actors_t
from sqlalchemy import func, select

api_f=APIRouter()


@api_f.get('/get_max_duration', tags=['consultas'])
def get_max_duration(anio:int, plat:str, type:str):
    with engine.connect() as con:
        consulta = con.execute(
            select(stream_t.c.dur_min, stream_t.c.title)
            .where(stream_t.c.platform == plat)
            .where(stream_t.c.release_year == anio)
            .where(stream_t.c.dur_temp == type)
            .order_by(stream_t.c.dur_min.desc())
        )
    return consulta.first()

# Cantidad de películas y series (separado) por plataforma
@api_f.get('/get_count_platform', tags=['consultas'])
def get_count_platform(plat:str):
    with engine.connect() as con:
        consulta = con.execute(select(func.count(stream_t.c.kind), stream_t.c.kind)
            .where(stream_t.c.platform == plat)
            .group_by(stream_t.c.kind)
            
        )
    return consulta.fetchall()

# Cantidad de veces que se repite un género y plataforma con mayor frecuencia del mismo. 
# El request debe ser: get_listedin('genero')
# Como ejemplo de género pueden usar 'comedy', el cuál deberia devolverles un count de 2099 
# para la plataforma de amazon.

@api_f.get('/get_listedin', tags=['consultas'])
def get_listedin(genero:str):
    with engine.connect() as con:
        consulta = con.execute(select(stream_t.c.platform, func.count(stream_t.c.platform))
            .join(stream_t, genre_t.c.index == stream_t.c.index)
            .where(genre_t.c.listed_in == genero)
            .group_by(stream_t.c.platform)
            .order_by(func.count(stream_t.c.platform).desc())
            
        )

    return consulta.first()

# Actor que más se repite según plataforma y año. El request debe ser: get_actor(plataforma, año)

@api_f.get('/get_actor', tags=['consultas'])
def get_actor(anio:int, plat:str):
    with engine.connect() as con:
        consulta = con.execute(select(
                            func.count(actors_t.c.cast),
                            actors_t.c.cast
                        )
                        .join(stream_t, stream_t.c.index == actors_t.c.index)
                        .where(stream_t.c.release_year == anio)
                        .where(stream_t.c.platform == plat)
                        .where(actors_t.c.cast != "sin dato")
                        .group_by(actors_t.c.cast)
                        .order_by(func.count(actors_t.c.cast).desc())
                        
                    )

        return consulta.first()

    