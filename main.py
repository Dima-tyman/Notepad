from modul import *
from Notepad import Notepad
from view import *

# Работа с файлом
# Вывод с выборкой по дате

current_notepad = [
    Notepad("Text", "Some text in more words"),
    Notepad("a", "text"),
    Notepad("b", "new test"),
    Notepad("Test note", "Значимость этих проблем настолько очевидна, что сложившаяся структура организации "
                         "позволяет оценить значение модели развития! Не следует, однако, забывать о том, "
                         "что реализация намеченного плана развития позволяет оценить значение направлений "
                         "прогрессивного развития. Повседневная практика показывает, что постоянное "
                         "информационно-техническое обеспечение нашей деятельности позволяет оценить значение модели "
                         "развития")
]

COMMANDS = ["exit", "show", "add", "remove", "edit", "help"]
FLAGS = {"exit": ['y', 'n', 's'],  # y - not confirm, n - not save, s - save
         "show": ['f', 'i'],  # f - filter, i - info
         "add": ['c', 'e'],  # c - content, e - empty(auto)
         "remove": ['c'],  # c - content
         "edit": ['r', 'o', 'f']  # r - rename, o - overwrite, f - file
         }

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
                    pass  # save
                elif input("Save notes? (y/n): ").lower() in ["y", "yes"]:
                    pass  # save
            print("Buy!")
            break
        else:
            if input("Really exit? (y/n): ").lower() in ["y", "yes"]:
                if not saved:
                    if 'n' in flags:
                        pass
                    elif 's' in flags:
                        pass  # save
                    elif input("Save notes? (y/n): ").lower() in ["y", "yes"]:
                        pass  # save
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
            else:
                remove_note(current_notepad, found_notes)

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
        found_note = find_note(current_notepad, options[0])
        if not found_note:
            print("Note not found!")
            continue

        if 'f' in flags:
            edit_note_content_f(current_notepad, options[0])

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
            found_note.content = options[2]

        elif 'r' in flags or 'o' in flags:
            if len(options) < 2:
                options.append(input("Entry new note name/content: "))
            if not options[1]:
                print("Not found option. Not edit.")
                continue
            if 'r' in flags:
                find_note(current_notepad, options[0]).name = options[1]
            else:
                find_note(current_notepad, options[0]).content = options[1]

        else:
            new_add_content = input("Enter what to add to the content: ") or ""
            found_note.content = found_note.content + new_add_content

        print("Note was edit!")
