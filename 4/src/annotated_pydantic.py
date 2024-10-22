from typing import Annotated, Optional
from pydantic import BaseModel, Field

class Foo(BaseModel):
    positive: Annotated[int, Field(gt=0)]
    non_negative: Optional[int] = Field(ge=0)

foo = Foo(
    positive=0,
    non_negative=0
)
print(foo)