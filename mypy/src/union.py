from typing import Union
from datetime import date

# 株式
class Stock:
    def __init__(self):
        self.issueCd = "1301"
        self.name = "極洋"
        self.price = 4510

# 債券
class Bond:
    def __init__(self):
        self.issueCd = "JGB0172"
        self.name = "利付国庫債券（5年）（第172回）"
        self.price = 100.19
        self.expire_date = date(2029, 6, 20)

# 先物
class Future:
    def __init__(self):
        self.issueCd = "NK2252412"
        self.name = "日経225先物24年12月"
        self.price = 37723.91
        self.expire_date = date(2024, 12, 13)

# 終了日を取得します
def get_end_date(issue: Union[Bond, Future]) -> date:
    return issue.expire_date

# 銘柄ごとの終了日を取得し、表示します
bond = Bond()
end_date = get_end_date(bond)
print(f"end_date = {end_date}")
future = Future()
end_date = get_end_date(future)
print(f"end_date = {end_date}")
# stock = Stock()
# end_date = get_end_date(stock)
# print(f"end_date = {end_date}")
