from fractions import Fraction
from music_data.skip import Skip
from utilities import is_note_or_chord

def add_skips_to_voice(voice):
    '''
    Loop through all measures in the measure_list of the current voice.
    We know the offsets of every durated element in this list and need
    to "fill the gaps" inbetween them with Skips to keep all the voices
    in sync. This is a potentially dangerous operation and a seemingly
    rich source of bugs -- be careful.
    '''

    new_measure_list = []
    curr_time_signature = None

    for measure in voice.measures:

        # 'offset' is a counter which keep track of the current
        # position in this measure. It is incremented by all elements
        # which have a 'duration' attribute, otherwise ignored.
        offset = 0
        new_elements = []

        # Keep track of current time signature. This is needed when an
        # empty measure is encountered, in which case we need to insert
        # a skip with the same length as the measure.
        if measure.time_signature is not None:
            curr_time_signature = measure.time_signature

        # CASE #1: Empty measure; no durated elements can be found.
        # Insert a skip of the same duration as the current time signature.
        if not measure.has_any_durated_element:

            # First, add all elements (Attributes etc.)...
            for elt in measure.elements:
                new_elements.append(elt)

            # ...then, append the Skip, filling the measure completely.
            skip = Skip(duration=curr_time_signature.duration_as_fraction)
            new_elements.append(skip)

        # CASE #2: There are one or more durated elements in this measure.
        else:

            for elt in measure.elements:

                # If we are dealing with a durated element (either a NoteElement,
                # BackupElement of ForwardElement), we now need to calculate the
                # difference between the current and previous offset. ('offset'
                # is set by the function xml2ly.part.set_measure_list_offsets --
                # if any weird behavior is encountered, please check that one as well.)
                if is_note_or_chord(elt):

                    diff = elt.measure_offset - offset
                    # Get the endpoint of this element by adding its duration
                    # to its offset. Multiply the duration with the element's
                    # time_modification to get the actual duration (this is necessary
                    # when dealing with tuplets and nested tuplets.
                    offset = elt.measure_offset + (
                        elt.duration_as_fraction / elt.time_modification_as_fraction)

                    # If the difference between this element's offset and the
                    # position in the measure which the counter is currently at,
                    # it probably means that we're dealing with a voice which doesn't
                    # start at the beginning of the piece. In this case, we need to
                    # add skips to keep up with the other voices in this staff, such
                    # that the different voices are perfectly 'aligned' at the end
                    # of every measure.
                    if diff > 0:
                        skip = Skip(duration=Fraction(diff))
                        new_elements.append(skip)
                    new_elements.append(elt)

                else:
                    new_elements.append(elt)

        # Copy the current measure, minus its elements...
        measure.elements = None
        new_measure = measure.copy()

        # ...and add the new elements.
        new_measure.elements = new_elements

        # Finally, append the result to the top-level variable 'new_measure_list',
        # which contains all measures in the current voice.
        new_measure_list.append(new_measure)

    return new_measure_list


