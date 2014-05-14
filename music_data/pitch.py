from resources.musicxml import pitch

class PitchMixin(object):

    @property
    def xml_step(self):
        if self.step is not None:
            return musicxml_step_to_lily(self.step)

    @property
    def xml_alteration(self):
        if self.alter is not None:
            return self.alter
        else:
            return 0

    @property
    def xml_octave(self):
        if self.octave is not None:
            return self.octave - 4
        else:
            return 0

    def transposed (self, interval):
        c = self.copy ()
        c.alteration += interval.alteration
        c.step += interval.step
        c.octave += interval.octave
        c.normalize ()
        target_st = self.semitones() + interval.semitones()
        c.alteration += target_st - c.semitones()
        return c

    def normalize (c):
        while c.step < 0:
            c.step += 7
            c.octave -= 1
        c.octave += c.step / 7
        c.step = c.step % 7

    def lisp_expression (self):
        return '(ly:make-pitch %s %s %s)' % (self.octave,
                                             self.step,
                                             self.alteration)

    def copy (self):
        p = pitch ()
        p.alteration = Alteration(self.alteration)
        p.step = Step(self.step)
        p.octave = Octave(self.octave)
        p._force_absolute_pitch = True
        return p

    def steps (self):
        return self.step + self.octave * 7

    def semitones (self):
        return self.octave * 12 + [0, 2, 4, 5, 7, 9, 11][self.step] + self.alteration

    def normalize_alteration (c):
        if(c.alteration < 0 and [True, False, False, True, False, False, False][c.step]):
            c.alteration += 1
            c.step -= 1
        elif(c.alteration > 0 and [False, False, True, False, False, False, True][c.step]):
            c.alteration -= 1
            c.step += 1
        c.normalize ()

    def add_semitones (self, number):
        semi = number + self.alteration
        self.alteration = 0
        if(semi == 0):
            return
        sign = (1,-1)[semi < 0]
        prev = self.semitones()
        while abs((prev + semi) - self.semitones ()) > 1:
            self.step += sign
            self.normalize()
        self.alteration += (prev + semi) - self.semitones ()
        self.normalize_alteration ()

    def ly_step_expression (self):
        a = pitch_general(self)
        return a

    def absolute_pitch (self):
        octave = self.xml_octave
        if octave >= 0:
            return "'" * (octave + 1)
        elif octave < -1:
            return "," * (-octave - 1)
        else:
            return ''

    def ly_expression (self):
        str = self.ly_step_expression ()
        str += self.absolute_pitch ()
        return str

    def print_ly(self, outputter):
        outputter(self.ly_expression())

    @property
    def lilypond_format(self):
        str = self.ly_step_expression()
        str += self.absolute_pitch ()
        return str

def interpret_alter_element(elt):
    alter = 0
    if elt:
        alter = string_to_number(elt)
    return alter
	
def musicxml_step_to_lily(step):
    if step:
        return (ord(step) - ord('A') + 7 - 2) % 7
    else:
        return None

def generic_tone_to_pitch (tone):
    accidentals_dict = {
	"" : 0,
	"es" : -1,
	"s" : -1,
	"eses" : -2,
	"ses" : -2,
	"is" : 1,
	"isis" : 2
    }
    p = Pitch ()
    tone_ = tone.strip().lower()
    p.octave = tone_.count("'") - tone_.count(",")
    tone_ = tone_.replace(",","").replace("'","")
    p.step = ((ord (tone_[0]) - ord ('a') + 5) % 7)
    p.alteration = accidentals_dict.get(tone_[1:], 0)
    return p


# Implement the different note names for the various languages
def pitch_generic (pitch, notenames, accidentals):

    str = notenames[pitch.xml_step]
    halftones = int (pitch.xml_alteration)
    if halftones < 0:
        str += accidentals[0] * (-halftones)
    elif pitch.xml_alteration > 0:
        str += accidentals[3] * (halftones)
    # Handle remaining fraction to pitch.alteration (for microtones)
    if (halftones != pitch.xml_alteration):
        if None in accidentals[1:3]:
            pass
        else:
            try:
                str += {-0.5: accidentals[1], 0.5: accidentals[2]}[pitch.xml_alteration - halftones]
            except KeyError:
                pass
    return str


def pitch_general (pitch):
    str = pitch_generic (pitch, ['c', 'd', 'e', 'f', 'g', 'a', 'b'], ['es', 'eh', 'ih', 'is'])
    return str.replace ('aes', 'as').replace ('ees', 'es')
