# Notepad
Данный блокнот умеет записывать/считывать файлы формата json во внутренний буфер с целью редактирования.
Редактирование заключается в добавлении/удалении/редактировании записи.
* Добавление осуществляется посредством команды ADD со следующими флагами и опциями:
  * ADD - без опций, интерактивное добавление
  * ADD -e - добавить пустую записку в автоматически сгенерированным названием
  * ADD [note_name] - добавить с названием и интерактивным вводом содержания
  * ADD [note_name] [content] - добавить с названием и содержанием
  * ADD -c [content] - добавить с содержанием и интерактивным вводом названия (или автоматически при отсутствии)
* Удаление REMOVE поддерживает выбор записей для удаления:
  * REMOVE [notes_name] - удалить запись/записи с названием
  * REMOVE -c [notes_name] - удалить содержание записи/записией с названием
* Редактирование EDIT записей так же с поддрежкой выбора записи:
  * EDIT [note_name] - дописать содержание в выбранную запись
  * EDIT -r [note_name] - изменить название выбранной записи в интерактивном режиме
  * EDIT -r [note_name] [new_name] - изменить название выбранной записи
  * EDIT -o [note_name] - перезаписать содержание в выбранную запись в интерактивном виде
  * EDIT -o [note_name] [new_content] - перезаписать содержание в выбранную запись
  * EDIT -ro [note_name] [new_name] [new_content] - перезаписать содержание в выбранную запись и изменить название записи
  * EDIT -f [note_name] - полноценное редактирование выбранной записи в специальном отдельном файле
Так же реализован вывод списка записей в открытом блокноте командой SHOW:
* SHOW - показать все записи (название и дата создания) в блокноте
* SHOW [notes_name] - показать название и содержимое всех выбранных записей в блокноте
* SHOW -d [date_start] [date_end] - показать все записи (название и дата создания) в блокноте с выборкой по дате в формате YYYY-MM-DD
* SHOW -i [notes_name] - показать всю информацию обо всех выбранных записей в блокноте (кроме содержания)
* SHOW -f [filter] - показать все записи (название и дата создания) в блокноте с сортировкой по параметру

Командой NEW можно создать новый файл указав имя файла, при этом текущий будет оповещение о необходимости сохранять открытый файл.
Статус текущего файла можно проверить командой STATS.
Команда для выхода EXIT так же дополнительно спросит о необходимости сохранения и выхода из приложения.
Флаги могут ускорить выход:
* EXIT -y - выход из приложения без подтверждения (предупреждение о сохранении файла останется)
* EXIT -s - выход из приложения с сохранением файла (предупреждение о выходе из риложения останется)
* EXIT -n - выход из приложения без сохранения файла (предупреждение о выходе из риложения останется)

Команда SAVE может сохранить копию файла с введённым названием и последующим вопросом о необходимости открыть вновь сохранённый файл

Ввод опций для многих команд реализован интерактивно (не обязательно вводить в команде).

Флаги для многих команд допускается комбинировать, например
* SHOW -di 2023-06-20 2023-06-25 name - покзать подробную информацию о всех записях с 2023-06-20 по 2023-06-25

# BUGS
* возможна ошибка при сохранении файла при введении недопустимого имени файла (отсутсвие обработчика ошибок при введении названия)
