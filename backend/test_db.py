import psycopg2

conn = psycopg2.connect(
    host="localhost",
    database="secure_auth_system",
    user="postgres",
    password="Nandini#17"
)

print("Database Connected Successfully!")

conn.close()
