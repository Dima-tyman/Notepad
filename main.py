from modul import *
from view import *
from convert import *

# Вывод с выборкой по дате


def open_file(open_file_name):
    global file_name, current_notepad, saved
    file_name = open_file_name
    current_notepad = open_file_json(open_file_name)
    saved = True
    print("Open new notepad - " + file_name)


def new_file(new_file_name):
    global file_name, current_notepad, saved
    file_name = new_file_name
    current_notepad.clear()
    saved = False
    print("New notepad - " + file_name)


COMMANDS = ["exit", "show", "add", "remove", "edit", "open", "save", "new", "status"]
FLAGS = {"exit": ['y', 'n', 's'],  # y - not confirm, n - not save, s - save
         "show": ['f', 'i'],  # f - filter, i - info
         "add": ['c', 'e'],  # c - content, e - empty(auto)
         "remove": ['c'],  # c - content
         "edit": ['r', 'o', 'f']  # r - rename, o - overwrite, f - file
         }

current_notepad = []
file_name = "new"
saved = True


print("Welcome to Notepad!")
print("Command list:", ', '.join(COMMANDS))

while True:

    command = ""
    flags = ""
    options = []

    input_command = input("Enter command: ").strip()
    if not input_command:
        continue
    if ' ' in input_command:
        parsed_command = parse_command(input_command)
        command = parsed_command[0]
        flags = parsed_command[1]
        options = parsed_command[2]
    else:
        command = input_command.lower()

    # EXIT - exit with confirm and check save notepad
    # -y - not confirm exit (no if file not saved!)
    # -n - not save (if file not saved)
    # -s - auto save (if file not saved)

    if command == COMMANDS[0]:
        if 'y' in flags:
            if not saved:
                if 'n' in flags:
                    pass
                elif 's' in flags:
                    save_file_json(file_name, current_notepad)
                elif input("Save notes? (y/n): ").lower() in ["y", "yes"]:
                    save_file_json(file_name, current_notepad)
            print("Buy!")
            break
        else:
            if input("Really exit? (y/n): ").lower() in ["y", "yes"]:
                if not saved:
                    if 'n' in flags:
                        pass
                    elif 's' in flags:
                        save_file_json(file_name, current_notepad)
                    elif input("Save notes? (y/n): ").lower() in ["y", "yes"]:
                        save_file_json(file_name, current_notepad)
                print("Buy!")
                break

    # SHOW - show all notes
    # SHOW [notes_name] - show selected notes_name
    # -i [notes_name] - show info selected notes_name
    # -f [filter] - show all notes with filter

    elif command == COMMANDS[1]:
        if 'f' not in flags:
            if not options:
                show_notes(current_notepad)
            else:
                found_note = find_notes(current_notepad, options)
                if not found_note:
                    print("Note not found!")
                if 'i' in flags:
                    for note in found_note:
                        show_note_info(note.get_dictionary())
                else:
                    for note in found_note:
                        show_note(note.get_dictionary())
        elif 'f' in flags:
            if not options:
                print("Not filter! Filter list: " + ', '.join(POSSIBLE_FILTER) + '.')
            else:
                show_notes(current_notepad, options[0])

    # ADD - add new note full interactive
    # ADD [note_name] - add new note with note_name and interactive content
    # ADD [note_name] [content] - add new note with note_name and content
    # -c [content] - add new note with content and interactive name
    # -e - add new note without content and with auto name

    elif command == COMMANDS[2]:
        new_note_name = ""
        new_note_content = ""

        if 'e' in flags:
            pass

        elif not options:
            new_note_name = input("Enter name for new note: ").strip()
            if not new_note_name:
                print("You entered empty name. The name is generated automatically!")
            new_note_content = input("Enter content for new note:\n")

        elif len(options) == 1:
            if 'c' in flags:
                new_note_name = input("Enter name for new note: ").strip()
                if not new_note_name:
                    print("You entered empty name. The name is generated automatically!")
                new_note_content = options[0]
            else:
                new_note_name = options[0]
                new_note_content = input("Enter content for new note:\n")

        elif len(options) > 1:
            new_note_name = options[0]
            new_note_content = '\n'.join(options[1:])

        current_notepad.append(Notepad(new_note_name, new_note_content))
        print("Added new note " + '"' + current_notepad[-1].name + '"!')
        saved = False

    # REMOVE [notes_name] - remove notes with notes_name
    # -c [notes_name] - remove content at notes_name

    elif command == COMMANDS[3]:
        if not options:
            options.extend(input("Entry note name for remove: ").split())
        if options:
            found_notes = find_notes(current_notepad, options)
            if len(found_notes) > len(options):
                show_notes(found_notes)
                note_index = input("Enter nums notes for remove (sep 'space'): ")
                modify_list_for_remove(found_notes, note_index)
            if 'c' in flags:
                remove_note_content(found_notes)
                saved = False
            else:
                remove_note(current_notepad, found_notes)
                saved = False

    # EDIT [note_name] - edit note with note_name
    # -r [note_name] - new interactive name at note_name
    # -r [note_name] [new_name] - new name at note_name with new_name
    # -o [note_name] - new interactive content at note_name
    # -o [note_name] [new_content] - new content at note_name with new_content
    # -ro [note_name] [new_name] [new_content] - **
    # -f [note_name] - edit content note_name in file

    elif command == COMMANDS[4]:
        if not options:
            options.append(input("Entry note name: ").strip())
        if not options[0]:
            print("Not found option. Not edit.")
            continue

        found_notes = find_notes(current_notepad, options)
        if not found_notes:
            print("Note not found!")
            continue
        elif len(found_notes) > 1:
            show_notes(found_notes)
            note_index = input("Enter num note for edit: ")
            if not note_index.isdigit():
                print("You didn't enter a number!")
                continue
            note_index = int(note_index) - 1
            if note_index in range(0, len(found_notes)):
                found_note = found_notes[note_index]
            else:
                print("Num note not fount!")
                continue
        else:
            found_note = found_notes[0]

        if 'f' in flags:
            edit_note_content_f(found_note)

        elif 'r' in flags and 'o' in flags:
            if len(options) < 2:
                options.append(input("Entry new note name: ").strip())
                if not options[1]:
                    print("Not found option. Not edit.")
                    continue
                options.append(input("Entry new note content: ")) or ""
            if len(options) < 3:
                options.append("")
                options[2] = input("Entry new note content: ")
            found_note.name = options[1]
            found_note.modify(options[2])

        elif 'r' in flags or 'o' in flags:
            if len(options) < 2:
                options.append(input("Entry new note name/content: "))
            if not options[1]:
                print("Not found option. Not edit.")
                continue
            if 'r' in flags:
                found_note.name = options[1]
            else:
                found_note.modify(options[1])

        else:
            new_add_content = input("Enter what to add to the content: ") or ""
            found_note.modify(found_note.content + new_add_content)

        print("Note was edit!")
        saved = False

    # OPEN [file_name] - open new notepad

    elif command == COMMANDS[5]:
        if not options:
            options.append(input("Entry file name: ").strip())
        if not options:
            print("Not file name!")
            continue

        if not saved:
            if input("Save current file? (n - no): ").lower() == 'n':
                open_file(options[0])
            else:
                save_file_json(file_name, current_notepad)
                open_file(options[0])
        else:
            open_file(options[0])

    # SAVE [file_name] - save as file_name
    # SAVE - save in current file (if is)

    elif command == COMMANDS[6]:
        if not options:
            save_file_json(file_name, current_notepad)
            saved = True
        else:
            save_file_json(options[0], current_notepad)
            saved = True
            if input("Open new file? (y -yes): ").lower() == 'y':
                open_file(options[0])

    # NEW [file_name] - create for edit new notepad

    elif command == COMMANDS[7]:
        if not options:
            options.append(input("Entry file name: ").strip())
        if not options:
            print("Not file name!")
            continue
        if saved:
            new_file(options[0])
        else:
            if input("Save current file? (n - no): ").lower() == 'n':
                new_file(options[0])
            else:
                save_file_json(file_name, current_notepad)
                new_file(options[0])

    # STATUS - show current file and saved status

    elif command == COMMANDS[8]:
        print("FILE - " + file_name, end='')
        if saved:
            print(" (SAVE)")
        else:
            print(" (NOT SAVE)")