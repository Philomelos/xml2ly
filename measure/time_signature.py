from fractions import Fraction

class TimeSignature(object):

    styles = {
        'default': "\\defaultTimeSignature",
        'numeric': "\\numericTimeSignature",
        }

    def __init__(self, numerator=None, denominator=None):
        self.numerator=numerator
        self.denominator=denominator

    @property
    def time_signature_style(self):
        # TODO: implement styles, set globally?
        return 'numeric'

    @property
    def lilypond_format(self):
        if self.numerator and self.denominator:
            result = '\n\\time {num}/{denom}\n'
            return result.format(num=self.numerator, denom=self.denominator)

    @property
    def duration_as_fraction(self):
        return Fraction(self.numerator, self.denominator)
