# How to contribute to mathlib

Here are some tips and tricks
to make the process of contributing as smooth as possible.

* Use [Zulip](https://leanprover.zulipchat.com/) to
   discuss your contribution before and while you are working on it.
* Adhere to the guidelines:
   - The [style guide](style.html) for contributors.
   - The explanation of [naming conventions](naming.html).
   - The [documentation guidelines](doc.html).

Once you have code that you'd like to contribute, you should open a PR.

## Working on mathlib

We use `git` to manage and version control `mathlib`.
The `master` branch is the "production" version of mathlib.
It is essential that everything in the master branch compiles without errors, and there are no `sorry`s.
To ensure this, we only commit changes to `master` that have passed CI tests, and have been approved by mathlib maintainers.

While you're working on a new contribution to `mathlib`, you should do this on a different branch.
It's okay to do this in your own fork of the `mathlib` repository,
or you can introduce yourself on Zulip and ask for write access to non-`master` branches of the mathlib repository,
you can either [make your own thread](https://leanprover.zulipchat.com/#narrow/stream/113489-new-members) to introduce yourself, or ask for access in
[this topic](https://leanprover.zulipchat.com/#narrow/stream/287929-mathlib4/topic/github.20permission).
Please include your GitHub username in your request (and add this username to your Zulip profile, using the personal settings panel).
It's polite to prefix the branch name with your username, so it's easier for us to clean up clutter.
(Once you're making a pull request, we'll ask you to do so from a branch of the mathlib repository,
rather than from your own fork, as CI works better this way.)

Typical workflow:
* To get started, you'll need a local copy of mathlib.
* If you've asked for write access (recommended above), you can just use <https://github.com/leanprover-community/mathlib4>.
  Otherwise, you'll need to go to https://github.com/leanprover-community/mathlib4 and click "Fork" in the top right,
  to make your own fork of the repository.
  Your fork is at [https://github.com/USER/mathlib4](https://github.com/USER/mathlib4).
* Now make a local clone of the repository.
  ```
  git clone https://github.com/leanprover-community/mathlib4.git
  cd mathlib4
  lake exe cache get
  ```
* The steps above only need to be done once (not once for each contribution).
* Now, each time you want to work on a new change to mathlib, create a new branch:
  ```
  git switch -c my_new_branch   # This creates a new branch and switches to it
  ```
  If you've asked for write access you can push your new branch to mathlib which
  comes with some advantages (see below).
* Sometimes you may not want to create a new branch, but instead work on a branch
  that someone else created, or you created from a different computer.
  In that case you need to use `git switch their_new_branch` (note there is no `-c` here).
* Make local changes, e.g. using Visual Studio Code using the Lean extension.
* Commit your changes using `git commit -a` (or via the VS Code interface).
* If you'd like to compile everthing locally to check you didn't break anything, run
`lake build`. This may take a long time if you modified files low down in the import hierarchy.
It's also okay to let our central CI servers do this for you by pushing your changes.
* In order to push your changes back to the repository on github, use
  ```
  git push
  ```
  If this complains about the remote not being configured, follow the advice in the output from `git` and run
  ```
  git push --set-upstream origin my_new_branch
  ```
* If you're working on the main `mathlib` repository rather than your own fork,
  continuous integration will automatically kick in at this point.
  You can view the output by visiting
  https://github.com/leanprover-community/mathlib4/tree/my_new_branch
  (There will be a green tick on the line describing the most recent commit if everything works,
  otherwise a yellow circle if CI is still working, or a red cross if something went wrong.
  Click on the red cross to see details.)
  You can also check CI status on the command line by installing [`hub`](https://hub.github.com/) and running `hub ci-status`.
* After CI finishes, you can run `lake exe cache get` to download compiled oleans.


## Making a Pull Request (PR)

Once you're happy with your local changes, it's time to make a pull request.

* If you haven't already asked for write access to non-master branches of the mathlib repository,
please come to https://leanprover.zulipchat.com/, introduce yourself, and ask for this permission.

* Push your changes to a branch on the main repository, if they weren't already there.

* If you've made a lot of changes/additions, try to make many PRs containing small, self-contained pieces; in general, the smaller the better!
  This helps you get feedback as you go along, and it is much easier to review.
  This is especially important for new contributors as it prevents wasted effort.

* The title and description of the PR should follow our [commit conventions](commit.html).

## Lifecycle of a PR

We use GitHub "labels" to manage review. (Labels can only be edited by "GitHub collaborators", which is approximately the same as "people who have asked for write access".)

On the main page for a PR, on the right-hand side,
there should be a sidebar with panels "reviewers", "assignees", "labels", etc.
Click on the "labels" header to add or remove labels from the current project.

The most important labels are "awaiting-review" and "awaiting-author". If your PR builds (has a green checkmark) and you label your PR with **"awaiting-review"**, someone will probably "review" it within a few days (depending on the size of the PR; smaller PRs will get quicker responses). The reviewer will probably leave comments and change the label to **"awaiting-author"**. You should address each comment, clicking the "resolve conversation" button once the problem is resolved. Ideally each problem is resolved with a new commit, but there is no hard rule here. Once all requested changes are implemented, you should change the label back to "awaiting-review" to start the process over again.

After some iteration, a reviewer will "approve" the PR and the "ready-to-merge" label will be automatically applied to the PR. A bot called `bors` will take it from here. (See [here](https://github.com/leanprover-community/mathlib/blob/master/docs/contribute/bors.md) for more detail about bors.)
After responding appropriately to bors (if necessary), the PR will get added to the ["merge queue"](https://app.bors.tech/repositories/37904). The merge queue gets cleared automatically, but this takes some finite amount of time as it requires building branches of mathlib.

Here are some other frequently-used labels:

- A **"WIP"** (= work in progress) PR still needs some foundational work (e.g. maybe it still contains `sorry`s) before getting reviewed. Post a WIP if you want to announce that you're working on something you expect to finish soon.

- A **"RFC"** (= request for comment) is a PR about a change that might be controversial or need a decision from an expert about
whether to proceed at all.

- You can add **"awaiting-CI"**, which will temporarily hide the PR on the main review queue.
  This label will be automatically removed when CI is complete.

- Consider adding the **"help wanted"** label to directly solicit contributions.

- The **"blocked-by-other-PR"** label means that some specific other PR(s) should be resolved before addressing this one. To add the "blocked-by-other-PR" label to your PR, include the PR numbers of the dependencies in the PR comment (following the example hidden in the comment there) so that others can see at a glance which PRs should be reviewed first. The label will be added automatically by a bot and will also be removed automatically when the other PRs have been merged.

- The **easy** label should be used to mark PRs that can be immediately approved. Maintainers and reviewers often look at easy PRs first to keep the queue flowing. Easy PRs typically add a single lemma, correct typos in documentation, or similar. If you have any doubt whether your PR is trivial you should not add this label. In particular, a PR is generally *not* easy if the diff is more than 25 lines, it adds any definitions or new files, or it adds any `simp` lemmas or instances that are not immediately analogous to existing `simp` lemmas or instances.

### Dealing with merge conflicts

Due to the fact that multiple people work on mathlib in parallel, someone might have introduced a change on `master` that conflicts with a change that you're proposing on your PR. If it happens with your PR, check [this GitHub tutorial](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/addressing-merge-conflicts/resolving-a-merge-conflict-on-github) on how to resolve merge conflicts by using their online tool.
