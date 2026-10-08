# The Lean Github ecosystem

Documentation of the branches, tags, and CI workflows relevant for making pull requests to Lean, Batteries, and
Mathlib.

* [Things you need to know](#things-you-need-to-know) is relevant for everyone
* [Tags and branches](#tags-and-branches) is for "experts only" who are making or fixing
  breaking changes in Lean, or who want to understand the inner workings of Mathlib CI.

## Things you need to know

* If you are making a pull request to `leanprover/lean4` which may involve breaking changes,
  please rebase your PR onto `downstream-green` and label it `downstream`.
  This will create an adaptation PR in `leanprover/downstream-lean4`.

* If you are making a pull request to `leanprover-community/mathlib4`,
  please make it from a fork. Mathlib's `.olean` cache now works with PRs from forks.

## Tags and branches

### `leanprover/lean4`

* Development occurs on the `master` branch.
* Stable releases and release candidates have tags, e.g. `v4.2.0` or `v4.3.0-rc1`.
  * To use one of these releases in a project, your `lean-toolchain` file should contain e.g. `leanprover/lean4:v4.2.0`.
* Stable releases usually arrive near the middle of the month, and are often identical to the last release candidate.
* The first release candidate of the next version is released immediately after the stable release.
* Each version has a `releases/v4.X.0` feature branch, which may contain cherry-picked or backported commits from `master`.
  Release candidates are cut from this branch.
* We cut a regular nightly release from `master`, which has a tag like `nightly-2023-11-01` on the `leanprover/lean4-nightly` repository.
  * To use a nightly release in a project, your `lean-toolchain` file should contain e.g. `leanprover/lean4:nightly-2023-11-01`.
    (Note that it should not be `leanprover/lean4-nightly:nightly-2023-11-01`, because `elan` applies some magic wisdom here.)
  * A nightly may be *revised* by manually triggering the release workflow. Revised nightlies
    have tags of the form `nightly-YYYY-MM-DD-revK` (with K starting at 1) on `leanprover/lean4-nightly`.
    To use a revised nightly in a project, your `lean-toolchain` file should contain e.g.
    `leanprover/lean4:nightly-2023-11-01-rev1`.
    Revised nightlies are ordered after the base nightly: base < rev1 < rev2 < next day's nightly.
    The Mathlib nightly testing infrastructure handles revised nightlies automatically.
* There is a `nightly` branch on `leanprover/lean4`
  which follows the most recent commit which was used to construct a nightly release.
* Every PR automatically receives a toolchain after it builds successfully.
  The PR will then have label `toolchain-available`.
  To use PR #NNNN in a project, your `lean-toolchain` file should contain `leanprover/lean4-pr-releases:pr-release-NNNN`.
* For any PR that potentially breaks packages like Batteries or Mathlib, use a `downstream-lean4` adaptation PR.
  * Base your PR off of the `downstream-green` branch and label it `downstream`.
    This creates an adaptation PR for your PR in `leanprover/downstream-lean4`
    where you can check for and fix breakages before your PR is merged.
  * If you have write access to `leanprover/downstream-lean4` but have insufficient permissions to edit labels in your original PR,
    you can comment `downstream` on your original PR instead and CI will add the label.
  * If you don't have write access to `leanprover/downstream-lean4`, you can request access on zulip in the
    [`ecosystem infrastructure` channel](https://leanprover.zulipchat.com/#narrow/channel/536994-ecosystem-infrastructure).

### `leanprover-community/batteries` (aka 'Batteries')

* Development occurs on `main`.
* Batteries uses the latest stable release or release candidate in its `lean-toolchain`.
  * Because we release `v4.X+1.0-rc1` immediately after releasing `v4.X.0`,
    Batteries is only very briefly on stable releases.
* The first commit on `main` which uses a new toolchain is tagged with the version number of that
  toolchain (e.g. `v4.2.0`).
* There is a branch `stable` which follows the `v4.X.Y` tags.
* Batteries has a branch `bump/v4.X.0` for the upcoming stable release of Lean,
  * which contains adaptations for breaking changes that have been approved by the maintainers
  * and which will be using a `leanprover-lean4:nightly-YYYY-MM-DD` toolchain.
* Batteries has a branch `nightly-testing` which
  * uses a recent nightly release (this is updated automatically)
  * has all commits from `main` merged into it automatically
  * may have any changes from `bump/v4.X.0` merged into it manually
  * may have any other commits, including unreviewed ones, required to keep the `nightly-testing`
    branch working against recent nightly releases.
* Failures in CI on the `nightly-testing` branch are reported by a bot to zulip [in the `nightly-testing-batteries` channel](https://leanprover.zulipchat.com/#narrow/channel/595626-nightly-testing-batteries/topic/Batteries.20status.20updates/with/592700605).
* Success in CI on the `nightly-testing` branch results in the creation of a tag
  `nightly-testing-YYYY-MM-DD` to match that commit, if this tag does not already exist.
  * Thus if `nightly-testing-YYYY-MM-DD` exists, we know that on it:
    * the `lean-toolchain` is `leanprover/lean4:nightly-YYYY-MM-DD`, and
    * CI succeeds.
* It is always allowed to merge `bump/v4.X.0` into `nightly-testing`, but not conversely.
  (Changes to `bump/v4.X.0` have been reviewed, but changes to `nightly-testing` may not have been.)
* When it is time to update Batteries to a new Lean rc1,
  *hopefully* all that is required is to make a new PR
  consisting of squash merging `bump/v4.X.0` to `main`.

### `leanprover-community/mathlib4` (aka 'Mathlib')

* Everything said above about Batteries applies to Mathlib, except:
  * Development occurs on `master`.
  * `nightly-testing` status updates are posted in [this thread](https://leanprover.zulipchat.com/#narrow/channel/595625-nightly-testing-mathlib/topic/Mathlib.20status.20updates/with/592729346) in `#nightly-testing-mathlib`.
  * PRs to Mathlib should be made from forks. Mathlib's `.olean` cache now works with PRs from forks.
* The `nightly-testing`, `nightly-testing-*` tags, and `bump/v4*` branches
  all live at `leanprover-community/mathlib4-nightly-testing`, which is a fork of mathlib4.
  If you will regularly need write access to these branches, you can ask in the
  [`nightly-testing-mathlib` channel](https://leanprover.zulipchat.com/#narrow/channel/595625-nightly-testing-mathlib)
  on Zulip to be added to the `nightly-testing` GitHub team.
* Note that the `nightly-testing` branch of Mathlib may use the `nightly-testing` branch of Batteries as required.
* Similarly a `bump/v4.X.0` branch of Mathlib may use the `bump/v4.X.0` branch of Batteries as required.

### Mathlib nightly and bump branches

Every month there is a new Lean release,
and Mathlib aims to migrate to the new Lean release as soon as possible.
To make this process as smooth as possible, we follow the following procedure:

* The `nightly-testing` branch lives at `leanprover-community/mathlib4-nightly-testing` and uses nightly toolchain releases of Lean.
  In other words, the `lean-toolchain` file on that branch contains something like `leanprover/lean4:nightly-2024-09-26`.
  - This branch is not guaranteed to build without errors.
  - Changes to this branch are not reviewed by the Mathlib maintainer team.
  - This branch is not protected: members of the `nightly-testing` GitHub team can push fixes to it.
  - The purpose of this branch is to adapt Mathlib to changes in the nightly toolchain releases of Lean.
  - Adaptations made in `leanprover/downstream-lean4` will automatically be pushed here.
  - If CI fails on this branch, then it posts a message to ["nightly-testing-mathlib > Mathlib status updates"](https://leanprover.zulipchat.com/#narrow/channel/595625-nightly-testing-mathlib/topic/Mathlib.20status.20updates) on Zulip, indicating the failure.
  - If CI passes on this branch, then a message is posted to the same thread, indicating success, and giving instructions to create a PR to review the adaptations. (See below.)
* The `nightly-testing-green` branch in `leanprover-community/mathlib4-nightly-testing` tracks the last commit of `nightly-testing` which built successfully.
  Tooling for builds of `nightly-testing` is fetched from this branch.
* The `bump/v4.X.Y` branches also live at `leanprover-community/mathlib4-nightly-testing` and use nightly toolchain releases of Lean.
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

The following image is slightly outdated as it still contains references to the now obsolete `lean-pr-testing-NNNN` branches.
Their role has been replaced by the `leanprover/downstream-lean4` repository,
which automatically pushes adaptations developed inside itself to the `nightly-testing` branch as plain commits
(similar to any other contributor).
<img src="img/tags_and_branches.png" alt="Overview of branches at Mathlib/Batteries" width="80%"/>
