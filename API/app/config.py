from sqlalchemy import create_engine, MetaData

engine = create_engine("mysql+pymysql://root:#soloD1osbasta@host.docker.internal:3306/pi_data05")
meta = MetaData()

