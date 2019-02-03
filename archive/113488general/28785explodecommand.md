---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/28785explodecommand.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [explode command](https://leanprover-community.github.io/archive/113488general/28785explodecommand.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Mario Carneiro (Aug 31 2018 at 01:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/explode%20command/near/133093714):
<p>While on the flight home, I decided to actually write the wishlist tactic I've mentioned to a few people, which displays lean proofs in a line by line style heavily annotated with type ascriptions so it looks more like a Fitch style proof. I'm still tweaking the display options, but here's what it looks like right now:</p>
<div class="codehilite"><pre><span></span><span class="kn">import</span> <span class="n">tactic</span><span class="bp">.</span><span class="n">explode</span>
<span class="kn">section</span> <span class="kn">end</span>
<span class="bp">#</span><span class="n">explode</span> <span class="n">iff_true</span>
</pre></div>


<div class="codehilite"><pre><span></span>iff_true : ∀ (a : Prop), a ↔ true ↔ a
0│   │ a              ├ Prop
1│   │ h              │ ┌ a ↔ true
2│   │ trivial        │ │ true
3│1,2│ iff.mpr        │ │ a
4│3  │ ∀I             │ (a ↔ true) → a
5│   │ iff_true_intro │ a → (a ↔ true)
6│4,5│ iff.intro      │ a ↔ true ↔ a
</pre></div>

#### [ Johan Commelin (Aug 31 2018 at 06:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/explode%20command/near/133103016):
<p>Ok, I can parse this, and it looks really helpful... but why is line <code>0</code> at the top, instead of the bottom?</p>

#### [ Mario Carneiro (Aug 31 2018 at 06:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/explode%20command/near/133103024):
<p>it's numbered like lines of proof</p>

#### [ Johan Commelin (Aug 31 2018 at 06:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/explode%20command/near/133103025):
<p>It seems to me that <code>0</code> follows from <code>6</code>, but maybe I misunderstand <code>0</code></p>

#### [ Johan Commelin (Aug 31 2018 at 06:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/explode%20command/near/133103034):
<p>Also, I'd rather read them upside down.</p>

#### [ Mario Carneiro (Aug 31 2018 at 06:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/explode%20command/near/133103036):
<p>lambdas are introduced with the intro variable on top of the bracket</p>

#### [ Johan Commelin (Aug 31 2018 at 06:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/explode%20command/near/133103037):
<p>First split the goal, then you get two subtrees... etc..</p>

#### [ Mario Carneiro (Aug 31 2018 at 06:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/explode%20command/near/133103078):
<p>Yes, I usually read metamath proofs bottom up as well</p>

#### [ Johan Commelin (Aug 31 2018 at 06:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/explode%20command/near/133103081):
<p>Aaah, that is what <code>0</code> is doing, of course!</p>

#### [ Johan Commelin (Aug 31 2018 at 06:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/explode%20command/near/133103084):
<p>Well... there is a solution to that: have <code>#explode</code> reverse the order...</p>

#### [ Johan Commelin (Aug 31 2018 at 06:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/explode%20command/near/133103085):
<p>But now I see that <code>0</code> should remain at the top.</p>

#### [ Johan Commelin (Aug 31 2018 at 06:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/explode%20command/near/133103087):
<p>So it's not that easy...</p>

#### [ Mario Carneiro (Aug 31 2018 at 06:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/explode%20command/near/133103088):
<p>I suppose, but that will get confusing to explain to people</p>

#### [ Mario Carneiro (Aug 31 2018 at 06:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/explode%20command/near/133103099):
<p>I would prefer a forward proof ordering on the page</p>

#### [ Mario Carneiro (Aug 31 2018 at 06:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/explode%20command/near/133103103):
<p>even if your interest is drawn from the bottom up</p>

#### [ Johan Commelin (Aug 31 2018 at 06:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/explode%20command/near/133103114):
<p>How far is this representation from writing a <code>begin end</code> proof?</p>

#### [ Johan Commelin (Aug 31 2018 at 06:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/explode%20command/near/133103115):
<p>Could you generate that as well?</p>

#### [ Mario Carneiro (Aug 31 2018 at 06:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/explode%20command/near/133103152):
<p>what do you mean?</p>

#### [ Mario Carneiro (Aug 31 2018 at 06:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/explode%20command/near/133103157):
<p>like you want the lines to correspond to <code>apply</code> and <code>intro</code>?</p>

#### [ Johan Commelin (Aug 31 2018 at 06:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/explode%20command/near/133103162):
<p>Right.</p>

#### [ Johan Commelin (Aug 31 2018 at 06:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/explode%20command/near/133103166):
<p><code>#deobfuscate</code></p>

#### [ Mario Carneiro (Aug 31 2018 at 06:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/explode%20command/near/133103181):
<p>it's pretty close, there are some edge cases where you see explicit <code>∀E</code> and <code>∀I</code> steps</p>

#### [ Johan Commelin (Aug 31 2018 at 06:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/explode%20command/near/133103233):
<p>Even if it isn't perfect, I'dd really like it.</p>

#### [ Mario Carneiro (Aug 31 2018 at 06:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/explode%20command/near/133103257):
<p>can you mockup?</p>

#### [ Johan Commelin (Aug 31 2018 at 06:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/explode%20command/near/133103303):
<p>What do you mean? This example? Or more general?</p>

#### [ Mario Carneiro (Aug 31 2018 at 06:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/explode%20command/near/133103369):
<p>either, something that shows off what you would like to see</p>

#### [ Johan Commelin (Aug 31 2018 at 06:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/explode%20command/near/133103381):
<p>Rob has this interface with mathematica... with certain terms corresponding to certain mathematica terms</p>

#### [ Johan Commelin (Aug 31 2018 at 06:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/explode%20command/near/133103392):
<p>So we could also have a dictionary <code>\lam &lt;-&gt; intros</code> etc...</p>

#### [ Johan Commelin (Aug 31 2018 at 06:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/explode%20command/near/133103394):
<p>But I don't have a clear picture how to actually implement this</p>

#### [ Mario Carneiro (Aug 31 2018 at 06:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/explode%20command/near/133103440):
<p>oh, there is a potential problem with making a real runnable proof script, as opposed to just a display like this... it has to parse as valid lean, and sometimes <code>pp</code> doesn't give good results</p>

#### [ Mario Carneiro (Aug 31 2018 at 06:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/explode%20command/near/133103451):
<p>I am currently hiding non proof terms in <code>#explode</code>, but probably this won't work in a proof script</p>

#### [ Johan Commelin (Aug 31 2018 at 06:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/explode%20command/near/133103511):
<div class="codehilite"><pre><span></span>iff_true : ∀ (a : Prop), a ↔ true ↔ a
0│   │ a              ├ Prop            | intro (intros?)
1│   │ h              │ ┌ a ↔ true      | intro (intros?)
2│   │ trivial        │ │ true          | exact trivial
3│1,2│ iff.mpr        │ │ a             | apply iff.mpr
4│3  │ ∀I             │ (a ↔ true) → a  | ???
5│   │ iff_true_intro │ a → (a ↔ true)  | exact iff_true_intro
6│4,5│ iff.intro      │ a ↔ true ↔ a    | apply iff.intro (split?)
</pre></div>

#### [ Johan Commelin (Aug 31 2018 at 06:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/explode%20command/near/133103558):
<p>I just added an extra column, and it totally wouldn't run.</p>

#### [ Mario Carneiro (Aug 31 2018 at 06:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/explode%20command/near/133103567):
<p>I guess part of the problem with line for line translating this display into a proof script is that forward proving is less natural</p>

#### [ Mario Carneiro (Aug 31 2018 at 06:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/explode%20command/near/133103572):
<p>you have to use lots of <code>have</code></p>

#### [ Johan Commelin (Aug 31 2018 at 06:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/explode%20command/near/133103577):
<p>Right</p>

#### [ Mario Carneiro (Aug 31 2018 at 06:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/explode%20command/near/133103584):
<p>and the positioning of the <code>intro</code> is weird</p>

#### [ Mario Carneiro (Aug 31 2018 at 06:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/explode%20command/near/133103676):
<p>The hard stuff is when dealing with <code>eq.rec</code> though</p>
<div class="codehilite"><pre><span></span>iff_not_comm : ∀ {a b : Prop} [_inst_1 : decidable a] [_inst_2 : decidable b], a ↔ ¬b ↔ (b ↔ ¬a)
0 │     │ a            ├ Prop
1 │     │ b            ├ Prop
2 │     │ _inst_1      ├ decidable a
3 │     │ _inst_2      ├ decidable b
4 │     │ eq.refl      │ (a ↔ ¬b ↔ (b ↔ ¬a)) = (a ↔ ¬b ↔ (b ↔ ¬a))
5 │     │ iff_def      │ a ↔ ¬b ↔ (a → ¬b) ∧ (¬b → a)
6 │5    │ propext      │ (a ↔ ¬b) = ((a → ¬b) ∧ (¬b → a))
7 │4,6  │ eq.rec       │ (a ↔ ¬b ↔ (b ↔ ¬a)) = ((a → ¬b) ∧ (¬b → a) ↔ (b ↔ ¬a))
8 │7    │ id           │ (a ↔ ¬b ↔ (b ↔ ¬a)) = ((a → ¬b) ∧ (¬b → a) ↔ (b ↔ ¬a))
9 │     │ eq.refl      │ ((a → ¬b) ∧ (¬b → a) ↔ (b ↔ ¬a)) = ((a → ¬b) ∧ (¬b → a) ↔ (b ↔ ¬a))
10│     │ iff_def      │ b ↔ ¬a ↔ (b → ¬a) ∧ (¬a → b)
11│10   │ propext      │ (b ↔ ¬a) = ((b → ¬a) ∧ (¬a → b))
12│9,11 │ eq.rec       │ ((a → ¬b) ∧ (¬b → a) ↔ (b ↔ ¬a)) = ((a → ¬b) ∧ (¬b → a) ↔ (b → ¬a) ∧ (¬a → b))
13│12   │ id           │ ((a → ¬b) ∧ (¬b → a) ↔ (b ↔ ¬a)) = ((a → ¬b) ∧ (¬b → a) ↔ (b → ¬a) ∧ (¬a → b))
14│     │ imp_not_comm │ a → ¬b ↔ b → ¬a
15│     │ not_imp_comm │ ¬b → a ↔ ¬a → b
16│14,15│ and_congr    │ (a → ¬b) ∧ (¬b → a) ↔ (b → ¬a) ∧ (¬a → b)
17│13,16│ eq.mpr       │ (a → ¬b) ∧ (¬b → a) ↔ (b ↔ ¬a)
18│8,17 │ eq.mpr       │ a ↔ ¬b ↔ (b ↔ ¬a)
</pre></div>

#### [ Reid Barton (Aug 31 2018 at 08:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/explode%20command/near/133105985):
<p>You should make a version which outputs those judgment tree things and outputs LaTeX</p>

#### [ Patrick Massot (Aug 31 2018 at 09:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/explode%20command/near/133108796):
<p>Noooo! We triggered Mario's immune defenses. He spent three days with people who want Lean to prove everything by itself, he merged tidy and then, flying back, he wrote the Lean2metamath tactic!</p>

#### [ Kevin Buzzard (Aug 31 2018 at 14:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/explode%20command/near/133121291):
<p>"On the flight home, I wrote an explode command" = "I just risked getting the plane diverted because the guy next to me panicked"</p>

#### [ Mario Carneiro (Aug 31 2018 at 14:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/explode%20command/near/133121314):
<p>I originally called it <code>mmshow</code> but I decided against metamath branding it</p>


{% endraw %}
