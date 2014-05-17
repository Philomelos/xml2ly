class PartGroupMixin(object):

    @property
    def is_opening(self):
        return self.type == 'start'

    @property
    def is_closing(self):
        return self.type == 'stop'

    # @property
    # def staff_group_name(self):
    #     retu

    @property
    def lilypond_format(self):
        return ''

    @property
    def score_block_format(self):
        print self.group_name, self.group_abbreviation
        return ''
