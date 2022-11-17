from gendiff.parser import generate_diff
from gendiff.parser import prepare_data
from gendiff.parser import parse
from gendiff.parser import normalize_values
from tests import get_path
import json
from os.path import splitext
import pytest


@pytest.mark.parametrize(
    "file1, file2, expected",
    [
        pytest.param(
            'file1.json',
            'file2.json',
            'correct.txt',
            id="flat_json_file"
        ),
    ]
)
def test_gen_diff(file1, file2, expected):
    expected_path = get_path(expected)
    with open(expected_path, 'r') as file:
        result = file.read()
        file1 = get_path(file1)
        file2 = get_path(file2)
        assert generate_diff(file1, file2) == result
