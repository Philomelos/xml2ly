from group_chords import group_chords
from group_grace_notes import group_grace_notes
from set_note_attributes import set_note_attributes
from set_measure_list_offsets import set_measure_list_offsets
from resources.musicxml import (
    note,
    backup,
    forward,
    )
from resources.musicxml import direction

class Voice(object):
    pass

class PartMixin(object):

    opening = '{\n'
    closing = '\n } \n'

    @property
    def elements(part):
        result = [] 
        for measure in part.measure[:]:
            for elt in measure.content():
                result.append(elt)
        return result

    @property
    def formatted_elements(self):
        from resources.musicxml import note
        result = []
        for elt in self.grouped_elements():
            if isinstance(elt, note):
                result.append(elt.lilypond_format)
        return ' '.join(result)

    @property
    def parameters(self):
        return (
            self.opening,
            self.formatted_elements,
            self.closing,
            )

    @property
    def lilypond_format(self):
        return ' '.join(self.parameters)

    def grouped_elements(self):
        # adjust all elements
        set_note_attributes(self.measure[:])
        result = group_chords(self.elements)
        result = group_grace_notes(result)
        set_measure_list_offsets(self.measure[:])

        # associate directions + voices
        # print notes
        return result

