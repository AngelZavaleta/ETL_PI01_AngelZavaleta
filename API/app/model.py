from sqlalchemy import Table, Column
from sqlalchemy.types import Integer, String
from config import engine, meta

stream_t= Table("stream_df",meta,
            Column("index",Integer),                   #(columna si es int no se declara int)
            Column("kind",String(30)),	                #(columna con el mismo valor de string)
            Column("title",String(200)),
            Column("release_year",Integer),
            Column("platform",String(30)),
            Column("dur_min",Integer),
            Column("dur_temp",String(30))
            )	

genre_t= Table("genre",meta,
            Column("index",Integer),                 #(clumna si es int no se declara int)
            Column("listed_in",String(1100))	          #(columna con el mismo valor de string)
            )

actors_t= Table("actors",meta,
            Column("index",Integer),               #(clumna si es int no se declara int)
            Column("cast",String(1100))	            #(columna con el mismo valor de string)
            )	

meta.create_all(engine)