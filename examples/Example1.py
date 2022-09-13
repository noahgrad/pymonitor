from PyMonitoring import PyMonitoring, monitor
import logging
from datetime import datetime, timedelta

logger = logging.getLogger()

def monitor(end_ts: int):
    table = "my_table"
    logger.info(f"Going to check if there is data in table {table} for the last 3 days")
    dt = datetime.fromtimestamp(end_ts)
    delta = timedelta(days=1)
    start_dt = dt - delta
    # Here you should create you snowflake client for example
    sf_client = None
    return PyMonitoring.check_table_in_sf(start_ts=start_dt.timestamp(), end_ts=end_ts,sf_client=sf_client,
                                          table=table, send_slack_if_no_data=True, time_field_name="updated_ts")
