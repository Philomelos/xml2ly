def is_note_or_chord(elt):
    from resources.musicxml import note
    from music_data.chord import Chord

    return isinstance(elt, note) or isinstance(elt, Chord)

def group_grace_notes(elts):
    from music_data.grace_container import GraceContainer

    groups = []
    pending_grace_container = []
    prev_note = None

    for elt in elts:
        if is_note_or_chord(elt) and elt.is_grace:
            pending_grace_container.append(elt)
        elif is_note_or_chord(elt):
            prev_note = elt
            if pending_grace_container:
                elt.grace_container = GraceContainer(elements=pending_grace_container)
                pending_grace_container = []
            else:
                elt.grace_container = None
            groups.append(elt)
        else:
            # Insert main note before appending GraceContainer
            groups.append(elt)

    if pending_grace_container: 
        # todo: these are afterGraces!
        prev_note.grace_container = GraceContainer(
            elements=pending_grace_container,
            is_aftergrace=True)
        assert prev_note.grace_container.is_aftergrace

    return groups
