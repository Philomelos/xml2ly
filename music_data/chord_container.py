class ChordContainer(object):

    opening = '<'
    closing = '>'

    def __init__(self, elements=None):
        self.elements=elements

    @property
    def is_grace(self):
        return any([note.is_grace for note in self.elements])

    @property
    def is_slashed(self):
        return self.elements[0].is_slashed

    @property
    def duration_as_fraction(self):
        return self.elements[0].duration_as_fraction

    @property
    def time_modification_as_fraction(self):
        return self.elements[0].time_modification_as_fraction

    @property
    def pitches(self):
        result = []
        for note in self.elements:
            result.append(note.pitch.lilypond_format)
        return ' '.join(result)

    @property
    def format_contributions(self):
        return self.elements[0].format_contributions

    @property
    def duration(self):
        return self.elements[0].duration_string

    @property
    def before_note(self):
        return self.elements[0].b

    @property
    def lilypond_format(self):
        result = []

        for elt in self.format_contributions:
            if elt is not None and elt.before_note is not None:
                result.append(elt.before_note)

        result.append(self.opening)
        result.append(self.pitches)
        result.append(self.closing)
        result.append(self.duration)

        for elt in self.format_contributions:
            if elt is not None and elt.after_note is not None:
                result.append(elt.after_note)

        return ''.join(result)

    @property
    def voice(self):
        return self.elements[0].lily_voice or 1

    @property
    def measure_offset(self):
        return self.elements[0].measure_offset

    @measure_offset.setter
    def measure_offset(self, value):
        self.elements[0].measure_offset = value
