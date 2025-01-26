# Tips and suggestions for teaching with Lean 

In order to help people interested in teaching with Lean,
we've collected some strategies and approaches here 
that have worked well for people in the community. 
Depending on the context of your course, these approaches may or may not make sense.

## Planning your course

If you are thinking about introducing Lean into a course,
or designing a course around Lean,
there are some important questions you should ask yourself.
Your answers to these questions can help find comparable courses that people have already taught,
and can help you choose materials to use.

* Do you want to teach Lean, or do you want to teach *using* Lean?
  In other words, what are the learning objectives of your course?
  Some courses try to teach math or CS topics with Lean as an "implementation language,"
  without expecting that students develop strong Lean skills.
  Others explicitly teach verification and formal proof.

* How much Lean will your course actually use? 
  Especially in courses that try to teach *using* Lean, the amount of formalization
  can be minimal, e.g. optional exercises for extra credit or only instructor-produced demos.

* What technological prerequisites will you assume from your students?
  Should they have a GitHub account and understand `git`? 
  Have they programmed in a functional language, or in any language?
  Can they be expected to install Lean locally on their own computer?

* Some courses start with an introduction to the type theory of Lean,
  perhaps contrasting it with the set theory that mathematicians are used to.
  Other courses assume that students will pick up the analogy on their own -- 
  if they're familiar with set theory at all -- 
  and don't focus on the differences.
  Both approaches are reasonable, but it's a good idea to pick one early,
  and stick to it in your teaching materials.

* The syntax of Lean, and variety of options, can be overwhelming to students.
  It's important to choose a "dialect" for your course, that may grow as the course progresses.
  Limiting which tactics you introduce, avoiding library lemmas, 
  and teaching tactic or term mode (but not both) 
  are all ways in which people restrict the amount of language detail that students need to absorb at once.


## Organizing course projects

It is common to use a "course project" to distribute lecture notes, examples, assignments, etc. 
while ensuring that students all remain on a fixed version of Lean and mathlib.
Here are examples from [a course at Fordham](https://github.com/hrmacbeth/math2001/)
and [a course at Brown](https://github.com/BrownCS1951x/fpv2023).
The former includes detailed notes that get compiled to HTML; 
the latter relies on an external textbook reference.

Without some kind of structure like this -- for example, if students receive bare .lean files -- 
it is hard to ensure that they all use the same version of Lean.
It is also a good way to provide a "library" file or files 
containing basic definitions, tactics, and such that are useful for your course.

These projects are often hosted on GitHub. 
Students are asked to clone the project, or create a Codespace or Gitpod instance, 
at the start of the course.
They are instructed to pull updates periodically, for instance, when new homeworks are released.
If students are not expected to be proficient with `git`, you can provide 
[helper scripts](https://github.com/brown-cs22/CS22-Lean-2023/tree/main/scripts)
that attempt to do this management automatically.

Some instructors recommend that students copy homework files before beginning an assignment,
working on the copied version, 
to avoid merge conflicts if the assignment should change.

Other instructors have used GitHub Classrooms for assignment releases.
In this setup, each assignment must be its own standalone Lean project.

## Lean-in-the-cloud setups 

Our [resources page](resources.html#lean-in-the-cloud-setups) has pointers to setting up GitHub Codespaces and Gitpod
for use with a course project.
Especially for large courses aimed at students who might struggle to install Lean locally,
the use of cloud resources to run Lean can greatly simplify the beginning of a course.

In both approaches, students will be able to use VSCode in a browser
to edit Lean files with a Lean server running remotely.
With Codespaces, a convenient [VSCode plugin](https://marketplace.visualstudio.com/items?itemName=GitHub.codespaces)
makes it possible to work from a local VSCode installation too.
The obvious upsides are that there is a uniform environment for all students,
without installation headaches,
and that no student is using an underpowered machine.
Downsides include that student files are saved on the cloud, and students might struggle to 
download and submit them; 
these cloud services limit the number of free hours per student per month;
and internet access is required to work on the course.

Some instructors have successfully run large courses using these resources,
and many offer them as an option to students.
For GitHub Codespaces, it is important to remind students to sign up for 
GitHub's [student benefits](https://education.github.com/pack) 
to take advantage of extra Codespaces hours.

To save students time when creating new codespaces, GitHub has a "prebuild" option.
In your course repository, go to Settings -> Codespaces. 
You likely want to prebuild on every push and store 1 version.
There is a nominal cost to storing these images: 
currently (Jan. 2025) the image for a course with a full mathlib build will cost about US $0.40 per month. 

## Renaming and redefining tactics 

The Lean/mathlib names for tactics may not match how you present these topics in class.
In Lean 4 it is easy to create [aliases for certain tactic calls](https://github.com/brown-cs22/CS22-Lean-2023/blob/0a0a8e168559462a39e33a7b2940b11bd5a59e90/BrownCs22/Library/Tactics.lean#L59)
or [change the behavior of existing tactics](https://github.com/brown-cs22/CS22-Lean-2023/blob/0a0a8e168559462a39e33a7b2940b11bd5a59e90/BrownCs22/Library/Tactics.lean#L61)
within a course project.
(In the linked examples, in any course file importing `Tactics.lean`, the behavior of `linarith` will be redefined.)

## Ending proofs with `done`

It can sometimes be confusing to tell when a tactic proof is complete,
since the error message appears at the top of the proof but not at the bottom.
Some instructors have had success teaching students to begin writing a proof 
with the tactic `done` at the end.

```lean
example (x : ℕ) : x = x := by 
  -- fill in your proof here
  done
```

An alternative is to use curly braces after `by`:
```lean
example (x : ℕ) : x = x := by {
  -- fill in your proof here
}
```

