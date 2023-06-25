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


def remove_note(notes_list: list, names_list: list):
    found_note = find_notes(notes_list, names_list)

    for note in found_note:
        notes_list.remove(note)


def remove_note_content(notes_list: list, names_list: list):
    found_note = find_notes(notes_list, names_list)

    for note in found_note:
        note.content = ""


def edit_note_content(notes_list: list, name_note: str):
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
