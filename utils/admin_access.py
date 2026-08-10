from __future__ import annotations

from config import ADMIN_IDS
from database import db


async def is_admin(user_id: int) -> bool:
    if user_id in ADMIN_IDS:
        return True
    return await db.is_admin(user_id)
