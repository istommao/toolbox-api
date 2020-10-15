"""date utils."""
import datetime


DATE_FMT = '%Y-%m-%d'
DATE_FMT_SLASH = '%Y/%m/%d'

DATETIME_FMT = '%Y-%m-%d %H:%M:%S'


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


def get_day_range(days: int = 0, unbounded=False):
    """获取天的开始和结束时间.

    :param unbounded: 开区间
    """
    today = datetime.date.today()
    start_at = datetime.datetime.combine(today, datetime.time.min)

    if unbounded:
        end_at = datetime.datetime.combine(today + datetime.timedelta(days=1), datetime.time.min)
    else:
        end_at = datetime.datetime.combine(today, datetime.time.max)

    start_at = start_at + datetime.timedelta(days=days)
    end_at = end_at + datetime.timedelta(days=days)
    return start_at, end_at


def get_today_range(unbounded=False):
    """获取今天的开始和结束时间.

    :param unbounded: 开区间
    """
    return get_day_range(days=0, unbounded=unbounded)


def get_week_range(weeks=0, start='monday', unbounded=False):
    """获取周的开始和结束时间.

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

    start_at = start_at + datetime.timedelta(weeks=weeks)
    end_at = end_at + datetime.timedelta(weeks=weeks)

    return start_at, end_at


def get_this_week_range(start='monday', unbounded=False):
    """获取这周的开始和结束时间.

    :param start: monday or sunday
    :param unbounded: 开区间
    """
    return get_week_range(weeks=0, start=start, unbounded=unbounded)


def get_last_week_range(start='monday', unbounded=False):
    """获取上周的开始和结束时间.

    :param start: monday or sunday
    :param unbounded: 开区间
    """
    return get_week_range(weeks=-1, start=start, unbounded=unbounded)


def get_next_week_range(start='monday', unbounded=False):
    """获取下周的开始和结束时间.

    :param start: monday or sunday
    :param unbounded: 开区间
    """
    return get_week_range(weeks=1, start=start, unbounded=unbounded)


def get_month_range(months=0, unbounded=False):
    """获取月的开始和结束时间.

    :param unbounded: 开区间
    """

    today = datetime.date.today()
    year_diff = (today.month + months) // 12

    end = today.replace(
        month=(today.month + months) % 12 + 1,
        year=today.year + year_diff,
        day=1
    ) - datetime.timedelta(days=1)

    start_at = end.replace(day=1)
    start_at = datetime.datetime.combine(start_at, datetime.time.min)

    if unbounded:
        end_at = datetime.datetime.combine(end + datetime.timedelta(days=1), datetime.time.min)
    else:
        end_at = datetime.datetime.combine(end, datetime.time.max)

    return start_at, end_at


def get_this_month_range(unbounded=False):
    """获取 当前月的开始和结束时间.

    :param unbounded: 开区间
    """
    return get_month_range(months=0, unbounded=unbounded)


def get_last_month_range(unbounded=False):
    """获取 上个月的开始和结束时间.

    :param unbounded: 开区间
    """
    return get_month_range(months=-1, unbounded=unbounded)


def get_next_month_range(unbounded=False):
    """获取 下个月的开始和结束时间.

    :param unbounded: 开区间
    """
    return get_month_range(months=1, unbounded=unbounded)
