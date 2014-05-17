from resources.musicxml import note
from music_data.chord_container import ChordContainer
from part.group_chords import group_chords

class Measure(object):

    def __init__(self, attributes=None, elements=None):
        self.attributes=attributes
        self.elements=elements

    def group_chords(self):
        self.elements = group_chords(self.elements)

    def filter_non_printing_objects(self, objects):
        non_printing = lambda x: x is not None and isinstance(x, (note, ChordContainer))
        return filter(lambda x: non_printing(x), objects)

    @property
    def lilypond_format(self):
        result = self.filter_non_printing_objects(self.elements)
        return ' '.join([x.lilypond_format for x in result])

    def copy(self):
        copy = Measure()
        for var in vars(self):
            setattr(copy, var, getattr(self, var))
        return copy
