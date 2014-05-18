class TimeSignature(object):

    def __init__(self, numerator=None, denominator=None):
        self.numerator=numerator
        self.denominator=denominator

    @property
    def lilypond_format(self):
        if self.numerator and self.denominator:
            return '\\time {num}/{denom}'.format(num=self.numerator,
                                                 denom=self.denominator)
