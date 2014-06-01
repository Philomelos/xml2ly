from resources.musicxml import note
from music_data.chord_container import ChordContainer
from music_data.skip import Skip
from part.group_chords import group_chords
from time_signature import TimeSignature

class Measure(object):

    def __init__(self, attributes=None, elements=None):
        self.attributes=attributes
        self.elements=elements

    def group_chords(self):
        self.elements = group_chords(self.elements)

    @property
    def beats(self):
        try:
            return int(self.attributes[0].time[0].beats[0])
        except:
            return None

    @property
    def beat_type(self):
        try:
            return int(self.attributes[0].time[0].beat_type[0])
        except:
            return None

    @property
    def time_signature(self):
        beats, beat_type = self.beats, self.beat_type
        if beats and beat_type:
            return TimeSignature(beats, beat_type)

    @property
    def key_signature(self):
        try:
            return self.attributes[0].key[0]
        except IndexError:
            return None

    def copy(self):
        copy = Measure()
        for var in vars(self):
            setattr(copy, var, getattr(self, var))
        return copy

    @property
    def has_any_durated_element(self):
        from resources.musicxml import note
        from music_data.chord_container import ChordContainer
        return any([isinstance(x, (note, ChordContainer)) for x in self.elements])

    @property
    def printing_elements(self):
        printing = lambda x: isinstance(x, (note, ChordContainer, Skip))
        elements = filter(lambda x: printing(x), self.elements) 
        return elements

    @property
    def lilypond_format(self):
        result = []
        result.append(self.key_signature)
        result.append(self.time_signature)
        result.extend(self.printing_elements)
        result = filter(lambda x: x is not None, result)
        return ''.join([x.lilypond_format for x in result])
