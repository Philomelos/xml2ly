class HeaderInterface(object):

    def typed_credit(self, type_, default=''):
        type_matches = lambda x: x.lily_credit_type == type_
        credit = filter(type_matches, self.credit[:])
        if credit:
            return credit[0].lilypond_format
        else:
            return default

    @property
    def lily_title(self):
        if self.movement_title:
            return 'title = "{}"'.format(self.movement_title)

    @property
    def parameters(self):
        from collections import OrderedDict
        return OrderedDict([
            ('before', '\\header {\n'),
            ('title', self.lily_title),
            ('subtitle', self.typed_credit('subtitle')),
            ('after', '\n}'),
            ])

    @property
    def format_header(self):
        # filter out 
        result = filter(lambda x: x is not None, self.parameters.values())
        return '\n'.join(result)
