import list_world_items
import pets_inv
import player_inv
from utils import printlisteditems


def main():
    world_folder = '../world'
    mypet_db = '../plugins/MyPet/pets.db'

    all_items = dict()
    print('---Scanning player inventories and enderchests:')
    all_items.update(player_inv.main(world_folder + '/playerdata'))
    print('--Scanning MyPet Inventories:')
    all_items.update(pets_inv.main(mypet_db))
    print('--Scanning storage ojects in the world:')
    all_items.update(list_world_items.main(world_folder + '/region', is_valoria=False))

    print('Item entries: '+ str(len(all_items)))
    printlisteditems(all_items)


main()
