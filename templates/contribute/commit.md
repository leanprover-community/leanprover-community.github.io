# Pull request title and description conventions

We are using the following convention for writing pull request titles and descriptions.

## Format

Note: "Title:" and "Description:" do not actually appear

```markdown
  Title:
  <type>(<optional-scope>): <subject>

  Description:
  <body>
  <NEWLINE>
  <footer>
  <NEWLINE>
  <dependencies>
```

`<type>` is:

 - feat (feature)
 - fix (bug fix)
 - doc (documentation)
 - style (formatting, missing semicolons, ...)
 - refactor
 - test (when adding missing tests)
 - chore (maintain)
 - perf (performance improvement, optimization, ...)

`<optional-scope>` is a name of module or a directory which contains changed modules.
This is not necessary to include, but may be useful if the `<subject>` is insufficient.
The `Mathlib` directory prefix is always omitted.
For instance, it could be

- Data/Nat/Basic
- Algebra/Group/Defs
- Topology/Constructions

`<subject>` has the following constraints:

- use imperative, present tense: "change" not "changed" nor "changes"
- do not capitalize the first letter
- no dot(.) at the end

`<body>` has the following constraints:

- just as in ``<subject>``, use imperative, present tense
- include motivation for the change and contrast with previous
  behavior

`<footer>` is optional and may contain two items:

- Breaking changes: All breaking changes have to be mentioned in
  footer with the description of the change, justification and
  migration notes
- Referencing issues: Closed bugs should be listed on a separate line
  in the footer prefixed with "Closes" keyword like this: Closes #123, #456

`<dependencies>` if this PR depends on others, they should be listed 
in checkbox format, i.e., `- [ ] depends on: #XXXX`

## Examples

An example where `<scope>` is not necessary might be:

```markdown
feat: have library search use the whole range for replacement

previously `apply? using h` would replace to `refine blah using h` rather than `refine blah`.

This also changes the diagnostic message to be on the whole syntax `apply? using h` rather than just the `apply?` bit, which seems fine to me.
```

And an example where including `<scope>` does add value:

```markdown
docs(CategoryTheory/EssentialImage): typo and punctuation

Fix a typo, add two periods.
```

An example with dependent PRs:

```markdown
feat: The norm on `Unitization` is a C⋆-norm

This shows that C⋆-algebras are always `RegularNormedAlgebra`s, so that their `Unitization` is equipped with a norm. Moreover, we show this norm is a C⋆-norm.

---

- [ ] depends on: #5330
- [ ] depends on: #5741
- [ ] depends on: #5742
- [ ] depends on: #5743
```