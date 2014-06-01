import xml2ly

def xml_string_to_dom(xml):
    import pyxb.utils.domutils as domutils
    import resources.musicxml
    from xml2ly import register_mixins
    dom = resources.musicxml.CreateFromDocument(xml)
    register_mixins(dom)
    return dom

class TestPaper:

    xml = """
    <score-partwise>
    <defaults>
        <scaling>
          <millimeters>6.35</millimeters>
          <tenths>40</tenths>
        </scaling>
        <page-layout>
          <page-height>1760</page-height>
          <page-width>1360</page-width>
          <page-margins type="both">
            <left-margin>80</left-margin>
            <right-margin>80</right-margin>
            <top-margin>80</top-margin>
            <bottom-margin>80</bottom-margin>
          </page-margins>
        </page-layout>
        <system-layout>
          <system-margins>
            <left-margin>0</left-margin>
            <right-margin>0</right-margin>
          </system-margins>
          <system-distance>127</system-distance>
          <top-system-distance>127</top-system-distance>
        </system-layout>
        <staff-layout>
          <staff-distance>80</staff-distance>
        </staff-layout>
        <appearance>
          <line-width type="stem">1.25</line-width>
          <line-width type="beam">5</line-width>
          <line-width type="staff">0.8333</line-width>
          <line-width type="light barline">2.0833</line-width>
          <line-width type="heavy barline">6.6667</line-width>
          <line-width type="leger">1.25</line-width>
          <line-width type="ending">0.7682</line-width>
          <line-width type="wedge">0.957</line-width>
          <line-width type="enclosure">1.6667</line-width>
          <line-width type="tuplet bracket">1.3542</line-width>
          <note-size type="grace">66</note-size>
          <note-size type="cue">66</note-size>
          <distance type="hyphen">60</distance>
          <distance type="beam">8</distance>
        </appearance>
        <music-font font-family="Maestro,engraved" font-size="18"/>
        <word-font font-family="Times New Roman" font-size="8.25"/>
        <lyric-font font-family="Times New Roman" font-size="10"/>
      </defaults>
    </score-partwise>
    """

    def test_paper_default_global_staff_size(self):
        dom = xml_string_to_dom(self.xml)
        assert dom.default_global_staff_size == 20

        
        
