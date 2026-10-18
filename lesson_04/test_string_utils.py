import pytest
from string_utils import StringUtils
string_utils=StringUtils()
@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    ("skypro", "Skypro"), ("москва", "Москва"), ("hello world", "Hello world"),
    ("ашик-Кериб", "Ашик-Кериб")])
def test_capitalize_positive(input_str, expected):
    assert string_utils.capitalize(input_str)==expected
@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [
    ("5425", "5425"), ("$&*%_@!", "$&*%_@!"), ("", ""),
    ("HELLO", "HELLO"), ("   ", "   ")])
def test_capitalize_negative(input_str, expected):
    assert string_utils.capitalize(input_str)==expected
@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    (" hello", "hello"), ("   world", "world"),
    (" Hello world", "Hello world"), (" ", "")])
def test_trim_positive(input_str, expected):
    assert string_utils.trim(input_str)==expected
@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [
    ("", ""), ("hello", "hello")])
def test_trim_negative(input_str, expected):
    assert string_utils.trim(input_str)==expected
@pytest.mark.positive
@pytest.mark.parametrize("input_str, symbol", [
    ("Sky", "k"), ("Привет","в"), ("12тый", "2"), ("SkyPro", "yP")])
def test_contains_positive(input_str, symbol):
    assert string_utils.contains(input_str, symbol)==True
@pytest.mark.negative
@pytest.mark.parametrize("input_str, symbol", [
    ("SkyPro", ""), ("SkyPro", "Py"), ("SkyPro", "Р"),
    ("", " "), ("SkyPro", "sK")])
def test_contains_negative(input_str, symbol):
    assert string_utils.contains(input_str, symbol)==False
@pytest.mark.positive
@pytest.mark.parametrize("input_str, symbol, expected", [
    ("SkyPro", "S", "kyPro"), ("SkyPro", "V", "SkyPro"), ("SkyPro", "", "SkyPro"),
    ("Палата", "а", "Плт"), ("SkyPro", "Pro", "Sky"),
    ("SkyPro", "pRO", "SkyPro"), ("SkyPro", "569", "SkyPro"),
    ("SkyPro", "Руо", "SkyPro")])
def test_delete_symbol_positive(input_str, symbol, expected):
    assert string_utils.delete_symbol(input_str, symbol)==expected
