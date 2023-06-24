def find_note(notes_list: list, names_list: list):
    found_note = []

    for note in notes_list:
        if note.name in names_list:
            if note not in found_note:
                found_note.append(note)

    return found_note


def remove_note(notes_list: list, names_list: list):
    found_note = find_note(notes_list, names_list)

    for note in found_note:
        notes_list.remove(note)
