from group_chords import group_chords
from group_grace_notes import group_grace_notes

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
        result = group_chords(self.elements)
        result = group_grace_notes(result)
        return result

    # todo: offsets, durations etc.

