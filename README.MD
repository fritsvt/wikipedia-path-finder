# WikiRacer

WikiRacer inspired by the [wikiracer.io](https://wikiracer.io/) game.

**Please note:** this project was quickly written and uses web crawling to find a link 
between pages. **DO NOT** use extensively or try to find deep links as heavy scraping
is against Wikipedia's policy.

A more efficient implementation could use the [pagelinks](https://dumps.wikimedia.org/enwiki/latest/enwiki-latest-pagelinks.sql.gz) dump provided by Wikipedia.

## Requirements

- Python 3.11

## Installation

To install the project use the following steps.

1. Clone the repo
```
git clone https://github.com/fritsvt/wikiracer.git
```
2. Navigate in the project directory
```
cd wikiracer
```
3. Create a virtual environment
```
pyenv virtualenv 3.11.2 wikiracer
```
4. Install poetry dependencies
```
poetry install
```
5. Load `.envrc` file
```
source .envrc
```
6. Run the app
```
python src/wikiracer.py
```

## Running tests
Make sure you've loaded the `.envrc` file to configure PYTHON_PATH and then run:
```
make tests
```

## Code quality
To ensure code quality type checking and linting tools are used linters and type checking
has been setup.

Although before every commit `make` should be run to ensure the tests are green and
the linters are happy to only run type checking and formatting you can run:
```
make nice
```
This will run: `black`, `mypy`, `ruff` and `vulture`

Additionally tooling like `mypy`, `black` can also be run individually using `make toolname` 
or `make format` to run all formatting except mypy

## Technologies
[Poetry](https://www.poetryfoundation.org/)

[Pytest](https://docs.pytest.org/en/7.2.x/)

[Beautiful Soup](https://beautiful-soup-4.readthedocs.io/en/latest/)

[Mypy](https://mypy-lang.org/)

[Black](https://github.com/psf/black)

[Ruff](https://github.com/charliermarsh/ruff)

[Vulture](https://github.com/jendrikseipp/vulture)

## License
[MIT](LICENSE)