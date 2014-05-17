class WordsMixin(object):

    @property
    def before_note(self):
        return None

    @property
    def is_above(self):
        return self.default_y > 0

    @property
    def is_below(self):
        return self.default_y < 0

    @property
    def direction(self):
        if self.is_above:
            return '^'
        elif self.is_below:
            return '_'
        else:
            return '-' 

    @property
    def after_note(self):
        result = '{direction}\\markup {{ \left-align "{text}" }}'
        return result.format(direction=self.direction, text=self.value())
                             

        
