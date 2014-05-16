import pyxb
import pyxb.utils.domutils as domutils

def file_to_xml_dom_object(filename):
    with open(filename, 'r') as infile:
        xml_data = infile.read()
        dom = resources.musicxml.CreateFromDocument(xml_data)
        return dom

filename = '/Users/fredrik/Documents/voice_test.xml'
# filename = '/Users/fredrik/Dropbox/Philomelos/musicxml_com-reference-samples/ActorPreludeSample.xml'

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
from music_data.tuplet import TupletMixin
from music_data.notations import NotationsMixin
from music_data.slur import SlurMixin
from music_data.glissando import GlissandoMixin
from music_data.directions.dynamics import DynamicsMixin
from music_data.directions.wedge import WedgeMixin
from music_data.beam import BeamMixin
from score_partwise.score_partwise import ScorePartWiseMixin

def register_mixins(dom_object):

    interfaces = {
        resources.musicxml.attributes: (AttributesMixin, object),
        resources.musicxml.backup    : (BackupMixin, object),
        resources.musicxml.barline   : (BarlineMixin, object),
        resources.musicxml.tuplet   : (TupletMixin, object),
        resources.musicxml.credit    : (CreditMixin, object),
        resources.musicxml.direction : (DirectionMixin, object),
        resources.musicxml.forward   : (ForwardMixin, object),
        resources.musicxml.note      : (NoteMixin, object),
        resources.musicxml.notations      : (NotationsMixin, object),
        resources.musicxml.slur      : (SlurMixin, object),
        resources.musicxml.beam      : (BeamMixin, object),
        resources.musicxml.glissando      : (GlissandoMixin, object),
        resources.musicxml.part_group: (PartGroupMixin, object),
        resources.musicxml.pitch     : (PitchMixin, object),
        resources.musicxml.print_    : (PrintMixin, object),
        resources.musicxml.score_part: (ScorePartMixin, object),
        resources.musicxml.dynamics: (DynamicsMixin, object),
        resources.musicxml.sound     : (SoundMixin, object),
        resources.musicxml.wedge     : (WedgeMixin, object),
        }

    for cls, interface in interfaces.iteritems():
        new_bases = cls.__bases__ + interface
        cls.__bases__ = new_bases

    # Track and register "anonymous" classes
    part_cls = dom_object.part[:][0].__class__
    part_cls.__name__ = 'part'
    part_cls.__bases__ = (PartMixin, object)
    measure_cls = dom_object.part[:][0].measure[:][0].__class__
    measure_cls.__name__ = 'measure'
    score_cls = dom_object
    score_cls.__name__ = 'score_partwise'
    score_cls.__class__.__bases__ = (
        HeaderMixin,
        LayoutMixin,
        PaperMixin,
        ScorePartWiseMixin,
        object)

dom = file_to_xml_dom_object(filename)
register_mixins(dom)

print dom.format_parts()
print dom.format_score_block()

# for part in dom.part[:]:
#     print part.lilypond_score_representation

with open('test_out.ly', 'w') as outfile:
    outfile.write(dom.format_parts())
    outfile.write(dom.format_score_block())

# print dom.format_header()  # HeaderMixin
# print dom.format_paper_block()  # HeaderMixin
# print dom.format_layout_block()  # HeaderMixin

# for x in dom.parts[2].chords():
#     print type(x)

# for x in dom.parts[2].grouped_elements():
#     print x, type(x)
#     try:
#         print x.grace_container.elements, '******'
#     except:
#         pass

# \score {
#   << \new StaffGroup <<
#       \new Staff = "Staff_1" <<
#         \set Staff.instrumentName =  "Soprano"
#         \set Staff.shortInstrumentName =  "S"
        
#         \context Voice = "Part_P1_Voice_1" { \"Part_P1_Voice_1" }
        
#         \context Voice = "Part_P1_Voice_2" { \"Part_P1_Voice_2" }
        
#         >>
