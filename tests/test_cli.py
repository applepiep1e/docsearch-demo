import subprocess

def test_cli():
	result = subprocess.run(
		["docsearch", "tests/test_data", "Alice", "-w", "10"],
		capture_output=True,
		text=True
	)

	assert result.returncode == 0
	assert "Alice" in result.stdout