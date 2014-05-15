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

class TupletMixin(object):

    @property
    def is_opening(self):
        return self.type == 'start'

    @property
    def is_closing(self):
        return self.type == 'stop'

    @property
    def lilypond_format(self):
        # if self.is_opening:
        #     return '\\tuplet 3/2 {'
        # elif self.is_closing:
        #     return '}'
        return ''

    # xml_accessor = 'tuplet'
    # init_args = (
    #     'bracket',
    #     'show_number',
    #     'show_type',
    #     'type_',
    #     'line_shape',

    #     'tuplet_actual',
    #     'tuplet_normal',
    #     'tuplet_time_modification',
    #     )

    # bracket = TypedProperty('_bracket', TupletBracketAttribute)
    # show_number = TypedProperty('_show_number', TupletShowNumberAttribute)
    # show_type = TypedProperty('_show_type', TupletShowNumberAttribute)
    # type_ = TypedProperty('_type', TupletTypeAttribute)
    # line_shape = TypedProperty('_line_shape', TupletLineShapeAttribute)

    # tuplet_actual = TypedProperty('_tuplet_actual', TupletActualElement)
    # tuplet_normal = TypedProperty('_tuplet_normal', TupletNormalElement)

    # tuplet_time_modification = TypedProperty(
    #     '_tuplet_time_modification',
    #     TupletTimeModificationElement)

    # @property
    # def numerator(self):
    #     if self.tuplet_actual.tuplet_number:
    #         return self.tuplet_actual.tuplet_number
    #     else:
    #         return self.tuplet_time_modification.actual_notes

    # @property
    # def denominator(self):
    #     if self.tuplet_normal.tuplet_number:
    #         return self.tuplet_normal.tuplet_number
    #     else:
    #         return self.tuplet_time_modification.normal_notes

    # def opening_ly_expression(self):
    #     from fractions import Fraction
    #     cmd = '\\tuplet {ratio} {{'
    #     return cmd.format(ratio=Fraction(self.numerator, self.denominator))

    # def closing_ly_expression(self):
    #     return '}'

    # def print_before(self, printer):
    #     if self.type_ == 'start':
    #         printer.dump(self.opening_ly_expression())

    # def print_after(self, printer):
    #     if self.type_ == 'stop':
    #         printer.dump(self.closing_ly_expression())


