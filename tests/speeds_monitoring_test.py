from src.pymonitoring.PyMonitoring import PyMonitoring
from datetime import datetime, timedelta
from unittest.mock import MagicMock

def test_check_table_in_sf_true():

    tod = datetime.now()
    delta = timedelta(days=3)
    date_3_days_ago = tod - delta
    sf_client = None
    PyMonitoring.check_table_in_sf = MagicMock(return_value=True)
    res = PyMonitoring.check_table_in_sf(start_ts=date_3_days_ago.timestamp(), end_ts=tod.timestamp(),
                                       table="MY_TABLE",sf_client=sf_client,
                                       time_field_name="insertion_ts")

    assert res

def test_check_table_in_sf_false():
    tod = datetime.now()
    date_1_day_ahead = tod + timedelta(days=1)
    date_3_days_ahead = tod + timedelta(days=3)
    sf_client = None
    PyMonitoring.check_table_in_sf = MagicMock(return_value=[])
    res = PyMonitoring.check_table_in_sf(start_ts=date_1_day_ahead.timestamp(), end_ts=date_3_days_ahead.timestamp(),
                                       table="MY_TABLE",sf_client=sf_client,
                                       time_field_name="insertion_ts")

    assert not res
