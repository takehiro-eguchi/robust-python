from dataclasses import dataclass
from datetime import datetime
from enum import Enum, auto
from typing import Protocol, Union

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
    start_date: datetime
    end_data: datetime

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

# 通知内容
TopicContent = Union[
    NewSpecial, IngredientsOutOfStock, IngredientsExpired, NewMenuItem
]

# 通知のプロトタイプ
class Notification(Protocol):
    def notify(self, topic: TopicContent):
        '''実装不要'''

# テキストメッセージ
class TextNotification:
    phone_number: str
    def notify(self, topic: TopicContent):
        pass
# Eメール
class EmailNotification:
    email_address: str
    def notify(self, topic: TopicContent):
        pass
# API
class SupplierAPINotification:
    def notify(self, topic: TopicContent):
        pass

# 特別な処理
def declare_notification(
        dish: Dish, start_date: datetime, end_date: datetime):
    # 何らかの処理

    # 通知する
    notify(
        NewSpecial(dish, start_date, end_date))

def notify(topic: TopicContent):
    # 通知先を取得
    subscriptions: list[Notification] = provide(topic)

    # 通知を実行
    for subscription in subscriptions:
        subscription.notify(topic)

def provide(topic: TopicContent) -> list[Notification]:
    if (isinstance(topic, NewSpecial)):
        return __get_NewSpecial(topic)
    elif (isinstance(topic, IngredientsOutOfStock)):
        return __get_IngredientsOutOfStock(topic)
    elif (isinstance(topic, IngredientsExpired)):
        return __get_IngredientsExpired(topic)
    elif (isinstance(topic, NewMenuItem)):
        return __get_NewMenuItem(topic)
    else:
        raise ValueError(f"サポートされていない通知手段です。{topic}")

def __get_NewSpecial(topic: NewSpecial):
    return []
def __get_IngredientsOutOfStock(topic: IngredientsOutOfStock):
    return []
def __get_IngredientsExpired(topic: IngredientsExpired):
    return []
def __get_NewMenuItem(topic: NewMenuItem):
    return []