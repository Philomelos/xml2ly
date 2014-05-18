class SlurMixin(object):

    @property
    def is_opening(self):
        return self.type == 'start'

    @property
    def is_closing(self):
        return self.type == 'stop'

    @property
    def before_note(self):
        return None

    @property
    def after_note(self):
        if self.is_opening:
            return '('
        elif self.is_closing:
            return ')'


class SlurList(object):

    def __init__(self, elements=None):
        self.elements=elements

    @property
    def before_note(self):
        result = []
        for elt in self.elements:
            if elt.before_note is not None:
                result.append(elt.before_note)
        return ''.join(result)

    @property
    def after_note(self):
        result = []
        for elt in self.elements:
            if elt.after_note is not None:
                result.append(elt.after_note)
        return ''.join(result)

            
            
            
