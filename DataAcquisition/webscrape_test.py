import pytest
from webscrape_functions import soupify
from bs4 import BeautifulSoup


def test_soupify():

    expected_resp = 6
    resp = soupify(
        'https://pantelis.github.io/cs634/docs/common/lectures/ai-intro/course-introduction/')

    # should get 6 tags
    assert len(resp) == expected_resp

    # all tags should be images and have an img src url
    for tag in resp:
        assert tag.name == 'img' and tag['src']
