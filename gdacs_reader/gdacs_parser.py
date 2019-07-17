import re
from geojson import Point, Polygon
import xml.etree.ElementTree as ET


class GdacsXmlParser:

    def xml_to_dict(self, item):

        item_dict = {}

        for child in item:

            # Remove urls in curly braces
            tag = re.sub(r'\{(.*)\}', '', child.tag)
            item_dict[tag] = child.text

            for key, attrib in child.attrib.items():
                item_dict["{}_{}".format(tag, key)] = attrib

        return item_dict

    def parse(self, xml):
        xml_tree = ET.fromstring(xml)

        # Setup initial disaster list
        disasters = [self.xml_to_dict(item) for item in xml_tree.iter('item')]

        # Fix field names and formatting
        for idx, disaster in enumerate(disasters):

            # Format location fields into GeoJSON
            pt = [float(n) for n in disaster['point'].split()]
            disasters[idx]['location_point'] = Point([pt[1], pt[0]])

            bb = [float(n) for n in disaster['bbox'].split()]
            disasters[idx]['location_polygon'] = Polygon([
                (bb[2], bb[0]), (bb[2], bb[1]),
                (bb[3], bb[1]), (bb[3], bb[0])])

            # Clean up some fields...
            disasters[idx].pop('Point')
            disasters[idx].pop('bbox')

        return disasters
