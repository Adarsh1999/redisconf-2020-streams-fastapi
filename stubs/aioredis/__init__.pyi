from typing import Any, Optional, List, Tuple, Dict, Union

ReadMessageType = Tuple[bytes, bytes, Dict[bytes, bytes]]
RangeMessageType = Tuple[bytes, Dict[bytes, bytes]]

class CommandsMixin:
    async def xread(
        self, streams: List[str], timeout: int = 0, count: Optional[int] = None, latest_ids: Optional[List[str]] = None
    ) -> List[ReadMessageType]: ...
    async def xrange(
        self, stream: str, start: str = "-", stop: str = "+", count: Optional[int] = None
    ) -> List[RangeMessageType]: ...
    async def xrevrange(
        self, stream: str, start: str = "+", stop: str = "-", count: Optional[int] = None
    ) -> List[RangeMessageType]: ...
    async def xadd(self, stream: str, fields: Dict[str, Union[bytes, float, int, str]]) -> bytes: ...
    async def time(self) -> float: ...

class Redis(CommandsMixin):
    def __init__(self, pool_or_conn: Any) -> None: ...
    def close(self) -> None: ...
    async def wait_closed(self) -> None: ...

async def create_redis(address: str) -> Redis: ...
