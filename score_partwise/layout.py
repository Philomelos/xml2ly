class LayoutMixin(object):

    @property
    def layout_block_open(self):
        return '\\layout {\n'

    @property
    def layout_block_parameters(self):
        return (
            self.layout_block_open,
            self.closing,
            )

    def format_layout_block(self):
        result = filter(lambda x: x is not None, self.layout_block_parameters)
        return ''.join(result)

