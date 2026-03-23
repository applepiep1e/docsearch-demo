from __future__ import annotations

from pathlib import Path
from docx import Document

class docFile:
	def __init__(self, path=None, keyword=None):
		"""
		初始化
		:param path: 默认搜索路径
		:param keyword: 默认搜索关键字
		"""
		self.path = Path(path) if path else None
		self.keyword = keyword

	def search_for_docfiles(self, docfiles_path=None):
		"""
		列出目录下所有 .docx 文件
		:param docfiles_path: 可选覆盖路径
		:return: 文件路径列表
		"""
		path = Path(docfiles_path) if docfiles_path else self.path
		if not path:
			raise ValueError("Path for search must be provided")
		if not path.exists():
			raise FileNotFoundError(f"The provided path does not exsit: {path}")
		return [str(file) for file in path.rglob("*.docx")]

	def search_keyword(self, filepath, keyword=None, window=50):
		"""
		在单个文件中搜索关键字，并截取前后 window 个字符
		:param filepath: docx 文件路径
		:param keyword: 可选覆盖关键字
		:param window: 截取关键字前后字符数
		:return: 匹配片段列表
		"""
		keyword = keyword or self.keyword
		if not keyword:
			raise ValueError("keyword must be provided")

		doc = Document(filepath)
		results = []

		for para in doc.paragraphs:
			text = para.text
			idx = text.find(keyword)
			while idx != -1:
				start = max(0, idx - window)
				end = min(len(text), idx + len(keyword) + window)
				results.append(text[start:end])
				idx = text.find(keyword, idx + len(keyword))
		return results


	def search_keyword_in_path(self, docfiles_path=None, keyword=None, window=50):
		"""
		在目录下所有 docx 文件里搜索关键字
		:param docfiles_path: 可选覆盖路径
		:param keyword: 可选覆盖关键字
		:param window: 截取关键字前后字符数
		:return: {filepath: [匹配片段]}
		"""

		files = self.search_for_docfiles(docfiles_path)
		keyword = keyword or self.keyword

		results = {}
		for f in files:
			matches = self.search_keyword(f, keyword, window)
			if matches:
				results[f] = matches
		return results

	def display_results(self, results):
		"""
		在命令行中展示搜索结果
		:param results: {filepath: [匹配片段]}，由 search_keyword_in_path 返回
		"""
		if not results:
			print("No matching keywords were found.")
			return

		for filepath, snippets in results.items():
			print(f"\nfile: {filepath}")
			for i, snippets in enumerate(snippets, 1):
				print(f"    {i}. ...{snippets}...")


if __name__ == '__main__':
	df = docFile("test", keyword="Alice")
	all_files = df.search_for_docfiles()
	matches = df.search_keyword_in_path()
	df.display_results(matches)
	