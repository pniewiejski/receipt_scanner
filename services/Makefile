install:
	pip3 install -r requirements.txt 
cleanup:
	find . | grep -E "(__pycache__$$|.pytest_cache$$)" | xargs rm -r
.PHONY: all test clean
test:
	python3 -m pytest -v
run:
	python3 -m uploader.py