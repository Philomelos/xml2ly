def is_note(elt):
    from resources.musicxml import note
    return isinstance(elt, note)

def is_chord(elt):
    return is_note(elt) and elt.chord

def is_group(lst):
    return len(lst) > 1

def append_as_chord_if_multiple(lst, groups):
    from music_data.chord_container import ChordContainer

    if is_group(lst):
        groups.append(ChordContainer(lst))
    else:
        groups.extend(lst)
    return groups

def group_chords(elts):

    groups = []
    curr_elts = []

    for elt in elts:
        if is_chord(elt):
            curr_elts.append(elt)
        else:
            groups = append_as_chord_if_multiple(curr_elts, groups)

            if is_note(elt):
                curr_elts = [elt]
            else:
                curr_elts = []
                groups.append(elt)

    append_as_chord_if_multiple(curr_elts, groups)

    return groups
