class Voice(object):
    pass

class PartMixin(object):

    @property
    def music_elements(part):
        result = [] 
        for measure in part.measure[:]:
            for elt in measure.content():
                result.append(elt)
        return result

    @property
    def lilypond_format(self):
        from resources.musicxml import note
        for elt in self.music_elements:
            if isinstance(elt, note):
                print elt.lily_voice, elt.lily_note_type
        return self.id

