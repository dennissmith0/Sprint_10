import pandas as pd
import sqlite3


url = "https://raw.githubusercontent.com/bloominstituteoftechnology/DS-Unit-3-Sprint-2-SQL-and-Databases/master/module1-introduction-to-sql/buddymove_holidayiq.csv"
df = pd.read_csv(url)
print(df.shape)  # Check the shape of the DataFrame. It should be (249, 7).

conn = sqlite3.connect('buddymove_holidayiq.sqlite3')
df.to_sql('review', conn, if_exists='replace', index=False)

# To count how many rows you have in the table, you can use the SQL COUNT function:
query1 = "SELECT COUNT(*) FROM review;"
curs = conn.cursor()
curs.execute(query1)
print("Total rows: ", curs.fetchone()[0])

# To find out how many users who reviewed at least 100 in the 'Nature' category also reviewed at
# least 100 in the 'Shopping' category, you can use a WHERE clause in your SQL query:
query2 = "SELECT COUNT(*) FROM review WHERE Nature >= 100 AND Shopping >= 100;"
curs.execute(query2)
print("Users who reviewed at least 100 in both Nature and Shopping: ", curs.fetchone()[0])

# For the stretch goal, to find out the average number of reviews for each category,
# you can use the AVG function in SQL:
categories = ['Sports', 'Religious', 'Nature', 'Theatre', 'Shopping', 'Picnic']

for category in categories:
    query = f"SELECT AVG({category}) FROM review;"
    curs.execute(query)
    print(f"Average reviews for {category}: ", curs.fetchone()[0])

conn.close()
