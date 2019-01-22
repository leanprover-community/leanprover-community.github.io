---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/28164silentoverflow.html
---

## [general](index.html)
### [silent overflow](28164silentoverflow.html)

#### [Kevin Buzzard (Apr 09 2018 at 18:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/silent%20overflow/near/124842273):
```lean
#check id -- all seems fine

example : 1000 * 1000 = 123456 := rfl -- no error reported

#check id -- all still seems fine
```

#### [Kevin Buzzard (Apr 09 2018 at 18:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/silent%20overflow/near/124842287):
changing `example` to `theorem X` shows that there is a problem

#### [Kevin Buzzard (Apr 09 2018 at 18:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/silent%20overflow/near/124842294):
` deep recursion was detected at 'replace' (potential solution: increase stack space in your system) `

#### [Kevin Buzzard (Apr 09 2018 at 18:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/silent%20overflow/near/124842302):
but the error is not triggered if we use `example`

#### [Kenny Lau (Apr 09 2018 at 18:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/silent%20overflow/near/124842353):
no error reported!

#### [Kevin Buzzard (Apr 09 2018 at 18:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/silent%20overflow/near/124842357):
Changing example to theorem also gives us the ` not a rfl-lemma, even though marked as rfl ` error

#### [Kevin Buzzard (Apr 09 2018 at 18:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/silent%20overflow/near/124842368):
and perhaps this is relevant

#### [Kevin Buzzard (Apr 09 2018 at 18:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/silent%20overflow/near/124842378):
because `example : 1000  *  1000  =  123456  :=  by refl` gives the recursion error

#### [Kevin Buzzard (Apr 09 2018 at 18:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/silent%20overflow/near/124842389):
no error reported! So maybe we can prove 0=1

#### [Kevin Buzzard (Apr 09 2018 at 18:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/silent%20overflow/near/124842394):
but it's hard to work with

#### [Kevin Buzzard (Apr 09 2018 at 18:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/silent%20overflow/near/124842396):
I guess proving 1000000 = 123456 is just as good

#### [Kevin Buzzard (Apr 09 2018 at 18:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/silent%20overflow/near/124842398):
Do you know how to run this through Lean with max paranoia options on?

#### [Kevin Buzzard (Apr 09 2018 at 18:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/silent%20overflow/near/124842637):
```
buzzard@bob:~$ more wrong.lean 
example : 1000 * 1000 = 123456 := rfl -- no error reported
buzzard@bob:~$ lean --trust=0 wrong.lean 
buzzard@bob:~$ 
```

#### [Kevin Buzzard (Apr 09 2018 at 18:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/silent%20overflow/near/124842681):
looks good to me

#### [Kevin Buzzard (Apr 09 2018 at 18:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/silent%20overflow/near/124842908):
dammit `example : 0 = 1 := @nat.add_left_cancel (1000 * 1000) 0 1 rfl
` doesn't work :-(

#### [Kevin Buzzard (Apr 09 2018 at 18:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/silent%20overflow/near/124842921):
you get the recursion error

#### [Kevin Buzzard (Apr 09 2018 at 18:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/silent%20overflow/near/124843274):
```lean
theorem W : 0 = 1 → false := dec_trivial 

theorem X : 1000 * 1000 + 0 = 1000 * 1000 + 1 → false := λ H, W (nat.add_left_cancel H)

example : 1000 * 1000 + 0 = 1000 * 1000 + 1 := rfl -- no problem

example : false := X rfl -- recursion error

```

#### [Kevin Buzzard (Apr 09 2018 at 18:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/silent%20overflow/near/124843311):
so near and yet so far

#### [Kevin Buzzard (Apr 09 2018 at 18:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/silent%20overflow/near/124843350):
" As far as we know, no proof of `false` has ever been accepted by Lean when using `-t0`. " (from the FAQ)

#### [Kenny Lau (Apr 09 2018 at 18:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/silent%20overflow/near/124843354):
who is `-t0`?

#### [Kevin Buzzard (Apr 09 2018 at 18:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/silent%20overflow/near/124843359):
same as `--trust 0`

#### [Kevin Buzzard (Apr 09 2018 at 18:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/silent%20overflow/near/124843363):
"trust no-one"

#### [Kevin Buzzard (Apr 09 2018 at 18:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/silent%20overflow/near/124843411):
`0 means do not trust any macro, and type check all imported modules`

#### [Kevin Buzzard (Apr 09 2018 at 18:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/silent%20overflow/near/124843433):
My session earlier had Lean accepting wrong.lean even at `-t0` but it's not a proof of false, it's just a proof of something which is false :-)

#### [Kevin Buzzard (Apr 09 2018 at 18:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/silent%20overflow/near/124843442):
well, AFAIK it's false

#### [Gabriel Ebner (Apr 09 2018 at 18:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/silent%20overflow/near/124843924):
This would be really awesome, but I get an error:
```
type mismatch, term
  rfl
has type
  ?m_2 = ?m_2
but is expected to have type
  1000 * 1000 + 0 = 1000 * 1000 + 1
```

#### [Kevin Buzzard (Apr 09 2018 at 18:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/silent%20overflow/near/124843933):
ooh

#### [Kevin Buzzard (Apr 09 2018 at 18:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/silent%20overflow/near/124843973):
so maybe there's a problem with my set-up

#### [Kevin Buzzard (Apr 09 2018 at 18:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/silent%20overflow/near/124843980):
```
$ lean --version
Lean (version 3.3.1, nightly-2018-04-06, commit 8f55ec4c5037, Release)
```

#### [Kevin Buzzard (Apr 09 2018 at 18:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/silent%20overflow/near/124843982):
Ubuntu 16.04

#### [Kevin Buzzard (Apr 09 2018 at 18:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/silent%20overflow/near/124843985):
mathlib HEAD

#### [Kevin Buzzard (Apr 09 2018 at 18:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/silent%20overflow/near/124843992):
Nothing to do with VS Code because I can reproduce on the command line

#### [Sebastian Ullrich (Apr 09 2018 at 18:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/silent%20overflow/near/124844000):
I can reproduce the issue

#### [Gabriel Ebner (Apr 09 2018 at 18:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/silent%20overflow/near/124844011):
I now see it with the nightly as well, but not with my git build from master..

#### [Sebastian Ullrich (Apr 09 2018 at 18:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/silent%20overflow/near/124844059):
...using my git build :)

#### [Kevin Buzzard (Apr 09 2018 at 18:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/silent%20overflow/near/124844068):
Let me know if you want me to open an issue

#### [Sebastian Ullrich (Apr 09 2018 at 18:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/silent%20overflow/near/124844077):
...in release mode, could be relevant

#### [Gabriel Ebner (Apr 09 2018 at 18:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/silent%20overflow/near/124844096):
I'm always running relwithdebinfo.

#### [Sebastian Ullrich (Apr 09 2018 at 19:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/silent%20overflow/near/124845066):
@**Gabriel Ebner** Some initial observations:
1) the exception is not reported by [check_example](https://github.com/leanprover/lean/blob/bdea7d420dbcdb7cce700eb62c129387707016fc/src/frontends/lean/definition_cmds.cpp#L711) because `stack_space_exception` is not a `lean::exception`
2) It's then caught by [task_queue::execute](https://github.com/leanprover/lean/blob/69322cd523e4087530af7cefe3198a1315f6379d/src/util/task.cpp#L60) but never reported, apparently

#### [Gabriel Ebner (Apr 09 2018 at 19:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/silent%20overflow/near/124845166):
Yeah, `task_queue::execute` doesn't report errors.

#### [Gabriel Ebner (Apr 09 2018 at 19:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/silent%20overflow/near/124845241):
I guess we should catch all exceptions in `check_example` to be consistent with `add` in `module.cpp`.

#### [Gabriel Ebner (Apr 09 2018 at 19:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/silent%20overflow/near/124845319):
I can now reproduce the error as well.  It just takes a slightly larger number:
```lean
example : 1000*1000*100 + 0 = 1000*1000*100 + 1 := rfl -- no problem
```

#### [Sebastian Ullrich (Apr 09 2018 at 19:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/silent%20overflow/near/124845399):
Surely we should try and report the caught exception at some point...?

#### [Gabriel Ebner (Apr 09 2018 at 19:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/silent%20overflow/near/124845410):
Yes, in `check_example`.  We just need to add `std::` in front of the exception, and add a second catch-all `...` case like in `add`.

#### [Sebastian Ullrich (Apr 09 2018 at 19:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/silent%20overflow/near/124845431):
That too, but the task_queue shouldn't just swallow exceptions silently

#### [Gabriel Ebner (Apr 09 2018 at 19:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/silent%20overflow/near/124845501):
~~Mmh, good point.  At least some debugging output on stderr would be good.  For exceptions inheriting `std::exception` we can even print the error message.~~

#### [Gabriel Ebner (Apr 09 2018 at 19:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/silent%20overflow/near/124845565):
That won't work, many tasks end in an exceptional state.  And these exceptions are eventually reported.  We wouldn't want to print something to stderr for every red squiggle the user sees.

#### [Gabriel Ebner (Apr 09 2018 at 19:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/silent%20overflow/near/124845579):
This is similar to the failed promise issue in javascript.  There, a promise can also fail without throwing an exception or printing anything, you only get notified of the error if you listen to it.

#### [Sebastian Ullrich (Apr 09 2018 at 19:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/silent%20overflow/near/124845952):
In the sane promise APIs I know, not extracting the exception will make the promise throw it in its destructor. Which may kill the process if the exception is not caught in a background thread.

#### [Sebastian Ullrich (Apr 09 2018 at 19:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/silent%20overflow/near/124845954):
We could do the same

