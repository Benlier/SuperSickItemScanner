import nbt
import sqlite3
import os
from list_world_items import get_nbt_items
from utils import add_dicts


def main(mypet_db_path):
    pet_inventories = dict()
    cursor = sqlite3.connect(mypet_db_path).cursor()
    pet_count = 0
    hundred_count = 0
    for row in cursor.execute("select skills from pets"):
        __write_to_file(row[0], 'tempBlob.nbt')
        pet_skills = nbt.nbt.NBTFile('tempBlob.nbt')
        if 'Backpack' in pet_skills:
            pet_inventories = add_dicts(pet_inventories, get_nbt_items(pet_skills['Backpack']['Items']))

        hundred_count += 1
        if hundred_count >= 100:
            pet_count += hundred_count
            hundred_count = 0
            print(f'Scanned {pet_count} pets')

    os.remove('tempBlob.nbt')
    pet_count += hundred_count
    print(f'Scanned {pet_count} pets in total and found {str(len(pet_inventories))} different items')
    return pet_inventories


def __write_to_file(data, filename):
    # Convert binary data to proper format and write it on Hard Disk
    with open(filename, 'wb') as file:
        file.write(data)



