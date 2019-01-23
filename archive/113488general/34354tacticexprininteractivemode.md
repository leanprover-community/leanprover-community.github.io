---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/34354tacticexprininteractivemode.html
---

## Stream: [general](index.html)
### Topic: [`tactic expr` in interactive mode](34354tacticexprininteractivemode.html)

---


{% raw %}
#### [ Scott Morrison (Aug 02 2018 at 16:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%60tactic%20expr%60%20in%20interactive%20mode/near/130780443):
Say I have a `tactic expr`. If I'm in interactive mode, how do I invoke it and assign the result to a named hypothesis?

#### [ Scott Morrison (Aug 02 2018 at 16:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%60tactic%20expr%60%20in%20interactive%20mode/near/130780624):
e.g.
````
meta def J : tactic expr := to_expr ``(5)
example : false :=
begin
 have j := /- execute J here -/ sorry,
end
````

#### [ Scott Morrison (Aug 02 2018 at 16:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%60tactic%20expr%60%20in%20interactive%20mode/near/130780759):
Maybe it's the wrong time of day for tactic questions, too many mathematicians are awake. :-)

#### [ Johan Commelin (Aug 02 2018 at 16:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%60tactic%20expr%60%20in%20interactive%20mode/near/130780842):
Maybe it's the wrong time of day for ~~tactic~~ questions...
It is `> body.temp` over here. Although aussies might be used to this...

#### [ Patrick Massot (Aug 02 2018 at 16:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%60tactic%20expr%60%20in%20interactive%20mode/near/130780892):
I'd love to help you but my children insist it's time  to go to the beach

#### [ Scott Morrison (Aug 02 2018 at 16:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%60tactic%20expr%60%20in%20interactive%20mode/near/130780959):
Have fun at the beach. :-) Winter here!

#### [ Rob Lewis (Aug 02 2018 at 16:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%60tactic%20expr%60%20in%20interactive%20mode/near/130781162):
```
example : false :=
begin
 have j := by J >>= tactic.exact,
 let j' := by J >>= tactic.exact,
end
```

#### [ Rob Lewis (Aug 02 2018 at 16:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%60tactic%20expr%60%20in%20interactive%20mode/near/130781187):
`let` instead of `have` will give you access to the value of your tactic, maybe necessary if the expr isn't a proof.

#### [ Scott Morrison (Aug 02 2018 at 16:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%60tactic%20expr%60%20in%20interactive%20mode/near/130781526):
Thanks!

#### [ Scott Morrison (Aug 02 2018 at 16:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%60tactic%20expr%60%20in%20interactive%20mode/near/130781551):
Now going the other way: if I have a named hypothesis and I want to get hold of an `expr`?

#### [ Rob Lewis (Aug 02 2018 at 16:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%60tactic%20expr%60%20in%20interactive%20mode/near/130781619):
`tactic.get_local`?

#### [ Scott Morrison (Aug 03 2018 at 04:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%60tactic%20expr%60%20in%20interactive%20mode/near/130812539):
Thanks @Rob, that does it.

#### [ Scott Morrison (Aug 03 2018 at 04:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%60tactic%20expr%60%20in%20interactive%20mode/near/130812580):
Now I want to get the 'other half' of a hypothesis. Say I have `h : t := p` amongst my hypotheses. How do I produce `p` as an `expr`?

#### [ Simon Hudon (Aug 03 2018 at 05:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%60tactic%20expr%60%20in%20interactive%20mode/near/130814956):
This might help: 

https://github.com/unitb/lean-lib/blob/master/src/util/meta/tactic/basic.lean#L16-L21

#### [ Sebastian Ullrich (Aug 03 2018 at 05:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%60tactic%20expr%60%20in%20interactive%20mode/near/130815320):
Heh, nice workaround

#### [ Scott Morrison (Aug 03 2018 at 06:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%60tactic%20expr%60%20in%20interactive%20mode/near/130817156):
Thanks, that works. Still struggling with my bigger problem, but that was helpful!

#### [ Simon Hudon (Aug 03 2018 at 08:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%60tactic%20expr%60%20in%20interactive%20mode/near/130821219):
Let us know what the bigger problem is. I'll have a look when I wake up


{% endraw %}
