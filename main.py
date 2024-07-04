import os
import psycopg2
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def get_total_records():
    try:
        database_url = os.getenv("DATABASE_URL")

        connection = psycopg2.connect(database_url)

        cursor = connection.cursor()

        query = f"SELECT COUNT(*) FROM customers;"
        cursor.execute(query)

        total_records = cursor.fetchone()[0]
        print(f"The total number of customers is: {total_records}")

    except (Exception, psycopg2.Error) as error:
        print(f"Error connecting to PostgreSQL: {error}")

    finally:
        if connection:
            cursor.close()
            connection.close()
            print("PostgreSQL connection closed.")
