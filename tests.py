from NumeralsRoman import convert

def test_convert():
    assert convert(1) == "I"
    assert convert(2) == "II"
    assert convert(3) == "III"
    assert convert(4) == "IV"
 

