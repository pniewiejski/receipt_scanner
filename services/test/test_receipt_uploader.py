import pytest

from receipt_reader import read_receipt

@pytest.mark.parametrize(("path", "expected_code", "expected_receit"), [
    ('notexistingfile.jpg', 500, "{}")
])
def test_receipt_uploader(path, expected_code, expected_receit):
    receipt, code = read_receipt(path)
    assert code == expected_code