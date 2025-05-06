import extension

def notify(
        method: extension.NotificationMethod,
        notification: extension.NotificationType):
    # 通知種別によって切り替える
    if (isinstance(method, extension.Text)):
        __send_text(method, notification)
    elif (isinstance(method, extension.Email)):
        __send_email(method, notification)
    elif (isinstance(method, extension.SupplierAPI)):
        __send_to_suppier(method, notification)
    else:
        raise ValueError(f"サポートされていない通知手段です。{method}")

# ショートメッセージを送信する
def __send_text(
        text: extension.Text,
        notification: extension.NotificationType):
    pass

# Eメールを送信する
def __send_email(
        email: extension.Email,
        notification: extension.NotificationType):
    pass

# APIを呼び出す
def __send_to_suppier(
        api: extension.SupplierAPI,
        notification: extension.NotificationType):
    pass