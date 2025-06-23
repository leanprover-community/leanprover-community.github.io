# Lean prover community website


The deployed website lives on the `master` branch of this repository.
To make changes to the website, please fork the repository and make a PR against the
[`lean4`](https://github.com/leanprover-community/leanprover-community.github.io/tree/lean4)
branch.
Once your PR is merged, CI will automatically deploy the changes to the `master` branch.

## Dependencies

* `pip install -r requirements.txt`

Building the bibliography requires [`bibtool`](https://github.com/ge-ne/bibtool). If `bibtool` is not found, the build script will print a warning and just copy the raw `lean.bib` file to the target.

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


If you want to retrieve the list of Zulip users to get the users map, the
environment variable `ZULIP_KEY` should be set with the Zulip API key of the
map scraper bot.

If you want to work on a new feature, there are several helpful tricks to know.

First you will very quickly hit the GitHub API rate limit without
authentication. You can
[create a personal access token](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens#creating-a-personal-access-token-classic)
and run `GITHUB_TOKEN=my_token_copied_from_github ./make_site --local` during
your experiments.

You can also run the script once normally and then run
`NODOWNLOAD=1 ./make_site --local` to build the website using the information
previously downloaded. This information is stored into the `data_cache` folder.
If you need the script to download something but not everything you can
temporarily change the relevant `if DOWNLOAD:` into a `if not DOWNLOAD:`.

You can also choose to render only certain templates using
`./make_site --local --only my_template.html`.
This argument can actually be a regular expression, but giving one template
name is the most common use case.


## TODO

* Better integration with API docs
* Use webpack or similar to bundle all the javascript?

## Lean 3 website

The files and history for the leanprover-community Lean 3 website can be found in the
[`lean3`](https://github.com/leanprover-community/leanprover-community.github.io/tree/lean3) branch of this repo.

## Old website

The files and history for the old leanprover-community website can be found in the
[`oldsite`](https://github.com/leanprover-community/leanprover-community.github.io/tree/oldsite) branch of this repo.
