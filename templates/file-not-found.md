    <div class="alert alert-info">
      <p>
      We are currently updating the Lean community website to describe working with Lean 4,
      but most of the information you will find here today still describes Lean 3.
      </p>
      <p>
      Pull requests updating this page for Lean 4 are very welcome.
      There is a link at the bottom of this page.
      </p>
      <p>
      Please visit <a href="https://leanprover.zulipchat.com">the leanprover zulip</a>
      and ask for whatever help you need during this transitional period!
      </p>
      <p>
      The website for Lean 3 has been <a href="https://leanprover-community.github.io/lean3/">archived</a>.
      If you need to link to Lean 3 specific resources please link there.
      </p>
    </div>

# File not found

Are you setting up your first Lean project, and seeing this error message? The problem might be:
- Did you open a bare file in VS Code? Try opening the root folder
  of your Lean package instead. See ["Creating a Lean project"](install/project.html).
- Is the Lean package configured correctly? Does a `leanpkg.path` file exist
  in the directory and contain valid locations? If not, try running
  `leanproject get-mathlib-cache` if your project depends on mathlib, or
  `leanpkg configure` otherwise.
