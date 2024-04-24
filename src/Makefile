# Default target
.DEFAULT_GOAL := all

# Variables
ZIP_FILE=xbojnaa00_xmihalm00_xpodmaj00_xpribik00

# Targets
all: run

pack: doc clean
	@rm -rf ../../$(ZIP_FILE)
	@rm -rf ../../$(ZIP_FILE).zip
	@mkdir -p ../../$(ZIP_FILE)/repo

	@cp -rf ../ ../../$(ZIP_FILE)/repo
	@cp -rf ../install ../../$(ZIP_FILE)
	@cp -rf ../doc ../../$(ZIP_FILE)
	@rm -rf ../../$(ZIP_FILE)/repo/install
	@rm -rf ../../$(ZIP_FILE)/repo/doc

	@cd ../../ && zip -r $(ZIP_FILE).zip $(ZIP_FILE)/

clean:
	@echo "Cleaning..."
	@rm -rf __pycache__
	@rm -rf .pytest_cache
	@rm -rf .vscode

run: gui.py
	@python3 $<

test: math_tests.py parse_tests.py clean
	@pytest math_tests.py || true
	@pytest parse_tests.py || true
	@echo "Testing done."
	@$(MAKE) clean
	
profile: profiling.py data.txt
	@python3 profiling.py < data.txt

doc: Doxyfile
	@rm -rf ../doc
	@mkdir ../doc
	@doxygen $<
	@rm -rf latex/
	@mv html/ ../doc

help:
	@echo "Available targets:"
	@echo "  all      - Run the program (default)"
	@echo "  pack     - Pack the project for submission"
	@echo "  clean    - Clean up unnecessary files"
	@echo "  run      - Run the program"
	@echo "  test     - Run tests"
	@echo "  profile  - Profile the program"
	@echo "  doc      - Generate documentation"
	@echo "  help     - Display this help message"

# Phony
.PHONY:	all pack clean run test profile doc help
