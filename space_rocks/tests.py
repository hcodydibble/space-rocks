"""Testing our Views."""
from pyramid.testing import DummyRequest
import pytest
import os.path

@pytest.fixture
def dummy_request():
    """Set up a dummy request for testing."""
    return DummyRequest()
'''

def test_home_view_returns_dict():
    """Test if home view returns a dictionary."""
    from space_rocks.views.default import home_view
    req = DummyRequest()
    response = home_view(req)
    assert isinstance(response, dict)


def test_about_view_returns_dict():
    """Test if about view returns a dictionary."""
    from space_rocks.views.default import about_view
    req = DummyRequest()
    response = about_view(req)
    assert isinstance(response, dict)


def test_distance_view_returns_dict():
    """Test if distance_view returns a dictionary."""
    from space_rocks.views.default import distance_view
    req = DummyRequest()
    req.matchdict['id'] = 1
    response = distance_view(req)
    assert isinstance(response, dict)


def test_size_view_returns_dict():
    """Test if size_view returns a dictionary."""
    from space_rocks.views.default import size_view
    req = DummyRequest()
    req.matchdict['id'] = 1
    response = size_view(req)
    assert isinstance(response, dict)


def test_absolute_magnitude_viewreturns_dict():
    """Test if absolute_magnitude_view returns a dictionary."""
    from space_rocks.views.default import absolute_magnitude_view
    req = DummyRequest()
    req.matchdict['id'] = 1
    response = absolute_magnitude_view(req)
    assert isinstance(response, dict)
'''

def test_abs_magnitude_graph_exists_no_arguments():
    """Test if absolute magnitude scatter plot is generated with no arguments passed."""
    from space_rocks.views.plot_magnitude import graph_abs_magnitude
    graph_abs_magnitude()
    assert os.path.isfile("static/abs_magnitude.html") 


def test_abs_magnitude_graph_exists_no_arguments():
    """Test if absolute magnitude scatter plot is generated with empty arguments passed."""
    from space_rocks.views.plot_magnitude import graph_abs_magnitude
    graph_abs_magnitude([],[])
    assert os.path.isfile("static/abs_magnitude.html")


def test_abs_magnitude_graph_exists_no_arguments():
    """Test if absolute magnitude scatter plot is generated with same length arguments passed."""
    from space_rocks.views.plot_magnitude import graph_abs_magnitude

    test_abs_mag = [1, 2, 3, 4, 5]
    test_velocity = [2, 5, 8, 2, 7]

    graph_abs_magnitude(test_abs_mag, test_velocity)
    assert os.path.isfile("static/abs_magnitude.html")


