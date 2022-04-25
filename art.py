import os
import json
import random
import shutil

AMOUNT = 0000
SOURCE = "build"

IPFS = "ipfs://PATH/"
OUTCOME = "shuffled_assets"
NAME = "Collection Name"
pre_selected_src_indices = []

if not os.path.exists('shuffled_assets/images'):
    os.makedirs('shuffled_assets/images')

if not os.path.exists('shuffled_assets/json'):
    os.makedirs('shuffled_assets/json')

src_indices = [n for n in range(0,AMOUNT) if n not in pre_selected_src_indices]
src_indices = pre_selected_src_indices + src_indices

pre_selected_dest_indices = [n for n in range(0, len(pre_selected_src_indices))]
dest_indices = [n for n in range(len(pre_selected_src_indices),AMOUNT)]
random.shuffle(dest_indices)
dest_indices = pre_selected_dest_indices + dest_indices

for index in range(0, AMOUNT):
    try:        
        src_img = f"{SOURCE}/{src_indices[index]}.png"
        dest_img = f"{OUTCOME}/images/{dest_indices[index]}.png"
        shutil.copy(src_img, dest_img)
        
        src_json = f"{SOURCE}/{src_indices[index]}.json"
        dest_json = f"{OUTCOME}/json/{dest_indices[index]}.json"
        shutil.copy(src_json, dest_json)
        
        file = open(f"{OUTCOME}/json/{dest_indices[index]}.json", "r")
        json_object = json.load(file)
        file.close()
        
        json_object["name"] = f"{NAME} #{dest_indices[index]}"
        json_object["description"] = f"PUT IN YOUR DESCRIPTION"
        json_object["image"] = f"{IPFS}{dest_indices[index]}.png"
        json_object["edition"] = dest_indices[index]
        
        file = open(f"{OUTCOME}/json/{dest_indices[index]}.json", "w")
        json.dump(json_object, file, ensure_ascii=False, indent=4)
        file.close()
        print("done")
    except Exception as e:
        print(e)
        pass
