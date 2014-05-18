from utilities import is_note_or_chord
from utilities import is_direction
from measure.measure import Measure

def partition_by_offset(elts, offset):
    lesser, greater, = [], []
    for elt in elts:
        if elt.offset <= offset:
            lesser.append(elt)
        else:
            greater.append(elt)
    return lesser, greater

def associate_directions_with_note_events(measure_list):
    from copy import deepcopy
    from music_data.direction import DirectionsRegister

    # Every element in result which is not a top-level musicevent
    # (i.e. a Note or rest), needs to be attached/appended to a
    # top-level musicevent.
    new_measure_list = []
    # Pending Directions, such as Wedge, Words, Slide.
     
    for measure in measure_list:

        new_elements = []
        pre_note_directions = []
        last_note_event = None

        for elt in measure.elements:
            # If elt is a NoteElement, check if there are any pending
            # directions to collect
            if is_note_or_chord(elt):
                elt.directions = DirectionsRegister()
                last_note_event = elt
                # Attach Directions if their offset is greater than
                # the offset of the current element. 
                if pre_note_directions:
                    insert, pre_note_directions = partition_by_offset(
                        pre_note_directions, elt.measure_offset)
                    elt.directions.extend(insert)
                new_elements.append(elt)

            elif is_direction(elt):
                pre_note_directions.append(elt)

            else:
                new_elements.append(elt)
        # At the end of the Measure, gather all pending Directions
        # and attach them to the last active NoteElement
        if pre_note_directions:
            if last_note_event:
                last_note_event.directions.extend(pre_note_directions)
            pre_note_directions = [] 

        measure.elements = new_elements
        new_measure_list.append(measure)

    return new_measure_list
