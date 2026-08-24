# pyright: strict

from lab01a import convert

def test_convert():
    assert convert("1,024,123.45") == "one million twenty-four thousand one hundred twenty-three pesos and forty-five centavos"
    assert convert("1.0") == "one peso"
    assert convert("10.0") == "ten pesos"
    assert convert("11.0") == "eleven pesos"
    assert convert("012.0") == "twelve pesos"
    assert convert("700.0") == "seven hundred pesos"
    assert convert("123.0") == "one hundred twenty-three pesos"
    assert convert("000,000,003.0") == "three pesos"
    assert convert("0.0") == "zero pesos"
    assert convert("1.1") == "one peso and ten centavos"
    assert convert("1,001,000.0") == "one million one thousand pesos"