CREATE DATABASE  IF NOT EXISTS `pi_data05`;
USE `pi_data05`;

ALTER TABLE `pi_data05`.`cast` 
CHANGE COLUMN `index` `index` INT NULL DEFAULT NULL ,
CHANGE COLUMN `cast` `cast` VARCHAR(1100) NULL DEFAULT NULL ;

ALTER TABLE `pi_data05`.`cast` 
RENAME TO  `pi_data05`.`actors` ;


ALTER TABLE `genre`
CHANGE COLUMN `index` `index` INT NULL DEFAULT NULL ,
CHANGE COLUMN `listed_in` `listed_in` VARCHAR(1100) NULL DEFAULT NULL ;

ALTER TABLE `stream_df`
CHANGE COLUMN `index` `index` INT NULL DEFAULT NULL ,
CHANGE COLUMN `kind` `kind` VARCHAR(30) NULL DEFAULT NULL ,
CHANGE COLUMN `title` `title` VARCHAR(200) NULL DEFAULT NULL ,
CHANGE COLUMN `release_year` `release_year` INT NULL DEFAULT NULL ,
CHANGE COLUMN `platform` `platform` VARCHAR(30) NULL DEFAULT NULL ,
CHANGE COLUMN `dur_temp` `dur_temp` VARCHAR(30) NULL DEFAULT NULL ;

# Máxima duración según tipo de film (película/serie), por plataforma y por año
SELECT dur_min, title
FROM stream_df
WHERE platform = "hulu" AND release_year = 2018 AND dur_temp = 'min'
ORDER BY dur_min DESC LIMIT 1;

# Cantidad de películas y series (separado) por plataforma (averiguar si van separados)
SELECT COUNT(*) AS 'Cantidad de Peliculas', kind AS 'Type'
FROM stream_df
WHERE platform = 'netflix'
GROUP BY kind;

# Cantidad de veces que se repite un género y plataforma con mayor frecuencia del mismo
SELECT 
    platform, COUNT(listed_in) AS frecuencia_genero
FROM
    stream_df
        INNER JOIN
    genre ON stream_df.index = genre.index
WHERE
    listed_in = 'comedy'
        AND platform = 'amazon'
GROUP BY platform
ORDER BY frecuencia_genero DESC
LIMIT 1;

# Actor que más se repite según plataforma y año.
select cast, COUNT(cast) as frecuencia_actor , platform
from actors
inner join stream_df
on actors.index = stream_df.index
where platform = 'netflix' and release_year = 2018 and cast != 'sin dato'
group by cast
order by frecuencia_actor desc limit 1;


