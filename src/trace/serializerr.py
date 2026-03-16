from dataclasses import asdict
import json


def trace_to_dict(trace) -> dict:
    return asdict(trace)


def trace_to_json(trace, *, indent: int = 2) -> str:
    return json.dumps(asdict(trace), indent=indent, ensure_ascii=False)
