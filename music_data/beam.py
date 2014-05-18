class BeamMixin(object):

    @property
    def is_opening(self):
        return self.value() == 'begin'

    @property
    def is_closing(self):
        return self.value() == 'end'

    @property
    def before_note(self):
        return None

    @property
    def after_note(self):
        if self.is_opening:
            return '['
        elif self.is_closing:
            return ']'
        else:
            return None
