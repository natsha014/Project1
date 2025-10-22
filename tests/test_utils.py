import json
from unittest.mock import patch

from src.utils import load_operations


def test_load_operations_with_tmp(tmp_path):
    test_file = tmp_path / "test_file_json"

    data = [{"key_1": "value_1", "number": 123}, {"key_2": "value_2", "number": 456}]
    with open(test_file, "w") as f:
        json.dump(data, f)

    result = load_operations(str(test_file))
    assert result == data
    # assert not isinstance(result, list) == []


@patch("os.path.exists")
def test_file_path_not_exists(mock_exists):
    mock_exists.return_value = False
    assert load_operations("non_exists_file_json") == []
    mock_exists.assert_called_with("non_exists_file_json")


@patch("os.path.exists")
@patch("os.path.getsize")
def test_file_not_empty(mock_exists, mock_getsize):
    mock_exists.return_value = True
    mock_getsize.return_value = 0
    assert load_operations("empty_file_json") == []
    mock_getsize.assert_called_with("empty_file_json")


def test_load_operations_not_list(tmp_path):
    test_file = tmp_path / "test_file_json"

    data = {"key_1": "value_1", "number": 123}
    with open(test_file, "w") as f:
        json.dump(data, f)

    result = load_operations(str(test_file))
    assert result == []
