import resources.musicxml
from pyxb.binding.datatypes import *

# DATATYPES:
# anySimpleType
# anyType
# anyURI
# base64
# base64Binary
# basis
# binascii
# boolean
# byte
# content
# date
# dateTime
# datetime
# decimal
# double
# duration
# float
# gDay
# gMonth
# gMonthDay
# gYear
# gYearMonth
# hexBinary
# int
# integer
# language
# logging
# long
# negativeInteger
# nonNegativeInteger
# nonPositiveInteger
# normalizedString
# positiveInteger
# pyxb
# re
# short
# string
# time
# token
# unsignedByte
# unsignedInt
# unsignedLong
# unsignedShort

class Base(object):
    pass

from fractions import Fraction

def musicxml_duration_to_fraction(dur):
    return  {'256th': Fraction(1, 256),
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
             'long': Fraction(4, 1)}.get(dur, 4)

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

class DurationInterface(decimal):

    @property
    def lilypond_format(self):
        return self

class PitchInterface(object):

    @property
    def lilypond_format(self):
        return self.step, self.octave
    
class NoteInterface(object):

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
        return self.maybe_property(self.type, default='quarter')

    @property
    def duration_string(self):
        dur = create_fraction_from_xml_data(self.lily_note_type, len(self.dot[:]))
        return fraction_to_lily_string(dur)

    @property
    def lilypond_format(self):
        if self.pitch and not self.is_rest:
            return '{pitch}{duration} {voice}'.format(
                pitch=self.pitch.lilypond_format,
                duration=self.duration_string,
                voice=self.lily_voice,
                )
        elif self.is_rest:
            return 'r4' 

class PartInterface(object):

    @property
    def notes(self):
        result = []
        for measure in self.measure[:]:
            for note in measure.note[:]:
                result.append(note)
        return result

