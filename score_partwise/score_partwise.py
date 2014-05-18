class ScorePartWiseMixin(object):

    score_block_open  = '\\score { \n <<'
    score_block_close = '\n >> } \n'

    @property
    def parts(self):
        return self.part[:]

    @property
    def score_block_contents(self):
        result = []
        for elt in self.part_list.content():
            result.append(elt.score_block_format)
        return result

    def format_parts(self):
        result = []
        for part in self.parts:
            result.append(part.lilypond_format)
        return '\n'.join(result)

    def format_lyrics(self):
        result = []
        for part in self.parts:
            result.append(part.format_lyrics)
        return '\n'.join(result)

    def format_score_block(self):
        result = []

        for score_part in self.part_list.score_part[:]:
            score_part.part = self.get_corresponding_part(score_part)

        result.append(self.score_block_open)
        result.extend(self.score_block_contents)
        result.append(self.score_block_close)

        return '\n'.join(result)
            
    def get_corresponding_part(self, score_part):
        try:
            return filter(lambda x: x.part_id == score_part.part_id, self.parts)[0]
        except:
            return None

# flow: -> a) part_contents, b) score_representation

