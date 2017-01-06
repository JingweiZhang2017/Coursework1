from graph import Greengraph
from map import Map
import numpy as np
from matplotlib import image as img

from nose.tools import assert_raises, assert_almost_equal, assert_equal
from mock import Mock, patch
import os
import yaml

from numpy import testing




def geolocate_testing():
    with open(os.path.join(os.path.dirname(__file__),'fixtures', 'geolocate_samples.yaml')) as fixtures_file:
        fixtures = yaml.load(fixtures_file)
        for fixture in fixtures:
            mygraph=Greengraph('', '')
            mygraph.geocoder.geocode = Mock(return_value=[[0,fixture['result']]])
            result = mygraph.geolocate(fixture['city'])
            assert_equal(fixture['result'], list(result))


def test_location_sequence():
    result=Greengraph.location_sequence(Greengraph("",""), (0,0),(10,10),5)
    np.testing.assert_equal(result[0],(0,0))
    np.testing.assert_equal(result[1],(2.5,2.5))

