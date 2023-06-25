from _datetime import datetime


class Notepad:

    def __init__(self, name="", content="", id=0, date_create="", date_modify=""):
        date_init = datetime.now()

        if id == 0:
            self.id = date_init.__hash__()
        else:
            self.id = id

        if date_create == "":
            self.date_create = date_init
        else:
            self.date_create = datetime.strptime(date_create, '%Y-%m-%d %H:%M:%S.%f')

        if date_modify == "":
            self.date_modify = date_init
        else:
            self.date_modify = datetime.strptime(date_modify, '%Y-%m-%d %H:%M:%S.%f')

        if name == "":
            self.name = "Note" + str(self.id)
        else:
            self.name = name

        self.content = content

    def __str__(self):
        return self.name + ' (' + str(self.date_create).split('.')[0] + ')'

    def modify(self, content):
        self.content = content
        self.date_modify = datetime.now()

    def get_dictionary(self):
        return {"id": self.id,
                "name": self.name,
                "content": self.content,
                "date_create": self.date_create,
                "date_modify": self.date_modify}
