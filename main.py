from modul import *
from Notepad import Notepad
from view import *

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

print("Welcome to Notepad!")
print("Current command:", ', '.join(COMMANDS))

while True:
    print("Enter command: ", end='')

    input_command = input().split()
    command = ""
    options = []
    if input_command:
        command = input_command[0].lower()
        if len(input_command) > 1:
            options = input_command[1:]

    # EXIT - with confirm and check save notepad

    if command == COMMANDS[0]:
        print("Really exit? (y/n): ", end='')
        if input().lower() in ["y", "yes"]:
            print("Buy!")
            break

    # SHOW - all notes in current notepad
    # SHOW [note_name] - selected note

    elif command == COMMANDS[1]:
        if not options:
            show_notes(current_notepad)
        else:
            found_note = find_note(current_notepad, options)
            if not found_note:
                print("Note not found!")
            for note in found_note:
                show_note(note.get_dictionary())

    # ADD - new note in current notepad (interactive)
    # ADD [note_name] - new note with note_name
    # ADD [note_name] [content] - new note with note_name and content

    elif command == COMMANDS[2]:
        new_note_name = ""
        new_note_content = ""
        if not options:
            new_note_name = input("Enter name for new note: ").strip()
            if not new_note_name:
                print("You entered empty name. The name is generated automatically!")
            new_note_content = input("Enter content for new note:\n")

        elif len(options) == 1:
            new_note_name = options[0]
            new_note_content = input("Enter content for new note:\n")

        elif len(options) > 1:
            new_note_name = options[0]
            new_note_content = '\n'.join(options[1:])

        current_notepad.append(Notepad(new_note_name, new_note_content))
        print("Added new note " + '"' + current_notepad[-1].name + '"!')

    # REMOVE [note_name] - note in current notepad with note_name

    elif command == COMMANDS[3]:
        if not options:
            options.extend(input("Entry note name for remove: ").split())
        if options:
            remove_note(current_notepad, options)

    # EDIT [note_name] - note in current notepad with note_name

    elif command == COMMANDS[4]:
        if not options:
            options.extend(input("Entry note name for edit: ").split())
        if options:
            pass
