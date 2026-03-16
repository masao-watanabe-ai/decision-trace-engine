import json
from pathlib import Path
from typing import List, Optional

from .models import DecisionLedgerEntry


class DecisionLedger:
    """
    Very small append-only ledger implementation.

    Purpose:
    - preserve decision history
    - keep records explicit and inspectable
    - provide a minimal reference implementation
    """

    def __init__(self, path: Optional[str] = None):
        self.entries: List[DecisionLedgerEntry] = []
        self.path = Path(path) if path else None

        if self.path and self.path.exists():
            self._load()

    def record(self, entry: DecisionLedgerEntry) -> DecisionLedgerEntry:
        self.entries.append(entry)
        if self.path:
            self._save()
        return entry

    def all(self) -> List[DecisionLedgerEntry]:
        return list(self.entries)

    def find_by_event(self, event_id: str) -> List[DecisionLedgerEntry]:
        return [e for e in self.entries if e.event_id == event_id]

    def find_by_signal(self, signal_id: str) -> List[DecisionLedgerEntry]:
        return [e for e in self.entries if e.signal_id == signal_id]

    def to_dict(self) -> List[dict]:
        return [entry.to_dict() for entry in self.entries]

    def _save(self) -> None:
        if not self.path:
            return
        self.path.parent.mkdir(parents=True, exist_ok=True)
        with self.path.open("w", encoding="utf-8") as f:
            json.dump(self.to_dict(), f, indent=2, ensure_ascii=False)

    def _load(self) -> None:
        if not self.path or not self.path.exists():
            return
        with self.path.open("r", encoding="utf-8") as f:
            raw = json.load(f)
        self.entries = [DecisionLedgerEntry(**item) for item in raw]
