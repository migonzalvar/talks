SHELL:=/bin/bash

.PHONY: start
start:
	@( \
	source .venv/bin/activate;\
	command -v doitlive >/dev/null 2>&1 || { echo >&2 "Please, install doitlive"; exit 1; };\
	doitlive play --prompt deadsimple -q session.sh;\
	)

.PHONY: install
install:
	env PIPENV_VENV_IN_PROJECT=1 pipenv sync
