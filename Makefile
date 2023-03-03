# Makefile

# Define source and test directories
SRC_DIR := src
TEST_DIR := tests

# Define the files to check with vulture
VULTURE_FILES := $(shell find $(SRC_DIR) $(TEST_DIR) -name '*.py' -not -path '*/__init__.py')

# Define the path to the vulture whitelist file
VULTURE_WHITELIST_FILE := vulture_whitelist.txt

.PHONY: all
all: black ruff mypy vulture tests

.PHONY: nice
nice: black ruff mypy vulture

.PHONY: format
format: black ruff

.PHONY: black
black:
	black $(SRC_DIR) $(TEST_DIR)

.PHONY: ruff
ruff:
	ruff $(SRC_DIR) $(TEST_DIR)

.PHONY: mypy
mypy:
	mypy $(SRC_DIR) $(TEST_DIR) --strict

.PHONY: vulture
vulture:
	vulture $(VULTURE_FILES) $(VULTURE_WHITELIST_FILE)

.PHONY: vulture_whitelist
vulture_whitelist:
	vulture $(VULTURE_FILES) --make-whitelist > $(VULTURE_WHITELIST_FILE)

.PHONY: tests
tests:
	pytest $(TEST_DIR)
