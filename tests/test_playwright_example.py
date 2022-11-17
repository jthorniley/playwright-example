from playwright_example import __version__
import pytest


@pytest.mark.django_db
def test_playwright_page(page):
    assert page is None
