from typing import NewType

TrimmedStr = NewType("TrimmedStr", str)

def get_word_count(text: TrimmedStr) -> int:
    return len(text)

text = "  aaaa  "
count = get_word_count(text)
print(count)

trimmed_str = TrimmedStr(text.strip())
count = get_word_count(trimmed_str)
print(count)