# Lean Tips and Tricks

This document contains some tips for intermediate and advanced users of Lean
It is currently focussed around Lean 3.

Yury's list from https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Tips.20and.20tricks/near/265408881:
use --old if you're going to edit low-level files (should we make it default?);
temporarily hide a part of a long proof behind sorry; to speed-up recompilation (saw recently somewhere on Zulip);
if refine times out, try convert instead and see which terms Lean fails to unify;
use library_search etc;
what else?

### Commenting out large proofs using `sorry`

Sometimes commenting out large chunks of a proof is helpful, this can be done using the default comment characters `--` or `/- multi-line comment-/`, but oftentimes a more convenient way is to comment out a long subproof of a focussed goal surrounded by braces by prepending `sorry;`
```
sorry; { rw blah,
  HUGE PROOF }
```
as only one line needs to be changed this is quite a minimal edit, and doesn't . It also has the advantage that it is extremely easy to remove all instances of `sorry;` from a file when finished using find and replace.

### Memory and deterministic timeout



### Old mode
If you change a file early on in the import hierarchy in a large project is changed and then attempt to work on a file that depends on it much later, then Lean will try to check all files in between to ensure they didn't break.
This behaviour can cause the Lean server to become unresponsive, or simply slow down development when.
You can also call lean with the "--old" flag to help in these situations, though it does come with some caveats.
In VSCode you can enable it by opening the VSCode settings and searching for "Lean: extra options" then add the flag "--old".
This causes lean not to recompile oleans for unedited files and just assume everything worked, so in this situation it is helpful to avoid recompilation, but you do then run the risk that your change broke /changed the meaning of some file in-between. Thus it most applicable when you are adding a new lemma/def early in the hierarchy that you are sure won't break things in between, rather than changing existing defs.
It is possible to "prove false" running lean with the old flag on, by changing a definition in an early file later results about that definition may become incorrect if Lean is asked not to rebuild those files.
The old flag should therefore not be used when consistency of the whole project is important (e.g. in CI), though it can speed up development.

### The `#exit` command and `.`

The command `#exit` will cause lean to stop reading the file at the location it is inserted.
This can be helpful when working on proofs in the middle of a file with many results or slow results below the current location.
This is related to switching to `check visible lines` mode, but gives the user more precise control over which parts of the file are slow.

### Profiling proofs

Sometimes long proofs are slow to execute and isolating the slow tactic or subgoals in an attempt to refactor or speed them up is necessary.
The basic option to enable this is `set_option profiler true`, which will print out timing information for tactic execution.

