from resources.musicxml import (
    note,
    direction,
    )
from music_data.chord_container import ChordContainer

def is_note(elt):
    from resources.musicxml import note
    return isinstance(elt, note)

def is_chord(elt):
    return is_note(elt) and elt.chord

def is_note_or_chord(elt):
    return isinstance(elt, note) or isinstance(elt, ChordContainer)

def is_direction(elt):
    return isinstance(elt, direction)

