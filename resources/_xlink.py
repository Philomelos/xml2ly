# ./_xlink.py
# -*- coding: utf-8 -*-
# PyXB bindings for NM:b43cd366527ddb6a0e58594876e07421e0148f30
# Generated 2014-05-10 21:39:11.037247 by PyXB version 1.2.3
# Namespace http://www.w3.org/1999/xlink [xmlns:xlink]

import pyxb
import pyxb.binding
import pyxb.binding.saxer
import io
import pyxb.utils.utility
import pyxb.utils.domutils
import sys

# Unique identifier for bindings created at the same time
_GenerationUID = pyxb.utils.utility.UniqueIdentifier('urn:uuid:c0742661-d87a-11e3-a304-d49a200dedda')

# Version of PyXB used to generate the bindings
_PyXBVersion = '1.2.3'
# Generated bindings are not compatible across PyXB versions
if pyxb.__version__ != _PyXBVersion:
    raise pyxb.PyXBVersionError(_PyXBVersion)

# Import bindings for namespaces imported into schema
import pyxb.binding.datatypes

# NOTE: All namespace declarations are reserved within the binding
Namespace = pyxb.namespace.NamespaceForURI(u'http://www.w3.org/1999/xlink', create_if_missing=True)
Namespace.configureCategories(['typeBinding', 'elementBinding'])

def CreateFromDocument (xml_text, default_namespace=None, location_base=None):
    """Parse the given XML and use the document element to create a
    Python instance.

    @param xml_text An XML document.  This should be data (Python 2
    str or Python 3 bytes), or a text (Python 2 unicode or Python 3
    str) in the L{pyxb._InputEncoding} encoding.

    @keyword default_namespace The L{pyxb.Namespace} instance to use as the
    default namespace where there is no default namespace in scope.
    If unspecified or C{None}, the namespace of the module containing
    this function will be used.

    @keyword location_base: An object to be recorded as the base of all
    L{pyxb.utils.utility.Location} instances associated with events and
    objects handled by the parser.  You might pass the URI from which
    the document was obtained.
    """

    if pyxb.XMLStyle_saxer != pyxb._XMLStyle:
        dom = pyxb.utils.domutils.StringToDOM(xml_text)
        return CreateFromDOM(dom.documentElement)
    if default_namespace is None:
        default_namespace = Namespace.fallbackNamespace()
    saxer = pyxb.binding.saxer.make_parser(fallback_namespace=default_namespace, location_base=location_base)
    handler = saxer.getContentHandler()
    xmld = xml_text
    if isinstance(xmld, unicode):
        xmld = xmld.encode(pyxb._InputEncoding)
    saxer.parse(io.BytesIO(xmld))
    instance = handler.rootObject()
    return instance

def CreateFromDOM (node, default_namespace=None):
    """Create a Python instance from the given DOM node.
    The node tag must correspond to an element declaration in this module.

    @deprecated: Forcing use of DOM interface is unnecessary; use L{CreateFromDocument}."""
    if default_namespace is None:
        default_namespace = Namespace.fallbackNamespace()
    return pyxb.binding.basis.element.AnyCreateFromDOM(node, default_namespace)


# Atomic simple type: [anonymous]
class STD_ANON (pyxb.binding.datatypes.NMTOKEN, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location(u'http://www.musicxml.org/xsd/xlink.xsd', 23, 2)
    _Documentation = None
STD_ANON._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=STD_ANON, enum_prefix=None)
STD_ANON.simple = STD_ANON._CF_enumeration.addEnumeration(unicode_value=u'simple', tag=u'simple')
STD_ANON._InitializeFacetMap(STD_ANON._CF_enumeration)

# Atomic simple type: [anonymous]
class STD_ANON_ (pyxb.binding.datatypes.NMTOKEN, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location(u'http://www.musicxml.org/xsd/xlink.xsd', 35, 2)
    _Documentation = None
STD_ANON_._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=STD_ANON_, enum_prefix=None)
STD_ANON_.new = STD_ANON_._CF_enumeration.addEnumeration(unicode_value=u'new', tag=u'new')
STD_ANON_.replace = STD_ANON_._CF_enumeration.addEnumeration(unicode_value=u'replace', tag=u'replace')
STD_ANON_.embed = STD_ANON_._CF_enumeration.addEnumeration(unicode_value=u'embed', tag=u'embed')
STD_ANON_.other = STD_ANON_._CF_enumeration.addEnumeration(unicode_value=u'other', tag=u'other')
STD_ANON_.none = STD_ANON_._CF_enumeration.addEnumeration(unicode_value=u'none', tag=u'none')
STD_ANON_._InitializeFacetMap(STD_ANON_._CF_enumeration)

# Atomic simple type: [anonymous]
class STD_ANON_2 (pyxb.binding.datatypes.NMTOKEN, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location(u'http://www.musicxml.org/xsd/xlink.xsd', 47, 2)
    _Documentation = None
STD_ANON_2._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=STD_ANON_2, enum_prefix=None)
STD_ANON_2.onRequest = STD_ANON_2._CF_enumeration.addEnumeration(unicode_value=u'onRequest', tag=u'onRequest')
STD_ANON_2.onLoad = STD_ANON_2._CF_enumeration.addEnumeration(unicode_value=u'onLoad', tag=u'onLoad')
STD_ANON_2.other = STD_ANON_2._CF_enumeration.addEnumeration(unicode_value=u'other', tag=u'other')
STD_ANON_2.none = STD_ANON_2._CF_enumeration.addEnumeration(unicode_value=u'none', tag=u'none')
STD_ANON_2._InitializeFacetMap(STD_ANON_2._CF_enumeration)
