def KeySignatureTonicPitch(mode):
    from music_data.pitch import LilyPitch
    modes = {
        'major'     : (0, 0), # (step, alteration)
        'minor'     : (5, 0),
        'ionian'    : (0, 0),
        'dorian'    : (1, 0),
        'phrygian'  : (2, 0),
        'lydian'    : (3, 0),
        'mixolydian': (4, 0),
        'aeolian'   : (5, 0),
        'locrian'   : (6, 0),
        }
    result = modes.get(mode, None)
    if result:
        step = result[0]
        pitch = LilyPitch(step=step, alteration=0, octave=0)
        return pitch


class KeySignatureMixin(object):

    @property
    def has_non_standard_key(self):
        # TODO: non-standard keys
        return self.non_standard_key is not None

    @property
    def tonic(self):
        from music_data.pitch import LilyPitch
        if self.mode and self.fifths:
            fifths = self.fifths # copy to avoid overwriting when reading
                                 # value multiple times.
            tonic = KeySignatureTonicPitch(self.mode)
            transposer = LilyPitch(step=4)
            if fifths < 0:
                fifths *= -1
                transposer.step *= -1
                transposer.normalize()
            for x in range(fifths):
                tonic = tonic.transposed(transposer)
            tonic.normalize()
            print tonic.step, tonic.ly_step_expression(), self.mode 
            return tonic

    @property
    def lilypond_format(self):
        from music_data.pitch import LilyPitch
        a = self.tonic
        if a:
            return '\\key %s \\%s' % (a.ly_step_expression(), self.mode)
        else:
            return ''
