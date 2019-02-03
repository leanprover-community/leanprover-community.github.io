---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113489newmembers/30462Timeoutwiththemathematicalbrackets.html
---

## Stream: [new members](index.html)
### Topic: [Time out with the mathematical brackets](30462Timeoutwiththemathematicalbrackets.html)

---


{% raw %}
#### [ AHan (Nov 04 2018 at 05:11)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Time%20out%20with%20the%20mathematical%20brackets/near/137141051):
<p>I've defined a prime field, and tried to define a function that maps <code>int</code> to<code>pf</code>, but somehow timeout at the function...</p>
<div class="codehilite"><pre><span></span>def pf {p : ℕ} := {e // prime p ∧ 0 ≤ e ∧ e &lt; p}

variable {p : ℕ}

def int_to_pf (x : ℤ) : @pf p := ⟨x, begin end⟩
</pre></div>


<p>while my friend succeed with</p>
<div class="codehilite"><pre><span></span>def pf (p  : ℕ ) [prime p] := {e // 0 ≤ e ∧ e &lt; p}

variable p : ℕ
variable [pp: prime p]

def int_to_pf (x : ℤ) : @pf p (prime p) :=  ⟨x, begin end⟩
</pre></div>


<p>Why is there a difference?</p>

#### [ Mario Carneiro (Nov 04 2018 at 05:34)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Time%20out%20with%20the%20mathematical%20brackets/near/137141678):
<p>you are casting an <code>int</code> to a <code>nat</code> in both examples, this times out searching for a coercion</p>

#### [ Mario Carneiro (Nov 04 2018 at 05:36)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Time%20out%20with%20the%20mathematical%20brackets/near/137141733):
<p>In the second example it fails fast only because it gets stuck in the type of the theorem: <code>@pf p (prime p)</code> is not well typed because <code>prime p</code> does not have type <code>prime p</code></p>

#### [ AHan (Nov 04 2018 at 05:41)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Time%20out%20with%20the%20mathematical%20brackets/near/137141838):
<p>sorry for a mistake, I think my friend wrote</p>
<div class="codehilite"><pre><span></span>pp: prime p
def int_to_pf (x : ℤ) : @pf p pp ...
</pre></div>

#### [ AHan (Nov 04 2018 at 05:42)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Time%20out%20with%20the%20mathematical%20brackets/near/137141882):
<p>Where did I cast int to nat?<br>
Aren't elements in pf all have value of type nat?</p>

#### [ Andrew Ashworth (Nov 04 2018 at 07:04)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Time%20out%20with%20the%20mathematical%20brackets/near/137144099):
<p>Your x in int to pf is an int?</p>

#### [ AHan (Nov 04 2018 at 07:24)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Time%20out%20with%20the%20mathematical%20brackets/near/137144602):
<p>yes, but aren't val of elements of type pf also int?</p>

#### [ Andrew Ashworth (Nov 04 2018 at 07:30)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Time%20out%20with%20the%20mathematical%20brackets/near/137144763):
<p>You defined p in pf as a nat</p>

#### [ AHan (Nov 04 2018 at 07:39)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Time%20out%20with%20the%20mathematical%20brackets/near/137144977):
<p>But the second example can work?</p>

#### [ Mario Carneiro (Nov 04 2018 at 07:51)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Time%20out%20with%20the%20mathematical%20brackets/near/137145287):
<p>lean does not have a subtyping relation, so if something has type <code>pf p</code> it does not have type <code>int</code>. But more importantly you are going the other way around here: <code>x</code> has type <code>int</code> and you are putting it in the first component of <code>pf p</code>, which you didn't write explicitly (it is the type of <code>e</code>) but is <code>nat</code>.</p>

#### [ AHan (Nov 04 2018 at 07:59)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Time%20out%20with%20the%20mathematical%20brackets/near/137145499):
<p>Oh!! Got it! thanks a lot!!</p>


{% endraw %}
