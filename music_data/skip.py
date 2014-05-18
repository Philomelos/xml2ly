from fractions import Fraction
from music_data.note import fraction_to_lily_string

class Skip(object):

    def __init__(self, duration):
        self.duration=duration

    @property
    def duration_as_fraction(self):
        return self.duration

    @property
    def lilypond_format(self):
        result = fraction_to_lily_string(Fraction(self.duration))
        return '\\skip{}'.format(result) 
