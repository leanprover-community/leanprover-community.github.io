---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113489newmembers/53044Variablewithbracesparenthesesandsquarebrackets.html
---

## Stream: [new members](https://leanprover-community.github.io/archive/113489newmembers/index.html)
### Topic: [Variable with braces, parentheses and  square brackets](https://leanprover-community.github.io/archive/113489newmembers/53044Variablewithbracesparenthesesandsquarebrackets.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ AHan (Nov 08 2018 at 07:23)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Variable%20with%20braces%2C%20parentheses%20and%20%20square%20brackets/near/147280537):
<p>The below code works.<br>
However, if I changed the <code>h</code> to <code>pp</code> in function <code>p_mod_range</code>, pp will become unknown identifier....<br>
No matter I changed the brackets of variable pp to parentheses or square brackets or braces, neither of them can make variable <code>pp</code> be identified by lean....<br>
Why can't lean identifies variable <code>pp</code>, and how can I fix this ?</p>
<div class="codehilite"><pre><span></span>import data.nat.prime
import data.int.basic
import data.int.modeq

open nat

lemma mod_range {b : ℕ} : (b &gt; 0) → ∀ (x : ℤ), 0 ≤ x % b ∧ x % b &lt; b :=
begin
  intros h₁ x,
  apply and.intro,
  begin
    apply int.mod_nonneg, simp,
    assume h₃,
    rw h₃ at *,
    cases h₁
  end,
  begin
    apply int.mod_lt_of_pos,
    apply int.coe_nat_lt.elim_right,
    assumption
  end,
end

namespace pf

variables { p: ℕ }  {pp : prime p}

lemma p_mod_range (h: prime p): ∀ (x : ℤ),  0 ≤ x % p ∧ x % p &lt; p :=
  begin
    intro, apply mod_range, apply (prime.pos h),
  end
</pre></div>

#### [ Mario Carneiro (Nov 08 2018 at 08:18)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Variable%20with%20braces%2C%20parentheses%20and%20%20square%20brackets/near/147282373):
<p><code>variables</code> are not added by default to the context of the current theorem unless they appear in the type</p>

#### [ Mario Carneiro (Nov 08 2018 at 08:18)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Variable%20with%20braces%2C%20parentheses%20and%20%20square%20brackets/near/147282417):
<p>you should use <code>include pp</code> to explicitly add it to the context</p>

#### [ AHan (Nov 08 2018 at 08:19)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Variable%20with%20braces%2C%20parentheses%20and%20%20square%20brackets/near/147282435):
<p>Oh Yeah!! include works!</p>

#### [ AHan (Nov 08 2018 at 08:20)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Variable%20with%20braces%2C%20parentheses%20and%20%20square%20brackets/near/147282473):
<p>But why isn't it be added by default to the context?</p>

#### [ Johan Commelin (Nov 08 2018 at 08:28)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Variable%20with%20braces%2C%20parentheses%20and%20%20square%20brackets/near/147282760):
<p>This allows you to introduce a bunch of variables at the top, and selectively use them in the theorems you prove.</p>

#### [ Johan Commelin (Nov 08 2018 at 08:28)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Variable%20with%20braces%2C%20parentheses%20and%20%20square%20brackets/near/147282770):
<p>Otherwise a lot of theorems (and definitions) would have unnecessary assumptions.</p>

#### [ AHan (Nov 08 2018 at 08:33)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Variable%20with%20braces%2C%20parentheses%20and%20%20square%20brackets/near/147282946):
<p>Got it!!<br>
Is the include scope ends until the end of the section or the namespace?<br>
Can I stop include in the middle point, like only include the variables for one function?</p>

#### [ Johan Commelin (Nov 08 2018 at 08:34)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Variable%20with%20braces%2C%20parentheses%20and%20%20square%20brackets/near/147282993):
<p>Yes: <code>omit pp</code>. Otherwise it stops at <code>end section/namespace</code></p>

#### [ AHan (Nov 08 2018 at 08:35)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Variable%20with%20braces%2C%20parentheses%20and%20%20square%20brackets/near/147283011):
<p>Ok! Thanks a lot for the explanations!</p>

#### [ AHan (Nov 08 2018 at 09:21)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Variable%20with%20braces%2C%20parentheses%20and%20%20square%20brackets/near/147284728):
<p>Although including variable works, some functions like <code>has_mul</code>, <code>has_one</code> in the following code, will have to explicitly name out the variables <code>p</code>, <code>p_gt_one</code>.<br>
And which seems to make using the symbols <code>*</code>, <code>1</code> failed, like in function <code>pf_is_right_inv</code> below...<br>
Is there any better way to handle this?</p>
<div class="codehilite"><pre><span></span>def pf {p : ℕ} := {e : ℤ// 0 ≤ e ∧ e &lt; p}

namespace pf

variables { p: ℕ } { p_gt_one : p &gt; 1 } { pp : prime p }
include p_gt_one

def mul (a b : @pf p) : @pf p :=  ⟨(a.val * b.val) % p,  begin apply mod_range, apply (trans p_gt_one zero_lt_one) end⟩
instance : has_mul (@pf p) := ⟨@mul p p_gt_one⟩
protected def one  : @pf p := ⟨1, begin apply and.intro, apply zero_le_one, apply (int.coe_nat_le.elim_right p_gt_one), end⟩
instance : has_one (@pf p) := ⟨@pf.one p p_gt_one⟩

lemma pf_is_right_inv (a : @pf p) : (a.1 &gt; 0) → a * (@pf.inv p p_gt_one a) = 1 := sorry
end pf
</pre></div>

#### [ Johan Commelin (Nov 08 2018 at 09:25)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Variable%20with%20braces%2C%20parentheses%20and%20%20square%20brackets/near/147284864):
<p>I don't think you should have <code>pp</code> and <code>p_gt_one</code>. Because you can deduce <code>p_gt_one</code> from <code>pp</code>.</p>

#### [ Johan Commelin (Nov 08 2018 at 09:25)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Variable%20with%20braces%2C%20parentheses%20and%20%20square%20brackets/near/147284880):
<p>Also, you should make the <code>p</code> argument of <code>pf</code> explicit, so that you can remove the <code>@</code> from <code>pf</code> later.</p>

#### [ AHan (Nov 08 2018 at 09:27)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Variable%20with%20braces%2C%20parentheses%20and%20%20square%20brackets/near/147284948):
<p>yeah I know I can deduce <code>p_gt_one</code> from <code>pp</code>, but I'm thinking of if in some cases like <code>add</code>, <code>mul</code>, <code>sub</code>, maybe I can make it a bit general, since <code>pp</code> isn't actually needed</p>

#### [ Johan Commelin (Nov 08 2018 at 09:30)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Variable%20with%20braces%2C%20parentheses%20and%20%20square%20brackets/near/147285095):
<p>Ok, but then I wouldn't make it a <code>variable</code>. Just include it as an assumption on that line.</p>

#### [ Johan Commelin (Nov 08 2018 at 09:30)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Variable%20with%20braces%2C%20parentheses%20and%20%20square%20brackets/near/147285106):
<p>And consider renaming <code>p</code> to <code>n</code> to show that you also care about non-primes.</p>

#### [ AHan (Nov 08 2018 at 09:32)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Variable%20with%20braces%2C%20parentheses%20and%20%20square%20brackets/near/147285194):
<p>What do you mean include it as an assumption on that line?</p>

#### [ AHan (Nov 08 2018 at 09:32)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Variable%20with%20braces%2C%20parentheses%20and%20%20square%20brackets/near/147285196):
<p>OH yes, renaming is a good suggestion!</p>

#### [ Johan Commelin (Nov 08 2018 at 09:33)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Variable%20with%20braces%2C%20parentheses%20and%20%20square%20brackets/near/147285207):
<p><code>def mul {h : p &gt; 1} (a b : @pf p) : @pf p := blah</code></p>

#### [ Johan Commelin (Nov 08 2018 at 09:33)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Variable%20with%20braces%2C%20parentheses%20and%20%20square%20brackets/near/147285211):
<p>But it will be annoying to use, because you have to carry that proof around all the time.</p>

#### [ Johan Commelin (Nov 08 2018 at 09:34)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Variable%20with%20braces%2C%20parentheses%20and%20%20square%20brackets/near/147285258):
<p>And I think you don't need it.</p>

#### [ Johan Commelin (Nov 08 2018 at 09:34)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Variable%20with%20braces%2C%20parentheses%20and%20%20square%20brackets/near/147285266):
<p>You can define it for <code>p = 1</code> just fine.</p>

#### [ AHan (Nov 08 2018 at 09:34)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Variable%20with%20braces%2C%20parentheses%20and%20%20square%20brackets/near/147285268):
<p>Yes.... seems like really annoying...<br>
Maybe I should give up the idea of taking care of non-primes</p>

#### [ Johan Commelin (Nov 08 2018 at 09:34)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Variable%20with%20braces%2C%20parentheses%20and%20%20square%20brackets/near/147285271):
<p>I guess <code>p = 0</code> is problematic.</p>

#### [ Johan Commelin (Nov 08 2018 at 09:35)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Variable%20with%20braces%2C%20parentheses%20and%20%20square%20brackets/near/147285280):
<p>Sure, after all, others have already done that. So if you are just experimenting, I wouldn't try to be as general as possible.</p>

#### [ AHan (Nov 08 2018 at 09:38)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Variable%20with%20braces%2C%20parentheses%20and%20%20square%20brackets/near/147285399):
<p>Yeah I'm just experimenting, but "others have already done that", do you mean in the mathlib or is it in some other trustable third party library?</p>

#### [ Johan Commelin (Nov 08 2018 at 09:38)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Variable%20with%20braces%2C%20parentheses%20and%20%20square%20brackets/near/147285404):
<p>No in mathlib.</p>

#### [ AHan (Nov 08 2018 at 09:40)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Variable%20with%20braces%2C%20parentheses%20and%20%20square%20brackets/near/147285486):
<p>Which file does it reside in?<br>
Cause this experiment isn't actually my main goal, I did this mainly because my main goal need this, and I didn't find this in mathlib...</p>

#### [ Mario Carneiro (Nov 08 2018 at 09:41)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Variable%20with%20braces%2C%20parentheses%20and%20%20square%20brackets/near/147285516):
<p>What are you doing exactly? I'm not sure if it's in mathlib but I don't know what it is. It looks sort of like <code>zmod</code></p>

#### [ AHan (Nov 08 2018 at 09:45)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Variable%20with%20braces%2C%20parentheses%20and%20%20square%20brackets/near/147285657):
<p>I want to examine some algorithms correctness, and the algorithms need <code>prime field</code><br>
So I'm thinking of defining a type of <code>prime field</code> and use as an instance of class <code>field</code></p>

#### [ Mario Carneiro (Nov 08 2018 at 09:46)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Variable%20with%20braces%2C%20parentheses%20and%20%20square%20brackets/near/147285717):
<p>If by prime field you mean Z/pZ where <code>p</code> is a prime, that's <code>zmod</code></p>

#### [ Mario Carneiro (Nov 08 2018 at 09:47)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Variable%20with%20braces%2C%20parentheses%20and%20%20square%20brackets/near/147285740):
<p>Or do you mean the smallest subfield of a given field? I don't think we have that but you can fake it with <code>rat.cast</code></p>

#### [ AHan (Nov 08 2018 at 09:48)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Variable%20with%20braces%2C%20parentheses%20and%20%20square%20brackets/near/147285787):
<p><span class="user-mention" data-user-id="112680">@Johan Commelin</span>  I've done what you suggested, but the problem that I can't use the symbol <code>*</code> and <code>1</code> still exists...</p>
<div class="codehilite"><pre><span></span>def pf (p : ℕ) := {e : ℤ// 0 ≤ e ∧ e &lt; p}

namespace pf

variables ( p: ℕ ) ( pp : prime p )
include pp

def mul (a b : pf p) : pf p := ⟨(a.val * b.val) % p,     begin apply mod_range, apply prime.pos pp end⟩
instance : has_mul (pf p) := ⟨@mul p pp⟩
protected def one  : pf p := ⟨1, begin apply and.intro, apply zero_le_one, apply (int.coe_nat_lt.elim_right (prime.gt_one pp)), end⟩
instance : has_one (pf p) := ⟨@pf.one p pp⟩

lemma pf_is_right_inv (a : pf p) : (a.1 &gt; 0) → a * (@pf.inv p pp a) = 1 :=
</pre></div>

#### [ Johan Commelin (Nov 08 2018 at 09:50)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Variable%20with%20braces%2C%20parentheses%20and%20%20square%20brackets/near/147285867):
<p>Ok, what happens if you do not include <code>pp</code>?</p>

#### [ Johan Commelin (Nov 08 2018 at 09:50)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Variable%20with%20braces%2C%20parentheses%20and%20%20square%20brackets/near/147285875):
<p>Just don't make any assumptions on <code>p</code>.</p>

#### [ Johan Commelin (Nov 08 2018 at 09:50)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Variable%20with%20braces%2C%20parentheses%20and%20%20square%20brackets/near/147285889):
<p>But, like Mario said, you are basically redefining <code>zmod n</code>.</p>

#### [ AHan (Nov 08 2018 at 09:53)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Variable%20with%20braces%2C%20parentheses%20and%20%20square%20brackets/near/147285989):
<p><span class="user-mention" data-user-id="110049">@Mario Carneiro</span>  Yeah <code>Z/pZ </code> exactly the thing I want<br>
Do you mean the <code>zmod</code> in <code>modeq</code> ? Isn't is some sort of equivalence class instead of some types like <code>int</code> or <code>nat</code> ?</p>

#### [ Johan Commelin (Nov 08 2018 at 09:54)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Variable%20with%20braces%2C%20parentheses%20and%20%20square%20brackets/near/147286042):
<p><a href="https://github.com/leanprover/mathlib/blob/dbb3ff0b5b2e42aa71d8167d7efdb3aa12d6e483/data/zmod/basic.lean#L10" target="_blank" title="https://github.com/leanprover/mathlib/blob/dbb3ff0b5b2e42aa71d8167d7efdb3aa12d6e483/data/zmod/basic.lean#L10">https://github.com/leanprover/mathlib/blob/dbb3ff0b5b2e42aa71d8167d7efdb3aa12d6e483/data/zmod/basic.lean#L10</a></p>

#### [ Johan Commelin (Nov 08 2018 at 09:54)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Variable%20with%20braces%2C%20parentheses%20and%20%20square%20brackets/near/147286049):
<p>It is really almost the same as what you did. The set of naturals between <code>0</code> and <code>n</code>.</p>

#### [ AHan (Nov 08 2018 at 09:57)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Variable%20with%20braces%2C%20parentheses%20and%20%20square%20brackets/near/147286167):
<p>If I don't include pp, since I have to prove the result of <code>mul</code> &lt; p, I will have to include something like <code>p_gt_zero</code>in the assumption</p>

#### [ AHan (Nov 08 2018 at 10:02)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Variable%20with%20braces%2C%20parentheses%20and%20%20square%20brackets/near/147286405):
<p>Oh!! Thank you very much! (Didn't notice this... as I can't find zmod via C-c C-d....)</p>

#### [ Johan Commelin (Nov 08 2018 at 10:34)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Variable%20with%20braces%2C%20parentheses%20and%20%20square%20brackets/near/147287978):
<p><span class="user-mention" data-user-id="133545">@AHan</span> Sure, that's right. You will notice that <code>zmod</code> uses <code>pnat</code>: positive natural numbers.</p>

#### [ AHan (Nov 08 2018 at 13:55)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Variable%20with%20braces%2C%20parentheses%20and%20%20square%20brackets/near/147296994):
<p>Yes, didn't even notice that there were <code>pnat</code>, this really helped a lot! Thank you!</p>


{% endraw %}
