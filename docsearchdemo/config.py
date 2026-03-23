import json
from pathlib import Path 

DEFAULT_CONFIG = {
	"window": 0,
}

def load_config(config_path=None):
	if not config_path:
		return DEFAULT_CONFIG

	path = Path(config_path)
	if not path.exists():
		raise FileNotFoundError(f"Config file not found: {config_path}")

	with open(path, 'r', encoding='utf-8') as f:
		user_config = json.load(f)

	# merge config (用户配置覆盖默认)
	config = DEFAULT_CONFIG.copy()
	config.update(user_config)
	return config
