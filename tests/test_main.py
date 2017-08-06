import os
import pytest
from getsize import main


def test_approximate_size():
    with pytest.raises(ValueError) as excinfo:
        main.approximate_size(-1)
    assert str(excinfo.value) == 'number must be non-negative'

    assert main.approximate_size(10000) == '9.8 KiB'

    assert main.approximate_size(
        10000, a_kilobyte_is_1024_bytes=False
    ) == '10.0 KB'

    with pytest.raises(ValueError) as excinfo:
        main.approximate_size(100**100)
    assert str(excinfo.value) == 'number too large'


def test_get_size():
    sample_file = os.path.join('tests', 'sample', 'sample1.png')
    assert main.get_size(sample_file) == 473831

    sample_dir = os.path.join('tests', 'sample')
    assert main.get_size(sample_dir) == 473831*4
