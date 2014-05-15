from fractions import Fraction

class DirectionMixin(object):

    @property
    def lilypond_format(self):
        return None 

    @property
    def offset_as_fraction(self):
        if self.offset is not None:
            try:
                numerator = int(self.offset.value()) 
                denominator = int(self.attributes.divisions)
                return Fraction(numerator, denominator)
            except TypeError as e:
                e.args += ('Cannot cast to Fraction', )
                raise
        else:
            return 0

            
# offset = ? avoid name conflicts
