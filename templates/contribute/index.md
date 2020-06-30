# How to contribute to mathlib

Here are some tips and tricks
to make the process of contributing as smooth as possible.

1. Use [Zulip](https://leanprover.zulipchat.com/) to
   discuss your contribution before and while you are working on it.
2. Adhere to the guidelines:
   - The [style guide](style.html) for contributors.
   - The explanation of [naming conventions](naming.html).
   - The [documentation guidelines](doc.html).
   
Once you have code that you'd like to contribute, you should open a PR.
  
## Making a Pull Request (PR)
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

## Working with an existing PR
We use GitHub "labels" to manage review. (Labels can only be edited by "GitHub collaborators", which is approximately the same as "people who have completed step 3 above")
On the main page for a PR, on the right-hand side, 
there should be a sidebar with panels "reviewers", "assignees", "labels", etc. 
Click on the "labels" header to add or remove labels from the current project. The most important labels are "request-review" and "changes-requested". If you label your PR with "request-review", someone will probably "review" it within a few days (depending on the size of the PR; smaller PRs will get quicker responses). The reviewer will probably leave comments and change the label to "changes-requested". You should address each comment, clicking the "resolve conversation" button once the problem is resolved. Ideally each problem is resolved with a new commit, but there is no hard rule here. Once all requested changes are implemented, you should change the label back to "request-review" to start the process over again.

After some iteration, a reviewer will "approve" the PR. A bot called `bors` will make a comment with instructions. After following these, the PR will get added to the "merge queue". The merge queue gets cleared automatically by bors, but this takes some finite amount of time as it requires building branches of mathlib.

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
