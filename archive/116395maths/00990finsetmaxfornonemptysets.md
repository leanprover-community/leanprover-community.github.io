---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/00990finsetmaxfornonemptysets.html
---

## Stream: [maths](index.html)
### Topic: [finset.max for nonempty sets](00990finsetmaxfornonemptysets.html)

---


{% raw %}
#### [ Kevin Buzzard (Jan 23 2019 at 20:29)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/finset.max%20for%20nonempty%20sets/near/156716988):
<p>I've been trying to use <code>finset.max</code> and it's a bit annoying in all my use cases because it takes in an arbitrary finset X and returns an option X (to deal with the case where the finset is empty). It would be very easy to write a variant which takes a non-empty finset and returns its max, and I find myself wanting this variant. What should I call it?</p>

#### [ Kenny Lau (Jan 23 2019 at 20:30)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/finset.max%20for%20nonempty%20sets/near/156717153):
<p>you want to write a partial function? <span aria-label="shock" class="emoji emoji-1f628" role="img" title="shock">:shock:</span></p>

#### [ Kevin Buzzard (Jan 23 2019 at 20:31)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/finset.max%20for%20nonempty%20sets/near/156717184):
<p>And is there room for it in finset.lean?</p>

#### [ Kenny Lau (Jan 23 2019 at 20:31)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/finset.max%20for%20nonempty%20sets/near/156717213):
<p>I think <code>finset.sup</code> might be what you seek</p>

#### [ Kevin Buzzard (Jan 23 2019 at 20:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/finset.max%20for%20nonempty%20sets/near/156717335):
<p>It's not that either, because <code>finset.sup</code> wants the lattice to have a bot, and in my use case there is no bot.</p>

#### [ Kenny Lau (Jan 23 2019 at 20:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/finset.max%20for%20nonempty%20sets/near/156717357):
<p>so you really want a partial function <span aria-label="shock" class="emoji emoji-1f628" role="img" title="shock">:shock:</span></p>

#### [ Kevin Buzzard (Jan 23 2019 at 20:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/finset.max%20for%20nonempty%20sets/near/156717365):
<p>I simply want a function which takes in a non-empty finite set of reals and produces its max.</p>

#### [ Kevin Buzzard (Jan 23 2019 at 20:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/finset.max%20for%20nonempty%20sets/near/156717381):
<p>I am happy to supply the proof that it's non-empty.</p>

#### [ Kevin Buzzard (Jan 23 2019 at 20:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/finset.max%20for%20nonempty%20sets/near/156717521):
<p>Surely there will be more use cases. Kenny this is for proving that a convergent sequence of reals is bounded. Working with the option is a pain, because I simply want the answer rather than having to keep talking about elements of the option output.</p>

#### [ Kevin Buzzard (Jan 23 2019 at 20:36)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/finset.max%20for%20nonempty%20sets/near/156717730):
<p>Is <code>finset.max'</code> a crap name?</p>

#### [ Kevin Buzzard (Jan 23 2019 at 20:39)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/finset.max%20for%20nonempty%20sets/near/156717989):
<p>Ultimately it will be easier to use than the contortions I'm having to go through to prove the results I need about finset.max. Kenny, try proving that if <code>f : nat -&gt; real</code> and B = max {f 0, f 1, f 2}` then for all i &lt;= 2, f i &lt;= B. I had to extract B from the option and then prove that it was in the option and it clutters up the local context -- both of these could be avoided because the fact that f 0 is in the set is easy to prove. I think my proposal makes it easier, but I might be wrong because it's only just occurred to me.</p>

#### [ Chris Hughes (Jan 23 2019 at 20:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/finset.max%20for%20nonempty%20sets/near/156718137):
<p>You can use <code>option.get </code></p>

#### [ Johannes Hölzl (Jan 23 2019 at 20:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/finset.max%20for%20nonempty%20sets/near/156718312):
<p>No, Kevin wants <code>option.iget</code>. Or a max version which assumes <code>inhabited</code>.</p>

#### [ Johan Commelin (Jan 23 2019 at 20:56)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/finset.max%20for%20nonempty%20sets/near/156719527):
<p>So we should fix ourselves a <code>finset.imax</code>?</p>

#### [ Johan Commelin (Jan 23 2019 at 20:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/finset.max%20for%20nonempty%20sets/near/156719571):
<p><code>iget</code> and <code>imax</code> sound like they were invented by Apple. <span aria-label="sad" class="emoji emoji-2639" role="img" title="sad">:sad:</span></p>

#### [ Kevin Buzzard (Jan 23 2019 at 21:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/finset.max%20for%20nonempty%20sets/near/156723283):
<p>I don't want to keep applying iget, I know the set is nonempty and I just want the max :-) There seem to be more contortions using what is there already. I should try writing the code and see if it's actually better.</p>

#### [ Kevin Buzzard (Jan 23 2019 at 22:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/finset.max%20for%20nonempty%20sets/near/156725776):
<p>rofl I decided to call it <code>finset.max'</code> and then I discovered it was there already :-)</p>

#### [ Kevin Buzzard (Jan 23 2019 at 22:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/finset.max%20for%20nonempty%20sets/near/156725955):
<p>Johannes put it there in October!</p>

#### [ Patrick Massot (Jan 23 2019 at 22:17)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/finset.max%20for%20nonempty%20sets/near/156726063):
<p>One day I taught Simon what was <code>convert</code>. At some point in the history section of the explanation, I was forced to mention that Simon himself wrote that tactic.</p>

#### [ Kevin Buzzard (Jan 23 2019 at 22:17)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/finset.max%20for%20nonempty%20sets/near/156726084):
<p>I see, the point is that <code>max'</code> wants a proof that <code>S ≠ ∅</code>, perhaps Johannes could see that I wanted something a bit more convenient.</p>

#### [ Mario Carneiro (Jan 24 2019 at 02:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/finset.max%20for%20nonempty%20sets/near/156740020):
<p>I am 100% on board with having <code>finset.imax</code> defined and including the obvious lemmas. (Johan, I don't think you can patent single letter prefixes.) I agree you shouldn't deal with <code>(finset.max s).iget</code>, there should be a definition for this combination.</p>

#### [ Kevin Buzzard (Jan 24 2019 at 08:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/finset.max%20for%20nonempty%20sets/near/156753780):
<p>So I'm currently using <code>finset.max'</code> and it's fine</p>


{% endraw %}
