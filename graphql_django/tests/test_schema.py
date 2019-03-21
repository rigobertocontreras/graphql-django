from py.test import raises
from ..schema import create_schema

print('__file__={0:<35} | __name__={1:<20} | __package__={2:<20}'.format(__file__, __name__, str(__package__)))


def test_should_raise_if_app():
    with raises(Exception) as excinfo:

        create_schema()

    assert "valid Django Model" in str(excinfo.value)
