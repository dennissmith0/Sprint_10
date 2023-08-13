import sqlite3

conn = sqlite3.connect('rpg_db.sqlite3')
curs = conn.cursor()

'''
Query Exercise:
List all characters with a level greater than 10 and sort them by experience points in descending order.

Hint:
To filter the characters with a level greater than 10, you'll want to use the WHERE clause with the appropriate condition.
To sort the results by experience points in descending order, you'll need the ORDER BY clause.

Obstacle:
The charactercreator_character table contains the relevant columns level and exp, each with 0 values.
We used the random module to generate random values for each attribute and update the database.
See update_values.py.
'''

query1 = """SELECT name, level, exp FROM charactercreator_character
            WHERE level > 10
            ORDER BY exp DESC;"""
curs.execute(query1)
print("Characters with level > 10: ", curs.fetchall(), "\n")

'''
Query Exercise:
Find the total value and weight of all items in the armory.

Hint:
You'll want to use the SUM aggregate function to calculate the total valueand weight of the items.
The armory_item table contains the relevant columns value and weight.

Your query should include:
A SELECT clause that applies the SUM function to both the value and weight columns.
A FROM clause that specifies the armory_item table, where the data is stored.

Obstacle:
The armory_item table contains value and weight columns, each with 0 values.
We used the random module to generate random values for each column.
See update_values.py.
'''

query2 = """SELECT SUM(value), SUM(weight) FROM armory_item;"""
curs.execute(query2)
print("Total value and weight of all items in the armory: ", curs.fetchall(), "\n")


'''
Query Exercise:
Join the armory_weapon table with the armory_item table to display the name and power of all weapons.

Hint:
You'll want to use a JOIN operation to combine the armory_weapon table with the armory_item table.
The common column between the two tables is the item_id in armory_item and item_ptr_id in armory_weapon.

Your query should include:
A SELECT clause to specify the columns you want to retrieve, namely the name from armory_item andpower from armory_weapon.
A FROM clause that specifies the main table (e.g., armory_item).
A JOIN operation that combines the armory_item and armory_weapon tables based on the common column.
An ON clause that defines the condition for the join, matching the item_id with item_ptr_id.

Obstacle:
The armory_weapon table contains the item_ptr_id column, which is a foreign key that references the item_id column in the armory_item table.
We used the random module to generate random values for the power column.
See update_values.py.
'''

query3 = """SELECT armory_item.name, armory_weapon.power FROM armory_item
            JOIN armory_weapon
            ON armory_item.item_id = armory_weapon.item_ptr_id;"""
curs.execute(query3)
print("Name and power of all weapons: ", curs.fetchall())


'''
Query Exercise:
Count the number of characters for each level and order by level.

Hint:
You'll want to use the COUNT aggregate function to count the number of characters for each level.
The charactercreator_character table contains the relevant columns.

Your query should include:
A SELECT clause that specifies the level column and applies the COUNT function to count the characters for each level.
A FROM clause that specifies the charactercreator_character table, where the data is stored.
A GROUP BY clause that groups the results by the level column, so you can count the characters for each level.
An ORDER BY clause that orders the results by the level column.
'''
query4 = """SELECT level, COUNT(*) FROM charactercreator_character
            GROUP BY level
            ORDER BY level;"""
curs.execute(query4)
print("Number of characters for each level: ", curs.fetchall(), "\n")


'''
Query Exercise:
Find the average weight of items carried by characters whose level is greater than 10.

Hint:
You'll want to use the AVG aggregate function to calculate the average weight of items.
You'll also need to perform a JOIN operation between the tables that contain character information (charactercreator_character) and item information (charactercreator_character_inventory, armory_item).

Your query should include:
A SELECT clause that applies the AVG function to calculate the average weight of items.
A series of JOIN operations to combine the tables containing character information and item information.
A WHERE clause to filter characters whose level is greater than 10.
Necessary GROUP BY or other clauses to properly structure the query.
'''
query5 = """SELECT AVG(weight) FROM charactercreator_character_inventory
            JOIN armory_item
            ON charactercreator_character_inventory.item_id = armory_item.item_id
            JOIN charactercreator_character
            ON charactercreator_character_inventory.character_id = charactercreator_character.character_id
            WHERE charactercreator_character.level > 10;"""
curs.execute(query5)
print("Average weight of items carried by characters whose level is greater than 10: ", curs.fetchall(), "\n")


'''
Query Exercise:
Join the charactercreator_character table with the charactercreator_character_inventory table to display the total number of items each character has.
'''


'''
Query Exercise:
Join the charactercreator_character table with the charactercreator_character_inventory table to display how many weapons each character has.
'''


# Close connection to the database
conn.close()
