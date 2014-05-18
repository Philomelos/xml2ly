class TieMixin(object):

    @property
    def before_note(self):
        return None

    @property
    def is_opening(self):
        return self.type == 'start'

    @property
    def before_note(self):
        return None

    @property
    def after_note(self):
        if self.is_opening:
            return '~'
        else:
            return ''







