from fractions import Fraction

class ForwardMixin(object):

    @property
    def lilypond_format(self):
        return 'forward'

    @property
    def time_modification_as_fraction(self):
        return 1

    def duration_string_from_duration_tag_and_divisions(self):
        dur = Fraction(int(self.duration),
                       int(self.attributes.divisions)) * Fraction(1, 4)
        return dur

    @property
    def duration_as_fraction(self):
        return self.duration_string_from_duration_tag_and_divisions()
