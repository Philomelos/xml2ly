from music_data.staff import Staff

class ScorePartMixin(object):

    @property
    def part_id(self):
        return self.id

    @property
    def score_part_name(self):
        if self.part_name_display is not None:
            return ''.join(x.value() for x in self.part_name_display.display_text[:])
        else:
            return self.part_name.value()

    @property
    def score_part_abbreviation(self):
        if self.part_abbreviation_display is not None:
            return ''.join(x.value() for x in self.part_abbreviation_display.display_text[:])
        else:
            return self.part_abbreviation

    # @property
    # def score_block_format(self):
    #     return self.part.lilypond_score_representation

    @property
    def score_block_format(self):
        # TODO: remove duplicated code
        if self.part.part_id:

            if self.part.staff_type.command == r'PianoStaff':
                result = []
                staff = self.part.staff_type
                # cmd = '\\new {command} <<'.format(command=staff.command)
                result.append(staff.score_representation)

                part_name = self.score_part_name
                part_abbreviation = self.score_part_abbreviation

                if part_name:
                    result.append(
                        '\\set ' + self.part.staff_type.command + '.instrumentName = ')
                    result.append('"{}"'.format(part_name))

                if part_abbreviation:
                    result.append(
                        '\\set ' + self.part.staff_type.command + '.shortInstrumentName = ')
                    result.append('"{}"'.format(part_abbreviation))

                staff_dict = staff.build_staff_dict(self.part.voices)
                for staff_number in staff_dict.keys():
                    s = Staff()
                    # set staff_number (use when switching between staves)
                    s.staff_number = staff_number
                    s.score_part = self
                    result.append(s.score_representation)
                    voices = staff_dict[staff_number]
                    for voice in voices:
                        result.append(voice.lilypond_score_representation)
                    result.append('>>')
                result.append('>>')
                return ' '.join(result)

            else:
                result = [] 
                result.append(self.part.staff_type.score_representation)
                part_name = self.score_part_name
                part_abbreviation = self.score_part_abbreviation

                if part_name:
                    result.append(
                        '\\set ' + self.part.staff_type.command + '.instrumentName = ')
                    result.append('"{}"'.format(part_name))

                if part_abbreviation:
                    result.append(
                        '\\set ' + self.part.staff_type.command + '.shortInstrumentName = ')
                    result.append('"{}"'.format(part_abbreviation))

                for voice in self.part.voices:
                    result.append(voice.lilypond_score_representation)

                result.append('>>')

                if result:
                    return ' '.join(result)
                else:
                    return ''
        else:
            return ''
