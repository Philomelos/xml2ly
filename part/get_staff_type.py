def get_staff_type(self):
    from music_data.staff import (
        Staff,
        RhythmicStaff,
        DrumStaff,
        PianoStaff,
        )

    try:
        attributes = self.measure[:][0].attributes[:][0]
    except:
        attributes = None

    sign = attributes.clef[:][0].sign
    try:
        clef_sign = {"percussion": "percussion", "TAB": "tab"}.get(sign, None)
    except:
        clef_sign = ''

    try:
        lines = attributes.staff_details.staff_lines
    except:
        lines = 5

    try:
        staff_count = attributes.staves
    except:
        staff_count = 1

    if clef_sign and lines == 1:
        staff = RhythmicStaff()
    elif clef_sign == 'percussion':
        staff = DrumStaff()
    elif clef_sign == 'tab':
        staff = TabStaff()
    elif staff_count > 1:
        staff = PianoStaff()
    else:
        staff = Staff()

    return staff
