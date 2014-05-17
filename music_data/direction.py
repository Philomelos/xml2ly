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

    @property
    def direction_content(self):
        result = []
        for type_ in self.direction_type[:]:
            result.append(type_.content()[0])
        return result

# offset = ? avoid name conflicts

class DirectionsRegister(object):

    def __init__(self, elements=None):
        if elements is not None:
            self.elements = elements
        else:
            self.elements = {}

    def append(self, direction):
        for elt in direction.direction_content:
            cls = elt.__class__.__name__
            if cls in self.elements:
                lst = self.elements[cls]
                lst.append(elt)
            else:
                lst = []
                lst.append(elt)
                self.elements[cls] = lst
            
    def extend(self, elts):
        for elt in elts:
            self.append(elt)

    def ordered_keys(self):
        return (
            'dynamics',
            'wedge', 
            'formatted_text', # <words>
            )

    @property
    def before_note(self):
        result = []
        for key in self.ordered_keys():
            elts = self.elements.get(key, None)
            if elts:
                for elt in elts:
                    if elt.before_note is not None:
                        result.append(elt.before_note)
        return ' '.join(result)

    @property
    def after_note(self):
        result = []
        for key in self.ordered_keys():
            elts = self.elements.get(key, None)
            if elts:
                for elt in elts:
                    if elt.after_note is not None:
                        result.append(elt.after_note)
        return ' '.join(result)
            
