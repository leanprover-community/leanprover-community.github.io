# How to contribute to mathlib

Here are some tips and tricks
to make the process of contributing as smooth as possible.

* Use [Zulip](https://leanprover.zulipchat.com/) to
   discuss your contribution before and while you are working on it.
* Create a GitHub account and add your GitHub username to your Zulip profile, using [the personal settings panel](https://leanprover.zulipchat.com/#settings/profile).
We also strongly encourage setting your display name on Zulip to be your real name.
* Adhere to the guidelines:
   - The [style guide](style.html) for contributors.
   - The explanation of [naming conventions](naming.html).
   - The [documentation guidelines](doc.html).

## What to contribute to mathlib

Small fixes (for example fixes in docstrings) and single-lemma additions in already-existing theories
are almost always welcome as contributions to mathlib. Longer PRs which extend existing theories are also almost
always welcome. 

But what about adding completely new theories to `mathlib`? Here, things can be more nuanced. The first question 
you will need to consider is whether the material you want to contribute is a good fit for `mathlib`. 
Whilst there is currently no formal description of exactly what mathlib's remit is, here are some questions which you 
can ask about your proposed contribution.

* Is the material typically taught or studied in a mathematics department? Would it naturally be part 
of an undergradute or graduate mathematics course, or research level mathematics study group? If not, then the material 
may not be in scope for `mathlib`.

* Is the topic of the material contained within the 
[mathematical interests of the `mathlib` maintainers](https://github.com/leanprover-community/mathlib4?tab=readme-ov-file#maintainers)? 
If not, then the maintainers might find your code hard to maintain as lean and `mathlib` evolve over time, 
which again may make it not a good fit for `mathlib`.

In particular the remit of mathlib should *not* be thought of as "all of mathematics and related areas". 
As the number of open PRs increases, the maintainers will sometimes need to make some hard decisions.

If you are not sure about whether your proposed topic is a good fit for mathlib, then please feel
free to open a discussion in the [`#mathlib` channel](https://leanprover.zulipchat.com/#narrow/channel/287929-mathlib4/) on the Lean Zulip.

An issue related to the fact that the expertise of the maintainers may not cover all of mathematics: 
you may want to think about *who* is going to review your potential PR. Contributors are encouraged 
to seek out reviewers for their PRs. A PR reviewer does *not* have to be a maintainer! This seems
to be a common misconception by the community. Reviews of PRs, especially from new reviewers, 
are essentially always welcome. 

Please also consider the possibility of creating a standalone repository, and adding `mathlib` as a dependency. 
There are many Lean repositories on github, indexed by [reservoir](https://reservoir.lean-lang.org). 
And [here](https://reservoir.lean-lang.org/@leanprover-community/mathlib/dependents) are those projects
which have `mathlib` has a dependency. The solution of having a new project which depends on
`mathlib` is a particularly good fit for projects in areas which do not align with the 
expertise of the mathlib maintainers. One example of such a repository is the [combinatorial game
theory repository](https://github.com/vihdzp/combinatorial-games). This solution is also a good fit
for projects which would like to move quickly; at the time of writing (Sep 2025), mathlib has just under 2000 open PRs
and it may take time for mathlib contributions to be reviewed and merged.

### Style changes

`mathlib` has a [style guide](https://leanprover-community.github.io/contribute/style.html) and PRs fixing
style violations documented in this guide are welcome. Other stylistic PRs that don't have explicit
approval by the authors of the affected files may be closed. We invite authors to instead discuss the proposed
change on Zulip and, when significant consensus among reviewers is reached, to open a PR to the style guide.

## Working on mathlib

We use `git` to manage and version control `mathlib`.

Please see [the Git Guide for Mathlib4 Contributors](git.html) for detailed instructions if you have not contributed to an open source project with git before.

The `master` branch is the "production" version of mathlib.
It is essential that everything in the master branch compiles without errors, and there are no `sorry`s.
To ensure this, we only commit changes to `master` that have passed automated Continuous Integration ("CI") tests, and have been approved by mathlib maintainers.

While you're working on a new contribution to `mathlib`, you should do this on a different branch.
You should do this in your own fork of the `mathlib` repository.

Typical workflow:
* To get started, you'll need a local copy of mathlib.
* First, you'll need to go to https://github.com/leanprover-community/mathlib4 and click "Fork" in the top right,
  to make your own fork of the repository.
  Your fork is at [https://github.com/USER/mathlib4](https://github.com/USER/mathlib4).
* Now make a local clone of your fork and configure it properly.
  See [the Git Guide for Mathlib4 Contributors](git.html) for detailed step-by-step instructions on setting up your fork correctly.
  ```
  git clone https://github.com/YOUR_USERNAME/mathlib4.git
  cd mathlib4
  lake exe cache get
  ```
* The steps above only need to be done once (not once for each contribution).
* Now, each time you want to work on a new change to mathlib, create a new branch:
  ```
  git switch -c my_new_branch   # This creates a new branch and switches to it
  ```
* Make local changes, e.g. using Visual Studio Code using the Lean extension.
* Commit your changes using `git commit -a` (or via the VS Code interface).
* If you'd like to compile everything locally to check you didn't break anything, run
`lake build`. This may take a long time if you modified files low down in the import hierarchy.
It's also okay to let our central CI servers do this for you by pushing your changes after you've opened a PR to the main repository.
* If you created new files, run `lake exe mk_all`. This will update `Mathlib.lean` to ensure that all files are imported there.
* In order to push your changes back to the repository on github, use
  ```
  git push
  ```
  If this complains about the remote not being configured, follow the advice in the output from `git` and run
  ```
  git push --set-upstream origin my_new_branch
  ```
* Once you've opened a PR to the main `mathlib` repository (see below),
  continuous integration will automatically kick in at this point.
  You can view the CI status on your PR page on GitHub (there will be a green tick if everything works,
  otherwise a yellow circle if CI is still working, or a red cross if something went wrong).
  You can also check CI status using the GitHub CLI: `gh pr status`.
* After CI finishes, you can run `lake exe cache get` to download compiled oleans.


## Making a Pull Request (PR)

Once you're happy with your local changes, it's time to make a pull request.

* If you haven't already, please come to https://leanprover.zulipchat.com/, introduce yourself, and mention your new PR.

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
Labels can only be edited directly by "GitHub collaborators", which is approximately the same as "people who have write access".
However, anyone can add/remove the labels below by writing the following commands in a comment on the PR (each on its own line):
- `awaiting-author` will add the **"awaiting-author"** label
- `-awaiting-author` will remove the **"awaiting-author"** label
- `WIP` will add the **"WIP"** label
- `-WIP` will remove the **"WIP"** label
- `easy` will add the **"easy"** label
- `-easy` will remove the **"easy"** label

This list is exhaustive.  If you would like to add a different label, please, bring it up on Zulip!

If your PR builds (has a green checkmark), someone will "review" it within a few weeks (depending on the size of the PR; smaller PRs will get quicker responses). They will probably leave comments and add the label **"awaiting-author"**. You should address each comment, clicking the "resolve conversation" button once the problem is resolved. Ideally each problem is resolved with a new commit, but there is no hard rule here. Once all requested changes are implemented, you should remove the **"awaiting-author"** label to start the process over again.

There are different groups of people that can review your PR: anyone, [reviewers](../teams/reviewers.html) and [maintainers](../teams/maintainers.html).
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
