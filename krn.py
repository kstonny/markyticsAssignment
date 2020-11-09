import psycopg2
print("Hello World")
db_database = "mtx"
#db_database = config.db_database
db_host = "localhost"
db_port = 5432
db_user = "postgres"
db_password = "krnsng"
schema = "public"
conn = psycopg2.connect(database=db_database, user=db_user, password=db_password,
            host=db_host, port=db_port, options = f'-c search_path={schema}')
pg_connection_object = conn
pg_cursor = pg_connection_object.cursor()
user_insert_query = """INSERT INTO public.user (user_id, user_name) VALUES (%s, %s)"""
pg_cursor.execute(user_insert_query, (100, 'mahesh_1'))
affected_rows = pg_cursor.rowcount
pg_connection_object.commit()
pg_connection_object.close()
print(f"{affected_rows} bye World")
