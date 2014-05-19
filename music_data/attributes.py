class AttributesMixin(object):

    @property
    def lilypond_format(self):
        return None


class ElementAttributes(object):

    def __init__(self,
                 divisions=None,
                 clef=None,
                 time=None,
                 key=None,
                 ):
        self.divisions=divisions
        self.clef=clef
        self.key=key
        self.time=time

    def update(self, measure_attributes):
        if measure_attributes:
            for var in vars(self):
                value = getattr(measure_attributes[0], var)
                if value is not None:
                    setattr(self, var, value)
        
    
