from dataclasses import dataclass
import datetime
from typing import Union
import notifier

# 料理を表すクラス
class Dish:
    pass

# 材料クラス
class ingredient:
    pass

# 新しい特別料理
@dataclass
class NewSpecial:
    dish: Dish
    start_date: datetime.datetime
    end_data: datetime.datetime

# 在庫切れ情報
@dataclass
class IngredientsOutOfStock:
    ingredients: set[ingredient]

# 賞味期限切れ情報
@dataclass
class IngredientsExpired:
    ingredients: set[ingredient]

# 新メニュー
@dataclass
class NewMenuItem:
    dish: Dish

# 通知情報としてまとめる
NotificationType = Union[
    NewSpecial, IngredientsOutOfStock, IngredientsExpired, NewMenuItem
]

# テキストメッセージ
@dataclass
class Text:
    phone_number: str

# Eメール
@dataclass
class Email:
    email_address: str

# API
@dataclass
class SupplierAPI:
    pass

# 通知手段としてまとめる
NotificationMethod = Union[
    Text, Email, SupplierAPI
]

# 特別な処理
def declare_notification(
        dish: Dish, start_date: datetime.datetime, end_date: datetime.datetime):
    # 何らかの処理

    # 通知する
    notifier.notify(
        Email("料理が作成されました"),
        NewSpecial(dish, start_date, end_date))

# 通知を送信する処理
def send_notification(notification: NotificationType):
    pass
