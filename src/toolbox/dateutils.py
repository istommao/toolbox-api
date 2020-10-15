"""date utils."""
import datetime


def ts_to_datetime(timestamp: int, raise_exception=False):
    """timestamp to datetime object

    :param timestamp: timestamp
    :param raise_exception: raise exception when timestamp args invalid

    :return datetime:
    """
    if timestamp == 0:
        return 0

    dobj = datetime.datetime.fromtimestamp(timestamp)
    return dobj


def datetime_to_ts(datetime_obj: object, ms=False):
    """datetime object to timestamp

    :param datetime_obj: datetime obj

    :return int/float timestamp:
    """
    timestamp = datetime_obj.timestamp()
    if not ms:
        timestamp = int(timestamp)

    return timestamp


def get_today_range(unbounded=False):
    """获取今天的开始和结束时间.

    :param unbounded: 开区间
    """
    today = datetime.date.today()
    start = datetime.datetime.combine(today, datetime.time.min)

    if unbounded:
        end = datetime.datetime.combine(today + datetime.timedelta(days=1), datetime.time.min)
    else:
        end = datetime.datetime.combine(today, datetime.time.max)

    return start, end


def get_this_week_range(start='monday', unbounded=False):
    """获取今天的开始和结束时间.

    :param start: monday or sunday
    :param unbounded: 开区间
    """
    today = datetime.date.today()
    weekday = today.isoweekday()

    if start.lower() == 'monday':
        start_diff_day = weekday - 1
    else:
        start_diff_day = weekday

    start_at = datetime.datetime.combine(
        today - datetime.timedelta(days=start_diff_day),
        datetime.time.min
    )

    if start.lower() == 'monday':
        if unbounded:
            end_diff_day = 7 - weekday + 1
        else:
            end_diff_day = 7 - weekday
    else:
        if unbounded:
            end_diff_day = 7 - weekday
        else:
            end_diff_day = 7 - weekday - 1

    end_time = datetime.time.min if unbounded else datetime.time.max

    end_at = datetime.datetime.combine(
        today + datetime.timedelta(days=end_diff_day), end_time
    )

    return start_at, end_at
