from fandango_classroom_test import parse_fan_file


def test_can_parse_spec():
    fan = parse_fan_file("nested.fan")
    assert fan is not None


def test_can_parse_input():
    fan = parse_fan_file("nested.fan")
    assert list(fan.parse("123")) == ["123"]


def can_parse_subinput_1():
    fan = parse_fan_file("nested.fan", "<a>")
    assert list(fan.parse("23")) == ["23"]


def can_parse_subinput_2():
    fan = parse_fan_file("nested.fan", "<b>")
    assert list(fan.parse("3")) == ["3"]


def test_only_produces_123():
    fan = parse_fan_file("nested.fan")
    res = fan.generate_solutions(max_generations=20)
    assert list(res) == ["123"]
