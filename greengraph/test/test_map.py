

from ..map import Map
import os
import yaml
from matplotlib import image as img
import geopy
import requests
from mock import Mock,patch
from nose.tools import assert_raises, assert_equal
import numpy as np
from numpy import testing






def Map_initial_test():
    with open(os.path.join(os.path.dirname(__file__), 'fixtures', 'London.png')) as mockimage:
      pixels = np.load(os.path.join(os.path.dirname(__file__), 'fixtures', 'London.npy'))
      with patch('requests.get', return_value=Mock(content=mockimage.read())) as mock_get:
        testMap = Map(51.5072,-0.1275)
        np.testing.assert_allclose(testMap.pixels,pixels)



def green_test(mock_get, mockimage):
    with open(os.path.join(os.path.dirname(__file__),'fixtures', '.yaml')) as fixtures_file:
        fixture = yaml.load(fixtures_file)
        testMap = Map(fixture['long'], fixture['lat'], size=(5, 5))
        testresult = testMap.green(fixture['threshold'])
        np.testing.assert_array_equal(np.asarray(fixture['result']), testresult)


def count_test(mock_get, mockimage):
    with open(os.path.join(os.path.dirname(__file__),'fixtures', '.yaml')) as fixtures_file:
        fixture = yaml.load(fixtures_file)
        testMap = Map(fixture['long'], fixture['lat'], size=(5,5))
        testcount= testMap.count_green(fixture['threshold'])
        np.testing.assert_array_equal(np.asarray(fixture['count']), testcount)


