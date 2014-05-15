class NotationsMixin(object):

    @property
    def lilypond_format(self):
        result = []
        for notation in self.content():
            result.append(notation.lilypond_format)
        return ' '.join(result)
