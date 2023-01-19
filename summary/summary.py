from __future__ import annotations
from dataclasses import dataclass

from os import PathLike
from typing import Protocol, Union

AnyPath = Union[str, bytes, PathLike]


class TFRecord(Protocol):
    def __init__(self, path: AnyPath) -> None:
        self.path = path
        ...

    def __iter__(self) -> TFRecord: ...

    def __next__(self) -> bytes: ...

    def numpy(self) -> bytes: ...


class TFRecordDataset(Protocol):
    def __init__(self, paths: list[AnyPath]) -> None:
        self.paths = paths
        ...

    def __iter__(self) -> TFRecordDataset: ...

    def __next__(self) -> TFRecord: ...


@dataclass
class ProtoSummaryValue(Protocol):
    tag: str
    simple_value: float


@dataclass
class ProtoSummary(Protocol):
    value: list[ProtoSummaryValue]


# noinspection PyPep8Naming
@dataclass
class ProtoEvent(Protocol):
    summary: ProtoSummary | None

    def MergeFromString(self, s: bytes) -> None: ...

    def SerializeToString(self) -> bytes: ...
