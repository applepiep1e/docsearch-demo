from docsearchdemo.main import execute
import sys

# 覆盖率测试
def test_execute(monkeypatch):
    monkeypatch.setattr(
        sys,
        "argv",
        ["docsearch", "tests/test_data", "Alice"]
    )
    execute()