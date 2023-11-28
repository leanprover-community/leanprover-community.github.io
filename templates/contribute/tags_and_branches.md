# The Lean Github ecosystem

Documentation of the branches, tags, and CI workflows relevant for making pull requests to Lean, Std, and
Mathlib.

* [Things you need to know](#things-you-need-to-know) is relevant for everyone
* [Tags and branches](#tags-and-branches) is for "experts only" who are making or fixing
  breaking changes in Lean, or who want to understand the inner workings of Mathlib CI.

## Things you need to know

* If you are making a pull request to `leanprover/lean4` which may involve breaking changes,
  please rebase your PR onto the `nightly` branch. This will enable combined CI with Mathlib.

* If you are making a pull request to `leanprover-community/mathlib4`,
  please ask for "write" access to the repository via the [zulip chat](https://leanprover.zulipchat.com/#narrow/stream/287929-mathlib4/topic/github.20permission), and push your branch to that repo.
  This will enable Mathlib's `.olean` cache to include your pull request.

## Tags and branches

### `leanprover/lean4`

* Development occurs on the `master` branch.
* Stable releases and release candidates have tags, e.g. `v4.2.0` or `v4.3.0-rc1`.
  * To use one of these releases in a project, your `lean-toolchain` should contain e.g. `leanprover/lean4:v4.2.0`.
* Stable releases arrive at the end of each month, and are identical to the last release candidate.
* The first release candidate of the next version is released immediately after the stable release.
* Each version has a `releases/v4.X.0` feature branch, which may contain
  * additional commits for release notes
  * cherry picked commits from `master` for critical fixes released via release candidates.
* We make a regular nightly release from `master`, which has a tag e.g. `nightly-2023-11-01` on the
  `leanprover/lean4-nightly` repository.
  * To use a nightly release in a project, your `lean-toolchain` should contain e.g. `leanprover/lean4:nightly-2023-11-01`.
* There is a `nightly` branch on `leanprover/lean4` which follows the most recent commit which was
  used to construct a nightly release.
* Every PR automatically receives a toolchain after CI completes successfully.
  To use PR #NNNN in a project, your `lean-toolchain` should contain
  `leanprover/lean4-pr-releases:pr-release-NNNN`.
* Every PR automatically generates a `lean-pr-testing-NNNN` branch at Mathlib,
  described in detail below, and results from this branch are reported via comments
  in the PR discussion.
* For any PR that potentially affects Std or Mathlib, you should base your PR off the HEAD of the `nightly` branch.
  The combined CI for Std and Mathlib will not run automatically unless this is the case.
* You can determine the most recent nightly release in the history of your PR by running
  `script/most-recent-nightly-tag.sh` in the Lean repository.

### `leanprover/std4` (aka 'Std')

* Development occurs on `main`.
* Std uses the latest stable release or release candidate in its `lean-toolchain`.
  * Because we release `v4.X+1.0-rc1` immediately after releasing `v4.X.0`,
    Std is only very briefly on stable releases.
* The first commit on `main` which uses a new toolchain is tagged with the version number of that
  toolchain (e.g. `v4.2.0`).
* There is a branch `stable` which follows the `v4.X.0` tags.
* Std has a branch `bump/v4.X.0` for the upcoming stable release of Lean,
  * which contains adaptations for breaking changes that have been approved by the maintainers
  * and which will be using a `leanprover-lean4:nightly-YYYY-MM-DD` toolchain.
* Std has a branch `nightly-testing` which
  * uses a recently nightly release (this is updated automatically)
  * has all commits from `main` merged into it automatically
  * may have any changes from `bump/v4.X.0` merged into it manually
  * may have any other commits, including unreviewed ones, required to keep the `nightly-testing`
    branch working again recent nightly releases.
* Failures in CI on the `nightly-testing` are reported by a bot to zulip in the private
  "Mathlib reviewers" stream.
* Success in CI on the `nightly-testing` branch results in the creation or updating of a branch
  `nightly-testing-YYYY-MM-DD` to match that commit.
  * Thus if `nightly-testing-YYYY-MM-DD` exists, we know that on it:
    * the `lean-toolchain` is `leanprover/lean4:nightly-YYYY-MM-DD`, and
    * CI succeeds.
* When changes are required to Std to adapt to a breaking change in Lean,
  you will need to make a branch, and later open a PR from that branch.
  (Note that the steps below happen automatically at Mathlib,
  but need to be done manually for Std.)
  * If the change was made in `leanprover/lean4#NNNN`,
    then the Std adaptation branch should be called `lean-pr-testing-NNNN`.
  * The Std adaptation branch should be based off the branch `nightly-testing-YYYY-MM-DD`
    where `YYYY-MM-DD` is the date of the nightly release that your Lean PR is based off
    (you can check this will `script/most-recent-nightly-tag.sh` in the Lean repository).
  * If the `nightly-testing-YYYY-MM-DD` branch does not yet exist, you will need to wait
    (and possibly move forward to a subsequent nightly).
    Contact @semorrison for assistance if needed.
  * Ideally you will push the `lean-pr-testing-NNNN` branch to the main Std repository;
    we can provide write access if needed.
  * The `lean-toolchain` on this branch must contain `leanprover/lean4-pr-releases:pr-release-NNNN`.
  * You may open a PR from the `lean-pr-testing-NNNN` branch, either before or after
    making the required adaptations.
  * When opening the PR, remember to set the base branch to `nightly-testing-YYYY-MM-DD`.
  * Please label the PR with the `v4.X.0` and 'depends on core changes' labels.
    (Or ask for this to be done if you don't have write access.)
  * Once the Lean PR has been merged and published in a nightly release, the Std adaptation PR
    * should have its `lean-toolchain` updated to `leanprover/lean4:nightly-YYYY-MM-DD`
    * may be merged into `nightly-testing` as needed to keep `nightly-testing` working
  * Once the Std adaptation PR has been approved,
    a maintainer will merge it into `bump/v4.X.0` (not `nightly-testing-YYYY-MM-DD`).
* It is always allowed to merge `bump/v4.X.0` into `nightly-testing`, but not conversely.
  (Changes to `bump/v4.X.0` have been reviewed, but changes to `nightly-testing` may not have been.)
* When it is time to update Std to a new Lean release,
  *hopefully* all that is required is to make a new PR
  consisting of squash merging `bump/v4.X.0` to `main`.

### `leanprover-community/mathlib4` (aka 'Mathlib')

* Everything said above about Std applies to Mathlib, except:
  * Development occurs on `master`.
  * All PRs to Mathlib should be made from branches of the Mathlib repository itself.
    * This is required for Mathlib's `.olean` caching mechanism.
    * Please ask on the [zulip chat](https://leanprover.zulipchat.com/#narrow/stream/287929-mathlib4/topic/github.20permission) for "write" permission to Mathlib.
      Please write a sentence about your background and plans.
* The `nightly-testing-*` and `bump/v4*` branches are write protected,
  so may only be modified via PRs, maintainers, or the relevant bots.
* Note that the `nightly-testing` branch of Mathlib may use the `nightly-testing` branch of Std as required.
* Similarly a `bump/v4.X.0` branch of Mathlib may use the `bump/v4.X.0` branch of Std as required.
* Branches `lean-pr-testing-NNNN` are automatically created for any Lean PR that passes CI,
  and is based off a nightly release. (Unlike for Std, where they must be created manually.)
* Mathlib adaptation PRs on `lean-pr-testing-NNNN` branches may need to change the Std dependency
  to use a `lean-pr-testing-NNNN` branch of Std, if Std also experiences breakages.

### Combined CI between Lean and Mathlib

* For every PR to Lean, we attempt to run Mathlib CI against the resulting toolchain.
* For this to work, you will need to rebase your PR onto the `nightly` branch.
  * If you have not done this, a bot will comment saying that it can not run Mathlib CI,
    and advising that if you need this you will need to rebase your PR onto `nightly`.
* Further, the latest nightly release may or may not have a corresponding
  `nightly-testing-YYYY-MM-DD` branch on Std and Mathlib (see above).
  * If this branch does not yet exist, a bot will comment on your PR notifying you
    that it can not run Mathlib CI, and advising that it will try again when you either
    * push more commits, or
    * rebase your PR onto a future update of the `nightly` branch
      (note that this may be necessary if Mathlib is having persistent problems adapting
      to the most recent nightly release).
  * If this branch does exist, then the bot will automatically create a
    `lean-pr-testing-NNNN` branch at Mathlib from the `nightly-testing-YYYY-MM-DD` branch,
    and set the toolchain to `leanprover/lean4-pr-releases:pr-release-NNNN`.
    * Subsequent CI results from that Mathlib branch will be reported back to the Lean PR
      in the form of comments.

![Overview of branches at Mathlib/Std](img/tags_and_branches.png)