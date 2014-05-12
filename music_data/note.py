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
    def is_rest(self):
        return self.rest is not None

    def maybe_property(self, param, default):
        try:
            value = param.value()
            return value
        except AttributeError:
            return default

    @property
    def lily_voice(self):
        # TODO: prefix properties to avoid overriding
        return self.maybe_property(self.voice, default=1)

    @property
    def lily_note_type(self):
        return self.maybe_property(self.type, default=None)

    @property
    def dots(self):
        return len(self.dot[:])

    @property
    def duration_type(self):
        if self.type is not None:
            return self.type.value()

    def duration_string_from_type(self):
        return create_fraction_from_xml_data(
            self.duration_type,
            self.dots,
            )

    def duration_string_from_duration_tag_and_divisions(self):
        return 'from duration_tag'

    @property
    def duration_string(self):

        try:
            return self.duration_string_from_type()
        except:
            pass

        try:
            return self.duration_string_from_duration_tag_and_divisions()
        except:
            pass
            

    @property
    def template(self, indent=0):
        return '{before}{pitch}{duration}{voice}'

    @property
    def before(self):
        # All methods which collect multiple items and joins them
        #     must provide a default return value '' ?
        result = []
        for x in range(0, 4):
            result.append(str(x))
        return '.'.join(result)

    def indent(self, indent=0):
        return '\t' * indent

    @property
    def parameters(self):
        return {
            'before'  : self.before,
            'pitch'   : self.pitch.lilypond_format,
            'duration': self.duration_string,
            'voice'   : self.lily_voice,
            }

    @property
    def lilypond_format(self, indent=0):
        # if self.pitch and not self.is_rest:
        #     return self.indent(indent) + self.template.format(**self.parameters)
        # elif self.is_rest:
        #     return 'r4' 
        return 'note'

