def clef_dict():
    clefs = {
        ('G', 2): "treble",
        ('G', 1): "french",
        ('C', 1): "soprano",
        ('C', 2): "mezzosoprano",
        ('C', 3): "alto",
        ('C', 4): "tenor",
        ('C', 5): "baritone",
        ('F', 3): "varbaritone",
        ('F', 4): "bass",
        ('F', 5): "subbass",
        ("percussion", 0): "percussion", 
        # Workaround: MuseScore uses PERC instead of percussion
        ("PERC", 0): "percussion",
        ("TAB", 5): "tab",
        }
    return clefs


def octave_modifiers_dict():
    return {
        1: "^8",
        2: "^15",
        -1: "_8",
        -2: "_15"
    }

class ClefMixin(object):

    clef_dict = clef_dict()
    octave_modifiers_dict = octave_modifiers_dict()

    @property
    def clef_line(self):
        return self.line or 0

    @property
    def clef_number(self):
        return self.number or 1

    @property
    def clef_name(self):
        return self.clef_dict.get((self.sign, self.clef_line), 'treble')

    @property
    def octave_modifier(self):
        return self.octave_modifiers_dict.get(self.clef_octave_change, '')

    @property
    def before_note(self):
        print self.clef_name
        return '\n\\clef "{}{}"\n'.format(self.clef_name, self.octave_modifier)

    @property
    def after_note(self):
        return None


class ClefList(object):

    def __init__(self, lily_voice=1, elements=None):
        self.lily_voice=lily_voice
        self.elements=elements

    @property
    def before_note(self):
        result = []
        clef = filter(lambda x: str(x.clef_number) == self.lily_voice, self.elements)
        if clef: 
            result.append(clef[0].before_note)
        return ''.join(result)

    @property
    def after_note(self):
        return None
