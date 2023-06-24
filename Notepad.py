import datetime


class Notepad:

    def __init__(self, name="", content=""):
        date_init = datetime.datetime.now()
        self.id = date_init.__hash__()
        self.date_create = date_init
        self.date_modify = date_init

        if name == "":
            self.name = "Note" + str(self.id)
        else:
            self.name = name

        self.content = content

    def __str__(self):
        return self.name + ' (' + str(self.date_create).split('.')[0] + ')'

    def modify(self, content):
        self.content = content
        self.date_modify = datetime.datetime.now().date()

    def get_dictionary(self):
        return {"id": self.id,
                "name": self.name,
                "content": self.content,
                "date_create": self.date_create,
                "date_modify": self.date_modify}
