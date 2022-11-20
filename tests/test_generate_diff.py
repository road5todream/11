from gendiff.generate import generate_diff
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
            'correct1.txt',
            id="flat_json_file"
        ),
        pytest.param(
            'file1.yaml',
            'file2.yaml',
            'correct1.txt',
            id="flat_yaml_file"
        ),
        pytest.param(
            'file3.json',
            'file4.json',
            'correct2.txt',
            id="flat_json_file"
        ),
        pytest.param(
            'file3.yaml',
            'file4.yaml',
            'correct2.txt',
            id="flat_yaml_file"
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
