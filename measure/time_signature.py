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
        # TODO: implement more styles 
        return 'numeric'

    @property
    def lilypond_format(self):
        if self.numerator and self.denominator:
            style = self.styles.get(self.time_signature_style, None)
            result = '{style} \n \\time {num}/{denom}'
            return result.format(style=style, num=self.numerator, denom=self.denominator)
