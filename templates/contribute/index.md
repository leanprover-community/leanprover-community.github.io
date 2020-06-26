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
5. You can use `leanproject get-cache` to fetch `.olean` binaries.
   ```text
   leanproject get-cache
   git checkout -b my_new_feature
   ```
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
