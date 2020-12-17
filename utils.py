def get_nbt_items(items):
    entity_items = dict()
    for item in items:
        count = item['Count']
        item_id = str(item['id'])
        if "tag" in item:
            if "display" in item['tag']:
                if 'Name' in item['tag']['display']:
                    item_id += str(item['tag']['display']['Name'])
            if "BlockEntityTag" in item['tag']:
                if 'Items' in item['tag']['BlockEntityTag']: # Shulker boxes for example
                    nested_items = get_nbt_items(item['tag']['BlockEntityTag']['Items'])
                    entity_items.update(nested_items)

        if entity_items.get(str(item_id)):
            entity_items[str(item_id)] = entity_items[str(item_id)] + int(str(count))
        else:
            entity_items[str(item_id)] = int(str(count))
    return entity_items


def printlisteditems(itemlist: dict[str, str]):
    with open('itemList.txt', 'w', encoding='utf8') as f:
        for item in itemlist:
            f.write(item + " = " + str(itemlist[item]) + "\n")
