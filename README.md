# Lean prover community website

## Dependencies

* `pip install -r requirements.txt`

Building the bibliography requires [`bibtool`](https://github.com/ge-ne/bibtool).

In order to rebuild the CSS from SCSS, you also need:

* [sass](https://sass-lang.com/)
* [bootstrap](https://github.com/twbs/bootstrap/archive/v4.4.1.zip)
  should be unpacked at the project root

The website relies on several components which are built in other repositories:
- [`mathlib_stats`](https://github.com/leanprover-community/mathlib_stats)
- [`lean4web`](https://github.com/leanprover-community/lean4web)
- [`mathlib4_docs`](https://github.com/leanprover-community/mathlib4_docs) (built by CI in [doc-gen4](https://github.com/leanprover/doc-gen4/))

## Building

* Build CSS if needed: `sass scss/lean.scss > css/lean.css`
* Build site using `make_site.py`. Use option `--local` for local
  viewing (internal url will be prefixed by local file path).
  Use option `--reload` to continuously build when templates are
  changed (this won't work for watching changes in `data/`).

## TODO

* Better integration with Zulip archive
* Better integration with API docs
* Use webpack or similar to bundle all the javascript?

## Lean 3 website

The files and history for the leanprover-community Lean 3 website can be found in the
[`lean3`](https://github.com/leanprover-community/leanprover-community.github.io/tree/lean3) branch of this repo.

## Old website

The files and history for the old leanprover-community website can be found in the
[`oldsite`](https://github.com/leanprover-community/leanprover-community.github.io/tree/oldsite) branch of this repo.
