# test/test_docfile.py
import pytest
from pathlib import Path 
from docsearchdemo.docfile_processor import docFile

TEST_DIE = Path("tests/test_data")

# ------------ 4. 集成测试 -------------------
def test_search_keyword_in_path():
	df = docFile(path=TEST_DIE, keyword="Alice")

	results = df.search_keyword_in_path()

	assert isinstance(results, dict)
	assert any(len(v) > 0 for v in results.values())

# ------------ 5. 异常测试 -------------------
def test_invalid_path():
	df = docFile(path="non_existing_path")

	with pytest.raises(FileNotFoundError):
		df.search_for_docfiles()
	