from pyxb.binding.datatypes import *
from fractions import Fraction

from fractions import Fraction

def musicxml_duration_to_fraction(dur):
    value =  {'256th': Fraction(1, 256),
             '128th': Fraction(1, 128),
             '64th': Fraction(1, 64),
             '32nd': Fraction(1, 32),
             '16th': Fraction(1, 16),
             'eighth': Fraction(1, 8), 
             'quarter': Fraction(1, 4),
             'half': Fraction(1, 2),
             'whole': Fraction(1, 1),
             'breve': Fraction(2, 1),
             'longa': Fraction(4, 1),
             'long': Fraction(4, 1)}.get(dur, None)
    return value

def create_fraction_from_xml_data(duration, dots):
    a = Fraction(musicxml_duration_to_fraction(duration))
    mul = []
    mul.append(a)
    b = Fraction(1,2)
    for x in range(dots):
        mul.append(a * b)
        b = b / 2
    a = sum(mul)
    return a

def apply_dots_to_fraction(duration, dots):
    mul = []
    mul.append(duration)
    b = Fraction(1,2)
    for x in range(dots):
        mul.append(duration * b)
        b = b / 2
    a = sum(mul)
    return a

def integer_to_binary_string(n):
    result = bin(abs(n)).lstrip('-0b')
    if n < 0:
        result = '-' + result
    return result

def fraction_dot_count(fraction):
    binary_string = integer_to_binary_string(fraction.numerator)
    digit_sum = sum([int(x) for x in list(binary_string)])
    dot_count = digit_sum - 1
    return dot_count

def fraction_to_lily_string(a):
    import math
    dot_count = fraction_dot_count(a)
    gpo2 = lambda n: 2 ** (math.floor(math.log(n, 2)) - 0)
    base_value = Fraction(gpo2(a))
    string = [str(base_value.denominator)] + list('.' * fraction_dot_count(a))
    result = ''.join(string)
    return result


class NoteMixin(object):

    @property
    def is_grace(self):
        return self.grace is not None

    @property
    def is_rest(self):
        return self.rest is not None

    @property
    def is_slashed(self):
        return self.grace.slash == 'yes'

    @property
    def is_pitched(self):
        return self.pitch is not None

    @property
    def is_unpitched(self):
        return self.unpitched is not None

    @property
    def is_non_printing_object(self):
        return self.print_object == 'no'

    @property
    def lily_voice(self):
        return self.voice

    @property
    def lily_note_type(self):
        try:
            return self.type.value()
        except AttributeError:
            return None

    @property
    def dots(self):
        return len(self.dot[:])

    @property
    def duration_type(self):
        if self.type is not None:
            return self.type.value()

    @property
    def time_modification_as_fraction(self):
        mod = self.time_modification
        if mod is not None:
            return Fraction(mod.actual_notes, mod.normal_notes)
        else:
            return Fraction(1, 1)

    def get_alternative_tuplet_numerator(self):
        return self.time_modification.actual_notes

    def get_alternative_tuplet_denominator(self):
        return self.time_modification.normal_notes

    def set_alternative_tuplet_values(self, tuplet):
        if tuplet.numerator is None:
            tuplet.alternative_numerator = self.get_alternative_tuplet_numerator()
        if tuplet.denominator is None:
            tuplet.alternative_denominator = self.get_alternative_tuplet_denominator()

    @property
    def tuplets(self):
        from music_data.tuplet import TupletList
        tuplet_list = TupletList()
        for notation in self.notations[:]:
            for tuplet in notation.tuplet[:]:
                self.set_alternative_tuplet_values(tuplet)
                tuplet_list.elements.append(tuplet)
        return tuplet_list

    def duration_from_type(self):
        return create_fraction_from_xml_data(
            self.duration_type,
            self.dots,
            )

    def duration_string_from_duration_tag_and_divisions(self):
        dur = Fraction(int(self.duration),
                       int(self.attributes.divisions)) * Fraction(1, 4)
        return dur

    @property
    def duration_as_fraction(self):
        try:
            return self.duration_from_type()
        except:
            pass
        try:
            return self.duration_string_from_duration_tag_and_divisions()
        except:
            pass

    @property
    def graces(self):
        if hasattr(self, 'grace_container') and self.grace_container is not None:
            return self.grace_container

    @property
    def duration_string(self):
        return fraction_to_lily_string(self.duration_as_fraction)

    @property
    def lyrics(self):
        return self.lyric[:]

    @property
    def lyric_numbers(self):
        result = []
        for lyric in self.lyrics:
            result.append(lyric.number)
        return result

    @property
    def beam_element(self):
        # TODO: use all beams?
        beam = self.beam[:]
        if beam:
            return self.beam[:][0]

    @property
    def tie_element(self):
        for notation in self.notations:
            try:
                return notation.tied[0]
            except IndexError as e:
                pass
        try:
            return self.tie[0]
        except IndexError as e:
            pass

    @property
    def format_contributions(self):
        return (
            self.tie_element,
            self.beam_element,
            self.tuplets,
            self.directions,
            )

    @property
    def lilypond_format(self, indent=0):
        result = []

        # TODO: clean up
        for elt in self.format_contributions:
            if elt is not None and elt.before_note is not None:
                result.append(elt.before_note)

        if self.graces:
            result.append(self.graces.lilypond_format)

        if self.is_non_printing_object:
            from music_data.skip import Skip
            skip = Skip(self.duration_as_fraction)
            result.append(skip.lilypond_format)

        else:
            if self.is_pitched:
                result.append('{}{}'.format(
                    self.pitch.lilypond_format,
                    self.duration_string))

            elif self.is_rest:
                result.append('r{}'.format(self.duration_string))

            elif self.is_unpitched:
                from resources.musicxml import pitch
                pitch = pitch()
                pitch.step = self.unpitched.display_step
                pitch.octave = self.unpitched.display_octave
                result.append('{}{}'.format(
                    pitch.lilypond_format,
                    self.duration_string))

        for elt in self.format_contributions:
            if elt is not None and elt.after_note is not None:
                result.append(elt.after_note)

        return ''.join(result)

                        
# Names: before/after? 'type' -> lily_type? before_note/after_note? body?
# collect chords and graces in a simple way.
