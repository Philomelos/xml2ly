from fractions import Fraction
from resources.musicxml import (
    note,
    backup,
    forward,
    direction,
    )
from music_data.chord_container import ChordContainer

def is_note_or_chord(elt):
    return isinstance(elt, note) or isinstance(elt, ChordContainer)

def is_chord(elt):
    return is_note(elt) and elt.chord

def is_grace(elt):
    return hasattr(elt, 'grace') and elt.is_grace

def is_backup(elt):
    return isinstance(elt, backup)

def is_forward(elt):
    return isinstance(elt, forward)

def offset_increment(elt):
    if is_backup(elt):
        return -1
    elif is_forward(elt):
        return 1
    elif is_grace(elt):
        return 0
    elif is_note_or_chord(elt):
        return 1
    else:
        return None

def set_measure_list_offsets(measure_list):
    last_divisions = None
    for measure in measure_list:

        offset = 0
        new_elements = []
        for elt in measure.elements:
            # print offset_increment(elt), elt, elt.attributes.divisions

            # only use 'next_new_offset' if elt increments counter
            if offset_increment(elt) is not None:
                elt.measure_offset = offset
                time_modification = elt.time_modification_as_fraction
                offset = offset + ((elt.duration_as_fraction / time_modification) * offset_increment(elt))
                # offset = offset + elt.duration_as_fraction
                # if offset > 1:
                #     print offset, elt.duration_as_fraction, elt.time_modification_as_fraction

            elif isinstance(elt, direction):
                elt.measure_offset = offset + (Fraction(1,4) * elt.offset_as_fraction)

            else:
                elt.measure_offset = offset

    return measure_list

