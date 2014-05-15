class Voice(object):

    opening = '{\n'
    closing = '\n } \n'

    def __init__(self, name=None, measures=None):
        self.name=name
        self.measures=measures

    @property
    def music_events(self):
        result = []
        for measure in self.measures:
            for elt in measure.elements:
                result.append(elt)
        return result
                

    @property
    def voice_label(self):
        result = '"Part_{part_id}_Voice_{voice_name}" = {{ \n'
        label = result.format(part_id=self.part.part_id,
                              voice_name=self.name)
        return label

    @property
    def lily_measures(self):
        result = []
        for elt in self.measures:
            result.append(elt.lilypond_format)
        return ' '.join(result)

    @property
    def parameters(self):
        return (
            self.voice_label,
            self.lily_measures,
            self.closing,
            )

    @property
    def lilypond_format(self):
        return ''.join(self.parameters)

    def print_score_representation(self):
        label = '"Part_{part_id}_Voice_{voice_name}"'.format(
            part_id=self.part.part_id,
            voice_name=self.name)

        cmd = '\\context {voice_command} = '.format(
            voice_command=self.part.staff_type.voice_command,
            )

        var = '{{ \\"Part_{part_id}_Voice_{voice_name}" }}'.format(
            part_id=self.part.part_id,
            voice_name=self.name)

        # lyric_part_label = '\\"Part_{part_id}_Voice_{voice_name}_{lyric_verse}"'
        # printer.newline()
        # if self.get_all_lyric_numbers():
        #     for lyric_part in self.get_all_lyric_numbers():
        #         printer.dump('\\new Lyrics \lyricsto')
        #         printer.dump(label)
        #         printer.dump(
        #             lyric_part_label.format(
        #                 part_id=self.part.part_id,
        #                 voice_name=self.name,
        #                 lyric_verse=lyric_part))

        return ' '.join([cmd, label, var])

    @property
    def lilypond_score_representation(self):
        return self.print_score_representation()

    def get_all_lyric_numbers(self):
        result = []
        for elt in self.music_events: 
            try:
                lyric_numbers = elt.lyric_numbers
            except:
                lyric_numbers = None
            if lyric_numbers:
                result.extend(lyric_numbers)
        return sorted(set(result))

    def print_lyrics(self, printer):

        label = '"Part_{part_id}_Voice_{voice_name}_{lyric_verse}" = \\lyricmode'

        for lyric_part in self.get_all_lyric_numbers():
            printer.dump(
                label.format(part_id=self.part.part_id,
                             voice_name=self.name,
                             lyric_verse=lyric_part))
            printer.open_expression()
            printer.dump('\\set ignoreMelismata = ##t')
            for elt in self.music_events:
                if hasattr(elt, 'lyrics'):
                    lyric = filter(lambda x: x.number == lyric_part,
                                   elt.lyrics)
                    if lyric:
                        lyric[0].print_ly(printer)
                    else:
                        if not elt.rest:
                            printer.dump('\\skip1')
            printer.close_expression()

