from copy import copy
from music_data.attributes import ElementAttributes

def set_note_attributes(measure_list):

    curr_attr = ElementAttributes()

    for measure in measure_list:
        measure_attributes = measure.attributes[:]
        curr_attr.update(measure_attributes)
        for elt in measure.elements:
            elt.attributes = copy(curr_attr)
