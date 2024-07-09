class Dir:
    name = ""
    subdirs = []
    leaves = []
    def __init__(self, name):
        self.name = name

class LeafFile:
    id = ""
    name = ""
    title = ""
    template = ""
    filetype = ""
    def __init__(self, id, name, title, template):
        self.id = id
        self.name = name
        self.title = title
        self.template = template
