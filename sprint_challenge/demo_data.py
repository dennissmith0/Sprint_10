import sqlite3

# Open a connection to a new database file
conn = sqlite3.connect('demo_data.sqlite3')
curs = conn.cursor()

# Create the table
create_table_query = """
CREATE TABLE demo (
    s TEXT,
    x INT,
    y INT
);
"""
curs.execute(create_table_query)

# Insert the data
insert_data_query = """
INSERT INTO demo (s, x, y)
VALUES
    ('g', 3, 9),
    ('v', 5, 7),
    ('f', 8, 7);
"""
curs.execute(insert_data_query)

# Commit the changes
conn.commit()

# Execute the queries
row_count_query = "SELECT COUNT(*) FROM demo;"
curs.execute(row_count_query)
row_count = curs.fetchall()

xy_at_least_5_query = "SELECT COUNT(*) FROM demo WHERE x >= 5 AND y >= 5;"
curs.execute(xy_at_least_5_query)
xy_at_least_5 = curs.fetchall()

unique_y_query = "SELECT COUNT(DISTINCT y) FROM demo;"
curs.execute(unique_y_query)
unique_y = curs.fetchall()

# Close the cursor and connection
curs.close()
conn.close()

# Print the results
print("Row count:", row_count)
print("Rows where both x and y are at least 5:", xy_at_least_5)
print("Unique values of y:", unique_y)
