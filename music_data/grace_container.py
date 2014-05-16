class GraceContainer(object):

    def __init__(self, elements=None, is_aftergrace=False):
        self.elements=elements
        self.is_aftergrace=is_aftergrace

    @property
    def opening(self):
        return "\\grace {"

    @property
    def closing(self):
        return '}'

    @property
    def format_contributions(self):
        result = []
        for elt in self.elements:
            result.append(elt.lilypond_format)
        return result

    @property
    def lilypond_format(self):
        result = []
        result.append(self.opening)
        result.extend(self.format_contributions)
        result.append(self.closing)
        return ' '.join(result)
