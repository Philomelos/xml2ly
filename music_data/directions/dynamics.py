class DynamicsMixin(object):

    dynamic_marks = (
        'f',
        'ff',
        'fff',
        'ffff',
        'fffff',
        'ffffff',
        'fp',
        'fz','mf',
        'mp',
        'p',
        'pp',
        'ppp',
        'pppp',
        'ppppp',
        'pppppp',
        'rf',
        'rfz',
        'sf',
        'sffz',
        'sfp',
        'sfpp',
        'sfz',
        )

    @property
    def before_note(self):
        return None

    def has_dynamic_mark(self, mark):
        value = getattr(self, mark)
        return len(value) > 0

    @property
    def after_note(self):
        # TODO: get mark directly
        for mark in self.dynamic_marks:
            if self.has_dynamic_mark(mark):
                return '\\{}'.format(mark)


