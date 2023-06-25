POSSIBLE_FILTER = ["name", "create", "modify", "none"]
tad_len = 15


def show_notes(notes_list, filter_tag=POSSIBLE_FILTER[1]):
    if not isinstance(notes_list, list):
        print("ERROR(not array)")
    else:
        if filter_tag not in POSSIBLE_FILTER:
            print("Non available filter! Filter list: " + ', '.join(POSSIBLE_FILTER) + '.')
        else:
            print("NOTE LIST:", end='\n\t')
            if filter_tag == POSSIBLE_FILTER[0]:
                print(*sorted(notes_list, key=lambda note: note.name), sep='\n\t')
            elif filter_tag == POSSIBLE_FILTER[1]:
                print(*sorted(notes_list, key=lambda note: note.date_create), sep='\n\t')
            elif filter_tag == POSSIBLE_FILTER[2]:
                print(*sorted(notes_list, key=lambda note: note.date_modify), sep='\n\t')
            elif filter_tag == POSSIBLE_FILTER[3]:
                print(*notes_list, sep='\n\t')
            print("END")


def show_note(note_dict):
    if not isinstance(note_dict, dict):
        print("ERROR(not dictionary)")
    else:
        print("NAME\n\t" + note_dict.get("name"))
        print("CONTENT\n\t" + note_dict.get("content"))


def show_note_info(note_dict):
    if not isinstance(note_dict, dict):
        print("ERROR(not dictionary)")
    else:
        print("NOTE INFO")
        print("NAME: ".rjust(tad_len) + note_dict.get("name"))
        print("ID: ".rjust(tad_len) + str(note_dict.get("id")))
        print("DATE CREATE: ".rjust(tad_len) + note_dict.get("date_create"))
        print("DATE MODIFY: ".rjust(tad_len) + note_dict.get("date_modify"))
        print("SIZE: ".rjust(tad_len) + str(len(note_dict.get("content"))))
