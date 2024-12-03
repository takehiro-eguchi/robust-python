# MonkeyTypeのインストール

```ps1
pip install monkeytype
```

# MonkeyTypeの実行

```ps1
# 解析の実行
monkeytype run .\chapter7\src\main.py

# pasta_with_sausageのスタブ（修正案）の作成
monkeytype stub chapter7.src.pasta_with_sausage

# pasta_with_sausageのスタブ（修正案）の適用
monkeytype apply chapter7.src.pasta_with_sausage
```

# Pytypeのインストール

```ps1
pip install pytype
```

VC++ 14.0 以上が必要なため、
https://visualstudio.microsoft.com/visual-cpp-build-tools/
にてC++デスクトップ開発ツールをインストール

# Pytypeの実行

```ps1
pytype chapter7/src
```

以下のメッセージが出るときは python を Path に追加する
※ 私は `C:\Users\nss430011\AppData\Local\Microsoft\WindowsApps`
```ps1
CRITICAL Could not find a valid python3.12 interpreter in path (found )
```
