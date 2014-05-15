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
from get_staff_type import get_staff_type

def is_note_or_chord(elt):
    from resources.musicxml import note
    from music_data.chord_container import ChordContainer
    return isinstance(elt, note) or isinstance(elt, ChordContainer)

def filter_by_voice_name(measure_list, voice_name):
    from copy import deepcopy
    from measure.measure import Measure
    result = []
    for measure in measure_list:
        elts = measure.elements
        new_measure = measure.copy()
        new_measure.elements = []
        for elt in elts:
            if is_note_or_chord(elt) and elt.voice == voice_name:
                new_measure.elements.append(elt)
        result.append(new_measure)
    voice = Voice(name=voice_name, measures=result)
    return voice
            
from voice import Voice

class PartMixin(object):

    def group_voices(self, measures):

        self.staff_type = get_staff_type(self)

        voice_numbers = []
        for measure in measures:
            for elt in measure.elements:
                if isinstance(elt, note):
                    voice = elt.voice
                    if voice is not None and not voice in voice_numbers:
                        voice_numbers.append(voice)

        voices = []
        for voice_number in voice_numbers:
            voice = filter_by_voice_name(measures, voice_number)
            voice.part = self
            voices.append(voice)

        return voices

    @property
    def part_id(self):
        return self.id

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
        elements = [x.lilypond_format for x in self.extract_voices()]
        result = filter(lambda x: x is not None, elements)
        return ' '.join(result)

    @property
    def parameters(self):
        return (
            self.formatted_elements,
            )

    @property
    def lilypond_format(self):
        return ' '.join(self.parameters)

    # @property
    # def lilypond_score_representation(self):
    #     result = []
    #     result.append(self.staff_type.score_representation)
    #     for voice in self.extract_voices():
    #         result.append(voice.lilypond_score_representation)
    #     result.append(self.staff_type.score_representation_end)
    #     return '\n'.join(result)

    def get_measures(self):
        from measure.measure import Measure
        result = [] 
        for xml_measure in self.measure[:]:
            attributes = xml_measure.attributes[:]
            measure = Measure(attributes=attributes, elements=[])
            for elt in xml_measure.content():
                measure.elements.append(elt)
            result.append(measure)
        return result

    def extract_voices(self):

        measures = self.get_measures()
        set_note_attributes(measures)
        set_measure_list_offsets(measures)

        for measure in measures:
            measure.elements = group_chords(measure.elements)
            measure.elements = group_grace_notes(measure.elements)

        # # result = associate_directions_with_note_events(result)
        voices = self.group_voices(measures)
        self.voices = voices
        return voices

    def grouped_elements(self):
        result = []
        return ''


def associate_directions_with_note_events(elements):
    pass

    
