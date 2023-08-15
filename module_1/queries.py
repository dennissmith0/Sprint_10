import sqlite3

conn = sqlite3.connect('rpg_db.sqlite3')
curs = conn.cursor()

# Total Characters - count all rows in the character table.
query1 = "SELECT COUNT(*) FROM charactercreator_character;"
curs.execute(query1)
print("Total characters: ", curs.fetchone()[0])

# Total Subclass - count all rows in the necromancer table.
query2 = "SELECT COUNT(*) FROM charactercreator_necromancer;"
curs.execute(query2)
print("Total necromancers: ", curs.fetchone()[0])

# Total Items - count all rows in the items table.
query3 = "SELECT COUNT(*) FROM armory_item;"
curs.execute(query3)
print("Total items: ", curs.fetchone()[0])

# Total Weapons - count all rows in the weapons table.
query4 = "SELECT COUNT(*) FROM armory_weapon;"
curs.execute(query4)
print("Total weapons: ", curs.fetchone()[0])

# Non-Weapons - subtract the count of weapons from the total items.
query5 = "SELECT (SELECT COUNT(*) FROM armory_item) - (SELECT COUNT(*) FROM armory_weapon);"
curs.execute(query5)
print("Non-weapons: ", curs.fetchone()[0])

# Character Items - join the character table with the item table on the character id,
# then group by the character id and count the items. Limit your results to the first 20 rows.
query6 = """
SELECT cc.character_id, COUNT(ai.item_id)
FROM charactercreator_character AS cc
JOIN charactercreator_character_inventory AS cci ON cc.character_id = cci.character_id
JOIN armory_item AS ai ON cci.item_id = ai.item_id
GROUP BY cc.character_id
LIMIT 20;
"""
curs.execute(query6)
print("Items per character (first 20): ", curs.fetchall())

# Character Weapon Count - similar to the previous query,
# but you'll join the character table with the weapon table instead of the item table.
query7 = """
SELECT cc.character_id, COUNT(aw.item_ptr_id)
FROM charactercreator_character AS cc
JOIN charactercreator_character_inventory AS cci ON cc.character_id = cci.character_id
JOIN armory_weapon AS aw ON cci.item_id = aw.item_ptr_id
GROUP BY cc.character_id
LIMIT 20;
"""
curs.execute(query7)
print("Weapons per character (first 20): ", curs.fetchall())

# Character Items Average - To find out on average how many items each character has,
# you'll need to average the counts from the query for CHARACTER_ITEMS.
query8 = """
SELECT AVG(item_count)
FROM (
    SELECT COUNT(ai.item_id) as item_count
    FROM charactercreator_character AS cc
    JOIN charactercreator_character_inventory AS cci ON cc.character_id = cci.character_id
    JOIN armory_item AS ai ON cci.item_id = ai.item_id
    GROUP BY cc.character_id
);
"""
curs.execute(query8)
print("Average items per character: ", curs.fetchone()[0])

# Character Weapons Average - to find out on average how many weapons each character has,
# average the counts from the CHARACTER_WEAPONS query.
query9 = """
SELECT AVG(weapon_count)
FROM (
    SELECT COUNT(aw.item_ptr_id) as weapon_count
    FROM charactercreator_character AS cc
    JOIN charactercreator_character_inventory AS cci ON cc.character_id = cci.character_id
    JOIN armory_weapon AS aw ON cci.item_id = aw.item_ptr_id
    GROUP BY cc.character_id
);
"""
curs.execute(query9)
print("Average weapons per character: ", curs.fetchone()[0])

# Close connection to the database
conn.close()
