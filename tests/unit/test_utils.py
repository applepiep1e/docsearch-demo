# test/test_docfile.py
import pytest
from pathlib import Path 
from docsearchdemo.docfile_processor import docFile

TEST_DIE = Path("tests/test_data")

# ---------------1. 测试文件搜索 ---------------
def test_search_for_docfiles():
	df = docFile(path=TEST_DIE)
	files = df.search_for_docfiles()

	assert len(files) >= 2
	assert any("test1.docx" in f for f in files)

# --------------2. 测试关键词搜索 --------------
def test_search_keyword_found():
	df = docFile(keyword="Alice")
	file = TEST_DIE / "test1.docx"

	results = df.search_keyword(file)

	assert len(results) > 0
	assert any("Alice" in r for r in results)

def test_search_keyword_not_found():
	df = docFile(keyword="Alice")
	file = TEST_DIE / "test2.docx"

	results = df.search_keyword(file)

	assert results == []

# ------------ 3. 测试上下文截取 --------------
def test_extract_context():
	df = docFile(keyword="Alice")
	file = TEST_DIE / "test3.docx"

	snippet = df.search_keyword(file, window=0)

	assert "Alice" in snippet


	