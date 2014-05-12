import pyxb

pyxb.RequireValidWhenParsing(False)
pyxb.RequireValidWhenGenerating(False)

import pyxb.utils.domutils as domutils
import resources.musicxml

def file_to_xml_dom_object(filename):

    # with open(filename, 'r') as infile:
    #     xml_data = infile.read()
    #     dom = domutils.StringToDOM(xml_data)
    #     mapped_request = resources.musicxml.CreateFromDOM(dom)
    #     return mapped_request

    with open(filename, 'r') as infile:
        xml_data = infile.read()
        # dom = domutils.StringToDOM(xml_data)
        # mapped_request = resources.musicxml.CreateFromDOM(dom)
        # return mapped_request
        dom = resources.musicxml.CreateFromDocument(xml_data)
        return dom 

filename = '/Users/fredrik/Documents/voice_test.xml'
filename = '/Users/fredrik/Dropbox/Philomelos/musicxml_com-reference-samples/ActorPreludeSample.xml'
# filename = '/Users/fredrik/repos/musicxml2ly/xml2ly/MusicXML-TestSuite/01c-Pitches-NoVoiceElement.xml'
xml = file_to_xml_dom_object(filename)

print xml.part


from load import *
import music_data.note 
import headers.credit
import headers.header

resources.musicxml.note.__bases__  = (music_data.note.NoteInterface, object)
resources.musicxml.pitch.__bases__ = (PitchInterface, object)
resources.musicxml.positive_divisions.__bases__ = (DurationInterface, object)
resources.musicxml.credit.__bases__  = (headers.credit.CreditInterface, object)


try:
    score = xml
    score.__class__.__bases__ = (headers.header.HeaderInterface, object)
    part = xml.part[0].__class__
    part.__bases__ = (PartInterface, object)
except:
    pass


# notes = xml.part[:][0].measure[:][0].note[:]
parts = xml.part[:]

print xml.format_header

print xml.identification.creator[:]
print xml.identification.rights[:]

for part in parts[:]:
    for note in part.notes:
        print note.lilypond_format


