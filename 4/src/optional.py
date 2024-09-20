from typing import Optional

def get_user_name(id: int) -> Optional[str]:
    users = {
        1: "User1",
        2: "User2"
    }
    return users.get(id, None)

name = get_user_name(1)
print(f"lower name = {name.lower()}")
name = get_user_name(3)
print(f"lower name = {name.lower()}")