from datetime import datetime
from optparse import OptionParser
import importlib.util
import pathlib
import logging 

logging.basicConfig(level = logging.INFO)

def parse_options():
    parser = OptionParser()
    parser.add_option('--end_ts', type=int)
    parser.add_option('--dir', type=str)
    parser.add_option('--filename', type=str, default='monitor.py')
    parser.add_option('--methodname', type=str, default='monitor')

    options, _ = parser.parse_args()
    return options


def main(options):
    """
    Get all files name options.filename in options.dir
    for each file:
        execute the method options.methodname with the end_ts
    :param options:
    :return:
    """
    logging.info(f"Going to monitor all {options.filename} files in dir {options.dir} end ts is {datetime.fromtimestamp(options.end_ts)}")
    for pyfile in pathlib.Path(options.dir).glob(f'**/{options.filename}'):
        try:
            logging.info(f"Going to monitor {pyfile}")
            spec = importlib.util.spec_from_file_location(f"{__name__}.imported_{pyfile.stem}" , pyfile)
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)
            monitor_method = getattr(module, options.methodname)
            res = monitor_method(options.end_ts)
            logging.info(f"monitor ends with status {res}")
        except Exception as e:
            message = f"Couldn't monitor {pyfile} exception is {e}"
            logging.error(message)
            # you can add slack or email notification


if __name__ == '__main__':
    options = parse_options()
    main(options)
