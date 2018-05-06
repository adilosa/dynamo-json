import json


def marshall(value):
    if isinstance(value, str):
        return {"S": value}
    elif isinstance(value, bool):
        return {"BOOL": value}
    elif isinstance(value, float) or isinstance(value, int):
        return {"N": str(value)}
    elif value is None:
        return {"NULL": True}
    elif isinstance(value, list):
        return {"L": [marshall(v) for v in value]}
    elif isinstance(value, dict):
        return {"M": {k1: marshall(v1) for k1, v1 in value.items()}}


def unmarshall(value):
    if "S" in value:
        return str(value["S"])
    elif "BOOL" in value:
        return value["BOOL"]
    elif "N" in value:
        return float(value["N"]) if "." in value["N"] else int(value["N"])
    elif "NULL" in value:
        return None
    elif "L" in value:
        return [unmarshall(v) for v in value["L"]]
    elif "M" in value:
        return {k: unmarshall(v) for k, v in value["M"].items()}

