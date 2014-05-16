from part.group_chords import group_chords

class Measure(object):

    def __init__(self, attributes=None, elements=None):
        self.attributes=attributes
        self.elements=elements

    def group_chords(self):
        self.elements = group_chords(self.elements)

    def filter_non_printing_objects(self, objects):
        return filter(lambda x: x is not None, objects)

    @property
    def lilypond_format(self):
        result = [x.lilypond_format for x in self.elements]
        result = self.filter_non_printing_objects(result)
        return ' '.join(result)

    def copy(self):
        copy = Measure()
        for var in vars(self):
            setattr(copy, var, getattr(self, var))
        return copy
