---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/16816Uselistasanargument.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [Use list as an argument](https://leanprover-community.github.io/archive/113488general/16816Uselistasanargument.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Blair Shi (Jul 11 2018 at 10:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Use%20list%20as%20an%20argument/near/129458509):
<p>I define a function which takes a list as a argument but I do not know why it always break when I use it in my other theorem or function.<br>
my function no error:</p>
<div class="codehilite"><pre><span></span>def f_span (l : list V) : set V :=
span {vc : V | vc ∈ l}
</pre></div>


<p>use it later in</p>
<div class="codehilite"><pre><span></span>def are_basis_equal (l₀ : list V) (l₁ : list V) : Prop :=
∀vc : V, vc ∈ (f_span l₀) ∧ vc ∈ (f_span l₁)
</pre></div>


<p>it reports error :</p>
<div class="codehilite"><pre><span></span>[Lean]
type mismatch at application
  f_span l₀
term
  l₀
has type
  list V : Type v
but is expected to have type
  Type ? : Type (?+1)
</pre></div>

#### [ Kevin Buzzard (Jul 11 2018 at 10:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Use%20list%20as%20an%20argument/near/129458841):
<p>You have some variable <code>V</code> somewhere, I guess?</p>

#### [ Kevin Buzzard (Jul 11 2018 at 10:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Use%20list%20as%20an%20argument/near/129458858):
<p>If you look at what you wrote as the definition of <code>f_span</code> then it <em>looks</em> like it is expecting one input, namely <code>l</code> of type <code>list V</code></p>

#### [ Kevin Buzzard (Jul 11 2018 at 10:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Use%20list%20as%20an%20argument/near/129458871):
<p>But after the definition of <code>f_span</code>, if you write <code>#check f_span</code> you will probably see a different story!</p>

#### [ Kevin Buzzard (Jul 11 2018 at 10:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Use%20list%20as%20an%20argument/near/129458902):
<p>Probably <code>f_span</code> is also expecting you to input <code>V</code> itself. So that's my guess as to what your error is caused by -- you need <code>f_span V l_0</code></p>

#### [ Kevin Buzzard (Jul 11 2018 at 10:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Use%20list%20as%20an%20argument/near/129458955):
<p>The trick is to make <code>V</code> a <code>{}</code> variable; then <code>f_span</code> won't ask for it. I've got to run but that's the idea</p>

#### [ Sean Leather (Jul 11 2018 at 10:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Use%20list%20as%20an%20argument/near/129459298):
<blockquote>
<p>But after the definition of <code>f_span</code>, if you write <code>#check f_span</code> you will probably see a different story!</p>
</blockquote>
<p>Even better would be to write <code>#check @f_span</code>. That fills in those pesky metavariables with something readable.</p>

#### [ Blair Shi (Jul 11 2018 at 11:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Use%20list%20as%20an%20argument/near/129459870):
<p>I added more argument using <code>[]</code> and it works now. thank you !</p>

#### [ Sean Leather (Jul 11 2018 at 11:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Use%20list%20as%20an%20argument/near/129460007):
<p><span class="user-mention" data-user-id="119876">@Blair Shi</span> Can you show us what it looks like now?</p>

#### [ Blair Shi (Jul 11 2018 at 11:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Use%20list%20as%20an%20argument/near/129460651):
<div class="codehilite"><pre><span></span>def f_span (l : list V) : set V :=
span {vc : V | vc ∈ l}
def are_basis_equal (l₀ : list V) (l₁ : list V) : Prop :=
∀vc : V, vc ∈ (f_span k V l₀) ∧ vc ∈ (f_span k V l₁)
</pre></div>


<p>I just added k V everywhere when I using the function <code>f_span</code> without any change of <code>f_span</code> </p>
<p>Because if you check my <code>f_span</code>, the type is</p>
<div class="codehilite"><pre><span></span>f_span :
  Π (k : Type u_1) (V : Type u_2) [_inst_1 : field k] [_inst_2 : ring k] [_inst_3 : module k V], list V → set V
</pre></div>


<p>I also tried like added <code>(k : Type u_1) (V : Type u_2) [_inst_1 : field k] [_inst_2 : ring k] [_inst_3 : module k V]</code> all of them as arguments to my <code>f_span</code> but I realized I don't need to do so. But adding arguments also works for me.</p>

#### [ Patrick Massot (Jul 11 2018 at 11:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Use%20list%20as%20an%20argument/near/129460809):
<p>Are you sure you're not duplicating stuff around <a href="https://github.com/leanprover/mathlib/blob/master/linear_algebra/basic.lean#L122" target="_blank" title="https://github.com/leanprover/mathlib/blob/master/linear_algebra/basic.lean#L122">https://github.com/leanprover/mathlib/blob/master/linear_algebra/basic.lean#L122</a>?</p>

#### [ Blair Shi (Jul 11 2018 at 11:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Use%20list%20as%20an%20argument/near/129461143):
<p><span class="user-mention" data-user-id="110031">@Patrick Massot</span>  because the vector space in mathlib does not support finite dimensional vector space. I am currently working on finite dimensional vector space and in the definition of finite dimensional vector space, the basis is a list.</p>

#### [ Blair Shi (Jul 11 2018 at 11:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Use%20list%20as%20an%20argument/near/129461329):
<p><span class="user-mention" data-user-id="110045">@Sean Leather</span> <br>
I realized I have wrote the global variables and if I delete them the code does not work</p>
<div class="codehilite"><pre><span></span>variables (k : Type u) (V : Type v)
variable [field k]
variables [ring k] [module k V]
variables (a : k) (b : V)
include k
</pre></div>

#### [ Patrick Massot (Jul 11 2018 at 12:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Use%20list%20as%20an%20argument/near/129461449):
<p>Ok. I remember we had this discussion about ordering basis elements here.</p>

#### [ Mario Carneiro (Jul 11 2018 at 12:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Use%20list%20as%20an%20argument/near/129461828):
<p>You want <code>variables {k : Type u} {V : Type v}</code> in the first line</p>

#### [ Blair Shi (Jul 11 2018 at 12:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Use%20list%20as%20an%20argument/near/129462340):
<p>I change it to be <code>{k : Type u} {V : Type v}</code>as you said. Now I delete all <code>k V</code> when I use the function:)</p>

#### [ Kevin Buzzard (Jul 11 2018 at 12:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Use%20list%20as%20an%20argument/near/129462359):
<p>ordering basis elements -- it's a funny situation! In the general case you seem to want a basis to be a set. But to prove the standard undergraduate theorems about linear maps = matrices you seem to want the basis to be a finite totally ordered set.</p>

#### [ Kevin Buzzard (Jul 11 2018 at 12:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Use%20list%20as%20an%20argument/near/129462488):
<p><span class="user-mention" data-user-id="119876">@Blair Shi</span> yes -- if you are doing vector spaces over a field field <code>k</code> then you don't want to have to keep mentioning <code>k</code>. If you're doing <code>k</code>-linear maps between vector spaces <code>V</code> and <code>W</code> then you probably want to mention <code>V</code> but if you're doing things with a fixed <code>V</code> like showing that sets of size less than dim(V) can't span then you might not even want to mention <code>V</code>. This is how those <code>{}</code> and <code>()</code> brackets that I talked about in my lecture on Monday work in practice. There are tricks to change the variable from <code>()</code> to <code>{}</code>and back in the middle of a file which I can tell you about later if you need them.</p>


{% endraw %}
