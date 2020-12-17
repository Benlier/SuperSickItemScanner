import nbt
import sqlite3
import os
from list_world_items import get_nbt_items


def main(mypet_db_path):
    pet_inventories = dict()
    cursor = sqlite3.connect(mypet_db_path).cursor()
    for row in cursor.execute("select skills from pets"):
        __write_to_file(row[0], 'tempBlob.nbt')
        pet_skills = nbt.nbt.NBTFile('tempBlob.nbt')
        if 'Backpack' in pet_skills:
            pet_inventories.update(get_nbt_items(pet_skills['Backpack']['Items']))
    os.remove('tempBlob.nbt')
    return pet_inventories


def __write_to_file(data, filename):
    # Convert binary data to proper format and write it on Hard Disk
    with open(filename, 'wb') as file:
        file.write(data)



