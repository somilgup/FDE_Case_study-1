from src.utils import clean_text


def test_clean_text():

    text = "Login Error!!!"

    result = clean_text(text)

    assert result == "login error"


def test_clean_text_keeps_numbers():

    text = "Error Code 500"

    result = clean_text(text)

    assert result == "error code 500"