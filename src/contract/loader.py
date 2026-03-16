from pathlib import Path
from .parser import parse_contract


def load_contract(path: str):

    text = Path(path).read_text()

    contract = parse_contract(text)

    return contract
