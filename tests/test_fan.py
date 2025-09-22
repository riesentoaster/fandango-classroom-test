from fandango_classroom_test import parse_fan_file


def test_can_parse_spec():
    fan = parse_fan_file("dummy.fan")
    assert fan is not None


def test_can_parse_input():
    fan = parse_fan_file("dummy.fan")
    assert list(fan.parse("123")) == ["123"]


def can_parse_subinput_1():
    fan = parse_fan_file("dummy.fan", "<a>")
    assert list(fan.parse("23")) == ["23"]


def can_parse_subinput_2():
    fan = parse_fan_file("dummy.fan", "<b>")
    assert list(fan.parse("3")) == ["3"]
