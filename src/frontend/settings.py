import os
print(os.environ)
port = "5432"
# database = os.environ['DB_NAME']
# username = os.environ['DB_USERNAME']
# password = os.environ['DB_PASSWORD']
database = "files_db"
password = "Asafba123"
username = "hello"
host = "postgres_db"

# Connection string

connection_string = (
    f"postgres://{username}:{password}@{host}:{port}/{database}"
)
