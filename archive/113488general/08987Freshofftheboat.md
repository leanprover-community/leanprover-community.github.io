---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/08987Freshofftheboat.html
---

## Stream: [general](index.html)
### Topic: [Fresh off the boat](08987Freshofftheboat.html)

---


{% raw %}
#### [ Nima (Mar 29 2018 at 06:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124351061):
<p>Anyone is willing to prove this example for me? It seems too obvious, but I have not luck doing it within the past hour.</p>
<div class="codehilite"><pre><span></span>universe u

variable {α : Type u}

structure constraint (α:Type u) :=
  cnstr::
  (trv:bool) -- is trivial
  (stt:bool) -- is strict
  (low:bool) -- is lower-bound
  (bnd:α)
open constraint

def setof : constraint α → α → Prop
| (cnstr tt _  _   _  ) _ := tt
| (cnstr _  tt low bnd) a := tt --if low then bnd &lt; a else a &lt; bnd
| (cnstr _  ff low bnd) a := tt --if low then bnd ≤ a else a ≤ bnd

example (c: constraint α) (a:α) : setof c a := sorry
</pre></div>

#### [ Kenny Lau (Mar 29 2018 at 06:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124351110):
<p>It doesn't even typecheck <span class="user-mention" data-user-id="112062">@Nima</span></p>

#### [ Nima (Mar 29 2018 at 06:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124351152):
<p><span class="user-mention" data-user-id="110064">@Kenny Lau</span> Sorry, I  added "open constraint". Now it is typed checked</p>

#### [ Simon Hudon (Mar 29 2018 at 06:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124351206):
<p>you can prove it as:</p>
<div class="codehilite"><pre><span></span>example (c: constraint α) (a:α) : setof c a :=
by cases c ; trivial
</pre></div>


<p>I believe</p>

#### [ Nima (Mar 29 2018 at 06:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124351263):
<p><span class="user-mention" data-user-id="110026">@Simon Hudon</span> internal.lean:21:59: error<br>
trivial tactic failed<br>
state:<br>
α : Type u,<br>
a : α,<br>
trv stt low : bool,<br>
bnd : α<br>
⊢ setof {trv := trv, stt := stt, low := low, bnd := bnd} a</p>

#### [ Mario Carneiro (Mar 29 2018 at 06:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124351376):
<p>You probably want <code>true</code> instead of <code>tt</code> in the definition of <code>setof</code></p>

#### [ Simon Hudon (Mar 29 2018 at 06:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124351484):
<p>And you may find it easier to use this definition rather than yours:</p>
<div class="codehilite"><pre><span></span>inductive constraint (a : Type u)
| trivial : constraint
| strict_upper (x : a) : constraint
| strict_lower (x : a) : constraint
| nonstrict_upper (x : a) : constraint
| nonstrict_lower (x : a) : constraint
</pre></div>

#### [ Nima (Mar 29 2018 at 06:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124351488):
<p><span class="user-mention" data-user-id="110049">@Mario Carneiro</span> <br>
The following gives me the same error</p>
<div class="codehilite"><pre><span></span>def  setof : constraint α → α →  Prop
| (cnstr tt _ _ _ ) _ := true
| (cnstr _ tt low bnd) a := true --if low then bnd &lt; a else a &lt; bnd
| (cnstr _ ff low bnd) a := true --if low then bnd ≤ a else a ≤ bnd
</pre></div>


<p>The following is not typechecked</p>
<div class="codehilite"><pre><span></span>def  setof : constraint α → α →  Prop
| (cnstr true _ _ _ ) _ := true
| (cnstr _ true low bnd) a := true --if low then bnd &lt; a else a &lt; bnd
| (cnstr _ false low bnd) a := true --if low then bnd ≤ a else a ≤ bnd
</pre></div>

#### [ Mario Carneiro (Mar 29 2018 at 06:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124351496):
<p>The first one is what I mean. FYI you can code block with triple backquote before and after</p>

#### [ Mario Carneiro (Mar 29 2018 at 06:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124351539):
<div class="codehilite"><pre><span></span>def setof : constraint α → α → Prop
| (cnstr tt _ _ _ ) _ := true
| (cnstr ff tt low bnd) a := true --if low then bnd &lt; a else a &lt; bnd
| (cnstr ff ff low bnd) a := true --if low then bnd ≤ a else a ≤ bnd

example : ∀ (c : constraint α) (a:α), setof c a
| (cnstr tt _ _ _) _ := trivial
| (cnstr ff tt low bnd) a := trivial
| (cnstr ff ff low bnd) a := trivial
</pre></div>

#### [ Kenny Lau (Mar 29 2018 at 06:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124351545):
<p><span class="user-mention" data-user-id="110049">@Mario Carneiro</span> you don't need after :P</p>

#### [ Mario Carneiro (Mar 29 2018 at 06:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124351546):
<p>Are you one of those people who leaves off <code>&lt;/html&gt;</code></p>

#### [ Mario Carneiro (Mar 29 2018 at 06:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124351547):
<p>YOU RUINED THE INTERNET</p>

#### [ Nima (Mar 29 2018 at 06:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124351592):
<p><span class="user-mention" data-user-id="110049">@Mario Carneiro</span> Not sure what you mean!?</p>

#### [ Mario Carneiro (Mar 29 2018 at 06:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124351593):
<p>About what? The example shows how to prove the theorem by cases</p>

#### [ Mario Carneiro (Mar 29 2018 at 06:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124351594):
<p>my quip about the internet was for kenny's benefit</p>

#### [ Mario Carneiro (Mar 29 2018 at 06:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124351633):
<p>Note that you need to explicitly specify <code>ff</code> for the latter two cases in the definition of <code>setof</code> for the proof to work</p>

#### [ Nima (Mar 29 2018 at 06:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124351638):
<p><span class="user-mention" data-user-id="110049">@Mario Carneiro</span> Thanks a lot, it worked</p>

#### [ Mario Carneiro (Mar 29 2018 at 06:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124351677):
<p>Also, if you want to use <code>&lt;</code> you will need an appropriate typeclass, e.g.</p>
<div class="codehilite"><pre><span></span>def setof [linear_order α] : constraint α → α → Prop
| (cnstr tt _ _ _ ) _ := true
| (cnstr ff tt low bnd) a := if low then bnd &lt; a else a &lt; bnd
| (cnstr ff ff low bnd) a := if low then bnd ≤ a else a ≤ bnd
</pre></div>

#### [ Nima (Mar 29 2018 at 06:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124351684):
<p><span class="user-mention" data-user-id="110049">@Mario Carneiro</span> too soon for those lessons ;)</p>

#### [ Mario Carneiro (Mar 29 2018 at 06:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124351726):
<p>I agree with simon though about your encoding; having a bunch of <code>bool</code> flags will make things harder than just having a single inductive case split</p>

#### [ Mario Carneiro (Mar 29 2018 at 06:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124351776):
<p>You can also replace <code>α → Prop</code> with <code>set α</code> in the definition of <code>setof</code> (they are the same, but <code>set α</code> has more associated notations)</p>

#### [ Nima (Mar 29 2018 at 06:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124351777):
<p><span class="user-mention" data-user-id="110049">@Mario Carneiro</span> Is there any easy explanation for why do I need "to explicitly specify <code>ff</code> for the latter two cases in the definition of <code>setof</code> for the proof to work "</p>

#### [ Simon Hudon (Mar 29 2018 at 06:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124351821):
<p>And if you want to avoid type classes, you should pick a specific type (e.g. <code>ℕ</code>, <code>ℤ</code>, <code>ℚ</code>, <code>ℝ</code>) and the order will come from there</p>

#### [ Simon Hudon (Mar 29 2018 at 06:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124351866):
<blockquote>
<p><span class="user-mention" data-user-id="110049">@Mario Carneiro</span> Is there any easy explanation for why do I need "to explicitly specify <code>ff</code> for the latter two cases in the definition of <code>setof</code> for the proof to work "</p>
</blockquote>
<p>Because your definition has three equations and you can't match against the bools unless you know their values because you use their exact values in the equations</p>

#### [ Simon Hudon (Mar 29 2018 at 06:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124351867):
<p>E.g.:</p>
<div class="codehilite"><pre><span></span>| (cnstr tt _ _ _ ) _ := true
</pre></div>

#### [ Mario Carneiro (Mar 29 2018 at 06:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124351870):
<div class="codehilite"><pre><span></span>def setof : constraint α → α → Prop
| (cnstr tt _ _ _ ) _ := true
| (cnstr ff tt low bnd) a := true
| (cnstr ff ff low bnd) a := true
#print prefix setof.equations
-- setof.equations._eqn_1 : ∀ {α : Type u} (low : bool) (bnd a : α), setof {trv := ff, stt := ff, low := low, bnd := bnd} a = true
-- setof.equations._eqn_2 : ∀ {α : Type u} (low : bool) (bnd a : α), setof {trv := ff, stt := tt, low := low, bnd := bnd} a = true
-- setof.equations._eqn_3 : ∀ {α : Type u} (_x _x_1 : bool) (_x_2 _x_3 : α), setof {trv := tt, stt := _x, low := _x_1, bnd := _x_2} _x_3 = true

def setof : constraint α → α → Prop
| (cnstr tt _ _ _ ) _ := true
| (cnstr _ tt low bnd) a := true
| (cnstr _ ff low bnd) a := true
#print prefix setof.equations
-- setof.equations._eqn_1 : ∀ {α : Type u} (low : bool) (bnd a : α), setof {trv := ff, stt := ff, low := low, bnd := bnd} a = true
-- setof.equations._eqn_2 : ∀ {α : Type u} (low : bool) (bnd a : α), setof {trv := ff, stt := tt, low := low, bnd := bnd} a = true
-- setof.equations._eqn_3 : ∀ {α : Type u} (_x : bool) (_x_1 _x_2 : α), setof {trv := tt, stt := ff, low := _x, bnd := _x_1} _x_2 = true
-- setof.equations._eqn_4 : ∀ {α : Type u} (_x : bool) (_x_1 _x_2 : α), setof {trv := tt, stt := tt, low := _x, bnd := _x_1} _x_2 = true
</pre></div>

#### [ Mario Carneiro (Mar 29 2018 at 06:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124351918):
<p>Actually, the problem is that without specifying that the last two cases are <code>ff</code>, it does its first case split on the second bool, leading to four cases overall (with a superfluous case split on <code>stt</code> in the trivial case). This means that later you will need to case on it in the theorem</p>

#### [ Nima (Mar 29 2018 at 06:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124351924):
<p><span class="user-mention" data-user-id="110049">@Mario Carneiro</span> So the following from "8.2. Wildcards and Overlapping Patterns" is not that useful " But Lean handles the ambiguity by using the first applicable equation, so the net result is the same "</p>

#### [ Mario Carneiro (Mar 29 2018 at 06:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124351972):
<p>This has more to do with internals of the heuristics for what to case split when you aren't being explicit about it</p>

#### [ Nima (Mar 29 2018 at 06:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124351976):
<p><span class="user-mention" data-user-id="110049">@Mario Carneiro</span> Got it! Thanks</p>

#### [ Mario Carneiro (Mar 29 2018 at 06:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124351979):
<p>There's really no need to use a variable in the latter cases, you know it's <code>ff</code> and by writing it you tell lean to split there</p>

#### [ Nima (Mar 29 2018 at 16:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124369160):
<p>Have I defined <code>has_coe_to_sort</code> correctly? If so, how do I fix the <code>admit</code>s in my proof?</p>
<div class="codehilite"><pre><span></span>inductive constraint
| trv                    : constraint
| stt (bnd:ℕ) (low:Prop) : constraint
| nst (bnd:ℕ) (low:Prop) : constraint

namespace constraint

def setof : constraint → ℕ → Prop :=
begin
  intros c a,
  cases c with bnd lft bnd lft,
    case trv         {exact true},
    case stt bnd lft {exact lft ∧ bnd&lt;a ∨ a &lt; bnd},
    case nst bnd lft {exact lft ∧ bnd≤a ∨ a ≤ bnd},
end

instance constraint_to_sort : has_coe_to_sort constraint :=
  {S := Type, coe := λ S, {x // setof S x}}

example : ∀ (c:constraint) (n:c), setof c n :=
begin
  intros c n,
  cases c,
    trivial,
    begin
      admit
    end,
    begin
      admit
    end
end

end constraint
</pre></div>

#### [ Kevin Buzzard (Mar 29 2018 at 17:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124371359):
<p>This doesn't typecheck for me.</p>

#### [ Kevin Buzzard (Mar 29 2018 at 17:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124371371):
<div class="codehilite"><pre><span></span>invalid `case`, there is no goal tagged with prefix [constraint.stt, bnd, lft]
state:
2 goals
case constraint.stt
a bnd : ℕ,
lft : Prop
⊢ Prop

case constraint.nst
a bnd : ℕ,
lft : Prop
⊢ Prop
</pre></div>

#### [ Kevin Buzzard (Mar 29 2018 at 17:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124371375):
<p>line 13</p>

#### [ Kevin Buzzard (Mar 29 2018 at 17:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124371556):
<p>fixed it</p>

#### [ Kevin Buzzard (Mar 29 2018 at 17:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124371576):
<div class="codehilite"><pre><span></span>def setof : constraint → ℕ → Prop :=
begin
  intros c a,
  cases c with bnd lft bnd lft,
    case trv         {exact true},
    case stt {exact lft ∧ bnd&lt;a ∨ a &lt; bnd},
    case nst {exact lft ∧ bnd≤a ∨ a ≤ bnd},
end
</pre></div>

#### [ Kevin Buzzard (Mar 29 2018 at 17:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124371579):
<p>I'm using a recent lean nightly</p>

#### [ Nima (Mar 29 2018 at 17:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124371678):
<p><span class="user-mention" data-user-id="110038">@Kevin Buzzard</span> <br>
The following two lines fixed it (replace <code>admit</code>s)<br>
<code>exact @subtype.property nat (setof (stt bnd low)) n</code><br>
<code>exact @subtype.property nat (setof (nst bnd low)) n</code><br>
In fact I can solve the example in the following way</p>
<div class="codehilite"><pre><span></span>example : ∀ (c:constraint) (n:c), setof c n :=
begin
  intros c n,
  exact @subtype.property nat (setof c) n
end
</pre></div>

#### [ Kevin Buzzard (Mar 29 2018 at 17:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124371841):
<p>I am confused about what's going on.</p>

#### [ Kevin Buzzard (Mar 29 2018 at 17:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124371847):
<p><code>setof c</code> wants a nat, and you give it <code>n</code>, which is a <code>c</code>.</p>

#### [ Nima (Mar 29 2018 at 19:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124375020):
<p>Why the following is invalid? <br>
Error Message " invalid universe declaration, 'u_1' shadows a local universe"<br>
If I use <code>variable α : Type u</code> then everything will be fine</p>
<div class="codehilite"><pre><span></span>universe u
constant  α : Type u
variables x y : α
</pre></div>


<p>The following gives me no error (why?):</p>
<div class="codehilite"><pre><span></span>universe u
constant α : Type u
variable x : α
variable y : α
</pre></div>

#### [ Nima (Mar 29 2018 at 19:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124376097):
<p>I know the following example can be solve by replacing the last line with <code>exact hm</code>. But why I receive a this error:</p>
<div class="codehilite"><pre><span></span>universe u
variable {α : Type u}
constant le : α → α → Prop
example :
∀ (α : Type u)
  (hm : ∃ (m : α), ∀ (m&#39; : α), le m m&#39;),
  (∃ (m : α), ∀ (a : α) , le m a) :=
begin
  intros α hm,
  match hm with ⟨m,hh⟩ := sorry
end
</pre></div>


<p>It gives me</p>
<div class="codehilite"><pre><span></span>tmp.lean:12:2: error
don&#39;t know how to synthesize placeholder
context:
⊢ Type ?

tmp.lean:12:2: error
equation compiler failed (use &#39;set_option trace.eqn_compiler.elim_match true&#39; for additional details)

tmp.lean:12:8: error
unknown identifier &#39;hm&#39;

tmp.lean:12:8: error
don&#39;t know how to synthesize placeholder
context:
⊢ Sort ?

tmp.lean:12:16: error
invalid constructor ⟨...⟩, expected type is not an inductive type
  ?m_1
</pre></div>

#### [ Kevin Buzzard (Mar 29 2018 at 19:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124376139):
<p>That is funny. Generally I never use constants at all.</p>

#### [ Kenny Lau (Mar 29 2018 at 19:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124376145):
<p>right, you shouldn't use constant</p>

#### [ Nima (Mar 29 2018 at 19:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124376163):
<p><span class="user-mention" data-user-id="110038">@Kevin Buzzard</span> You mean constant for types, right? Otherwise, how do you assume a relation is given to you?</p>

#### [ Kevin Buzzard (Mar 29 2018 at 19:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124376512):
<p>I never ever use constants. I would write something like <code>example (le : X -&gt; X -&gt; Prop) : blah</code></p>

#### [ Kenny Lau (Mar 29 2018 at 19:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124376522):
<p><span class="user-mention" data-user-id="112062">@Nima</span> you use variable</p>

#### [ Kevin Buzzard (Mar 29 2018 at 19:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124376538):
<p>Or <code>variable</code> yes</p>

#### [ Kevin Buzzard (Mar 29 2018 at 19:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124376552):
<p>I would use variables or the trick above for an abstract relation.</p>

#### [ Kevin Buzzard (Mar 29 2018 at 19:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124376596):
<p>For a "well-known" one like <code>le</code> I would use the type class system</p>

#### [ Kevin Buzzard (Mar 29 2018 at 19:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124376626):
<p>Like this:</p>

#### [ Kevin Buzzard (Mar 29 2018 at 19:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124376674):
<div class="codehilite"><pre><span></span>variables (X : Type) [has_le X]
variables (x y : X)
#check has_le.le x y
#check x ≤ y
</pre></div>

#### [ Kevin Buzzard (Mar 29 2018 at 19:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124376689):
<p>Making X an instance of class <code>has_le</code> enables me to use the notation <code>\leq</code></p>

#### [ Kenny Lau (Mar 29 2018 at 19:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124376695):
<p><code>\le</code> :)</p>

#### [ Kevin Buzzard (Mar 29 2018 at 19:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124376696):
<p>no way!</p>

#### [ Kevin Buzzard (Mar 29 2018 at 19:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124376706):
<p>You'll be telling me I don't have to type <code>\forall</code> next</p>

#### [ Kenny Lau (Mar 29 2018 at 19:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124376707):
<p>I know the shortest code for the symbols I use :P</p>

#### [ Kenny Lau (Mar 29 2018 at 19:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124376709):
<p><code>\fo</code></p>

#### [ Kevin Buzzard (Mar 29 2018 at 20:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124376760):
<p>I discovered that one because I once typed something like <code>\fo4all</code> followed by a space</p>

#### [ Kevin Buzzard (Mar 29 2018 at 20:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124376772):
<p>and was like "wooah, it's magic"</p>

#### [ Kevin Buzzard (Mar 29 2018 at 20:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124376783):
<p>"it worked anyway"</p>

#### [ Kevin Buzzard (Mar 29 2018 at 20:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124376817):
<p>Back to the point</p>

#### [ Kevin Buzzard (Mar 29 2018 at 20:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124376872):
<p>you can write <code>[H : has_le X]</code> if you want to give the construction a name. Otherwise it ends up being called something like <code>_inst_1</code></p>

#### [ Kenny Lau (Mar 29 2018 at 20:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124376882):
<p>but most of the time you don't want to do that</p>

#### [ Kevin Buzzard (Mar 29 2018 at 20:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124376920):
<p>Right, most of the time you want Lean to figure it out for you</p>

#### [ Nima (Mar 29 2018 at 20:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124377820):
<p>Thanks, <br>
Would you please answer this one as well?</p>
<blockquote>
<p>I know the following example can be solve by replacing the last line with <code>exact hm</code>. But why I receive a this error:</p>
</blockquote>

#### [ Mario Carneiro (Mar 29 2018 at 20:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124377930):
<p>match is not a tactic. If you want to use it you have to say <code>exact match ...</code></p>

#### [ Mario Carneiro (Mar 29 2018 at 20:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124377984):
<p>When you write it there lean gets all sorts of confused in the parsing</p>

#### [ Mario Carneiro (Mar 29 2018 at 20:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124378010):
<p>also <code>match</code> requires <code>end</code> after it</p>

#### [ Nima (Mar 29 2018 at 20:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124378069):
<p><span class="user-mention" data-user-id="110049">@Mario Carneiro</span> Awesome!</p>

#### [ Mario Carneiro (Mar 29 2018 at 20:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124378075):
<p>The tactic equivalent of <code>match</code> is <code>cases</code>, but I think you have already discovered this</p>

#### [ Mario Carneiro (Mar 29 2018 at 20:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124378087):
<p>so you could use <code>cases hm with m hh,</code> in place of the match line</p>

#### [ Nima (Mar 29 2018 at 21:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124379367):
<p><span class="user-mention" data-user-id="110049">@Mario Carneiro</span> Thanks a lot, I finally finished a proof! (super simple one, yet 65 lines!!)</p>

#### [ Nima (Mar 29 2018 at 22:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124383712):
<p>This is about <strong> coercions </strong><br>
The first example in the following code works perfectly fine.<br>
However, the second example cannot be type-checked. I know this direction in general is not possible. But this example, <code>trv α</code> contains all elements of <code>α</code>. So how should I prove the second example?</p>
<div class="codehilite"><pre><span></span>universe u
variables {α : Type u} [linear_order α]

inductive constraint (α:Type u)
| trv                    : constraint
| stt (bnd:α) (low:Prop) : constraint
| nst (bnd:α) (low:Prop) : constraint

namespace constraint

def setof : constraint α → α → Prop :=
begin
  intros c a,
  cases c with bnd low bnd low,
    case trv         {exact true},
    case stt bnd low {exact low ∧ bnd&lt;a ∨ ¬ low ∧ a &lt; bnd},
    case nst bnd low {exact low ∧ bnd≤a ∨ ¬ low ∧ a ≤ bnd},
end

instance constraint_to_sort : has_coe_to_sort (constraint α) :=
  {S := Type u, coe := λ S, {x // setof S x}}

example : ∀ (c:constraint α) (a:c), setof c a :=
begin
  intros c a,
  exact @subtype.property α (setof c) a
end

example : (∀ (a : (trv α)), ff) → ∀ a:α, ff :=
begin
  intros h a,
  exact h a
end

end constraint
</pre></div>

#### [ Kenny Lau (Mar 29 2018 at 22:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124383739):
<p>what is the intuition behind all these?</p>

#### [ Nima (Mar 29 2018 at 22:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124383794):
<p>Using coercion we can say every natural number is a real number. But what if we know <code>r</code> is a real number <code>2</code>. How we can use it as a natural number.</p>

#### [ Kenny Lau (Mar 29 2018 at 22:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124383804):
<p>what is trv stt nst?</p>

#### [ Nima (Mar 29 2018 at 22:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124383989):
<p>Constructors of <code>constraint</code>. The code defines coercion from <code>constraint  α</code> to <code>α</code>. I am trying to go back from <code>α</code> to <code>constraint α</code>.  In the second example, <code>trv α</code> is a trivial constraint that is satisfied by every element of type <code>α</code>.</p>

#### [ Kenny Lau (Mar 29 2018 at 23:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124384111):
<p>btw <code>setof</code> doesn't type check</p>

#### [ Nima (Mar 29 2018 at 23:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124384152):
<p>I copy pasted it from VSCode, it type checks perfectly fine.<br>
Someone else told me if they remove <code>bnd</code> and <code>low</code> right after <code>case stt</code> and <code>case nst</code> they can compile it as well.</p>

#### [ Kenny Lau (Mar 29 2018 at 23:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124384192):
<p>right</p>

#### [ Kenny Lau (Mar 29 2018 at 23:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124384196):
<div class="codehilite"><pre><span></span>universe u
variables {α : Type u} [linear_order α]

inductive constraint (α:Type u)
| trv                    : constraint
| stt (bnd:α) (low:Prop) : constraint
| nst (bnd:α) (low:Prop) : constraint

namespace constraint

def setof : constraint α → α → Prop :=
begin
  intros c a,
  cases c with bnd low bnd low,
    case trv {exact true},
    case stt {exact low ∧ bnd&lt;a ∨ ¬ low ∧ a &lt; bnd},
    case nst {exact low ∧ bnd≤a ∨ ¬ low ∧ a ≤ bnd},
end

instance constraint_to_sort : has_coe_to_sort (constraint α) :=
  {S := Type u, coe := λ S, {x // setof S x}}

example : ∀ (c:constraint α) (a:c), setof c a :=
begin
  intros c a,
  exact @subtype.property α (setof c) a
end

example : (∀ (a : (trv α)), ff) → ∀ a:α, ff :=
begin
  intros h a,
  exact h ⟨a, trivial⟩
end

end constraint
</pre></div>

#### [ Kenny Lau (Mar 29 2018 at 23:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124384198):
<p>solution ^</p>

#### [ Kenny Lau (Mar 29 2018 at 23:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124384222):
<p>also, I would avoid using any tactics in definitions</p>

#### [ Nima (Mar 29 2018 at 23:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124384230):
<p>Thanks, so <code>trivial</code> is basically a proof that <code>a</code> is satisfied by <code>trv α</code>. Right?</p>

#### [ Nima (Mar 29 2018 at 23:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124384300):
<blockquote>
<p>also, I would avoid using any tactics in definitions</p>
</blockquote>
<p>"Fresh off the boat", so no idea what best practices are. Just trying to survive ;)</p>

#### [ Kenny Lau (Mar 29 2018 at 23:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124384333):
<p>oh, ok, sorry</p>

#### [ Kenny Lau (Mar 29 2018 at 23:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124384399):
<div class="codehilite"><pre><span></span>def setof : constraint α → α → Prop
| (trv α)       a := true
| (stt bnd low) a := low ∧ bnd&lt;a ∨ ¬ low ∧ a &lt; bnd
| (nst bnd low) a := low ∧ bnd≤a ∨ ¬ low ∧ a ≤ bnd
</pre></div>

#### [ Nima (Mar 29 2018 at 23:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124384477):
<p>Cool, thanks</p>

#### [ Nima (Mar 30 2018 at 00:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124387596):
<p>Is there any tactic that can push the negation inside quantifiers?<br>
For example <code>¬  ∀ x,∃ y, p x y</code> should become <code>∃ x,∀ y, ¬ p x y</code>.<br>
Using <code>classical</code> is fine.</p>

#### [ Andrew Ashworth (Mar 30 2018 at 01:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124388893):
<p>no. use a lemma</p>

#### [ Nima (Mar 30 2018 at 01:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124389077):
<p><span class="user-mention" data-user-id="110025">@Andrew Ashworth</span> You mean some lemma (probably two) twice. Right? I was looking for some tactic to push the negation all the way inside. Not sure how difficult it is to write such a tactic. I don't think writing a lemma is the solution, or at least I don't know how that can be done using a lemma such that one invocation of it will do the job.</p>

#### [ Andrew Ashworth (Mar 30 2018 at 01:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124389453):
<p>i mean, literally write a lemma stating <code> ¬ ∀ x,∃ y, p x y </code> iff <code> ∃ x,∀ y, ¬ p x y </code>. Then rewrite with it.</p>

#### [ Nima (Mar 30 2018 at 04:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124394062):
<p>How do I find Lean version that is running online? I am using 3.3.0 (re-downloaded 5 minutes ago) and cannot typecheck the following code from Programming in Lean (the online Lean typechecks it):</p>
<div class="codehilite"><pre><span></span>import system.io
variable [io.interface]
open nat io

def print_squares : ℕ → io unit
| 0        := return ()
| (succ n) := print_squares n &gt;&gt;
              put_str (nat.to_string n ++ &quot;^2 = &quot; ++
                       nat.to_string (n * n) ++ &quot;\n&quot;)

#eval print_squares 100
</pre></div>

#### [ Mario Carneiro (Mar 30 2018 at 04:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124394417):
<p>The latest version of lean doesn't use <code>io.interface</code>. Try removing that line and the rest should work</p>

#### [ Nima (Mar 30 2018 at 04:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124394471):
<p>Removing that adds to error.  The current error I am receiving is <code> unknown identifier 'nat.to_string' </code>.<br>
If it is of any help, I am on Mac and downloaded the binary version.</p>

#### [ Mario Carneiro (Mar 30 2018 at 05:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124395469):
<p>Looks like it's just <code>to_string</code> now</p>

#### [ Kenny Lau (Mar 30 2018 at 05:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124395480):
<p>what did I just see</p>

#### [ Kenny Lau (Mar 30 2018 at 05:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124395481):
<p>is Lean basically python now</p>

#### [ Andrew Ashworth (Mar 30 2018 at 05:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124396126):
<p>i think there's room to add more handy programming gadgets once lean 4 rolls around and we can extend the parser</p>

#### [ Andrew Ashworth (Mar 30 2018 at 05:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124396196):
<p><code>map (fun x -&gt; x * x) [0 .. 10] = [0, 1, 4, 9, 16, 25, 36, 49, 56, 64, 81, 100]</code> would be sweet</p>

#### [ Kenny Lau (Mar 30 2018 at 05:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124396199):
<p>we already have list.map</p>

#### [ Andrew Ashworth (Mar 30 2018 at 05:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124396203):
<p>you can't write <code>[0 .. 10]</code> right now</p>

#### [ Kenny Lau (Mar 30 2018 at 05:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124396204):
<p>list.range</p>

#### [ Andrew Ashworth (Mar 30 2018 at 05:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124396214):
<p>or more generally <code>[0 .. 2 .. 10]</code> where you can supply a step</p>

#### [ Andrew Ashworth (Mar 30 2018 at 05:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124396257):
<p>aha, that's not quite so simple to declare with a <code>notation</code> command</p>

#### [ Kenny Lau (Mar 30 2018 at 05:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124396269):
<div class="codehilite"><pre><span></span>import system.io

open nat io

def print_fib_core : ℕ → ℕ × ℕ × io unit
| 0        := (0, 1, return ())
| (succ n) := let (a, b, c) := print_fib_core n in
              (b, a+b, c &gt;&gt;
                  put_str (&quot;fib &quot; ++ to_string n ++ &quot; = &quot; ++
                       to_string a ++ &quot;\n&quot;))

def print_fib : ℕ → io unit :=
λ n, (print_fib_core n).2.2

#eval print_fib 100
</pre></div>

#### [ Kenny Lau (Mar 30 2018 at 05:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124396274):
<div class="codehilite"><pre><span></span>fib 0 = 0
fib 1 = 1
fib 2 = 1
fib 3 = 2
fib 4 = 3
fib 5 = 5
fib 6 = 8
fib 7 = 13
fib 8 = 21
fib 9 = 34
fib 10 = 55
[...]
fib 90 = 2880067194370816120
fib 91 = 4660046610375530309
fib 92 = 7540113804746346429
fib 93 = 12200160415121876738
fib 94 = 19740274219868223167
fib 95 = 31940434634990099905
fib 96 = 51680708854858323072
fib 97 = 83621143489848422977
fib 98 = 135301852344706746049
fib 99 = 218922995834555169026
</pre></div>

#### [ Kenny Lau (Mar 30 2018 at 05:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124396276):
<p>cool, now I can do Project Euler with it</p>

#### [ Kenny Lau (Mar 30 2018 at 05:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124396325):
<p>this is ridiculous</p>

#### [ Andrew Ashworth (Mar 30 2018 at 05:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124396360):
<p>project euler in a functional language is painful, but that's probably because i don't speak monad</p>

#### [ Kenny Lau (Mar 30 2018 at 05:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124396406):
<p>you only need <code>io unit</code> :P</p>

#### [ Nima (Mar 30 2018 at 05:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124396431):
<p><span class="user-mention" data-user-id="110064">@Kenny Lau</span> Thank you, it worked (I still need <code> variable [io.interface]</code>, but it works)</p>

#### [ Kenny Lau (Mar 30 2018 at 05:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124396472):
<p>ok</p>

#### [ Mario Carneiro (Mar 30 2018 at 05:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124396942):
<p>I get <code> VM does not have code for 'unsafe_monad_from_pure_bind' </code> when I try to run that code</p>

#### [ Kenny Lau (Mar 30 2018 at 05:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124396946):
<p>which code?</p>

#### [ Mario Carneiro (Mar 30 2018 at 05:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124396991):
<p>your fib code</p>

#### [ Kenny Lau (Mar 30 2018 at 05:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124396992):
<p>what is your lean version?</p>

#### [ Kenny Lau (Mar 30 2018 at 05:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124396995):
<div class="codehilite"><pre><span></span>Lean (version 3.3.1, commit 28f4143be31b, RELEASE)
</pre></div>

#### [ Mario Carneiro (Mar 30 2018 at 05:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124396996):
<p>28f414</p>

#### [ Kenny Lau (Mar 30 2018 at 05:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124396998):
<p>wow</p>

#### [ Kenny Lau (Mar 30 2018 at 05:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124397036):
<p>what does that mean</p>

#### [ Mario Carneiro (Mar 30 2018 at 05:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124397039):
<p>same as yours, evidently</p>

#### [ Mario Carneiro (Mar 30 2018 at 05:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124397111):
<p>I can't even find<code>unsafe_monad_from_pure_bind</code> in the lean repo, it's a mystery where that comes from</p>

#### [ Mario Carneiro (Mar 30 2018 at 05:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124397117):
<p>meh, restart and it's fine</p>

#### [ Kenny Lau (Mar 30 2018 at 05:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124397125):
<p>what is the intended use for bit0 and bit1?</p>

#### [ Kenny Lau (Mar 30 2018 at 05:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124397127):
<p>can I use them in recursion?</p>

#### [ Mario Carneiro (Mar 30 2018 at 06:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124397368):
<p>Here's my version of the fib printer:</p>
<div class="codehilite"><pre><span></span>def fib_core : ℕ → ℕ × ℕ
| 0        := (0, 1)
| (succ n) := let (a, b) := fib_core n in (b, a+b)

def fib (n) := (fib_core n).1

def print_fib (n : ℕ) : io unit :=
(list.range 100).mmap&#39; (λ n,
  put_str (&quot;fib &quot; ++ to_string n ++ &quot; = &quot; ++
    to_string (fib n) ++ &quot;\n&quot;))

#eval print_fib 100
</pre></div>


<p>It's asymptotically slower than Kenny's version since it recomputes <code>fib</code> rather than calculating as it goes, but this is a bit closer to what you would expect in another programming language without any fancy tricks</p>

#### [ Mario Carneiro (Mar 30 2018 at 06:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124397445):
<p><code>bit0</code> and <code>bit1</code> are used by the parser to construct natural number literals and other number literals like <code>7</code>, which is actually <code>bit1 (bit1 (bit1 1)))</code> in whatever type (it must have typeclasses for <code>has_add</code> and <code>has_one</code>)</p>

#### [ Mario Carneiro (Mar 30 2018 at 06:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124397459):
<p>If you want to define a function by binary recursion over <code>nat</code>, use <code>nat.binary_rec_on</code>, which uses <code>bit b n</code> which generalizes <code>bit0</code> and <code>bit1</code> with a boolean bit parameter</p>

#### [ Kenny Lau (Mar 30 2018 at 06:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124397505):
<div class="codehilite"><pre><span></span>def list.update {α : Type*} : list α → list nat → α → list α
| L []     x := L
| L (h::t) x := (L.update t x).update_nth h x

namespace eratosthenes

def aux1 : nat → nat → nat
| sq lo := if (lo+1)*(lo+1) &gt; sq then lo else lo+1

def isqrt : nat → nat
| n := if H : n / 4 &lt; n then
         (aux1 n (isqrt (n / 4) * 2))
       else n

def aux2 : list bool → nat → nat → list bool :=
λ L len n, L.update (list.map (λ z, (z + n) * n) (list.range $ len / n)) ff

def aux3 : list bool → nat → nat → list bool
| L len 0     := L
| L len 1     := L
| L len (n+1) := aux2 (aux3 L len n) len (n+1)

def aux4 : nat → list bool :=
λ n, aux3 (list.repeat tt n) n (isqrt n)

def aux5 : list bool → nat → list nat :=
λ L n, (list.range n).filter $ λ z, L.nth z = tt

end eratosthenes

def eratosthenes : nat → list nat :=
λ n, (eratosthenes.aux5 (eratosthenes.aux4 n) n).drop 2

#eval eratosthenes 1000
</pre></div>

#### [ Kenny Lau (Mar 30 2018 at 06:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124397508):
<p>why is this so slow</p>

#### [ Mario Carneiro (Mar 30 2018 at 06:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124397558):
<p>geez, name your stuff better</p>

#### [ Kenny Lau (Mar 30 2018 at 06:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124397560):
<p>well I don't intend to PR it :P</p>

#### [ Mario Carneiro (Mar 30 2018 at 06:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124397565):
<p>it's like reading decompiled sources</p>

#### [ Kenny Lau (Mar 30 2018 at 06:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124397566):
<p>oh, sorry</p>

#### [ Kenny Lau (Mar 30 2018 at 06:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124397567):
<p>aux1 is for isqrt</p>

#### [ Andrew Ashworth (Mar 30 2018 at 06:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124397568):
<p>heh, sieve of e</p>

#### [ Kenny Lau (Mar 30 2018 at 06:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124397569):
<p>aux2 does one sieve</p>

#### [ Andrew Ashworth (Mar 30 2018 at 06:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124397570):
<p><a href="https://www.cs.hmc.edu/~oneill/papers/Sieve-JFP.pdf" target="_blank" title="https://www.cs.hmc.edu/~oneill/papers/Sieve-JFP.pdf">https://www.cs.hmc.edu/~oneill/papers/Sieve-JFP.pdf</a></p>

#### [ Mario Carneiro (Mar 30 2018 at 06:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124397571):
<p>What's the anticipated order?</p>

#### [ Kenny Lau (Mar 30 2018 at 06:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124397611):
<p>of what?</p>

#### [ Mario Carneiro (Mar 30 2018 at 06:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124397613):
<p>of the code</p>

#### [ Kenny Lau (Mar 30 2018 at 06:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124397615):
<p>it sieves sqrt(n) times</p>

#### [ Kenny Lau (Mar 30 2018 at 06:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124397616):
<p>each time taking n</p>

#### [ Kenny Lau (Mar 30 2018 at 06:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124397619):
<p>I think it's O(n^1.5) then</p>

#### [ Mario Carneiro (Mar 30 2018 at 06:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124397620):
<p>I see several quadratic passes at least</p>

#### [ Kenny Lau (Mar 30 2018 at 06:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124397621):
<p>where is the quadratic pass</p>

#### [ Mario Carneiro (Mar 30 2018 at 06:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124397628):
<p><code>(list.range n).filter $ λ z, L.nth z = tt</code> passes over <code>L</code> for each <code>n</code></p>

#### [ Kenny Lau (Mar 30 2018 at 06:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124397638):
<p>oh, how should I fix that</p>

#### [ Kenny Lau (Mar 30 2018 at 06:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124397639):
<p>ah, I should deconstruct the list</p>

#### [ Andrew Ashworth (Mar 30 2018 at 06:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124397640):
<p>paper i linked discusses the sieve in a functional setting exhaustively</p>

#### [ Mario Carneiro (Mar 30 2018 at 06:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124397681):
<p>You should put comments or something, it's not obvious what the auxes do</p>

#### [ Kenny Lau (Mar 30 2018 at 06:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124397689):
<p>should I implement the code form your paper?</p>

#### [ Andrew Ashworth (Mar 30 2018 at 06:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124397730):
<p>i mean, if you want a functional Sieve of Eratosthenes , that is also pretty fast, yes</p>

#### [ Kenny Lau (Mar 30 2018 at 06:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124397735):
<p>does it use data structures that I don't have?</p>

#### [ Kenny Lau (Mar 30 2018 at 06:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124397738):
<p>PriorityQ?</p>

#### [ Andrew Ashworth (Mar 30 2018 at 06:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124397777):
<p>this is getting a bit out of hand, but you could implement one from okasaki's "purely functional data structures"</p>

#### [ Mario Carneiro (Mar 30 2018 at 06:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124397780):
<p>Yeah, we don't have that, maybe <code>rb_map</code> will work</p>

#### [ Mario Carneiro (Mar 30 2018 at 06:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124397784):
<p>Beware, Okasaki assumes a <code>susp</code> type (aka memoization), but we don't have one</p>

#### [ Andrew Ashworth (Mar 30 2018 at 06:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124397828):
<p>hm. then i'd use the red-black tree in lean core for everything</p>

#### [ Mario Carneiro (Mar 30 2018 at 06:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124397833):
<p>You actually could make your original code a lot faster simply by using arrays instead of lists. You are using them like arrays anyway</p>

#### [ Mario Carneiro (Mar 30 2018 at 06:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124397834):
<p>and that will make <code>L.nth</code> asymptotically fast</p>

#### [ Kenny Lau (Mar 30 2018 at 06:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124397874):
<p>I've never used array :P</p>

#### [ Kenny Lau (Mar 30 2018 at 06:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124397875):
<p>I don't even know arrays exist</p>

#### [ Mario Carneiro (Mar 30 2018 at 06:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124397896):
<p><code>array</code> is like <code>vector</code>, it's a list with a fixed (in the type) size</p>

#### [ Mario Carneiro (Mar 30 2018 at 06:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124397938):
<p>and importantly, it's implemented as an C++ array, meaning that updates and nth are fast</p>

#### [ Kenny Lau (Mar 30 2018 at 06:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124397993):
<p>can I trace the function calls? i.e. debugging?</p>

#### [ Andrew Ashworth (Mar 30 2018 at 06:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124397996):
<p>is vector a dynamically growing array under the hood?</p>

#### [ Andrew Ashworth (Mar 30 2018 at 06:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124398049):
<p>... i wonder how much work it would take to use a dynamically growing array for lean's list impl</p>

#### [ Mario Carneiro (Mar 30 2018 at 06:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124398148):
<p><code>vector</code> is literally just a subtype of <code>list</code>. <code>array</code> is isomorphic to <code>vector</code>, and is implemented as the <code>parray</code> type in C++, which is a C++ array with some added support for end extension and persistent usage</p>

#### [ Andrew Ashworth (Mar 30 2018 at 06:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124398220):
<p>ahh, i see</p>

#### [ Kenny Lau (Mar 30 2018 at 06:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124398431):
<div class="codehilite"><pre><span></span>def list.update {α : Type*} : list α → list nat → α → list α
| L []     x := L
| L (h::t) x := (L.update t x).update_nth h x

def list.extract {α : Type*} [decidable_eq α] : list α → nat → α → list nat
| L      0     x := []
| []     (n+1) x := []
| (h::t) (n+1) x := if h = x then n :: t.extract n x else t.extract n x

namespace eratosthenes

def aux1 : nat → nat → nat
| sq lo := if (lo+1)*(lo+1) &gt; sq then lo else lo+1

def isqrt : nat → nat
| n := if H : n / 4 &lt; n then aux1 n (isqrt (n / 4) * 2) else n

-- from L, make every n-th item false
def step : list bool → nat → nat → list bool :=
λ L len n, L.update (list.map (λ z, (z + n) * n) (list.range $ len / n)) ff

-- do &quot;step&quot; for every integer from 2 to n
def sieve : list bool → nat → nat → list bool
| L len 0     := L
| L len 1     := L
| L len (n+1) := if L.nth (n+1) = tt then step (sieve L len n) len (n+1) else sieve L len n

-- invoke sieve with sqrt(n)
def prime.bool : nat → list bool :=
λ n, sieve (list.repeat tt n) n (isqrt n)

end eratosthenes

def eratosthenes : nat → list nat :=
λ n, ((eratosthenes.prime.bool n).reverse.extract n tt).reverse.drop 2

#eval eratosthenes 1000
</pre></div>

#### [ Kenny Lau (Mar 30 2018 at 06:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124398434):
<p><span class="user-mention" data-user-id="110049">@Mario Carneiro</span> what do you think is the complexity of this?</p>

#### [ Kenny Lau (Mar 30 2018 at 06:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124398474):
<p>ah, I see a quadratic pass</p>

#### [ Mario Carneiro (Mar 30 2018 at 06:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124398480):
<p><code>L.update</code> is quadratic</p>

#### [ Kenny Lau (Mar 30 2018 at 06:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124398481):
<p>right</p>

#### [ Mario Carneiro (Mar 30 2018 at 06:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124398484):
<p>I think you should define <code>step</code> by recursion</p>

#### [ Mario Carneiro (Mar 30 2018 at 06:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124398494):
<p>it shouldn't be hard to make every <code>n</code>th item false by keeping an accumulator</p>

#### [ Mario Carneiro (Mar 30 2018 at 06:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124398539):
<p>You can't do <code>step</code> in less than O(n) time with this data structure, so <code>sieve</code> is necessarily O(n^2)</p>

#### [ Kenny Lau (Mar 30 2018 at 06:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124398540):
<p>what do you mean?</p>

#### [ Mario Carneiro (Mar 30 2018 at 06:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124398547):
<p><code>step</code> has to walk down the entire list to change stuff</p>

#### [ Kenny Lau (Mar 30 2018 at 06:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124398551):
<p>but I only need to call step <code>sqrt(n)</code> times</p>

#### [ Mario Carneiro (Mar 30 2018 at 06:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124398592):
<p>Ah, that's true. So n^1.5 seems likely</p>

#### [ Mario Carneiro (Mar 30 2018 at 06:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124398597):
<p>As that paper will tell you though, this isn't "true" eratosthenes since you have to visit all the skipped entries multiple times</p>

#### [ Kenny Lau (Mar 30 2018 at 06:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124398599):
<p>I see</p>

#### [ Kenny Lau (Mar 30 2018 at 06:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124398639):
<p>well that paper is too technical</p>

#### [ Kenny Lau (Mar 30 2018 at 06:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124398687):
<p>it's O(n^1.5) now, empirically</p>

#### [ Kenny Lau (Mar 30 2018 at 06:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124398688):
<p>because I can do 10000 now</p>

#### [ Kenny Lau (Mar 30 2018 at 06:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124398691):
<p>(how pathetic)</p>

#### [ Kenny Lau (Mar 30 2018 at 06:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124398692):
<div class="codehilite"><pre><span></span>def list.extract {α : Type*} [decidable_eq α] : list α → nat → α → list nat
| L      0     x := []
| []     (n+1) x := []
| (h::t) (n+1) x := if h = x then n :: t.extract n x else t.extract n x

namespace eratosthenes

def aux1 : nat → nat → nat
| sq lo := if (lo+1)*(lo+1) &gt; sq then lo else lo+1

def isqrt : nat → nat
| n := if H : n / 4 &lt; n then aux1 n (isqrt (n / 4) * 2) else n

-- from L, make every n-th item false
def step : list bool → nat → nat → list bool :=
λ L n start, L.enum.map (λ z, if z.1 % n = 0 ∧ start ≤ z.1 then ff else z.2)

-- do &quot;step&quot; for every integer from 2 to n
def sieve : list bool → nat →list bool
| L 0     := L
| L 1     := L
| L (n+1) := if L.nth (n+1) = tt then step (sieve L n) (n+1) ((n+1)*(n+1)) else sieve L n

-- invoke sieve with sqrt(n)
def prime.bool : nat → list bool :=
λ n, sieve (list.repeat tt n) (isqrt n)

end eratosthenes

def eratosthenes : nat → list nat :=
λ n, ((eratosthenes.prime.bool n).reverse.extract n tt).reverse.drop 2

#eval eratosthenes 10000
</pre></div>

#### [ Kenny Lau (Mar 30 2018 at 06:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124398695):
<p>now I'm going to redo it</p>

#### [ Kenny Lau (Mar 30 2018 at 06:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124398698):
<p>i.e. use <code>list nat</code> instead of <code>list bool</code></p>

#### [ Kenny Lau (Mar 30 2018 at 06:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124398701):
<p>and use accumulator instead of mod</p>

#### [ Andrew Ashworth (Mar 30 2018 at 06:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124398704):
<p>well, that paper has a list based implementation on page 11</p>

#### [ Kenny Lau (Mar 30 2018 at 06:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124398743):
<p>oh</p>

#### [ Andrew Ashworth (Mar 30 2018 at 06:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124398745):
<p>but, you'll need a lazy sequence type</p>

#### [ Kenny Lau (Mar 30 2018 at 06:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124398746):
<p>coinduction is coming soon, I hope :)</p>

#### [ Andrew Ashworth (Mar 30 2018 at 06:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124398747):
<p>i don't know if lean supports lazy semantics right now</p>

#### [ Kenny Lau (Mar 30 2018 at 06:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124398749):
<p>we already have stream</p>

#### [ Kenny Lau (Mar 30 2018 at 06:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124398750):
<p>but I don't know how computable it is</p>

#### [ Mario Carneiro (Mar 30 2018 at 06:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124398751):
<p>Seriously, use <code>array</code></p>

#### [ Mario Carneiro (Mar 30 2018 at 06:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124398757):
<p>if you care about speed, use <code>array</code></p>

#### [ Mario Carneiro (Mar 30 2018 at 06:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124398760):
<p>linked lists are known horrible in almost all cases in CS theory</p>

#### [ Mario Carneiro (Mar 30 2018 at 06:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124398802):
<p><code>stream</code> exists and is computable, but is not remotely efficient as a stream</p>

#### [ Mario Carneiro (Mar 30 2018 at 06:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124398808):
<p>the hard part about making that paper applicable in lean is all the tricks used to take advantage of laziness</p>

#### [ Mario Carneiro (Mar 30 2018 at 06:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124398847):
<p>AFAIK there are no plans to make lean lazy. You can manually add laziness using <code>thunk</code></p>

#### [ Andrew Ashworth (Mar 30 2018 at 06:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124398849):
<p>yeah, it's unfortunate that the most popular pure functional language emphasizes laziness so much</p>

#### [ Andrew Ashworth (Mar 30 2018 at 06:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124398853):
<p>it's really hard to move code snippets and ideas over</p>

#### [ Mario Carneiro (Mar 30 2018 at 06:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124398857):
<p>ML is a good functional strict language, but I find it often does too much impure stuff</p>

#### [ Andrew Ashworth (Mar 30 2018 at 06:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124398859):
<p>that's a benefit :)</p>

#### [ Andrew Ashworth (Mar 30 2018 at 06:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124398860):
<p>(i use f# when i can)</p>

#### [ Mario Carneiro (Mar 30 2018 at 07:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124398899):
<p>In the sense that it makes it difficult to transfer ideas over</p>

#### [ Andrew Ashworth (Mar 30 2018 at 07:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124398907):
<p>i haven't tried to do much imperative programming in lean</p>

#### [ Andrew Ashworth (Mar 30 2018 at 07:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124398909):
<p>is it hard to emulate?</p>

#### [ Kenny Lau (Mar 30 2018 at 07:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124399059):
<p>now it's much faster!</p>

#### [ Kenny Lau (Mar 30 2018 at 07:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124399060):
<div class="codehilite"><pre><span></span>namespace eratosthenes

def aux1 : nat → nat → nat
| sq lo := if (lo+1)*(lo+1) &gt; sq then lo else lo+1

def isqrt : nat → nat
| n := if H : n / 4 &lt; n then aux1 n (isqrt (n / 4) * 2) else n

-- from L, remove every item divisible by n
def step : list nat → nat → list nat
| []     n := []
| (h::t) n := if h%n = 0 then step t n else h::step t n

-- each time : remove one element, do step on that element
def sieve : nat → list nat → list nat
| hi []     := []
| hi (h::t) := if h ≤ hi then (h::step t h) else (h::t)

end eratosthenes

def eratosthenes : nat → list nat :=
λ n, eratosthenes.sieve (eratosthenes.isqrt n) ((list.range n).drop 2)

#eval eratosthenes 10000
</pre></div>

#### [ Mario Carneiro (Mar 30 2018 at 07:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124399219):
<p>I think <code>step</code> can be expressed as a <code>list.filter</code> without a performance hit with this approach</p>

#### [ Mario Carneiro (Mar 30 2018 at 07:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124399222):
<p>Isn't <code>sieve</code> recursive?</p>

#### [ Kenny Lau (Mar 30 2018 at 07:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124399244):
<p>yes, I just discovered the bug xd</p>

#### [ Kenny Lau (Mar 30 2018 at 07:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124399282):
<p>now Lean doesn't trust that my recursion is well-founded</p>

#### [ Kenny Lau (Mar 30 2018 at 07:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124399283):
<p>I can't be bothered to prove that to Lean</p>

#### [ Kenny Lau (Mar 30 2018 at 07:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124399284):
<p>so, see you :P</p>

#### [ Kenny Lau (Mar 30 2018 at 07:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124399694):
<div class="codehilite"><pre><span></span>namespace eratosthenes

-- O(1)
def aux1 : nat → nat → nat
| sq lo := if (lo+1)*(lo+1) &gt; sq then lo else lo+1

-- O(log n)
def isqrt : nat → nat
| n := if H : n / 4 &lt; n then aux1 n (isqrt (n / 4) * 2) else n

-- O(n)
-- from L, remove every item divisible by n
def step : list nat → nat → list nat
| []     n := []
| (h::t) n := if h%n = 0 then step t n else h::step t n

theorem aux (t : list nat) (h : nat) : list.sizeof (step t h) ≤ list.sizeof t :=
begin
  induction t with h1 t1 ih,
  { dsimp [step],
    refl },
  { dsimp [step],
    by_cases H : h1 % h = 0,
    { simp [H, list.sizeof],
      apply le_trans ih,
      apply le_trans (nat.le_add_right _ (sizeof h1)),
      exact nat.le_add_left _ _ },
    { simp [H, list.sizeof],
      apply nat.add_le_add_left,
      rw add_comm,
      apply nat.add_le_add_right,
      exact ih } }
end

theorem aux2 (t : list nat) (h : nat) : has_well_founded.r (step t h) (h :: t) :=
begin
  dsimp [has_well_founded.r, sizeof_measure, measure, inv_image, sizeof, has_sizeof.sizeof, list.sizeof],
  apply lt_of_le_of_lt (aux t h),
  apply nat.lt_add_of_pos_left,
  rw add_comm,
  exact nat.zero_lt_succ _
end

-- O(n^1.5)
-- each time : remove one element, do step on that element
def sieve (hi : nat) : list nat → list nat
| []     := []
| (h::t) := if h ≤ hi then (h::(sieve $ step t h)) else (h::t)
using_well_founded { dec_tac := `[exact aux2 t h] }

end eratosthenes

-- O(n^1.5)
def eratosthenes : nat → list nat :=
λ n, eratosthenes.sieve (eratosthenes.isqrt n) ((list.range n).drop 2)

#eval eratosthenes 10000
</pre></div>

#### [ Kenny Lau (Mar 30 2018 at 07:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124399696):
<p><span class="user-mention" data-user-id="110049">@Mario Carneiro</span> I lied</p>

#### [ Mario Carneiro (Mar 30 2018 at 07:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124399751):
<p>If you used <code>filter</code> for <code>step</code>, the lemma would be easier</p>

#### [ Kenny Lau (Mar 30 2018 at 07:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124400262):
<p>btw it can handle <code>100000</code> now</p>

#### [ Kenny Lau (Mar 30 2018 at 07:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124400366):
<p><span class="user-mention" data-user-id="110049">@Mario Carneiro</span> I don't see what difference it makes. It isn't a lemma that L.filter p has size at most L</p>

#### [ Mario Carneiro (Mar 30 2018 at 07:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124400386):
<p>It's a sublist from <code>filter_sublist</code>, and sublist implies length less equal</p>

#### [ Kenny Lau (Mar 30 2018 at 07:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124400388):
<p>so how exactly would I prove its well-foundedness?</p>

#### [ Mario Carneiro (Mar 30 2018 at 08:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124401268):
<div class="codehilite"><pre><span></span>def step (L : list nat) (n : nat) : list nat :=
L.filter (λ a, a%n ≠ 0)

def sieve (hi : nat) : list nat → list nat
| []     := []
| (h::t) :=
  have (step t h).length &lt; (h :: t).length, from
  lt_succ_of_le $ list.length_le_of_sublist $ list.filter_sublist _,
  if h ≤ hi then h::sieve (step t h) else h::t
using_well_founded {
  rel_tac := λ _ _, `[exact ⟨_, measure_wf list.length⟩],
  dec_tac := `[exact this] }
</pre></div>

#### [ Kenny Lau (Mar 30 2018 at 08:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124401276):
<p>oh, changing the relation</p>

#### [ Kenny Lau (Mar 30 2018 at 08:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124401277):
<p>I see</p>

#### [ Nima (Mar 31 2018 at 02:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124436819):
<p>The following is from Programming in Lean and works perfectly fine in the online Lean. Any idea how I should make it also work in version 3.3.0?</p>
<div class="codehilite"><pre><span></span>open expr tactic classical

meta def normalize_hyp (lemmas : list expr) (hyp : expr) : tactic unit :=
do try (simp_at hyp lemmas)
</pre></div>

#### [ Simon Hudon (Mar 31 2018 at 02:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124436867):
<p>what errors are you encountering?</p>

#### [ Kenny Lau (Mar 31 2018 at 02:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124436869):
<div class="codehilite"><pre><span></span>sandbox3.lean:6:3: error

don&#39;t know how to synthesize placeholder
context:
lemmas : list expr,
hyp : expr,
normalize_hyp : tactic unit
⊢ Type ?


sandbox3.lean:6:8: error

unknown identifier &#39;simp_at&#39;
</pre></div>

#### [ Nima (Mar 31 2018 at 02:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124436964):
<p>Yes, those errors</p>

#### [ Simon Hudon (Mar 31 2018 at 02:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124437019):
<p>Can you try <code>simp_hyp</code> instead of <code>simp_at</code>?</p>

#### [ Kenny Lau (Mar 31 2018 at 02:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124437022):
<div class="codehilite"><pre><span></span>type mismatch at application
  simp_hyp hyp
term
  hyp
has type
  expr
but is expected to have type
  simp_lemmas
</pre></div>

#### [ Simon Hudon (Mar 31 2018 at 03:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124437257):
<p>ok, first, swap the order of the arguments: <code> simp_hyp lemmas hyp</code></p>

#### [ Simon Hudon (Mar 31 2018 at 03:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124437259):
<p>second, let's construct a <code>simp_lemmas</code></p>

#### [ Simon Hudon (Mar 31 2018 at 03:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124437309):
<div class="codehilite"><pre><span></span>meta def normalize_hyp (lemmas : list expr) (hyp : expr) : tactic unit :=
do s &lt;- simp_lemmas.append simp_lemmas.mk lemmas,
   try (simp_at s hyp)
</pre></div>

#### [ Nima (Mar 31 2018 at 03:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124437406):
<p><code>simp_at</code>(<code>unknown identifier</code>)?<br>
If I use <code>simp_hyp</code> give me the same error</p>
<div class="codehilite"><pre><span></span>type mismatch at application
  simp_hyp hyp
term
  hyp
has type
  expr
but is expected to have type
  simp_lemmas
Additional information:
/Users/nima/Dropbox/Codes/Lean/Interval/tmp.lean:5:8: context: switched to simple application elaboration procedure because failed to use expected type to elaborate it, error message
  type mismatch, term
    (simp_hyp ?m_1 ?m_2 h
       {max_steps := simp.default_max_steps,
        contextual := ff,
        lift_eq := tt,
        canonize_instances := tt,
        canonize_proofs := ff,
        use_axioms := tt,
        zeta := tt,
        beta := tt,
        eta := tt,
        proj := tt,
        iota := tt,
        single_pass := ff,
        fail_if_unchanged := tt,
        memoize := tt})
  has type
    expr → tactic expr : Type
  but is expected to have type
    tactic ?m_1 : Type ?
</pre></div>

#### [ Simon Hudon (Mar 31 2018 at 03:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124437425):
<p>Sorry, the second version was wrong. I fixed it</p>

#### [ Nima (Mar 31 2018 at 03:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124437594):
<p>Is there any lean file that I can download from github to have the fix?</p>

#### [ Simon Hudon (Mar 31 2018 at 03:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124437603):
<p>I mean, this is what it should be:</p>
<div class="codehilite"><pre><span></span>meta def normalize_hyp (lemmas : list expr) (hyp : expr) : tactic unit :=
do s &lt;- simp_lemmas.append simp_lemmas.mk lemmas,
   try (simp_at s hyp)
</pre></div>

#### [ Nima (Mar 31 2018 at 03:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124437655):
<p>but <code>simp_at</code> gives me <code>unknown identifier 'simp_at' </code> error</p>

#### [ Simon Hudon (Mar 31 2018 at 03:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124437699):
<p>Sorry I keep making the same typo:</p>
<div class="codehilite"><pre><span></span>meta def normalize_hyp (lemmas : list expr) (hyp : expr) : tactic unit :=
do s &lt;- simp_lemmas.append simp_lemmas.mk lemmas,
   try (simp_hyp s hyp)
</pre></div>

#### [ Nima (Mar 31 2018 at 03:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124437706):
<p>This gives me the following error:</p>
<div class="codehilite"><pre><span></span>type mismatch at application
  simp_hyp s hyp
term
  hyp
has type
  expr
but is expected to have type
  opt_param (list name) list.nil
Additional information:
/Users/nima/Dropbox/Codes/Lean/Interval/tmp.lean:5:8: context: switched to simple application elaboration procedure because failed to use expected type to elaborate it, error message
  type mismatch, term
    (simp_hyp ?m_1 ?m_2 h
       {max_steps := simp.default_max_steps,
        contextual := ff,
        lift_eq := tt,
        canonize_instances := tt,
        canonize_proofs := ff,
        use_axioms := tt,
        zeta := tt,
        beta := tt,
        eta := tt,
        proj := tt,
        iota := tt,
        single_pass := ff,
        fail_if_unchanged := tt,
        memoize := tt})
  has type
    expr → tactic expr : Type
  but is expected to have type
    tactic ?m_1 : Type ?
</pre></div>

#### [ Simon Hudon (Mar 31 2018 at 03:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124437753):
<p>that's progress</p>

#### [ Simon Hudon (Mar 31 2018 at 03:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124437795):
<p>How about</p>
<div class="codehilite"><pre><span></span>meta def normalize_hyp (lemmas : list expr) (hyp : expr) : tactic unit :=
do s &lt;- simp_lemmas.append simp_lemmas.mk lemmas,
   try (simp_hyp s [] hyp)
</pre></div>

#### [ Nima (Mar 31 2018 at 03:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124437842):
<p>Wow! Thanks</p>

#### [ Simon Hudon (Mar 31 2018 at 03:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124437851):
<p>No problems. Sorry for the excessive back and forth.</p>

#### [ Mario Carneiro (Mar 31 2018 at 03:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124437890):
<p>I don't see <code>simp_at</code> in the lean web editor either. Is it in 3.3.0?</p>

#### [ Nima (Mar 31 2018 at 03:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124437950):
<p>No problem at all.<br>
I don't know how to check Lean version, mine is supposed to be 3.3.0.<br>
The same chapter gives me error. <br>
Last line <code> unknown identifier 'monad.for''</code><br>
Is there a magic fix for this one as well?</p>
<blockquote>
<p>The for' tactic, like the for tactic, applies the second argument to each element of the first, but it returns unit rather than accumulate the results in a list. </p>
</blockquote>
<div class="codehilite"><pre><span></span>open expr tactic classical monad

meta def normalize_hyp (lemmas : list expr) (hyp : expr) : tactic unit :=
do s &lt;- simp_lemmas.append simp_lemmas.mk lemmas,
   try (simp_hyp s [] hyp)

meta def normalize_hyps : tactic unit :=
do hyps ← local_context,
   lemmas ← monad.mapm mk_const [``not_not_intro],
   monad.for&#39; hyps (normalize_hyp lemmas)
</pre></div>

#### [ Simon Hudon (Mar 31 2018 at 03:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124437965):
<blockquote>
<p>I don't see <code>simp_at</code> in the lean web editor either. Is it in 3.3.0?</p>
</blockquote>
<p>It disappeared in <a href="https://github.com/leanprover/lean/commit/69ed291aab8493a7fb33b52dc2982e2db417761f" target="_blank" title="https://github.com/leanprover/lean/commit/69ed291aab8493a7fb33b52dc2982e2db417761f">https://github.com/leanprover/lean/commit/69ed291aab8493a7fb33b52dc2982e2db417761f</a><br>
in July</p>

#### [ Simon Hudon (Mar 31 2018 at 03:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124437997):
<p><span class="user-mention" data-user-id="112062">@Nima</span> you can check your version with <code>lean --version</code></p>

#### [ Simon Hudon (Mar 31 2018 at 03:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124438043):
<p>Instead of <code> monad.for' hyps (normalize_hyp lemmas) </code> try <code>hyps.mmap' (normalize_hyp lemmas)</code></p>

#### [ Nima (Mar 31 2018 at 03:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124438094):
<p>Fantastic!<br>
Thanks a lot,<br>
Also, my version is <code>Lean (version 3.3.0, commit fa9c868ed2bb, Release)</code></p>

#### [ Simon Hudon (Mar 31 2018 at 03:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124438145):
<p>Yeah, that's exactly 3.3.0</p>

#### [ Simon Hudon (Mar 31 2018 at 03:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124438148):
<p>Programming in Lean seems to be working with a pretty old version of Lean</p>

#### [ Nima (Mar 31 2018 at 06:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124442486):
<p>Sorry if this is too stupid, but why the following does not type-checks (I don't care the example itself) :</p>
<div class="codehilite"><pre><span></span>universe u
variable {α : Type u}
example (p:α → Prop) : (¬(∃ (a:α), ¬ p a)) → (∀ (a:α), p a) :=
begin
  intros h a,
  have h&#39; : (p a) → p a,
  from admit,
  admit
end
</pre></div>


<p>I get the following error at <code>have</code></p>
<div class="codehilite"><pre><span></span>type mismatch at application
  p a
term
  a
has type
  p a : Prop
but is expected to have type
  α : Type u
state:
α : Type u,
p : α → Prop,
h : ¬∃ (a : α), ¬p a,
a : α
⊢ p a
</pre></div>


<p>This is Tactic State right before <code>have</code></p>
<div class="codehilite"><pre><span></span>α : Type u,
p : α → Prop,
h : ¬∃ (a : α), ¬p a,
a : α
⊢ p a
</pre></div>

#### [ Simon Hudon (Mar 31 2018 at 06:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124442534):
<p>That's puzzling</p>

#### [ Mario Carneiro (Mar 31 2018 at 06:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124442585):
<p>You can't <code>from admit</code>, <code>admit</code> is a tactic not a term. Use <code>from sorry</code> or just <code>admit</code></p>

#### [ Simon Hudon (Mar 31 2018 at 06:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124442624):
<p>Dang! I completely missed that!</p>

#### [ Mario Carneiro (Mar 31 2018 at 06:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124442625):
<p>But the error is actually an issue with the variable <code>a</code> together with <code>p -&gt; q</code> instead of <code>\forall (_ : p), q</code></p>

#### [ Nima (Mar 31 2018 at 06:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124442632):
<p>So the following change gives me the same error:</p>
<div class="codehilite"><pre><span></span>have h&#39; : (p a) → (p a),
  admit,
  admit
</pre></div>

#### [ Mario Carneiro (Mar 31 2018 at 06:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124442672):
<p><a href="https://github.com/leanprover/lean/issues/1822" target="_blank" title="https://github.com/leanprover/lean/issues/1822">https://github.com/leanprover/lean/issues/1822</a></p>

#### [ Simon Hudon (Mar 31 2018 at 06:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124442673):
<p>Oooooooh! I had to stare a it for a while. I almost bore a whole through my monitor</p>

#### [ Mario Carneiro (Mar 31 2018 at 06:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124442681):
<p>You can work around the issue by writing <code>∀_:p a, p a</code> instead of <code>p a -&gt; p a</code></p>

#### [ Mario Carneiro (Mar 31 2018 at 06:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124442682):
<p>or use a variable other than <code>a</code></p>

#### [ Simon Hudon (Mar 31 2018 at 06:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124442723):
<p>Is there any plan to change that horrible convention to name that bound variable <code>a</code>?</p>

#### [ Mario Carneiro (Mar 31 2018 at 06:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124442724):
<p>I think? There are two separate autonaming approaches, one produces <code>a_n</code> and the other produces <code>_x_n</code></p>

#### [ Mario Carneiro (Mar 31 2018 at 06:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124442729):
<p>The underscore trick switches to the other naming convention</p>

#### [ Mario Carneiro (Mar 31 2018 at 06:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124442731):
<p>But it's never as simple as it seems for this stuff. See the issue</p>

#### [ Mario Carneiro (Mar 31 2018 at 06:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124442770):
<p>also <a href="https://github.com/leanprover/lean/pull/1844" target="_blank" title="https://github.com/leanprover/lean/pull/1844">https://github.com/leanprover/lean/pull/1844</a></p>

#### [ Simon Hudon (Mar 31 2018 at 06:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124442778):
<p>Yeah, don't I know it</p>

#### [ Mario Carneiro (Mar 31 2018 at 06:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124442779):
<p>Looks like Leo wanted to postpone a fix because of the new parser (sigh...)</p>

#### [ Simon Hudon (Mar 31 2018 at 06:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124442780):
<p>Thanks for the link</p>

#### [ Simon Hudon (Mar 31 2018 at 06:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124442822):
<p>I've heard that song before :D</p>

#### [ Simon Hudon (Mar 31 2018 at 06:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124442823):
<p>Here's hoping that the new parser also cures cancer :D</p>

#### [ Mario Carneiro (Mar 31 2018 at 06:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124442824):
<p>but don't bother with any medicine or chemotherapy in the meantime</p>

#### [ Kenny Lau (Mar 31 2018 at 06:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124442829):
<p>oh, what does double colon mean? as in, <code>{x : : p a}</code> something like that</p>

#### [ Mario Carneiro (Mar 31 2018 at 06:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124442830):
<p>that's malformed</p>

#### [ Kenny Lau (Mar 31 2018 at 06:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124442869):
<p><a href="https://github.com/leanprover/mathlib/pull/88#discussion_r178095763" target="_blank" title="https://github.com/leanprover/mathlib/pull/88#discussion_r178095763">https://github.com/leanprover/mathlib/pull/88#discussion_r178095763</a></p>

#### [ Kenny Lau (Mar 31 2018 at 06:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124442871):
<blockquote>
<p>what about <code>def next.fixed_point {x : : α} (H : x ≤ f x) : fixed_point</code> (in similar for previous) then you can shorten some proofs below.</p>
</blockquote>

#### [ Mario Carneiro (Mar 31 2018 at 06:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124442872):
<p>looks like a typo</p>

#### [ Kenny Lau (Mar 31 2018 at 06:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124442874):
<p>oh</p>

#### [ Nima (Mar 31 2018 at 06:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124443018):
<blockquote>
<p>But the error is actually an issue with the ...</p>
</blockquote>
<p><span class="user-mention" data-user-id="110049">@Mario Carneiro</span> I only understood that part, but it worked. So thank you  :)</p>

#### [ Simon Hudon (Mar 31 2018 at 07:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124443076):
<p>Basically, <code>have h' : (p a) → p a,</code> is the same as <code>have h' : ∀ a : p a, p a,</code> so the first <code>a</code> has type <code> α</code> and the second one has type <code>p a</code></p>

#### [ Nima (Mar 31 2018 at 07:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124443709):
<p>Thanks for the clarification,<br>
Some of the discussion on those links were about how Lean should choose name of the bounded variable in <code>∀ a : p ...</code>. Right? (I mean is it always <code>a</code> or starts with <code>a</code>, so if I don't start names with <code>a</code> then I will never see this problem again?)</p>

#### [ Mario Carneiro (Mar 31 2018 at 07:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124443809):
<p>Yes. Ideally it should be chosen to be distinct from the variables on the RHS, but for some reason this is complicated, so it just uses a name generator and you the user are responsible for not choosing the same name. You should beware of naming your variables <code>a</code>, <code>a_1</code>, <code>a_2</code> etc. as well as <code>_x</code>, <code>_x_1</code>, <code>_x_2</code> etc. Also <code>_inst</code> and <code>_match</code> and other underscore names are taken, so you should avoid starting your variables with an underscore.</p>

#### [ Kenny Lau (Mar 31 2018 at 09:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124447155):
<div class="codehilite"><pre><span></span>has type
  α → α → Prop : Type u
but is expected to have type
  α → α → Type ? : Type (max u (?+1))
</pre></div>

#### [ Kenny Lau (Mar 31 2018 at 09:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124447156):
<p>is Prop not a type?</p>

#### [ Kenny Lau (Mar 31 2018 at 09:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124447161):
<p>btw <code>plift</code> seems to have resolved the error</p>

#### [ Mario Carneiro (Mar 31 2018 at 09:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124447207):
<p>Prop is a Type, but Prop is not Type</p>

#### [ Kenny Lau (Mar 31 2018 at 09:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124447211):
<p>Prop is Type 0, no?</p>

#### [ Mario Carneiro (Mar 31 2018 at 09:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124447214):
<p>Prop is Sort 0, Type u is Sort (u+1)</p>

#### [ Kenny Lau (Mar 31 2018 at 09:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124447215):
<p>oh</p>

#### [ Kenny Lau (Mar 31 2018 at 10:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124447258):
<div class="codehilite"><pre><span></span>don&#39;t know how to synthesize placeholder
context:
α : Type u,
_inst_1 : partial_order α,
x y : α,
hxy : plift (x ≤ y)
⊢ {down := le_trans (hxy.down) ({down := le_refl y}.down)} = hxy
</pre></div>

#### [ Kenny Lau (Mar 31 2018 at 10:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124447262):
<p>proof irrelevance after plift...?</p>

#### [ Mario Carneiro (Mar 31 2018 at 10:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124447269):
<p>you have to case on <code>hxy</code> first</p>

#### [ Mario Carneiro (Mar 31 2018 at 10:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124447308):
<p>or rewrite with <code>plift.up_down</code></p>

#### [ Kenny Lau (Mar 31 2018 at 10:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124447315):
<p><code>congr_arg plift.up rfl</code> works</p>

#### [ Kenny Lau (Mar 31 2018 at 10:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124447316):
<p>after casing</p>

#### [ Kenny Lau (Mar 31 2018 at 10:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124447317):
<p><code> λ x y ⟨hxy⟩, congr_arg plift.up rfl</code></p>

#### [ Mario Carneiro (Mar 31 2018 at 10:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124447318):
<p>but <code>rfl</code> doesn't?</p>

#### [ Kenny Lau (Mar 31 2018 at 10:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124447354):
<p>I'm stupid</p>

#### [ Kenny Lau (Mar 31 2018 at 10:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124447355):
<p>it does</p>

#### [ Kenny Lau (Mar 31 2018 at 10:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124447362):
<p>interesting</p>

#### [ Kenny Lau (Mar 31 2018 at 10:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124447363):
<p>it goes assertion error without the casing</p>

#### [ Kenny Lau (Mar 31 2018 at 10:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124447364):
<p>but I've been getting too many assertion errors I decided to stop caring</p>

#### [ Mario Carneiro (Mar 31 2018 at 10:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124447372):
<p>hm, that's not a place I've seen an assertion error before</p>

#### [ Kenny Lau (Mar 31 2018 at 10:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124447461):
<p>is there polymorphic empty type?</p>

#### [ Kenny Lau (Mar 31 2018 at 10:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124447507):
<div class="codehilite"><pre><span></span>def empty : category empty :=
{ Mor := empty.rec _,
  Comp := empty.rec _,
  Id := empty.rec _,
  Hid_left := empty.rec _,
  Hid_right := empty.rec _,
  Hassoc := empty.rec _ }
</pre></div>

#### [ Kenny Lau (Mar 31 2018 at 10:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124447508):
<p>lol</p>

#### [ Mario Carneiro (Mar 31 2018 at 10:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124447548):
<p>Surprisingly no. You can use <code>ulift empty</code> in a pinch</p>

#### [ Kenny Lau (Mar 31 2018 at 10:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124447555):
<p>and yes, I'm doing category theory again</p>

#### [ Kenny Lau (Mar 31 2018 at 10:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124447600):
<p><code>λ x y z, unit.cases_on z rfl</code></p>

#### [ Kenny Lau (Mar 31 2018 at 10:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124447601):
<p>is there a way to case on <code>z</code> in the lambda part?</p>

#### [ Kenny Lau (Mar 31 2018 at 10:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124447641):
<div class="codehilite"><pre><span></span>def one : category unit :=
{ Mor := λ _ _, unit,
  Comp := λ _ _ _ _ _, unit.star,
  Id := λ _, unit.star,
  Hid_left := λ _ _, unit.rec rfl,
  Hid_right := λ _ _, unit.rec rfl,
  Hassoc := λ _ _ _ _ _ _ _, rfl }
</pre></div>

#### [ Mario Carneiro (Mar 31 2018 at 10:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124447688):
<p>you can write <code>()</code> in the lambda I think, or <code>⟨⟩</code></p>

#### [ Kenny Lau (Mar 31 2018 at 10:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124447693):
<p>the latter works</p>

#### [ Kenny Lau (Mar 31 2018 at 10:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124447782):
<div class="codehilite"><pre><span></span>def of_monoid (α : Type u) [monoid α] : category unit :=
{ Mor := λ _ _, α,
  Comp := λ _ _ _, (*),
  Id := λ _, 1,
  Hid_left := λ _ _, one_mul,
  Hid_right := λ _ _, mul_one,
  Hassoc := λ _ _ _ _, mul_assoc }
</pre></div>

#### [ Kenny Lau (Mar 31 2018 at 10:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124447783):
<p>how beautifully the structures are compatible</p>

#### [ Kenny Lau (Mar 31 2018 at 10:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124447841):
<div class="codehilite"><pre><span></span>def of_monoid (α : Type u) [monoid α] : category unit :=
{ Mor := λ _ _, α,
  Comp := λ _ _ _, (*),
  Id := λ _, 1,
  Hid_left := λ _ _, one_mul,
  Hid_right := λ _ _, mul_one,
  Hassoc := λ _ _ _ _, mul_assoc }

def to_monoid (C: category unit) : monoid (C.Mor () ()) :=
{ mul := C.Comp _ _ _,
  mul_assoc := C.Hassoc () () () (),
  one := C.Id (),
  one_mul := C.Hid_left () (),
  mul_one := C.Hid_right () () }
</pre></div>

#### [ Kenny Lau (Mar 31 2018 at 10:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124447878):
<p>this is very beautiful</p>

#### [ Mario Carneiro (Mar 31 2018 at 10:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124447888):
<p>I think you can do better in that last one... in any category, the homs from an object to itself forms a monoid</p>

#### [ Kenny Lau (Mar 31 2018 at 10:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124447931):
<div class="codehilite"><pre><span></span>def to_monoid {α : Type u} (C: category α) (x : α) : monoid (C.Mor x x) :=
{ mul := C.Comp _ _ _,
  mul_assoc := C.Hassoc x x x x,
  one := C.Id x,
  one_mul := C.Hid_left x x,
  mul_one := C.Hid_right x x }
</pre></div>

#### [ Kenny Lau (Mar 31 2018 at 10:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124447932):
<p>done</p>

#### [ Kenny Lau (Mar 31 2018 at 10:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124447974):
<p>I just realized the forgetful functor and its adjoint exists in Cat</p>

#### [ Kenny Lau (Mar 31 2018 at 10:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124448020):
<p>now <code>one</code> is a special case of <code>discrete</code></p>

#### [ Kenny Lau (Mar 31 2018 at 10:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124448021):
<div class="codehilite"><pre><span></span>def discrete (α : Type u) : category α :=
{ Mor := λ _ _, unit,
  Comp := λ _ _ _ _ _, (),
  Id := λ _, (),
  Hid_left := λ _ _ ⟨⟩, rfl,
  Hid_right := λ _ _ ⟨⟩, rfl,
  Hassoc := λ _ _ _ _ _ _ _, rfl }

def one : category unit :=
discrete unit
</pre></div>

#### [ Kenny Lau (Mar 31 2018 at 10:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124448022):
<p>ok technically zero also, but...</p>

#### [ Kenny Lau (Mar 31 2018 at 10:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124448023):
<div class="codehilite"><pre><span></span>def discrete (α : Type u) : category α :=
{ Mor := λ _ _, unit,
  Comp := λ _ _ _ _ _, (),
  Id := λ _, (),
  Hid_left := λ _ _ ⟨⟩, rfl,
  Hid_right := λ _ _ ⟨⟩, rfl,
  Hassoc := λ _ _ _ _ _ _ _, rfl }

def zero : category empty :=
discrete empty

def one : category unit :=
discrete unit
</pre></div>

#### [ Kenny Lau (Mar 31 2018 at 10:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124448158):
<p><span class="user-mention" data-user-id="110049">@Mario Carneiro</span>  how would you call the category <code>* -&gt; *</code> and the category <code>* =&gt; *</code>?</p>

#### [ Kenny Lau (Mar 31 2018 at 10:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124448159):
<p>(one arrow, two arrows)</p>

#### [ Mario Carneiro (Mar 31 2018 at 10:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124448161):
<p>what do they mean?</p>

#### [ Kenny Lau (Mar 31 2018 at 10:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124448162):
<p>the former is the category with 2 objects and 3 morphisms</p>

#### [ Mario Carneiro (Mar 31 2018 at 10:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124448202):
<p>that's <code>two</code></p>

#### [ Kenny Lau (Mar 31 2018 at 10:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124448203):
<p>and the latter is with 4 morphisms</p>

#### [ Mario Carneiro (Mar 31 2018 at 10:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124448205):
<p><code>two'</code>? <code>two_eq</code> (since it's the equalizer diagram)</p>

#### [ Kenny Lau (Mar 31 2018 at 10:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124448210):
<p>so it doesn't have a name in convention?</p>

#### [ Mario Carneiro (Mar 31 2018 at 10:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124448212):
<p>I've never seen it have an official name</p>

#### [ Kenny Lau (Mar 31 2018 at 10:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124448213):
<p>yes, I meant official. words.</p>

#### [ Kenny Lau (Mar 31 2018 at 10:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124448250):
<p>maybe <code>equalizer_diagram</code> lol</p>

#### [ Mario Carneiro (Mar 31 2018 at 10:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124448259):
<p>Alternatively <code>two_mor</code> since it's the canonical two morphism diagram</p>

#### [ Kenny Lau (Mar 31 2018 at 10:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124448260):
<p>what do you mean?</p>

#### [ Kenny Lau (Mar 31 2018 at 10:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124448261):
<p>and how are you going to name the pullback diagram</p>

#### [ Mario Carneiro (Mar 31 2018 at 10:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124448300):
<p><code>three_in</code> and <code>three_out</code>?</p>

#### [ Kenny Lau (Mar 31 2018 at 10:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124448301):
<p>hmm</p>

#### [ Kenny Lau (Mar 31 2018 at 10:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124448302):
<p>ok</p>

#### [ Kenny Lau (Mar 31 2018 at 10:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124448348):
<div class="codehilite"><pre><span></span>def Mor : bool → bool → Type
| ff ff := unit
| ff tt := bool
| tt ff := empty
| tt tt := unit
</pre></div>

#### [ Kenny Lau (Mar 31 2018 at 10:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124448349):
<p>do you want to switch <code>bool</code> and <code>empty</code>?</p>

#### [ Mario Carneiro (Mar 31 2018 at 10:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124448398):
<p>Hm, that seems a bit painful to work with</p>

#### [ Kenny Lau (Mar 31 2018 at 10:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124448400):
<p>how would you do it?</p>

#### [ Kenny Lau (Mar 31 2018 at 10:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124448441):
<div class="codehilite"><pre><span></span>def Mor : bool → bool → Type
| ff ff := unit
| ff tt := bool
| tt ff := empty
| tt tt := unit

def Comp : Π x y z : bool, Mor y z → Mor x y → Mor x z
| ff ff ff _ g := g
| ff ff tt f _ := f
| ff tt tt _ g := g
| tt tt tt _ _ := ()
</pre></div>

#### [ Mario Carneiro (Mar 31 2018 at 10:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124448446):
<div class="codehilite"><pre><span></span>inductive Mor : bool → bool → Type
| id : ∀ b, Mor b b
| par : bool → Mor ff tt
</pre></div>

#### [ Kenny Lau (Mar 31 2018 at 10:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124448452):
<p>heh...</p>

#### [ Kenny Lau (Mar 31 2018 at 10:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124448454):
<p>what does <code>par</code> stand for?</p>

#### [ Mario Carneiro (Mar 31 2018 at 10:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124448455):
<p>parallel</p>

#### [ Mario Carneiro (Mar 31 2018 at 10:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124448456):
<p>making up names is hard...</p>

#### [ Kenny Lau (Mar 31 2018 at 10:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124448496):
<p>eu entendo</p>

#### [ Mario Carneiro (Mar 31 2018 at 10:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124448540):
<p>It might be worth generalizing this example to a whole bouquet of parallel arrows indexed by <code>A</code></p>

#### [ Kenny Lau (Mar 31 2018 at 10:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124448542):
<p>fair enough</p>

#### [ Kenny Lau (Mar 31 2018 at 10:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124448543):
<p>would you like to do the hard job of naming it for me</p>

#### [ Mario Carneiro (Mar 31 2018 at 10:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124448544):
<p><code>par</code> :)</p>

#### [ Kenny Lau (Mar 31 2018 at 10:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124448545):
<p>wonderful</p>

#### [ Kenny Lau (Mar 31 2018 at 10:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124448546):
<div class="codehilite"><pre><span></span>inductive Mor : bool → bool → Type
| id : ∀ b, Mor b b
| par : bool → Mor ff tt

def Comp : Π x y z : bool, Mor y z → Mor x y → Mor x z
| ff ff _  f _ := f
| _  tt tt _ g := g
</pre></div>

#### [ Kenny Lau (Mar 31 2018 at 10:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124448549):
<p>two cases!</p>

#### [ Kenny Lau (Mar 31 2018 at 11:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124448782):
<div class="codehilite"><pre><span></span>namespace par

variable α : Type u

inductive Mor : bool → bool → Type u
| id : ∀ b, Mor b b
| par : α → Mor ff tt

def Comp : Π x y z, Mor α y z → Mor α x y → Mor α x z
| ff ff _  f _ := f
| _  tt tt _ g := g

def Hid_left : ∀ x y f, Comp α x y y (Mor.id α y) f = f
| ff ff (Mor.id α b) := rfl
| ff tt _ := rfl
| tt tt (Mor.id α b) := rfl

def Hid_right : ∀ x y f, Comp α x x y f (Mor.id α x) = f
| ff ff (Mor.id α b) := rfl
| ff tt _ := rfl
| tt tt (Mor.id α b) := rfl

def Hassoc : ∀ x y z w f g h, Comp α x y w (Comp α y z w f g) h = Comp α x z w f (Comp α x y z g h)
| ff ff _  _  _ _ _ := rfl
| ff tt tt tt _ _ _ := rfl
| tt tt tt tt _ _ _ := rfl

end par

def par (α : Type u) : category bool :=
{ Mor := par.Mor α,
  Comp := par.Comp α,
  Id := par.Mor.id α,
  Hid_left := par.Hid_left α,
  Hid_right := par.Hid_right α,
  Hassoc := par.Hassoc α }

def two_mor : category bool :=
par bool
</pre></div>

#### [ Kenny Lau (Mar 31 2018 at 11:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124448783):
<p><span class="user-mention" data-user-id="110049">@Mario Carneiro</span> do you see any possible golf on the casings?</p>

#### [ Mario Carneiro (Mar 31 2018 at 11:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124448833):
<p>I sometimes use secondary cases when a bunch of cases are the same; there isn't too much of that in this example but you could write <code>Hassoc</code> as</p>
<div class="codehilite"><pre><span></span>def Hassoc : ∀ x y z w f g h, Comp α x y w (Comp α y z w f g) h = Comp α x z w f (Comp α x y z g h)
| ff ff _  _  _ _ _ := rfl
| b tt tt tt _ _ _ := by cases b; refl
</pre></div>

#### [ Kenny Lau (Mar 31 2018 at 11:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124448872):
<p>well...</p>

#### [ Kenny Lau (Mar 31 2018 at 11:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124448874):
<p>that tactic was |unnecessary|</p>

#### [ Mario Carneiro (Mar 31 2018 at 11:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124448879):
<p>The advantage really shows itself when you need to deal with a wildcard case which abbreviates five identical cases with five identical proofs</p>

#### [ Kenny Lau (Mar 31 2018 at 11:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124448880):
<p>I see</p>

#### [ Mario Carneiro (Mar 31 2018 at 11:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124448921):
<p>it doesn't make the generated proof any shorter, but it's a slightly neater arrangement</p>

#### [ Kenny Lau (Mar 31 2018 at 11:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124448922):
<div class="codehilite"><pre><span></span>structure category (α : Type u) : Type (max u v + 1) :=
(Mor : Π x y : α, Type v)
(Comp : Π x y z, Mor y z → Mor x y → Mor x z)
(Id : Π x, Mor x x)
(Hid_left : ∀ x y (f : Mor x y), Comp _ _ _ (Id _) f = f)
(Hid_right : ∀ x y (f : Mor x y), Comp _ _ _ f (Id _) = f)
(Hassoc : ∀ x y z w (f : Mor z w) (g : Mor y z) (h : Mor x y), Comp _ _ _ (Comp _ _ _ f g) h = Comp _ _ _ f (Comp _ _ _ g h))
</pre></div>

#### [ Kenny Lau (Mar 31 2018 at 11:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124448923):
<p>I run into type problem when I try to define a cone</p>

#### [ Kenny Lau (Mar 31 2018 at 11:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124448924):
<p>namely, option</p>

#### [ Kenny Lau (Mar 31 2018 at 11:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124448929):
<p>the problem is the type of the morphism...</p>

#### [ Mario Carneiro (Mar 31 2018 at 11:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124448930):
<p>I was thinking about doing the same for the <code>Mor.id</code> cases in <code>Hid_left</code> and such but you need the cases there so that the <code>ff tt</code> case works</p>

#### [ Kenny Lau (Mar 31 2018 at 11:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124448973):
<p>wait</p>

#### [ Kenny Lau (Mar 31 2018 at 11:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124448974):
<div class="codehilite"><pre><span></span>def Mor : option α → option α → Type u_1
| none none := punit
| none (some y) := punit
| (some x) none := ulift empty
| (some x) (some y) := C.Mor x y
</pre></div>

#### [ Kenny Lau (Mar 31 2018 at 11:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124448975):
<p>how the hell does this work</p>

#### [ Kenny Lau (Mar 31 2018 at 11:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124448977):
<div class="codehilite"><pre><span></span>variables {α : Type u} (C : category α)
</pre></div>

#### [ Mario Carneiro (Mar 31 2018 at 11:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124448978):
<p>what's the problem?</p>

#### [ Kenny Lau (Mar 31 2018 at 11:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124448979):
<p>this is amazing</p>

#### [ Kenny Lau (Mar 31 2018 at 11:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124448980):
<p>I never defined <code>u_1</code></p>

#### [ Kenny Lau (Mar 31 2018 at 11:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124448982):
<p>it comes with <code>C</code>, but I never gave it a name</p>

#### [ Mario Carneiro (Mar 31 2018 at 11:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124448987):
<p>yeah, it's a really thin abstraction</p>

#### [ Kenny Lau (Mar 31 2018 at 11:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124448988):
<p>how does it work</p>

#### [ Mario Carneiro (Mar 31 2018 at 11:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124448990):
<p>also why <code>variables A B : Sort*</code> doesn't work</p>

#### [ Kenny Lau (Mar 31 2018 at 11:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124448991):
<p>it's unprecedented, the ability to have an unnamed name</p>

#### [ Mario Carneiro (Mar 31 2018 at 11:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124449030):
<p>Whenever you have a free universe variable in a <code>variable</code> declaration, it adds a <code>universe u_n</code> definition to the file and uses that</p>

#### [ Mario Carneiro (Mar 31 2018 at 11:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124449031):
<p>it's not magically named or a metavariable or anything</p>

#### [ Kenny Lau (Mar 31 2018 at 11:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124449049):
<div class="codehilite"><pre><span></span>inductive Mor : option α → option α → Type (max u u_1)
| id : ∀ y, Mor none y
| mor : ∀ x y (f : C.Mor x y), Mor (some x) (some y)
</pre></div>

#### [ Kenny Lau (Mar 31 2018 at 11:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124449050):
<p>why do I need <code>max</code> here but not that one?</p>

#### [ Kenny Lau (Mar 31 2018 at 11:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124449052):
<div class="codehilite"><pre><span></span>def Mor : option α → option α → Type u_1
| none none := punit
| none (some y) := punit
| (some x) none := ulift empty
| (some x) (some y) := C.Mor x y
</pre></div>

#### [ Mario Carneiro (Mar 31 2018 at 11:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124449108):
<p>I don't recommend using <code>u_1</code>, you should name your variables</p>

#### [ Kenny Lau (Mar 31 2018 at 11:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124449109):
<p>how would I do that?</p>

#### [ Mario Carneiro (Mar 31 2018 at 11:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124449111):
<p><code>universes u v</code>?</p>

#### [ Kenny Lau (Mar 31 2018 at 11:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124449150):
<p>no...</p>

#### [ Kenny Lau (Mar 31 2018 at 11:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124449153):
<div class="codehilite"><pre><span></span>structure category (α : Type u) : Type (max u v + 1) :=
(Mor : Π x y : α, Type v)
(Comp : Π x y z, Mor y z → Mor x y → Mor x z)
(Id : Π x, Mor x x)
(Hid_left : ∀ x y (f : Mor x y), Comp _ _ _ (Id _) f = f)
(Hid_right : ∀ x y (f : Mor x y), Comp _ _ _ f (Id _) = f)
(Hassoc : ∀ x y z w (f : Mor z w) (g : Mor y z) (h : Mor x y), Comp _ _ _ (Comp _ _ _ f g) h = Comp _ _ _ f (Comp _ _ _ g h))
</pre></div>

#### [ Kenny Lau (Mar 31 2018 at 11:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124449154):
<p>I can't name it</p>

#### [ Kenny Lau (Mar 31 2018 at 11:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124449155):
<p>it comes with the <code>Mor</code> of the category variable</p>

#### [ Kenny Lau (Mar 31 2018 at 11:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124449156):
<div class="codehilite"><pre><span></span>variables {α : Type u} (C : category α)
</pre></div>

#### [ Mario Carneiro (Mar 31 2018 at 11:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124449157):
<p>You can write universe arguments of a constant explicitly with <code>category.{u v}</code></p>

#### [ Kenny Lau (Mar 31 2018 at 11:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124449162):
<p>oh worked</p>

#### [ Kenny Lau (Mar 31 2018 at 11:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124449215):
<div class="codehilite"><pre><span></span>inductive Mor : option α → option α → Type (max u v)
| id : ∀ y, Mor none y
| mor : ∀ x y (f : C.Mor x y), Mor x y
</pre></div>

#### [ Kenny Lau (Mar 31 2018 at 11:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124449216):
<p><span class="user-mention" data-user-id="110049">@Mario Carneiro</span> the name <code>id</code> is morally wrong; how would you name it?</p>

#### [ Kenny Lau (Mar 31 2018 at 11:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124449217):
<p>maybe <code>proj</code></p>

#### [ Mario Carneiro (Mar 31 2018 at 11:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124449258):
<p>you should use <code>some</code> instead of the coercion</p>

#### [ Mario Carneiro (Mar 31 2018 at 11:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124449259):
<p>like you were before</p>

#### [ Kenny Lau (Mar 31 2018 at 11:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124449262):
<div class="codehilite"><pre><span></span>inductive Mor : option α → option α → Type (max u v)
| proj : ∀ y, Mor none y
| mor : ∀ x y (f : C.Mor x y), Mor (some x) (some y)
</pre></div>

#### [ Kenny Lau (Mar 31 2018 at 11:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124449263):
<p>this?</p>

#### [ Kenny Lau (Mar 31 2018 at 11:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124449266):
<p>komu eesu?</p>

#### [ Mario Carneiro (Mar 31 2018 at 11:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124449267):
<p>maybe just <code>none_le</code> or something like that?</p>

#### [ Kenny Lau (Mar 31 2018 at 11:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124449268):
<p>i don't like thinking it in a poset-manner</p>

#### [ Kenny Lau (Mar 31 2018 at 11:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124449269):
<p>about</p>

#### [ Mario Carneiro (Mar 31 2018 at 11:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124449314):
<p>I think this one should be defined with a <code>def</code>; that will fix the universe <code>max</code> thing</p>

#### [ Kenny Lau (Mar 31 2018 at 11:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124449315):
<p>what do you mean by "fix", is it a bug?</p>

#### [ Mario Carneiro (Mar 31 2018 at 11:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124449355):
<p>The problem is that lean isn't smart enough to notice that the <code>∀ y</code> in proj only fills out one morphism per type in the family</p>

#### [ Mario Carneiro (Mar 31 2018 at 11:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124449360):
<p>If you just try to push it all in a single inductive type, it overestimates the best universe</p>

#### [ Kenny Lau (Mar 31 2018 at 11:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124449489):
<div class="codehilite"><pre><span></span>def Mor : option α → option α → Type v
| none none := punit
| none (some y) := punit
| (some x) none := ulift empty
| (some x) (some y) := C.Mor x y

def Comp : Π x y z, Mor C y z → Mor C x y → Mor C x z
| none none _ f _ := f
| none _ (some z) _ _ := punit.star
| (some x) (some y) (some z) f g := C.Comp x y z f g
</pre></div>

#### [ Kenny Lau (Mar 31 2018 at 11:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124449490):
<p>the sky is blue again</p>

#### [ Kenny Lau (Mar 31 2018 at 11:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124449496):
<p><span class="user-mention" data-user-id="110049">@Mario Carneiro</span> what next, are you going to tell me that you can generalize <code>option</code> to <code>sum</code></p>

#### [ Mario Carneiro (Mar 31 2018 at 11:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124449536):
<div class="codehilite"><pre><span></span>def Mor : option α → option α → Type v
| none     y        := punit
| _        none     := ulift empty
| (some x) (some y) := C.Mor x y
</pre></div>

#### [ Kenny Lau (Mar 31 2018 at 11:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124449537):
<p>ok thanks</p>

#### [ Kenny Lau (Mar 31 2018 at 11:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124449543):
<p>ok it's really 3 equations</p>

#### [ Mario Carneiro (Mar 31 2018 at 11:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124449544):
<p>You can generalize option to sum, there are two interesting structures there - disjoint union and union where the left objects have morphisms to the right</p>

#### [ Mario Carneiro (Mar 31 2018 at 11:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124449586):
<p>but <code>option</code> is nicer to use than <code>sum punit</code></p>

#### [ Kenny Lau (Mar 31 2018 at 11:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124449587):
<div class="codehilite"><pre><span></span>def Mor : option α → option α → Type v
| none y := punit
| (some x) none := ulift empty
| (some x) (some y) := C.Mor x y

/-
._eqn_1 : ∀ {α : Type u} (C : category α) (y : option α), Mor C none y = punit
._eqn_2 : ∀ {α : Type u} (C : category α) (x : α), Mor C (some x) none = ulift empty
._eqn_3 : ∀ {α : Type u} (C : category α) (x y : α), Mor C (some x) (some y) = C.Mor x y
-/

def Mor : option α → option α → Type v
| none y := punit
| _ none := ulift empty
| (some x) (some y) := C.Mor x y

/-
._eqn_1 : ∀ {α : Type u} (C : category α), Mor C none none = punit
._eqn_2 : ∀ {α : Type u} (C : category α) (val : α), Mor C none (some val) = punit
._eqn_3 : ∀ {α : Type u} (C : category α) (val : α), Mor C (some val) none = ulift empty
._eqn_4 : ∀ {α : Type u} (C : category α) (x y : α), Mor C (some x) (some y) = C.Mor x y
-/
</pre></div>

#### [ Kenny Lau (Mar 31 2018 at 11:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124449592):
<p>por que pasa isso</p>

#### [ Kenny Lau (Mar 31 2018 at 11:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124449594):
<p>ok I know why I'm just exclaiming</p>

#### [ Mario Carneiro (Mar 31 2018 at 11:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124449633):
<p>¡</p>

#### [ Kenny Lau (Mar 31 2018 at 11:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124449678):
<p>pojish einteindeh si eu falu assii?</p>

#### [ Kenny Lau (Mar 31 2018 at 11:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124449685):
<p><span class="user-mention" data-user-id="110049">@Mario Carneiro</span></p>

#### [ Mario Carneiro (Mar 31 2018 at 11:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124449722):
<p>your portuguese is getting harder to read</p>

#### [ Kenny Lau (Mar 31 2018 at 11:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124449725):
<p>:P</p>

#### [ Kenny Lau (Mar 31 2018 at 11:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124449727):
<p>"podes entender se eu falo assim"</p>

#### [ Mario Carneiro (Mar 31 2018 at 11:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124449736):
<p>I think Nima had a similar issue the other day</p>

#### [ Kenny Lau (Mar 31 2018 at 11:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124449737):
<p>not understanding my portuguese?</p>

#### [ Mario Carneiro (Mar 31 2018 at 11:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124449774):
<p>something about the order of case splits causing superfluous splitting</p>

#### [ Kenny Lau (Mar 31 2018 at 11:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124449778):
<p>oh</p>

#### [ Kenny Lau (Mar 31 2018 at 11:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124449780):
<p>I could do disjoint union</p>

#### [ Kenny Lau (Mar 31 2018 at 11:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124449782):
<p>but I don't think there's this notion in the category theory community?</p>

#### [ Mario Carneiro (Mar 31 2018 at 11:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124449789):
<p>Have you coordinated with Scott?</p>

#### [ Kenny Lau (Mar 31 2018 at 11:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124449790):
<p>I mean, it is probably some universal objects in the category of categories</p>

#### [ Kenny Lau (Mar 31 2018 at 11:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124449791):
<p>no</p>

#### [ Mario Carneiro (Mar 31 2018 at 11:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124449792):
<p>The disjoint union is certainly the coproduct in Cat</p>

#### [ Kenny Lau (Mar 31 2018 at 11:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124449793):
<p>aha</p>

#### [ Kenny Lau (Mar 31 2018 at 11:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124449876):
<p>is there a shorthand for <code>punit.star</code>?</p>

#### [ Kenny Lau (Mar 31 2018 at 11:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124450072):
<p>why does <code>#check  Type  1000000</code> crash?</p>

#### [ Mario Carneiro (Mar 31 2018 at 11:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124450073):
<p>no, although you could open <code>punit</code></p>

#### [ Mario Carneiro (Mar 31 2018 at 11:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124450110):
<p>lol stop breaking lean</p>

#### [ Kenny Lau (Mar 31 2018 at 11:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124450113):
<p>I mean, it should be just a construct</p>

#### [ Kenny Lau (Mar 31 2018 at 11:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124450114):
<p>unless you're telling me that it creates an array with a million entries</p>

#### [ Kenny Lau (Mar 31 2018 at 11:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124450115):
<p>but most of them should be just empty?</p>

#### [ Mario Carneiro (Mar 31 2018 at 11:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124450116):
<p>I think it does something by recursion a million times and busts the stack</p>

#### [ Kenny Lau (Mar 31 2018 at 11:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124450118):
<p>hmm</p>

#### [ Kenny Lau (Mar 31 2018 at 11:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124450123):
<p>Is there a general construction that abstracts "from set to pointed set"?</p>

#### [ Kenny Lau (Mar 31 2018 at 12:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124450186):
<p>oh, it's just the coslice category isn't it</p>

#### [ Kenny Lau (Mar 31 2018 at 12:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124451065):
<div class="codehilite"><pre><span></span>def Cat : category Σ α : Type u, category.{u v} α :=
{ Mor := λ C D, functor C.2 D.2,
  Comp := λ C D E, functor.comp C.2 D.2 E.2,
  Id := λ C, functor.id C.2,
  Hid_left := λ C D F, by cases F; refl,
  Hid_right := λ C D F, by cases F; refl,
  Hassoc := λ _ _ _ _ _ _ _, rfl, }
</pre></div>

#### [ Kenny Lau (Mar 31 2018 at 12:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124451066):
<p>my life is now complete</p>

#### [ Kenny Lau (Mar 31 2018 at 13:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124452180):
<div class="codehilite"><pre><span></span>def comma {α : Type u} (C : category.{u v} α)
  {β : Type u₁} (D : category.{u₁ v₁} β)
  {γ : Type u₂} (E : category.{u₂ v₂} γ)
  (F : functor C E) (G : functor D E) :
  category Σ c d, E.Mor (F.F c) (G.F d) :=
{ Mor := λ x y, { P : C.Mor x.1 y.1 × D.Mor x.2.1 y.2.1 //
      E.Comp (F.F x.1) (F.F y.1) (G.F y.2.1) y.2.2 (F.mor x.1 y.1 P.1)
    = E.Comp (F.F x.1) (G.F x.2.1) (G.F y.2.1) (G.mor x.2.1 y.2.1 P.2) x.2.2 },
  Comp := λ x y z P Q, ⟨(C.Comp x.1 y.1 z.1 P.1.1 Q.1.1, D.Comp x.2.1 y.2.1 z.2.1 P.1.2 Q.1.2),
    by rw [← F.Hcomp, ← G.Hcomp, E.Hassoc, ← Q.2, ← E.Hassoc, P.2, E.Hassoc]⟩,
  Id := λ x, ⟨(C.Id x.1, D.Id x.2.1), by rw [F.Hid, G.Hid, E.Hid_left, E.Hid_right]⟩,
  Hid_left := λ x y P, subtype.eq $ by dsimp; rw [C.Hid_left, D.Hid_left]; cases P.1; refl,
  Hid_right := λ x y P, subtype.eq $ by dsimp; rw [C.Hid_right, D.Hid_right]; cases P.1; refl,
  Hassoc := λ x y z w P Q R, subtype.eq $ by dsimp; rw [C.Hassoc, D.Hassoc] }
</pre></div>


<p>Now I can have pointed sets :P</p>

#### [ Nima (Mar 31 2018 at 21:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124464151):
<p>How do we pass arguments to meta definition?<br>
The following does not typecheck</p>
<div class="codehilite"><pre><span></span>universe u
open tactic monad expr classical

meta def inst {α: Type u} (p:α → Prop) (h:∀ (n:α), p n) (a:α) : tactic unit :=
do skip

example {α:Type u} (b:α) (p:α → Prop) : (∀ (a:α), p a) → p b :=
begin
  intro h,
  have h&#39; : p b, from h b, -- I want the next line have does the same thing
  inst p h b, -- error: unknown identifier &#39;p&#39; &#39;h&#39; &#39;b&#39;
end
</pre></div>


<p>Tactic State:</p>
<div class="codehilite"><pre><span></span>α : Type u,
b : α,
p : α → Prop,
h : ∀ (a : α), p a,
h&#39; : p b
⊢ p b
</pre></div>

#### [ Simon Hudon (Mar 31 2018 at 21:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124464196):
<p>I believe there exists a tactic for what you're trying to do. I'm still going to assume that you want an answer to the question you actually asked</p>

#### [ Nima (Mar 31 2018 at 21:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124464258):
<p>I don't know such tactic, but sure, I would like to know an answer to what I asked.</p>

#### [ Simon Hudon (Mar 31 2018 at 21:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124464348):
<p>It is called <code>specialize</code>. It is pretty nice. </p>
<p>Let's put your tactic in its section because we need to open a bunch of namespaces:</p>
<div class="codehilite"><pre><span></span><span class="kn">section</span>
<span class="kn">open</span> <span class="n">tactic</span> <span class="n">interactive</span> <span class="n">interactive</span><span class="bp">.</span><span class="n">types</span> <span class="n">lean</span><span class="bp">.</span><span class="n">parser</span>

<span class="n">meta</span> <span class="n">def</span> <span class="n">inst</span> <span class="o">(</span><span class="n">fa</span> <span class="o">:</span> <span class="n">parse</span> <span class="n">texpr</span><span class="o">)</span> <span class="o">(</span><span class="n">x</span> <span class="o">:</span> <span class="n">parse</span> <span class="n">texpr</span><span class="o">)</span> <span class="o">:</span> <span class="n">tactic</span> <span class="n">unit</span> <span class="o">:=</span>
<span class="n">do</span> <span class="n">trace</span> <span class="n">fa</span><span class="o">,</span>
   <span class="n">trace</span> <span class="n">x</span>

<span class="kn">end</span>
</pre></div>

#### [ Simon Hudon (Mar 31 2018 at 21:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124464361):
<p>When you're given information to a tactic, you're basically giving them syntactic objects and you need provide a way for Lean to parse it. That's because you can invent a lot of different notations for your tactics.</p>

#### [ Nima (Mar 31 2018 at 21:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124464414):
<p>When I write <code>inst h b</code>, I still get the same error(?)</p>

#### [ Simon Hudon (Mar 31 2018 at 21:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124464460):
<p>I'm not sure it will solve anything but let's see if it does. Add the following between your tactic and your lemma:</p>
<div class="codehilite"><pre><span></span><span class="n">run_cmd</span> <span class="n">add_interactive</span> <span class="o">[</span><span class="bp">`</span><span class="n">inst</span><span class="o">]</span>
</pre></div>

#### [ Nima (Mar 31 2018 at 21:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124464516):
<p>Instead of the previous error, this gives me  error <code>expression expected </code>, error is below <code>b</code> in <code>inst h b</code></p>

#### [ Nima (Mar 31 2018 at 22:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124464668):
<p>Also, is there anyway I can use <code>specialize</code> on a <strong>goal</strong>  like <code>∃ (b : α), p b</code></p>

#### [ Simon Hudon (Mar 31 2018 at 22:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124464676):
<p>To your second question: no, you need <code>existsi</code> and you feel it your witness or a list of witnesses</p>

#### [ Simon Hudon (Mar 31 2018 at 22:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124464723):
<p>What if you erase <code>b</code> in <code>inst h b</code>?</p>

#### [ Nima (Mar 31 2018 at 22:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124464777):
<p>Here is the status:</p>
<div class="codehilite"><pre><span></span>universe u

section
open tactic interactive interactive.types lean.parser
meta def inst (fa : parse texpr) (x : parse texpr) : tactic unit :=
do trace fa,
   trace x
end
run_cmd add_interactive [`inst]

example {α:Type u} (b:α) (p:α → Prop) : (∀ (a:α), p a) → p b :=
begin
  intro h,
  inst h,  -- error: expression expected
  admit
end
</pre></div>

#### [ Simon Hudon (Mar 31 2018 at 22:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124464788):
<p>Ok, I get it. Sorry it took me a while. Lean seems <code>h b</code> as one expression in <code>inst h b</code> so we need a separator</p>

#### [ Simon Hudon (Mar 31 2018 at 22:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124464829):
<p>We could require the user to enter <code>inst (h, b)</code>, how does that look to you?</p>

#### [ Nima (Mar 31 2018 at 22:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124464839):
<p>Fine by me, but does that mean we should change definition of <code>inst</code>? (right now I am getting the same error)</p>

#### [ Simon Hudon (Mar 31 2018 at 22:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124464843):
<p>In that case, you'd define your tactic as:</p>
<div class="codehilite"><pre><span></span>meta def inst (fa : parse $ tk &quot;(&quot; *&gt; texpr &lt;* tk &quot;,&quot;)
              (x : parse $ texpr &lt;* tk &quot;)&quot;) : tactic unit :=
do trace fa,
   trace x

end
</pre></div>

#### [ Nima (Mar 31 2018 at 22:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124464845):
<p>wow! this is scary</p>

#### [ Simon Hudon (Mar 31 2018 at 22:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124464886):
<p><code>tk</code> and <code>texpr</code> are commands for the parser: literally "parse a parenthesis" and "parse an expression"</p>

#### [ Simon Hudon (Mar 31 2018 at 22:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124464934):
<p><code>&lt;*</code> and <code>*&gt;</code> is just to get them to be executed one after the other. <code>a &lt;* b</code> runs <code>a</code> first, then <code>b</code> and returns whatever <code>a</code> returns. <code>a *&gt; b</code> runs <code>a</code> first as well and then runs <code>b</code> and returns the result of <code>b</code></p>

#### [ Nima (Mar 31 2018 at 22:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124464941):
<p>I see, and <code>$</code> ?</p>

#### [ Simon Hudon (Mar 31 2018 at 22:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124464990):
<p>It's a way of making function application nicer by using fewer parentheses. If you'd write <code>f (g (h x))</code> instead you can write <code>f $ g $ h x</code></p>

#### [ Simon Hudon (Mar 31 2018 at 22:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124465039):
<p>So, instead of <code> parse $ tk "(" *&gt; texpr &lt;* tk "," </code>, one could write:</p>
<div class="codehilite"><pre><span></span><span class="n">parse</span>
   <span class="o">(</span><span class="n">do</span> <span class="n">tk</span> <span class="s2">&quot;(&quot;</span><span class="o">,</span>
       <span class="n">e</span> <span class="err">←</span> <span class="n">texpr</span><span class="o">,</span>
       <span class="n">tk</span> <span class="s2">&quot;,&quot;</span><span class="o">,</span>
       <span class="n">return</span> <span class="n">e</span><span class="o">)</span>
</pre></div>

#### [ Nima (Mar 31 2018 at 22:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124465047):
<p>We can only use <code>$</code> in meta world. Right?<br>
The following gives me error</p>
<div class="codehilite"><pre><span></span>def f (n:ℕ) := n+1
example : f $ f $ 1 = 3 := sorry
</pre></div>


<p>Error is:</p>
<div class="codehilite"><pre><span></span>type mismatch at application
  f (1 = 3)
term
  1 = 3
has type
  Prop
but is expected to have type
  ℕ
</pre></div>

#### [ Simon Hudon (Mar 31 2018 at 22:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124465095):
<p>No actually, it works everywhere. The problem with your expression is <code>f $ f 1</code> is of type <code>ℕ </code> but you're using it to specify the type of <code>example</code> it should have type <code>Sort u</code></p>

#### [ Simon Hudon (Mar 31 2018 at 22:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124465142):
<p>Now the problem is precedence: <code>$</code> has lower precedence than <code>=</code> and Lean reads your expression as <code>f (f (1 = 3))</code></p>

#### [ Nima (Mar 31 2018 at 22:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124465144):
<p>Nice, thanks a lot,<br>
Also, <code>existsi</code> you mentioned worked as a charm.</p>

#### [ Simon Hudon (Mar 31 2018 at 22:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124465151):
<p><code>$</code> won't make your expression nicer but if you applied <code>f</code> once more, you could write <code>f (f $ f 1) = 3</code> where you use <code>(</code> and <code>)</code> to "protect" <code>=</code> from <code>$</code>, in a sense</p>

#### [ Nima (Mar 31 2018 at 22:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124465245):
<p>I see, it is good to have an alternative to parenthesis</p>

#### [ Moses Schönfinkel (Mar 31 2018 at 22:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124465259):
<p>to be fair I would then do <code>example : (f ∘ f ∘ f) 1 = 4 := sorry</code> :)</p>

#### [ Moses Schönfinkel (Mar 31 2018 at 22:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124465306):
<p>it's an eternal Haskell bikeshed as to how to mix parens, composition, flip and low priority application :P</p>

#### [ Simon Hudon (Mar 31 2018 at 22:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124465522):
<p>I agree on second point, not on first. I prefer <code> f ∘ f ∘ f $ 1</code> if we're going to use <code>∘</code> to avoid parenthesis ... but in this case, it doesn't help</p>

#### [ Moses Schönfinkel (Mar 31 2018 at 22:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124465562):
<p>oh, you're absolutely right in this regard, it doesn't avoid the parens :)</p>

#### [ Moses Schönfinkel (Mar 31 2018 at 22:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124465563):
<p>in general I do prefer composition over anything else tho</p>

#### [ Nima (Apr 08 2018 at 05:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124784334):
<p>I know <code>exact fact p</code> finishes the proof, but how can I break it into the following two steps:<br>
1. add <code>fact</code> to my set of hypotheses (named <code>fa</code>)<br>
2. use <code>fa</code> to finish the proof</p>
<div class="codehilite"><pre><span></span>constant fact : ∀ (p:Prop), ¬p
example (p:Prop) : ¬p :=
begin
  exact fact p
end
</pre></div>


<p>Also, I used <code>constant</code> to define an axiom. Is this the usual method?</p>

#### [ Kenny Lau (Apr 08 2018 at 05:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124784341):
<p>we don't usually use <code>constant/axiom</code></p>

#### [ Mario Carneiro (Apr 08 2018 at 05:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124784342):
<p><code>have fa := fact, exact fa p</code></p>

#### [ Mario Carneiro (Apr 08 2018 at 05:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124784382):
<p>The usual method is not to add axioms at all. Usually it suffices to use <code>variable</code> instead, which adds the "axiom" as a precondition of the theorem</p>

#### [ Mario Carneiro (Apr 08 2018 at 05:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124784383):
<p>You can also use <code>apply fa</code> instead of <code>exact fa p</code> to finish the proof</p>

#### [ Kenny Lau (Apr 08 2018 at 05:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124784427):
<p>as a useless and obvious remark, your axiom is inconsistent:</p>

#### [ Kenny Lau (Apr 08 2018 at 05:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124784428):
<div class="codehilite"><pre><span></span>constant fact : ∀ (p:Prop), ¬p
example : false :=
begin
  apply fact (fact = fact),
  exact rfl
end
</pre></div>

#### [ Nima (Apr 08 2018 at 05:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124784429):
<p>If I have many axioms, isn't it going to be a problem?<br>
Suppose I define a lot of axioms to use in a project.<br>
But I am sure I am not going to use all of them in all of theorems.<br>
Isn't it considered a problem that I see all of them in my proof status?</p>

#### [ Kenny Lau (Apr 08 2018 at 05:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124784434):
<p>what are your axioms?</p>

#### [ Mario Carneiro (Apr 08 2018 at 05:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124784480):
<p>One way to manage a large collection of axioms is to bundle them all in a typeclass like <code>field A</code></p>

#### [ Mario Carneiro (Apr 08 2018 at 05:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124784487):
<p>If you use <code>variable</code> to declare your axioms, only the ones you actually use in a given theorem will be added as preconditions to the theorem</p>

#### [ Nima (Apr 08 2018 at 05:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124784530):
<blockquote>
<p>If you use <code>variable</code> to declare your axioms, only the ones you actually use in a given theorem will be added as preconditions to the theorem</p>
</blockquote>
<p>So in that case, what is the difference between constant and variable?</p>

#### [ Kenny Lau (Apr 08 2018 at 05:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124784578):
<p><code>constant</code> is global, in the sense that it is true once and for all</p>

#### [ Kenny Lau (Apr 08 2018 at 05:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124784587):
<p>whereas, e.g. <code>example : P -&gt; Q := sorry</code> is the same as</p>
<div class="codehilite"><pre><span></span>variable (h : P)
example : Q := sorry
</pre></div>

#### [ Kenny Lau (Apr 08 2018 at 05:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124784588):
<p><code>variable</code> is more like a local assumption</p>

#### [ Nima (Apr 08 2018 at 05:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124784629):
<p>I have not written any large collection of axioms, I am thinking of a <code>C++</code> type with a lot of constraints.<br>
If all these constraints are satisfied then the operations that I will define on this type make sense.<br>
So how should I define all type constraints so I can easily use them later? (obviously I am going to have more than one type)</p>

#### [ Kenny Lau (Apr 08 2018 at 05:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124784640):
<div class="codehilite"><pre><span></span>class module (α : out_param $ Type u) (β : Type v) [out_param $ ring α]
  extends has_scalar α β, add_comm_group β :=
(smul_add : ∀r (x y : β), r • (x + y) = r • x + r • y)
(add_smul : ∀r s (x : β), (r + s) • x = r • x + s • x)
(mul_smul : ∀r s (x : β), (r * s) • x = r • s • x)
(one_smul : ∀x : β, (1 : α) • x = x)
</pre></div>

#### [ Kenny Lau (Apr 08 2018 at 05:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124784641):
<p>make it a structure / class</p>

#### [ Simon Hudon (Apr 08 2018 at 05:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124784749):
<p>A <code>constant</code> / <code>axiom</code> (they're the same) is like you gained knowledge for free. With <code>variables</code>, <code>class</code> and <code>structure</code>, you get to assume certain properties but whatever you assume eventually has to be proved.</p>

#### [ Simon Hudon (Apr 08 2018 at 05:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124784821):
<p>If you have <code>variable h : false</code>, you can prove any theorem statement you want but using that theorem will be much more demanding. If you have <code>constant h : false</code>, you'll be able to prove all the theorems that you want and you'll never have to "pay" for such a strong assumption. That means that you may be building a bunch of nonsense. Especially if you have two or more axioms and you don't realize that they contradict each other</p>

#### [ Simon Hudon (Apr 08 2018 at 05:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124784910):
<p>(actually, I can't think of a use for a theorem that assumes false (with <code>variable</code>), it's probably useless but also harmless)</p>

#### [ Kenny Lau (Apr 08 2018 at 05:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124784913):
<p>you can never prove false, so you can never use that theorem</p>

#### [ Kenny Lau (Apr 08 2018 at 05:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124784914):
<p>oh wait</p>

#### [ Nima (Apr 08 2018 at 05:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124784918):
<p>So would you finish this example (if I use <code>constant</code> then I can do it):</p>
<div class="codehilite"><pre><span></span>variable h : false
example : ∀ (p:Prop), ¬ p :=  sorry
</pre></div>

#### [ Kenny Lau (Apr 08 2018 at 05:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124784919):
<p>that theorem is exactly <code>false.elim</code></p>

#### [ Mario Carneiro (Apr 08 2018 at 05:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124784922):
<p>I use <code>false.elim</code> all the time...</p>

#### [ Kenny Lau (Apr 08 2018 at 05:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124784923):
<p><code>false.elim h</code></p>

#### [ Simon Hudon (Apr 08 2018 at 05:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124784924):
<blockquote>
<p>I use <code>false.elim</code> all the time...</p>
</blockquote>
<p>Yes, me too but you only need one of those</p>

#### [ Mario Carneiro (Apr 08 2018 at 05:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124784961):
<p>What is true is that you don't really need anything other than <code>false.elim</code> in an inconsistent context</p>

#### [ Nima (Apr 08 2018 at 05:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124784964):
<p>I see, thanks</p>

#### [ Mario Carneiro (Apr 08 2018 at 05:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124784965):
<p>since it's like <code>sorry</code>, it's the best theorem</p>

#### [ Mario Carneiro (Apr 08 2018 at 05:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124784972):
<p>You can also write <code>h.elim</code> if <code>h : false</code> btw</p>

#### [ Nima (Apr 08 2018 at 05:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124785013):
<p>When I wasn't using <code>class</code>, I defined a constant for an operator and then define notation for it. How can I do the same for class?</p>
<div class="codehilite"><pre><span></span>universe u
class number(α : Type u) [linear_order α] :=
(neg₀ : α     → option α)

prefix `-₀`:40 := neg₀ -- won&#39;t type check
</pre></div>

#### [ Kenny Lau (Apr 08 2018 at 05:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124785015):
<p><code>number.neg_o</code></p>

#### [ Kenny Lau (Apr 08 2018 at 05:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124785021):
<p>not sure what you're trying to do though</p>

#### [ Kenny Lau (Apr 08 2018 at 05:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124785022):
<p>neg maps alpha to option alpha?</p>

#### [ Mario Carneiro (Apr 08 2018 at 05:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124785023):
<p>optional negation, I assume</p>

#### [ Mario Carneiro (Apr 08 2018 at 05:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124785024):
<p>something like <code>nat.ppred</code>?</p>

#### [ Nima (Apr 08 2018 at 05:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124785063):
<p>Excellent,<br>
Suppose I have a value of type <code>int</code> (in <code>C++</code>). Just because negation is defined it does not mean that I can take negation of every value. So I defined it to be something like this!</p>

#### [ Kenny Lau (Apr 08 2018 at 05:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124785065):
<p>but shouldn't that not be a field</p>

#### [ Kenny Lau (Apr 08 2018 at 05:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124785066):
<p>I mean, you don't want to permit any map from alpha to option alpha</p>

#### [ Mario Carneiro (Apr 08 2018 at 05:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124785071):
<p>Who said anything about it being a field?</p>

#### [ Kenny Lau (Apr 08 2018 at 05:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124785072):
<p>by field I mean a field of the class</p>

#### [ Kenny Lau (Apr 08 2018 at 05:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124785073):
<p>i.e. the things after <code>:=</code></p>

#### [ Mario Carneiro (Apr 08 2018 at 05:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124785074):
<p>what's wrong with specifying a negation operation like this?</p>

#### [ Kenny Lau (Apr 08 2018 at 05:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124785113):
<p>oh</p>

#### [ Kenny Lau (Apr 08 2018 at 05:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124785114):
<p>I thought it's like making int from nat</p>

#### [ Kenny Lau (Apr 08 2018 at 05:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124785115):
<p>misinterpreted</p>

#### [ Nima (Apr 08 2018 at 05:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124785258):
<p>Section 6.6 of Theorem Proving in Lean says</p>
<blockquote>
<p>They can also include subscripts, which can be entered by typing <code>\_</code> followed by the desired subscripted character</p>
</blockquote>
<p>I can only use single digits as subscript in VS Code. Am I missing something?</p>

#### [ Kenny Lau (Apr 08 2018 at 05:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124785259):
<p><code>\_m\_g</code></p>

#### [ Kenny Lau (Apr 08 2018 at 05:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124785260):
<p>you need to do it twice</p>

#### [ Nima (Apr 08 2018 at 05:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124785311):
<p>I type <code>m</code> then <code>\</code> then <code>_</code> them <code>m</code> then <code>\</code> then <code>_</code> then <code>g</code>then space <br>
I got: <code>m</code> followed by a box followed by a dash followed by <code>g</code></p>

#### [ Kenny Lau (Apr 08 2018 at 05:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124785350):
<p><code>\_m \_g </code></p>

#### [ Kenny Lau (Apr 08 2018 at 05:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124785351):
<p>space after <code>m</code></p>

#### [ Nima (Apr 08 2018 at 05:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124785358):
<p>I typed <code>m</code> then <code>\</code> then <code>_</code> them <code>m</code> then space then <code>\</code> then <code>_</code> then <code>g</code>then space  <br>
I got: <code>m</code> followed by a box followed by a space followed by dash followed by <code>g</code></p>

#### [ Kenny Lau (Apr 08 2018 at 05:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124785399):
<p>maybe <code>m</code> doesn't work then</p>

#### [ Kenny Lau (Apr 08 2018 at 05:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124785400):
<p><code>\_r \_g</code></p>

#### [ Kenny Lau (Apr 08 2018 at 05:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124785401):
<p>not every letter has subscript</p>

#### [ Kenny Lau (Apr 08 2018 at 05:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124785408):
<p>the point being, make each letter separately</p>

#### [ Nima (Apr 08 2018 at 05:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124785448):
<p>Thank, <code>r</code> worked</p>

#### [ Nima (Apr 08 2018 at 06:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124785544):
<p>Would you let me know why the following won't type check</p>
<div class="codehilite"><pre><span></span>universe u
class number(α : Type u) [linear_order α] :=
(neg₀ : α     → option α)
prefix `-₀`:40 := number.neg₀
example (α : Type u) [linear_order α] : ∀ (n:number α), (-₀ n) = (neg₀ n) := sorry
</pre></div>

#### [ Kenny Lau (Apr 08 2018 at 06:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124785546):
<p><code>number.neg_0 n</code></p>

#### [ Kenny Lau (Apr 08 2018 at 06:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124785547):
<p>or <code>n.neg_0</code></p>

#### [ Nima (Apr 08 2018 at 06:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124785599):
<p>oops!<br>
When I defined everything in terms of a class, then type of my operators don't make any sense</p>

#### [ Kenny Lau (Apr 08 2018 at 06:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124785603):
<p>how so?</p>

#### [ Nima (Apr 08 2018 at 06:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124785644):
<p>Ok, here is two errors I still receive</p>
<div class="codehilite"><pre><span></span>failed to synthesize type class instance for
α : Type u,
_inst_1 : linear_order α,
n : number α
⊢ linear_order (number α)
</pre></div>


<div class="codehilite"><pre><span></span>invalid field notation, function &#39;number.neg₀&#39; does not have explicit argument with type (number ...)
</pre></div>

#### [ Kenny Lau (Apr 08 2018 at 06:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124785645):
<p>right\</p>

#### [ Kenny Lau (Apr 08 2018 at 06:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124785646):
<p>aha</p>

#### [ Kenny Lau (Apr 08 2018 at 06:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124785647):
<p>you should have <code>[number \alpha]</code></p>

#### [ Kenny Lau (Apr 08 2018 at 06:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124785654):
<p>and then <code>\forall n:\alpha, -\_o n = number.neg\_o n</code></p>

#### [ Kenny Lau (Apr 08 2018 at 06:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124785696):
<p>but I would use <code>extends</code>:</p>
<div class="codehilite"><pre><span></span>universe u

class number (α : Type u) extends linear_order α :=
(neg₀ : α → option α)

prefix `-₀`:40 := number.neg₀

example (α : Type u) [number α] : ∀ (n:α), (-₀ n) = (number.neg₀ n) := λ _, rfl
</pre></div>

#### [ Simon Hudon (Apr 08 2018 at 06:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124785697):
<p>When going from an OO-ish language (like C++) to a functional language (like Lean and Haskell), one pitfall is that <code>class</code> don't mean the same thing anymore. In C++, a class defines a type while in Lean, a class is a sort of packet of information that can be inferred about your types</p>

#### [ Nima (Apr 08 2018 at 06:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124785789):
<p>Thanks, without <code>[linear_order α]</code> --&gt; <code>extends linear_order α</code> it would not type checked</p>

#### [ Kenny Lau (Apr 08 2018 at 06:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124785790):
<p>there's a way to do it without <code>extends</code>:</p>
<div class="codehilite"><pre><span></span>universe u

class number (α : Type u) [linear_order α] :=
(neg₀ : α → option α)

prefix `-₀`:40 := number.neg₀

example (α : Type u) [linear_order α] [number α] : ∀ (n:α), (-₀ n) = (number.neg₀ n) := λ _, rfl
</pre></div>

#### [ Kenny Lau (Apr 08 2018 at 06:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124785792):
<p>but I prefer the version with <code>extends</code></p>

#### [ Nima (Apr 08 2018 at 06:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124785807):
<p>Also, can I do something so instead of <code> _inst_1 : number α </code> I will get something like <code>hn : number α</code>?</p>

#### [ Kenny Lau (Apr 08 2018 at 06:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124785847):
<p>if you want to do that, you can, but you should also make it a structure</p>

#### [ Kenny Lau (Apr 08 2018 at 06:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124785851):
<div class="codehilite"><pre><span></span>universe u

class number (α : Type u) [linear_order α] :=
(neg₀ : α → option α)

prefix `-₀`:40 := number.neg₀

example (α : Type u) [linear_order α] [hn : number α] : ∀ (n:α), (-₀ n) = (number.neg₀ n) := λ _, rfl
</pre></div>

#### [ Nima (Apr 08 2018 at 06:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124785895):
<p>Awesome, thank you</p>

#### [ Nima (Apr 08 2018 at 06:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124786746):
<p>Sorry if it is too obvious, but how do you finish this example:</p>
<div class="codehilite"><pre><span></span>universe u
class  number(α : Type u) extends linear_order α := unit
example (α : Type u) [nn:number α] (a:α) (b:α) : (a&lt;b) → (a≤ b) := sorry
</pre></div>

#### [ Mario Carneiro (Apr 08 2018 at 06:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124786752):
<p><code>le_of_lt</code></p>

#### [ Kenny Lau (Apr 08 2018 at 06:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124786753):
<p><code>and.left</code> :-)</p>

#### [ Mario Carneiro (Apr 08 2018 at 06:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124786755):
<p>eww</p>

#### [ Mario Carneiro (Apr 08 2018 at 06:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124786756):
<p>actually that won't work now that I come to think of it</p>

#### [ Nima (Apr 08 2018 at 06:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124786805):
<p>Thanks, but I was thinking of how I can directly use <code>preorder.lt</code>?<br>
When I say <code>have hh:=nn.lt</code> all I get is <code> hh : α → α → Prop </code>. But <code>preorder.lt</code> is defined to be <code> (lt := λ a b, a ≤ b ∧ ¬ b ≤ a) </code></p>

#### [ Kenny Lau (Apr 08 2018 at 06:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124786844):
<p>use <code>let</code> instead of <code>have</code></p>

#### [ Kenny Lau (Apr 08 2018 at 06:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124786845):
<p><code>have</code> forgets definitions</p>

#### [ Mario Carneiro (Apr 08 2018 at 06:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124786846):
<p>This was also kenny's mistake - <code>preorder.lt</code> is not defined as that</p>

#### [ Mario Carneiro (Apr 08 2018 at 06:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124786847):
<p>that's only the default value</p>

#### [ Mario Carneiro (Apr 08 2018 at 06:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124786850):
<p>there is a second field that says that <code>preorder.lt</code> is equivalent to that, from which <code>le_of_lt</code> is proven</p>

#### [ Mario Carneiro (Apr 08 2018 at 06:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124786896):
<p>Perhaps you are oversimplifying your problem, but <code>le_of_lt</code> is certainly the way to solve the original question</p>

#### [ Nima (Apr 08 2018 at 07:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124786999):
<p>sure, I am trying to see how I can directly use all those properties defined for a class.<br>
I used <code>let hh := nn.lt</code> and got <code> hh : α → α → Prop := linear_order.lt </code>.<br>
Why does it say <code>linear_order</code> and not <code>preorder</code>?</p>
<div class="codehilite"><pre><span></span>class preorder (α : Type u) extends has_le α, has_lt α :=
(le_refl : ∀ a : α, a ≤ a)
(le_trans : ∀ a b c : α, a ≤ b → b ≤ c → a ≤ c)
(lt := λ a b, a ≤ b ∧ ¬ b ≤ a)
(lt_iff_le_not_le : ∀ a b : α, a &lt; b ↔ (a ≤ b ∧ ¬ b ≤ a) . order_laws_tac)

class partial_order (α : Type u) extends preorder α :=
(le_antisymm : ∀ a b : α, a ≤ b → b ≤ a → a = b)

class linear_order (α : Type u) extends partial_order α :=
(le_total : ∀ a b : α, a ≤ b ∨ b ≤ a)
</pre></div>

#### [ Mario Carneiro (Apr 08 2018 at 07:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124787296):
<p><code>linear_order.lt</code> extracts the <code>lt</code> field of a <code>linear_order</code>. It is defined in terms of <code>preorder.lt</code>, just composing with the parent structure conversions</p>

#### [ Nima (Apr 08 2018 at 07:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124787337):
<p>When <code>lt_iff_le_not_le</code> is defined for <code>preorder</code>, why do we need a lemma with same name for <code>preorder</code>?</p>

#### [ Mario Carneiro (Apr 08 2018 at 07:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124787343):
<p>If you know <code> number α</code>, then you can write <code>number.lt a b</code> where <code>a b : α</code> (you don't need to refer to <code>nn</code>) and it will refer to the <code>lt</code> field inherited from <code>preorder</code></p>

#### [ Mario Carneiro (Apr 08 2018 at 07:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124787383):
<p>The lemmas of a structure are often restated as separate theorems in order to get the notations and implicitness of arguments right</p>

#### [ Mario Carneiro (Apr 08 2018 at 07:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124787393):
<p>so for instance you can write <code>a &lt; b</code> where <code>a b : α</code> and it will find the <code>number</code> instance and work it back to the <code>preorder</code> that supplies the implementation of <code>&lt;</code></p>

#### [ Mario Carneiro (Apr 08 2018 at 07:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124787434):
<p>but this is not the same term as <code>number.lt a b</code> (it is definitionally equal), which can affect rewrites and things</p>

#### [ Nima (Apr 08 2018 at 07:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124787435):
<p><code>let hh := number.lt a b</code> gives me error: <code> unknown identifier 'number.lt' </code></p>

#### [ Mario Carneiro (Apr 08 2018 at 07:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124787444):
<p>The new structure command doesn't create <code>number.lt</code> type fields, it just has parent structure fields</p>

#### [ Mario Carneiro (Apr 08 2018 at 07:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124787446):
<p>the preferred way to refer to it is <code>a &lt; b</code> of course</p>

#### [ Mario Carneiro (Apr 08 2018 at 07:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124787486):
<p>but should be able to write <code>preorder.lt a b</code> or <code>linear_order.lt a b</code>.. they are all the same, definitionally</p>

#### [ Nima (Apr 08 2018 at 07:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124787575):
<p>I have no problem with <code>a&lt;b</code>. My problem is that I still don't know how to finish this example (how do I expand definition <code>nn.lt</code> or  <code>preorder.lt a b</code>,  I failed to do it using <code>rw</code>)? I don't care about the full proof, just how do I bring definition or the lemma itself into my hypotheses?</p>
<div class="codehilite"><pre><span></span>universe u
class number(α : Type u) extends linear_order α := unit
example (α : Type u) [nn:number α] (a:α) (b:α) : (a&lt;b) → (a≤ b) :=
begin
  intro less,
  let hh := nn.lt,
  admit
end
</pre></div>

#### [ Mario Carneiro (Apr 08 2018 at 07:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124787720):
<p>The relevant lemma is <code>lt_iff_le_not_le</code>, which you can refer to directly by <code>preorder.lt_iff_le_not_le</code> or through the restated version (which uses notation for le and lt). So the proof would be something like <code>(preorder.lt_iff_le_not_le _ _).1 less</code></p>

#### [ Mario Carneiro (Apr 08 2018 at 07:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124787762):
<p>Again, <code>nn.lt</code> <em>is not a definition</em>, despite the <code>:=</code>. It is a default value for a field, which is allowed to be anything. The reason we know it is in fact equivalent to that default value is because of <code>lt_iff_le_not_le</code>.</p>

#### [ Nima (Apr 08 2018 at 07:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124788049):
<blockquote>
<p>Again, <code>nn.lt</code> <em>is not a definition</em>, despite t...</p>
</blockquote>
<p>Very helpful, thank you.<br>
How can I  expand/replace <code> ≤ </code> to/with <code> preorder.le </code>?</p>

#### [ Kenny Lau (Apr 08 2018 at 07:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124788056):
<p><code>dsimp [( ≤ )]</code></p>

#### [ Nima (Apr 08 2018 at 07:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124788059):
<p>Nice</p>

#### [ Nima (Apr 08 2018 at 18:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124802900):
<p>How should I write the <code>match</code> so the whole thing will type-check?</p>
<div class="codehilite"><pre><span></span>universe u
class number(α : Type u) extends linear_order α :=
(min : option α)
(min_prop : match min with
            | none := true -- some predicate
            | sime m := true -- some predicate
            end)
</pre></div>

#### [ Kevin Buzzard (Apr 08 2018 at 18:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124802998):
<p>Some not sime</p>

#### [ Kenny Lau (Apr 08 2018 at 18:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124802999):
<p>still does not typecheck</p>

#### [ Kevin Buzzard (Apr 08 2018 at 18:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124803001):
<p>And brackets round some m</p>

#### [ Kevin Buzzard (Apr 08 2018 at 18:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124803003):
<p>That should do it</p>

#### [ Kenny Lau (Apr 08 2018 at 18:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124803004):
<p>nope</p>

#### [ Kenny Lau (Apr 08 2018 at 18:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124803007):
<p>I don't think you can do funny things inside that particular position</p>

#### [ Kevin Buzzard (Apr 08 2018 at 18:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124803012):
<p>Then we need the big guns to save us</p>

#### [ Nima (Apr 08 2018 at 18:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124803051):
<div class="codehilite"><pre><span></span>universe u
class number(α : Type u) extends linear_order α :=
(min : option α)
(min_prop : match min with
            | none := true -- some predicate
            | (some m) := true -- some predicate
            end)
</pre></div>


<p>gives me <code> invalid match/convoy expression, expected type is not known </code></p>

#### [ Kevin Buzzard (Apr 08 2018 at 18:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124803052):
<p>min might also mean something else</p>

#### [ Kenny Lau (Apr 08 2018 at 18:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124803053):
<div class="codehilite"><pre><span></span>universe u
class number(α : Type u) extends linear_order α :=
(min : option α)
(min_prop : @option.rec_on α (λ x, Prop) min true (λ x, true))
</pre></div>

#### [ Kenny Lau (Apr 08 2018 at 18:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124803054):
<p>this worked</p>

#### [ Kevin Buzzard (Apr 08 2018 at 18:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124803055):
<p>He is just rewriting the match into what lean expands it to</p>

#### [ Kevin Buzzard (Apr 08 2018 at 18:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124803063):
<p>Given the error</p>

#### [ Nima (Apr 08 2018 at 18:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124803065):
<p>To me <code>match</code> or <code>cases</code> are a lot more readable that <code>rec_on</code>.<br>
Is there any way to fix this and use <code>match</code>?</p>

#### [ Kevin Buzzard (Apr 08 2018 at 18:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124803106):
<p>Is the issue that lean needs to be told the type earlier on?</p>

#### [ Kenny Lau (Apr 08 2018 at 18:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124803107):
<p>I think so</p>

#### [ Nima (Apr 08 2018 at 19:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124804468):
<p>Any way I can fix the error message <code> failed to register private name '_match_2', prefix has not been registered </code> for this:</p>
<div class="codehilite"><pre><span></span>universe u
class number(α : Type u) extends linear_order α :=
(min : option α)
(max_prop : Prop := match min with
                    | none := true
                    | (some _) := true
                    end))
</pre></div>

#### [ Simon Hudon (Apr 08 2018 at 19:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124804999):
<p>Interesting. I'm not sure you can use <code>match</code> this way because it requires the creation of auxiliary definitions. You can try <code>option.cases_on min true (λ _, true)</code> instead or create a definition yourself that you refer to in that expression.</p>

#### [ Nima (Apr 08 2018 at 19:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124805183):
<p>I know <code>option.cases_on min true (λ _, true)</code> works, but to me <code>match</code> and <code>cases</code> are a lot more readable.<br>
I am just trying to define some property to my <code>class</code> and it seems impossible without using <code>cases_on</code> or <code>rec_on</code></p>

#### [ Simon Hudon (Apr 08 2018 at 19:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124805272):
<p>You can also do:</p>
<div class="codehilite"><pre><span></span>def max_prop_def (α : Type*) : option α -&gt; Prop
  | none := true
  | (some _) := true
</pre></div>


<p>And use <code>max_prop_def min</code> as your default value.</p>

#### [ Nima (Apr 08 2018 at 19:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124805367):
<p>Fantastic, thanks a lot!<br>
<code>Type*</code> means Type at some universe?</p>

#### [ Simon Hudon (Apr 08 2018 at 20:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124805679):
<p>Exactly! And Lean infers that universe for you</p>

#### [ Kevin Buzzard (Apr 08 2018 at 20:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124805978):
<p>you can also write <code>universe u</code> at the top and then <code>(alpha : Type u)</code>. It's like variables -- you are implicitly quantifying over universes.</p>

#### [ Mario Carneiro (Apr 08 2018 at 20:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124806249):
<p>I strongly recommend Simon's solution over inlining the match (even assuming you can get it to work). It might look nice up front, but as soon as you start using these properties in proofs, you will have to reference those internals</p>

#### [ Nima (Apr 08 2018 at 20:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124806595):
<p>Would you please tell me how I should change this, so it will type check?</p>
<div class="codehilite"><pre><span></span>inductive constraint (α:Type*)
| trv                                        : constraint
| stt (bnd:α) (low:Prop) (d : decidable low) : constraint

namespace constraint
def setof {α : Type*} [linear_order α] : constraint α → α → Prop
| (trv α)         a := true
| (stt bnd low d) a := if low then bnd&lt;a else a&lt;bnd -- ERROR: failed to synthesize type class instance for
</pre></div>

#### [ Simon Hudon (Apr 08 2018 at 20:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124806903):
<p>I'm not sure what <span class="user-mention" data-user-id="110049">@Mario Carneiro</span> will think of it but I propose:</p>
<div class="codehilite"><pre><span></span><span class="kn">inductive</span> <span class="n">bound</span> <span class="o">(</span><span class="n">α</span><span class="o">:</span><span class="kt">Type</span><span class="bp">*</span><span class="o">)</span>
<span class="bp">|</span> <span class="n">upper</span>  <span class="o">(</span><span class="n">bnd</span><span class="o">:</span><span class="n">α</span><span class="o">)</span> <span class="o">:</span> <span class="n">bound</span>
<span class="bp">|</span> <span class="n">lower</span>  <span class="o">(</span><span class="n">bnd</span><span class="o">:</span><span class="n">α</span><span class="o">)</span> <span class="o">:</span> <span class="n">bound</span>

<span class="n">def</span> <span class="kn">check</span> <span class="o">{</span><span class="n">α</span><span class="o">:</span><span class="kt">Type</span><span class="bp">*</span><span class="o">}</span> <span class="o">[</span><span class="n">decidable_linear_order</span>  <span class="n">α</span><span class="o">]</span> <span class="o">:</span> <span class="n">bound</span> <span class="n">α</span> <span class="bp">→</span> <span class="n">α</span> <span class="bp">→</span> <span class="n">bool</span>
<span class="bp">|</span> <span class="o">(</span><span class="n">bound</span><span class="bp">.</span><span class="n">lower</span> <span class="n">x</span><span class="o">)</span> <span class="n">y</span> <span class="o">:=</span> <span class="n">x</span> <span class="bp">&lt;</span> <span class="n">y</span>
<span class="bp">|</span> <span class="o">(</span><span class="n">bound</span><span class="bp">.</span><span class="n">upper</span> <span class="n">x</span><span class="o">)</span> <span class="n">y</span> <span class="o">:=</span> <span class="n">x</span> <span class="bp">&gt;</span> <span class="n">y</span>

<span class="kn">inductive</span> <span class="n">constraint</span> <span class="o">(</span><span class="n">α</span><span class="o">:</span><span class="kt">Type</span><span class="bp">*</span><span class="o">)</span>
<span class="bp">|</span> <span class="n">trv</span>                     <span class="o">:</span> <span class="n">constraint</span>
<span class="bp">|</span> <span class="n">stt</span> <span class="o">(</span><span class="n">bnd</span><span class="o">:</span><span class="n">bound</span> <span class="n">α</span><span class="o">)</span> <span class="o">:</span> <span class="n">constraint</span>

<span class="kn">namespace</span> <span class="n">constraint</span>
<span class="n">def</span> <span class="n">setof</span> <span class="o">{</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span><span class="bp">*</span><span class="o">}</span> <span class="o">[</span><span class="n">decidable_linear_order</span> <span class="n">α</span><span class="o">]</span> <span class="o">:</span> <span class="n">constraint</span> <span class="n">α</span> <span class="bp">→</span> <span class="n">α</span> <span class="bp">→</span> <span class="n">bool</span>
<span class="bp">|</span> <span class="o">(</span><span class="n">trv</span> <span class="n">α</span><span class="o">)</span>         <span class="n">a</span> <span class="o">:=</span> <span class="n">true</span>
<span class="bp">|</span> <span class="o">(</span><span class="n">stt</span> <span class="n">bnd</span><span class="o">)</span> <span class="n">a</span> <span class="o">:=</span> <span class="kn">check</span> <span class="n">bnd</span> <span class="n">a</span>
</pre></div>

#### [ Nima (Apr 08 2018 at 21:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124807220):
<p>Thanks for showing <code>lean</code> :)<br>
I have to think about/learn/understand your solution.<br>
In a meantime, is there a way to merge similar cases?<br>
Consider the following example</p>
<div class="codehilite"><pre><span></span><span class="kn">inductive</span> <span class="n">constraint</span> <span class="o">(</span><span class="n">α</span><span class="o">:</span><span class="kt">Type</span><span class="bp">*</span><span class="o">)</span>
<span class="bp">|</span> <span class="n">trv</span>        <span class="o">:</span> <span class="n">constraint</span>
<span class="bp">|</span> <span class="n">lt</span> <span class="o">(</span><span class="n">bnd</span><span class="o">:</span><span class="n">α</span><span class="o">)</span> <span class="o">:</span> <span class="n">constraint</span>
<span class="bp">|</span> <span class="n">le</span> <span class="o">(</span><span class="n">bnd</span><span class="o">:</span><span class="n">α</span><span class="o">)</span> <span class="o">:</span> <span class="n">constraint</span>
<span class="bp">|</span> <span class="n">gt</span> <span class="o">(</span><span class="n">bnd</span><span class="o">:</span><span class="n">α</span><span class="o">)</span> <span class="o">:</span> <span class="n">constraint</span>
<span class="bp">|</span> <span class="n">ge</span> <span class="o">(</span><span class="n">bnd</span><span class="o">:</span><span class="n">α</span><span class="o">)</span> <span class="o">:</span> <span class="n">constraint</span>

<span class="kn">open</span> <span class="n">constraint</span>
<span class="n">def</span> <span class="n">prop</span> <span class="o">(</span><span class="n">α</span><span class="o">:</span><span class="kt">Type</span><span class="bp">*</span><span class="o">)</span> <span class="o">:</span> <span class="n">constraint</span> <span class="n">α</span> <span class="bp">→</span> <span class="kt">Prop</span>
<span class="bp">|</span> <span class="o">(</span><span class="n">trv</span> <span class="n">α</span><span class="o">):=</span> <span class="n">true</span> <span class="c1">-- short term</span>
<span class="bp">|</span> <span class="o">(</span><span class="n">lt</span> <span class="bp">_</span><span class="o">)</span> <span class="o">:=</span> <span class="n">true</span> <span class="c1">-- very long term 1</span>
<span class="bp">|</span> <span class="o">(</span><span class="n">le</span> <span class="bp">_</span><span class="o">)</span> <span class="o">:=</span> <span class="n">true</span> <span class="c1">-- very long term 1</span>
<span class="bp">|</span> <span class="o">(</span><span class="n">gt</span> <span class="bp">_</span><span class="o">)</span> <span class="o">:=</span> <span class="n">true</span> <span class="c1">-- very long term 2</span>
<span class="bp">|</span> <span class="o">(</span><span class="n">ge</span> <span class="bp">_</span><span class="o">)</span> <span class="o">:=</span> <span class="n">true</span> <span class="c1">-- very long term 2</span>
</pre></div>


<p>Is there any way I use pattern matching and merge those cases where the right hand side is going to be the same?<br>
I know it is a long shot, but even better: may be cases for <code>lt</code> and <code>le</code> have a lot in common, <code>very_long ∧p1</code> and <code>very_long∧p2</code>.  Is there a way to effectively write something like </p>
<div class="codehilite"><pre><span></span><span class="n">def</span> <span class="n">prop</span> <span class="o">(</span><span class="n">α</span><span class="o">:</span><span class="kt">Type</span><span class="bp">*</span><span class="o">)</span> <span class="o">:</span> <span class="n">constraint</span> <span class="n">α</span> <span class="bp">→</span> <span class="kt">Prop</span>
<span class="bp">|</span> <span class="o">(</span><span class="n">trv</span> <span class="n">α</span><span class="o">):=</span> <span class="n">true</span> <span class="c1">-- short term</span>
<span class="bp">|</span> <span class="n">x</span><span class="o">:(</span><span class="n">lt</span> <span class="bp">_</span><span class="o">)</span> <span class="n">or</span> <span class="n">x</span><span class="o">:(</span><span class="n">le</span> <span class="bp">_</span><span class="o">)</span> <span class="o">:=</span> <span class="n">very_long</span> <span class="bp">∧</span> <span class="k">match</span> <span class="n">x</span> <span class="k">with</span> <span class="bp">|</span><span class="o">(</span><span class="n">lt</span> <span class="bp">_</span><span class="o">):=</span> <span class="n">p1</span> <span class="bp">|</span> <span class="o">(</span><span class="n">le</span> <span class="bp">_</span><span class="o">):=</span><span class="n">p2</span> <span class="kn">end</span>
<span class="bp">|</span> <span class="o">(</span><span class="n">gt</span> <span class="bp">_</span><span class="o">)</span> <span class="o">:=</span> <span class="n">true</span> <span class="c1">-- very long term 2</span>
<span class="bp">|</span> <span class="o">(</span><span class="n">ge</span> <span class="bp">_</span><span class="o">)</span> <span class="o">:=</span> <span class="n">true</span> <span class="c1">-- very long term 2</span>
</pre></div>

#### [ Simon Hudon (Apr 08 2018 at 21:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124807668):
<blockquote>
<p>Thanks for showing <code>lean</code></p>
</blockquote>
<p>My pleasure! I love sharing my excitement for Lean.</p>
<p>I would go back to the separation of <code>constraint</code> and <code>bound</code> and define <code>prop</code> as:</p>
<div class="codehilite"><pre><span></span><span class="kn">inductive</span> <span class="n">strictness</span>
<span class="bp">|</span> <span class="n">strict</span> <span class="bp">|</span> <span class="n">non_strict</span>

<span class="kn">inductive</span> <span class="n">bound</span> <span class="o">(</span><span class="n">α</span><span class="o">:</span><span class="kt">Type</span><span class="bp">*</span><span class="o">)</span>
<span class="bp">|</span> <span class="n">upper</span>  <span class="o">(</span><span class="n">bnd</span><span class="o">:</span><span class="n">α</span><span class="o">)</span> <span class="o">:</span> <span class="n">strictness</span> <span class="bp">→</span> <span class="n">bound</span>
<span class="bp">|</span> <span class="n">lower</span>  <span class="o">(</span><span class="n">bnd</span><span class="o">:</span><span class="n">α</span><span class="o">)</span> <span class="o">:</span> <span class="n">strictness</span> <span class="bp">→</span> <span class="n">bound</span>

<span class="kn">open</span> <span class="n">bound</span> <span class="n">strictness</span>
<span class="c1">-- ...</span>

<span class="n">def</span> <span class="n">prop</span> <span class="o">(</span><span class="n">α</span><span class="o">:</span><span class="kt">Type</span><span class="bp">*</span><span class="o">)</span> <span class="o">:</span> <span class="n">constraint</span> <span class="n">α</span> <span class="bp">→</span> <span class="kt">Prop</span>
<span class="bp">|</span> <span class="o">(</span><span class="n">trv</span> <span class="n">α</span><span class="o">):=</span> <span class="n">true</span> <span class="c1">-- short term</span>
<span class="bp">|</span> <span class="o">(</span><span class="n">stt</span> <span class="o">(</span><span class="n">lower</span> <span class="n">b</span> <span class="n">str</span><span class="o">))</span> <span class="o">:=</span> <span class="n">very_long</span> <span class="bp">∧</span> <span class="k">match</span> <span class="n">str</span> <span class="k">with</span> <span class="bp">|</span> <span class="n">strict</span><span class="o">:=</span> <span class="n">p1</span> <span class="bp">|</span> <span class="n">non_strict</span> <span class="o">:=</span><span class="n">p2</span> <span class="kn">end</span>
<span class="bp">|</span> <span class="o">(</span><span class="n">stt</span> <span class="o">(</span><span class="n">upper</span> <span class="n">b</span> <span class="n">str</span><span class="o">))</span> <span class="o">:=</span> <span class="c1">-- very long term 2</span>
</pre></div>

#### [ Simon Hudon (Apr 08 2018 at 21:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124807713):
<p>So the short answer is that you can't combine pattern matching and propositional notation. You can, however, try to get a bit closer and define functions like <code>is_strict</code> or <code>is_le</code> and use them in <code>if _ then _ else _</code>.</p>

#### [ Nima (Apr 08 2018 at 21:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124807940):
<p>Thanks a lot,<br>
About <code>[decidable_linear_order ℕ]</code><br>
At the intuitive level, does this mean if you give me two natural numbers, I can tell you which one is larger?<br>
I think the answer yes, but it should be no.<br>
For example, if you give me two natural number in <strong>binary format</strong> then comparing them is decidable. But who said you are going to always give them in binary format?<br>
So if I use <code>[decidable_linear_order ℕ]</code> in a definition, and use <code>classical</code> to find two numbers inside that definition, does that mean comparing them is decidable? (I think the answer should be no, but I don't know why)</p>

#### [ Simon Hudon (Apr 08 2018 at 21:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124808142):
<blockquote>
<p>At the intuitive level, does this mean if you give me two natural numbers, I can tell you which one is larger?</p>
</blockquote>
<p>Yes that's correct. </p>

#### [ Simon Hudon (Apr 08 2018 at 21:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124808241):
<blockquote>
<p>I think the answer yes, but it should be no.</p>
</blockquote>
<p>In Lean, no set of numbers are postulated (i.e. we say "let there be natural numbers" and they appear). Instead, each set of numbers is constructed as an inductive type. In particular, natural numbers are defined as follows:</p>
<div class="codehilite"><pre><span></span><span class="kn">inductive</span> <span class="n">nat</span>
<span class="bp">|</span> <span class="n">zero</span> <span class="o">:</span> <span class="n">nat</span>
<span class="bp">|</span> <span class="n">succ</span> <span class="o">:</span> <span class="n">nat</span> <span class="bp">-&gt;</span> <span class="n">nat</span>
</pre></div>


<p>You may recognize the structure of Peano's axiomatization of natural numbers. The big difference is that the above is a valid definition. Whenever you are given two natural numbers, they are given to you in unary notation (e.g. 11111 for 5, 111 for 3 and so on). This makes comparison decidable</p>

#### [ Simon Hudon (Apr 08 2018 at 21:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124808252):
<p>For the sake of performances however, the virtual machine and some tactics use binary representations (in the case of the vm, it's implemented by gmp, I believe)</p>

#### [ Simon Hudon (Apr 08 2018 at 21:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124808255):
<p>Is this what you were getting at?</p>

#### [ Nima (Apr 08 2018 at 21:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124808675):
<p>That makes sense, thanks.</p>

#### [ Nima (Apr 09 2018 at 00:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124812752):
<p>How can I finish the last definition?</p>
<div class="codehilite"><pre><span></span><span class="kn">open</span> <span class="n">nat</span>

<span class="kn">inductive</span> <span class="n">ind</span>
<span class="bp">|</span> <span class="n">emt</span> <span class="o">:</span> <span class="n">ind</span>
<span class="bp">|</span> <span class="n">val</span> <span class="o">(</span><span class="n">a</span><span class="o">:</span><span class="bp">ℕ</span><span class="o">)</span> <span class="o">:</span><span class="n">ind</span>
<span class="kn">open</span> <span class="n">ind</span>

<span class="n">def</span> <span class="n">is_nonempty</span> <span class="o">:</span> <span class="n">ind</span> <span class="bp">→</span> <span class="kt">Prop</span>
<span class="bp">|</span> <span class="n">emt</span>     <span class="o">:=</span> <span class="n">false</span>
<span class="bp">|</span> <span class="o">(</span><span class="n">val</span> <span class="bp">_</span><span class="o">)</span> <span class="o">:=</span> <span class="n">true</span>

<span class="n">def</span> <span class="n">valof</span> <span class="o">(</span><span class="n">i</span> <span class="o">:</span> <span class="n">ind</span><span class="o">)</span> <span class="o">(</span><span class="n">h</span> <span class="o">:</span> <span class="n">is_nonempty</span> <span class="n">i</span><span class="o">)</span> <span class="o">:</span> <span class="bp">ℕ</span> <span class="o">:=</span> <span class="k">match</span> <span class="n">i</span> <span class="k">with</span>
<span class="bp">|</span> <span class="o">(</span><span class="n">val</span> <span class="n">n</span><span class="o">)</span> <span class="o">:=</span> <span class="n">n</span>
<span class="bp">|</span> <span class="bp">_</span> <span class="o">:=</span> <span class="k">begin</span> <span class="n">admit</span> <span class="kn">end</span>
<span class="kn">end</span>
</pre></div>


<p>Status is </p>
<div class="codehilite"><pre><span></span>i : ind,
h : is_nonempty i,
_match : ind → ℕ,
_x : ind
⊢ ℕ
</pre></div>


<p>It seems <code>lean</code> forgot about the first case!</p>

#### [ Nima (Apr 09 2018 at 01:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124813315):
<p>I don't understand what the difference is, but it could be done using the following definition:</p>
<div class="codehilite"><pre><span></span><span class="n">def</span> <span class="n">valof</span> <span class="o">(</span><span class="n">i</span> <span class="o">:</span> <span class="n">ind</span><span class="o">)</span> <span class="o">(</span><span class="n">h</span> <span class="o">:</span> <span class="n">is_nonempty</span> <span class="n">i</span><span class="o">)</span> <span class="o">:</span> <span class="bp">ℕ</span> <span class="o">:=</span>
<span class="k">begin</span>
  <span class="n">cases</span> <span class="n">i</span><span class="o">,</span>
  <span class="n">rw</span> <span class="n">is_nonempty</span> <span class="n">at</span> <span class="n">h</span><span class="o">,</span>
  <span class="n">contradiction</span><span class="o">,</span>
  <span class="n">exact</span> <span class="n">a</span>
<span class="kn">end</span>
</pre></div>

#### [ Kevin Buzzard (Apr 09 2018 at 01:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124813425):
<p>Here's how to avoid the <code>a</code>:</p>

#### [ Kevin Buzzard (Apr 09 2018 at 01:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124813433):
<div class="codehilite"><pre><span></span><span class="n">def</span> <span class="n">valof</span> <span class="o">(</span><span class="n">i</span> <span class="o">:</span> <span class="n">ind</span><span class="o">)</span> <span class="o">(</span><span class="n">h</span> <span class="o">:</span> <span class="n">is_nonempty</span> <span class="n">i</span><span class="o">)</span> <span class="o">:</span> <span class="bp">ℕ</span> <span class="o">:=</span>
<span class="k">begin</span>
  <span class="n">cases</span> <span class="n">i</span> <span class="k">with</span> <span class="n">n</span><span class="o">,</span>
  <span class="o">{</span> <span class="n">exact</span> <span class="n">false</span><span class="bp">.</span><span class="n">elim</span> <span class="n">h</span> <span class="o">},</span>
  <span class="o">{</span> <span class="n">exact</span> <span class="n">n</span> <span class="o">}</span>
<span class="kn">end</span>
</pre></div>

#### [ Kevin Buzzard (Apr 09 2018 at 01:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124813486):
<p>After <code>cases</code> you have two goals, and it's encouraged to wrap them in curly brackets so you can deal with them one at a time (it helps with debugging later on when Leo changes everything and stuff stops working)</p>

#### [ Nima (Apr 09 2018 at 01:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124813493):
<p>what is wrong with <code>a</code>? <br>
Is it because <code>a</code> is used internally?</p>

#### [ Kevin Buzzard (Apr 09 2018 at 01:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124813835):
<p>the fact that Lean randomly calls variables a is considered a bug ;-)</p>

#### [ Kevin Buzzard (Apr 09 2018 at 01:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124813836):
<p>Not least because you might already have another variable called a!</p>

#### [ Kevin Buzzard (Apr 09 2018 at 01:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124813884):
<p><a href="https://github.com/leanprover/lean/issues/1822" target="_blank" title="https://github.com/leanprover/lean/issues/1822">https://github.com/leanprover/lean/issues/1822</a></p>

#### [ Kevin Buzzard (Apr 09 2018 at 01:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124813925):
<p>In Lean 4 your code will stop working but mine should be OK. In fact your code does not work for me -- which version of Lean are you using?</p>

#### [ Kevin Buzzard (Apr 09 2018 at 01:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124813927):
<p>I am on the nightly from 6th April.</p>

#### [ Kevin Buzzard (Apr 09 2018 at 01:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124813932):
<p>All my code does, of course, is explicitly names the variable when we do the case split.</p>

#### [ Nima (Apr 09 2018 at 01:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124813984):
<p>Lean (version 3.3.0, commit fa9c868ed2bb, Release)</p>

#### [ Kevin Buzzard (Apr 09 2018 at 01:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124814034):
<p>v3.4 is coming soon. A lot has happened since 3.3.</p>

#### [ Kevin Buzzard (Apr 09 2018 at 01:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124814079):
<p>Oh, this works for me:</p>

#### [ Kevin Buzzard (Apr 09 2018 at 01:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124814083):
<div class="codehilite"><pre><span></span><span class="n">def</span>  <span class="n">valof&#39;</span> <span class="o">:</span> <span class="bp">Π</span> <span class="o">(</span><span class="n">i</span> <span class="o">:</span> <span class="n">ind</span><span class="o">),</span> <span class="n">is_nonempty</span> <span class="n">i</span> <span class="bp">→</span> <span class="bp">ℕ</span>
<span class="bp">|</span> <span class="o">(</span><span class="n">val</span> <span class="n">n</span><span class="o">)</span> <span class="n">h</span> <span class="o">:=</span> <span class="n">n</span>
<span class="bp">|</span> <span class="n">emt</span> <span class="n">h</span> <span class="o">:=</span> <span class="n">false</span><span class="bp">.</span><span class="n">elim</span> <span class="n">h</span>
</pre></div>

#### [ Kevin Buzzard (Apr 09 2018 at 01:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124814089):
<p>The equation compiler is apparently more clever than match</p>

#### [ Kevin Buzzard (Apr 09 2018 at 01:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124814129):
<p>that can't be right because they are the same thing. The difference is that I am getting h involved in the matching process here.</p>

#### [ Kevin Buzzard (Apr 09 2018 at 01:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124814192):
<div class="codehilite"><pre><span></span><span class="n">def</span>  <span class="n">valof</span> <span class="o">(</span><span class="n">i</span> <span class="o">:</span> <span class="n">ind</span><span class="o">)</span> <span class="o">(</span><span class="n">h</span> <span class="o">:</span> <span class="n">is_nonempty</span> <span class="n">i</span><span class="o">)</span> <span class="o">:</span> <span class="bp">ℕ</span> <span class="o">:=</span>  <span class="k">match</span> <span class="n">i</span><span class="o">,</span><span class="n">h</span> <span class="k">with</span>
<span class="bp">|</span> <span class="o">(</span><span class="n">val</span> <span class="n">n</span><span class="o">),</span> <span class="n">h</span> <span class="o">:=</span> <span class="n">n</span>
<span class="bp">|</span> <span class="n">emt</span><span class="o">,</span> <span class="n">h</span> <span class="o">:=</span> <span class="n">false</span><span class="bp">.</span><span class="n">elim</span> <span class="n">h</span>
<span class="kn">end</span>
</pre></div>

#### [ Kevin Buzzard (Apr 09 2018 at 01:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124814194):
<p>You need to tell the equation compiler about h explicitly, so it seems.</p>

#### [ Nima (Apr 09 2018 at 01:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124814735):
<p>Thanks, your solution worked for me,<br>
But I did not understand why I should use <code>h</code> in the match (I know it won't type-check without it, but I don't know why)</p>

#### [ Nima (Apr 09 2018 at 02:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124815048):
<p>How can I mark result Prop decidable?</p>
<div class="codehilite"><pre><span></span><span class="n">def</span> <span class="n">func</span><span class="o">(</span><span class="n">p</span><span class="o">:</span><span class="kt">Prop</span><span class="o">)[</span><span class="n">decidable</span> <span class="n">p</span><span class="o">]</span> <span class="o">:</span> <span class="kt">Prop</span> <span class="o">:=</span> <span class="n">p</span>
<span class="kn">example</span> <span class="o">(</span><span class="n">p</span><span class="o">:</span><span class="kt">Prop</span><span class="o">)[</span><span class="n">decidable</span> <span class="n">p</span><span class="o">]</span> <span class="o">:</span> <span class="k">if</span> <span class="o">(</span><span class="n">func</span> <span class="n">p</span><span class="o">)</span> <span class="k">then</span> <span class="n">true</span> <span class="k">else</span> <span class="n">false</span> <span class="o">:=</span> <span class="n">sorry</span> <span class="c1">-- won&#39;t type check</span>
</pre></div>

#### [ Kevin Buzzard (Apr 09 2018 at 02:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124815254):
<div class="codehilite"><pre><span></span><span class="n">def</span> <span class="n">func</span> <span class="o">(</span><span class="n">p</span><span class="o">:</span><span class="kt">Prop</span><span class="o">)</span> <span class="o">:</span> <span class="kt">Prop</span> <span class="o">:=</span> <span class="n">p</span>

<span class="kn">instance</span> <span class="n">func_of_decidable_is_decidable</span> <span class="o">(</span><span class="n">p</span> <span class="o">:</span> <span class="kt">Prop</span><span class="o">)</span> <span class="o">[</span><span class="n">H</span> <span class="o">:</span> <span class="n">decidable</span> <span class="n">p</span><span class="o">]</span> <span class="o">:</span> <span class="n">decidable</span> <span class="o">(</span><span class="n">func</span> <span class="n">p</span><span class="o">)</span> <span class="o">:=</span> <span class="n">H</span>

<span class="kn">example</span> <span class="o">(</span><span class="n">p</span><span class="o">:</span><span class="kt">Prop</span><span class="o">)</span> <span class="o">[</span><span class="n">decidable</span> <span class="n">p</span><span class="o">]</span> <span class="o">:</span> <span class="k">if</span> <span class="o">(</span><span class="n">func</span> <span class="n">p</span><span class="o">)</span> <span class="k">then</span> <span class="n">true</span> <span class="k">else</span> <span class="n">false</span> <span class="o">:=</span> <span class="n">sorry</span>
</pre></div>

#### [ Kevin Buzzard (Apr 09 2018 at 02:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124815294):
<p>I explain to the type class inference system that it should spot that if p is decidable then func p is too.</p>

#### [ Nima (Apr 09 2018 at 02:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124815298):
<p>Great, thanks</p>

#### [ Kevin Buzzard (Apr 09 2018 at 02:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124815365):
<p>As for the equation compiler question (why it's not smart enough to make deductions about h) -- I'm afraid that's beyond my pay grade. You can see in your begin/end attempt that by the time we've got to the right of the colon-equals, Lean doesn't even seem to know that i is emt -- even if you explicitly write that it is -- so it can't make any deductions about h.</p>

#### [ Simon Hudon (Apr 09 2018 at 02:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124815524):
<p>I think that when you match on both <code>i</code> and <code>h</code>, it allows Lean to change the type of <code>h</code> (or rather, its patterns) to reflect that you're matching on <code>i</code>. In the first branch, <code>h : is_empty (val n)</code> and in the second, <code>h : is_empty emt</code>. After that, we have definitional equality with <code>false</code> (resp. <code>true</code>) by simply unfolding <code>is_empty</code></p>

#### [ Simon Hudon (Apr 09 2018 at 02:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124815579):
<p>With regards to decidable, when a function returns <code>true</code> or <code>false</code> and then that you need it to be decidable, you can use <code>bool</code> instead and it will be automatically decidable because there is an implicit conversion from <code>bool</code> to <code>Prop</code> and the resulting <code>Prop</code> is decidable.</p>

#### [ Nima (Apr 09 2018 at 02:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124815709):
<p>How do I prove <code>decidable true</code>?<br>
Regarding using <code>bool</code>, it works, but then either I have write <code>p=tt</code> or I will see the left symbol <code>↥p</code> everywhere (not sure how comfortable I am with that, or how much trouble it is going to cause me later).</p>

#### [ Kevin Buzzard (Apr 09 2018 at 02:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124815760):
<p><code>decidable true</code> has type <code>Type</code>so I'm not sure you can prove it.</p>

#### [ Kevin Buzzard (Apr 09 2018 at 02:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124815761):
<p>Here's the definition of decidable -- it's an inductive type.</p>

#### [ Kevin Buzzard (Apr 09 2018 at 02:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124815801):
<div class="codehilite"><pre><span></span>class inductive decidable (p : Prop)
| is_false (h : ¬p) : decidable
| is_true  (h : p) : decidable
</pre></div>

#### [ Kevin Buzzard (Apr 09 2018 at 02:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124815802):
<p>So you have two constructors, <code>is_true</code> and <code>is_false</code></p>

#### [ Kevin Buzzard (Apr 09 2018 at 02:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124815813):
<p><code>#check is_true trivial -- decidable true</code></p>

#### [ Kevin Buzzard (Apr 09 2018 at 02:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124815856):
<p><code>true</code> is a Prop and <code>trivial</code> is a proof of <code>true</code></p>

#### [ Nima (Apr 09 2018 at 02:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124815867):
<p>So if output of a function is either <code>true</code> or <code>false</code>, how do I say this output is decidable (without going to <code>bool</code>)? From what you just said, what I am trying to write in <code>lean</code> does not even make sense. Right?</p>
<div class="codehilite"><pre><span></span><span class="n">def</span> <span class="n">func</span><span class="o">(</span><span class="n">p</span><span class="o">:</span><span class="kt">Prop</span><span class="o">)[</span><span class="n">decidable</span> <span class="n">p</span><span class="o">]</span> <span class="o">:</span> <span class="kt">Prop</span> <span class="o">:=</span> <span class="n">true</span>
<span class="kn">example</span> <span class="o">(</span><span class="n">p</span><span class="o">:</span><span class="kt">Prop</span><span class="o">)[</span><span class="n">decidable</span> <span class="n">p</span><span class="o">]</span> <span class="o">:</span> <span class="k">if</span> <span class="o">(</span><span class="n">func</span> <span class="n">p</span><span class="o">)</span> <span class="k">then</span> <span class="n">true</span> <span class="k">else</span> <span class="n">false</span> <span class="o">:=</span> <span class="n">sorry</span> <span class="c1">-- won&#39;t type check</span>
</pre></div>

#### [ Kevin Buzzard (Apr 09 2018 at 02:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124815916):
<p>Well you have to prove that the output is either true or false, and then you can make an instance of the decidable class by using is_false if it's false and is_true if it's true</p>

#### [ Kevin Buzzard (Apr 09 2018 at 02:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124815978):
<p>Take a look at how core Lean proves that less than or equal to is decidable on nat</p>

#### [ Kevin Buzzard (Apr 09 2018 at 02:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124815981):
<div class="codehilite"><pre><span></span><span class="kn">instance</span> <span class="n">decidable_le</span> <span class="o">:</span> <span class="bp">∀</span> <span class="n">a</span> <span class="n">b</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">,</span> <span class="n">decidable</span> <span class="o">(</span><span class="n">a</span> <span class="bp">≤</span> <span class="n">b</span><span class="o">)</span>
<span class="bp">|</span> <span class="mi">0</span>     <span class="n">b</span>     <span class="o">:=</span> <span class="n">is_true</span> <span class="o">(</span><span class="n">zero_le</span> <span class="n">b</span><span class="o">)</span>
<span class="bp">|</span> <span class="o">(</span><span class="n">a</span><span class="bp">+</span><span class="mi">1</span><span class="o">)</span> <span class="mi">0</span>     <span class="o">:=</span> <span class="n">is_false</span> <span class="o">(</span><span class="n">not_succ_le_zero</span> <span class="n">a</span><span class="o">)</span>
<span class="bp">|</span> <span class="o">(</span><span class="n">a</span><span class="bp">+</span><span class="mi">1</span><span class="o">)</span> <span class="o">(</span><span class="n">b</span><span class="bp">+</span><span class="mi">1</span><span class="o">)</span> <span class="o">:=</span>
  <span class="k">match</span> <span class="n">decidable_le</span> <span class="n">a</span> <span class="n">b</span> <span class="k">with</span>
  <span class="bp">|</span> <span class="n">is_true</span> <span class="n">h</span>  <span class="o">:=</span> <span class="n">is_true</span> <span class="o">(</span><span class="n">succ_le_succ</span> <span class="n">h</span><span class="o">)</span>
  <span class="bp">|</span> <span class="n">is_false</span> <span class="n">h</span> <span class="o">:=</span> <span class="n">is_false</span> <span class="o">(</span><span class="bp">λ</span> <span class="n">a</span><span class="o">,</span> <span class="n">h</span> <span class="o">(</span><span class="n">le_of_succ_le_succ</span> <span class="n">a</span><span class="o">))</span>
  <span class="kn">end</span>
</pre></div>

#### [ Kevin Buzzard (Apr 09 2018 at 02:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124816022):
<p>Given the statement <code>a &lt;= b</code> it either proves that it's true or proves that it's false, and in each case it creates an instance of <code>decidable (a &lt;= b)</code></p>

#### [ Kevin Buzzard (Apr 09 2018 at 02:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124816028):
<p>using the <code>is_true</code> or <code>is_false</code> constructors</p>

#### [ Kevin Buzzard (Apr 09 2018 at 02:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124816073):
<p>things like <code>nat.zero_le</code> are lemmas in Lean (that one says "forall n, 0 &lt;= n")</p>

#### [ Kevin Buzzard (Apr 09 2018 at 02:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124816076):
<p>Earlier in the file they must have written "open nat" so you don't have to keep writing "nat."</p>

#### [ Nima (Apr 09 2018 at 02:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124816172):
<p>Sorry, but I still cannot figure out how to make this example work without going to <code>bool</code></p>
<div class="codehilite"><pre><span></span><span class="n">def</span> <span class="n">func</span><span class="o">(</span><span class="n">p</span><span class="o">:</span><span class="kt">Prop</span><span class="o">)</span> <span class="o">:</span> <span class="kt">Prop</span> <span class="o">:=</span> <span class="n">true</span>
<span class="kn">instance</span> <span class="n">func_of_decidable_is_decidable</span> <span class="o">(</span><span class="n">p</span> <span class="o">:</span> <span class="kt">Prop</span><span class="o">)</span> <span class="o">:</span>
<span class="n">decidable</span> <span class="o">(</span><span class="n">func</span> <span class="n">p</span><span class="o">)</span> <span class="o">:=</span>
<span class="k">begin</span>
  <span class="n">simp</span> <span class="o">[</span><span class="n">func</span><span class="o">],</span>
  <span class="c1">-- I have to prove decidable true</span>
  <span class="n">admit</span>
<span class="kn">end</span>

<span class="kn">example</span> <span class="o">(</span><span class="n">p</span><span class="o">:</span><span class="kt">Prop</span><span class="o">)</span> <span class="o">:</span> <span class="k">if</span> <span class="o">(</span><span class="n">func</span> <span class="n">p</span><span class="o">)</span> <span class="k">then</span> <span class="n">true</span> <span class="k">else</span> <span class="n">false</span> <span class="o">:=</span> <span class="n">sorry</span>
</pre></div>

#### [ Kevin Buzzard (Apr 09 2018 at 02:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124816222):
<div class="codehilite"><pre><span></span><span class="n">def</span> <span class="n">func</span><span class="o">(</span><span class="n">p</span><span class="o">:</span><span class="kt">Prop</span><span class="o">)</span> <span class="o">:</span> <span class="kt">Prop</span> <span class="o">:=</span> <span class="n">true</span>
<span class="kn">instance</span> <span class="n">func_of_decidable_is_decidable</span> <span class="o">(</span><span class="n">p</span> <span class="o">:</span> <span class="kt">Prop</span><span class="o">)</span> <span class="o">:</span>
<span class="n">decidable</span> <span class="o">(</span><span class="n">func</span> <span class="n">p</span><span class="o">)</span> <span class="o">:=</span> <span class="n">is_true</span> <span class="n">trivial</span>
</pre></div>

#### [ Kevin Buzzard (Apr 09 2018 at 02:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124816227):
<p>I just use the constructor</p>

#### [ Kevin Buzzard (Apr 09 2018 at 02:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124816265):
<p>in tactic mode you can write <code>exact is_true trivial</code></p>

#### [ Nima (Apr 09 2018 at 02:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124816270):
<p>Thanks, now I got it!</p>

#### [ Kevin Buzzard (Apr 09 2018 at 02:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124816272):
<p>The only way you can ever prove decidable anything is to use a constructor. decidable is an inductive type with two constructors and the only way to make an instance of it is to use one of the constructors.</p>

#### [ Mario Carneiro (Apr 09 2018 at 02:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124816379):
<p><code>decidable.true</code> proves <code>decidable true</code></p>

#### [ Mario Carneiro (Apr 09 2018 at 03:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124816479):
<div class="codehilite"><pre><span></span>instance (i) : decidable (is_nonempty i) :=
by cases i; unfold is_nonempty; apply_instance
</pre></div>

#### [ Mario Carneiro (Apr 09 2018 at 03:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124816490):
<p><code>valof</code> can also be defined without the <code>emt</code> case at all:</p>
<div class="codehilite"><pre><span></span>def valof : Π (i : ind), is_nonempty i → ℕ
| (val n) h := n
</pre></div>


<p>This is because lean does cases on <code>h</code> there and needs no cases since it's <code>false</code></p>

#### [ Mario Carneiro (Apr 09 2018 at 03:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124816533):
<p>I don't recommend using <code>bool</code> in this case if you can help it; it's possible but the coercions will get in your way sooner or later</p>

#### [ Nima (Apr 09 2018 at 03:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124816581):
<p>what is the difference between <code>unfold</code> and <code>rw</code>?</p>

#### [ Mario Carneiro (Apr 09 2018 at 03:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124816582):
<p>Also, you can prove <code>decidable T</code> for any expression <code>T</code> that is already known to be decidable from earlier stuff (like ands of ors of true and natural number equality and other things like that) by <code>apply_instance</code>.</p>

#### [ Mario Carneiro (Apr 09 2018 at 03:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124816591):
<p><code>unfold</code> does definitional unfolding; the syntax is <code>unfold X</code> where <code>X</code> is a definition will rewrite with the equation lemmas for <code>X</code>. <code>rw</code> does arbitrary (non-definitional) rewriting with any equations you give it</p>

#### [ Mario Carneiro (Apr 09 2018 at 03:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124816634):
<p>However, <code>rw X</code> also works as a shorthand for "rewrite with the equation lemmas for <code>X</code>" which makes it very similar to <code>unfold</code> in this instance</p>

#### [ Nima (Apr 09 2018 at 03:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124817111):
<p>Thank you,<br>
After all these helps and more than an hour I wrote <strong>6 lines</strong> as a proof  <span class="emoji emoji-1f631" title="scream">:scream:</span></p>

#### [ Mario Carneiro (Apr 09 2018 at 03:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124817178):
<p>"perfection is when there is nothing left to take away" - Antoine de Saint-Exupery</p>

#### [ Nima (Apr 09 2018 at 03:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124817309):
<p>Just to be clear, that was just survival; no perfection was involved!</p>

#### [ Simon Hudon (Apr 09 2018 at 03:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124817314):
<p>I also like to quote Adventure Time when it comes to learning functional programming and proving: sucking is the first step towards being kind of good at something.</p>

#### [ Simon Hudon (Apr 09 2018 at 03:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124817408):
<p>The fun thing about Haskell and Lean is that ugly code is still very much usable. As you learn more, you see it improve over time. My ugly Haskell and Lean code is still easier to refactor and evolve than anything I wrote in any language. Just to say: starting with bad code is not too much of a problem</p>

#### [ Nima (Apr 09 2018 at 04:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124819331):
<p>When I use <code>cases </code> on an inductive type, how can I specify the first case that I would like to consider?<br>
When I am in tactic mode, how can I have pattern matching on two inductive types at the same time?</p>

#### [ Kenny Lau (Apr 09 2018 at 05:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124819379):
<p>nested cases?</p>

#### [ Kenny Lau (Apr 09 2018 at 05:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124819382):
<blockquote>
<p>When I use <code>cases </code> on an inductive type, how can I specify the first case that I would like to consider?</p>
</blockquote>
<p>in tactic mode you can write</p>
<div class="codehilite"><pre><span></span>case list.nil
{ simp },
case list.cons
{ simp }
</pre></div>

#### [ Nima (Apr 09 2018 at 05:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124819491):
<p>Thanks for <code>case</code><br>
By "nested cases" you mean writing multiple <code>cases</code>?<br>
I meant something like <code>match a,b with</code>? Is there anything like that available?</p>

#### [ Kenny Lau (Apr 09 2018 at 05:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124819500):
<p><code>exact match a,b with</code></p>

#### [ Kenny Lau (Apr 09 2018 at 05:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124819501):
<p>you can always use <code>exact</code> to go into term mode</p>

#### [ Kenny Lau (Apr 09 2018 at 05:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124819502):
<p>and <code>by</code> to go into tactic mode</p>

#### [ Kenny Lau (Apr 09 2018 at 05:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124819503):
<p>no, I don't think there's a tactic for nested cases</p>

#### [ Nima (Apr 09 2018 at 05:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124819545):
<p><code>exact match a,b with</code> is exactly what I was looking for. Thank you.</p>

#### [ Mario Carneiro (Apr 09 2018 at 06:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124820994):
<p><code>rcases</code>, from the mathlib tactics, does multiple cases</p>

#### [ Mario Carneiro (Apr 09 2018 at 06:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124821038):
<p>but it only works with one input expression. In fact regular cases will automatically generalize dependent hypotheses like <code>match i, h with</code> in your earlier example.</p>

#### [ Nima (Apr 10 2018 at 03:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124863817):
<p>Does it make any sense if I use <code>classical</code> to prove something like <code> decidable (number.choose α = none) </code>?</p>

#### [ Mario Carneiro (Apr 10 2018 at 03:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124864641):
<p>You can, but <code>option.is_none</code> is already decidable</p>

#### [ Simon Hudon (Apr 10 2018 at 04:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124865269):
<p>There's also something contradictory to using classical reasoning to prove decidability: decidability is preferable to <code>classical.em</code> (excluded middle) especially to preserve computability. If you bring in classical reasoning, you lose computability so you might as well go all the way and just use <code>classical.prop_decidable</code> to make every proposition decidable:</p>
<div class="codehilite"><pre><span></span><span class="n">local</span> <span class="n">attribute</span> <span class="o">[</span><span class="kn">instance</span><span class="o">]</span> <span class="n">classical</span><span class="bp">.</span><span class="n">prop_decidable</span>
</pre></div>


<p>This is useful to use <code>if _ then _ else _</code> without proving decidability.</p>

#### [ Nima (Apr 10 2018 at 04:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124865624):
<p>So if I want to use <code>decidable</code> as what it is intended to be then I should not use <code>classical</code>. Right?</p>

#### [ Kenny Lau (Apr 10 2018 at 04:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124865732):
<p>but <code>classical.prop_decidable</code> just says that every <code>prop</code> is <code>decidable</code></p>

#### [ Mario Carneiro (Apr 10 2018 at 04:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124865767):
<p><code>decidable</code> is a proof obligation that is trivial if you are being classical. Most conventional math in lean is classical, so you usually don't have to worry about this. You should think about decidability if you are writing an executable program (if you have to mark your program <code>noncomputable</code> it won't run).</p>

#### [ Mario Carneiro (Apr 10 2018 at 04:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124865820):
<p>You can attempt to avoid LEM even when proving theorems, like Kenny, but the library won't really help you in this quest so it's an uphill battle</p>

#### [ Nima (Apr 10 2018 at 04:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124865830):
<p>Please look at the last two lines, as I am not sure if anything else there is relevant</p>
<div class="codehilite"><pre><span></span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u_1</span><span class="o">,</span>
<span class="bp">_</span><span class="n">inst_1</span> <span class="o">:</span> <span class="n">number</span> <span class="n">α</span><span class="o">,</span>
<span class="n">c</span> <span class="o">:</span> <span class="n">constraint</span> <span class="n">α</span><span class="o">,</span>
<span class="n">d₁</span> <span class="o">:</span> <span class="n">decidable</span> <span class="o">(</span><span class="n">is_trivial</span> <span class="n">c</span><span class="o">),</span>
<span class="n">d₂</span> <span class="o">:</span> <span class="n">decidable_linear_order</span> <span class="n">α</span><span class="o">,</span>
<span class="bp">_</span><span class="n">match</span> <span class="o">:</span> <span class="bp">Π</span> <span class="o">(</span><span class="bp">_</span><span class="n">a</span> <span class="o">:</span> <span class="n">decidable</span> <span class="o">(</span><span class="n">is_trivial</span> <span class="n">c</span><span class="o">)),</span> <span class="n">decidable</span> <span class="o">(</span><span class="n">is_satisfiable</span> <span class="n">c</span><span class="o">),</span>
<span class="n">hnt</span> <span class="o">:</span> <span class="bp">¬</span><span class="n">is_trivial</span> <span class="n">c</span><span class="o">,</span>
<span class="n">d₃</span> <span class="o">:</span> <span class="n">decidable</span> <span class="o">(</span><span class="n">is_lower_bound</span> <span class="n">c</span><span class="o">),</span>
<span class="bp">_</span><span class="n">match</span> <span class="o">:</span>
  <span class="n">decidable</span> <span class="o">(</span><span class="n">is_lower_bound</span> <span class="n">c</span><span class="o">)</span> <span class="bp">→</span>
  <span class="n">decidable</span>
    <span class="o">(</span><span class="n">ite</span> <span class="o">(</span><span class="n">is_lower_bound</span> <span class="n">c</span><span class="o">)</span> <span class="o">(</span><span class="n">is_satisfiable</span><span class="bp">._</span><span class="n">match_3</span> <span class="n">c</span> <span class="n">hnt</span> <span class="o">(</span><span class="n">number</span><span class="bp">.</span><span class="n">max</span> <span class="n">α</span><span class="o">))</span>
       <span class="o">(</span><span class="n">is_satisfiable</span><span class="bp">._</span><span class="n">match_4</span> <span class="n">c</span> <span class="n">hnt</span> <span class="o">(</span><span class="n">number</span><span class="bp">.</span><span class="n">min</span> <span class="n">α</span><span class="o">))),</span>
<span class="n">hl</span> <span class="o">:</span> <span class="n">is_lower_bound</span> <span class="n">c</span><span class="o">,</span>
<span class="bp">_</span><span class="n">match</span> <span class="o">:</span> <span class="bp">Π</span> <span class="o">(</span><span class="bp">_</span><span class="n">a</span> <span class="o">:</span> <span class="n">option</span> <span class="n">α</span><span class="o">),</span> <span class="n">decidable</span> <span class="o">(</span><span class="n">is_satisfiable</span><span class="bp">._</span><span class="n">match_3</span> <span class="n">c</span> <span class="n">hnt</span> <span class="bp">_</span><span class="n">a</span><span class="o">),</span>
<span class="n">m</span> <span class="o">:</span> <span class="n">α</span><span class="o">,</span>
<span class="n">aa</span> <span class="o">:</span> <span class="n">decidable</span> <span class="o">(</span><span class="n">get_bound</span> <span class="n">c</span> <span class="n">hnt</span> <span class="bp">&lt;</span> <span class="n">m</span><span class="o">)</span>
<span class="err">⊢</span> <span class="n">decidable</span> <span class="o">(</span><span class="n">get_bound</span> <span class="n">c</span> <span class="n">hnt</span> <span class="bp">&lt;</span> <span class="n">m</span><span class="o">)</span>
</pre></div>


<p>If I do <code> exact aa,</code> I receive this cryptic error message.</p>
<div class="codehilite"><pre><span></span><span class="n">invalid</span> <span class="n">type</span> <span class="n">ascription</span><span class="o">,</span> <span class="n">term</span> <span class="n">has</span> <span class="n">type</span>
  <span class="n">decidable</span>
    <span class="o">(</span><span class="bp">@</span><span class="n">has_lt</span><span class="bp">.</span><span class="n">lt</span> <span class="n">α</span>
       <span class="o">(</span><span class="bp">@</span><span class="n">preorder</span><span class="bp">.</span><span class="n">to_has_lt</span> <span class="n">α</span>
          <span class="o">(</span><span class="bp">@</span><span class="n">partial_order</span><span class="bp">.</span><span class="n">to_preorder</span> <span class="n">α</span>
             <span class="o">(</span><span class="bp">@</span><span class="n">linear_order</span><span class="bp">.</span><span class="n">to_partial_order</span> <span class="n">α</span>
                <span class="o">(</span><span class="bp">@</span><span class="n">linear_order</span><span class="bp">.</span><span class="n">mk</span> <span class="n">α</span> <span class="o">(</span><span class="bp">@</span><span class="n">decidable_linear_order</span><span class="bp">.</span><span class="n">le</span> <span class="n">α</span> <span class="n">d₂</span><span class="o">)</span> <span class="o">(</span><span class="bp">@</span><span class="n">decidable_linear_order</span><span class="bp">.</span><span class="n">lt</span> <span class="n">α</span> <span class="n">d₂</span><span class="o">)</span> <span class="bp">_</span> <span class="bp">_</span> <span class="bp">_</span> <span class="bp">_</span>
                   <span class="bp">_</span><span class="o">))))</span>
       <span class="o">(</span><span class="bp">@</span><span class="n">constraint</span><span class="bp">.</span><span class="n">get_bound</span> <span class="n">α</span> <span class="bp">_</span><span class="n">inst_1</span> <span class="n">c</span> <span class="n">hnt</span><span class="o">)</span>
       <span class="n">m</span><span class="o">)</span>
<span class="n">but</span> <span class="n">is</span> <span class="n">expected</span> <span class="n">to</span> <span class="k">have</span> <span class="n">type</span>
  <span class="n">decidable</span>
    <span class="o">(</span><span class="bp">@</span><span class="n">has_lt</span><span class="bp">.</span><span class="n">lt</span> <span class="n">α</span>
       <span class="o">(</span><span class="bp">@</span><span class="n">preorder</span><span class="bp">.</span><span class="n">to_has_lt</span> <span class="n">α</span>
          <span class="o">(</span><span class="bp">@</span><span class="n">partial_order</span><span class="bp">.</span><span class="n">to_preorder</span> <span class="n">α</span>
             <span class="o">(</span><span class="bp">@</span><span class="n">linear_order</span><span class="bp">.</span><span class="n">to_partial_order</span> <span class="n">α</span> <span class="o">(</span><span class="bp">@</span><span class="n">number</span><span class="bp">.</span><span class="n">number</span><span class="bp">.</span><span class="n">to_linear_order</span> <span class="n">α</span> <span class="bp">_</span><span class="n">inst_1</span><span class="o">))))</span>
       <span class="o">(</span><span class="bp">@</span><span class="n">constraint</span><span class="bp">.</span><span class="n">get_bound</span> <span class="n">α</span> <span class="bp">_</span><span class="n">inst_1</span> <span class="n">c</span> <span class="n">hnt</span><span class="o">)</span>
       <span class="n">m</span><span class="o">)</span>
<span class="n">state</span><span class="o">:</span>
<span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u_1</span><span class="o">,</span>
<span class="bp">...</span>
</pre></div>


<p>I know I might not gave enough information to receive an exact answer, but is there any clue you can share about why this might happen?</p>

#### [ Mario Carneiro (Apr 10 2018 at 04:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124865882):
<p>You have <code>decidable (is_trivial c)</code> as an assumption, which is probably a bad sign. How is <code>is_trivial</code> and <code>constraint</code> defined?</p>

#### [ Kenny Lau (Apr 10 2018 at 04:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124865889):
<p>diamond of death?</p>

#### [ Simon Hudon (Apr 10 2018 at 04:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124865935):
<p>I think <code> decidable_linear_order α</code> is more problematic because it is already subsumed by <code>number α</code></p>

#### [ Mario Carneiro (Apr 10 2018 at 04:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124865937):
<p>yes, <code> number α</code> and <code> decidable_linear_order α</code> both supply a less-equal relation</p>

#### [ Mario Carneiro (Apr 10 2018 at 04:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124865947):
<p>you should replace <code>decidable_linear_order α</code> with <code>@decidable_rel α (&lt;)</code></p>

#### [ Nima (Apr 10 2018 at 04:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124865948):
<div class="codehilite"><pre><span></span><span class="n">def</span> <span class="n">is_trivial</span> <span class="o">:</span> <span class="n">constraint</span> <span class="n">α</span> <span class="bp">→</span> <span class="kt">Prop</span>
<span class="bp">|</span> <span class="o">(</span><span class="n">cnstr</span>  <span class="n">ktrv</span>        <span class="bp">_</span> <span class="bp">_</span> <span class="bp">_</span> <span class="bp">_</span><span class="o">)</span> <span class="o">:=</span> <span class="n">true</span>
<span class="bp">|</span> <span class="o">(</span><span class="n">cnstr</span> <span class="o">(</span><span class="n">kdyn</span> <span class="n">trv</span> <span class="bp">_</span><span class="o">)</span> <span class="bp">_</span> <span class="bp">_</span> <span class="bp">_</span> <span class="bp">_</span><span class="o">)</span> <span class="o">:=</span> <span class="n">true</span>
<span class="bp">|</span> <span class="bp">_</span>                            <span class="o">:=</span> <span class="n">false</span>
</pre></div>

#### [ Mario Carneiro (Apr 10 2018 at 04:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124865950):
<p>or define <code>decidable_number</code></p>

#### [ Mario Carneiro (Apr 10 2018 at 04:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124865991):
<p>You should be able to prove <code>decidable (is_trivial c)</code> for all <code>c</code> as an instance, so it shouldn't need to be an assumption</p>

#### [ Nima (Apr 10 2018 at 04:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124865997):
<p>I make <strong>no claim</strong> of writing in the best or even a good way. Just trying to find my way through.</p>
<div class="codehilite"><pre><span></span><span class="kn">inductive</span> <span class="n">triviality</span>
<span class="bp">|</span> <span class="n">trv</span>
<span class="bp">|</span> <span class="n">ntr</span>

<span class="kn">inductive</span> <span class="n">direction</span>
<span class="bp">|</span> <span class="n">lower</span>
<span class="bp">|</span> <span class="n">upper</span>

<span class="kn">inductive</span> <span class="n">strictness</span>
<span class="bp">|</span> <span class="n">stt</span>
<span class="bp">|</span> <span class="n">nst</span>

<span class="kn">inductive</span> <span class="n">triviality_kind</span> <span class="o">{</span><span class="n">α</span><span class="o">:</span><span class="kt">Type</span><span class="bp">*</span><span class="o">}</span>
<span class="bp">|</span> <span class="n">ktrv</span>                             <span class="o">:</span> <span class="n">triviality_kind</span>
<span class="bp">|</span> <span class="n">kntr</span>                   <span class="o">(</span><span class="n">bnd</span> <span class="o">:</span> <span class="n">α</span><span class="o">)</span> <span class="o">:</span> <span class="n">triviality_kind</span>
<span class="bp">|</span> <span class="n">kdyn</span> <span class="o">(</span><span class="n">tr</span> <span class="o">:</span> <span class="n">triviality</span><span class="o">)</span> <span class="o">(</span><span class="n">bnd</span> <span class="o">:</span> <span class="n">α</span><span class="o">)</span> <span class="o">:</span> <span class="n">triviality_kind</span>

<span class="kn">inductive</span> <span class="n">direction_kind</span>
<span class="bp">|</span> <span class="n">none</span>
<span class="bp">|</span> <span class="n">klower</span>
<span class="bp">|</span> <span class="n">kupper</span>
<span class="bp">|</span> <span class="n">kdynam</span> <span class="o">(</span><span class="n">dir</span> <span class="o">:</span> <span class="n">direction</span><span class="o">)</span>

<span class="kn">inductive</span> <span class="n">strictness_kind</span>
<span class="bp">|</span> <span class="n">none</span>
<span class="bp">|</span> <span class="n">kstt</span>
<span class="bp">|</span> <span class="n">knst</span>
<span class="bp">|</span> <span class="n">kdyn</span> <span class="o">(</span><span class="n">st</span> <span class="o">:</span> <span class="n">strictness</span><span class="o">)</span>

<span class="kn">structure</span> <span class="n">constraint</span> <span class="o">(</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span><span class="bp">*</span><span class="o">)</span> <span class="o">:=</span>
<span class="n">cnstr</span> <span class="bp">::</span>
  <span class="o">(</span><span class="n">trvk</span> <span class="o">:</span> <span class="bp">@</span><span class="n">triviality_kind</span> <span class="n">α</span><span class="o">)</span>
  <span class="o">(</span><span class="n">dirk</span> <span class="o">:</span> <span class="n">direction_kind</span> <span class="o">)</span>
  <span class="o">(</span><span class="n">strk</span> <span class="o">:</span> <span class="n">strictness_kind</span><span class="o">)</span>
  <span class="o">(</span><span class="n">ndir</span> <span class="o">:</span> <span class="n">dirk</span> <span class="bp">=</span> <span class="n">direction_kind</span><span class="bp">.</span><span class="n">none</span>  <span class="bp">↔</span> <span class="n">trvk</span> <span class="bp">=</span> <span class="n">triviality_kind</span><span class="bp">.</span><span class="n">ktrv</span><span class="o">)</span>
  <span class="o">(</span><span class="n">nstr</span> <span class="o">:</span> <span class="n">strk</span> <span class="bp">=</span> <span class="n">strictness_kind</span><span class="bp">.</span><span class="n">none</span> <span class="bp">↔</span> <span class="n">trvk</span> <span class="bp">=</span> <span class="n">triviality_kind</span><span class="bp">.</span><span class="n">ktrv</span><span class="o">)</span>
</pre></div>


<div class="codehilite"><pre><span></span><span class="kn">instance</span>  <span class="n">is_trivial_is_decidable</span> <span class="o">(</span><span class="n">c</span> <span class="o">:</span> <span class="n">constraint</span> <span class="n">α</span><span class="o">)</span> <span class="o">:</span>
<span class="n">decidable</span> <span class="o">(</span><span class="n">is_trivial</span> <span class="n">c</span><span class="o">)</span> <span class="o">:=</span>
<span class="k">begin</span>
  <span class="n">cases</span> <span class="n">c</span><span class="bp">;</span> <span class="n">cases</span> <span class="n">trvk</span><span class="bp">;</span>
  <span class="n">try</span> <span class="o">{</span> <span class="n">unfold</span> <span class="n">is_trivial</span> <span class="o">}</span><span class="bp">;</span>
  <span class="n">try</span> <span class="o">{</span> <span class="n">cases</span> <span class="n">tr</span> <span class="o">}</span><span class="bp">;</span>
  <span class="n">try</span> <span class="o">{</span> <span class="n">exact</span> <span class="n">decidable</span><span class="bp">.</span><span class="n">true</span> <span class="o">}</span><span class="bp">;</span>
  <span class="n">try</span> <span class="o">{</span> <span class="n">exact</span> <span class="n">decidable</span><span class="bp">.</span><span class="n">false</span><span class="o">},</span>
<span class="kn">end</span>
</pre></div>

#### [ Mario Carneiro (Apr 10 2018 at 04:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124866049):
<p>You seem to already have the proof I mention there</p>

#### [ Mario Carneiro (Apr 10 2018 at 04:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124866094):
<p>What produced the <code>d₁ : decidable (is_trivial c)</code> in the theorem you are proving?</p>

#### [ Nima (Apr 10 2018 at 04:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124866108):
<p>I am trying to prove  the following is decidable</p>
<div class="codehilite"><pre><span></span><span class="n">def</span> <span class="n">is_satisfiable</span> <span class="o">(</span><span class="n">c</span> <span class="o">:</span> <span class="n">constraint</span> <span class="n">α</span><span class="o">)</span> <span class="o">[</span><span class="n">d</span> <span class="o">:</span> <span class="n">decidable</span> <span class="o">(</span><span class="n">is_trivial</span> <span class="n">c</span><span class="o">)]</span> <span class="o">:</span> <span class="kt">Prop</span> <span class="o">:=</span>
  <span class="k">match</span> <span class="n">d</span> <span class="k">with</span>
  <span class="bp">|</span> <span class="n">is_true</span>  <span class="bp">_</span>  <span class="o">:=</span> <span class="n">number</span><span class="bp">.</span><span class="n">choose</span> <span class="n">α</span> <span class="bp">≠</span> <span class="n">none</span>
  <span class="bp">|</span> <span class="n">is_false</span> <span class="n">ht</span> <span class="o">:=</span>
    <span class="k">match</span> <span class="n">get_strictness</span> <span class="n">c</span> <span class="n">ht</span> <span class="k">with</span>
    <span class="bp">|</span> <span class="n">nst</span> <span class="o">:=</span>  <span class="n">true</span>
    <span class="bp">|</span> <span class="n">stt</span> <span class="o">:=</span>  <span class="k">if</span> <span class="n">is_lower_bound</span> <span class="n">c</span> <span class="k">then</span>
                <span class="k">match</span> <span class="n">number</span><span class="bp">.</span><span class="n">max</span> <span class="n">α</span> <span class="k">with</span>
                <span class="bp">|</span> <span class="n">none</span>   <span class="o">:=</span> <span class="n">true</span>
                <span class="bp">|</span> <span class="n">some</span> <span class="n">m</span> <span class="o">:=</span> <span class="n">get_bound</span> <span class="n">c</span> <span class="n">ht</span> <span class="bp">&lt;</span> <span class="n">m</span>
                <span class="kn">end</span>
              <span class="k">else</span>
                <span class="k">match</span> <span class="n">number</span><span class="bp">.</span><span class="n">min</span> <span class="n">α</span> <span class="k">with</span>
                <span class="bp">|</span> <span class="n">none</span>   <span class="o">:=</span> <span class="n">true</span>
                <span class="bp">|</span> <span class="n">some</span> <span class="n">m</span> <span class="o">:=</span> <span class="n">m</span> <span class="bp">&lt;</span> <span class="n">get_bound</span> <span class="n">c</span> <span class="n">ht</span>
                <span class="kn">end</span>
    <span class="kn">end</span>
  <span class="kn">end</span>
</pre></div>


<p>Second line:</p>
<div class="codehilite"><pre><span></span><span class="kn">instance</span>  <span class="n">is_satisfiable_is_decidable</span> <span class="o">(</span><span class="n">c</span> <span class="o">:</span> <span class="n">constraint</span> <span class="n">α</span><span class="o">)</span>
          <span class="o">[</span><span class="n">d₁</span> <span class="o">:</span> <span class="n">decidable</span> <span class="o">(</span><span class="n">is_trivial</span> <span class="n">c</span><span class="o">)]</span>
          <span class="o">[</span><span class="n">d₂</span> <span class="o">:</span> <span class="n">decidable_linear_order</span> <span class="n">α</span><span class="o">]</span> <span class="o">:</span>
<span class="n">decidable</span> <span class="o">(</span><span class="n">is_satisfiable</span> <span class="n">c</span><span class="o">)</span> <span class="o">:=</span>
<span class="k">match</span> <span class="n">d₁</span> <span class="k">with</span>
<span class="bp">|</span> <span class="n">is_true</span>  <span class="n">ht</span>  <span class="o">:=</span> <span class="k">by</span> <span class="n">unfold</span> <span class="n">is_satisfiable</span><span class="bp">;</span> <span class="n">simp</span><span class="bp">;</span> <span class="n">apply_instance</span>
<span class="bp">|</span> <span class="n">is_false</span> <span class="n">hnt</span> <span class="o">:=</span>
  <span class="k">begin</span>
    <span class="n">unfold</span> <span class="n">is_satisfiable</span><span class="o">,</span>
    <span class="n">cases</span> <span class="n">get_strictness</span> <span class="n">c</span> <span class="n">hnt</span><span class="bp">;</span> <span class="n">unfold</span> <span class="n">is_satisfiable</span><span class="bp">._</span><span class="n">match_2</span><span class="o">,</span>
    <span class="k">begin</span>
      <span class="k">have</span> <span class="n">d₃</span> <span class="o">:</span> <span class="n">decidable</span> <span class="o">(</span><span class="n">is_lower_bound</span> <span class="n">c</span><span class="o">),</span> <span class="k">by</span> <span class="n">apply_instance</span><span class="o">,</span>
      <span class="n">exact</span> <span class="k">match</span> <span class="n">d₃</span> <span class="k">with</span>
      <span class="bp">|</span> <span class="n">is_true</span>  <span class="n">hl</span>  <span class="o">:=</span>
        <span class="k">begin</span>
          <span class="n">simp</span> <span class="o">[</span><span class="n">hl</span><span class="o">],</span>
          <span class="n">exact</span> <span class="k">match</span> <span class="n">number</span><span class="bp">.</span><span class="n">max</span> <span class="n">α</span> <span class="k">with</span>
          <span class="bp">|</span> <span class="n">none</span>   <span class="o">:=</span> <span class="k">by</span> <span class="n">unfold</span> <span class="n">is_satisfiable</span><span class="bp">._</span><span class="n">match_3</span><span class="bp">;</span> <span class="n">exact</span> <span class="n">decidable</span><span class="bp">.</span><span class="n">true</span>
          <span class="bp">|</span> <span class="n">some</span> <span class="n">m</span> <span class="o">:=</span> <span class="k">begin</span>
                      <span class="n">unfold</span> <span class="n">is_satisfiable</span><span class="bp">._</span><span class="n">match_3</span><span class="o">,</span>
                      <span class="k">have</span> <span class="n">aa</span> <span class="o">:=</span> <span class="n">decidable_linear_order</span><span class="bp">.</span><span class="n">decidable_lt</span> <span class="n">α</span> <span class="o">(</span><span class="n">get_bound</span> <span class="n">c</span> <span class="n">hnt</span><span class="o">)</span> <span class="n">m</span><span class="o">,</span>
                      <span class="n">exact</span> <span class="n">aa</span><span class="o">,</span>
                      <span class="kn">end</span>
          <span class="c1">-- by unfold is_satisfiable._match_3; apply_instance</span>
          <span class="kn">end</span>
        <span class="kn">end</span>
      <span class="bp">|</span> <span class="n">is_false</span> <span class="n">hnl</span> <span class="o">:=</span> <span class="k">begin</span> <span class="n">simp</span> <span class="o">[</span><span class="n">hnl</span><span class="o">],</span> <span class="n">admit</span> <span class="kn">end</span>
      <span class="kn">end</span><span class="o">,</span>
    <span class="kn">end</span><span class="o">,</span>
    <span class="n">exact</span> <span class="n">decidable</span><span class="bp">.</span><span class="n">true</span>
  <span class="kn">end</span>
<span class="kn">end</span>
</pre></div>

#### [ Mario Carneiro (Apr 10 2018 at 04:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124866109):
<p>drop the line <code>           [d₁ : decidable (is_trivial c)] </code></p>

#### [ Mario Carneiro (Apr 10 2018 at 04:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124866111):
<p>You can do the match by writing <code>if ht : is_trivial c then ... else ...</code></p>

#### [ Nima (Apr 10 2018 at 04:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124866223):
<p>Should I drop <code> [d : decidable (is_trivial c)] </code> from definition of <code>is_satisfiable</code> as well?</p>

#### [ Mario Carneiro (Apr 10 2018 at 04:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124866253):
<p>Given the complexity of your definition, I think you would do better to change <code>is_satisfiable</code> to type <code>def is_satisfiable (c : constraint α) : bool :=</code>. Same for <code>is_trivial</code>, since it's just a bunch of <code>true</code> and <code>false</code> branches</p>

#### [ Mario Carneiro (Apr 10 2018 at 04:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124866261):
<p>Then decidability will be trivial, and you can prove the unfolding of the individual branches as (much easier) lemmas</p>

#### [ Mario Carneiro (Apr 10 2018 at 04:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124866476):
<p>I don't have all your definitions so I don't know if this typechecks, but something like this:</p>
<div class="codehilite"><pre><span></span>def is_trivial : constraint α → bool
| (cnstr  ktrv        _ _ _ _) := tt
| (cnstr (kdyn trv _) _ _ _ _) := tt
| _                            := ff

def is_satisfiable (c : constraint α) : bool :=
if ht : is_trivial c then
  (number.choose α).is_some
else
  match get_strictness c ht with
  | nst := tt
  | stt :=
    if is_lower_bound c then
      match number.max α with
      | none   := tt
      | some m := get_bound c ht &lt; m
      end
    else
      match number.min α with
      | none   := tt
      | some m := m &lt; get_bound c ht
      end
  end
</pre></div>

#### [ Nima (Apr 10 2018 at 04:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124866687):
<p>Would you please tell me why I should have dropped <code>[d₁ : decidable (is_trivial c)]</code>?<br>
Shouldn't I have one of these for every property I put in <code>if then else</code>?</p>

#### [ Simon Hudon (Apr 10 2018 at 04:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124866740):
<p>When you look at <code>(get_bound c hnt &lt; m)</code> you should see that <code>&lt;</code> is generic, i.e. it is inferred from instances. Because of that you should see that it takes four parameters, not two:</p>
<ul>
<li><code>α </code></li>
<li>some instance of <code>has_lt α</code></li>
<li><code>get_bound c hnt</code></li>
<li><code>m</code></li>
</ul>
<p>This means that if different instances of <code>has_lt</code> are inferred for two <code>&lt;</code> propositions, they are not syntactically the same so you can't use one to prove the other</p>

#### [ Simon Hudon (Apr 10 2018 at 04:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124866786):
<p>That means that you have to consciously try to have a unique path to any instance that you're going to use. If the instances are conceptually the same, it might still be hard to prove and the effort is usually not worth it</p>

#### [ Mario Carneiro (Apr 10 2018 at 05:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124866904):
<p>When you say <code>[d₁ : decidable (is_trivial c)]</code> , you are defining a function parametric over proofs that triviality is decidable. There's no need to do this, you already have such a proof/function and want to call it whenever you want to decide if a constraint is trivial</p>

#### [ Mario Carneiro (Apr 10 2018 at 05:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124866963):
<p>If you say <code>if ht : is_trivial c then ...</code>, it automatically infers the <code>decidable (is_trivial c)</code> argument (using the environment, not just the local context), which is what you want.</p>

#### [ Nima (Apr 10 2018 at 05:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124867141):
<p>Thank you both,<br>
I need time to take these in ...</p>

#### [ Simon Hudon (Apr 10 2018 at 05:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124867357):
<p>Sure :) it's a slow process. You can have Lean's pretty printer show more information and, among others, show the implicit and type class arguments by using <code>set_option pp.all true</code> before your theorem.</p>

#### [ Nima (Apr 10 2018 at 06:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124869749):
<p>OK, after I changed something and I will get back to it later, I managed to rewrote the whole proof in the following nicer way.<br>
As you can see something is almost duplicated. Is there anyway I can make this even shorter (ie remove those duplications)?</p>
<div class="codehilite"><pre><span></span><span class="kn">instance</span>  <span class="n">is_satisfiable_is_decidable</span> <span class="o">(</span><span class="n">c</span> <span class="o">:</span> <span class="n">constraint</span> <span class="n">α</span><span class="o">)</span> <span class="o">:</span>
<span class="n">decidable</span> <span class="o">(</span><span class="n">is_satisfiable</span> <span class="n">c</span><span class="o">)</span> <span class="o">:=</span>
  <span class="k">if</span> <span class="n">ht</span> <span class="o">:</span> <span class="n">is_trivial</span>     <span class="n">c</span> <span class="k">then</span> <span class="k">by</span> <span class="o">{</span> <span class="n">unfold</span> <span class="n">is_satisfiable</span><span class="o">,</span> <span class="n">simp</span> <span class="o">[</span><span class="n">ht</span><span class="o">],</span> <span class="n">apply_instance</span> <span class="o">}</span> <span class="k">else</span>
  <span class="k">if</span> <span class="n">hs</span> <span class="o">:</span> <span class="n">is_nonstrict</span>   <span class="n">c</span> <span class="k">then</span> <span class="k">by</span> <span class="o">{</span> <span class="n">unfold</span> <span class="n">is_satisfiable</span><span class="o">,</span> <span class="n">simp</span> <span class="o">[</span><span class="n">hs</span><span class="o">],</span> <span class="n">apply_instance</span> <span class="o">}</span> <span class="k">else</span>
  <span class="k">if</span> <span class="n">hl</span> <span class="o">:</span> <span class="n">is_lower_bound</span> <span class="n">c</span> <span class="k">then</span> <span class="k">by</span>
    <span class="n">unfold</span> <span class="n">is_satisfiable</span><span class="bp">;</span>
    <span class="n">cases</span> <span class="n">number</span><span class="bp">.</span><span class="n">max</span> <span class="n">α</span> <span class="k">with</span> <span class="n">m</span><span class="bp">;</span>
    <span class="n">simp</span> <span class="o">[</span><span class="n">ht</span><span class="o">,</span><span class="n">hs</span><span class="o">,</span><span class="n">hl</span><span class="o">,</span><span class="n">is_satisfiable</span><span class="o">]</span><span class="bp">;</span>
    <span class="n">apply_instance</span>
  <span class="k">else</span> <span class="k">by</span>
    <span class="n">unfold</span> <span class="n">is_satisfiable</span><span class="bp">;</span>
    <span class="n">cases</span> <span class="n">number</span><span class="bp">.</span><span class="n">min</span> <span class="n">α</span> <span class="k">with</span> <span class="n">m</span><span class="bp">;</span>
    <span class="n">simp</span> <span class="o">[</span><span class="n">ht</span><span class="o">,</span><span class="n">hs</span><span class="o">,</span><span class="n">hl</span><span class="o">,</span><span class="n">is_satisfiable</span><span class="o">]</span><span class="bp">;</span>
    <span class="n">apply_instance</span>
</pre></div>

#### [ Simon Hudon (Apr 10 2018 at 06:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124869940):
<p>Can you reproduce the definitions of <code>is_satisfiable</code>, <code>constraint</code>, <code>is_trivial</code>, <code>is_nonstrict</code> and <code>is_lower_bound</code> please?</p>

#### [ Nima (Apr 10 2018 at 06:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124870028):
<p>I did not mean shorter proof using all these definitions. I thought just because those lines look a lot like each other, one should be able to merge them using something like <code>try</code>. But if I write <code>if ht : is_trivial c ∨ is_nonstrict c then</code> then I cannot even write <code>cases ht</code>, and I did not understand why.</p>
<div class="codehilite"><pre><span></span><span class="kn">structure</span> <span class="n">constraint</span> <span class="o">(</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span><span class="bp">*</span><span class="o">)</span> <span class="o">:=</span>
<span class="n">cnstr</span> <span class="bp">::</span>
  <span class="o">(</span><span class="n">trvk</span> <span class="o">:</span> <span class="bp">@</span><span class="n">triviality_kind</span> <span class="n">α</span><span class="o">)</span>
  <span class="o">(</span><span class="n">dirk</span> <span class="o">:</span> <span class="n">direction_kind</span> <span class="o">)</span>
  <span class="o">(</span><span class="n">strk</span> <span class="o">:</span> <span class="n">strictness_kind</span><span class="o">)</span>
  <span class="o">(</span><span class="n">ndir</span> <span class="o">:</span> <span class="n">dirk</span> <span class="bp">=</span> <span class="n">direction_kind</span><span class="bp">.</span><span class="n">none</span>  <span class="bp">↔</span> <span class="n">trvk</span> <span class="bp">=</span> <span class="n">triviality_kind</span><span class="bp">.</span><span class="n">ktrv</span><span class="o">)</span>
  <span class="o">(</span><span class="n">nstr</span> <span class="o">:</span> <span class="n">strk</span> <span class="bp">=</span> <span class="n">strictness_kind</span><span class="bp">.</span><span class="n">none</span> <span class="bp">↔</span> <span class="n">trvk</span> <span class="bp">=</span> <span class="n">triviality_kind</span><span class="bp">.</span><span class="n">ktrv</span><span class="o">)</span>

<span class="n">def</span> <span class="n">is_trivial</span> <span class="o">:</span> <span class="n">constraint</span> <span class="n">α</span> <span class="bp">→</span> <span class="kt">Prop</span>
<span class="bp">|</span> <span class="o">(</span><span class="n">cnstr</span>  <span class="n">ktrv</span>        <span class="bp">_</span> <span class="bp">_</span> <span class="bp">_</span> <span class="bp">_</span><span class="o">)</span> <span class="o">:=</span> <span class="n">true</span>
<span class="bp">|</span> <span class="o">(</span><span class="n">cnstr</span> <span class="o">(</span><span class="n">kdyn</span> <span class="n">trv</span> <span class="bp">_</span><span class="o">)</span> <span class="bp">_</span> <span class="bp">_</span> <span class="bp">_</span> <span class="bp">_</span><span class="o">)</span> <span class="o">:=</span> <span class="n">true</span>
<span class="bp">|</span> <span class="bp">_</span>                            <span class="o">:=</span> <span class="n">false</span>

<span class="n">def</span> <span class="n">is_lower_bound</span> <span class="o">:</span> <span class="n">constraint</span> <span class="n">α</span> <span class="bp">→</span> <span class="kt">Prop</span>
<span class="bp">|</span> <span class="o">(</span><span class="n">cnstr</span> <span class="bp">_</span>  <span class="n">klower</span>        <span class="bp">_</span> <span class="bp">_</span> <span class="bp">_</span><span class="o">)</span> <span class="o">:=</span> <span class="n">true</span>
<span class="bp">|</span> <span class="o">(</span><span class="n">cnstr</span> <span class="bp">_</span> <span class="o">(</span><span class="n">kdynam</span> <span class="n">lower</span><span class="o">)</span> <span class="bp">_</span> <span class="bp">_</span> <span class="bp">_</span><span class="o">)</span> <span class="o">:=</span> <span class="n">true</span>
<span class="bp">|</span> <span class="bp">_</span>                              <span class="o">:=</span> <span class="n">false</span>

<span class="n">def</span> <span class="n">is_nonstrict</span> <span class="o">:</span> <span class="n">constraint</span> <span class="n">α</span> <span class="bp">→</span> <span class="kt">Prop</span>
<span class="bp">|</span> <span class="o">(</span><span class="n">cnstr</span> <span class="bp">_</span> <span class="bp">_</span>  <span class="n">knst</span>      <span class="bp">_</span> <span class="bp">_</span><span class="o">)</span> <span class="o">:=</span> <span class="n">true</span>
<span class="bp">|</span> <span class="o">(</span><span class="n">cnstr</span> <span class="bp">_</span> <span class="bp">_</span> <span class="o">(</span><span class="n">kdyn</span> <span class="n">nst</span><span class="o">)</span> <span class="bp">_</span> <span class="bp">_</span><span class="o">)</span> <span class="o">:=</span> <span class="n">true</span>
<span class="bp">|</span> <span class="bp">_</span>                          <span class="o">:=</span> <span class="n">false</span>

<span class="n">def</span> <span class="n">is_satisfiable</span> <span class="o">(</span><span class="n">c</span> <span class="o">:</span> <span class="n">constraint</span> <span class="n">α</span><span class="o">)</span> <span class="o">:</span> <span class="kt">Prop</span> <span class="o">:=</span>
  <span class="k">if</span> <span class="n">ht</span> <span class="o">:</span> <span class="n">is_trivial</span>     <span class="n">c</span> <span class="k">then</span> <span class="n">number</span><span class="bp">.</span><span class="n">choose</span> <span class="n">α</span> <span class="bp">≠</span> <span class="n">none</span> <span class="k">else</span>
  <span class="k">if</span>      <span class="n">is_nonstrict</span>   <span class="n">c</span> <span class="k">then</span> <span class="n">true</span> <span class="k">else</span>
  <span class="k">if</span>      <span class="n">is_lower_bound</span> <span class="n">c</span> <span class="k">then</span>
    <span class="k">match</span> <span class="n">number</span><span class="bp">.</span><span class="n">max</span> <span class="n">α</span> <span class="k">with</span>
    <span class="bp">|</span> <span class="n">none</span>   <span class="o">:=</span> <span class="n">true</span>
    <span class="bp">|</span> <span class="n">some</span> <span class="n">m</span> <span class="o">:=</span> <span class="n">get_bound</span> <span class="n">c</span> <span class="n">ht</span> <span class="bp">&lt;</span> <span class="n">m</span>
    <span class="kn">end</span>
  <span class="k">else</span>
    <span class="k">match</span> <span class="n">number</span><span class="bp">.</span><span class="n">min</span> <span class="n">α</span> <span class="k">with</span>
    <span class="bp">|</span> <span class="n">none</span>   <span class="o">:=</span> <span class="n">true</span>
    <span class="bp">|</span> <span class="n">some</span> <span class="n">m</span> <span class="o">:=</span> <span class="n">m</span> <span class="bp">&lt;</span> <span class="n">get_bound</span> <span class="n">c</span> <span class="n">ht</span>
    <span class="kn">end</span>
</pre></div>

#### [ Simon Hudon (Apr 10 2018 at 06:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124870217):
<p>I'd like to replace your big <code>if _ then _ else _ </code> with a <code>match</code> but I can't think of a nice way to do it. Instead, let's try this:</p>
<div class="codehilite"><pre><span></span><span class="k">begin</span>
   <span class="n">refine</span> <span class="o">(</span> <span class="k">if</span> <span class="n">ht</span> <span class="o">:</span> <span class="n">is_trivial</span>     <span class="n">c</span> <span class="k">then</span> <span class="bp">_</span>
            <span class="k">else</span> <span class="k">if</span>      <span class="n">is_nonstrict</span>   <span class="n">c</span> <span class="k">then</span> <span class="bp">_</span>
            <span class="k">else</span> <span class="k">if</span>      <span class="n">is_lower_bound</span> <span class="n">c</span> <span class="k">then</span>
                <span class="k">match</span> <span class="n">number</span><span class="bp">.</span><span class="n">max</span> <span class="n">α</span> <span class="k">with</span>
                 <span class="bp">|</span> <span class="n">none</span>   <span class="o">:=</span> <span class="bp">_</span>
                 <span class="bp">|</span> <span class="n">some</span> <span class="n">m</span> <span class="o">:=</span> <span class="bp">_</span>
                <span class="kn">end</span>
            <span class="k">else</span>
                <span class="k">match</span> <span class="n">number</span><span class="bp">.</span><span class="n">min</span> <span class="n">α</span> <span class="k">with</span>
                 <span class="bp">|</span> <span class="n">none</span>   <span class="o">:=</span> <span class="bp">_</span>
                 <span class="bp">|</span> <span class="n">some</span> <span class="n">m</span> <span class="o">:=</span> <span class="bp">_</span>
                <span class="kn">end</span> <span class="o">)</span>
   <span class="bp">;</span> <span class="n">simp</span> <span class="o">[</span><span class="bp">*</span><span class="o">,</span> <span class="n">is_satisfiable</span><span class="o">]</span> <span class="bp">;</span> <span class="n">apply_instance</span>
<span class="kn">end</span>
</pre></div>

#### [ Simon Hudon (Apr 10 2018 at 06:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124870219):
<p>Not very concise but less repetitive</p>

#### [ Simon Hudon (Apr 10 2018 at 07:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124870361):
<p>As a side note: I suggest you pick more obvious names -- that is, names whose meaning is obvious rather than names that are easy to pick -- that names such as <code>knst</code>. I feel overly short names pose a puzzle to the reader.</p>

#### [ Nima (Apr 10 2018 at 07:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124870419):
<p>Thanks a lot, seems something I can use often.<br>
Regarding <code>refine</code>, I found this:</p>
<blockquote>
<p>The refine tactic applies the expression in question to the goal, but leaves any remaining metavariables for us to fill</p>
</blockquote>
<p>Is that what you are trying to do?<br>
How does <code>refine</code> knows inside <code>(..)</code> is supposed to be definition of <code>is_satisfiable</code> and so it can fill all the <code>_</code>?</p>

#### [ Nima (Apr 10 2018 at 07:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124870519):
<blockquote>
<p>As a side note: I suggest you pick more ...</p>
</blockquote>
<p>Sometimes I think I might be sick, since I prefer <code>stt</code> and <code>nst</code> over <code>strict</code> and <code>non_strict</code>, mainly because when you write them in two consecutive lines, they are nicely aligned! <span class="emoji emoji-1f643" title="upside down face">:upside_down_face:</span></p>

#### [ Simon Hudon (Apr 10 2018 at 07:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124870612):
<p>Yes that's what I'm trying to do. Think of refine as applying type inference to <code>(if ... then _ else ... :  decidable (is_satisfiable c))</code>. Before we start, we don't know the type of <code>_</code> but then, we use the type of <code>dite</code> (the <code>if _ then _ else _</code> function) and we can figure out that <code>_</code> has type <code>decidable (is_satisfiable c)</code>. When we're done with type inference / type checking, we still don't know a term (or proof) to assign to <code>_</code> so building such a term becomes the goal of a subproof.</p>

#### [ Simon Hudon (Apr 10 2018 at 07:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124870621):
<p>Symbols that line up do look nice! As a compromise, you may consider padding with spaces</p>

#### [ Nima (Apr 10 2018 at 07:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124870724):
<p>OK, I copy-pasted your suggestion and I am receiving the following error (highlighted below the first <code>;</code>), is this a version issue? (I am on 3.3.0)</p>
<div class="codehilite"><pre><span></span><span class="n">Tactic</span> <span class="n">State</span>
<span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u_1</span><span class="o">,</span>
<span class="bp">_</span><span class="n">inst_1</span> <span class="o">:</span> <span class="n">number</span> <span class="n">α</span><span class="o">,</span>
<span class="n">c</span> <span class="o">:</span> <span class="n">constraint</span> <span class="n">α</span>
<span class="err">⊢</span> <span class="n">decidable</span> <span class="o">(</span><span class="n">is_satisfiable</span> <span class="n">c</span><span class="o">)</span>


<span class="n">don&#39;t</span> <span class="n">know</span> <span class="n">how</span> <span class="n">to</span> <span class="n">synthesize</span> <span class="n">placeholder</span>
<span class="kn">context</span><span class="o">:</span>
<span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u_1</span><span class="o">,</span>
<span class="bp">_</span><span class="n">inst_1</span> <span class="o">:</span> <span class="n">number</span> <span class="n">α</span><span class="o">,</span>
<span class="n">c</span> <span class="o">:</span> <span class="n">constraint</span> <span class="n">α</span><span class="o">,</span>
<span class="n">ht</span> <span class="o">:</span> <span class="bp">¬</span><span class="n">is_trivial</span> <span class="n">c</span><span class="o">,</span>
<span class="bp">_</span><span class="n">match</span> <span class="o">:</span> <span class="n">option</span> <span class="n">α</span> <span class="bp">→</span> <span class="n">decidable</span> <span class="o">(</span><span class="n">is_satisfiable</span> <span class="n">c</span><span class="o">)</span>
<span class="err">⊢</span> <span class="n">decidable</span> <span class="o">(</span><span class="n">is_satisfiable</span> <span class="n">c</span><span class="o">)</span>
<span class="n">state</span><span class="o">:</span>
<span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u_1</span><span class="o">,</span>
<span class="bp">_</span><span class="n">inst_1</span> <span class="o">:</span> <span class="n">number</span> <span class="n">α</span><span class="o">,</span>
<span class="n">c</span> <span class="o">:</span> <span class="n">constraint</span> <span class="n">α</span>
<span class="err">⊢</span> <span class="n">decidable</span> <span class="o">(</span><span class="n">is_satisfiable</span> <span class="n">c</span><span class="o">)</span>
</pre></div>

#### [ Mario Carneiro (Apr 10 2018 at 07:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124870774):
<p>I don't think your approach will work, Simon. First of all, <code>match</code> and <code>let match</code> have a tendency to be insulated from pexpr metavariable generation, so that they end up being immediate (term) goals even if they appear in a <code>refine</code></p>

#### [ Mario Carneiro (Apr 10 2018 at 07:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124870822):
<p>Second, it is important for Nima's proof approach that the <code> number.max α </code> argument be exposed at the point of the <code>match</code>/<code>cases</code>, otherwise it won't be generalized. That means that the <code>unfold is_satisfiable</code> command has to come <em>before</em> the match attempt</p>

#### [ Simon Hudon (Apr 10 2018 at 07:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124870826):
<p><span class="user-mention" data-user-id="110049">@Mario Carneiro</span> I think you're right.</p>
<p><span class="user-mention" data-user-id="112062">@Nima</span> Would you mind using <a href="https://gist.github.com/" target="_blank" title="https://gist.github.com/">https://gist.github.com/</a> to share all the definitions needed to make the example work?</p>

#### [ Simon Hudon (Apr 10 2018 at 07:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124870878):
<p>I'll try to make a proof work on my side and get back to you</p>

#### [ Nima (Apr 10 2018 at 07:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124871580):
<p>Here is a link<br>
<strong><a href="https://github.com/nima-roohi/lets-learn-some-lean" target="_blank" title="https://github.com/nima-roohi/lets-learn-some-lean">lets-learn-some-lean</a></strong></p>

#### [ Mario Carneiro (Apr 10 2018 at 07:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124871630):
<p>In <code>number.lean</code>, you almost certainly want <code>:</code> instead of <code>:=</code> in the fields <code> neg₀</code> etc</p>

#### [ Nima (Apr 10 2018 at 07:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124871678):
<p>Sure,  thanks,</p>

#### [ Simon Hudon (Apr 10 2018 at 08:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124872748):
<p>Here's my next suggestion:</p>
<div class="codehilite"><pre><span></span><span class="kn">instance</span>  <span class="n">is_satisfiable_is_decidable</span> <span class="o">(</span><span class="n">c</span> <span class="o">:</span> <span class="n">constraint</span> <span class="n">α</span><span class="o">)</span> <span class="o">:</span>
<span class="n">decidable</span> <span class="o">(</span><span class="n">is_satisfiable</span> <span class="n">c</span><span class="o">)</span> <span class="o">:=</span>
<span class="k">begin</span>
  <span class="n">refine</span> <span class="o">(</span> <span class="k">if</span> <span class="n">ht</span> <span class="o">:</span> <span class="n">is_trivial</span>     <span class="n">c</span> <span class="k">then</span> <span class="bp">_</span>
            <span class="k">else</span> <span class="k">if</span> <span class="n">hs</span> <span class="o">:</span> <span class="n">is_nonstrict</span>   <span class="n">c</span> <span class="k">then</span> <span class="bp">_</span>
            <span class="k">else</span> <span class="k">if</span> <span class="n">hl</span> <span class="o">:</span> <span class="n">is_lower_bound</span> <span class="n">c</span> <span class="k">then</span>
                <span class="bp">_</span>
            <span class="k">else</span>
                <span class="bp">_</span> <span class="o">)</span>
   <span class="bp">;</span> <span class="n">simp</span> <span class="o">[</span><span class="bp">*</span><span class="o">,</span> <span class="n">is_satisfiable</span><span class="o">]</span>
   <span class="bp">;</span> <span class="n">try</span> <span class="o">{</span> <span class="n">generalize</span> <span class="o">:</span> <span class="n">number</span><span class="bp">.</span><span class="n">max</span> <span class="n">α</span> <span class="bp">=</span> <span class="n">x</span><span class="o">,</span> <span class="n">cases</span> <span class="n">x</span><span class="o">,</span> <span class="o">}</span>
   <span class="bp">;</span> <span class="n">try</span> <span class="o">{</span> <span class="n">generalize</span> <span class="o">:</span> <span class="n">number</span><span class="bp">.</span><span class="n">min</span> <span class="n">α</span> <span class="bp">=</span> <span class="n">x</span><span class="o">,</span> <span class="n">cases</span> <span class="n">x</span><span class="o">,</span> <span class="o">}</span>
   <span class="bp">;</span> <span class="n">try</span> <span class="o">{</span> <span class="n">simp</span> <span class="o">[</span><span class="bp">*</span><span class="o">,</span> <span class="n">is_satisfiable</span><span class="o">]</span> <span class="o">}</span>
   <span class="bp">;</span> <span class="n">apply_instance</span><span class="o">,</span>
<span class="kn">end</span>
</pre></div>

#### [ Simon Hudon (Apr 10 2018 at 08:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124872756):
<p>It could work without the <code>generalize</code>s but it would produce many more cases</p>

#### [ Mario Carneiro (Apr 10 2018 at 08:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124872798):
<p>why is that?</p>

#### [ Mario Carneiro (Apr 10 2018 at 08:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124872799):
<p>also isn't the first <code>simp</code> redundant?</p>

#### [ Simon Hudon (Apr 10 2018 at 08:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124872801):
<p>Yeah, I just noticed that</p>

#### [ Mario Carneiro (Apr 10 2018 at 08:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124872807):
<p>also the parens around the <code>refine</code> should be unnecessary</p>

#### [ Simon Hudon (Apr 10 2018 at 08:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124872808):
<p>I mean: which first <code>simp</code>?</p>

#### [ Simon Hudon (Apr 10 2018 at 08:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124872859):
<blockquote>
<p>also the parens around the <code>refine</code> should be unnecessary</p>
</blockquote>
<p>I think it might create a precedence problem with <code>;</code></p>

#### [ Simon Hudon (Apr 10 2018 at 08:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124872982):
<p>To answer your first question: it generates many more cases because we only need <code>cases number.max α</code> (resp. <code>cases number.min α</code>) in one branch out of four so, at the first <code>try</code>, without the <code>generalize</code>, we end up with <code>8</code> cases instead of <code>5</code> and, at the second try, we end up with <code>16</code> cases instead of <code>6</code>. We don't see all those cases but somehow knowing that they're there would give me nightmares</p>

#### [ Mario Carneiro (Apr 10 2018 at 08:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124873026):
<p>does <code>generalize</code> fail if the target expression is not present?</p>

#### [ Simon Hudon (Apr 10 2018 at 08:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124873080):
<p><code>generalize : number.max α = x</code> does but not <code>generalize h : number.max α = x</code></p>

#### [ Simon Hudon (Apr 10 2018 at 08:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124873185):
<p>I kind of like this use of <code>refine</code>. Maybe a tactic such as <code>if_then_else [is_trivial c,is_nonstrict c,is_lower_bound c]</code> would be nicer though.</p>

#### [ Mario Carneiro (Apr 10 2018 at 08:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124873190):
<p>A remark on theorems like this, where you have to go through all the cases in your original definition: You have to do this every time you want to prove anything about <code>is_satisfiable</code>, which is why I prefer to write a custom recursor that does the match splits for you. You can then use it to define <code>is_satisfiable</code> itself, as well as theorems proving properties about it</p>

#### [ Simon Hudon (Apr 10 2018 at 08:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124873193):
<p>That make sense. Do you also write a tactic to apply the recursor?</p>

#### [ Mario Carneiro (Apr 10 2018 at 08:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124873194):
<p><code>by_cases</code> is the tactic version of <code>if then else</code></p>

#### [ Simon Hudon (Apr 10 2018 at 08:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124873237):
<p>Can you give it multiple conditions?</p>

#### [ Mario Carneiro (Apr 10 2018 at 08:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124873238):
<p>Not usually, I will either write it explicitly as a term or use <code>apply is_satisfiable.rec</code></p>

#### [ Mario Carneiro (Apr 10 2018 at 08:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124873239):
<p>no</p>

#### [ Mario Carneiro (Apr 10 2018 at 08:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124873246):
<p>I'm not convinced you will always have this structure anyway; it seems like it's best just to nest the <code>by_cases</code> applications</p>

#### [ Mario Carneiro (Apr 10 2018 at 08:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124873287):
<p>you could also have <code>if h1 then if h2 then e1 else e2 else e3</code></p>

#### [ Nima (Apr 10 2018 at 08:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124873419):
<p>Thank you for the solution.<br>
By actually doing it, I can see <code>cases number.max α</code> creates a lot more cases than <code>generalize : number.max α = x, cases x</code>. But why (aren't they both cases on <code>none</code> and <code>some _</code>)?</p>

#### [ Simon Hudon (Apr 10 2018 at 09:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124873477):
<p>In <code>generalize : number.max α = x, cases x</code>, <code>generalize : number.max α = x</code> fails if <code>number.max α</code> is not used in the goal and therefore <code>cases x</code> doesn't get executed. It's a complicated way of saying <code>cases number.max α</code> but only if I actually use <code>number.max α</code></p>

#### [ Nima (Apr 10 2018 at 09:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124873546):
<p>I see,<br>
Also, is this <strong>recuroser</strong> a concept in lean or Haskell?</p>
<blockquote>
<p>... which is why I prefer to write a custom recursor that does the match splits for you. ...</p>
</blockquote>
<p>Theorem Proving in Lean, Section 7.1</p>
<blockquote>
<p>... It is also known as a recursor, and it is what makes the type “inductive” ...</p>
</blockquote>
<p>??</p>

#### [ Simon Hudon (Apr 10 2018 at 09:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124873547):
<p>By the time it is used, <code>number.max α</code> has disappeared from all but one goal</p>

#### [ Simon Hudon (Apr 10 2018 at 09:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124873636):
<p>The recursor is a Lean and dependent type theory concept</p>

#### [ Simon Hudon (Apr 10 2018 at 09:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124873689):
<p>In Lean, an inductive type definition is not a first class citizen. It is translated into a bunch of constants and definitions.</p>

#### [ Simon Hudon (Apr 10 2018 at 09:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124873691):
<p>Let's take a look at:</p>
<div class="codehilite"><pre><span></span><span class="kn">inductive</span> <span class="n">my_option</span> <span class="o">(</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span><span class="bp">*</span><span class="o">)</span>
 <span class="bp">|</span> <span class="n">none</span> <span class="o">:</span> <span class="n">my_option</span>
 <span class="bp">|</span> <span class="n">some</span> <span class="o">:</span> <span class="n">α</span> <span class="bp">→</span> <span class="n">my_option</span>
</pre></div>

#### [ Sean Leather (Apr 10 2018 at 09:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124873696):
<p>It's not limited to dependent types, of course. <span class="emoji emoji-1f642" title="simple smile">:simple_smile:</span></p>

#### [ Simon Hudon (Apr 10 2018 at 09:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124873741):
<p>Thanks for the precision!</p>

#### [ Sean Leather (Apr 10 2018 at 09:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124873747):
<p>Gotta keep you on your toes. <span class="emoji emoji-1f609" title="wink">:wink:</span></p>

#### [ Simon Hudon (Apr 10 2018 at 09:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124873752):
<p>If we type in </p>
<div class="codehilite"><pre><span></span><span class="bp">#</span><span class="kn">print</span> <span class="kn">prefix</span> <span class="n">my_option</span>
</pre></div>


<p>we see the constants and definitions that <code>my_option</code> is translated into</p>

#### [ Simon Hudon (Apr 10 2018 at 09:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124873906):
<p>Sean will correct me if I'm wrong but I think only three of them are constants: two constructors</p>
<div class="codehilite"><pre><span></span>my_option.none : Π (α : Type u_1), my_option α
my_option.some : Π {α : Type u_1}, α → my_option α
</pre></div>


<p>and one recursor</p>
<div class="codehilite"><pre><span></span>my_option.cases_on : Π {α : Type u_1} {C : my_option α → Sort l} (n : my_option α),
  C (my_option.none α) → (Π (a : α), C (my_option.some a)) → C n
</pre></div>


<p>(I just realized that <code>no_confusion</code> is actually a definition)</p>

#### [ Simon Hudon (Apr 10 2018 at 09:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124873964):
<p>The recursor basically tells you how to pattern match on <code>my_option</code>. When you pattern match on <code>opt : my_option α</code>, you're constructing a value of <code>C opt</code> (for some <code>C</code>) and you have to provide a way to construct <code>C opt</code> in the case where <code>opt</code> is <code>none</code> and in the case where <code>opt</code> is <code>some a</code></p>

#### [ Mario Carneiro (Apr 10 2018 at 09:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124874009):
<p>Actually the constant is <code>my_option.rec_on</code>, and of course <code>my_option</code> itself is also a constant</p>

#### [ Gabriel Ebner (Apr 10 2018 at 09:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124874019):
<p><code>rec_on</code> should be a definition as well.  <code>rec</code> is the recursor constant.</p>

#### [ Simon Hudon (Apr 10 2018 at 09:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124874021):
<p>Aren't <code>rec_on</code> and <code>cases_on</code> defined in term of each other?</p>

#### [ Mario Carneiro (Apr 10 2018 at 09:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124874026):
<p><code>rec_on</code> and <code>cases_on</code> are the same for a nonrecursive inductive type</p>

#### [ Simon Hudon (Apr 10 2018 at 09:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124874078):
<p>What I mean is, for recursive inductive types, do we actually have two separate constants for <code>cases</code> and <code>rec</code>?</p>

#### [ Mario Carneiro (Apr 10 2018 at 09:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124874127):
<p>there is no <code>cases</code> for some reason, just <code>cases_on</code>, and no, <code>rec</code> is the only elimination-like constant, <code>cases_on</code> just ignores the inductive hypotheses</p>

#### [ Kevin Buzzard (Apr 10 2018 at 09:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124874175):
<p><span class="user-mention" data-user-id="110026">@Simon Hudon</span> <a href="https://xenaproject.wordpress.com/2018/03/24/no-confusion-over-no_confusion/" target="_blank" title="https://xenaproject.wordpress.com/2018/03/24/no-confusion-over-no_confusion/">https://xenaproject.wordpress.com/2018/03/24/no-confusion-over-no_confusion/</a> -- <code>no_confusion</code> is defined in terms of the eliminator, but I always found the definition rather obscure. I wrote some notes about it in the link.</p>

#### [ Simon Hudon (Apr 10 2018 at 09:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124874176):
<p>Ok, that's what I thought. So I cut some cornets in my explanation by making it about <code>cases_on</code> instead of <code>rec</code></p>

#### [ Simon Hudon (Apr 10 2018 at 09:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124874189):
<p><span class="user-mention" data-user-id="110038">@Kevin Buzzard</span> Thanks! I was sure it had to be postulated too. I guess i got confused <span class="emoji emoji-1f61d" title="stuck out tongue closed eyes">:stuck_out_tongue_closed_eyes:</span></p>

#### [ Sean Leather (Apr 10 2018 at 09:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124874229):
<p>Just for the sake of completeness and posterity, is this what everybody is seeing after <code>#print prefix my_option</code>?</p>
<div class="codehilite"><pre><span></span><span class="n">my_option</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u_1</span> <span class="bp">→</span> <span class="kt">Type</span> <span class="n">u_1</span>
<span class="n">my_option</span><span class="bp">.</span><span class="n">cases_on</span> <span class="o">:</span> <span class="bp">Π</span> <span class="o">{</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u_1</span><span class="o">}</span> <span class="o">{</span><span class="n">C</span> <span class="o">:</span> <span class="n">my_option</span> <span class="n">α</span> <span class="bp">→</span> <span class="n">Sort</span> <span class="n">l</span><span class="o">}</span> <span class="o">(</span><span class="n">n</span> <span class="o">:</span> <span class="n">my_option</span> <span class="n">α</span><span class="o">),</span>
  <span class="n">C</span> <span class="o">(</span><span class="n">my_option</span><span class="bp">.</span><span class="n">none</span> <span class="n">α</span><span class="o">)</span> <span class="bp">→</span> <span class="o">(</span><span class="bp">Π</span> <span class="o">(</span><span class="n">a</span> <span class="o">:</span> <span class="n">α</span><span class="o">),</span> <span class="n">C</span> <span class="o">(</span><span class="n">my_option</span><span class="bp">.</span><span class="n">some</span> <span class="n">a</span><span class="o">))</span> <span class="bp">→</span> <span class="n">C</span> <span class="n">n</span>
<span class="n">my_option</span><span class="bp">.</span><span class="n">has_sizeof_inst</span> <span class="o">:</span> <span class="bp">Π</span> <span class="o">(</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u_1</span><span class="o">)</span> <span class="o">[</span><span class="n">α_inst</span> <span class="o">:</span> <span class="n">has_sizeof</span> <span class="n">α</span><span class="o">],</span> <span class="n">has_sizeof</span> <span class="o">(</span><span class="n">my_option</span> <span class="n">α</span><span class="o">)</span>
<span class="n">my_option</span><span class="bp">.</span><span class="n">no_confusion</span> <span class="o">:</span> <span class="bp">Π</span> <span class="o">{</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u_1</span><span class="o">}</span> <span class="o">{</span><span class="n">P</span> <span class="o">:</span> <span class="n">Sort</span> <span class="n">l</span><span class="o">}</span> <span class="o">{</span><span class="n">v1</span> <span class="n">v2</span> <span class="o">:</span> <span class="n">my_option</span> <span class="n">α</span><span class="o">},</span> <span class="n">v1</span> <span class="bp">=</span> <span class="n">v2</span> <span class="bp">→</span> <span class="n">my_option</span><span class="bp">.</span><span class="n">no_confusion_type</span> <span class="n">P</span> <span class="n">v1</span> <span class="n">v2</span>
<span class="n">my_option</span><span class="bp">.</span><span class="n">no_confusion_type</span> <span class="o">:</span> <span class="bp">Π</span> <span class="o">{</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u_1</span><span class="o">},</span> <span class="n">Sort</span> <span class="n">l</span> <span class="bp">→</span> <span class="n">my_option</span> <span class="n">α</span> <span class="bp">→</span> <span class="n">my_option</span> <span class="n">α</span> <span class="bp">→</span> <span class="n">Sort</span> <span class="n">l</span>
<span class="n">my_option</span><span class="bp">.</span><span class="n">none</span> <span class="o">:</span> <span class="bp">Π</span> <span class="o">(</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u_1</span><span class="o">),</span> <span class="n">my_option</span> <span class="n">α</span>
<span class="n">my_option</span><span class="bp">.</span><span class="n">none</span><span class="bp">.</span><span class="n">inj</span> <span class="o">:</span> <span class="bp">∀</span> <span class="o">{</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u_1</span><span class="o">},</span> <span class="n">my_option</span><span class="bp">.</span><span class="n">none</span> <span class="n">α</span> <span class="bp">=</span> <span class="n">my_option</span><span class="bp">.</span><span class="n">none</span> <span class="n">α</span> <span class="bp">→</span> <span class="n">true</span>
<span class="n">my_option</span><span class="bp">.</span><span class="n">none</span><span class="bp">.</span><span class="n">inj_arrow</span> <span class="o">:</span> <span class="bp">Π</span> <span class="o">{</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u_1</span><span class="o">},</span> <span class="n">my_option</span><span class="bp">.</span><span class="n">none</span> <span class="n">α</span> <span class="bp">=</span> <span class="n">my_option</span><span class="bp">.</span><span class="n">none</span> <span class="n">α</span> <span class="bp">→</span> <span class="bp">Π</span> <span class="o">⦃</span><span class="n">P</span> <span class="o">:</span> <span class="n">Sort</span> <span class="n">l</span><span class="o">⦄,</span> <span class="o">(</span><span class="n">true</span> <span class="bp">→</span> <span class="n">P</span><span class="o">)</span> <span class="bp">→</span> <span class="n">P</span>
<span class="n">my_option</span><span class="bp">.</span><span class="n">none</span><span class="bp">.</span><span class="n">inj_eq</span> <span class="o">:</span> <span class="bp">∀</span> <span class="o">{</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u_1</span><span class="o">},</span> <span class="n">my_option</span><span class="bp">.</span><span class="n">none</span> <span class="n">α</span> <span class="bp">=</span> <span class="n">my_option</span><span class="bp">.</span><span class="n">none</span> <span class="n">α</span> <span class="bp">=</span> <span class="n">true</span>
<span class="n">my_option</span><span class="bp">.</span><span class="n">none</span><span class="bp">.</span><span class="n">sizeof_spec</span> <span class="o">:</span> <span class="bp">∀</span> <span class="o">(</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u_1</span><span class="o">)</span> <span class="o">[</span><span class="n">α_inst</span> <span class="o">:</span> <span class="n">has_sizeof</span> <span class="n">α</span><span class="o">],</span> <span class="n">my_option</span><span class="bp">.</span><span class="n">sizeof</span> <span class="n">α</span> <span class="o">(</span><span class="n">my_option</span><span class="bp">.</span><span class="n">none</span> <span class="n">α</span><span class="o">)</span> <span class="bp">=</span> <span class="mi">1</span>
<span class="n">my_option</span><span class="bp">.</span><span class="n">rec</span> <span class="o">:</span> <span class="bp">Π</span> <span class="o">{</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u_1</span><span class="o">}</span> <span class="o">{</span><span class="n">C</span> <span class="o">:</span> <span class="n">my_option</span> <span class="n">α</span> <span class="bp">→</span> <span class="n">Sort</span> <span class="n">l</span><span class="o">},</span>
  <span class="n">C</span> <span class="o">(</span><span class="n">my_option</span><span class="bp">.</span><span class="n">none</span> <span class="n">α</span><span class="o">)</span> <span class="bp">→</span> <span class="o">(</span><span class="bp">Π</span> <span class="o">(</span><span class="n">a</span> <span class="o">:</span> <span class="n">α</span><span class="o">),</span> <span class="n">C</span> <span class="o">(</span><span class="n">my_option</span><span class="bp">.</span><span class="n">some</span> <span class="n">a</span><span class="o">))</span> <span class="bp">→</span> <span class="bp">Π</span> <span class="o">(</span><span class="n">n</span> <span class="o">:</span> <span class="n">my_option</span> <span class="n">α</span><span class="o">),</span> <span class="n">C</span> <span class="n">n</span>
<span class="n">my_option</span><span class="bp">.</span><span class="n">rec_on</span> <span class="o">:</span> <span class="bp">Π</span> <span class="o">{</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u_1</span><span class="o">}</span> <span class="o">{</span><span class="n">C</span> <span class="o">:</span> <span class="n">my_option</span> <span class="n">α</span> <span class="bp">→</span> <span class="n">Sort</span> <span class="n">l</span><span class="o">}</span> <span class="o">(</span><span class="n">n</span> <span class="o">:</span> <span class="n">my_option</span> <span class="n">α</span><span class="o">),</span>
  <span class="n">C</span> <span class="o">(</span><span class="n">my_option</span><span class="bp">.</span><span class="n">none</span> <span class="n">α</span><span class="o">)</span> <span class="bp">→</span> <span class="o">(</span><span class="bp">Π</span> <span class="o">(</span><span class="n">a</span> <span class="o">:</span> <span class="n">α</span><span class="o">),</span> <span class="n">C</span> <span class="o">(</span><span class="n">my_option</span><span class="bp">.</span><span class="n">some</span> <span class="n">a</span><span class="o">))</span> <span class="bp">→</span> <span class="n">C</span> <span class="n">n</span>
<span class="n">my_option</span><span class="bp">.</span><span class="n">sizeof</span> <span class="o">:</span> <span class="bp">Π</span> <span class="o">(</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u_1</span><span class="o">)</span> <span class="o">[</span><span class="n">α_inst</span> <span class="o">:</span> <span class="n">has_sizeof</span> <span class="n">α</span><span class="o">],</span> <span class="n">my_option</span> <span class="n">α</span> <span class="bp">→</span> <span class="bp">ℕ</span>
<span class="n">my_option</span><span class="bp">.</span><span class="n">some</span> <span class="o">:</span> <span class="bp">Π</span> <span class="o">{</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u_1</span><span class="o">},</span> <span class="n">α</span> <span class="bp">→</span> <span class="n">my_option</span> <span class="n">α</span>
<span class="n">my_option</span><span class="bp">.</span><span class="n">some</span><span class="bp">.</span><span class="n">inj</span> <span class="o">:</span> <span class="bp">∀</span> <span class="o">{</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u_1</span><span class="o">}</span> <span class="o">{</span><span class="n">a</span> <span class="n">a_1</span> <span class="o">:</span> <span class="n">α</span><span class="o">},</span> <span class="n">my_option</span><span class="bp">.</span><span class="n">some</span> <span class="n">a</span> <span class="bp">=</span> <span class="n">my_option</span><span class="bp">.</span><span class="n">some</span> <span class="n">a_1</span> <span class="bp">→</span> <span class="n">a</span> <span class="bp">=</span> <span class="n">a_1</span>
<span class="n">my_option</span><span class="bp">.</span><span class="n">some</span><span class="bp">.</span><span class="n">inj_arrow</span> <span class="o">:</span> <span class="bp">Π</span> <span class="o">{</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u_1</span><span class="o">}</span> <span class="o">{</span><span class="n">a</span> <span class="n">a_1</span> <span class="o">:</span> <span class="n">α</span><span class="o">},</span> <span class="n">my_option</span><span class="bp">.</span><span class="n">some</span> <span class="n">a</span> <span class="bp">=</span> <span class="n">my_option</span><span class="bp">.</span><span class="n">some</span> <span class="n">a_1</span> <span class="bp">→</span> <span class="bp">Π</span> <span class="o">⦃</span><span class="n">P</span> <span class="o">:</span> <span class="n">Sort</span> <span class="n">l</span><span class="o">⦄,</span> <span class="o">(</span><span class="n">a</span> <span class="bp">=</span> <span class="n">a_1</span> <span class="bp">→</span> <span class="n">P</span><span class="o">)</span> <span class="bp">→</span> <span class="n">P</span>
<span class="n">my_option</span><span class="bp">.</span><span class="n">some</span><span class="bp">.</span><span class="n">inj_eq</span> <span class="o">:</span> <span class="bp">∀</span> <span class="o">{</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u_1</span><span class="o">}</span> <span class="o">{</span><span class="n">a</span> <span class="n">a_1</span> <span class="o">:</span> <span class="n">α</span><span class="o">},</span> <span class="n">my_option</span><span class="bp">.</span><span class="n">some</span> <span class="n">a</span> <span class="bp">=</span> <span class="n">my_option</span><span class="bp">.</span><span class="n">some</span> <span class="n">a_1</span> <span class="bp">=</span> <span class="o">(</span><span class="n">a</span> <span class="bp">=</span> <span class="n">a_1</span><span class="o">)</span>
<span class="n">my_option</span><span class="bp">.</span><span class="n">some</span><span class="bp">.</span><span class="n">sizeof_spec</span> <span class="o">:</span> <span class="bp">∀</span> <span class="o">(</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u_1</span><span class="o">)</span> <span class="o">[</span><span class="n">α_inst</span> <span class="o">:</span> <span class="n">has_sizeof</span> <span class="n">α</span><span class="o">]</span> <span class="o">(</span><span class="n">a</span> <span class="o">:</span> <span class="n">α</span><span class="o">),</span> <span class="n">my_option</span><span class="bp">.</span><span class="n">sizeof</span> <span class="n">α</span> <span class="o">(</span><span class="n">my_option</span><span class="bp">.</span><span class="n">some</span> <span class="n">a</span><span class="o">)</span> <span class="bp">=</span> <span class="mi">1</span> <span class="bp">+</span> <span class="n">sizeof</span> <span class="n">a</span>
</pre></div>

#### [ Simon Hudon (Apr 10 2018 at 09:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124874240):
<p>Yes</p>

#### [ Sean Leather (Apr 10 2018 at 09:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124874243):
<p>Awesome. I haven't upgraded Lean in a while, so some things may have changed. <span class="emoji emoji-1f642" title="simple smile">:simple_smile:</span></p>

#### [ Simon Hudon (Apr 10 2018 at 09:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124874244):
<p>Or rather, until other people answer: I don't know</p>

#### [ Kevin Buzzard (Apr 10 2018 at 09:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124874245):
<p><span class="user-mention" data-user-id="110026">@Simon Hudon</span> here's an indication that it doesn't have to be postulated -- once you have <code>cases</code> for <code>nat</code> you can define <code>is_zero</code> by <code>is_zero 0 = tt</code> and <code>is_zero (succ n) = ff</code> and then prove that zero can't be a successor that way.</p>

#### [ Kevin Buzzard (Apr 10 2018 at 09:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124874287):
<p>Is this what _everybody_ is seeing??</p>

#### [ Kevin Buzzard (Apr 10 2018 at 09:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124874290):
<p>I don't know either.</p>

#### [ Sean Leather (Apr 10 2018 at 09:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124874297):
<p>One response was enough for me, it seems.</p>

#### [ Kevin Buzzard (Apr 10 2018 at 09:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124874298):
<p>[i.e. it's what I am seeing]</p>

#### [ Kenny Lau (Apr 10 2018 at 09:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124874302):
<blockquote>
<p>Is this what _everybody_ is seeing??</p>
</blockquote>
<p>we all know you teach m1f</p>

#### [ Simon Hudon (Apr 10 2018 at 09:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124874311):
<p>I don't. What is m1f?</p>

#### [ Sean Leather (Apr 10 2018 at 09:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124874312):
<p>I only required an extistential result, rather than a universal quantification.</p>

#### [ Kevin Buzzard (Apr 10 2018 at 09:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124874317):
<p>m1f = introduction to proof course</p>

#### [ Kenny Lau (Apr 10 2018 at 09:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124874358):
<p><span class="user-mention" data-user-id="110038">@Kevin Buzzard</span> one should probably change the course name then</p>

#### [ Simon Hudon (Apr 10 2018 at 09:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124874359):
<p>So let's rephrase then: does there exist a participant other than myself that also sees the following output ... ?</p>

#### [ Kevin Buzzard (Apr 10 2018 at 09:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124874360):
<p>Yes.</p>

#### [ Nima (Apr 10 2018 at 09:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124874361):
<p>Yes</p>

#### [ Sean Leather (Apr 10 2018 at 09:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124874422):
<p><span class="user-mention" data-user-id="110064">@Kenny Lau</span> I think it's not only the <a href="#narrow/stream/113488-general/subject/constructing.20proofs.20by.20hand/near/124872856" title="#narrow/stream/113488-general/subject/constructing.20proofs.20by.20hand/near/124872856">dictionary</a> that uses English to describe English. We also do that here.</p>

#### [ Kenny Lau (Apr 10 2018 at 09:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124874443):
<p>doom day's clock is ticking</p>

#### [ Sean Leather (Apr 10 2018 at 09:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124874490):
<p><span class="user-mention" data-user-id="112062">@Nima</span> I'm just curious what your background is relevant to Lean. Have you worked with functional programming or proof assistants?</p>

#### [ Simon Hudon (Apr 10 2018 at 09:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124874634):
<p>Alright! Enough excitement for today. I have to wake up in a few hours and get back to writing. Good &lt;&lt;insert current period of the day of your timezone here&gt;&gt; everyone!</p>

#### [ Sean Leather (Apr 10 2018 at 09:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124874652):
<p>And good night to you, <span class="user-mention" data-user-id="110026">@Simon Hudon</span>!</p>

#### [ Moses Schönfinkel (Apr 10 2018 at 09:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124874654):
<p>Good night. <span class="user-mention" data-user-id="110045">@Sean Leather</span> has returned too, neat! Hello.</p>

#### [ Kevin Buzzard (Apr 10 2018 at 09:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124874656):
<p>You can check time zones on Zulip I noticed.</p>

#### [ Kenny Lau (Apr 10 2018 at 09:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124874658):
<p>interesting</p>

#### [ Sean Leather (Apr 10 2018 at 09:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124874661):
<p><span class="user-mention" data-user-id="110027">@Moses Schönfinkel</span> Hello, hello! You don't have any news on Lean 5 to tell me about, do you? <span class="emoji emoji-1f61f" title="worried">:worried:</span></p>

#### [ Kevin Buzzard (Apr 10 2018 at 09:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124874663):
<p>click on the down-arrow which appears when you mouse over a person's name on the right</p>

#### [ Kevin Buzzard (Apr 10 2018 at 09:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124874703):
<p>and you see their local time</p>

#### [ Moses Schönfinkel (Apr 10 2018 at 09:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124874704):
<p>I have been having some issues with my crystal ball ever since my cat cracked it.</p>

#### [ Kevin Buzzard (Apr 10 2018 at 09:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124874706):
<p>although Kenny went from Lon to HK and didn't update his</p>

#### [ Nima (Apr 10 2018 at 09:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124874708):
<blockquote>
<p>functional programming:</p>
</blockquote>
<p>Only Scala, which based on what I see, I would not be surprised if people find it insulting that I put Scala and FP side by side ;)</p>
<blockquote>
<p>proof assistants</p>
</blockquote>
<p>I worked with PVS, for example, I have a paper in which I said something is wrong and this is the right version. In order to be more confident, I proved some of the stuff in PVS (about 25K proof commands, which of course could be very inefficient proofs)</p>

#### [ Kenny Lau (Apr 10 2018 at 09:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124874716):
<blockquote>
<p>although Kenny went from Lon to HK and didn't update his</p>
</blockquote>
<p>done</p>

#### [ Moses Schönfinkel (Apr 10 2018 at 09:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124874766):
<p>Scala is the best way to target JVM.</p>

#### [ Simon Hudon (Apr 10 2018 at 09:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124874825):
<p><span class="user-mention" data-user-id="112062">@Nima</span> Would you mind giving us a reference to your paper? I did some PVS too and I'd like to see what you did</p>

#### [ Nima (Apr 10 2018 at 09:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124874898):
<p>Revisiting MITL to Fix Decision Procedures <br>
<a href="https://link.springer.com/chapter/10.1007/978-3-319-73721-8_22" target="_blank" title="https://link.springer.com/chapter/10.1007/978-3-319-73721-8_22">https://link.springer.com/chapter/10.1007/978-3-319-73721-8_22</a><br>
Proofs can be found here (link is also in the paper)<br>
<a href="http://uofi.box.com/v/PVSProofsOfMITL" target="_blank" title="http://uofi.box.com/v/PVSProofsOfMITL">http://uofi.box.com/v/PVSProofsOfMITL</a></p>

#### [ Simon Hudon (Apr 10 2018 at 09:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124874946):
<p>Thanks!</p>

#### [ Simon Hudon (Apr 10 2018 at 09:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124874949):
<p>Ok, now I'm really off</p>

#### [ Nima (Apr 10 2018 at 21:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124899110):
<p>I have a type <code>constraint</code> which represents something like <code>bnd &lt; x</code> or <code>x &lt; bnd</code>.<br>
I have a function <code>sem</code> (semantics) that receives a constraint as input and return a predicate one <code>ℕ</code> as output (the set of values satisfied by the constraint). Let <code>c</code> be a constraint. I would like to be able to write <code>x : c</code>. For that, I have the following code, but I am not sure about <code>{x // sem S x}</code>. Is there a mistake or a better way there?</p>
<div class="codehilite"><pre><span></span><span class="kn">open</span> <span class="n">nat</span>

<span class="kn">inductive</span> <span class="n">constraint</span>
<span class="bp">|</span> <span class="n">low</span> <span class="o">(</span><span class="n">bnd</span><span class="o">:</span> <span class="bp">ℕ</span><span class="o">)</span>
<span class="bp">|</span> <span class="n">upp</span> <span class="o">(</span><span class="n">bnd</span><span class="o">:</span> <span class="bp">ℕ</span><span class="o">)</span>
<span class="kn">open</span> <span class="n">constraint</span>

<span class="n">def</span> <span class="n">sem</span> <span class="o">(</span><span class="n">c</span> <span class="o">:</span> <span class="n">constraint</span><span class="o">)</span> <span class="o">(</span><span class="n">a</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">)</span> <span class="o">:</span> <span class="kt">Prop</span> <span class="o">:=</span>
<span class="k">match</span> <span class="n">c</span> <span class="k">with</span>
<span class="bp">|</span> <span class="n">low</span> <span class="n">bnd</span> <span class="o">:=</span> <span class="n">bnd</span> <span class="bp">&lt;</span> <span class="n">a</span>
<span class="bp">|</span> <span class="n">upp</span> <span class="n">bnd</span> <span class="o">:=</span> <span class="n">a</span> <span class="bp">&lt;</span> <span class="n">bnd</span>
<span class="kn">end</span>

<span class="kn">instance</span> <span class="n">constraint_to_pred</span> <span class="o">:</span>
  <span class="n">has_coe</span> <span class="o">(</span><span class="n">constraint</span><span class="o">)</span> <span class="o">(</span><span class="bp">ℕ</span> <span class="bp">→</span> <span class="kt">Prop</span><span class="o">)</span> <span class="o">:=</span>
  <span class="bp">⟨λ</span> <span class="n">c</span><span class="o">,</span> <span class="bp">λ</span> <span class="n">a</span><span class="o">,</span> <span class="n">sem</span> <span class="n">c</span> <span class="n">a</span><span class="bp">⟩</span>

<span class="kn">instance</span> <span class="n">constraint_to_sort</span><span class="o">:</span>
  <span class="n">has_coe_to_sort</span> <span class="o">(</span><span class="n">constraint</span> <span class="o">)</span> <span class="o">:=</span>
  <span class="o">{</span><span class="n">S</span> <span class="o">:=</span> <span class="kt">Type</span><span class="bp">*</span><span class="o">,</span> <span class="n">coe</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">S</span><span class="o">,</span> <span class="o">{</span><span class="n">x</span> <span class="bp">//</span> <span class="n">sem</span> <span class="n">S</span> <span class="n">x</span><span class="o">}}</span>
</pre></div>


<p>If everything is fine, how do I finish the following example:</p>
<div class="codehilite"><pre><span></span><span class="kn">example</span> <span class="o">:</span> <span class="bp">∀</span> <span class="n">a</span> <span class="o">:</span> <span class="o">(</span><span class="n">low</span> <span class="mi">1</span><span class="o">),</span> <span class="n">a</span><span class="bp">.</span><span class="n">val</span> <span class="bp">&gt;</span> <span class="mi">1</span> <span class="o">:=</span>
<span class="k">begin</span>
  <span class="n">intro</span> <span class="n">a</span><span class="o">,</span>
  <span class="n">admit</span><span class="o">,</span>
<span class="kn">end</span>
</pre></div>

#### [ Simon Hudon (Apr 10 2018 at 21:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124899250):
<p>It looks good to me except that I don't know that you actually need the <code>has_coe</code> instance</p>

#### [ Simon Hudon (Apr 10 2018 at 21:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124899258):
<p>For the proof, you can try:</p>
<div class="codehilite"><pre><span></span><span class="kn">example</span> <span class="o">:</span> <span class="bp">∀</span> <span class="n">a</span> <span class="o">:</span> <span class="o">(</span><span class="n">low</span> <span class="mi">1</span><span class="o">),</span> <span class="n">a</span><span class="bp">.</span><span class="n">val</span> <span class="bp">&gt;</span> <span class="mi">1</span> <span class="o">:=</span>
<span class="k">begin</span>
  <span class="n">unfold_coes</span><span class="o">,</span>
  <span class="n">intro</span> <span class="n">a</span><span class="o">,</span>
  <span class="n">admit</span><span class="o">,</span>
<span class="kn">end</span>
</pre></div>

#### [ Simon Hudon (Apr 10 2018 at 21:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124899280):
<p>It should unfold all the coercions and then you should see a clear way to finishing the proof</p>

#### [ Nima (Apr 10 2018 at 21:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124899441):
<p>If I comment the first instance then the second one won't type check (may be because of <code>{x // sem S x}</code> that I prefer not to have any way)</p>
<div class="codehilite"><pre><span></span>type mismatch at field &#39;coe&#39;
  λ (S : constraint), {x // ⁇}
has type
  constraint → Sort (max 1 ?) : Type (max 1 ?)
but is expected to have type
  constraint → Type ? : Type (?+1)
</pre></div>


<p>If I don't comment the first instance then I will receive the following error: <code>unknown identifier 'unfold_coes'</code></p>

#### [ Simon Hudon (Apr 10 2018 at 21:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124899492):
<p>You need <code>import tactic</code></p>

#### [ Simon Hudon (Apr 10 2018 at 21:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124899573):
<p>If you want to remove the first instance, I think you need to change the second to:</p>
<div class="codehilite"><pre><span></span>instance constraint_to_sort:
  has_coe_to_sort (constraint ) :=
  {S := Sort*, coe := λ S, {x // sem S x}}
</pre></div>

#### [ Nima (Apr 10 2018 at 21:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124899844):
<p>OK, I don't know what happened, but removing the first instance does not give me error any more</p>
<blockquote>
<p>You need import tactic</p>
</blockquote>
<p>Do you mean <code>open tactic</code>? Line <code>import init.meta.tactic</code> will type check, but <code>import tactic</code> will not.</p>

#### [ Simon Hudon (Apr 10 2018 at 21:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124899858):
<p>You're not using <code>leanpkg</code> and <code>mathlib</code> right? Now would be a good time to bring them in</p>

#### [ Simon Hudon (Apr 10 2018 at 21:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124899909):
<p>In a terminal where your sources are, type in:</p>
<div class="codehilite"><pre><span></span>leanpkg init lets-learn-some-lean
leanpkg add leanprover/mathlib
</pre></div>

#### [ Nima (Apr 10 2018 at 22:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124902193):
<p>OK, I have imported tactic. But I still receive the same error.</p>
<div class="codehilite"><pre><span></span><span class="kn">import</span> <span class="n">tactic</span>
<span class="kn">import</span> <span class="n">tactic</span><span class="bp">.</span><span class="n">interactive</span>
<span class="kn">open</span> <span class="n">nat</span>

<span class="kn">inductive</span> <span class="n">constraint</span>
<span class="bp">|</span> <span class="n">low</span> <span class="o">(</span><span class="n">bnd</span><span class="o">:</span> <span class="bp">ℕ</span><span class="o">)</span>
<span class="bp">|</span> <span class="n">upp</span> <span class="o">(</span><span class="n">bnd</span><span class="o">:</span> <span class="bp">ℕ</span><span class="o">)</span>
<span class="kn">open</span> <span class="n">constraint</span>

<span class="n">def</span> <span class="n">sem</span> <span class="o">(</span><span class="n">c</span> <span class="o">:</span> <span class="n">constraint</span><span class="o">)</span> <span class="o">(</span><span class="n">a</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">)</span> <span class="o">:</span> <span class="kt">Prop</span> <span class="o">:=</span>
<span class="k">match</span> <span class="n">c</span> <span class="k">with</span>
<span class="bp">|</span> <span class="n">low</span> <span class="n">bnd</span> <span class="o">:=</span> <span class="n">bnd</span> <span class="bp">&lt;</span> <span class="n">a</span>
<span class="bp">|</span> <span class="n">upp</span> <span class="n">bnd</span> <span class="o">:=</span> <span class="n">a</span> <span class="bp">&lt;</span> <span class="n">bnd</span>
<span class="kn">end</span>

<span class="c1">-- this instance seems redundant for now</span>
<span class="kn">instance</span> <span class="n">constraint_to_pred</span> <span class="o">:</span>
  <span class="n">has_coe</span> <span class="o">(</span><span class="n">constraint</span><span class="o">)</span> <span class="o">(</span><span class="bp">ℕ</span> <span class="bp">→</span> <span class="kt">Prop</span><span class="o">)</span> <span class="o">:=</span>
  <span class="bp">⟨λ</span> <span class="n">c</span><span class="o">,</span> <span class="bp">λ</span> <span class="n">a</span><span class="o">,</span> <span class="n">sem</span> <span class="n">c</span> <span class="n">a</span><span class="bp">⟩</span>

<span class="kn">instance</span> <span class="n">constraint_to_sort</span><span class="o">:</span>
  <span class="n">has_coe_to_sort</span> <span class="o">(</span><span class="n">constraint</span> <span class="o">)</span> <span class="o">:=</span>
  <span class="o">{</span><span class="n">S</span> <span class="o">:=</span> <span class="kt">Type</span><span class="bp">*</span><span class="o">,</span> <span class="n">coe</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">S</span><span class="o">,</span> <span class="o">{</span><span class="n">x</span> <span class="bp">//</span> <span class="n">sem</span> <span class="n">S</span> <span class="n">x</span><span class="o">}}</span>

<span class="kn">example</span> <span class="o">:</span> <span class="bp">∀</span> <span class="n">a</span> <span class="o">:</span> <span class="o">(</span><span class="n">low</span> <span class="mi">1</span><span class="o">),</span> <span class="n">a</span><span class="bp">.</span><span class="n">val</span> <span class="bp">&gt;</span> <span class="mi">1</span> <span class="o">:=</span>
<span class="k">begin</span>
  <span class="n">unfold_coes</span><span class="o">,</span> <span class="c1">-- ERROR: unknown identifier &#39;unfold_coes&#39;</span>
  <span class="n">intro</span> <span class="n">a</span><span class="o">,</span>
  <span class="n">admit</span><span class="o">,</span>
<span class="kn">end</span>
</pre></div>


<p>I think dependency is successfully created. For example, I can make the following work perfectly fine.</p>
<div class="codehilite"><pre><span></span><span class="kn">variables</span> <span class="n">A</span> <span class="n">B</span> <span class="n">C</span> <span class="n">D</span> <span class="o">:</span> <span class="kt">Prop</span>
<span class="kn">example</span> <span class="o">(</span><span class="n">H</span> <span class="o">:</span> <span class="n">A</span><span class="o">)</span> <span class="o">(</span><span class="n">H₁</span> <span class="o">:</span> <span class="bp">¬</span> <span class="n">B</span><span class="o">)</span> <span class="o">:</span> <span class="bp">¬</span> <span class="o">(</span><span class="n">A</span> <span class="bp">→</span> <span class="n">B</span><span class="o">)</span> <span class="o">:=</span> <span class="k">by</span> <span class="n">finish</span>
</pre></div>


<p>But no luck with <code>unfold_coes</code></p>

#### [ Nima (Apr 12 2018 at 08:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124970239):
<p>Inside a proof, I have two cases. In case 1, I prove something about lower bound and in case 2, I prove something about upper bound. Each case has multiple steps, but the structure is identical (in order to obtain the second part from the first part, all I need to do is replace word <code>mid</code> with <code>max</code>).<br>
How do I write both these cases without practically writing a part of the proof twice?</p>

#### [ Kenny Lau (Apr 12 2018 at 08:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124970283):
<p>where is the word <code>mid</code> and <code>max</code>?</p>

#### [ Kenny Lau (Apr 12 2018 at 08:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124970284):
<p>could you post your code?</p>

#### [ Nima (Apr 12 2018 at 08:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124970345):
<p>The whole code is too long, but here is the part I was talking about (I just wanted to see what the general approach is in these situations. Do you create a whole new <code>meta</code> function, or you can do something inline):</p>
<div class="codehilite"><pre><span></span>  <span class="n">by_cases</span> <span class="n">is_lower_bound</span> <span class="n">c</span> <span class="k">with</span> <span class="n">hl</span> <span class="bp">;</span> <span class="n">simp</span> <span class="o">[</span><span class="n">hl</span><span class="o">],</span>
  <span class="k">begin</span>
    <span class="k">have</span> <span class="n">hl&#39;</span> <span class="o">:=</span> <span class="n">iff</span><span class="bp">.</span><span class="n">mp</span> <span class="o">(</span><span class="n">is_lower_bound_is_lower</span> <span class="n">c</span> <span class="n">ht</span><span class="o">)</span> <span class="n">hl</span><span class="o">,</span>
    <span class="k">have</span> <span class="n">hm</span> <span class="o">:=</span> <span class="n">number</span><span class="bp">.</span><span class="n">min_prop</span> <span class="n">α</span><span class="o">,</span>
    <span class="n">cases</span> <span class="n">number</span><span class="bp">.</span><span class="n">min</span> <span class="n">α</span> <span class="k">with</span> <span class="n">m</span><span class="bp">;</span> <span class="n">unfold</span> <span class="n">min_prop</span> <span class="n">at</span> <span class="n">hm</span><span class="o">,</span>
    <span class="k">begin</span>
      <span class="n">specialize</span> <span class="n">hm</span> <span class="n">bnd</span><span class="o">,</span>
      <span class="n">cases</span> <span class="n">hm</span> <span class="k">with</span> <span class="n">m&#39;</span> <span class="n">hm&#39;</span><span class="o">,</span>
      <span class="n">specialize</span> <span class="n">h₁</span> <span class="n">m&#39;</span><span class="o">,</span>
      <span class="n">unfold</span> <span class="n">sem</span> <span class="n">at</span> <span class="n">h₁</span><span class="o">,</span>
      <span class="n">simp</span> <span class="o">[</span><span class="n">ht</span><span class="o">,</span><span class="n">hb</span><span class="o">,</span><span class="n">hl&#39;</span><span class="o">,</span><span class="n">hs&#39;</span><span class="o">,</span><span class="n">sem</span><span class="o">]</span> <span class="n">at</span> <span class="n">h₁</span><span class="o">,</span>
      <span class="k">have</span> <span class="o">:=</span> <span class="n">iff</span><span class="bp">.</span><span class="n">mp</span> <span class="n">lt_iff_le_not_le</span> <span class="n">hm&#39;</span><span class="o">,</span>
      <span class="n">simp</span> <span class="o">[</span><span class="n">h₁</span><span class="o">,</span><span class="n">this</span><span class="o">]</span> <span class="n">at</span> <span class="n">h₁</span><span class="o">,</span>
      <span class="n">contradiction</span><span class="o">,</span>
    <span class="kn">end</span><span class="o">,</span>
    <span class="n">specialize</span> <span class="n">hm</span> <span class="n">bnd</span><span class="o">,</span>
    <span class="n">specialize</span> <span class="n">h₁</span> <span class="n">m</span><span class="o">,</span>
    <span class="n">unfold</span> <span class="n">sem</span> <span class="n">at</span> <span class="n">h₁</span><span class="o">,</span>
    <span class="n">simp</span> <span class="o">[</span><span class="n">ht</span><span class="o">,</span><span class="n">hb</span><span class="o">,</span><span class="n">hl&#39;</span><span class="o">,</span><span class="n">hs&#39;</span><span class="o">]</span> <span class="n">at</span> <span class="n">h₁</span><span class="o">,</span>
    <span class="n">unfold</span> <span class="n">sem</span> <span class="n">at</span> <span class="n">h₁</span><span class="o">,</span>
    <span class="k">have</span> <span class="o">:=</span> <span class="n">le_antisymm</span> <span class="n">hm</span> <span class="n">h₁</span><span class="o">,</span>
    <span class="n">simp</span> <span class="o">[</span><span class="n">this</span><span class="o">],</span>
  <span class="kn">end</span><span class="o">,</span>
<span class="c1">-- next case replace words &quot;lower&quot; with &quot;upper&quot; and &quot;min&quot; with &quot;max&quot;</span>
</pre></div>

#### [ Mario Carneiro (Apr 12 2018 at 08:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124970386):
<p>You are not likely to be able to simplify this unless you formalize the symmetry between <code>min</code> and <code>max</code> here</p>

#### [ Mario Carneiro (Apr 12 2018 at 08:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124970390):
<p>You can try to extract a lemma with something with the same type as <code>min</code> and <code>max</code></p>

#### [ Nima (Apr 12 2018 at 08:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124970450):
<p>If I don't extract any lemma, is there any way, I can write this proof but replace for example <code>(is_lower_bound_is_lower c ht)</code> with a placeholder and later fill that placeholder twice?</p>

#### [ Mario Carneiro (Apr 12 2018 at 08:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124970504):
<p>You can run the same tactic script twice. As long as you set up the state (before or after) with suitable modifications, you can do this kind of thing</p>

#### [ Mario Carneiro (Apr 12 2018 at 08:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124970548):
<p>For example, you could have <code>have lem := is_lower_bound_is_lower</code> in one branch and <code>have lem := is_upper_bound_is_upper</code> in the other branch, and then run a script that refers to <code>lem</code> which means different things in the two branches</p>

#### [ Nima (Apr 12 2018 at 08:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124970597):
<p>gotcha, thanks</p>

#### [ Kenny Lau (Apr 12 2018 at 08:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124970598):
<p>or just copy it once already</p>

#### [ Nima (Apr 12 2018 at 08:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124971067):
<p>How do I combine the following two:</p>
<div class="codehilite"><pre><span></span><span class="n">unfold</span> <span class="n">f1</span> <span class="n">at</span> <span class="n">h1</span> <span class="n">h2</span> <span class="c1">-- only at h1 and h2</span>
<span class="n">unfold</span> <span class="n">f1</span> <span class="c1">-- only at goal (?)</span>
</pre></div>

#### [ Mario Carneiro (Apr 12 2018 at 08:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124971268):
<p><code>unfold f1</code> can also be written <code>unfold f1 at |-</code>, and you can do both with <code>unfold f1 at h1 h2 |-</code></p>

#### [ Mario Carneiro (Apr 12 2018 at 08:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124971269):
<p>there's also a unicode version of <code>|-</code></p>

#### [ Nima (Apr 12 2018 at 08:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124971554):
<p>thanks</p>

#### [ Simon Hudon (Apr 12 2018 at 13:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/124981003):
<p>I wonder if <code>wlog</code> might be of help for your repetition problem. Like Mario said, you'd need to formalize the symmetry some more but maybe <code>wlog</code> can do some of that</p>

#### [ Nima (Apr 12 2018 at 23:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/125005327):
<p>Sorry, but how do I finish this example?</p>
<div class="codehilite"><pre><span></span>class number := (aa1 := tt)
example [nn:number] : number.aa1 = tt := sorry
</pre></div>

#### [ Simon Hudon (Apr 12 2018 at 23:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/125005396):
<p>Try <code>by simp!</code></p>

#### [ Simon Hudon (Apr 12 2018 at 23:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/125005400):
<p>(the <code>!</code> is part of the proof)</p>

#### [ Nima (Apr 12 2018 at 23:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/125005417):
<p>I got error: <code>command expected</code></p>

#### [ Simon Hudon (Apr 12 2018 at 23:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/125005472):
<p>Restart your Lean server (C-c C-r in emacs)</p>

#### [ Nima (Apr 12 2018 at 23:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/125005522):
<p>I am on VS Code, restarted the whole program. But no luck!</p>
<div class="codehilite"><pre><span></span><span class="n">class</span> <span class="n">number</span> <span class="o">:=</span> <span class="o">(</span><span class="n">aa1</span> <span class="o">:=</span> <span class="n">tt</span><span class="o">)</span>
<span class="kn">example</span> <span class="o">[</span><span class="n">nn</span><span class="o">:</span><span class="n">number</span><span class="o">]</span> <span class="o">:</span> <span class="n">number</span><span class="bp">.</span><span class="n">aa1</span> <span class="bp">=</span> <span class="n">tt</span> <span class="o">:=</span> <span class="k">by</span> <span class="n">simp</span><span class="bp">!</span>  <span class="c1">-- error command expected</span>
</pre></div>


<p>Lean 3.3.0</p>

#### [ Simon Hudon (Apr 12 2018 at 23:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/125005571):
<p>Oh! 3.3.0 ...</p>

#### [ Simon Hudon (Apr 12 2018 at 23:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/125005574):
<p>ok, one sec</p>

#### [ Simon Hudon (Apr 12 2018 at 23:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/125005580):
<p>ok <code>by refl</code> should do it</p>

#### [ Nima (Apr 12 2018 at 23:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/125005670):
<div class="codehilite"><pre><span></span><span class="n">invalid</span> <span class="n">apply</span> <span class="n">tactic</span><span class="o">,</span> <span class="n">failed</span> <span class="n">to</span> <span class="n">unify</span>
  <span class="n">number</span><span class="bp">.</span><span class="n">aa1</span> <span class="bp">=</span> <span class="n">tt</span>
<span class="k">with</span>
  <span class="err">?</span><span class="n">m_2</span> <span class="bp">=</span> <span class="err">?</span><span class="n">m_2</span>
<span class="n">state</span><span class="o">:</span>
<span class="n">nn</span> <span class="o">:</span> <span class="n">number</span>
<span class="err">⊢</span> <span class="n">number</span><span class="bp">.</span><span class="n">aa1</span> <span class="bp">=</span> <span class="n">tt</span>
</pre></div>

#### [ Simon Hudon (Apr 12 2018 at 23:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/125005701):
<p>What happens if you do:</p>
<div class="codehilite"><pre><span></span>begin
  unfold number.aa1
end
</pre></div>

#### [ Simon Hudon (Apr 12 2018 at 23:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/125005794):
<p>Sorry, I just got what is happening. The proof shouldn't work</p>

#### [ Nima (Apr 12 2018 at 23:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/125005855):
<p>Yep, it does not.</p>

#### [ Simon Hudon (Apr 12 2018 at 23:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/125005877):
<p>In <code>class number := (aa1 := tt)</code>, <code>aa1</code> is a field of type <code>bool</code> whose default value (when you build an instance) is <code>tt</code>. You can still specify a different value so you don't know for sure that <code>aa1</code> is <code>tt</code> in your example</p>

#### [ Simon Hudon (Apr 12 2018 at 23:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/125005923):
<p>What are you trying to do with that example? I suspect you're misusing classes</p>

#### [ Nima (Apr 12 2018 at 23:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/125005995):
<p>First, how do I change a default value? Is this like a programming language that I can assign value to variables??<br>
I wanted to show <code>number.has_prev a</code> is decidable for any value <code>a</code>. But I guess you are saying value of <code>has_prev</code> can be changed later (can mark it like a constant! I am lost)</p>
<div class="codehilite"><pre><span></span><span class="o">(</span><span class="n">has_prev</span>  <span class="o">:=</span> <span class="bp">λ</span> <span class="n">a</span><span class="o">:</span><span class="n">α</span><span class="o">,</span> <span class="n">dense</span> <span class="bp">=</span> <span class="n">ff</span> <span class="bp">∧</span> <span class="n">some</span> <span class="n">a</span> <span class="bp">≠</span> <span class="n">min</span><span class="o">)</span>
</pre></div>

#### [ Simon Hudon (Apr 12 2018 at 23:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/125006160):
<p>No, this is not about mutating variables. Think of <code>class number</code> as a type declaration:</p>
<div class="codehilite"><pre><span></span>@[class]
structure number :=
  (aa1 : bool)
</pre></div>


<p>the <code>:= tt</code> part allows you to write:</p>
<div class="codehilite"><pre><span></span>instance : number :=
{ }
</pre></div>


<p>and it is taken to mean:</p>
<div class="codehilite"><pre><span></span>instance : number :=
{ aa1 := tt }
</pre></div>

#### [ Nima (Apr 12 2018 at 23:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/125006189):
<p>ooo!</p>

#### [ Simon Hudon (Apr 12 2018 at 23:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/125006246):
<p>And in keeping with desugaring the <code>class</code> / <code>instance</code> syntax, the latter is equivalent to:</p>
<div class="codehilite"><pre><span></span>@[instance]
def my_number_instance : number :=
{ aa1 := tt }
</pre></div>

#### [ Nima (Apr 12 2018 at 23:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/125006293):
<p>What was I thinking!!<br>
Thanks a lot.</p>

#### [ Simon Hudon (Apr 12 2018 at 23:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/125006340):
<p>No worries</p>

#### [ Nima (Apr 15 2018 at 22:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/125121921):
<p>How do I finish this example without using <code>finish</code>?</p>
<div class="codehilite"><pre><span></span><span class="kn">inductive</span> <span class="n">param</span> <span class="bp">|</span> <span class="n">p1</span> <span class="bp">|</span> <span class="n">p2</span> <span class="bp">|</span> <span class="n">p3</span>
<span class="kn">example</span> <span class="o">:</span> <span class="n">param</span><span class="bp">.</span><span class="n">p1</span> <span class="bp">=</span> <span class="n">param</span><span class="bp">.</span><span class="n">p2</span> <span class="bp">→</span> <span class="n">false</span> <span class="o">:=</span> <span class="n">sorry</span>
</pre></div>

#### [ Patrick Massot (Apr 15 2018 at 22:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/125121986):
<p><code>example : param.p1 = param.p2 → false := λ h, param.no_confusion h</code></p>

#### [ Mario Carneiro (Apr 15 2018 at 22:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/125122032):
<p>you can also use <code>by injection h</code></p>

#### [ Nima (Apr 15 2018 at 22:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/125122172):
<p>Thank you both</p>

#### [ Patrick Massot (Apr 15 2018 at 22:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/125122183):
<p>I think you could create new topics, instead of always reusing the same one. It would make it easier for other readers to decide whether they could learn something from your questions.</p>

#### [ Nima (Apr 15 2018 at 23:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/125123108):
<p>That is definitely an option. However, most (if not all) of my questions are trivially answered by experienced users like Simon or Mario. I look at "Fresh off the boat" as a topic that contains questions a new user like me with a very little experience might ask. Nothing deep, but they come from everywhere (for example, because I read a book and that book talks about lots of different things). That is how I see them related. </p>
<p>Of course, another option is to create one topic for basically every one of them. The point is, 1) I don't know the answer is in <code>no_confusion</code> or <code>injection</code>, so most likely the topic I would create won't have a meaningful representation of its content. 2) I doubt that a user will learn much just by reading a single one of them. Either, they already know the answer, or if they don't, they are likely to benefit from similar questions that now they would not know how to find.</p>
<p>I agree, for some concepts having a separate topic makes a lot of sense. For example, Code Generation, Meta Programming, mathlib (may be each with subtopics as well). But I don't see enough benefit to bloat list of topic by wanting every topic to be as specific as possible. Maybe having both kinds would be more helpful. Some are general-nothing-deep-scattered-subjects and some focused-deep-into-a-concent topics.</p>
<p>Please let me know what you think. If I see you guys prefer separate topics anyway, I will do my best to post that way.</p>

#### [ Simon Hudon (Apr 15 2018 at 23:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/125123341):
<p>I think you can already pick a good topic by describing the problem that you're having. In this case you could say "how to I prove that different constructors form distinct values". I don't think the topic should contain the answer to your question because, if someone has the same problem as you, they won't know to look in the thread you created.</p>

#### [ Simon Hudon (Apr 15 2018 at 23:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/125123382):
<p>You can also pick a very bad topic name and change it later as suggestions come in</p>

#### [ Nima (Apr 15 2018 at 23:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Fresh%20off%20the%20boat/near/125123395):
<p>No problem,<br>
Thanks for letting me know your thought.</p>


{% endraw %}
