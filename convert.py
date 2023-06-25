import json
from Notepad import Notepad


def open_file(file_name):
    new_note_list = []
    with open(file_name + ".json", 'r') as f:
        new_dict_list = json.load(f)

    for note_dict in new_dict_list:
        new_note_list.append(Notepad(
                note_dict.get("name"),
                note_dict.get("content"),
                note_dict.get("id"),
                note_dict.get("date_create"),
                note_dict.get("date_modify")))
    return new_note_list


def save_file(file_name):
    pass
