import requests

from . import gdacs_parser


parser = gdacs_parser.GdacsXmlParser()


def fetch(url="http://www.gdacs.org/xml/rss_24h.xml", offset=3):
    results = requests.get(url)

    # skip first 3 characters
    results_text = results.text[offset:]
    disasters = parser.parse(results_text)
    print(disasters)

    return disasters
