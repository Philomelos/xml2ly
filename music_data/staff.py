class Staff(object):
    command = r'Staff'
    voice_command = r'Voice'

    def __init__(self, staff_number=1):
        self.staff_number=staff_number

    def print_instrument_name(self, printer):
        pass

    @property
    def score_representation(self):
        cmd = '\\new {command} = "{command}_{staff_number}" <<'.format(
            command=self.command,
            staff_number=self.staff_number)
        return cmd

    @property
    def score_representation_end(self):
        return '>> \n'


class PianoStaff(Staff):

    command = r'PianoStaff'
    voice_command = r'Voice'

    @staticmethod
    def guess_staff_number(voice):
        import operator
        import collections
        result = []
        for elt in voice.music_events:
            if hasattr(elt, 'staff'):
                result.append(elt.staff)
        count = collections.Counter(result)
        try:
            return max(count.iteritems(), key=operator.itemgetter(1))[0]
        except:
            return 1

    def build_staff_dict(self, voices):
        staff_dict = {}
        for voice in voices:
            staff_number = self.guess_staff_number(voice)
            voice.staff_number = staff_number

            if staff_number in staff_dict:
                staff_dict[staff_number].append(voice)

            else:
                staff_dict[staff_number] = [voice]

        return staff_dict

    @property
    def score_representation(self):
        cmd = '\\new {command} <<'.format(command=self.command)
        return cmd

class TabStaff(Staff):
    command = r'TabStaff'
    voice_command = r'TabVoice'

class DrumStaff(Staff):
    command = r'DrumStaff'
    voice_command = r'DrumVoice'

class RhythmicStaff(Staff):
    command = r'RhythmicStaff'
