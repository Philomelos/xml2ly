class PaperMixin(object):

    @property
    def default_global_staff_size(self):
        return 20
    
    @property
    def global_staff_size(self):
        return '#(set-global-staff-size 18.1428571429)'

    @property
    def tenths(self):
        pass

    @property
    def scaling(self):
        pass

    @property
    def page_height(self):
        pass

    @property
    def page_width(self):
        pass

    @property
    def left_margin(self):
        pass

    @property
    def right_margin(self):
        pass

    @property
    def top_margin(self):
        pass

    @property
    def bottom_margin(self):
        pass

    @property
    def system_left_margin(self):
        pass

    @property
    def system_right_margin(self):
        pass

    @property
    def system_distance(self):
        pass

    @property
    def top_system_distance(self):
        pass

    @property
    def note_size(self):
        pass

    # TODO: music-font, word-font, lyric-font

    @property
    def paper_block_open(self):
        return'\\paper {\n' 

    @property
    def paper_block_parameters(self):
        return (
            self.global_staff_size,
            self.paper_block_open,
            self.closing,
            )

    def format_paper_block(self):
        result = filter(lambda x: x is not None, self.paper_block_parameters)
        return ''.join(result)

