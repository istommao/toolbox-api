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


def datetime_to_ts(datetime_obj: object, keep_millisecond=False):
    """datetime object to timestamp

    :param datetime_obj: datetime obj

    :return int/float timestamp:
    """
    timestamp = datetime_obj.timestamp()
    if not keep_millisecond:
        timestamp = int(timestamp)

    return timestamp
