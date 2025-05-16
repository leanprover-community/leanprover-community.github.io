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
To ensure this, we only commit changes to `master` that have passed automated Continuous Integration ("CI") tests, and have been approved by mathlib maintainers.

While you're working on a new contribution to `mathlib`, you should do this on a different branch.
It's okay to do this in your own fork of the `mathlib` repository.

Eventually, to make a pull request, you'll need to migrate your work to a branch of the main mathlib repository,
as our CI works better this way.
It's polite to prefix the branch name with your github username, so it's easier for us to clean up clutter.
To work in the main repository, you can introduce yourself on Zulip and ask for write access to non-`master` branches of the mathlib repository.
Either [make your own thread](https://leanprover.zulipchat.com/#narrow/stream/113489-new-members) to introduce yourself, or ask for access in
[this topic](https://leanprover.zulipchat.com/#narrow/stream/287929-mathlib4/topic/github.20permission).
Please include your GitHub username in your request and add this username to your Zulip profile, using [the personal settings panel](https://leanprover.zulipchat.com/#settings/profile).
We also strongly encourage setting your display name on Zulip to be your real name.

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
* If you'd like to compile everything locally to check you didn't break anything, run
`lake build`. This may take a long time if you modified files low down in the import hierarchy.
It's also okay to let our central CI servers do this for you by pushing your changes.
* If you created new files, run `lake exe mk_all`. This will update `Mathlib.lean` to ensure that all files are imported there.
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

* If you are moving or deleting declarations, please include these lines at the bottom of the commit message
(that is, before the `---`) using the following format:

Moves:
- Vector.* -> Mathlib.Vector.*
- ...

Deletions:
- Nat.bit1_add_bit1
- ...

Any other comments you want to keep out of the PR commit should go
below the `---`.

## Lifecycle of a PR

Many reviewers use the [review queue](../queueboard/review_dashboard.html) to identify PRs that are ready for review.
The instructions below will ensure that your PR appears on that queue; if it doesn't appear there it may not receive much attention.
Everyone is also invited to regularly look at the queue (it is linkified as `#queueboard` on Zulip), and write reviews of PRs within their expertise.
You can check if your [PR is on the queue](../queueboard/on_the_queue.html), and if not, what is needed to get it on.

The review queue is controlled by GitHub "labels".
On the main page for a PR, on the right-hand side,
there should be a sidebar with panels "reviewers", "assignees", "labels", etc.
Click on the "labels" header to add or remove labels from the current project.
(Labels can only be edited by "GitHub collaborators", which is approximately the same as "people who have asked for write access".)

If your PR builds (has a green checkmark), someone will "review" it within a few weeks (depending on the size of the PR; smaller PRs will get quicker responses). They will probably leave comments and add the label **"awaiting-author"**. You should address each comment, clicking the "resolve conversation" button once the problem is resolved. Ideally each problem is resolved with a new commit, but there is no hard rule here. Once all requested changes are implemented, you should remove the **"awaiting-author"** label to start the process over again.

There are diffent groups of people that can review your PR: anyone, [reviewers](../teams/reviewers.html) and [maintainers](../teams/maintainers.html).
Anyone who has something useful to say can review your PR. 
If they think your PR is ready to move to the next stage, they might leave an "approving" review on GitHub. 
These reviews are taken into account by reviewers. 
If a reviewer considers your PR ready to be merged, they will add the **"maintainer-merge"** label to your PR. 
These are used by maintainers to prioritize their review.
Maintainers are always the ones to give final approval.
Maintainers have reviewer rights, but also further powers (such as merging PRs).
Depending on availability, a maintainer could be the first reviewer to look at your PR: in this case,
your PR could get merged without being "maintainer merge"d first. 
Review times can vary depending on availability of our volunteers. 
To speed up the process, you can look at the [review guidelines](pr-review.html) and try to make sure your PR adheres to them.
If you want to explicitly ask for a review, please create a topic in the [PR reviews](https://leanprover.zulipchat.com/#narrow/channel/144837-PR-reviews/) stream on Zulip.

If a maintainer has approved your PR, a **"ready-to-merge"** label is automatically applied to the PR.
A bot called `bors` will take it from here. (See [here](https://github.com/leanprover-community/mathlib/blob/master/docs/contribute/bors.md) for more detail about bors.)
The PR will get added to the ["merge queue"](https://mathlib-bors-ca18eefec4cb.herokuapp.com/repositories/16).
The merge queue is processed automatically, but this takes some finite amount of time as it requires building branches of mathlib.

In some cases, a maintainer will "delegate" the PR. You'll see that your PR now has a **"delegated"** label. This either means that there are a few final changes requested, but that the maintainer trusts you to make these and send the PR to bors yourself, or that the maintainer wants to give you one final chance to look things over before the PR is merged. In either case, when you are ready, writing a comment containing the line "bors merge" will result in the PR being merged.

Here are some other frequently-used labels:

- A **"WIP"** (= work in progress) PR still needs some foundational work (e.g. maybe it still contains `sorry`s) before getting reviewed. Post a WIP if you want to announce that you're working on something you expect to finish soon.

- A **"RFC"** (= request for comment) is a PR about a change that might be controversial or need a decision from an expert about
whether to proceed at all.

- You can add **"awaiting-CI"** if you're not certain whether CI will succeed.
  This will temporarily hide the PR on the main review queue.
  The label will be automatically removed when CI is complete.

- Consider adding the **"help wanted"** label to directly solicit contributions.

- The **"blocked-by-other-PR"** label means that some specific other PR(s) should be resolved before addressing this one. To add the "blocked-by-other-PR" label to your PR, include the PR numbers of the dependencies in the PR comment (following the example hidden in the comment there) so that others can see at a glance which PRs should be reviewed first. The label will be added automatically by a bot and will also be removed automatically when the other PRs have been merged. PRs with this label do not appear on the review queue.

- The **easy** label should be used to mark PRs that can be immediately approved. Maintainers and reviewers often look at easy PRs first to keep the queue flowing. Easy PRs typically add a single lemma, correct typos in documentation, or similar. If you have any doubt whether your PR is trivial you should not add this label. In particular, a PR is generally *not* easy if the diff is more than 25 lines, it adds any definitions or new files, or it adds any `simp` lemmas or instances that are not immediately analogous to existing `simp` lemmas or instances.

- The **delegated** label means that a maintainer has issued the "bors delegate" (or "bors d+") command. The author of the PR
should now merge the PR themselves once any final requested changes have been made, and CI has succeeded. They can do this using
"bors merge".

### Dealing with merge conflicts

Due to the fact that multiple people work on mathlib in parallel, someone might have introduced a change on `master` that conflicts with a change that you're proposing on your PR. If it happens with your PR, a bot will automatically add the **"merge-conflict"** label, and your PR will not appear on the review queue. Check [this GitHub tutorial](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/addressing-merge-conflicts/resolving-a-merge-conflict-on-github) on how to resolve merge conflicts by using their online tool.
Once the conflict has been resolved, the **"merge-conflict"** label will automatically be removed, and your PR will return to the review queue.
