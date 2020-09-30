
from src.apis import dateutils


def test_ts_to_datetime():
    ts_str = 1601452767

    dt_obj = dateutils.ts_to_datetime(ts_str)

    assert dt_obj.strftime('%Y-%m-%d %H:%M:%S') == '2020-09-30 15:59:27'
