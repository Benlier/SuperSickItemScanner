from anvil import Region
from anvil import Chunk
from os import listdir
from utils import get_nbt_items


def main(regions_folder: str, is_valoria: bool):
    region_names: [str]
    if is_valoria:
        region_names = __get_valoria_region_names()
    else:
        region_names = __get_local_region_names(regions_folder)

    world_items = __list_world_items(region_names)
    return world_items


def __get_local_region_names(file_path: str):
    local_names = list(filter(lambda x: x.endswith(".mca"), listdir(file_path)))
    region_paths = [file_path + '/' + name for name in local_names]
    return region_paths


def __get_valoria_region_names(file_path: str):
    names = list()
    for x in range(-16, 16):
        for z in range(-16, 16):
            names.append(f'{file_path}/r.{x}.{z}.mca')
    return names


def __list_world_items(region_names: [str]):
    world_items = dict()
    region_amount = str(len(region_names))
    scanned_regions = 0
    for region_name in region_names:
        region = Region.from_file(region_name)
        world_items.update(__list_region_items(region))
        scanned_regions += 1
        print(str(scanned_regions) + "/" + region_amount)
    return world_items


def __list_region_items(region: Region):
    region_items = dict()
    for x in range(32):
        for z in range(32):
            try:
                chunk_items = __list_chunk_items(region.get_chunk(x, z))
                region_items.update(chunk_items)
            except Exception:
                pass
    return region_items


def __list_chunk_items(chunk: Chunk):
    chunk_items = dict()
    for tile_entity in chunk.tile_entities:
        if "Items" in tile_entity:
            entity_items = get_nbt_items(tile_entity['Items'])
            chunk_items.update(entity_items)

    return chunk_items
