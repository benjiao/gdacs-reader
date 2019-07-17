import re
from datetime import datetime
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

    def str_to_bool(self, s):
        if isinstance(s, str):
            return s.lower() == 'false'
        else:
            return s

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
            disasters[idx].pop('point')
            disasters[idx].pop('bbox')

            # Convert time strings into iso format
            disasters[idx]['fromdate'] = datetime.strptime(disaster['fromdate'], "%a, %d %b %Y %H:%M:%S %Z").isoformat() + "Z"
            disasters[idx]['todate'] = datetime.strptime(disaster['todate'], "%a, %d %b %Y %H:%M:%S %Z").isoformat() + "Z"
            disasters[idx]['pubDate'] = datetime.strptime(disaster['pubDate'], "%a, %d %b %Y %H:%M:%S %Z").isoformat() + "Z"

            # Convert numbers strings into numbers
            disasters[idx]['eventid'] = int(disasters[idx]['eventid'])
            disasters[idx]['episodeid'] = int(disasters[idx]['episodeid'])
            disasters[idx]['population_value'] = int(disasters[idx]['population_value'])

            disasters[idx]['durationindays'] = float(disasters[idx]['durationindays'])
            disasters[idx]['durationinweek'] = float(disasters[idx]['durationinweek'])
            disasters[idx]['enclosure_length'] = float(disasters[idx]['enclosure_length'])
            disasters[idx]['alertscore'] = float(disasters[idx]['alertscore'])
            disasters[idx]['episodealertscore'] = float(disasters[idx]['episodealertscore'])
            disasters[idx]['severity_value'] = float(disasters[idx]['severity_value'])
            disasters[idx]['vulnerability_value'] = float(disasters[idx]['vulnerability_value'])

            # Convert boolean strings into boolean
            disasters[idx]['temporary'] = self.str_to_bool(disasters[idx]['temporary'])
            disasters[idx]['iscurrent'] = self.str_to_bool(disasters[idx]['iscurrent'])
            disasters[idx]['guid_isPermaLink'] = self.str_to_bool(disasters[idx]['guid_isPermaLink'])

        return disasters
