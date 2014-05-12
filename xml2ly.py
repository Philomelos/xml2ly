import pyxb

# pyxb.RequireValidWhenParsing(False)
# pyxb.RequireValidWhenGenerating(False)

import pyxb.utils.domutils as domutils

def file_to_xml_dom_object(filename):
    # with open(filename, 'r') as infile:
    #     xml_data = infile.read()
    #     dom = domutils.StringToDOM(xml_data)
    #     mapped_request = resources.musicxml.CreateFromDOM(dom)
    #     return mapped_request
    with open(filename, 'r') as infile:
        xml_data = infile.read()
        dom = resources.musicxml.CreateFromDocument(xml_data)
        return dom 

filename = '/Users/fredrik/Documents/voice_test.xml'
# filename = '/Users/fredrik/Dropbox/Philomelos/musicxml_com-reference-samples/ActorPreludeSample.xml'
# filename = '/Users/fredrik/repos/musicxml2ly/xml2ly/MusicXML-TestSuite/01c-Pitches-NoVoiceElement.xml'

# from load import *

import resources.musicxml

from music_data.note import NoteMixin
from music_data.barline import BarlineMixin
from music_data.forward import ForwardMixin
from music_data.backup import BackupMixin
from music_data.pitch import PitchMixin
from music_data.direction import DirectionMixin
from music_data.attributes import AttributesMixin
from music_data.sound import SoundMixin
from score_partwise import ScorePartWiseMixin
from headers.credit import CreditMixin
from headers.header import HeaderMixin
from part.part import PartMixin
from part_list.part_group import PartGroupMixin
from part_list.score_part import ScorePartMixin
from music_data.print_ import PrintMixin

xml = file_to_xml_dom_object(filename)

interfaces = {
    resources.musicxml.credit: (CreditMixin, object),
    resources.musicxml.attributes: (AttributesMixin, object),
    resources.musicxml.note: (NoteMixin, object),
    resources.musicxml.barline: (BarlineMixin, object),
    resources.musicxml.sound: (SoundMixin, object),
    resources.musicxml.backup: (BackupMixin, object),
    resources.musicxml.forward: (ForwardMixin, object),
    resources.musicxml.direction: (DirectionMixin, object),
    resources.musicxml.part_group: (PartGroupMixin, object),
    resources.musicxml.print_: (PrintMixin, object),
    resources.musicxml.score_part: (ScorePartMixin, object),
    resources.musicxml.pitch: (PitchMixin, object),
    # resources.musicxml.positive_divisions: (DurationMixin, object),
    }

for cls, interface in interfaces.iteritems():
    new_bases = cls.__bases__ + interface
    cls.__bases__ = new_bases

score_cls = xml
score_cls.__class__.__bases__ = (
    ScorePartWiseMixin,
    HeaderMixin,
    object)
part_cls = xml.part[:][0].__class__
part_cls.__bases__ = (PartMixin, object)


def music_events(part):
    result = [] 
    current_attributes = None
    for measure in part.measure[:]:
        attr = measure.attributes
        if attr:
            current_attributes = attr[0]
        for elt in measure.content():
            if current_attributes:
                elt.attributes = current_attributes
            result.append(elt)
    return result


# print xml.format_header
print xml.format_parts()
# print xml.format_score_block()

