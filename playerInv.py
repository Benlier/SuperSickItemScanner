from os import listdir
import nbt
from nbt.nbt import TAG_Compound
from SuperSickUtils import get_nbt_items


def main(playerdata_folder: str):
    player_file_names = get_local_player_files(playerdata_folder)
    all_player_items = list_players_items(player_file_names)
    return all_player_items


def get_local_player_files(playerdata_folder: str):
    local_files = list(filter(lambda x: x.endswith(".dat"), listdir(playerdata_folder)))
    playerdata_paths = [playerdata_folder + '/' + name for name in local_files]
    return playerdata_paths


def list_players_items(player_files: [str]):
    players_items = dict()
    player_count = str(len(player_files))
    scanned_players = 0

    for player_file in player_files:
        player = nbt.nbt.NBTFile(player_file)
        players_items.update(list_player_items(player))
        scanned_players += 1
        print(str(scanned_players) + "/" + player_count)
    return players_items


def list_player_items(player: TAG_Compound):
    player_items = dict()
    player_items.update(get_nbt_items(player['Inventory']))
    player_items.update(get_nbt_items(player['EnderItems']))
    return player_items
