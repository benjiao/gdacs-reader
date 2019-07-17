import json
from gdacs_reader import gdacs_parser
from unittest2 import TestCase

test_data = {
    "title": "Green flood alert in Nepal",
    "description": "On 01/07/2019, a flood started in Nepal, lasting until 01/08/2019 (last update). The flood caused 64 deaths and 3186 families  displaced .",
    "enclosure": None,
    "enclosure_type": "image/png",
    "enclosure_length": 1.0,
    "enclosure_url": "http://dma.gdacs.org/saved/gdacs/fl/dfo2019_1100100.png",
    "temporary": True,
    "link": "http://www.gdacs.org/report.aspx?eventtype=FL&eventid=1100100",
    "pubDate": "2019-08-01T15:00:00Z",
    "iscurrent": False,
    "fromdate": "2019-07-01T15:00:00Z",
    "todate": "2019-08-01T15:00:00Z",
    "durationindays": 31.0,
    "durationinweek": 4.0,
    "year": "2019",
    "subject": "FL1",
    "guid": "FL1100100",
    "guid_isPermaLink": True,
    "cap": "http://www.gdacs.org/contentdata/resources/FL/1100100/cap_1100100.xml",
    "icon": "http://www.gdacs.org/Images/gdacs_icons/alerts/Green/FL.png",
    "version": "1",
    "eventtype": "FL",
    "alertlevel": "Green",
    "alertscore": 0.5,
    "episodealertlevel": "Green",
    "episodealertscore": 1.0,
    "eventname": None,
    "eventid": 1100100,
    "episodeid": 1,
    "calculationtype": None,
    "severity": "Magnitude 0 ",
    "severity_unit": "",
    "severity_value": 0.0,
    "population": "64 deaths and 3186 families  displaced ",
    "population_unit": "Population Affected",
    "population_value": 64,
    "vulnerability": None,
    "vulnerability_value": 0.0,
    "iso3": "NP",
    "country": "Nepal",
    "glide": None,
    "mapimage": None,
    "maplink": None,
    "gtsimage": None,
    "gtslink": None,
    "resources": "\n        ",
    "identifiers": "\n        ",
    "location_point": {
        "type": "Point",
        "coordinates": [
            84.137763,
            27.934800000000006
        ]
    },
    "location_polygon": {
        "type": "Polygon",
        "coordinates": [
            [
                23.9348,
                80.137763
            ],
            [
                23.9348,
                88.137763
            ],
            [
                31.9348,
                88.137763
            ],
            [
                31.9348,
                80.137763
            ]
        ]
    }
}


class TestParser(TestCase):
    def setUp(self):
        pass

    def testParse24h(self):
        with open('tests/data/rss_24h.xml', 'r') as f:
            xml_string = f.read()

        parser = gdacs_parser.GdacsXmlParser()
        disasters = parser.parse(xml_string)
        self.assertDictEqual(disasters[0], test_data)
