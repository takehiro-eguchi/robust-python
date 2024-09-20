from typing import Annotated, Optional
from pydantic import Field

def get_janken_name(id: Annotated[int, Field(ge=1, le=3)]) -> Optional[str]:
    jankens = {
        1:"グー", 2: "チョキ", 3:"パー"
    }
    return jankens.get(id)

name = get_janken_name(1)
print(name)
name = get_janken_name(5)
print(name)