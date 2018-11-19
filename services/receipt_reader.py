# This is cheating
import sys, os
sys.path.insert(0, os.path.abspath('./reader'))

import reader.read as reader
import reader.parsing.receipt as r

def read_receipt(path: str):
    """
    Returns a tuple: `receipt_json, http_status_code`
    """
    try:
        receipt = reader.read(path)
    except: 
        return r.Receipt("", 0, []).to_json(), 418
    else:
        return receipt, 200
