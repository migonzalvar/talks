.PHONY: clean compile install minify open watch

ALL: install compile open

compile:
	pandoc -t revealjs --template ./default.revealjs -s -V revealjs-url:reveal.js -V theme:beige virtualenvs.md -o index.html

clean:
	rm -f reveal.js.tar.gz
	rm -f default.revealjs
	rm -Rf reveal.js

install: default.revealjs reveal.js.tar.gz reveal.js minify

minify:
	[ ! -e reveal.js/css/reveal.min.css ] && (cd reveal.js/css && ln -s reveal.css reveal.min.css) || true
	[ ! -e reveal.js/js/reveal.min.js ] && (cd reveal.js/js && ln -s reveal.js reveal.min.js) || true

open:
	xdg-open index.html

watch:
	browser-sync start --server --files='*.html'

default.revealjs:
	wget https://raw.githubusercontent.com/jgm/pandoc-templates/master/default.revealjs -O default.revealjs

reveal.js.tar.gz:
	wget -O reveal.js.tar.gz https://github.com/hakimel/reveal.js/archive/3.1.0.tar.gz

reveal.js: reveal.js.tar.gz
	tar xzf reveal.js.tar.gz
	mv reveal.js-3.1.0/ reveal.js
