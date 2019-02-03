---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/03873isleftassociative.html
---

## Stream: [general](index.html)
### Topic: [^ is left associative](03873isleftassociative.html)

---


{% raw %}
#### [ Kevin Buzzard (Mar 13 2018 at 16:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%5E%20is%20left%20associative/near/123659529):
<p>Is that normal? <code>#eval 2^3^2</code> gives 64. I don't know any other language where this is the case. I just tried python, pari, sage and they all give me 2^(3^2)=512.</p>

#### [ Kevin Buzzard (Mar 13 2018 at 21:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%5E%20is%20left%20associative/near/123670890):
<p>Wikipedia page on associativity <a href="https://en.wikipedia.org/wiki/Operator_associativity" target="_blank" title="https://en.wikipedia.org/wiki/Operator_associativity">https://en.wikipedia.org/wiki/Operator_associativity</a> explicitly mentions <code>^</code> as being essentially a canonical example of a right associative operator. This is a very bizarre implementation decision. Whatever reason is there for it? <code>(a^b)^c</code> is just <code>a^(b*c)</code> but <code>a^(b^c)</code> cannot be written in any simpler way and is hence the natural choice. Should I file an issue? Is this just an oversight? Should I just fix it and submit a PR?</p>

#### [ Simon Hudon (Mar 13 2018 at 21:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%5E%20is%20left%20associative/near/123670972):
<p>I might be at fault for that issue. As far as I know, I was the first one to commit code for the exponential operator and I think I didn't put much thought into its associativity. It's worth filing an issue. It's also easy to fix so they might be happy if you file a PR that they just have to merge</p>

#### [ Kevin Buzzard (Mar 13 2018 at 21:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%5E%20is%20left%20associative/near/123671027):
<p>We're talking init/data/nat/basic.lean, copyright 2014 Floris van Doora and Leo de Moura</p>

#### [ Andrew Ashworth (Mar 13 2018 at 21:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%5E%20is%20left%20associative/near/123671157):
<p>i think this falls under the nitpicking issues will not be tolerated clause</p>

#### [ Andrew Ashworth (Mar 13 2018 at 21:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%5E%20is%20left%20associative/near/123671166):
<p>:/ but i agree ideally it should be right associative</p>

#### [ Kevin Buzzard (Mar 13 2018 at 21:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%5E%20is%20left%20associative/near/123671419):
<p>:/</p>

#### [ Kevin Buzzard (Mar 13 2018 at 21:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%5E%20is%20left%20associative/near/123671428):
<p>It's not a nitpicking issue, it's a nitpicking PR!</p>

#### [ Kevin Buzzard (Mar 13 2018 at 21:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%5E%20is%20left%20associative/near/123671439):
<p>If it breaks anything, the thing it breaks deserves to be broken!</p>

#### [ Simon Hudon (Mar 13 2018 at 21:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%5E%20is%20left%20associative/near/123671737):
<blockquote>
<p>We're talking init/data/nat/basic.lean, copyright 2014 Floris van Doora and Leo de Moura</p>
</blockquote>
<p>I initially put it in a <code>pow</code> file. They probably merged it with basic and dropped my name</p>

#### [ Sebastian Ullrich (Mar 13 2018 at 22:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%5E%20is%20left%20associative/near/123672684):
<p>Wasn't there a discussion that this should be generalized to a typeclass anyway? If someone PRs those changes, they'll get a "looks good to me" from me.</p>

#### [ Simon Hudon (Mar 13 2018 at 22:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%5E%20is%20left%20associative/near/123673194):
<p>that type class exists in <code>mathlib</code>. It would be great indeed to move it to core. That would remove the operator clash</p>

#### [ Sebastian Ullrich (Mar 13 2018 at 22:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%5E%20is%20left%20associative/near/123673243):
<p>Alternatively, do a PR that removes the notation :P</p>

#### [ Simon Hudon (Mar 13 2018 at 22:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%5E%20is%20left%20associative/near/123673328):
<p>Isn't it used in core?</p>

#### [ Simon Hudon (Mar 13 2018 at 22:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%5E%20is%20left%20associative/near/123673342):
<p>I see that bitvec uses it</p>

#### [ Simon Hudon (Mar 13 2018 at 22:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%5E%20is%20left%20associative/near/123673469):
<p>Is that something that should be moved to <code>mathlib</code>?</p>

#### [ Kevin Buzzard (Mar 13 2018 at 22:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%5E%20is%20left%20associative/near/123673796):
<p>Well so far I have cloned lean, changed <code>infix `^` := pow</code> to <code>infixr `^` := pow</code>, recompiled, and found that <code>#print notation ^</code> still reports <code>_ `^`:80 _:80 := nat.pow #1 #0</code></p>

#### [ Kevin Buzzard (Mar 13 2018 at 22:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%5E%20is%20left%20associative/near/123673800):
<p>I could have made a mistake I guess.</p>

#### [ Kevin Buzzard (Mar 13 2018 at 23:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%5E%20is%20left%20associative/near/123674953):
<p>Ok so I did it again and the same thing happened. Changing line 204 of <code>library/init/data/nat/basic.lean</code> from <code>infix `^` = pow</code> to <code>`infixr </code>^<code> = pow</code> and then compiling lean and feeding a test file into it directly with <code>./lean ~/test.lean</code> still gives me left associativity. Aah well.</p>

#### [ Kevin Buzzard (Mar 13 2018 at 23:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%5E%20is%20left%20associative/near/123675029):
<p>PS It's needed as a map <code>G x Z -&gt; G</code> (G a group, Z the integers), as a map <code>M x N -&gt; M</code> (M a multiplicative monoid, N the naturals) etc. Is a typeclass the best solution? I think Mario explained all this once to me on gitter but I doubt I'll ever find it :-/</p>

#### [ Mario Carneiro (Mar 13 2018 at 23:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%5E%20is%20left%20associative/near/123675077):
<p>Your modification is correct, I think you aren't compiling something</p>

#### [ Kevin Buzzard (Mar 13 2018 at 23:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%5E%20is%20left%20associative/near/123675099):
<p>I'm just cut and pasting from the generic build instructions like a moron</p>

#### [ Kevin Buzzard (Mar 13 2018 at 23:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%5E%20is%20left%20associative/near/123675109):
<p>I surely don't have to use git in any way?</p>

#### [ Kevin Buzzard (Mar 13 2018 at 23:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%5E%20is%20left%20associative/near/123675151):
<p>I am just cloning, editing the file, and then making</p>

#### [ Kevin Buzzard (Mar 13 2018 at 23:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%5E%20is%20left%20associative/near/123675216):
<p>I've done it three times now so I suspect that it's not me failing to edit the file or failing to run the correct binary, I think now that it's more likely either that the generic build instructions are somehow clobbering my edits or that there's something else I'm missing. I've tried defining a new right associative operator to mean nat.pow and it works fine. It's just <code>^</code> that is still misbehaving</p>


{% endraw %}
