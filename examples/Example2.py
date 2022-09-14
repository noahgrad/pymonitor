from pymonitoring.PyMonitoring import PyMonitoring, monitor
import logging
from datetime import datetime, timedelta

logger = logging.getLogger()

def monitor(end_ts: int):
    table = "my_table"
    dt = datetime.fromtimestamp(end_ts)
    delta = timedelta(days=3)
    start_dt = dt - delta
    sf_client = None
    logger.info(f"Going to check if there is data in table {table} for the last 3 days")
    res = PyMonitoring.check_query_in_sf(query = f"select * from {table} where start_ts between {start_dt.timestamp()}"
                                                 f" and {end_ts}", sf_client=sf_client)
    if res and len(res)> 1000:
        return True

    logger.error(f"Table: {table} contains less data then expected. count is {len(res)}")
    return False