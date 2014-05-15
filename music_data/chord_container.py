class ChordContainer(object):

    def __init__(self, elements=None):
        self.elements=elements

    @property
    def is_grace(self):
        return any([note.is_grace for note in self.elements])

    @property
    def lilypond_format(self):
        return '\n %%% chord \n'

    @property
    def voice(self):
        return self.elements[0].lily_voice or 1
