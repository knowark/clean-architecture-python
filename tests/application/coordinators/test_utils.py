from pytest import raises
from datetime import datetime, date
from taskit.infrastructure.data.json import json_serialize


def test_json_serialize():
    sample_date = datetime.strptime('2018-02-15', '%Y-%m-%d')
    result = json_serialize(sample_date)
    assert result == '2018-02-15T00:00:00'


def test_json_serialize_unserializable():
    class SampleClass:
        pass
    with raises(TypeError):
        json_serialize(SampleClass)
