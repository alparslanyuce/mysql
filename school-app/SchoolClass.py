class SchoolClass:
    def __init__(self, id, name, teacherid):
        if id is None:
            self.id = 0
        else:
            self.id = id
        self.name = name
        self.teacherid = teacherid

    @staticmethod
    def createClass(obj):
        class_list = []

        for i in obj:
            class_list.append(SchoolClass(i[0],i[1],i[2]))

        return class_list