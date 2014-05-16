# class TupletAttribute(TypedStringElement):
#     xml_accessor = 'tuplet'
#     attr_name = ()
#     @classmethod
#     def from_xml(cls, elt):
#         value = elt.attrib.get(cls.attr_name, None)
#         if value:
#             return cls(value)
#         else:
#             return cls()

# class TupletBracketAttribute(TupletAttribute):
#     attr_name = 'bracket'

#     def ly_expression(self):
#         if self == 'no':
#             return "\\once \\override TupletBracket #'stencil = ##f"


# class TupletShowNumberAttribute(TupletAttribute):
#     attr_name = 'show-number'

#     def ly_expression(self):
#         if self == 'both':
#             return "\\once \\override TupletNumber.text = #(tuplet-number::non-default-tuplet-fraction-text {numerator} {denominator})"
#         elif self == 'none':
#             return "#f"
#         elif self == 'actual':
#             # default behavior
#             pass


# class TupletShowTypeAttribute(TupletAttribute):
#     attr_name = 'show-type'


# class TupletTypeAttribute(TupletAttribute):

#     attr_name = 'type'

#     def ly_expression(self):
#         if self == 'start':
#             return '{'
#         elif self == 'stop':
#             return '}'


# class TupletLineShapeAttribute(TupletAttribute):
#     attr_name = 'line-shape'

#     def ly_expression(self):
#         curved = "\\once \\override TupletBracket #'stencil = #ly:slur::print"
#         if self == 'curved':
#             return curved

# class TupletNumberElement(TypedIntElement):
#     xml_accessor = 'tuplet-number'


# class TupletTypeElement(TypedStringElement):
#     xml_accessor = 'tuplet-type'


# class TupletActualElement(BaseItem):
#     xml_accessor = 'tuplet-actual'
#     init_args = (
#         'tuplet_number',
#         'tuplet_type',
#         )
#     tuplet_number = TypedProperty('_tuplet_number', TupletNumberElement)
#     tuplet_type = TypedProperty('_tuplet_type', TupletTypeElement)

#     @classmethod
#     def from_xml(cls, xml):
#         assert xml.tag == 'tuplet'
#         xml = xml.find(cls.xml_accessor)
#         result = super(TupletActualElement, cls).from_xml(xml)
#         return result

# class TupletNormalElement(TupletActualElement):
#     xml_accessor = 'tuplet-normal'

# class TupletTimeModificationElement(TypedStringElement):

#     @classmethod
#     def from_xml(cls, xml):
#         from music_data.Note import TimeModificationElement
#         try:
#             notations_tag = xml.getparent()
#             note = notations_tag.getparent()
#             return TimeModificationElement.from_xml(note)
#         except:
#             pass

class TupletList(object):

    def __init__(self, elements=None):
        if elements is not None:
            self.elements = elements
        else:
            self.elements = []

    @property
    def before_note(self):
        result = []
        for elt in self.elements:
            if elt.before_note is not None:
                result.append(elt.before_note)
        return ' '.join(result)

    @property
    def after_note(self):
        result = []
        for elt in self.elements:
            if elt.after_note is not None:
                result.append(elt.after_note)
        return ' '.join(result)

class TupletMixin(object):

    # TODO: show/hide bracket, line styles, non-conventional tuplet values,
    # TODO: show/hide number

    @property
    def is_opening(self):
        return self.type == 'start'

    @property
    def is_closing(self):
        return self.type == 'stop'

    @property
    def numerator(self):
        return self.tuplet_actual.tuplet_number.value()

    @property
    def denominator(self):
        return self.tuplet_normal.tuplet_number.value()

    @property
    def numerator_note_type(self):
        return self.tuplet_actual.tuplet_type

    @property
    def denominator_note_type(self):
        return self.tuplet_normal.tuplet_type

    @property
    def body(self):
        return "\\tuplet {num}/{denom} {{"

    @property
    def before_note(self):
        if self.is_opening:
            return self.body.format(num=self.numerator, denom=self.denominator)

    @property
    def after_note(self):
        if self.is_closing:
            return '}'
    

