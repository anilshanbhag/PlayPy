import urllib2
from lxml import html
from lxml.cssselect import CSSSelector
from dateutil.parser import parse

class PlayAPI:
    PACKAGE_URL = "https://play.google.com/store/apps/details?id=%s"

    def __init__(self, debug = False):
        self.debug = debug

    def get_last_updated(self, tree):
        sel = CSSSelector('div[itemprop="datePublished"]')
        matches = tree.xpath(sel.path)
        assert len(matches) == 1
        updated = parse(matches[0].text)
        return updated

    def get_ratings(self, tree):
        sel = CSSSelector('.rating-bar-container .bar-number')
        matches = tree.xpath(sel.path)
        ratings = [int(x.text.replace(',','')) for x in matches]
        return ratings

    def get_stats(self, package):
        content = urllib2.urlopen(self.PACKAGE_URL % package).read()
        tree = html.fromstring(content)
        ratings = self.get_ratings(tree)
        last_updated = self.get_last_updated(tree)
        if self.debug:
            print "Number of ratings:"
            for i in xrange(0, 5):
                print 5-i, ":", ratings[i]

            print "Last Updated: ", last_updated
        else:
            return (ratings, last_updated)

