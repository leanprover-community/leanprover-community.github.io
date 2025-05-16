# The Lean Github ecosystem

Documentation of the branches, tags, and CI workflows relevant for making pull requests to Lean, Std, and
Mathlib.

* [Things you need to know](#things-you-need-to-know) is relevant for everyone
* [Tags and branches](#tags-and-branches) is for "experts only" who are making or fixing
  breaking changes in Lean, or who want to understand the inner workings of Mathlib CI.

## Things you need to know

* If you are making a pull request to `leanprover/lean4` which may involve breaking changes,
  please rebase your PR onto the `nightly-with-mathlib` branch. This will enable combined CI with Mathlib.

* If you are making a pull request to `leanprover-community/mathlib4`,
  please ask for "write" access to the repository via the [zulip chat](https://leanprover.zulipchat.com/#narrow/stream/287929-mathlib4/topic/github.20permission), and push your branch to that repo.
  This will enable Mathlib's `.olean` cache to include your pull request.

## Tags and branches

### `leanprover/lean4`

* Development occurs on the `master` branch.
* Stable releases and release candidates have tags, e.g. `v4.2.0` or `v4.3.0-rc1`.
  * To use one of these releases in a project, your `lean-toolchain` file should contain e.g. `leanprover/lean4:v4.2.0`.
* Stable releases arrive at the end of each month, and are identical to the last release candidate.
* The first release candidate of the next version is released immediately after the stable release.
* Each version has a `releases/v4.X.0` feature branch, which may contain
  * additional commits for release notes
  * cherry picked commits from `master` for critical fixes released via release candidates.
* We make a regular nightly release from `master`, which has a tag e.g. `nightly-2023-11-01` on the
  `leanprover/lean4-nightly` repository.
  * To use a nightly release in a project, your `lean-toolchain` file should contain e.g. `leanprover/lean4:nightly-2023-11-01`. (Note that it should not be `leanprover/lean4-nightly:nightly-2023-11-01`, because `elan` applies some magic wisdom here.)
* There is a `nightly` branch on `leanprover/lean4` which follows the most recent commit which was
  used to construct a nightly release.
* Every PR automatically receives a toolchain after it builds successfully. The PR will then have label `toolchain-available`.
  To use PR #NNNN in a project, your `lean-toolchain` file should contain
  `leanprover/lean4-pr-releases:pr-release-NNNN`.
* For any PR that potentially affects Std or Mathlib, you should base your PR off the HEAD of the `nightly-with-mathlib` branch.
  In that case, a `lean-pr-testing-NNNN` Mathlib branch is created, described in detail below, and results from this branch are
  reported via comments in the PR discussion.

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
  * uses a recent nightly release (this is updated automatically)
  * has all commits from `main` merged into it automatically
  * may have any changes from `bump/v4.X.0` merged into it manually
  * may have any other commits, including unreviewed ones, required to keep the `nightly-testing`
    branch working against recent nightly releases.
* Failures in CI on the `nightly-testing` are reported by a bot to zulip in the private
  "Mathlib reviewers" channel.
* Success in CI on the `nightly-testing` branch results in the creation of a tag
  `nightly-testing-YYYY-MM-DD` to match that commit, if this tag does not already exist.
  * Thus if `nightly-testing-YYYY-MM-DD` exists, we know that on it:
    * the `lean-toolchain` is `leanprover/lean4:nightly-YYYY-MM-DD`, and
    * CI succeeds.
* When changes are required to Std to adapt to a breaking change in Lean,
  you will need to make a branch, and later open a PR from that branch.
  (Note that the steps below happen automatically at Mathlib,
  but need to be done manually for Std.)
  * If the change was made in `leanprover/lean4#NNNN`,
    then the Std adaptation branch should be called `lean-pr-testing-NNNN`.
  * The Std adaptation branch should be based off the tag `nightly-testing-YYYY-MM-DD`
    where `YYYY-MM-DD` is the date of the nightly release that your Lean PR is based off.
  * If the `nightly-testing-YYYY-MM-DD` tag does not yet exist, you will need to wait
    (and possibly move forward to a subsequent nightly).
    Contact @semorrison for assistance if needed.
  * Ideally you will push the `lean-pr-testing-NNNN` branch to the main Std repository;
    we can provide write access if needed.
  * The `lean-toolchain` on this branch must contain `leanprover/lean4-pr-releases:pr-release-NNNN`.
  * You may open a PR from the `lean-pr-testing-NNNN` branch, either before or after
    making the required adaptations.
  * When opening the PR, remember to set the base branch to `nightly-testing`.
  * Please label the PR with the `v4.X.0` and 'depends on core changes' labels.
    (Or ask for this to be done if you don't have write access.)
  * Once the Lean PR has been merged and published in a nightly release, the Std adaptation PR
    * should have its `lean-toolchain` updated to `leanprover/lean4:nightly-YYYY-MM-DD`
    * its changes may be merged manually into `nightly-testing` as needed to keep `nightly-testing`
      working (do not change the base and merge the PR, we still need it).
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
* The `nightly-testing-*` tags and `bump/v4*` branches are write protected,
  so may only be modified via PRs, maintainers, or the relevant bots.
* Note that the `nightly-testing` branch of Mathlib may use the `nightly-testing` branch of Std as required.
* Similarly a `bump/v4.X.0` branch of Mathlib may use the `bump/v4.X.0` branch of Std as required.
* Branches `lean-pr-testing-NNNN` are automatically created for any Lean PR that passes CI,
  and is based off a nightly release. (Unlike for Std, where they must be created manually.)
* Mathlib adaptation PRs on `lean-pr-testing-NNNN` branches may need to change the Std dependency
  to use a `lean-pr-testing-NNNN` branch of Std, if Std also experiences breakages.

### Mathlib nightly and bump branches

Every month there is a new Lean release,
and Mathlib aims to migrate to the new Lean release as soon as possible.
To make this process as smooth as possible, we follow the following procedure:

* The `nightly-testing` branch of Mathlib uses the nightly toolchain releases of Lean.
  In other words, the `lean-toolchain` file on that branch contains something like `leanprover/lean4:nightly-2024-09-26`.
  - This branch is not guaranteed to build without errors.
  - Change to this branch are not reviewed by the Mathlib maintainer team.
  - This branch is not protected: anybody can push fixes to it.
  - The purpose of this branch is to adapt Mathlib to changes in the nightly toolchain releases of Lean.
  - Typically, a PR `#NNNN` to Lean core will be accompanied by adaptations to Mathlib in a branch `lean-pr-testing-NNNN`.
    Once the Lean core PR lands in a nightly toolchain, the Mathlib branch `lean-pr-testing-NNNN` can be merged into `nightly-testing`.
    Often one needs to fix merge conflicts in `lean-toolchain`, `lakefile.lean`, and/or `lake-manifest.json`.
  - If CI fails on this branch, then it posts a message to ["nightly-testing > Mathlib status updates"](https://leanprover.zulipchat.com/#narrow/stream/428973-nightly-testing/topic/Mathlib.20status.20updates) on Zulip, indicating the failure.
  - If CI passes on this branch, then a message is posted to the same thread, indicating success, and giving instructions to create a PR to review the adaptations. (See below.)
* The `bump/v4.X.Y` branches of Mathlib also use nightly toolchain releases of Lean.
  - This branch should always build without errors.
  - Changes to this branch are reviewed by the Mathlib maintainer team.
  - This branch is protected: only Mathlib maintainers and certain bots can push to it.
  - The purpose of this branch is to prepare a parallel version of Mathlib's `master` branch that builds on the upcoming version of Lean.
    Once that version is released, the `bump/v4.X.Y` branch is merged into `master`.
    This merge is essentially atomic, since the diff has already been reviewed via all the daily adaptation PRs. (See below.)
* When `nightly-testing` passes CI, a bot posts to Zulip with instructions to create an "adaptation PR" to merge changes on `nightly-testing` into `bump/v4.X.Y`.
  - This PR can be prepared using `scripts/create-adaptation-pr.sh` as indicated in the Zulip message.
  - This PR should be reviewed by the Mathlib maintainer team.
* Over the course of the Lean release cycle (i.e., a month), `bump/v4.X.Y` accumulates adaptations to the future Lean release.
  - But `master` also accumulates thousands of lines of changes.
  - Hence `master` should be merged into `bump/v4.X.Y` on a regular basis.
  - At the time of writing, this step is combined into the `scripts/create-adaptation-pr.sh` process.
  - Occasionally, merge conflicts occur. These ought to be reviewed by the Mathlib maintainer team, although that currently does not happen.

### Combined CI between Lean and Mathlib

* For every PR to Lean, we attempt to run Mathlib CI against the resulting toolchain.
* For this to work, you will need to rebase your PR onto the `nightly-with-mathlib` branch.
  The `nightly-with-mathlib` branch points to the latest nightly lean release which passes mathlib CI,
  and for which a `nightly-testing-YYYY-MM-DD` tag exists on Mathlib (and possibly Std).
* The bot will create a `lean-pr-testing-NNNN` branch at Mathlib from the `nightly-testing-YYYY-MM-DD` tag,
  or push an empty commit to it if it already exists.
* Subsequent CI results from that Mathlib branch will be reported back to the Lean PR
  in the form of comments.
* If your PR does not branch off a nightly release for which Mathlib builds, a bot will comment on your
  PR.
  It will try again whenever you push to your PR.
* If `nightly-with-mathlib` is too old for your purposes, you can base off `nightly`, and mathlib CI
  will commence as soon as that nightly release itself passes the Mathlib CI and you push to the PR.
* It may be the case that that nightly release never passes the Mathlib CI. In that case you may have
  to wait for `nightly-with-mathlib` to be updated and rebase onto that.


<img src="img/tags_and_branches.png" alt="Overview of branches at Mathlib/Std" width="80%"/>
