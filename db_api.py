import time
from cfg import cfg
from typing import Any, List, Optional

from models import db, MintTask


class DatabaseApi:
    max_timestamp: int
    host: str
    port: int
    user: str
    database: str
    url: str
    password: str
    _database: Any

    def __init__(self):
        self.start_time = None

    def set_start_time(self, start):
        self.start_time = start

    @staticmethod
    async def create_api():
        self = DatabaseApi()

        self.mode = None
        self.host = cfg.db.host
        self.port = cfg.db.port
        self.user = cfg.db.user
        self.password = cfg.db.password
        self.database = cfg.db.database

        self.url = f"postgresql://{self.user}:{self.password}@{self.host}:{self.port}/{self.database}"

        self.max_timestamp = 1893474000  # 01/01/2030 timestamp
        self._database = db

        await self._database.set_bind(self.url)

        await self._database.gino.create_all()
        return self

    async def get_mint_id(self):
        ordering = MintTask.mint_id.desc()
        posts: List[MintTask] = (
            await MintTask.query.order_by(ordering).offset(0).limit(1).gino.all()
        )
        try:
            mint_id = posts[0].mint_id
        except IndexError:
            mint_id = -1

        return mint_id + 1

    async def get_mint_task(self, parent_id) -> Optional[MintTask]:
        task = await MintTask.query.where(MintTask.parent_id == parent_id).gino.one_or_none()
        return task

    async def create_mint_task(self, parent_id: str, to_puzzle_hash: str):
        mint_id = await self.get_mint_id()
        mint = await MintTask.create(
            mint_id=mint_id,
            to_address=to_puzzle_hash,
            status=0,
            valid_from=int(time.time()),
            parent_id=parent_id,
            valid_to=self.max_timestamp
        )
        return mint

    async def get_pending_tasks(self) -> List[MintTask]:
        ordering = MintTask.mint_id.asc()
        tasks = await MintTask.query.order_by(ordering).where(MintTask.status == 0).gino.all()
        return tasks
