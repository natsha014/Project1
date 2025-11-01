import json
import pandas as pd
from unittest.mock import patch

from src.read_data import read_csv, read_excel


@patch('pandas.read_csv')
def test_read_csv(mock_read_csv):
    mock_data = [{"id": 1, "state": "EXECUTED", "amount": 100}]
    mock_read_csv.return_value = pd.DataFrame(mock_data)
    result = read_csv('dummy_path')
    expected = json.dumps(mock_data, ensure_ascii=False, indent=4)
    assert result == expected


@patch('pandas.read_excel')
def test_read_excel(mock_read_excel):
    mock_data = [{"id": 1, "state": "EXECUTED", "amount": 100}]
    mock_read_excel.return_value = pd.DataFrame(mock_data)
    result = read_excel('dummy_path')
    expected = json.dumps(mock_data, ensure_ascii=False, indent=4)
    assert result == expected
