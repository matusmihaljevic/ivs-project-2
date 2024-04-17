# Default target
.DEFAULT_GOAL := all

# Variables
GUI=gui.py
MATH_LIB=calc.py
MATH_TESTS=math_tests.py
PARSE_TESTS=parse_tests.py
PROFILE=profiling.py
PROFILE_INPUT=data.txt
ZIP_FILE=xbojnaa00_xmihalm00_xpodmaj00_xpribik00

# Targets
all: run

pack: clean
	@rm -rf ../../$(ZIP_FILE)
	@rm -rf ../../$(ZIP_FILE).zip
	@mkdir -p ../../$(ZIP_FILE)/repo

	@cp -r ../ ../../$(ZIP_FILE)/repo
	@cp -r ../install ../../$(ZIP_FILE)
	@cp -r ../doc ../../$(ZIP_FILE)

	@rm -rf ../../$(ZIP_FILE)/repo/install
	@rm -rf ../../$(ZIP_FILE)/repo/doc

	@cd ../../ && zip -r $(ZIP_FILE).zip $(ZIP_FILE)/

clean:
	@echo "Cleaning..."
	@rm -rf __pycache__
	@rm -rf .pytest_cache

run: $(GUI)
	@python3 $(GUI)

test: $(MATH_TESTS) $(PARSE_TESTS) clean
	@pytest $(MATH_TESTS) || true
	@pytest $(PARSE_TESTS) || true
	@echo "Testing done."
	@$(MAKE) clean
	
profile: $(PROFILE) $(PROFILE_INPUT)
	@python3 $(PROFILE) < $(PROFILE_INPUT)

help:
	@echo "Available targets:"
	@echo "  all      - Run the program (default)"
	@echo "  pack     - Pack the project for submission"
	@echo "  clean    - Clean up unnecessary files"
	@echo "  run      - Run the program"
	@echo "  test     - Run tests"
	@echo "  profile  - Profile the program"
	@echo "  help     - Display this help message"

# Phony
.PHONY: 
	all
	pack
	clean
	run
	test
	profile
	help
