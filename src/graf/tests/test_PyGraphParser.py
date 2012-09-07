# -*- coding: utf-8 -*-
#
# Poio Tools for Linguists
#
# Copyright (C) 2009-2012 Poio Project
# Author: António Lopes <alopes@cidles.eu>
# URL: <http://www.cidles.eu/ltll/poio>
# For license information, see LICENSE.TXT
"""This module contains the tests to the class
PyGraphParser in module PyGraphParser.

This test serves to ensure the viability of the
methods of the class PyGraphParser in PyGraphParser.py.
"""
import xml

from graf.PyGraphParser import PyGraphParser
from graf.PyAnnotationSet import PyAnnotationSet
from graf.PyAnnotationSpace import PyAnnotationSpace
from graf.PyNode import PyNode
from graf.PyEdge import PyEdge
from graf.PyRegion import PyRegion
from graf.PyStandoffHeader import PyStandoffHeader

# Create the Annotation Graph
gparser = PyGraphParser()

class TestPyGraphParser:
    """
    This class contain the test methods if the class PyGraphParser.

    """

    def test_parse(self):
        """Raise an assertion if can't find a file.

        Return a PyGraph.

        Raises
        ------
        AssertionError
            If the can't find the file.

        """

        # Test values
        file = '/home/alopes/nltk_data/corpora/masc/spoken/Day3PMSession-vc.xml'

        assert(gparser.parse(file, None))

    def test_startElement(self):
        """Raise an assertion if can't set the tag value.

        Processes the opening xml tags, according to their type.
        It's a method from ContentHandler class.

        Raises
        ------
        AssertionError
            If can't set the tag value.

        """

        # Test values
        name = 'graph' # This value changes among the results.
        attrs = {'xmlns': 'http://www.xces.org/ns/GrAF/1.0/'}
        # Is need to instance the value to the SAX type
        attrs = xml.sax.xmlreader.AttributesImpl(attrs)

        # If name variable change to newname requires the graph_'newname'
        assert(gparser.startElement(name, attrs) == gparser.graph_start(attrs))

    # Move to the note important test neither API important part
    def test_characters(self):
        """Raise an assertion if can't set the character.

        Processes any characters within the xml file.
        It's a method from ContentHandler class.

        Raises
        ------
        AssertionError
            If can't set the character.

        """

        # Test values
        ch = '\n'

        assert(gparser.characters(ch))

    def test_endElement(self):
        """Raise an assertion if can't find the node to end.

        Processes the end xml tags, according to their type.
        It's a method from ContentHandler class.

        Raises
        ------
        AssertionError
            If value is not the expected.

        """

        # Test values
        name = 'graph' # This value changes among the results.
        attrs = {'xmlns': 'http://www.xces.org/ns/GrAF/1.0/'}
        # Is need to instance the value to the SAX type
        attrs = xml.sax.xmlreader.AttributesImpl(attrs)

        # Is need to start at least one node
        gparser.startElement(name, attrs)

        # If name variable change to newname requires the graph_'newname'
        assert(gparser.endElement(name) == gparser.graph_end())

    def test_graph_start(self):
        """Raise an assertion if can't set the tag value.

        Processes the opening xml tags, according to their type.
        It's a method from ContentHandler class.

        Raises
        ------
        AssertionError
            If can't set the tag value.

        """

        # Test values
        name = 'graph' # This value changes among the results.
        attrs = {'xmlns': 'http://www.xces.org/ns/GrAF/1.0/'}
        # Is need to instance the value to the SAX type
        attrs = xml.sax.xmlreader.AttributesImpl(attrs)

        # If name variable change to newname requires the graph_'newname'
        assert(gparser.graph_start(attrs))

    def test_graph_end(self):
        """Raise an assertion if can't set the tag value.

        Executes when the parser encounters the end graph tag.
        Sets the root node and adds all the edges to the graph.
        Neither of these tasks can be safely performed until all nodes
        have been added.

        Raises
        ------
        AssertionError
            If can't set the tag value.

        """

        # Test values
        name = 'graph' # This value changes among the results.
        attrs = {'xmlns': 'http://www.xces.org/ns/GrAF/1.0/'}
        # Is need to instance the value to the SAX type
        attrs = xml.sax.xmlreader.AttributesImpl(attrs)
        gparser.ann_start(attrs)

        # If name variable change to newname requires the graph_'newname'
        assert(gparser.graph_end())

    def test_node_start(self):
        """Raise an assertion if can't set the tag value.

        Executes when the parser encounters the end graph tag.
        Sets the root node and adds all the edges to the graph.
        Neither of these tasks can be safely performed until all nodes
        have been added.

        Raises
        ------
        AssertionError
            If can't set the tag value.

        """

        # Test values
        attrs = {u'xml:id': u'penn-n0'}
        # Is need to instance the value to the SAX type
        attrs = xml.sax.xmlreader.AttributesImpl(attrs)

        # If name variable change to newname requires the graph_'newname'
        assert(gparser.node_start(attrs))

    def test_node_end(self):
        """Raise an assertion if can't set the tag value.

        Executes when the parser encounters the end graph tag.
        Sets the root node and adds all the edges to the graph.
        Neither of these tasks can be safely performed until all nodes
        have been added.

        Raises
        ------
        AssertionError
            If can't set the tag value.

        """

        # Test values
        attrs = {u'xml:id': u'penn-n0'}
        # Is need to instance the value to the SAX type
        attrs = xml.sax.xmlreader.AttributesImpl(attrs)

        assert(gparser.node_end())

    def annotation_set_start(self):
        """Raise an assertion if can't set the annotation set
        start.

        Used to parse <annotationSet .../> elements in the XML
        representation.

        Raises
        ------
        AssertionError
        If can't set the value.

        """

        # Test values
        attrs = {u'xml:id': u'penn-n0'}
        # Is need to instance the value to the SAX type
        attrs = xml.sax.xmlreader.AttributesImpl(attrs)

        assert(gparser.annotation_set_start(attrs))

    def test_annotation_space_start(self):
        """Raise an assertion if can't set the annotation sapce
        start.

        Used to parse <annotationSpace .../> elements in the XML
        representation.

        Raises
        ------
        AssertionError
        If can't set the value.

        """

        # Test values
        attrs = {u'xml:id': u'penn-n0'}
        # Is need to instance the value to the SAX type
        attrs = xml.sax.xmlreader.AttributesImpl(attrs)

        assert(gparser.annotation_space_start(attrs))

    def test_ann_start(self):
        """Raise an assertion if can't set annotation start.

        Raises
        ------
        AssertionError
        If can't set the value.

        """

        # Test values
        attrs = {u'xml:id': u'penn-n0'}
        # Is need to instance the value to the SAX type
        attrs = xml.sax.xmlreader.AttributesImpl(attrs)

        assert(gparser.ann_start(attrs))

    def test_ann_end(self):
        """Raise an assertion if can't set annotation end.

        Raises
        ------
        AssertionError
        If can't set the value.

        """

        # Test values

        assert(gparser.ann_end())

    def test_edge_start(self):
        """Raise an assertion if can't set edge.

        Used to parse edge elements in the XML representation.
        Edge information is stored and the edges are added after
        all nodes/spans have been parsed.

        Raises
        ------
        AssertionError
        If can't set the value.

        """

        # Test values
        attrs = {u'xml:id': u'penn-n0'}
        # Is need to instance the value to the SAX type
        attrs = xml.sax.xmlreader.AttributesImpl(attrs)

        assert(gparser.edge_start(attrs))

    def test_region_start(self):
        """Raise an assertion if can't set region.

        Used to pare the region elements in the XML representation.
        A tolkenizer is used to separate the anchors listed in the XML tag,
        and a new PyAnchor instance is created for each one.
        A PyRegion instance is then created with the id from the
        XML tag and added to the graph.

        Raises
        ------
        AssertionError
        If can't set the value.

        """

        # Test values
        attrs = {u'xml:id': u'penn-n0'}
        # Is need to instance the value to the SAX type
        attrs = xml.sax.xmlreader.AttributesImpl(attrs)

        assert(gparser.region_start(attrs))

    def test_fs_start(self):
        """Raise an assertion if can't set inside feature start.

        Used to parse <fs> elements in the XML representation.

        Raises
        ------
        AssertionError
        If can't set the value.

        """

        # Test values
        attrs = {u'xml:id': u'penn-n0'}
        # Is need to instance the value to the SAX type
        attrs = xml.sax.xmlreader.AttributesImpl(attrs)

        assert(gparser.fs_start(attrs))

    def test_fs_end(self):
        """Raise an assertion if can't set inside feature end.

        Used to parse </fs> elements in the XML representation.

        Raises
        ------
        AssertionError
        If can't set the value.

        """

        # Test values

        assert(gparser.fs_end())

    def test_feature_start(self):
        """Raise an assertion if can't set feature start.

        Used to parse start features elements in the XML
        representation.

        Raises
        ------
        AssertionError
        If can't set the value.

        """

        # Test values
        attrs = {u'xml:id': u'penn-n0'}
        # Is need to instance the value to the SAX type
        attrs = xml.sax.xmlreader.AttributesImpl(attrs)

        assert(gparser.feature_start(attrs))

    def test_feature_end(self):
        """Raise an assertion if can't set the feature end.

        Used to parse end features elements in the XML representation.

        Raises
        ------
        AssertionError
        If can't set the value.

        """

        # Test values

        assert(gparser.feature_end())


    def test_as_start(self):
        """Raise an assertion if can't set the start of the
        annotation set.

        Used to parse start <as/ ...> elements in the XML representation.

        Raises
        ------
        AssertionError
        If can't set the value.

        """

        # Test values
        attrs = {u'xml:id': u'penn-n0'}
        # Is need to instance the value to the SAX type
        attrs = xml.sax.xmlreader.AttributesImpl(attrs)

        assert(gparser.as_start(attrs))

    def test_as_end(self):
        """Raise an assertion if can't set the end of the
        annotation set.

         Used to parse end /as> elements in the XML representation.

        Raises
        ------
        AssertionError
        If can't set the value.

        """

        # Test values

        assert(gparser.as_end())

    def test_link_start(self):
        """Raise an assertion if can't set the link.

        Used to parse link elements in the XML representation.

        Raises
        ------
        AssertionError
        If can't set the value.

        """

        # Test values
        attrs = {u'xml:id': u'penn-n0'}
        # Is need to instance the value to the SAX type
        attrs = xml.sax.xmlreader.AttributesImpl(attrs)

        assert(gparser.link_start(attrs))

    def test_depends_on_start(self):
        """Raise an assertion if can't set the dependencies.

        Used to parse dependsOn elements in the XML representation.
        Finds other XML annotation files on which depend the current
        XML file. Parses the dependency files and adds the resulting graph
        to the current graph.

        Raises
        ------
        AssertionError
        If can't set the value.

        """

        # Test values
        attrs = {u'xml:id': u'penn-n0'}
        # Is need to instance the value to the SAX type
        attrs = xml.sax.xmlreader.AttributesImpl(attrs)

        assert(gparser.depends_on_start(attrs))


    def test_root_start(self):
        """Raise an assertion if can't find the start root.

        Used to parse start root elements in the XML representation.
        The root characters are processed by the characters() method
        and stored in self._buffer.

        self._root_element is a flag indicating the presence of a root.

        Raises
        ------
        AssertionError
            If can't set the value.

        """

        # Test values
        attrs = {u'xml:id': u'penn-n0'}
        # Is need to instance the value to the SAX type
        attrs = xml.sax.xmlreader.AttributesImpl(attrs)

        assert(gparser.root_start(attrs))

    def test_root_end(self):
        """Raise an assertion if can't find the end root.

        Used to parse end root elements in the XML representation.

        Raises
        ------
        AssertionError
            If can't set the value.

        """

        assert(gparser.root_end())