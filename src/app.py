import os
import duckdb

S3URI = os.environ.get('S3URI')

con = duckdb.connect()
con.execute("""
INSTALL httpfs;
LOAD httpfs;

CREATE SECRET (
      TYPE S3,
      PROVIDER CREDENTIAL_CHAIN
);
""")

def lambda_handler(event, context):
    req = con.sql(f"SELECT * FROM read_csv('{S3URI}') LIMIT 3")
    print(req)
