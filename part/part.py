from group_chords import group_chords
from group_grace_notes import group_grace_notes
from set_note_attributes import set_note_attributes
from associate_directions_with_note_events import associate_directions_with_note_events
from add_skips_to_voice import add_skips_to_voice
from set_measure_list_offsets import set_measure_list_offsets
from resources.musicxml import (
    note,
    backup,
    forward,
    )
from resources.musicxml import direction
from get_staff_type import get_staff_type
from utilities import is_note_or_chord

def filter_by_voice_name(measure_list, voice_name):
    from copy import deepcopy
    from measure.measure import Measure
    result = []
    for measure in measure_list:
        elts = measure.elements
        new_measure = measure.copy()
        new_measure.elements = []
        for elt in elts:
            if is_note_or_chord(elt):
                if elt.lily_voice == voice_name:
                    new_measure.elements.append(elt)
            # else:
            #     new_measure.elements.append(elt)
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
                if is_note_or_chord(elt):
                    voice = elt.lily_voice
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
        if self.part_id:
            return ' '.join(self.parameters)
        else:
            ' '.join(self.parameters)
            return ''

    @property
    def format_lyrics(self):
        result = []
        for voice in self.voices:
            result.append(voice.format_lyrics)
        return ''.join(result)

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

        for measure in measures:
            measure.elements = group_chords(measure.elements)
            measure.elements = group_grace_notes(measure.elements)

        set_measure_list_offsets(measures)
        measures = associate_directions_with_note_events(measures)

        voices = self.group_voices(measures)

        for voice in voices:
            voice.measures = add_skips_to_voice(voice)
        # for voice in voices:
        #     for measure in voice.measures:
        #         for elt in measure.elements:
        #             print elt.measure_offset, elt

        self.voices = voices
        # for measure in self.voices[0].measures:
        #     for elt in measure.elements:
        #         # only notes and chords -- how to deal with the other objects?
        #         print elt
        # TODO: filter out everything except notes and chords?

        return voices

    def grouped_elements(self):
        result = []
        return ''



    
