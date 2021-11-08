from web_scraper import __version__
from web_scraper.scraper import get_citations_needed_count,get_citations_needed_report

def test_version():
    assert __version__ == '0.1.0'

def test_get_citations_needed_count():
    url = 'https://en.wikipedia.org'
    expected = 5
    actual = get_citations_needed_count(url)
    assert expected == actual

def test_get_citations_needed_report():
    url = 'https://en.wikipedia.org'
    list_string=get_citations_needed_report(url)
    a=list_string.split("\n")
    expected="The first people to settle in Mexico encountered a climate far milder than the current one. In particular, the Valley of Mexico contained several large paleo-lakes (known collectively as Lake Texcoco) surrounded by dense forest. Deer were found in this area, but most fauna were small land animals and fish and other lacustrine animals were found in the lake region.[citation needed][6] Such conditions encouraged the initial pursuit of a hunter-gatherer existence."
    actual=a[0]
    assert actual==expected