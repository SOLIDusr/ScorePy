import utils.logs as logger
from requesto import Requesto


def registration(login: str, email: str, password: str) -> bool | None:
    db = Requesto.db
    userdata = db.newTable("userdata", db.cursor)
    data = userdata.returnAll(prop='email, login')
    for account in data:
        logger.data(account)
        for data in account:
            logger.info(email)
            logger.info(password)
    return False