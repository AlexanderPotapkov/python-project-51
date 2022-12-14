

install:
	poetry install

page-loader:
	poetry run page-loader -h

build:
	poetry build

package-install:
	python3 -m pip install --user dist/*.whl --force-reinstall

lint:
	poetry run flake8 page_loader

test:
	poetry run pytest

test-coverage:
	poetry run coverage run -m pytest
	poetry run coverage xml

publish:
	poetry publish --dry-run