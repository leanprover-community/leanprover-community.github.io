---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/39122buildinfrastructure.html
---

## Stream: [general](index.html)
### Topic: [build infrastructure](39122buildinfrastructure.html)

---

#### [Scott Morrison (Nov 19 2018 at 22:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/build%20infrastructure/near/147995454):
Ok, I think I am going to take a pause on "math in Lean", and do some infrastructure work.

* I'm going to set up a virtual machine running on a fast machine that watches a shared Dropbox folder, and runs `lean --make` every time it sees anything change. Others can then `cd ~/Dropbox/lean-box/yourname/`, `ln -s ~/my-lean-project/`, and Dropbox will continuously deliver `.olean` files back to their project directory. I've tried this before, and it works, at least on a single OS.
* I'm going to try to catch up on @**Simon Hudon**'s investigation of `sccache`, and see what would need to happen to make this work, as it seems like an excellent solution. If we need to patch Lean, no problem; `elan` makes it very simple to work with forks these days.
* Keeley has told me that per-`begin ... end` block caching may be feasible, but probably requiring a small patch to Lean. When he has time, I'll ask him what's involved.

All of these seem more valuable than writing out explicit proofs of boring facts.

#### [Mario Carneiro (Nov 19 2018 at 22:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/build%20infrastructure/near/147995576):
sounds good to me... nothing like a little fear of tedium to get the ball rolling on more advanced automation and caching :)

#### [Patrick Massot (Nov 19 2018 at 22:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/build%20infrastructure/near/147995589):
https://github.com/leanprover/lean/issues/1601 makes me slightly pessimistic about the third item

#### [Scott Morrison (Nov 19 2018 at 22:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/build%20infrastructure/near/147995766):
I think Keeley's idea is hackier than what Leo had in mind, and so may have an orthogonal set of issues. :-)

#### [Johan Commelin (Nov 20 2018 at 05:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/build%20infrastructure/near/148015546):
@**Scott Morrison|110087** That sounds fantastic. I got the impression from Sebastian that Lean 3 might not be completely frozen, so minor tweaks might even be patched back into Lean.

#### [Johan Commelin (Nov 20 2018 at 05:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/build%20infrastructure/near/148015564):
Would it be an idea to develop some git hooks that look at your build server? And then instead of indexing by username, maybe index by git commit hash?

#### [Johan Commelin (Nov 20 2018 at 05:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/build%20infrastructure/near/148015578):
That way new users that install elan will automatically pull up to date oleans for the latest mathlib master.

#### [Johan Commelin (Nov 20 2018 at 06:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/build%20infrastructure/near/148017230):
@**Scott Morrison|110087** What kind of specs will your build machine have? Can I contribute with my little monster, or is it just a drop in the ocean compared to yours? I've got a 16-threaded beast with 24G RAM, but it is pretty oldish (7 years?). When otherwise idle, it compiles mathlib from scratch in about 6 minutes (using 12 threads on average).

#### [Scott Morrison (Nov 20 2018 at 06:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/build%20infrastructure/near/148017800):
Let's wait and see if we can actually build something that works, first. :-) This machine is slightly bigger (18 Xeon W cores, and 128gb of RAM), with a similar compile time (I actually remember timing 7 minutes?) The hardware is not the hard part, in any case.

#### [Keeley Hoek (Nov 20 2018 at 10:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/build%20infrastructure/near/148026785):
@**Scott Morrison|110087** The poor little Xeon :D On caching: we can really get arbitrarily fancy. My config monad work should be done in a day, so I'll finally get on it. (I had a migraine today :()

I really think the biggest obstacle is just syntax. If people can figure out a way to override lean's use of `tactic.execute` and `tactic.step`, then you'll only need an import to do caching in vanilla lean. From reading the source code `src/frontends/lean/tactic_notation.cpp` (see `parse_tactic_class()` in that file), I don't think this is possible and I will have to change one line of code. Otherwise you will have to type extra character(s), like `begin [cache] ... end` or `begin [c] ... end` or maybe `cbegin ... end` (but this would be vanilla supported).

The other option will be to point `elan` to to the fork with a `lean_version = "xxx"` in `leanpkg.toml`, which will get everything working without touching `begin ... end` blocks at all. This would be vanilla compatible---if you don't run the fork, you just don't get caching of these blocks.

My current understanding is that the actual caching implementation will not be too difficult. My "caching program" (not in the sense of an executable program), would be to first write fast `expr` serialization. I can think of all sorts of things---like storing proofs hot in mutable state in a user_attribute---which we could tack-on to speed up a naive caching implementation after-the-fact.

I suspect we could get more speed using a buddy-process and some tricks with writing the proofs directly to bytecode and back again (I have a strategy for getting lean to do this without touching bytecode handling ourselves), but perhaps this should be saved for the future. Since `begin...end` blocks can be processed in parallel, this step would definitely require a "buddy process" (such a thing would be completely invisible to the user, just like the communication processes that start up when you launch `rewrite_search`'s graph visualiser).

#### [Johan Commelin (Nov 20 2018 at 10:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/build%20infrastructure/near/148026910):
Awesome! I'm cheering for you!

#### [Keeley Hoek (Nov 20 2018 at 10:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/build%20infrastructure/near/148027124):
Also worth noting is that I keep having ideas to try to trick `[user_notation]`-like features into capturing a `begin...end`, but all have failed. Maybe someone else will come up with a smart way to do it. That's the problem which has been making me hesitant, though, so I guess I'll press onward for now.

#### [Sebastian Ullrich (Nov 20 2018 at 10:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/build%20infrastructure/near/148027203):
@**Keeley Hoek** How are you planning to deal with the nondeterminism issues described in the Github issue? That is, a cached proof term will most likely not be a valid term in the recomputed context, even though the input hasn't changed.

#### [Keeley Hoek (Nov 20 2018 at 11:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/build%20infrastructure/near/148029332):
I'm not confident about what you mean Sebastian---which of course is a bit scary.

The plan was (at least to start---and what everything I mentioned up there was about) just remembering the entire proof term which was generated in a `begin...end` block. The obvious impact is not having to re-run really expensive tactics which appear in that block, and only recompiling a small piece of a big file---or a huge chunk of mathlib if you changed a core file---if you only changed a proof, or added a new definition, etc. (I'm not claiming that any of this would be guaranteed to be *safe*, but I think Kenny's work is a testament to how much things could get better if you only have to run a `by simp` once to figure out it actually did, for example.)

So even though we don't remember what individual tactics did, or guarantee that the proof we remembered will work at all, I think this could still be really useful. Especially because, even when definitions of theorems are broken or a lemma argument is changed generated proofs using them will not work, this kind of hard caching will still stop the spread of the recompilation like a cancer throughout the entire library---hopefully only 1 level of recompilation will need to be done.

#### [Mario Carneiro (Nov 20 2018 at 11:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/build%20infrastructure/near/148029388):
the problem is that a context contains variables, identified by unique names, and these unique names will be different when you use an old term in a new context

#### [Mario Carneiro (Nov 20 2018 at 11:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/build%20infrastructure/near/148029446):
I think this can be fixed by just remembering the variables by their position instead of their name, or using positional information to reconstruct a bad name

#### [Keeley Hoek (Nov 20 2018 at 11:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/build%20infrastructure/near/148029476):
But do any such names actually appear in the final proof term? Like if I run `#print my_lemma`, surely there won't be much state in there?

#### [Mario Carneiro (Nov 20 2018 at 11:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/build%20infrastructure/near/148029581):
For example, if you have `\lam x y z, begin exact f x end` then lean sees `\lam x0 y1 z2, begin exact f x0 end`, and so if you store `f x0`, then when lean reparses the exact same theorem it sees `\lam x3 y4 z5, f x0` which doesn't typecheck

#### [Mario Carneiro (Nov 20 2018 at 11:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/build%20infrastructure/near/148029677):
The pp names and unique names are still associated to the binders in the final proof term

#### [Mario Carneiro (Nov 20 2018 at 11:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/build%20infrastructure/near/148029706):
and unique means something like globally unique since you turned on lean, I'm not sure how far you can push nonuniqueness

#### [Keeley Hoek (Nov 20 2018 at 11:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/build%20infrastructure/near/148030499):
I'm not sure I understand. Do you mean a program like this:
````
structure my_struct :=
(n : ℕ)
(g : ℕ → ℕ)

def f (y : ℕ) : ℕ := 2 * y

def a_constructor (n : ℕ) : my_struct :=
{
  n := n,
  g := λ x, begin exact f x end
}
````
for example?

If I do
````
run_cmd (do
  e ← tactic.get_env,
  l ← e.get `a_constructor,
  tactic.trace l.value.to_raw_fmt
)
````
I get
````
(lam n default (const nat []) (app (app (const my_struct.mk []) (var 0)) (lam x default (const nat []) (app (const f []) (var 0)))))
````
In particular, the `x` is bound under the lambda, so I don't need to worry about matching up the `x` with anything. Am I missing the point?

#### [Mario Carneiro (Nov 20 2018 at 11:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/build%20infrastructure/near/148030682):
well, two things: first the `lam` there is actually storing the unique id of the bound variable (so the `var` doesn't have to)

#### [Mario Carneiro (Nov 20 2018 at 11:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/build%20infrastructure/near/148030725):
and second, a tactic doesn't deal with closed terms, it is elaborated in an "open" context (with local constants in surrounding binders) corresponding to where `begin ... end` actually appears

#### [Mario Carneiro (Nov 20 2018 at 11:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/build%20infrastructure/near/148030785):
`to_raw_fmt` doesn't print the unique ids to save our sanity, I guess

#### [Mario Carneiro (Nov 20 2018 at 11:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/build%20infrastructure/near/148030794):
but you can pattern match it out

#### [Keeley Hoek (Nov 20 2018 at 11:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/build%20infrastructure/near/148031137):
I'm looking at the `expr` definition and it has `lam : name → binder_info → expr → expr → expr`---In particular, I don't see any room for a secret id `name` which could be stored in the second argument of the `local_const` constructor, for example
But I see the problem if a `local_const` (for example?) appears---and I understand your way to fix it, too

#### [Mario Carneiro (Nov 20 2018 at 11:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/build%20infrastructure/near/148031384):
oh, I guess I was mistaken

#### [Mario Carneiro (Nov 20 2018 at 11:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/build%20infrastructure/near/148031433):
looks like it's only when in a local context that you have to worry about the uids of local constants

#### [Scott Morrison (Nov 21 2018 at 03:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/build%20infrastructure/near/148084471):
Okay, so I can confirm that for sufficiently simple `.lean` files, as long as you consistently use the same version of Lean (preferably provided by elan, following a leanpkg.toml file), that the `.olean` files are completely cross platform.

#### [Scott Morrison (Nov 21 2018 at 03:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/build%20infrastructure/near/148084527):
With a very simple lean file containing `#print "compiling"` and a few definitions, then syncing that file via Dropbox between a mac, windows, and linux computer, I can verify that the olean file produced on any of the 3, works on the other two.

#### [Scott Morrison (Nov 21 2018 at 08:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/build%20infrastructure/near/148094316):
Unfortunately once you scale up to "all of mathlib", Dropbox puts too many timestamps in the wrong order, and essentially isn't useful.

#### [Scott Morrison (Nov 21 2018 at 08:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/build%20infrastructure/near/148094334):
Repeatedly running `lean --make` on two different computers (waiting for each to complete before running again) usually results in a small subset of mathlib being compiled each time you switch computers.

#### [Scott Morrison (Nov 21 2018 at 09:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/build%20infrastructure/near/148094418):
That said, I don't think I ever saw more than a minute of compiling on a single computer, so maybe it could be better than nothing...

#### [Scott Morrison (Nov 21 2018 at 09:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/build%20infrastructure/near/148094430):
`sccache` will hopefully be much more awesome. :-)

#### [Johan Commelin (Nov 21 2018 at 09:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/build%20infrastructure/near/148094459):
That minute on your computers translates to 6 minutes on my laptop, or Chris's...

#### [Johan Commelin (Nov 21 2018 at 09:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/build%20infrastructure/near/148094494):
But sure, it still is helpful.

#### [Scott Morrison (Nov 21 2018 at 09:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/build%20infrastructure/near/148094635):
Ok, I will soon add some scripts that relentlessly run `lean --make` on appropriate subdirectories, and try it out for real. (e.g. have my desktop machine compile for my laptop, and if anyone else wants to try it to)

#### [Patrick Massot (Nov 21 2018 at 14:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/build%20infrastructure/near/148108370):
Before doing fancy Dropbox things, why not trying to copy-paste what the main Lean repository is doing to produce lean nightlies  and get a lean-community/mathlib-nightlies/ repository? Should I try to do that?

#### [Patrick Massot (Nov 21 2018 at 14:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/build%20infrastructure/near/148108687):
@**Sebastian Ullrich** do you have comments about the above plan? Is there anything I should know about why the Lean nightlies are setup that way?

#### [Sebastian Ullrich (Nov 21 2018 at 14:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/build%20infrastructure/near/148108897):
You mean why is it a separate repo?

#### [Patrick Massot (Nov 21 2018 at 14:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/build%20infrastructure/near/148108950):
Yes, for instance

#### [Patrick Massot (Nov 21 2018 at 14:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/build%20infrastructure/near/148108959):
or any other comment

#### [Patrick Massot (Nov 21 2018 at 14:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/build%20infrastructure/near/148108963):
maybe no comment is needed

#### [Sebastian Ullrich (Nov 21 2018 at 14:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/build%20infrastructure/near/148109070):
I suppose the Dropbox solution makes it easy to actually deliver the output to people

#### [Patrick Massot (Nov 21 2018 at 14:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/build%20infrastructure/near/148109097):
I really don't like to idea to ask people interested in mathlib to use Dropbox

#### [Sebastian Ullrich (Nov 21 2018 at 14:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/build%20infrastructure/near/148109177):
The nightlies are in a separate repository so that they are not mixed with the official releases on the Github Releases page

#### [Sebastian Ullrich (Nov 21 2018 at 14:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/build%20infrastructure/near/148109267):
I guess what you'd want to have is to point `leanpkg` to a Github Release including .olean files instead of a git hash, just like with `elan`. But that... would not be a small task.

#### [Sebastian Ullrich (Nov 21 2018 at 14:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/build%20infrastructure/near/148109317):
Or alternatively have `sccache` do that

#### [Patrick Massot (Nov 21 2018 at 14:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/build%20infrastructure/near/148109511):
What I mean is much more naive: I want to be able to write a tiny bash script that downloads a compiled version of mathlib inside the `_target` subdirectory of the current directory, and uses touch to pretend every olean have just been created.

#### [Sebastian Ullrich (Nov 21 2018 at 14:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/build%20infrastructure/near/148109913):
Yeah, that doesn't sound too bad to me

#### [Patrick Massot (Nov 21 2018 at 14:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/build%20infrastructure/near/148110228):
Ok, thanks. I'll try to do that

#### [Simon Hudon (Nov 22 2018 at 02:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/build%20infrastructure/near/148148031):
That can be a viable solution but if someone wanted to figure out how to setup sccache to share storable, I think that would be more effective. That way, we wouldn't have to upload a new version of mathlib every few day. Just compiling would get the mathlib that others have compiled

