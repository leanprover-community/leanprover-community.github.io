---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/39364compiletimestatistics.html
---

## Stream: [general](index.html)
### Topic: [compile time statistics](39364compiletimestatistics.html)

---


{% raw %}
#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Sep 24 2018 at 07:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/134506913):
Can we get some data on how long it takes for *each* file to compile?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Sep 24 2018 at 07:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/134506915):
in mathlib, that is

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Sep 24 2018 at 07:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/134507008):
You can call `lean file.lean --profile` on each. You can get the list of all the files of `mathlib` with `git ls-files *.lean`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Sep 24 2018 at 08:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/134508030):
Make sure everything is already compiled before starting this, so it's only recompiling the particular file you've asked about.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Sep 24 2018 at 08:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/134508037):
However I'd guess that even this could give misleading results: lean still has to reparse all the imported `.olean` files, so at the end of a huge development you'd expect even tiny files to have very large compile times with this technique.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Sep 24 2018 at 08:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/134508409):
@**Scott Morrison|110087** then what should I do?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Sep 24 2018 at 08:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/134508430):
Well, I guess you could measure how bad the effect I pointed out it, by timing compiling an empty olean file that imports everything?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Sep 24 2018 at 08:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/134508454):
Or even fancier, you could time compiling an empty olean file with the exact same imports, and subtract that time off.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Sep 24 2018 at 08:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/134508499):
I really don't have a good sense of whether this is necessary!

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Sep 24 2018 at 08:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/134508504):
I can't think of any direct way to get these per-file timings, however.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Sep 24 2018 at 08:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/134508534):
I'm really tempted to neglect that time

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Sep 24 2018 at 08:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/134508584):
You can do it once with all the files to get an upper bound on how much time that is but I feel like that must be negligible compared with everything else

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Sep 24 2018 at 08:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/134509157):
if I have a file `e.lean` that imports `a` and `b` and `c` and `d`, can I look at the time of `e` and subtract from it the times of the other four files?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Sep 24 2018 at 08:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/134509337):
I've now tracked 57 out of 255 files

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Sep 24 2018 at 08:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/134509338):
this is really slow

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Sep 24 2018 at 08:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/134509339):
You shouldn't do it that way.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Sep 24 2018 at 08:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/134509342):
Start with `lean --make`, then build each file

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Sep 24 2018 at 08:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/134509348):
I have all the oleans already

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Sep 24 2018 at 08:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/134509352):
I'm running this command:
` git ls-files *.lean | xargs -n1 /c/lean/bin/lean --profile > junk.txt 2> time.txt`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Sep 24 2018 at 09:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/134509388):
Ok, in that case, all that is left is wait. The travis build takes more than an hour

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Sep 24 2018 at 09:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/134509410):
brilliant

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Sep 24 2018 at 09:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/134509424):
Yup

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Sep 24 2018 at 09:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/134510040):
117 out of 255 files

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Sep 24 2018 at 10:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/134514042):
there are 11 files that did not show any `cumulative profiling times:`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Sep 24 2018 at 10:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/134514044):
which 11 files is that?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Sep 24 2018 at 11:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/134514346):
https://gist.github.com/kckennylau/6ea2ca42e517ad801564a86fe7a1b7bd

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Sep 24 2018 at 11:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/134514354):
time in seconds, may have indexing error by at most 11

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Sep 24 2018 at 11:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/134514478):
```
commit ca7f118058342a2f077e836e643d26e0ad1f3ca6
Author: Rob Lewis <Rob.y.lewis@gmail.com>
Date:   Fri Sep 21 17:06:34 2018 +0200

    fix(docs/tactics.md): missing backquote, formatting

    I think I never previewed when I updated the `linarith` doc before, sorry.
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Sep 24 2018 at 11:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/134514888):
I guess afterall looking at the file size might be more reliable

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Sep 24 2018 at 11:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/134515602):
is it a good idea if I start working on making the files compile faster?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Sep 24 2018 at 11:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/134515606):
@**Mario Carneiro** will you guys accept my PR?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Sep 24 2018 at 11:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/134515948):
I think it's really a huge problem that we are tempted to sacrifice readability for compile time

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Sep 24 2018 at 11:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/134516218):
yes, if you can make a significant improvement on compile times without making the proof much longer, I think I would accept it without issue. I assume you will start from really bad offenders. If you can get at least ~70% reduction in compile time then I would accept a modest increase in proof size

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Sep 24 2018 at 11:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/134516273):
I find that readability is mostly orthogonal to compile time

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Sep 24 2018 at 11:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/134516451):
challenge accepted

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Sep 24 2018 at 15:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/134526934):
I would guess the 11 files which had no profiling information are the `.default` modules which do nothing but import other modules

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Sep 24 2018 at 15:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/134526938):
but I don't understand your data yet

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Sep 24 2018 at 16:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/134528608):
```quote
I think it's really a huge problem that we are tempted to sacrifice readability for compile time
```
But @**Patrick Massot**, it means we can join the programmers https://xkcd.com/303/

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Keeley Hoek (Sep 24 2018 at 16:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/134528990):
https://xkcd.com/1205/

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Sep 24 2018 at 17:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/134534111):
```quote
but I don't understand your data yet
```
just assume that big numbers means bad, no matter how many there are

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Sep 24 2018 at 19:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/134541798):
Another approach is to look at the frequent offenders, the tactics that most often eat up most of the run time of proofs. Then we can work on making them faster. If you find such offenders, I wouldn't mind pitching in to improve the tactics.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Sep 24 2018 at 21:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/134552824):
I think `simp` is like plastic

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Sep 24 2018 at 21:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/134552838):
when it was discovered, everyone thought it's the greatest idea in the world, and everyone used it

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Sep 24 2018 at 21:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/134552843):
and it's too late when everyone discovered the ramifications it brings

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Sep 24 2018 at 21:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/134552865):
Kurzgesagt compares plastic with the story of the king with the golden touch

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Sep 24 2018 at 22:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/134553864):
One way to improve the performances of `simp` is to create specialized list of simp lemmas. You can have a look at `functor_norm`. Sometimes, `simp only with <my-list>` can be sufficient and will be faster.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Sep 24 2018 at 22:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/134553952):
Are you really sure that `simp` is the slow thing? It seems to me elaboration is often very slow

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Sep 24 2018 at 22:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/134554391):
Do you know what kind of situation makes elaboration slow? 

Aside from that, if we divide a proof into proof search + elaboration + proof check, I think shrinking the proof search side will also shrink the elaboration and proof check side because proof search often uses both to select the right approach.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Sep 24 2018 at 22:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/134554606):
```quote
One way to improve the performances of `simp` is to create specialized list of simp lemmas. You can have a look at `functor_norm`. Sometimes, `simp only with <my-list>` can be sufficient and will be faster.
```
https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simp_attr

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Sep 24 2018 at 22:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/134554943):
Yes there are pitfalls

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Sep 24 2018 at 22:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/134554995):
One thing you can do is create simp attributes local to files or modules and group in that lemma everything useful for its proofs.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Sep 24 2018 at 22:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/134555063):
Then you can merge those lists as a shortcut for just listing all the useful lemmas.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Sep 24 2018 at 22:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/134555156):
The other possibility is to create a command for listing all the simp lemmas used in a file and printing out the way to create the required simp lemma

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Sep 25 2018 at 05:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/134572292):
```
$ git checkout master
Switched to branch 'master'
Your branch is up-to-date with 'origin/master'.

$ /c/lean/bin/lean --profile algebra/big_operators.lean >/dev/null
cumulative profiling times:
        compilation 1.37ms
        decl post-processing 7.92s
        elaboration 47.7s
        elaboration: tactic compilation 676ms
        elaboration: tactic execution 42s
        parsing 1.18s
        type checking 19.5ms

$ git checkout faster
Switched to branch 'faster'

$ /c/lean/bin/lean --profile algebra/big_operators.lean >/dev/null
cumulative profiling times:
        compilation 1.53ms
        decl post-processing 6.86s
        elaboration 7.37s
        elaboration: tactic compilation 561ms
        elaboration: tactic execution 3.82s
        parsing 995ms
        type checking 17.9ms
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Sep 25 2018 at 05:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/134572294):
@**Mario Carneiro**

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Sep 25 2018 at 05:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/134572336):
elaboration 47.7s --> 7.37s
elaboration: tactic execution 42s --> 3.82s

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Sep 25 2018 at 05:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/134572344):
Nice! What did you do?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Sep 25 2018 at 05:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/134572391):
I removed the simp

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Sep 25 2018 at 05:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/134572396):
and replaced them with either a term proof or `rw` or `simp only`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Sep 25 2018 at 05:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/134572472):
How long did it take for each proof?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Sep 25 2018 at 06:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/134572668):
https://gist.github.com/kckennylau/6d1e02b8289f24be38416642b5d91142

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Sep 25 2018 at 06:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/134572694):
https://github.com/leanprover-community/mathlib/commit/c347e9940c773faf79358b0bf320e73247f51023

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Keeley Hoek (Sep 25 2018 at 13:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/134590722):
I've got a setup where I can hook-in to `begin` blocks and take control away from lean when they occur, and do whatever I want to the `texpr`s in the `begin ... end` just by importing a file. One use case is replacing `simp` by what it did last time and seeing if it works---and saving this in a file to be used again later (the idea I mentioned before). You'd enable it by adding `import tactic.caching` or something at the top of your file.

This would mean you'd be able to get performance benefits like this without obfuscating the code (but as Scott, or someone else mentioned last time stale caches could break a fresh build for someone else, so you'd have to clear before shipping). If I can get everything working robustly, would anyone hacking on mathlib be willing to try it out?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Sep 25 2018 at 15:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/134596822):
I reckon if we removed all the simp, it can compile in under 10 minutes

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Sep 26 2018 at 15:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/134672859):
```
git ls-files *.lean | xargs -I % sh -c '>&2 echo %; /c/lean/bin/lean --profile % >/dev/null;' > profile.txt 2>&1
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Sep 26 2018 at 15:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/134672866):
https://gist.github.com/kckennylau/04917450f71db69f29150d64f360dd0f

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Sep 26 2018 at 15:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/134672884):
if A imports B and C, do I need to subtract the times of B and C from the time of A to get a more accurate datum?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Sep 26 2018 at 15:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/134672933):
also, I learnt the hard way that you need to `lean --make` it before doing this

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Sep 26 2018 at 15:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/134674307):
as long as you lean --make beforehand subtraction shouldn't be necessary

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Sep 26 2018 at 18:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/134687725):
https://gist.github.com/kckennylau/7cd92fe25114061b706d6c86aa8059ea

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Sep 26 2018 at 18:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/134687831):
sorted: https://gist.github.com/kckennylau/f7c6cbfb2aa8bf7e4784e8c65d6c4852

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Sep 26 2018 at 18:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/134687841):
all time in seconds

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Sep 26 2018 at 18:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/134687864):
well I can't say that any of the top ten are a surprise

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Sep 26 2018 at 18:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/134687936):
What do you get if you sort by compile time / length in characters?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Sep 26 2018 at 18:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/134687960):
the longest files are of course going to take a long time to compile

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Sep 26 2018 at 18:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/134687974):
what do the multiple numbers mean in the first gist?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Sep 26 2018 at 18:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/134688034):
so a raw datum looks like:
```
cumulative profiling times:
        compilation 253ms
        decl post-processing 2.84s
        elaboration 114s
        elaboration: tactic compilation 3.57s
        elaboration: tactic execution 86.9s
        parsing 5.23s
        type checking 229ms
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Sep 26 2018 at 18:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/134688037):
I filtered out the `ms`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Sep 26 2018 at 18:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/134688040):
and listed each item

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Sep 26 2018 at 18:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/134688045):
and added the numbers together in the last gist

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Sep 26 2018 at 18:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/134688450):
https://gist.github.com/kckennylau/7318d851eca2f951e7acdaa6ffbe65b7

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Sep 26 2018 at 18:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/134688451):
@**Mario Carneiro** ^

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Sep 26 2018 at 18:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/134688562):
complex/basic is a surprise

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Sep 26 2018 at 18:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/134688753):
```
elaboration: tactic execution took 1.31s
elaboration of ext_iff took 1.45s
elaboration: tactic execution took 1.51s
elaboration of of_real_neg took 1.6s
elaboration of mk_eq_add_mul_I took 1.62s
elaboration: tactic execution took 1.61s
elaboration of of_real_mul took 1.75s
elaboration: tactic execution took 1.26s
elaboration of re_add_im took 1.37s
elaboration: tactic execution took 1.08s
elaboration of conj_of_real took 1.17s
elaboration of conj_I took 1.16s
elaboration: tactic execution took 1.38s
elaboration of conj_add took 1.5s
elaboration: tactic execution took 2.08s
elaboration of conj_neg took 2.22s
elaboration: tactic execution took 1.99s
elaboration of conj_conj took 2.14s
elaboration: tactic execution took 2.22s
elaboration of conj_mul took 2.39s
elaboration: tactic execution took 2s
elaboration of conj_eq_zero took 2.13s
elaboration: tactic execution took 1.32s
elaboration of norm_sq_of_real took 1.45s
elaboration: tactic execution took 1.23s
elaboration of norm_sq_zero took 1.35s
elaboration of norm_sq_one took 1.4s
elaboration: tactic execution took 1.24s
elaboration of norm_sq_I took 1.35s
elaboration: tactic execution took 1.19s
elaboration of norm_sq_pos took 1.27s
elaboration: tactic execution took 1.27s
elaboration of norm_sq_neg took 1.37s
elaboration: tactic execution took 1.23s
elaboration of norm_sq_conj took 1.34s
elaboration: tactic execution took 1.49s
elaboration of norm_sq_mul took 1.6s
elaboration: tactic execution took 1.13s
elaboration of norm_sq_add took 1.22s
elaboration of add_conj took 1.14s
elaboration: tactic execution took 1.17s
elaboration of mul_conj took 1.29s
elaboration: tactic execution took 2.3s
elaboration of comm_ring took 3.35s
elaboration of inv_im took 1.06s
elaboration of inv_re took 1.09s
elaboration: tactic execution took 1.05s
elaboration of sub_conj took 1.14s
elaboration: tactic execution took 1.04s
elaboration of norm_sq_sub took 1.13s
elaboration: tactic execution took 1.29s
elaboration: tactic execution took 1.01s
elaboration of of_real_inv took 1.71s
elaboration of conj_inv took 1.54s
elaboration: tactic execution took 1.3s
elaboration of norm_sq_inv took 1.51s
elaboration: tactic execution took 1.36s
elaboration of of_real_int_cast took 1.9s
elaboration of abs_of_real took 1.01s
elaboration of re_eq_add_conj took 1.06s
elaboration: tactic execution took 1.22s
elaboration of of_real_rat_cast took 1.32s
elaboration of abs_conj took 1.04s
elaboration: tactic execution took 1.05s
elaboration of abs_add took 1.18s
elaboration: tactic execution took 1.02s
elaboration of abs_le_abs_re_add_abs_im took 1.11s
elaboration: tactic execution took 1.1s
elaboration of is_cau_seq_re took 1.24s
elaboration: tactic execution took 1.1s
elaboration of is_cau_seq_im took 1.27s
elaboration: tactic execution took 1.02s
elaboration of equiv_lim took 1.44s
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Sep 26 2018 at 18:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/134688766):
that's `grep /\d+(\.\d+)?s/`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Sep 26 2018 at 18:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/134688816):
(I know, I should have done `grep /\d+s/`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Sep 26 2018 at 18:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/134688835):
also, 47 usages of `simp`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Sep 26 2018 at 18:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/134688842):
that's `/^simp|^.simp|[^@].simp/` because VScode doesn't have lookbehind

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Sep 26 2018 at 19:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/134688935):
@**Mario Carneiro** what do you think?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Sep 26 2018 at 19:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/134689238):
Here are the top 30 files on the second list that take more than 100 seconds:
```
data/complex/basic.lean                   0.008525  104.10
data/finset.lean                          0.006419  359.15
order/conditionally_complete_lattice.lean 0.005851  152.78
data/polynomial.lean                      0.004392  213.90
data/finsupp.lean                         0.003828  121.20
group_theory/perm.lean                    0.003750  101.33
set_theory/ordinal.lean                   0.003531  397.60
linear_algebra/basic.lean                 0.003494  123.04
analysis/topology/topological_space.lean  0.002850  161.68
```
I suggest focusing on these

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Sep 26 2018 at 19:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/134689380):
ok

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Sep 26 2018 at 19:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/134689383):
if you can decrease the compile times of all of these by half that will take 15 minutes off the total compile time, or 30%

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Sep 26 2018 at 19:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/134690262):
A ton of lemmas in `complex.basic` are `rfl`, but were proved with `simp`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Sep 26 2018 at 19:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/134692162):
```quote
A ton of lemmas in `complex.basic` are `rfl`, but were proved with `simp`
```
@**Kenny Lau** I just pushed some improvements to `complex.basic`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Sep 26 2018 at 19:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/134692189):
thanks!

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Sep 28 2018 at 20:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/134841829):
before:
```
data/finset.lean
cumulative profiling times:
	compilation 138ms
	decl post-processing 178ms
	elaboration 173s
	elaboration: tactic compilation 1.83s
	elaboration: tactic execution 182s
	parsing 2.32s
	type checking 125ms
```
after:
```
cumulative profiling times:
        compilation 85.2ms
        decl post-processing 130ms
        elaboration 10.2s
        elaboration: tactic compilation 1.06s
        elaboration: tactic execution 4.98s
        parsing 1.48s
        type checking 90ms
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Sep 28 2018 at 20:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/134841841):
@**Mario Carneiro** that's way more than a 70% reduction :P

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Bryan Gin-ge Chen (Sep 28 2018 at 20:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/134841994):
That's awesome! Since I've been working almost exclusively with finset recently, I hope this gets in soon!

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 28 2018 at 21:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/134844724):
Very impressive Kenny. Is this all changing `simp` to `simp only`?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Sep 28 2018 at 21:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/134847149):
I'm going start an experiment to see if my idea for `squeeze_simp` is worthwhile. Is anybody else working on optimizing `conditionally_complete_lattice.lean`?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Sep 28 2018 at 22:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/134850447):
I'm going to work on `ordinal.lean` now

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Sep 29 2018 at 07:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/134869784):
@**Simon Hudon** How much improvement did `squeeze_simp` give in your experiment? Does it approach the magical 70%?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Sep 29 2018 at 08:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/134871081):
Yes, the file initially took 35s process, then, I used `squeeze_simp` and it went down to 11s.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Sep 29 2018 at 10:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/134873374):
```lean
theorem mul_le_of_limit {a b c : ordinal.{u}}
  (h : is_limit b) : a * b ≤ c ↔ ∀ b' < b, a * b' ≤ c :=
⟨λ h b' l, le_trans (mul_le_mul_left _ (le_of_lt l)) h,
λ H, le_of_not_lt $
induction_on a (λ α r _, induction_on b $ λ β s _ h H l, begin
try_for 300 {
  resetI,
  suffices : ∀ a b, prod.lex s r (b, a) (enum _ _ l),
  { cases enum _ _ l with b a, exact irrefl _ (this _ _) },
  intros a b,
  rw [← typein_lt_typein (prod.lex s r), typein_enum],
  have := H _ (h.2 _ (typein_lt_type s b)),
  rw [mul_succ] at this,
  have := lt_of_lt_of_le ((add_lt_add_iff_left _).2
    (typein_lt_type _ a)) this,
  refine lt_of_le_of_lt _ this,
  refine (type_le'.2 _),
  constructor,
}, try_for 800 {
  refine order_embedding.of_monotone (λ a, _) (λ a b, _),
},

/-  { rcases a with ⟨⟨b', a'⟩, h⟩,
    by_cases e : b = b',
    { refine sum.inr ⟨a', _⟩,
      subst e, cases h with _ _ _ _ h _ _ _ h,
      { exact (irrefl _ h).elim },
      { exact h } },
    { refine sum.inl (⟨b', _⟩, a'),
      cases h with _ _ _ _ h _ _ _ h,
      { exact h }, { exact (e rfl).elim } } },
  { rcases a with ⟨⟨b₁, a₁⟩, h₁⟩,
    rcases b with ⟨⟨b₂, a₂⟩, h₂⟩,
    intro h, by_cases e₁ : b = b₁; by_cases e₂ : b = b₂,
    { substs b₁ b₂, simpa only [subrel_val, prod.lex_def, @irrefl _ s _ b, true_and, false_or, eq_self_iff_true, dif_pos, sum.lex_inr_inr] using h },
    { subst b₁, simp only [subrel_val, prod.lex_def, e₂, prod.lex_def, dif_pos, subrel_val, eq_self_iff_true, or_false, dif_neg, not_false_iff, sum.lex_inr_inl, false_and] at h ⊢,
      cases h₂; [exact asymm h h₂_h, exact e₂ rfl] },
    { squeeze_simp [e₁, e₂, dif_pos, eq_self_iff_true, dif_neg, not_false_iff, sum.lex.sep] },
    { simpa only [dif_neg e₁, dif_neg e₂, prod.lex_def, subrel_val, subtype.mk_eq_mk, sum.lex_inl_inl] using h } }-/
end) h H⟩
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Sep 29 2018 at 10:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/134873377):
@**Mario Carneiro** this is your file

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Sep 29 2018 at 10:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/134873382):
I don't know what to do with this

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Sep 29 2018 at 10:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/134873432):
what's the question?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Sep 29 2018 at 10:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/134873433):
that one line takes 800 ms

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Sep 29 2018 at 10:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/134873435):
not to mention the lines afterwards

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Sep 29 2018 at 10:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/134873436):
somehow `order_embedding.of_monotone` is an expensive definition

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Sep 29 2018 at 10:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/134873437):
(it isn't a thoerem)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Sep 29 2018 at 10:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/134873478):
how can I make it faster?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Sep 29 2018 at 10:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/134873494):
I will let you know when my lean catches up to that definition :P

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Sep 29 2018 at 10:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/134873495):
if only it compiled faster...

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Sep 29 2018 at 10:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/134873534):
right, ironic

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Sep 29 2018 at 10:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/134873545):
I wonder if anyone is working on it

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Sep 29 2018 at 10:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/134873548):
Anyway, you can always skip it and return later

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Sep 29 2018 at 10:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/134873556):
right

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Sep 29 2018 at 10:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/134873558):
I doubt anyone is working on `ordinal` other than you right now

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Sep 29 2018 at 10:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/134873941):
@**Simon Hudon** Any chance you can register the hole command? After that we could easily distribute the work to everyone who has a couple of spare minutes.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Sep 29 2018 at 10:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/134874557):
The hole command is not trivial to build because I have to come up with a syntax for the expression found in the hole. It has to allow the encoding of information such as `simp! [h0,h1] with attr at *`. I'm going to postpone that until I have a better idea on how to do it. In the mean time, if you have `simp! [h0,h1] with attr at *`, simply replace it with `squeeze_simp! [h0,h1] with attr at *` and it will print out a replacement that you simply have to copy and paste. That same also works for `simpa`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Sep 29 2018 at 10:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/134874570):
Ok, cool!

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Sep 29 2018 at 10:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/134874575):
Thanks a lot for this.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Sep 29 2018 at 10:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/134874583):
:+1:

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Sep 29 2018 at 10:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/134874623):
Now I should really get some sleep :) Best of luck

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Sep 29 2018 at 10:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/134874839):
Sleep tight :in_bed:

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Sep 29 2018 at 11:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/134875338):
Hmm, I have proofs where `by simp` works, but `by squeeze_simp` fails. E.g., line 157 of `order/filter.lean`.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Sep 29 2018 at 19:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/134889142):
I `squeeze_simp`ed `order/filter.lean`. I didn't time carefully but I think I got the compile time down to maybe 25s.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Sep 29 2018 at 21:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/134893202):
```quote
I `squeeze_simp`ed `order/filter.lean`. I didn't time carefully but I think I got the compile time down to maybe 25s.
```
from what?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Sep 29 2018 at 21:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/134893462):
I think your gist said something like 150s

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Sep 29 2018 at 21:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/134893465):
But I don't have good tools to time an entire file

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Sep 29 2018 at 21:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/134893468):
I did see pretty nice speed-ups from some of the substitutions

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Sep 29 2018 at 21:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/134893517):
the time on my gist is relative to me and my computer

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Sep 29 2018 at 21:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/134893916):
@**Johan Commelin** In emacs at least, there's a `lean-std-exe` command. It will compile the current file, tell you the time at which it starts and the time at which it ends.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Sep 29 2018 at 22:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/134894297):
```lean
theorem add_le_add_left {a b : ordinal} : a ≤ b → ∀ c, c + a ≤ c + b :=
induction_on a $ λ α₁ r₁ _, induction_on b $ λ α₂ r₂ _ ⟨⟨⟨f, fo⟩, fi⟩⟩ c,
induction_on c $ λ β s _,
⟨⟨⟨(embedding.refl _).sum_congr f,
  λ a b, begin try_for 200 { cases a with a a; cases b with b b;
    split; intro H; cases H with _ _ H _ _ H _ _ H; constructor,
    { assumption }, { assumption },
    { rw ← fo, assumption }, { rw fo, assumption } }
  end⟩,
  λ a b H, begin try_for 200 { cases b with b b, { exact ⟨sum.inl b, rfl⟩ },
    cases a with a a, {cases H},
    cases fi _ _ (sum.lex_inr_inr.1 H) with w h, exact ⟨sum.inr w, congr_arg sum.inr h⟩ }
  end⟩⟩
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Sep 29 2018 at 22:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/134894298):
I'm at a bit of a loss here

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Sep 29 2018 at 22:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/134894299):
both blocks take < 200 ms

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Sep 29 2018 at 22:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/134894303):
but the whole thing takes 5 s

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Sep 29 2018 at 22:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/134894935):
Presumably some elaboration is taking ages then? Computing lots of motives.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Sep 29 2018 at 22:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/134894939):
i'm trying to convert it to term mode

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Sep 29 2018 at 22:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/134895382):
solved using term mode

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Sep 29 2018 at 22:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/134895383):
```lean
theorem add_le_add_left {a b : ordinal} : a ≤ b → ∀ c, c + a ≤ c + b :=
induction_on a $ λ α₁ r₁ _, induction_on b $ λ α₂ r₂ _ ⟨⟨⟨f, fo⟩, fi⟩⟩ c,
induction_on c $ λ β s _,
⟨⟨⟨(embedding.refl _).sum_congr f,
  λ a b, ⟨λ H, sum.lex.rec_on H (λ _ _, sum.lex_inl_inl.2)
      (λ _ _ h, sum.lex_inr_inr.2 $ fo.1 h) (λ _ _, sum.lex.sep _ _ _ _),
    sum.rec_on a (λ a, sum.rec_on b (λ b, sum.lex_inl_inl.2 ∘ sum.lex_inl_inl.1)
        (λ _ _, sum.lex.sep _ _ _ _))
      (λ a, sum.rec_on b (λ b, false.elim ∘ sum.lex_inr_inl)
        (λ b, sum.lex_inr_inr.2 ∘ fo.2 ∘ sum.lex_inr_inr.1))⟩⟩,
  λ a b, sum.rec_on b (λ _ _, ⟨sum.inl _, rfl⟩)
    (λ b, sum.rec_on a (λ a, false.elim ∘ sum.lex_inr_inl)
      (λ a H, let ⟨w, h⟩ := fi _ _ (sum.lex_inr_inr.1 H) in
        ⟨sum.inr w, congr_arg sum.inr h⟩))⟩⟩
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Sep 29 2018 at 22:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/134895385):
< 500 ms

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Sep 29 2018 at 22:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/134895440):
Is this copy and pasting the proof term built by tactic mode?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Sep 29 2018 at 22:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/134895441):
hardly

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Sep 29 2018 at 22:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/134895442):
I built the proof myself

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Sep 29 2018 at 22:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/134895494):
hand-crafted artisanal proofs

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Sep 30 2018 at 00:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/134898707):
set_theory/ordinal.lean
before:
```
cumulative profiling times:
	compilation 75.5ms
	decl post-processing 255ms
	elaboration 208s
	elaboration: tactic compilation 3.75s
	elaboration: tactic execution 179s
	parsing 6.85s
	type checking 155ms
```
after:
```
cumulative profiling times:
        compilation 81.1ms
        decl post-processing 286ms
        elaboration 39.8s
        elaboration: tactic compilation 3.67s
        elaboration: tactic execution 16.9s
        parsing 6.22s
        type checking 165ms
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Sep 30 2018 at 00:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/134898752):
I really wish Mario could help me speed up this file

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Sep 30 2018 at 00:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/134898756):
there are some parts that I can't speed up

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Sep 30 2018 at 00:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/134898873):
also, which one of the number is (closest to) the actual build time?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 30 2018 at 01:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/134899347):
```quote
also, which one of the number is (closest to) the actual build time?
```
The largest one.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 30 2018 at 01:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/134900435):
```quote
I really wish Mario could help me speed up this file
```
He's busy with modules, leave him be ;-)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 30 2018 at 01:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/134900438):
After he does modules you can do algebraic closure remember!

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Sep 30 2018 at 02:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/134901088):
> i'm trying to convert it to term mode

Is there a particular reason you are doing this? I don't think that converting to term mode is necessarily an improvement; in particular some tactics like `rw` and `induction` can actually be faster than their term mode equivalents because they can fill in the motives in a straightforward way while the elaborator has to deal with other stuff at the same time that can confound the issue

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Sep 30 2018 at 02:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/134901127):
Do you have evidence that a tactic proof that, say, does `refine refine rw cases exact` is faster than its term mode equivalent?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Sep 30 2018 at 02:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/134901227):
In particular, if an elaboration is slow, I find that converting to a sequence of `refine`s often speeds it up, or at least narrows the problem down to a particular term that should be written a different way

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Sep 30 2018 at 05:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/134906074):
no I'm not converting every proof to term mode.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Sep 30 2018 at 05:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/134906076):
I'm converting that particular proof to term mode and it turns out that the speed improved a lot.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Sep 30 2018 at 05:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/134906078):
I'm not making a general claim.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Sep 30 2018 at 05:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/134906086):
(although in my experience, pure term mode proofs do compile much faster)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Sep 30 2018 at 05:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/134906088):
I can give you the statistics for that particular theorem if you want.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Sep 30 2018 at 05:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/134906137):
it's not necessarily an improvement but in this case it is.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Sep 30 2018 at 05:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/134906248):
In this case I would probably take your term proof and reintroduce tactics to recover some of the original structure, while keeping an eye on the compile time and preventing it from growing again

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Sep 30 2018 at 05:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/134906366):
fair enough.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Sep 30 2018 at 08:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/134911308):
@**Mario Carneiro** Am I allowed to remove `exactI / resetI / letI` and use `@` to provide the typeclass instances whenever doing so would produce a significant speed boost?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Sep 30 2018 at 08:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/134911324):
oof, I really hope that's a last resort

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Sep 30 2018 at 08:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/134911365):
I don't think it matters whether `exactI` is used or not, sometimes typeclass inference is slow

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Sep 30 2018 at 08:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/134911366):
It is possible that with better hints you can shortcut the search

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Sep 30 2018 at 08:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/134911416):
well without exactI I can tell which typeclasses Lean is struggling to infer

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Sep 30 2018 at 08:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/134911424):
and I can provide it explicitly to save Lean's time

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Sep 30 2018 at 08:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/134911468):
I would try to use limited typeclass inference, i.e. write the hard part of the term and have lean figure out the rest

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Sep 30 2018 at 08:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/134911521):
But explicit typeclass parameters are a big loss in readability, especially if you have to say things more than once, so I would try *really* hard to avoid it

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Sep 30 2018 at 08:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/134911522):
I understand

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Sep 30 2018 at 08:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/134911834):
```lean
import set_theory.ordinal

universe u

set_option trace.class_instances true
#check
λ α : Type u,
λ r : α → α → Prop,
λ hr : is_well_order α r,
λ β : Type u,
λ s : β → β → Prop,
λ hs : is_well_order β s,
λ x : β, (by apply_instance : is_asymm (α ⊕ ↥{b : β | s b x}) (@sum.lex α ↥{b : β | s b x} r (@subrel β s {b : β | s b x})))
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Sep 30 2018 at 08:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/134911839):
@**Mario Carneiro** how to shorten the path for class instance?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Sep 30 2018 at 08:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/134911953):
it is much faster if I use `is_asymm_of_is_trans_of_is_irrefl` instead of `by apply_instance`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Sep 30 2018 at 08:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/134911994):
alternatively, prove and use `is_asymm_of_is_well_order`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Sep 30 2018 at 08:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/134912045):
well I'm not allowed to add / delete any theorem :P

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Sep 30 2018 at 09:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/134912452):
@**Mario Carneiro** Could you have a look at [the 3 theorems I marked with `try_for`](https://github.com/leanprover-community/mathlib/blob/a58bdb5ab50a3cb2d60e89b326e4f4d7afbf6b05/set_theory/ordinal.lean)?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Sep 30 2018 at 19:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/134929631):
```lean
@[simp] lemma forall₂_nil_left_iff {l} : forall₂ r nil l ↔ l = nil :=
by rw [forall₂_iff]; simp only [eq_self_iff_true, true_and, false_and, and_false, exists_false, or_false]

@[simp] lemma forall₂_nil_left_iff' {l} : forall₂ r nil l ↔ l = nil :=
⟨λ H, by cases H; refl, by rintro rfl; constructor⟩
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Sep 30 2018 at 19:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/134929634):
@**Mario Carneiro** which one do you like more? they take the same time

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Sep 30 2018 at 19:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/134929683):
the original proof was `by rw [forall₂_iff]; simp` so maybe the first one in order to avoid changing too much

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Sep 30 2018 at 19:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/134929728):
I would prefer the one below

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Sep 30 2018 at 23:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/134936006):
I would prefer the one below, although I would use `exact forall2.nil` instead of `constructor` (which has to search through the constructors to apply one)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Oct 01 2018 at 10:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/134957374):
before:
```
cumulative profiling times:
	compilation 85.7ms
	decl post-processing 1.17s
	elaboration 126s
	elaboration: tactic compilation 4.88s
	elaboration: tactic execution 90.9s
	parsing 7.79s
	type checking 145ms
```
after:
```
cumulative profiling times:
        compilation 46.9ms
        decl post-processing 159ms
        elaboration 12.5s
        elaboration: tactic compilation 1.58s
        elaboration: tactic execution 918ms
        parsing 5.4s
        type checking 109ms
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Oct 01 2018 at 11:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/134959164):
Is this `ordinal.lean`?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Oct 01 2018 at 11:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/134959180):
Mario, is all of this making you rethink your writing style?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 01 2018 at 11:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/134959310):
I'm worried about kenny's writing style

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 01 2018 at 11:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/134959318):
I don't want to sacrifice readability here if I can at all help it

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 01 2018 at 11:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/134959332):
but these numbers are hard to argue with

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 01 2018 at 11:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/134959355):
I think in the future we will need to work a post processing step into the workflow, using things like `squeeze_simp`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 01 2018 at 11:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/134959415):
But I *do not* want to be thinking about compile time when I am writing a proof

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 01 2018 at 11:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/134959421):
the mindset is completely different, it is a distraction

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 01 2018 at 11:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/134959496):
@**Mario Carneiro** You are talking like a mathematician.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Oct 01 2018 at 11:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/134959627):
this is data/list/basic.lean

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Oct 03 2018 at 01:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/135070742):
```
$ /c/lean/bin/lean --profile analysis/topology/topological_space.lean >/dev/null
cumulative profiling times:
        compilation 53.6ms
        decl post-processing 52.3ms
        elaboration 6.15s
        elaboration: tactic compilation 929ms
        elaboration: tactic execution 979ms
        parsing 1.24s
        type checking 35.9ms
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Oct 03 2018 at 01:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/135070748):
it was the 7th on my list sorted by time

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Oct 03 2018 at 01:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/135070752):
now it's 6.15 s

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 03 2018 at 06:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/135079880):
@**Kenny Lau** Do you want to PR `faster` in one go or in stages?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 03 2018 at 06:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/135079891):
What does your profile list look like now?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Oct 03 2018 at 08:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/135083606):
https://gist.github.com/kckennylau/f7c6cbfb2aa8bf7e4784e8c65d6c4852

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Oct 03 2018 at 09:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/135085735):
Is it worth PR'ing now? My impression is that Mario will want to check that you didn't do anything he doesn't approve of.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Oct 03 2018 at 09:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/135086194):
I see `uniform_space` may be the next target. You may want to skip that one since Johannes and I are currently working on it (see completions branch in the community fork). Actually part of the file moved to a `completion` file

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Oct 03 2018 at 09:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/135086353):
That's all the more reason to PR now I guess. Kenny did you see if anyone is working on any files you have already changed? This seems like a difficult task -- there are a million branches in community mathlib.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 03 2018 at 09:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/135086430):
The `determinants` PR is touching like 10 basic files.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 03 2018 at 09:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/135086437):
Hopefully git's merging strategies will be smart enough

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Oct 03 2018 at 10:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/135087752):
```quote
I see `uniform_space` may be the next target. You may want to skip that one since Johannes and I are currently working on it (see completions branch in the community fork). Actually part of the file moved to a `completion` file
```
ah well I almost finished. I'll deal with the merging issues then.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Oct 05 2018 at 11:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/135244802):
@**Mario Carneiro** I still haven't finished, but do you want me to PR them (a) one by one when I finish (so you'll have 100 PRs), (b) one by one now (so you'll have 100 PRs distributed across a month), or (c) all in one go (so you'll have 1 big PR)?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Oct 05 2018 at 11:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/135244846):
and 100 is not a hyperbole

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 05 2018 at 13:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/135249251):
I think we shouldn't have one mega-PR. It will only sit and wait and rot and die a silent death.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 05 2018 at 13:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/135249258):
100 PR's on 1 day won't work either.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 05 2018 at 13:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/135249281):
So I think it is best to either have 100 small PR's that appear on a continuous basis. Or chunk them into 20 PR's that take 5 files each.
Just my €0.02

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sean Leather (Oct 05 2018 at 13:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/135249828):
One issue that might influence the choice is whether the feedback from early changes will influence later changes. That is, from the reviewer's PoV, one doesn't want to make the same suggestion in large numbers. So to avoid this, you might start with a few small PRs and, as you get feedback, get them merged, and roll the feedback into later PRs, the PRs can either become larger or stay the same size but go through more easily. My R0.02.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 05 2018 at 13:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/135249991):
My €0.02 are worth R0.34 :lol: https://duckduckgo.com/?q=0.02EUR+in+ZAR&t=ffab&ia=currency

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sean Leather (Oct 05 2018 at 14:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/135250336):
Hmm, I should have given my US$0.02 instead. ([€ $$\approx$$ $!](https://ddg.gg/?q=0.02USD+in+EUR))

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sean Leather (Oct 05 2018 at 14:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/135250366):
Or you could say I'm thrifty...

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Oct 05 2018 at 15:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/135253455):
ok, I'll PR after this one

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Oct 05 2018 at 15:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/135255097):
`sum_sum_index` and friends™ have poor elaboration and often takes up time

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Oct 05 2018 at 15:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/135255398):
and it's worse than `simp` at friends™ because you can't track elaboration

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Oct 05 2018 at 15:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/135255639):
and I even used `calc`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Oct 05 2018 at 15:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/135255642):
```lean
import data.finsupp

open finsupp

variables (α:Type*) (β:Type*) (γ:Type*)

set_option profiler true
def finsupp_prod_equiv [add_comm_monoid γ] [decidable_eq α] [decidable_eq β] [decidable_eq γ] :
  ((α × β) →₀ γ) ≃ (α →₀ (β →₀ γ)) :=
⟨ finsupp.curry, finsupp.uncurry,
  assume f : α × β →₀ γ,
  calc  (f.sum $ λp c, single p.1 (single p.2 c)).sum (λa g, g.sum $ λb c, single (a, b) c)
      = f.sum (λ a b, sum (single a.1 (single a.2 b)) (λ a g, sum g (λ b c, single (a, b) c))) :
    sum_sum_index (λ _, sum_zero_index)
        (λ _ _ _, sum_add_index (λ _, single_zero) (λ _ _ _, single_add))
  ... = sum f (λ a b, sum (single a.2 b) (λ b c, single (a.1, b) c)) :
    congr_arg (sum f) (funext $ λ a, funext $ λ b, sum_single_index sum_zero_index)
  ... = sum f (λ a b, single (a.1, a.2) b) :
    congr_arg (sum f) (funext $ λ a, funext $ λ b, sum_single_index single_zero)
  ... = sum f single :
    congr_arg (sum f) (funext $ λ a, funext $ λ b, congr (congr_arg single prod.mk.eta) rfl)
  ... = f : sum_single,
  assume f, sorry ⟩
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Oct 05 2018 at 15:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/135255644):
MWE ^

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Oct 05 2018 at 16:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/135259451):
```
$ /c/lean/bin/lean --profile data/finsupp.lean >/dev/null
cumulative profiling times:
        compilation 143ms
        decl post-processing 1.9s
        elaboration 7.22s
        elaboration: tactic compilation 548ms
        elaboration: tactic execution 1.79s
        parsing 643ms
        type checking 110ms
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 05 2018 at 16:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/135259496):
Hurray!

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 05 2018 at 16:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/135259677):
@**Kenny Lau** Will you share the total progress after you PR?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 05 2018 at 16:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/135259725):
I know it won't be 70% reduction yet. But I think you took off a massive chunk anyway.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Oct 05 2018 at 17:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/135260053):
Kenny the sooner you PR what you've done so far the better. People like Chris will I think already appreciate your achievements.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Oct 05 2018 at 17:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/135261120):
```quote
@**Kenny Lau** Will you share the total progress after you PR?
```
it's always the same link

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Oct 05 2018 at 17:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/135261122):
https://gist.github.com/kckennylau/f7c6cbfb2aa8bf7e4784e8c65d6c4852

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Oct 05 2018 at 17:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/135262720):
[The PR is live](https://github.com/leanprover/mathlib/pull/391)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 05 2018 at 18:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/135264898):
@**Kenny Lau** I meant some total stats: So the sum of the "before" column, and the sum of the "after" column.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 05 2018 at 18:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/135264908):
I know I could throw your file through `awk`, but maybe you had already done that...

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Oct 05 2018 at 18:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/135266401):
you see, the before column isnt exactly before, and the after column isnt exactly after

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 05 2018 at 18:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/135266463):
I'm asking about *statistics* anyway... so you're allowed to be off by 10%.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Oct 05 2018 at 22:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/135280222):
Here are the new measurements: https://gist.github.com/kckennylau/fd94d8c3a1cd2be9953deffd53657185

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Oct 05 2018 at 22:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/135280312):
total compile time went from 3219 seconds to 3191 seconds

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Oct 05 2018 at 22:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/135280347):
28 seconds improvement!

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Oct 05 2018 at 22:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/135280423):
Impressive. No wonder that guy is the only one to get a personal message in Scott's talk

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Oct 05 2018 at 22:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/135280480):
which guy?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Oct 05 2018 at 22:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/135280580):
You

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Oct 05 2018 at 22:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/135280592):
I guess there is a typo in your numbers

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Oct 05 2018 at 22:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/135280641):
Or I don't understand what you mean, and I should go to bed

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 05 2018 at 22:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/135280699):
those numbers indeed seem unreasonably small compared to your earlier quotes. I thought you had trimmed at least 5 minutes off, what happened or am I not understanding your claim?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Oct 05 2018 at 22:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/135280788):
what happened is that the newly added `data/zmod/quadratic_reciprocity.lean` adds 2 minutes

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Oct 05 2018 at 22:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/135280815):
ha ha you are swimming against the tide. Oh boy.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Oct 05 2018 at 22:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/135280869):
that's what happens when I'm the only one doing all this

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Oct 05 2018 at 22:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/135280877):
what happens when we replace you by a computer?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Oct 05 2018 at 22:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/135280913):
and the newly added `data/padics/padic_numbers.lean` adds 1 minute

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Oct 05 2018 at 22:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/135280978):
`linear_algebra/basic.lean` went from 67.3 to 87.1 despite nothing having been changed, so this might just be a statistical noise

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Oct 05 2018 at 22:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/135280994):
`data/rat.lean` from 55.4 to 78 despite only having a small change

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Oct 05 2018 at 22:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/135281021):
Is there a more reliable way to time these things on average or something?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Oct 05 2018 at 22:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/135281097):
I don't know. All of these times are measured on my computer, which is far from being a constant environment

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Oct 05 2018 at 22:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/135281141):
there might be some statistical methods to make the results more representative of the situation at hand

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Oct 05 2018 at 22:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/135281151):
but I don't study statistics

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Oct 05 2018 at 22:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/135281254):
did you turn off discord?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Oct 05 2018 at 22:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/135281261):
no

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Oct 05 2018 at 22:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/135281333):
one should just look at [this bunch of data produced 9 days ago](https://gist.github.com/kckennylau/f7c6cbfb2aa8bf7e4784e8c65d6c4852) and [this bunch of data produced 1 hour ago](https://gist.github.com/kckennylau/fd94d8c3a1cd2be9953deffd53657185) and make of them what one wills

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 05 2018 at 23:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/135281384):
It's time consuming, but if you want better data you should just run it multiple times, say 3 times and average

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Oct 05 2018 at 23:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/135281467):
that would take me 6 hours, so maybe I'll do this tomorrow

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 05 2018 at 23:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/135281473):
Obviously I wouldn't count any new material in the count. I assume your PR doesn't introduce quadratic reciprocity, you should just compare before/after on the branch

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Oct 05 2018 at 23:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/135281492):
I'll actually compare between the origin/master branch and the lean-community/faster branch, both in the current (i.e. tomorrow) state

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Oct 05 2018 at 23:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/135281494):
how does this sound?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Oct 05 2018 at 23:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/135281542):
(I rebase the `faster` branch constantly to make sure that there are no conflicts with the origin/master branch)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 05 2018 at 23:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/135281561):
that should be fine. For the test you should stop rebasing for a bit, just use master as of the beginning of the test

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Oct 05 2018 at 23:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/135281592):
so you mean origin/master as of now?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Oct 05 2018 at 23:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/135281696):
oh, you mean no rebasing in those 6 hours

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Oct 05 2018 at 23:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/135281723):
Kenny if you send me instructions I can run some timing tests on a faster machine

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Oct 05 2018 at 23:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/135281772):
ok

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Tobias Grosser (Oct 06 2018 at 12:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/135306803):
I did some runs: https://gist.github.com/tobig/86477b42e1cc1d8f8f73666a002edc03

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Tobias Grosser (Oct 06 2018 at 12:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/135306849):
faster is at around 7m10s to 7m30s  vs master at 9m30s to 10m00.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Tobias Grosser (Oct 06 2018 at 12:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/135306852):
On one of our faster servers.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Oct 06 2018 at 12:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/135306914):
thanks

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Tobias Grosser (Oct 06 2018 at 12:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/135306925):
This is around 207m vs 320m single threaded.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 06 2018 at 12:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/135307121):
Well done Kenny! :thumbs_up:

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Oct 06 2018 at 16:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/135313490):
Hi @**Kenny Lau**, I just pushed `squeeze_simp` as a separate branch, as Simon requested.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Oct 06 2018 at 16:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/135313495):
If you'd like, I can rebase your `faster` branch on to that.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 06 2018 at 16:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/135313500):
I guess the current `faster` PR doesn't need it, right?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Oct 06 2018 at 16:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/135313545):
Well, the current `faster` branch includes `squeeze_simp`.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Oct 06 2018 at 16:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/135313549):
It's a bit of a mess, but Simon wanted the tactic PR'd separately from all the library improvements.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 06 2018 at 16:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/135313551):
Sure

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Oct 06 2018 at 16:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/135313552):
Now I should sleep, however.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Oct 07 2018 at 01:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/135330404):
@**Simon Hudon**,  I was  wondering if instead of have `squeeze_simp` be a `tactic unit`, we could have it be a `tactic string`, that also reports the `simp only ...` invocation it found via the return value.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Oct 07 2018 at 01:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/135330408):
The benefit of doing this is that `tidy` already produces "proof scripts", showing the sequence of successful tactics it found.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Oct 07 2018 at 01:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/135330416):
If `tidy` called `squeeze_simp`, then it would automatically generate `simp only ...` lines.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Oct 07 2018 at 03:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/135333526):
Nice! I like the idea. Yes it can do that. I just added an option for inhibiting the printout when nothing would change. I assume that would be detrimental to you. I can create a `tactic` version and an `interactive` version.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Oct 08 2018 at 21:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/135422821):
So this is what I do to each file:
1. Place `set_option profiler true` and `set_option trace.simplify.rewrite true` at the top of the file, and select "checking visible lines and above"
2. Click the name of each theorem to see if it takes too long to compile. (`simp` and `simpa` are the most reliable indicator for proofs that take a long time, but I always check the actual time used to be sure)
3. Then I click on each `simp` to see which simp lemmas are used, and decide what to do:
3a. I can change `simp` to `simp only` and insert all the simp lemmas that are used. Usually `eq_self_iff_true` and `iff_self` are redundant. Sometimes if the lemmas don't involving rewriting under a lambda, I may change it to `rw`, but this actually doesn't save a lot of time.
3b. If I see (with the help of the list of simp lemmas used) that the proof can be written to a short proof in term mode, then I may write it in term mode.
3c. If I see that the simp lemmas are all proved using `rfl`, I will replace the proof with `rfl` to see if it works (surprise, it is not infrequent to see a `rfl` proof being proved by `simp`).
4. And then I make sure that the proof is sped up after my changes.
5. And you can always ask me if you don't know how to deal with a certain theorem.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Oct 08 2018 at 21:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/135422977):
Do you keep a list of the worst offenders?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Oct 08 2018 at 21:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/135423054):
What do you mean?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Oct 08 2018 at 21:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/135423245):
I mean now that you've done all this work, what are the files that eat up most of the compile time

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Oct 08 2018 at 21:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/135423247):
https://gist.github.com/kckennylau/fd94d8c3a1cd2be9953deffd53657185

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Oct 08 2018 at 21:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/135423256):
this is the data as of Oct 05

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 09 2018 at 06:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/135444340):
@**Simon Hudon** You now have experience with git hooks. Can we have a git hook that will disallow commits that import squeeze_simp?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Oct 09 2018 at 07:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/135446493):
Yes, you write a script and you place it in `.git/hooks/` and call it `pre-commit` (no extensions). If you look in that directory, you can see a number of samples already present. They have `.sample` extension

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 09 2018 at 08:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/135447691):
@**Mario Carneiro** Do you think it's worth it to PR such a hook into mathlib?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 09 2018 at 08:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/135447694):
Could also have a hook that checks for end-of-line-whitespace

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 09 2018 at 08:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/135447749):
I think there are a variety of style things you could check

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 09 2018 at 08:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/135448002):
Sure, but I wouldn't mind to offload the more advanced checks to a proper linter.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Oct 09 2018 at 09:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/135449522):
In terms of performances, I think it might be worthwhile to check the import structure and trim the redundant dependencies. I'm still unsure how to do it well though

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 09 2018 at 14:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/135463886):
https://gist.github.com/jcommelin/ab7b99ee1dcd9084e2f73a940e91bb40 is a python script that I hacked together. If we change `squeeze_simp` enough, maybe we can automate the replacement into batch mode.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 09 2018 at 14:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/135463913):
Problem is that if I change `squeeze_simp` to
```lean
meta def squeeze_simp
  (pbegin : parse cur_pos)
  (use_iota_eqn : parse (tk "!")?) (no_dflt : parse only_flag) (hs : parse simp_arg_list)
  (attr_names : parse with_ident_list) (locat : parse location)
  (cfg : parse record_lit?)
  (pend : parse cur_pos) : tactic unit :=
do g ← main_goal,
   (cfg',c) ← parse_config cfg,
   hs' ← hs.mmap arg.to_tactic_format,
   simp use_iota_eqn no_dflt hs attr_names locat cfg',
   g ← instantiate_mvars g,
   let vs := g.list_constant,
   vs ← vs.mfilter (succeeds ∘ has_attribute `simp),
   let use_iota_eqn := if use_iota_eqn.is_some then "!" else "",
   let attrs := if attr_names.empty then "" else string.join (list.intersperse " " (" with" :: attr_names.map to_string)),
   let loc := loc.to_string locat,
   let args := hs' ++ vs.to_list.map to_fmt,
   trace format!"{pbegin.line}:{pbegin.column}:{pend.line}:{pend.column}:simp{use_iota_eqn} only {args}{attrs}{loc}{c}"
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 09 2018 at 14:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/135463953):
And I test with
```lean
example : true :=
begin
  have : 2 + 3 = 3 + 2 := 
  begin
    squeeze_simp -- this is line 105
  end,
  trivial
end
```
I get the output:
```lean
106:2:106:2:simp only [add_comm, eq_self_iff_true, add_right_inj]
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 09 2018 at 14:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/135463971):
So the line:col:line:col coordinates are not very useful atm

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Oct 09 2018 at 18:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/135480544):
Does it help if you add a comma after squeeze_simp?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Oct 10 2018 at 00:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/135503455):
`conv _ in _ etc` is slow

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Oct 10 2018 at 00:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/135503462):
slower than `simp`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Oct 10 2018 at 02:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/135508682):
[2018-10-10.png](/user_uploads/3121/WKTRF2rdqUEt60_Qu8goPD5c/2018-10-10.png)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Oct 10 2018 at 02:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/135508741):
if you do `set_option profiler true` and `set_option trace.simplify.rewrite true` then you can actually see which tactic takes the most time

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Oct 10 2018 at 02:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/135508796):
by observing when the green squiggly line comes up

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Oct 10 2018 at 02:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/135509069):
[2018-10-10-1.png](/user_uploads/3121/8zf8fXTD-Qbb-p_O1hIZTa2a/2018-10-10-1.png)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Oct 10 2018 at 02:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/135509074):
so I changed one line and suddenly the proof takes 20s less to compile

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Oct 10 2018 at 02:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/135509127):
(ok part of it is due to caching, but whatever)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Oct 10 2018 at 08:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/135521322):
```quote
(ok part of it is due to caching, but whatever)
```
Can you get a more robust method for timing?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 10 2018 at 09:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/135524641):
@**Scott Morrison|110087** How long does a full compile of mathlib take on your beast?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Oct 10 2018 at 11:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/135528668):
@**Johan Commelin**  7 min 52 s

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Oct 10 2018 at 11:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/135528937):
(During which 80m24s of core time is being used --- so it managed to average using 10 cores. I see it peak above 20 cores.)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sebastian Ullrich (Oct 10 2018 at 22:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/135566004):
@**Leonardo de Moura** and me just talked a bit about mathlib's performance troubles. Much of this will change in Lean 4 anyway, but it may still be interesting if someone other than us could take a look and profile (using e.g. `perf`) what parts in the C++ code are so slow. Some time ago, @**Gabriel Ebner** profiled that most time is spent in creating the simp lemmas cache from scratch, afair. Is this still the case? Does this mean the cache doesn't work at all, i.e. are subsequent `simp`s still slow even if no simp attributes have been changed in between? If not, might it be worth to e.g. delay and bundle up simp attribute additions where possible, instead of laboriously optimizing the proofs themselves? etc. pp.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 10 2018 at 22:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/135566074):
I am not sure how much of a problem this is at large scale in mathlib, but I think `haveI` and friends just turn off caching altogether, which is pretty bad from a performance standpoint

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 10 2018 at 22:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/135566092):
The semantics I wanted them to have was that `haveI` would clear the cache but not turn it off permanently

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 10 2018 at 22:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/135566171):
there was at least one example of a large proof that had a `haveI` early on and lots of typeclass problems later and it was super slow. I fixed it by breaking out a lemma, but I would prefer to avoid this in many cases

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 10 2018 at 22:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/135566234):
Is it possible to run simp with a prebuilt cache somehow?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sebastian Ullrich (Oct 10 2018 at 22:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/135566338):
I see. I had the impression that most proofs Kenny changed were `simp` one-liners. The typeclass cache story will probably change in Lean 4, but I don't think we want to touch that part before that

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 10 2018 at 22:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/135566361):
they were about 80% simp and 20% typeclass inference

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sebastian Ullrich (Oct 10 2018 at 22:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/135566404):
Ok, good to know

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 10 2018 at 22:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/135566434):
But it could also be that we (I) just use `simp` disproportionately

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sebastian Ullrich (Oct 10 2018 at 22:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/135566435):
```quote
Is it possible to run simp with a prebuilt cache somehow?
```
That should be possible using the tactic primitives, no? E.g. put simp lemma generation in one `timeit` and `simp_core` or whatever it was called in another

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 10 2018 at 22:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/135566447):
i.e. `ring` is slow but I know it is slow and avoid it when possible

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 10 2018 at 22:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/135566500):
If I put two copies of the same theorem one after another, will the second one have a hot simp cache?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 10 2018 at 22:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/135566519):
I guess multithreaded execution causes problems here

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sebastian Ullrich (Oct 10 2018 at 22:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/135566530):
Yeah. You should try running it with `-j0`.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 10 2018 at 22:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/135566539):
There are a lot of files like `multiset` where there are lots of simp proofs, but almost every theorem is also a simp lemma so the cache doesn't stay still

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 10 2018 at 22:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/135566626):
What about running some proofs as though the previous lemmas are added to the bracket list rather than adding them to the default simp set? That way you can chunk up additions to the simp set a bit and decrease the number of rebuilds

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sebastian Ullrich (Oct 10 2018 at 22:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/135566702):
Heh, that's kind of what we want to do in Lean 4. It would definitely be a helpful experiment

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Oct 10 2018 at 22:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/135567209):
It could probably be done with a wrapper around `simp`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Oct 10 2018 at 22:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/135567298):
And I'd use an attribute set on one dummy definition to keep track of the lemmas used in a proof.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Oct 10 2018 at 22:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/135567424):
```quote
What about running some proofs as though the previous lemmas are added to the bracket list rather than adding them to the default simp set? That way you can chunk up additions to the simp set a bit and decrease the number of rebuilds
```
Btw, do you mean the lemmas previously defined or the lemmas previously used?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Oct 10 2018 at 22:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/135567445):
Also, what's the difference between the lemmas in the `simp` brackets and those that are simply in the `simp` list?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Oct 11 2018 at 00:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/135573105):
@**Mario Carneiro** Can I add the following lemma to [`data/rat.lean`](https://github.com/leanprover/mathlib/blob/master/data/rat.lean#L196-L203)?
```lean
@[elab_as_eliminator] theorem {u} num_denom_cases_on'' {C : ℚ → Sort u}
   (a : ℚ) (H : ∀ (n:ℤ) (d:ℤ), d ≠ 0 → C (n /. d)) : C a :=
num_denom_cases_on' a $ λ n d h,
H n d $ int.coe_nat_ne_zero.2 h
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 11 2018 at 04:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/135580682):
Sure. You sure you don't want `d > 0` in the assumptions instead?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Oct 11 2018 at 10:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/135593540):
@**Mario Carneiro** yes, because `add_def` and friends all use `n /. d` with `d \ne 0`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Oct 11 2018 at 10:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/135594056):
well now `mk_nonneg` uses `n /. d` with `d > 0` so can I get another recursor?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Oct 11 2018 at 10:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/135594135):
actually I need `add_def` and `mk_nonneg` at the same time, so maybe I don't need a new recursor, but I would like to have this instead:

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Oct 11 2018 at 10:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/135594154):
```lean
@[elab_as_eliminator] theorem {u} num_denom_cases_on'' {C : ℚ → Sort u}
   (a : ℚ) (H : ∀ (n:ℤ) (d:ℤ), d ≠ 0 → d > 0 → C (n /. d)) : C a :=
num_denom_cases_on' a $ λ n d h,
H n d (int.coe_nat_ne_zero.2 h) (int.coe_nat_pos.2 $ nat.pos_of_ne_zero h)
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Oct 12 2018 at 02:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/135645931):
```
git ls-files *.lean | xargs -I % sh -c '>&2 echo %; /c/lean/bin/lean --profile % >/dev/null;' > profile.txt 2>&1
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Oct 12 2018 at 02:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/135645933):
I'm starting to think that this is the wrong thing to type

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Oct 12 2018 at 02:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/135645935):
somehow it only uses one thread

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Oct 12 2018 at 02:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/135645937):
@**Mario Carneiro** do you know enough bash magic to make it work?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Oct 12 2018 at 02:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/135645949):
or one core. I'm just guessing based on the output

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 12 2018 at 02:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/135646003):
did you try setting the `-j` option of lean?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 12 2018 at 02:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/135646023):
also, your latest version of `num_denom_cases_on''` seems sillier than the last. Is `ne_of_gt` so expensive?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Oct 12 2018 at 02:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/135646035):
well it's long

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 12 2018 at 02:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/135646084):
you have a strange sense of long

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Oct 12 2018 at 02:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/135646095):
you have a strange interpretation of convention

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 12 2018 at 02:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/135646109):
which one?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Oct 12 2018 at 02:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/135646128):
that there can be two conventions

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Oct 12 2018 at 02:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/135646133):
maybe we shouldn't have two conventions to start with

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 12 2018 at 02:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/135646176):
I will defend my right to have exceptions to rules, but I still don't know what you are talking about

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Oct 12 2018 at 02:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/135646188):
that add_def and friends uses "denom ne zero" and mk_nonneg uses "denom > zero"

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 12 2018 at 02:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/135646197):
um... `mk_nonneg` is about nonnegative things

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 12 2018 at 02:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/135646211):
of course it needs to know the inputs are nonnegative

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Oct 12 2018 at 02:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/135646215):
and who thought the original `num_denom_cases_on'` is a good idea despite literally every instance of it needing a fix

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 12 2018 at 02:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/135646269):
I don't see it. It gets used like 20 times immediately afterwards and there are no fixes

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Oct 12 2018 at 02:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/135646286):
by "fix" I mean, wrapper

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 12 2018 at 02:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/135646297):
The fact that `d` is referred to in a `\u` is deliberate

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 12 2018 at 02:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/135646303):
it's a cheap way of saying nonnegative integer without any overhead

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Oct 12 2018 at 02:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/135646339):
but matches none of the theorem's hypothesis

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 12 2018 at 02:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/135646403):
Maybe you are right, most of the theorems don't care that it's nonnegative so having it be an integer is just as well. But in that case I would stick to your first proposal

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Oct 12 2018 at 02:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/135646438):
ok


{% endraw %}
