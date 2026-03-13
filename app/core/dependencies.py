from fastapi import Depends

from app.db.session import get_session

get_session_dep = Depends(get_session)
