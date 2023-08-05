from sqlalchemy import create_engine, MetaData

engine = create_engine("mysql+pymysql://root:12345@localhost:3306/IntranetAirRey")

# conn = engine.connect()

meta_data = MetaData()

