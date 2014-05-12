class HeaderMixin(object):

    opening = '\\header {\n'
    closing = '\n } \n'

    def typed_credit(self, type_, default=''):
        type_matches = lambda x: x.lily_credit_type == type_
        credit = filter(type_matches, self.credit[:])
        if credit:
            return credit[0]
        else:
            return default

    def format_attribute(self, name, result):
        if result:
            return '{} = "{}"'.format(name, result)

    ### PROPERTIES ###

    @property
    def lily_title(self):
        result = (self.movement_title or
                  self.typed_credit('title'))
        if result:
            return self.format_attribute('title', result)

    @property
    def lily_subtitle(self):
        result = self.typed_credit('subtitle')
        if result:
            return result.lilypond_format

    @property
    def parameters(self):
        return (
            self.opening,
            self.lily_title,
            self.lily_subtitle,
            self.closing,
            )

    @property
    def format_header(self):
        result = filter(lambda x: x is not None, self.parameters)
        return '\n'.join(result)

