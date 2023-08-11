import random
import sqlite3

conn = sqlite3.connect('rpg_db.sqlite3')
curs = conn.cursor()

# Iterate over the charactercreator_character table and update each character with a new values for each attribute.
curs.execute("SELECT character_id FROM charactercreator_character")
character_ids = curs.fetchall()
for character_id in character_ids:
    level = random.randint(1, 20)
    curs.execute("UPDATE charactercreator_character SET level = ? WHERE character_id = ?", (level, character_id[0]))
    exp = random.randint(1, 100)
    curs.execute("UPDATE charactercreator_character SET exp = ? WHERE character_id = ?", (exp, character_id[0]))
    strength = random.randint(1, 100)
    curs.execute("UPDATE charactercreator_character SET strength = ? WHERE character_id = ?", (strength, character_id[0]))
    intelligence = random.randint(1, 100)
    curs.execute("UPDATE charactercreator_character SET intelligence = ? WHERE character_id = ?", (intelligence, character_id[0]))
    dexterity = random.randint(1, 100)
    curs.execute("UPDATE charactercreator_character SET dexterity = ? WHERE character_id = ?", (dexterity, character_id[0]))
    wisdom = random.randint(1, 100)
    curs.execute("UPDATE charactercreator_character SET wisdom = ? WHERE character_id = ?", (wisdom, character_id[0]))

# Iterate over the armory_item table and update each item with a new values for each attribute.
curs.execute("SELECT item_id FROM armory_item")
item_ids = curs.fetchall()
for item_id in item_ids:
    value = random.randint(1, 1000)
    curs.execute("UPDATE armory_item SET value = ? WHERE item_id = ?", (value, item_id[0]))
    weight = random.randint(1, 100)
    curs.execute("UPDATE armory_item SET weight = ? WHERE item_id = ?", (weight, item_id[0]))

# Iterate over the armory_weapon table and update each weapon with a new value for power.
curs.execute("SELECT item_ptr_id FROM armory_weapon")
weapon_ids = curs.fetchall()
for weapon_id in weapon_ids:
    power = random.randint(1, 20)
    curs.execute("UPDATE armory_weapon SET power = ? WHERE item_ptr_id = ?", (power, weapon_id[0]))

# Commit the changes to the database.
conn.commit()

# Close connection to the database
conn.close()