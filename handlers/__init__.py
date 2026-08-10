from aiogram import Router

from handlers.admin import router as admin_router
from handlers.deals import router as deals_router
from handlers.emoji_tools import router as emoji_router
from handlers.requisites import router as requisites_router
from handlers.start import router as start_router


def setup_routers() -> Router:
    root = Router()
    root.include_router(admin_router)
    root.include_router(deals_router)
    root.include_router(requisites_router)
    root.include_router(start_router)
    root.include_router(emoji_router)
    return root
