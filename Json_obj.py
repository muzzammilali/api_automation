from dataclasses import dataclass, field
from dataclasses_json import dataclass_json
from faker import Faker
from typing import Optional



@dataclass
class Python_Obj:
    position: int
    description: str
    creator: str
    user: str
    user_info: UserValue
    version: Optional[str] = field(compare=False, default=None)



class Json_obj:
    def create_generic_Python_Reqbody(self):
        faker = Faker()
        user = UserValue(
            uservalue=faker.random_int(min=1, max=100)
        )
        Json_body = BookmarkRequest(
            time=faker.date_time().isoformat(),
            position=faker.random_int(min=1, max=100),
            user=user,
            user_info=user,
            description=faker.sentence(),
            creator=faker.name()
        )

        return Json_body
