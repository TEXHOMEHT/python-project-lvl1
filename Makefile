install:
	poetry install

barin-games:
	poetry run barin-games

build:
	poetry build

publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install --user dist/*.whl