---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/20539squeezesimp.html
---

## Stream: [general](index.html)
### Topic: [squeeze_simp](20539squeezesimp.html)

---

#### [Johan Commelin (Oct 08 2018 at 15:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/squeeze_simp/near/135401004):
@**Simon Hudon** To what extend do you think `sed` and `lean` could cooperate to automatically turn every `simp` into a `squeeze_simp`, and then every `squeeze_simp` into a `simp only`? Can we automate Kenny?

#### [Simon Hudon (Oct 08 2018 at 16:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/squeeze_simp/near/135406348):
But we like Kenny!

#### [Simon Hudon (Oct 08 2018 at 16:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/squeeze_simp/near/135406424):
I was thinking along those lines but I was thinking of adding a feature to the emacs Lean mode. I'm not how I would do it for VS code though. Do you know how to script it?

#### [Johan Commelin (Oct 08 2018 at 16:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/squeeze_simp/near/135406432):
I don't know anything about VScode

#### [Johan Commelin (Oct 08 2018 at 16:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/squeeze_simp/near/135406440):
But couldn't this just be a CLI-only thing?

#### [Johan Commelin (Oct 08 2018 at 16:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/squeeze_simp/near/135406455):
For other purposes the output of `squeeze_simp` is already very useful.

#### [Patrick Massot (Oct 08 2018 at 16:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/squeeze_simp/near/135406473):
Can't we use a hole command here again?

#### [Mario Carneiro (Oct 08 2018 at 16:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/squeeze_simp/near/135406490):
you still have to click on a hole command

#### [Johan Commelin (Oct 08 2018 at 16:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/squeeze_simp/near/135406493):
Exactly

#### [Mario Carneiro (Oct 08 2018 at 16:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/squeeze_simp/near/135406537):
indeed, you have to manually edit the file to put a hole in in the first place

#### [Johan Commelin (Oct 08 2018 at 16:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/squeeze_simp/near/135406538):
I want `sed` to "click" on the hole command.

#### [Patrick Massot (Oct 08 2018 at 16:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/squeeze_simp/near/135406554):
Oh you mean you want this for batch processing?

#### [Simon Hudon (Oct 08 2018 at 16:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/squeeze_simp/near/135406562):
The difficult thing about using something like sed is detecting the end of the input `squeeze_simp`

#### [Simon Hudon (Oct 08 2018 at 16:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/squeeze_simp/near/135406574):
But I guess we could output it in Lean

#### [Simon Hudon (Oct 08 2018 at 16:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/squeeze_simp/near/135406591):
@**Patrick Massot** exactly

#### [Patrick Massot (Oct 08 2018 at 16:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/squeeze_simp/near/135406602):
Sorry I read too quickly the beginning of this thread (I'm fighting dependent rw)

#### [Simon Hudon (Oct 08 2018 at 16:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/squeeze_simp/near/135407907):
@**Mario Carneiro** has shown us how useful awk can be in these situations. Do you think if we output the beginning line and column number of the input, the ending line and column number of the input and the replacement, we can get awk to go in there and do the replacement? You'd probably also have to go from the last to the first if you want to do it in one go so that the line numbers don't get invalidated.

#### [Johan Commelin (Oct 08 2018 at 16:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/squeeze_simp/near/135408204):
Sure, that should definitely be possible

#### [Johan Commelin (Oct 08 2018 at 16:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/squeeze_simp/near/135408213):
I guess `squeeze_simp` can get access to its location in the file via some tactic_state magic, right?

#### [Johan Commelin (Oct 08 2018 at 16:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/squeeze_simp/near/135408290):
Or you make `squeeze_simp` output a patch (-;

#### [Johan Commelin (Oct 08 2018 at 16:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/squeeze_simp/near/135408296):
Then we can just commit it, and git takes care of the rest :lol:

#### [Simon Hudon (Oct 08 2018 at 18:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/squeeze_simp/near/135413309):
I just looked into the patch file format. It seems like more work to format than to just do it ourselves

#### [Johan Commelin (Oct 08 2018 at 18:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/squeeze_simp/near/135414054):
Ok, so how about your suggestion, with line+col numbers

#### [Simon Hudon (Oct 08 2018 at 18:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/squeeze_simp/near/135415134):
I think the best bet is to use `awk` but I'll have to learn it

#### [Simon Hudon (Oct 08 2018 at 18:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/squeeze_simp/near/135415187):
Right now I'm experimenting with emacs to see if I can get a nice first approximation

#### [Johan Commelin (Oct 08 2018 at 18:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/squeeze_simp/near/135415446):
`awk` is not hard. Also, I wouldn't mind helping you.

#### [Johan Commelin (Oct 08 2018 at 18:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/squeeze_simp/near/135415506):
We could use `sed` to squeeze_simpify a `.lean` file. After that, we run `lean --make` on the file, and capture the stdout.

#### [Johan Commelin (Oct 08 2018 at 18:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/squeeze_simp/near/135415521):
If `squeeze_simp` can produce output of the form `line:column:replacement_text` I think we can take it from there.

#### [Simon Hudon (Oct 08 2018 at 18:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/squeeze_simp/near/135415693):
I was thinking of a format like this:

```lean
84:23: 
86:0:
--- BEGIN ---
simp only [perm_cons, multiset.cons_coe, iff_self, multiset.coe_eq_coe, multiset.quot_mk_to_coe'']
--- END ---
```

#### [Johan Commelin (Oct 08 2018 at 18:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/squeeze_simp/near/135415718):
unix prefers to keep everything on 1 line.

#### [Simon Hudon (Oct 08 2018 at 18:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/squeeze_simp/near/135415785):
In that case, how about `line0:col0:line1:col1:replacement_text`?

#### [Johan Commelin (Oct 08 2018 at 18:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/squeeze_simp/near/135415873):
Looks good

#### [Johan Commelin (Oct 08 2018 at 18:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/squeeze_simp/near/135415884):
Unless we want to anticipate multiline replacement texts

#### [Simon Hudon (Oct 08 2018 at 18:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/squeeze_simp/near/135415997):
That's what I'm looking at now. The replacement is sometimes multiline but there's no real reason to be. I'll restrict it to one line and let the user reformat if needed

#### [Johan Commelin (Oct 08 2018 at 18:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/squeeze_simp/near/135416006):
There is no "user" if we run this in batch mode over 25 files.

#### [Johan Commelin (Oct 08 2018 at 19:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/squeeze_simp/near/135416069):
But we can write a smart awk script

#### [Johan Commelin (Oct 08 2018 at 19:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/squeeze_simp/near/135416073):
It can try to reformat that line, breaking on suitable `,`

#### [Simon Hudon (Oct 08 2018 at 19:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/squeeze_simp/near/135416182):
That's tricky because it might not be alone on its line

#### [Johan Commelin (Oct 08 2018 at 19:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/squeeze_simp/near/135416288):
I can compute the old line length, and the new one, etc...

#### [Johan Commelin (Oct 08 2018 at 19:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/squeeze_simp/near/135416292):
It definitely makes a trivial thing a lot harder

#### [Simon Hudon (Oct 08 2018 at 19:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/squeeze_simp/near/135416372):
Let's leave it for the "future work" section

#### [Simon Hudon (Oct 08 2018 at 19:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/squeeze_simp/near/135416427):
It might become necessary to have a Lean code formatter which would make all of that good work redundant

#### [Johan Commelin (Oct 08 2018 at 19:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/squeeze_simp/near/135416431):
Yep, sounds good

#### [Simon Hudon (Oct 08 2018 at 19:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/squeeze_simp/near/135416520):
This proof engineering stuff is so funny. We're tweaking eternal truths :P

#### [Simon Hudon (Oct 08 2018 at 19:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/squeeze_simp/near/135416567):
As impatient as I get with Lean and mathlib, it's pretty great that it finds my mistakes faster than my supervisor :D

#### [Bryan Gin-ge Chen (Oct 08 2018 at 19:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/squeeze_simp/near/135416822):
Are there other "tactics with output" where this kind of tooling would also be useful? Maybe `tidy`?

#### [Mario Carneiro (Oct 08 2018 at 19:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/squeeze_simp/near/135416879):
`tidy` already makes output

#### [Johan Commelin (Oct 08 2018 at 19:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/squeeze_simp/near/135416916):
I'll be reading a bit of Milne to my kids... see you guys soon!

#### [Simon Hudon (Oct 08 2018 at 19:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/squeeze_simp/near/135416940):
Have fun!

#### [Bryan Gin-ge Chen (Oct 08 2018 at 19:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/squeeze_simp/near/135417013):
Indeed, what I mean is the output format being discussed here something we should also consider for e.g. `tidy`?

#### [Simon Hudon (Oct 08 2018 at 19:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/squeeze_simp/near/135417183):
That could be useful. It might be more useful for `tidy` to have it tied into the IDE because you probably don't use `tidy`*en masse*

#### [Gabriel Ebner (Oct 08 2018 at 19:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/squeeze_simp/near/135417482):
Where are you printing the replacement text?  Trace messages?

#### [Simon Hudon (Oct 08 2018 at 19:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/squeeze_simp/near/135417541):
Yes exactly

#### [Gabriel Ebner (Oct 08 2018 at 19:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/squeeze_simp/near/135417756):
It's pretty easy to hook them up in vscode: in the extension, you just need to [return a list of code actions](https://github.com/Microsoft/vscode/blob/5b03dcd69d98b6540f789868cf4647b6486ed739/src/vs/vscode.d.ts#L2046-L2106).  Then you can execute these replacements with `ctrl+.` (similar to holes, which are also implemented using code actions in the extension).

#### [Simon Hudon (Oct 08 2018 at 19:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/squeeze_simp/near/135417850):
Emacs gives the line and column of the command issuing the trace. Does VS code also do the same?

#### [Gabriel Ebner (Oct 08 2018 at 19:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/squeeze_simp/near/135417859):
A few suggestions for the format: it should not occur by accident (in a simp trace e.g.).  And it would be nice to have a (textual) description for the replacement (vscode shows this in the dropdown).  Ideally also the [kind of code action](https://github.com/Microsoft/vscode/blob/5b03dcd69d98b6540f789868cf4647b6486ed739/src/vs/vscode.d.ts#L1926-L1996), e.g. vscode can apply *all* quickfixes in a given file automatically.

#### [Gabriel Ebner (Oct 08 2018 at 19:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/squeeze_simp/near/135417920):
We have access to the same position information, yes.  However it only includes the start position of the tactic unfortunately.

#### [Simon Hudon (Oct 08 2018 at 19:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/squeeze_simp/near/135417924):
Does it run them backward so that the line numbers remain valid?

#### [Gabriel Ebner (Oct 08 2018 at 19:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/squeeze_simp/near/135417971):
Good question.  I don't really know.  If we do one-line replacements then it shouldn't matter too much.

#### [Simon Hudon (Oct 08 2018 at 19:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/squeeze_simp/near/135417976):
In the parser `cur_pos` can give me an arbitrary position. I'm putting it at the end and it gives me a good approximation

#### [Mario Carneiro (Oct 08 2018 at 19:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/squeeze_simp/near/135417980):
Ooh, this is nice. Can we just get a generic hook for writing things from lean?

