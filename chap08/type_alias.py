from typing import Literal
from datetime import datetime

type UserInfo = tuple[str, Literal['male', 'female'], datetime, bool]
p: UserInfo = ('YAMADA, Yoshihiro', 'male', datetime(2007, 6, 25), True)

# UserInfo = tuple[str, Literal['male', 'female'], datetime, bool]
