
class Project():

    def __init__(self, name=None, status=None, description=None, id=None, public=None):
        self.name = name
        self.status = status
        self.description = description
        self.id = id
        self.public = public

    def __repr__(self):
        return "%s:%s:%s:%s" % (self.id, self.name, self.description, self.public)

    def __eq__(self, other):
        return self.name == other.name

