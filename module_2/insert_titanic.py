import psycopg2
import csv
from os import getenv

DBNAME = getenv('DBNAME')
USER = getenv('USER')
PASSWORD = getenv('PASSWORD')
HOST = getenv('HOST')

# Connect to your postgres DB
conn = psycopg2.connect(dbname=DBNAME, user=USER, password=PASSWORD, host=HOST)

# Open a cursor to perform database operations
cur = conn.cursor()

# Drop table if it exists
cur.execute("DROP TABLE IF EXISTS titanic;")

# Create the table
cur.execute("""
CREATE TABLE titanic (
    Survived INT,
    Pclass INT,
    Name TEXT,
    Sex TEXT,
    Age REAL,
    SiblingsSpousesAboard INT,
    ParentsChildrenAboard INT,
    Fare REAL
);
""")

# Open and read the CSV file
with open('titanic.csv', 'r') as f:
    reader = csv.reader(f)
    next(reader)  # Skip the header row
    for row in reader:
        cur.execute(
            "INSERT INTO titanic VALUES (%s, %s, %s, %s, %s, %s, %s, %s)",
            row
        )

# Commit changes
conn.commit()

# Close cursor and connection
cur.close()
conn.close()
