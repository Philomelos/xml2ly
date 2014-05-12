class Chord(object):

    def __init__(self, elements=None):
        self.elements=elements

    @property
    def is_grace(self):
        return any([note.is_grace for note in self.elements])

