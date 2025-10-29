COOKIECUTTERS_DIR ?= $(CURDIR)/../..
PROJECT_SLUG = \{\{cookiecutter.project_slug\}\}
TMP_DIR ?= /tmp

##
## == Testing ==
.PHONY: test
test:  ## Render the cookiecutter and test it
	@ cd  $(PROJECT_SLUG) && git clean -X -d -f
	@ pytest -s --doctest-modules --junitxml=junit/test-results.xml test.py


#
# File based recipes (advanced usage)
#

.DEFAULT_GOAL := help
help: Makefile
	@grep -E '(^[a-zA-Z_-]+:.*?##.*$$)|(^##)' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[32m%-30s\033[0m %s\n", $$1, $$2}' | sed -e 's/\[32m## /[33m/'
