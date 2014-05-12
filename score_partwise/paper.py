class PaperMixin(object):

    @property
    def paper_block_open(self):
        return'\\paper {\n'

    @property
    def paper_block_parameters(self):
        return (
            self.paper_block_open,
            self.closing,
            )

    def format_paper_block(self):
        result = filter(lambda x: x is not None, self.paper_block_parameters)
        return ''.join(result)

