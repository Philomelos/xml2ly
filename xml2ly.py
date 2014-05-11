import pyxb.utils.domutils as domutils
import resources.musicxml

def file_to_xml_dom_object(filename):

    with open(filename, 'r') as infile:
        xml_data = infile.read()
        dom = domutils.StringToDOM(xml_data)
        mapped_request = resources.musicxml.CreateFromDOM(dom)

        return mapped_request

filename = '/Users/fredrik/Documents/voice_test.xml'
# filename = '/Users/fredrik/repos/musicxml2ly/xml2ly/MusicXML-TestSuite/01c-Pitches-NoVoiceElement.xml'
xml = file_to_xml_dom_object(filename)

from load import *
import music_data.note 

resources.musicxml.note.__bases__  = (music_data.note.NoteInterface, object)
resources.musicxml.pitch.__bases__ = (PitchInterface, object)
resources.musicxml.positive_divisions.__bases__ = (DurationInterface, object)

try:
    part = xml.part[0].__class__
    part.__bases__ = (PartInterface, object)
except:
    pass


notes = xml.part[:][0].measure[:][0].note[:]


# # for note in notes:
# #     a = note.lilypond_format
# #     if a is not None:
# #         print a

parts = xml.part[:]

for part in parts:
    for note in part.notes:
        print note.lilypond_format

class Header(object):

    def __init__(self, xml):
        self.xml=xml

    @property
    def credits(self):
        result = {}
        for x in self.xml.credit[:]:
            if len(x.credit_type) > 0: 
                result[x.credit_type[0]] = x.credit_words
        return result

    @property
    def movement_title(self):
        movement_title = MovementTitle(self.xml.movement_title)
        return movement_title.lilypond_format

    @property
    def lilypond_format(self):
        print '\\header {'
        # public_props = (name for name in dir(self.xml) if not name.startswith('_'))
        # for arg in public_props:
        #     cls = classes.get(arg, None)
        #     if cls:
        #         obj = cls()
        #         print obj
        #         # print obj.lilypond_format
        


# part = Header(xml)
# part.lilypond_format

# for part in xml.part[:]:
#     for measure in part.measure[:]:
#         for note in measure.note[:]:
#             print print_note(note)
#             # n = classes[note.__class__.__name__]
#             # instance = n(obj=note)
#             # print instance.lilypond_format()

#             # note = build_new_cls(note)
#             # # NoteElement.lilypond_format(note)
#             # print note, note.is_rest, note.lilypond_format, note.duration
