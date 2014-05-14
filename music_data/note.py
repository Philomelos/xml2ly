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
    def time_modification_as_fraction(self):
        mod = self.time_modification
        if mod is not None:
            return Fraction(mod.actual_notes, mod.normal_notes)
        else:
            return Fraction(1, 1)
        
    @property
    def is_grace(self):
        return self.grace is not None

    @property
    def is_rest(self):
        return self.rest is not None

    @property
    def is_pitched(self):
        return self.pitch is not None

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
    def before(self):
        return ''

    def indent(self, indent=0):
        return '\t' * indent

    @property
    def parameters(self):
        return {
            'before'  : self.before,
            'pitch'   : self.pitch.lilypond_format,
            'duration': self.duration_string,
            'voice'   : self.lily_voice,
            'after'  : self.before,
            }

    def format_as_rest(self):
        pass

    @property
    def duration_string(self):
        return fraction_to_lily_string(self.duration_as_fraction)

    @property
    def lilypond_format(self, indent=0):
        if self.is_pitched:
            return '{}{}'.format(
                self.pitch.lilypond_format,
                self.duration_string,
                )
        elif self.is_rest:
            return 'r{}'.format(self.duration_string)
        elif self.is_unpitched:
            return ''
        else:
            return ''
            



# Names: before/after? 'type' -> lily_type? before_note/after_note? body?
# collect chords and graces in a simple way.
