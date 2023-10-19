# Teaching resources

We've collected different kinds of resources that might be helpful for running courses using Lean.

## Notes and Textbooks 

There are various [learning resources](../learn.html) collected on this website. 
Here we list texts that are explicitly designed for university courses. 

* [The Mechanics of Proof](https://hrmacbeth.github.io/math2001/index.html) by Heather Macbeth 
  is a set of lecture notes dealing with how to write careful, rigorous mathematical proofs,
  paired with material in Lean.
* [How To Prove It With Lean](https://djvelleman.github.io/HTPIwL/) by Daniel Velleman is a supplement to 
  the book *How To Prove It*.
* [The Hitchhiker's Guide to Logical Verification](https://lean-forward.github.io/hitchhikers-guide/2023/)
  by Jasmin Blanchette
  is a textbook that introduces the reader to interactive theorem proving using the Lean 4 proof assistant as its vehicle. The textbook is accompanied by Lean demonstration and exercise files.

## Games 

* [The Natural Number Game](https://adam.math.hhu.de/#/g/hhu-adam/NNG4) by Kevin Buzzard, Jon Eugster, and Mohammad Pedramfar is a popular introduction to Lean.
* The [engine behind the NNG](https://github.com/leanprover-community/lean4game)
  can be used to design custom games for courses.

## Autograders

* [A Gradescope autograder](https://github.com/robertylewis/lean4-autograder-main) for Lean 4
* [A GitHub Classrooms autograder](https://github.com/adamtopaz/hw_template) for Lean 4

## Lean-in-the-cloud setups

* Inserting the 
  [mathlib4 `.devcontainer` directory](https://github.com/leanprover-community/mathlib4/tree/master/.devcontainer) 
  into your course project will enable GitHub Codespaces for your project. 
  Encourage students to sign up for a (free) pro account through GitHub's education benefits 
  in order to get more Codespaces hours.
* Similarly, inserting the mathlib4 [`.gitpod.yml`](https://github.com/leanprover-community/mathlib4/blob/master/.gitpod.yml) and [`.docker/gitpod/Dockerfile`](https://github.com/leanprover-community/mathlib4/blob/master/.docker/gitpod/Dockerfile) will enable Gitpod usage.