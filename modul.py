def parse_command(input_command: str):
    command_list = input_command.split()
    command = command_list.pop(0).lower()

    flags = ""
    options = []
    for com in command_list:
        if '-' in com and len(com) > 1:
            flags = flags + com[1:]
        else:
            options.append(com)

    return [command, flags, options]


def modify_list_for_remove(remove_list: list, non_remove_index: str):
    index = non_remove_index.split()
    index_num = []
    for i in index:
        if i.isdigit() and (len(remove_list) >= int(i) > 0):
            index_num.append(int(i) - 1)

    for i in range(len(remove_list) - 1, -1, -1):
        if i not in index_num:
            remove_list.pop(i)


def find_notes(notes_list: list, names_list: list):
    found_notes = []

    for note in notes_list:
        if note.name in names_list:
            if note not in found_notes:
                found_notes.append(note)

    return found_notes


def find_note(notes_list: list, name_note: str):
    for note in notes_list:
        if note.name == name_note:
            return note


def remove_note(notes_list_src: list, notes_list_rem: list):
    for note in notes_list_rem:
        notes_list_src.remove(note)


def remove_note_content(notes_list_rem: list):
    for note in notes_list_rem:
        note.content = ""


def edit_note_content_f(notes_list: list, name_note: str):
    found_note = find_note(notes_list, name_note)
    if found_note:
        with open("edit.txt", 'w') as f:
            f.write(found_note.content)
        if input("Open file edit.txt and edit content.\nSave content? (y): ").lower() == 'y':
            with open("edit.txt", 'r') as f:
                found_note.content = f.read()
        with open("edit.txt", 'w') as f:
            f.write("")
    else:
        print("Note not found!")
