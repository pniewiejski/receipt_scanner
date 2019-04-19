# This is cheating
# TODO: refactor module imports
import sys, os
sys.path.insert(0, os.path.abspath('./reader'))

import reader.read as reader
import reader.parsing.receipt as r
from reader.parsing.parsing_error import ParsingException

def read_receipt(path: str):
    """
    Returns a tuple: `receipt_json, http_status_code`
    """
    try:
        receipt = reader.read(path)
    except ParsingException as e:
        print("DEBUG: Parsing exception")
        return r.Receipt("", 0, []).to_json(), 418
    except IOError as e: 
        print("DEBUG: Exception occured")
        print("DEBUG: IOError - most likely could not open a file")
        print(e)
        return r.Receipt("", 0, []).to_json(), 500
    except Exception as e:
        print("DEBUG: Exception occured")
        print(e)
        return r.Receipt("", 0, []).to_json(), 500
    else:
        return receipt, 200
