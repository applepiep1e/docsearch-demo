from argparse import ArgumentParser
from .docfile_processor import docFile

def execute():
	parser = ArgumentParser(description='Search keyword in the doc files \
		in the given path.')
	parser.add_argument('path', metavar='PATH',
						help='the directory to be searched')
	parser.add_argument('keyword', metavar='KEYWORD')
	parser.add_argument('-w', '--window', default=100, 
		                help='length of each search result summary')

	args = parser.parse_args()

	df = docFile(args.path, args.keyword)
	all_files = df.search_for_docfiles()
	matches = df.search_keyword_in_path(window=args.window)
	df.display_results(matches)





if __name__ == '__main__':
	execute()