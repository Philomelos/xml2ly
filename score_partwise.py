class ScorePartWiseMixin(object):

    score_block_open  = '\\score {\n'
    score_block_close = '\n } \n'

    @property
    def parts(self):
        return self.part[:]

    def format_parts(self):
        result = []
        for part in self.parts:
            result.append(part.lilypond_format)
        return '\n'.join(result)

    @property
    def score_block_contents(self):
        result = []
        for elt in self.part_list.content():
            result.append(elt.lilypond_format)
        return result

    def format_score_block(self):
        result = []
        result.append(self.score_block_open)
        result.extend(self.score_block_contents)
        result.append(self.score_block_close)
        return '\n'.join(result)
            

