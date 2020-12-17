import list_world_items
import pets_inv
import player_inv
from utils import printlisteditems, add_dicts


def main():
    world_folder = '../ThronecraftChapter3'
    mypet_db = '../plugins/MyPet/pets.db'

    all_items = dict()
    print('---Scanning player inventories and enderchests:')
    all_items = add_dicts(all_items, player_inv.main(world_folder + '/playerdata'))
    print('--Scanning MyPet Inventories:')
    all_items = add_dicts(all_items, pets_inv.main(mypet_db))
    print('--Scanning storage objects in the world:')
    all_items = add_dicts(all_items, list_world_items.main(world_folder + '/region', is_valoria=True))

    print('Item entries: ' + str(len(all_items)))
    printlisteditems(all_items)


main()
