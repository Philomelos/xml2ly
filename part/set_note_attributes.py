from copy import copy
from music_data.attributes import ElementAttributes
from resources.musicxml import attributes

def set_note_attributes(measure_list):

    curr_attr = ElementAttributes()

    for measure in measure_list:
        for elt in measure.elements:
            if isinstance(elt, attributes):
                measure_attributes = measure.attributes[:]
                curr_attr.update(measure_attributes)
            else:
                # initialize attributes and directions
                elt.attributes = copy(curr_attr)
                elt.directions = None
