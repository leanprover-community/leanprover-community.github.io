# CI for Lean projects on GitHub

The Lean community offers a number of [GitHub Actions](https://docs.github.com/en/actions) scripts
to help maintain Lean projects.
If you include these scripts in your repository,
they will help to keep your project up-to-date
and warn you when it fails to build.

You can copy the text below into corresponding files
in the `/.github/workflows` directory of your project.
For more advanced options,
see the README files for each action.


## Build project and update `lean-x.y.z` branches

This script will try to build every push made
to every branch of your repository.
When commits are pushed to the `master` branch,
it will mirror them to the corresponding `lean-x.y.z` branch,
where `x.y.z` is determined by the Lean version
in `leanpkg.toml`.

You can use the build and update actions separately,
but we recommend combining them as in the script below.

* [lean-build-action](https://github.com/leanprover-contrib/lean-build-action)
* [update-versions-action](https://github.com/leanprover-contrib/update-versions-action)

`/.github/workflows/lean_build.yml`
```yaml
on:
  push:

jobs:
  update_lean_xyz_branch_and_build:
    runs-on: ubuntu-latest
    name: Update lean-x.y.z branch and build project
    steps:

    - name: checkout project
      uses: actions/checkout@v2
      with:
        fetch-depth: 0

    - name: update branch
      if: github.ref == 'refs/heads/master'
      uses: leanprover-contrib/update-versions-action@master

    - name: build project
      uses: leanprover-contrib/lean-build-action@master
```


## Upgrade Lean and mathlib versions on schedule

This script will try once a day to update the versions
of Lean, mathlib, and any other projects that yours depends on.
If it succeeds, it will push the new `leanpkg.toml`
to your `master` branch.
If it fails, it will open an issue on your project.
(Don't worry, it won't spam you with repeated failures.)

You can change the schedule and frequency of the upgrade
by modifying the [cron schedule expression](https://crontab.guru/).

* [lean-upgrade-action](https://github.com/leanprover-contrib/lean-upgrade-action)

`/.github/workflows/upgrade_lean.yml`
```yaml
on:
  schedule:
    - cron: '0 2 * * *' # once a day at 2am UTC

jobs:
  upgrade_lean:
    runs-on: ubuntu-latest
    name: Bump Lean and dependency versions
    steps:
      - name: checkout project
        uses: actions/checkout@v2
      - name: upgrade Lean and dependencies
        uses: leanprover-contrib/lean-upgrade-action@master
        with:
          repo: ${{ github.repository }}
          access-token: ${{ secrets.GITHUB_TOKEN }}
      - name: update version branches
        uses: leanprover-contrib/update-versions-action@master
```
