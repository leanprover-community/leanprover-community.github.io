# Lean community blog

## Setup

```bash
pip install Nikola Jinja2 pyphen typogrify aiohttp watchdog ruamel.yaml html5lib
```

If you want shell completion for `nikola` commands, see [these instructions](https://getnikola.com/handbook.html#shell-tab-completion).

## Writing a new page or post

Use command `nikola new_page -e` or `nikola new_post -e`, give a title and edit
the content in markdown (you need to set the `EDITOR` environment variable). 
You can also simply copy and existing file from the `posts` folder and modify it.
See the existing pages and posts for inspiration.

## Editing an existing page of post

Pages are in the `pages` folder, posts in the `posts` folder.

## Building the website

`nikola auto` will build the website, serve it locally at `http://0.0.0.0:8000/` and wait for changes to rebuild it. The website is put in a `output` folder.
