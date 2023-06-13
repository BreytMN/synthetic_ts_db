import argparse
from datetime import datetime, timedelta


def get_start_time():
    parser = argparse.ArgumentParser()
    parser.add_argument('--start-time', type=str, default=None,
                        help='Start time in format "YYYY-MM-DD HH:MM:SS"')
    args = parser.parse_args()

    default_start_time = datetime.now() - timedelta(days=7)
    start_time_str = args.start_time or str(default_start_time)
    return datetime.strptime(start_time_str, '%Y-%m-%d %H:%M:%S')
