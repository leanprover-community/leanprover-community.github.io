# How to contribute to mathlib

Here are some tips and tricks
to make the process of contributing as smooth as possible.

1. Use [Zulip](https://leanprover.zulipchat.com/) to
   discuss your contribution before and while you are working on it.
2. Adhere to the guidelines:
   - The [style guide](style.html) for contributors.
   - The explanation of [naming conventions](naming.html).
   - The [documentation guidelines](doc.html).
3. Introduce yourself on Zulip and ask for write access to non-master branches of the mathlib repository. Make your changes on a branch of the main repository.
   - The title of the PR should follow our [commit conventions](https://github.com/leanprover-community/lean/blob/master/doc/commit_convention.md).
4. If you've made a lot of changes/additions, try to make many PRs containing small, self-contained pieces. This helps you get feedback as you go along, and it is much easier to review. This is especially important for new contributors.
5. You can use `leanproject` to manage your work. Here are some detailed steps for for sharing your shiny new lemmas about sets:
   * `leanproject get -b mathlib:shiny_lemma` This will create a (local) branch called `shiny_lemma` and also create a local folder called `mathlib_shiny_lemma` with a copy of mathlib for you to work on.
   * edit the necessary files, e.g. `data/set/basic.lean`
   * If you are anxious, `leanproject build` to check you didn't break anything. This will be long because you edit a fundamental file, imported by pretty much everything else.
   * `git commit -a`
   * `git push origin` This pushes your branch to GitHub.
   * Visit [mathlib on GitHub](https://github.com/leanprover/mathlib) to see an invitation to open a PR based on what you just did.
   * Wait for continuous integration to build your branch if you didn't do it locally, `leanproject get-cache` will then download what was built by CI (Continuous Integration)

- See [Caching compilation](#caching-compilation) for commands to automatically call `leanproject get-cache`.

## Caching compilation

In the `mathlib` git repository, you can run the following in a terminal:

```sh
sudo pip3 install mathlibtools
leanproject hooks
```

This will install the `leanproject` tool.  The call to `leanproject hooks`
sets up git hooks that will call cache the olean files when making a commit
and fetching the olean files when checking out a branch.
See the [mathlib-tools documentation](https://github.com/leanprover-community/mathlib-tools/blob/master/README.md)
for more information.
