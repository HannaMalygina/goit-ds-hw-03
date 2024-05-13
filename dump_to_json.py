import json

def dump_to_json(input_dict, filename):
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(input_dict, f)
