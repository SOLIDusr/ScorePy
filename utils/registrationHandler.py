import re

import utils.logs as logger
from requesto import Requesto


def registration(providedLogin: str, providedEmail: str, providedPassword: str) -> int | None:
    db = Requesto.db
    userdata = db.newTable("userdata", db.cursor)
    data = userdata.returnAll(prop='email')
    for account in data:
        if providedEmail in account:
            return -1
    data = userdata.returnAll(prop='login')
    for account in data:
        if providedLogin in account:
            return -2

    if not re.match(r"^[A-Za-z0-9\.\+_-]+@[A-Za-z0-9\._-]+\.[a-zA-Z]*$", providedEmail):
        if 5 > len(list(providedEmail)) > 32:
            return -3

    if 5 > len(list(providedLogin)) > 16 or providedLogin.lower() == "admin":
        return -4

    if len(providedPassword) < 8:
        return -51
    elif re.search('[0-9]', providedPassword) is None:
        return -52
    elif re.search('[A-Z]', providedPassword) is None:
        return -53

    if not(userdata.insert(rows="login, password, email", args=f"{providedLogin}, {providedPassword}, {providedEmail}")):
        return -6
    return 0