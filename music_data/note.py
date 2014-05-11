from pyxb.binding.datatypes import *
from fractions import Fraction

class NoteInterface(object):

    @property
    def is_rest(self):
        return self.rest is not None

    def maybe_property(self, param, default):
        try:
            value = param.value()
            return value
        except AttributeError:
            return default

    @property
    def lily_voice(self):
        # TODO: prefix properties to avoid overriding
        return self.maybe_property(self.voice, default=1)

    @property
    def lily_note_type(self):
        return self.maybe_property(self.type, default='quarter')

    @property
    def duration_string(self):
        # dur = create_fraction_from_xml_data(self.lily_note_type, len(self.dot[:]))
        # return fraction_to_lily_string(dur)
        return '4..'

    @property
    def template(self, indent=0):
        return '{before}{pitch}{duration}{voice}'

    @property
    def before(self):
        # All methods which collect multiple items and joins them
        #     must provide a default return value '' ?
        result = []
        for x in range(0, 4):
            result.append(str(x))
        return '.'.join(result)

    def indent(self, indent=0):
        return '\t' * indent

    @property
    def parameters(self):
        return {
            'before'  : self.before,
            'pitch'   : self.pitch.lilypond_format,
            'duration': self.duration_string,
            'voice'   : self.lily_voice,
            }

    @property
    def lilypond_format(self, indent=0):
        if self.pitch and not self.is_rest:
            return self.indent(indent) + self.template.format(**self.parameters)
        elif self.is_rest:
            return 'r4' 

