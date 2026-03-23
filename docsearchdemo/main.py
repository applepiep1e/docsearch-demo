from argparse import ArgumentParser
from .docfile_processor import docFile
from .config import load_config
from .logger import setup_logger



def execute():
	parser = ArgumentParser(description='Search keyword in the doc files \
		in the given path.')
	parser.add_argument('path', metavar='PATH',
						help='the directory to be searched')
	parser.add_argument('keyword', metavar='KEYWORD')
	parser.add_argument('-w', '--window', default=100, 
		                help='length of each search result summary')
	parser.add_argument("-c", "--config", help="path to config file")
	parser.add_argument("--log-level", default="INFO", 
		                choices=["DEBUG", "INFO", "WARNING", "ERROR"]
	)


	args = parser.parse_args()

	config = load_config(args.config)

	logger = setup_logger(args.log_level)

	# CLI 优先
	window = args.window if args.window else config["window"]

	df = docFile(args.path, args.keyword)
	all_files = df.search_for_docfiles()
	matches = df.search_keyword_in_path(window=window)
	df.display_results(matches)





if __name__ == '__main__':
	execute()