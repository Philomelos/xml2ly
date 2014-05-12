import pyxb
import pyxb.utils.domutils as domutils

def file_to_xml_dom_object(filename):
    with open(filename, 'r') as infile:
        xml_data = infile.read()
        dom = resources.musicxml.CreateFromDocument(xml_data)
        return dom

filename = '/Users/fredrik/Documents/voice_test.xml'

import resources.musicxml

from score_partwise.credit         import CreditMixin
from score_partwise.header         import HeaderMixin
from score_partwise.paper          import PaperMixin
from score_partwise.layout         import LayoutMixin
from music_data.attributes         import AttributesMixin
from music_data.backup             import BackupMixin
from music_data.barline            import BarlineMixin
from music_data.direction          import DirectionMixin
from music_data.forward            import ForwardMixin
from music_data.note               import NoteMixin
from music_data.pitch              import PitchMixin
from music_data.print_             import PrintMixin
from music_data.sound              import SoundMixin
from part.part                     import PartMixin
from part_list.part_group          import PartGroupMixin
from part_list.score_part          import ScorePartMixin
from score_partwise.score_partwise import ScorePartWiseMixin

def register_mixins(dom_object):

    interfaces = {
        resources.musicxml.attributes: (AttributesMixin, object),
        resources.musicxml.backup    : (BackupMixin, object),
        resources.musicxml.barline   : (BarlineMixin, object),
        resources.musicxml.credit    : (CreditMixin, object),
        resources.musicxml.direction : (DirectionMixin, object),
        resources.musicxml.forward   : (ForwardMixin, object),
        resources.musicxml.note      : (NoteMixin, object),
        resources.musicxml.part_group: (PartGroupMixin, object),
        resources.musicxml.pitch     : (PitchMixin, object),
        resources.musicxml.print_    : (PrintMixin, object),
        resources.musicxml.score_part: (ScorePartMixin, object),
        resources.musicxml.sound     : (SoundMixin, object),
        }

    for cls, interface in interfaces.iteritems():
        new_bases = cls.__bases__ + interface
        cls.__bases__ = new_bases

    # Track and register "anonymous" classes
    part_cls = dom_object.part[:][0].__class__
    part_cls.__bases__ = (PartMixin, object)
    score_cls = dom_object
    score_cls.__class__.__bases__ = (
        HeaderMixin,
        LayoutMixin,
        PaperMixin,
        ScorePartWiseMixin,
        object)

dom = file_to_xml_dom_object(filename)
register_mixins(dom)

print dom.format_parts() # ScorePartWiseMixin
print dom.format_header()  # HeaderMixin
print dom.format_paper_block()  # HeaderMixin
print dom.format_layout_block()  # HeaderMixin
