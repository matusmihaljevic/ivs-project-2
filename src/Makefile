# Default target
.DEFAULT_GOAL := all

# Variables
PYTHON := python3
PYTEST := pytest

# Targets
all: run

pack:
	@echo "TO DO!"

clean:
	@rm -rf __pycache__
	@rm -rf .pytest_cache
	@echo "Cleaning done."

run: gui.py
	@$(PYTHON) gui.py

test: math_tests.py parse_tests.py
	@$(PYTEST) math_tests.py || true
	@$(PYTEST) parse_tests.py || true
	@echo "Testing done."
	@$(MAKE) clean
	
profile:
	@echo "TO DO!"

help:
	@echo "Available targets:"
	@echo "  all      - Run the program (default)"
	@echo "  pack     - Pack the project for submission"
	@echo "  clean    - Clean up unnecessary files"
	@echo "  run      - Run the program"
	@echo "  profile  - Profile the program"
	@echo "  help     - Display this help message"

# Phony
.PHONY: all
