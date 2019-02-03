---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/18586Whendoesdectrivialfailfordecidableandtrueprops.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [When does dec_trivial fail for decidable and true props?](https://leanprover-community.github.io/archive/113488general/18586Whendoesdectrivialfailfordecidableandtrueprops.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Seul Baek (Nov 11 2018 at 18:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/When%20does%20dec_trivial%20fail%20for%20decidable%20and%20true%20props%3F/near/147484281):
<p>I'm encountering cases where I have a decidable prop <code>p</code> that is also true (which I know because the decidability proof term <code>t : decidable p</code> evaluates to <code>is_true ...</code> when checked with the vm) but <code>exact dec_trivial</code> fails to discharge the goal, with the message </p>
<div class="codehilite"><pre><span></span>exact tactic failed, type mismatch, given expression has type
  true
but is expected to have type
  as_true (p)
</pre></div>


<p>Are there specific conditions under which this happens? I'm guessing that some definitions in the decidability proof term is not unfolding, but I'm not sure why. </p>
<p>This is really strange because it used to work for the exact cases that's broken now. This started happening after I reinstalled mathlib. I wonder if that has anything to do with it.</p>

#### [ Seul Baek (Nov 11 2018 at 20:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/When%20does%20dec_trivial%20fail%20for%20decidable%20and%20true%20props%3F/near/147487874):
<p>More precisely : are there specific kinds of of definitions that might occur in a <code>t : decidable p</code>  that might prevent <code>as_true p</code> from evaluating to <code>true</code>?  I'm trying <code>exact dec_trivial</code> with various other decidable props, and it seems to have no problem reducing <code>as_true p</code> to <code>true</code>for most choices of <code>p</code>, so I'm wondering what's causing the difference.</p>

#### [ Bryan Gin-ge Chen (Nov 11 2018 at 21:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/When%20does%20dec_trivial%20fail%20for%20decidable%20and%20true%20props%3F/near/147489969):
<p>Can you give a minimum (non)working example that illustrates the problem?</p>

#### [ Seul Baek (Nov 11 2018 at 21:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/When%20does%20dec_trivial%20fail%20for%20decidable%20and%20true%20props%3F/near/147490427):
<p><a href="https://github.com/skbaek/qe/blob/master/src/tests.lean" target="_blank" title="https://github.com/skbaek/qe/blob/master/src/tests.lean">https://github.com/skbaek/qe/blob/master/src/tests.lean</a></p>
<p>In the first example </p>
<div class="codehilite"><pre><span></span>example : ∃ (x : int), (x = x) :=
begin
  lia.reify, lia.trim, lia.qelim,
  exact dec_trivial, exact dec_trivial,
end
</pre></div>


<p>the second use of <code>exact dec_trivial</code> fails now, although it used to work. <br>
I'm trying to find a more minimal example that does not require a whole library to reproduce, but I'm having trouble isolating the exact point where it fails</p>

#### [ Seul Baek (Nov 11 2018 at 21:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/When%20does%20dec_trivial%20fail%20for%20decidable%20and%20true%20props%3F/near/147490781):
<p>I think it would be easier to pinpoint the problem if I can see how far lean evaluates <code>as_true p</code> before failing to match it with <code>true</code>.  Are there options for displaying this?</p>

#### [ Mario Carneiro (Nov 11 2018 at 22:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/When%20does%20dec_trivial%20fail%20for%20decidable%20and%20true%20props%3F/near/147491600):
<p>what are the goals there?</p>

#### [ Mario Carneiro (Nov 11 2018 at 22:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/When%20does%20dec_trivial%20fail%20for%20decidable%20and%20true%20props%3F/near/147491631):
<p>Proofs are irreducible, meaning that definitions by well founded recursion will fail to reduce when using <code>dec_trivial</code> or <code>rfl</code></p>

#### [ Seul Baek (Nov 11 2018 at 22:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/When%20does%20dec_trivial%20fail%20for%20decidable%20and%20true%20props%3F/near/147492318):
<p>I didn't use <code>well_founded</code> in any of the definitions, if that's what you mean</p>

#### [ Seul Baek (Nov 13 2018 at 01:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/When%20does%20dec_trivial%20fail%20for%20decidable%20and%20true%20props%3F/near/147561312):
<p>Oh I see what you mean. There was a non-structural recursion hiding in one of the defs</p>

#### [ Seul Baek (Nov 13 2018 at 01:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/When%20does%20dec_trivial%20fail%20for%20decidable%20and%20true%20props%3F/near/147561483):
<p>Hunting these down isn't exactly fun though... a lot of time poring over the text output. Is there some option that displays all defs in a file/folder that use well-founded recursion?</p>


{% endraw %}
