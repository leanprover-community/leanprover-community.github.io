---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/66348natint.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [nat = int](https://leanprover-community.github.io/archive/113488general/66348natint.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Kenny Lau (Oct 09 2018 at 21:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nat%20%3D%20int/near/135492419):
<p>Is <code>nat = int</code> consistent with Lean?</p>

#### [ Mario Carneiro (Oct 09 2018 at 21:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nat%20%3D%20int/near/135492660):
<p>yes</p>

#### [ Mario Carneiro (Oct 09 2018 at 21:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nat%20%3D%20int/near/135492670):
<p>but it will make the VM not like you</p>

#### [ Kenny Lau (Oct 09 2018 at 21:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nat%20%3D%20int/near/135492671):
<p>good lord</p>

#### [ Kenny Lau (Oct 09 2018 at 21:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nat%20%3D%20int/near/135492701):
<p>so how can a constructor of an inductive type construct itself...</p>

#### [ Kevin Buzzard (Oct 09 2018 at 21:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nat%20%3D%20int/near/135492733):
<p>Equality of types is terrifying. I just stick to equality of terms.</p>

#### [ Mario Carneiro (Oct 09 2018 at 21:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nat%20%3D%20int/near/135492747):
<div class="codehilite"><pre><span></span>axiom nat_eq_int : nat = int

#eval cast nat_eq_int.symm (-5) -- 2147483643
</pre></div>

#### [ Kevin Buzzard (Oct 09 2018 at 21:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nat%20%3D%20int/near/135492754):
<p>I am not sure I have a good feeling as to what equality of types means.</p>

#### [ Kevin Buzzard (Oct 09 2018 at 21:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nat%20%3D%20int/near/135492774):
<p><code>equiv</code> of types -- that I understand.</p>

#### [ Mario Carneiro (Oct 09 2018 at 21:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nat%20%3D%20int/near/135492840):
<p>Unfortunately, as a cast off from HoTT, univalence is consistent in some weak forms</p>

#### [ Mario Carneiro (Oct 09 2018 at 21:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nat%20%3D%20int/near/135492856):
<p>but the VM assumes something much stricter, in order for type erasure to be sound</p>

#### [ Kevin Buzzard (Oct 09 2018 at 21:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nat%20%3D%20int/near/135493250):
<p>So an interesting thing happened in my lecture today. It was an interactive lecture and the students could vote on the questions I was asking, on their phones. And I asked them if "not P" was equal to "P implies false" and a lot of them said that these things were not equal.</p>

#### [ Patrick Massot (Oct 09 2018 at 21:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nat%20%3D%20int/near/135493310):
<p>I'm not surprised</p>

#### [ Chris Hughes (Oct 09 2018 at 21:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nat%20%3D%20int/near/135493313):
<p>Did you teach them the truth table definition of implies?</p>

#### [ Kevin Buzzard (Oct 09 2018 at 21:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nat%20%3D%20int/near/135493317):
<p>But they were all happy that these things were equivalent. I didn't tell them Lean's definition of "not P", I was doing basic propositional calculus, so the definition of "not" was "not false = true" and "not true = false" and that's it</p>

#### [ Patrick Massot (Oct 09 2018 at 21:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nat%20%3D%20int/near/135493324):
<p>Did you try on a room full of professional mathematicians next?</p>

#### [ Kevin Buzzard (Oct 09 2018 at 21:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nat%20%3D%20int/near/135493335):
<p>But this is somehow the same issue.</p>

#### [ Kevin Buzzard (Oct 09 2018 at 21:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nat%20%3D%20int/near/135493352):
<p>Two propositions can be equivalent, but it's a bit weird saying they are equal.</p>

#### [ Kevin Buzzard (Oct 09 2018 at 21:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nat%20%3D%20int/near/135493360):
<p>Especially when I told them that 2+2=4 and Fermat's Last Theorem were both true, and asked them if they thought that they were hence equal.</p>

#### [ Mario Carneiro (Oct 09 2018 at 21:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nat%20%3D%20int/near/135493365):
<p>aha, here's an example of a lie proposition from that axiom:</p>
<div class="codehilite"><pre><span></span>axiom nat_eq_int : nat = int
def lie : bool := cast nat_eq_int.symm (-int.of_nat (2^31)) &lt; 0
theorem not_lying : lie = ff := rfl
#eval lie -- tt
</pre></div>

#### [ Mario Carneiro (Oct 09 2018 at 21:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nat%20%3D%20int/near/135493376):
<p>This is bad because you can make the VM crash</p>

#### [ Kevin Buzzard (Oct 09 2018 at 21:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nat%20%3D%20int/near/135493426):
<p>That's not bad -- that just means that you shouldn't rely on the VM</p>

#### [ Kevin Buzzard (Oct 09 2018 at 21:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nat%20%3D%20int/near/135493428):
<p>If the kernel's happy, I'm happy</p>

#### [ Chris Hughes (Oct 09 2018 at 21:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nat%20%3D%20int/near/135493435):
<p>It means you shouldn't introduce axioms and then rely on the VM.</p>

#### [ Chris Hughes (Oct 09 2018 at 21:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nat%20%3D%20int/near/135493446):
<p>But you shouldn't introduce axioms and rely on the kernel either. So I don't think that's a problem.</p>

#### [ Mario Carneiro (Oct 09 2018 at 21:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nat%20%3D%20int/near/135493448):
<p>it means that some axioms are consistent with the VM and others aren't, even if they are consistent with lean itself</p>

#### [ Kevin Buzzard (Oct 09 2018 at 21:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nat%20%3D%20int/near/135493466):
<p>Mario do you _know_ that nat = int is consistent with Lean (assuming maths is consistent etc)</p>

#### [ Mario Carneiro (Oct 09 2018 at 21:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nat%20%3D%20int/near/135493513):
<p>I have strong evidence in the direction of a proof</p>

#### [ Kevin Buzzard (Oct 09 2018 at 21:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nat%20%3D%20int/near/135493517):
<p>Fair enough.</p>

#### [ Mario Carneiro (Oct 09 2018 at 21:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nat%20%3D%20int/near/135493521):
<p>the more general statement is that two types with the same cardinality are consistently equal</p>

#### [ Kevin Buzzard (Oct 09 2018 at 21:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nat%20%3D%20int/near/135493532):
<p>Aah I see equiv has popped up again</p>

#### [ Kenny Lau (Oct 09 2018 at 21:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nat%20%3D%20int/near/135493547):
<p>maybe we should add that as an axiom</p>

#### [ Kenny Lau (Oct 09 2018 at 21:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nat%20%3D%20int/near/135493553):
<p>just like how we added propext as an axiom</p>

#### [ Mario Carneiro (Oct 09 2018 at 21:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nat%20%3D%20int/near/135493557):
<p>But type erasure, used in the VM, assumes that the only provable equalities are between objects with the same runtime representation</p>

#### [ Kevin Buzzard (Oct 09 2018 at 21:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nat%20%3D%20int/near/135493564):
<p>Is <code>forall X Y : Type, equiv X Y iff X = Y</code> consistent with Lean?</p>

#### [ Mario Carneiro (Oct 09 2018 at 21:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nat%20%3D%20int/near/135493569):
<p>which has to do with the other thread</p>

#### [ Kenny Lau (Oct 09 2018 at 21:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nat%20%3D%20int/near/135493573):
<p><code>Type u</code> even</p>

#### [ Chris Hughes (Oct 09 2018 at 21:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nat%20%3D%20int/near/135493577):
<p>It doesn't type check</p>

#### [ Kevin Buzzard (Oct 09 2018 at 21:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nat%20%3D%20int/near/135493622):
<p>oh yeah</p>

#### [ Kenny Lau (Oct 09 2018 at 21:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nat%20%3D%20int/near/135493633):
<p>oh</p>

#### [ Kevin Buzzard (Oct 09 2018 at 21:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nat%20%3D%20int/near/135493636):
<p>nonempty (equiv X Y) iff X = Y or whatever</p>

#### [ Kenny Lau (Oct 09 2018 at 21:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nat%20%3D%20int/near/135493641):
<p>use <code>\to</code></p>

#### [ Mario Carneiro (Oct 09 2018 at 21:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nat%20%3D%20int/near/135493676):
<p>You have to be careful not to run afoul of the counterexample to HoTT</p>

#### [ Mario Carneiro (Oct 09 2018 at 21:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nat%20%3D%20int/near/135493788):
<p>Consider the <code>bnot : bool -&gt; bool</code> function, which swaps the two values. This is provably an equivalence in HoTT, so from univalence we get an equality <code>ua bnot : bool = bool</code>. It is provable in HoTT that <code>cast (ua bnot) tt = ff</code>, but <code>cast rfl tt = tt</code> and hence <code>ua bnot != rfl</code>, contradicting proof irrelevance</p>

#### [ Kenny Lau (Oct 09 2018 at 21:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nat%20%3D%20int/near/135493870):
<p>but you can't prove in lean that <code>cast (ua bnot) tt = ff</code> right</p>

#### [ Mario Carneiro (Oct 09 2018 at 21:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nat%20%3D%20int/near/135493930):
<p>In HoTT, this is provable because we know <code>ua</code> is the inverse of the natural function <code>A = B -&gt; A ~= B</code></p>

#### [ Kevin Buzzard (Oct 09 2018 at 21:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nat%20%3D%20int/near/135493990):
<p><span class="user-mention" data-user-id="110031">@Patrick Massot</span> this should sort out your <code>heq</code> problems:</p>
<div class="codehilite"><pre><span></span><span class="kn">import</span> <span class="n">data</span><span class="bp">.</span><span class="n">equiv</span><span class="bp">.</span><span class="n">basic</span>
<span class="kn">axiom</span> <span class="n">for_patrick</span> <span class="o">:</span> <span class="bp">∀</span> <span class="o">(</span><span class="n">X</span> <span class="n">Y</span> <span class="o">:</span> <span class="kt">Type</span><span class="bp">*</span><span class="o">),</span> <span class="n">equiv</span> <span class="n">X</span> <span class="n">Y</span> <span class="bp">→</span> <span class="n">X</span> <span class="bp">=</span> <span class="n">Y</span>
</pre></div>

#### [ Kevin Buzzard (Oct 09 2018 at 21:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nat%20%3D%20int/near/135493999):
<p>and apparently Mario thinks it's consistent, but just be careful with the VM OK?</p>

#### [ Mario Carneiro (Oct 09 2018 at 21:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nat%20%3D%20int/near/135494020):
<p>I strongly recommend against any axioms that don't obey type erasure</p>

#### [ Chris Hughes (Oct 09 2018 at 21:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nat%20%3D%20int/near/135494022):
<p>I don't think it helps. Patrick knows his Types are equal, he just can't <code>rw</code> using that equality.</p>

#### [ Patrick Massot (Oct 09 2018 at 21:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nat%20%3D%20int/near/135494056):
<p>We all want the same tactic: <code>rw_that_just_works</code></p>

#### [ Mario Carneiro (Oct 09 2018 at 21:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nat%20%3D%20int/near/135494119):
<p>this is a difficult research question</p>

#### [ Mario Carneiro (Oct 09 2018 at 21:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nat%20%3D%20int/near/135494128):
<p>the problem is always type dependency</p>

#### [ Kenny Lau (Oct 09 2018 at 21:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nat%20%3D%20int/near/135494130):
<p>What is type erasure?</p>

#### [ Kevin Buzzard (Oct 09 2018 at 21:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nat%20%3D%20int/near/135494140):
<blockquote>
<p>this is a difficult research question</p>
</blockquote>
<p>Mathematicians can do it in their heads!</p>

#### [ Patrick Massot (Oct 09 2018 at 21:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nat%20%3D%20int/near/135494184):
<p>Then do you have example where all those <code>subst</code> or <code>generalize</code> tricks works? I haven't been able to find any math example</p>

#### [ Kevin Buzzard (Oct 09 2018 at 21:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nat%20%3D%20int/near/135494327):
<p><a href="#narrow/stream/116395-maths/subject/Continuous.20Functions.20Preserve.20Limits/near/134675116" title="#narrow/stream/116395-maths/subject/Continuous.20Functions.20Preserve.20Limits/near/134675116">https://leanprover.zulipchat.com/#narrow/stream/116395-maths/subject/Continuous.20Functions.20Preserve.20Limits/near/134675116</a></p>

#### [ Kevin Buzzard (Oct 09 2018 at 21:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nat%20%3D%20int/near/135494366):
<p>Rohan wanted to prove that if <span class="katex"><span class="katex-mathml"><math><semantics><mrow><msub><mi>x</mi><mn>0</mn></msub><mo separator="true">,</mo><msub><mi>x</mi><mn>1</mn></msub><mo separator="true">,</mo><msub><mi>x</mi><mn>2</mn></msub><mi mathvariant="normal">.</mi><mi mathvariant="normal">.</mi><mi mathvariant="normal">.</mi></mrow><annotation encoding="application/x-tex">x_0,x_1,x_2...</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.43056em;"></span><span class="strut bottom" style="height:0.625em;vertical-align:-0.19444em;"></span><span class="base"><span class="mord"><span class="mord mathit">x</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.30110799999999993em;"><span style="top:-2.5500000000000003em;margin-left:0em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mathrm mtight">0</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.15em;"></span></span></span></span></span><span class="mpunct">,</span><span class="mord"><span class="mord mathit">x</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.30110799999999993em;"><span style="top:-2.5500000000000003em;margin-left:0em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mathrm mtight">1</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.15em;"></span></span></span></span></span><span class="mpunct">,</span><span class="mord"><span class="mord mathit">x</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.30110799999999993em;"><span style="top:-2.5500000000000003em;margin-left:0em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mathrm mtight">2</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.15em;"></span></span></span></span></span><span class="mord mathrm">.</span><span class="mord mathrm">.</span><span class="mord mathrm">.</span></span></span></span> tended to <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>x</mi></mrow><annotation encoding="application/x-tex">x</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.43056em;"></span><span class="strut bottom" style="height:0.43056em;vertical-align:0em;"></span><span class="base"><span class="mord mathit">x</span></span></span></span> then <span class="katex"><span class="katex-mathml"><math><semantics><mrow><msub><mi>x</mi><mn>1</mn></msub><mo separator="true">,</mo><msub><mi>x</mi><mn>2</mn></msub><mo separator="true">,</mo><msub><mi>x</mi><mn>3</mn></msub><mo separator="true">,</mo><mi mathvariant="normal">.</mi><mi mathvariant="normal">.</mi><mi mathvariant="normal">.</mi></mrow><annotation encoding="application/x-tex">x_1,x_2,x_3,...</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.43056em;"></span><span class="strut bottom" style="height:0.625em;vertical-align:-0.19444em;"></span><span class="base"><span class="mord"><span class="mord mathit">x</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.30110799999999993em;"><span style="top:-2.5500000000000003em;margin-left:0em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mathrm mtight">1</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.15em;"></span></span></span></span></span><span class="mpunct">,</span><span class="mord"><span class="mord mathit">x</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.30110799999999993em;"><span style="top:-2.5500000000000003em;margin-left:0em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mathrm mtight">2</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.15em;"></span></span></span></span></span><span class="mpunct">,</span><span class="mord"><span class="mord mathit">x</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.30110799999999993em;"><span style="top:-2.5500000000000003em;margin-left:0em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mathrm mtight">3</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.15em;"></span></span></span></span></span><span class="mpunct">,</span><span class="mord mathrm">.</span><span class="mord mathrm">.</span><span class="mord mathrm">.</span></span></span></span> also tended to <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>x</mi></mrow><annotation encoding="application/x-tex">x</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.43056em;"></span><span class="strut bottom" style="height:0.43056em;vertical-align:0em;"></span><span class="base"><span class="mord mathit">x</span></span></span></span>. We formalised the change of variables using filters and then Kenny proved it using <code>subst</code></p>

#### [ Mario Carneiro (Oct 09 2018 at 22:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nat%20%3D%20int/near/135494504):
<p>the solution of course is extensional type theory but I might be contractually obligated to say that's silly</p>

#### [ Andrew Ashworth (Oct 09 2018 at 22:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nat%20%3D%20int/near/135494641):
<p>was OTT (<a href="https://github.com/leanprover/lean/issues/654" target="_blank" title="https://github.com/leanprover/lean/issues/654">https://github.com/leanprover/lean/issues/654</a>) no good?</p>

#### [ Chris Hughes (Oct 09 2018 at 22:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nat%20%3D%20int/near/135494975):
<p>One thing I've wondered for a while is why does this work?</p>
<div class="codehilite"><pre><span></span><span class="kn">example</span> <span class="o">:</span> <span class="o">(</span><span class="mi">0</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">)</span> <span class="bp">=</span> <span class="n">eq</span><span class="bp">.</span><span class="n">rec</span> <span class="mi">0</span> <span class="o">(</span><span class="n">classical</span><span class="bp">.</span><span class="n">choice</span> <span class="bp">⟨</span><span class="n">eq</span><span class="bp">.</span><span class="n">refl</span> <span class="bp">ℕ⟩</span><span class="o">)</span> <span class="o">:=</span> <span class="n">rfl</span>
</pre></div>

#### [ Mario Carneiro (Oct 09 2018 at 22:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nat%20%3D%20int/near/135495482):
<p>there is a kernel reduction rule <code>eq.rec e h ~&gt; e</code> when <code>h : a = a</code>. Intuitively this is justified by using proof irrelevance to replace <code>h</code> with <code>rfl</code> and then iota reducing</p>

#### [ Kevin Buzzard (Oct 09 2018 at 22:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nat%20%3D%20int/near/135495777):
<p>Chris it looks like it's about time you learn C++</p>

#### [ Mario Carneiro (Oct 09 2018 at 22:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nat%20%3D%20int/near/135495803):
<p>or type theory</p>

#### [ Patrick Massot (Oct 09 2018 at 22:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nat%20%3D%20int/near/135496147):
<p>Kevin means learning type theory by reading C++ code of the Lean kernel</p>

#### [ Patrick Massot (Oct 09 2018 at 22:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nat%20%3D%20int/near/135496158):
<p>That's the proper way for brave men</p>

#### [ Mario Carneiro (Oct 09 2018 at 22:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nat%20%3D%20int/near/135496744):
<p>I should note that I have written a paper on this topic and I still haven't fully understood the kernel of lean</p>

#### [ Mario Carneiro (Oct 09 2018 at 22:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nat%20%3D%20int/near/135496776):
<p>it is much easier to read the reference typecheckers like trepplein</p>


{% endraw %}
