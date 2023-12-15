import pandas as pd
from sqlalchemy import create_engine

user="dbadmin"
password="1234_HALLO"
host= "localhost"
port= "3306"
database="SMARTPHONE"

# create the engine
engine = create_engine(f"mysql+pymysql://{user}:{password}@{host}:{port}/{database}")

# stage 1 - import read files
df_stage1_bf = pd.read_csv("Data/smartphones_24.11.2023_stage1.csv")
df_stage1_cm = pd.read_csv("Data/smartphones_27.11.2023_stage1.csv")
df_stage1_af = pd.read_csv("Data/smartphones_04.12.2023_stage1.csv")

# stage 1 - load files into table
df_stage1_bf.to_sql('stage1', con=engine, if_exists='replace', index=False)
df_stage1_cm.to_sql('stage1', con=engine, if_exists='append', index=False)
df_stage1_af.to_sql('stage1', con=engine, if_exists='append', index=False)

# stage 1 - print result
result_stage1 = pd.read_sql("""SELECT * FROM stage1;""", con=engine)
print("Stage 1 - Anzahl der Datensätze: " + str(len(result_stage1)))
print(result_stage1.head().to_string())


# stage 2 - read file
df_stage2 = pd.read_csv("Data/smartphones_stage2.csv")

# stage 2 - load files into table
df_stage2.to_sql('stage2', con=engine, if_exists='replace', index=False)

# stage 2 - print result
result_stage2 = pd.read_sql("""SELECT * FROM stage2;""", con=engine)
print("Anzahl der Datensätze: " + str(len(result_stage2)))
print(result_stage2.head().to_string())


# stage 3 - read file
df_stage3 = pd.read_csv("Data/smartphones_stage3.csv")

# stage 3 - load files into table
df_stage3.to_sql('stage3', con=engine, if_exists='replace', index=False)

# stage 3 - print result
result_stage3 = pd.read_sql("""SELECT * FROM stage3;""", con=engine)
print("Anzahl der Datensätze: " + str(len(result_stage3)))
print(result_stage3.head().to_string())
