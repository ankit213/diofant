import re
import sys
import warnings

import pytest

from diofant.core.cache import clear_cache, USE_CACHE
from diofant.core.compatibility import GROUND_TYPES

sp = re.compile(r'([0-9]+)/([1-9][0-9]*)')


def process_split(session, config, items):
    split = config.getoption("--split")
    if not split:
        return
    m = sp.match(split)
    if not m:
        raise ValueError("split must be a string of the form a/b "
                         "where a and b are ints.")
    i, t = map(int, m.groups())
    start, end = (i - 1)*len(items)//t, i*len(items)//t

    if i < t:
        del items[end:]
    del items[:start]


def pytest_report_header(config):
    return """
cache: %s
ground types: %s
""" % (USE_CACHE, GROUND_TYPES)


def pytest_addoption(parser):
    parser.addoption("--split", action="store", default="", help="split tests")


def pytest_collection_modifyitems(session, config, items):
    process_split(session, config, items)


@pytest.fixture(autouse=True, scope='module')
def file_clear_cache():
    clear_cache()


@pytest.fixture(autouse=True, scope='module')
def check_disabled(request):
    if getattr(request.module, 'disabled', False):
        pytest.skip("test requirements not met.")


@pytest.fixture(autouse=True, scope='session')
def set_displayhook():
    sys.__displayhook__ = sys.displayhook  # https://bugs.python.org/26092


@pytest.fixture(autouse=True, scope='session')
def enable_deprecationwarnings():
    warnings.simplefilter('error', DeprecationWarning)
