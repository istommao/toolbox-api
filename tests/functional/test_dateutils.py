import datetime

from src.toolbox import dateutils


def test_ts_to_datetime():
    ts_str = 1601452767

    dt_obj = dateutils.ts_to_datetime(ts_str)

    assert dt_obj.strftime('%Y-%m-%d %H:%M:%S') == '2020-09-30 15:59:27'


def test_datetime_to_ts():

    dt_obj = datetime.datetime(2020, 9, 30, 15, 59, 27)


    ts_str = dateutils.datetime_to_ts(dt_obj)

    assert ts_str == 1601452767
