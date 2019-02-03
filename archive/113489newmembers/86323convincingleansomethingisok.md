---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113489newmembers/86323convincingleansomethingisok.html
---

## Stream: [new members](https://leanprover-community.github.io/archive/113489newmembers/index.html)
### Topic: [convincing lean something is ok](https://leanprover-community.github.io/archive/113489newmembers/86323convincingleansomethingisok.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Ned Summers (Aug 20 2018 at 17:15)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/convincing%20lean%20something%20is%20ok/near/132461786):
<p>I'm trying to construct a function <code>f :  a → b</code> (as part of an instance of a structure) with two types a and b and non-trivially I have that for some type c defined differently in fact <code>b=c</code> (and I can prove that if needed).  </p>
<p>How can I let lean know that in fact, what might appear to be of type <code>a → c</code> (being given by <code>λ x , y</code>, for some <code>y : c</code>) is in fact totally fine and fulfils the requirement for being of type <code>a → b</code>?</p>

#### [ Simon Hudon (Aug 20 2018 at 17:18)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/convincing%20lean%20something%20is%20ok/near/132461983):
<p>One way do it is to use <code>cast</code>. It does get in the way when trying to reason about the function but it does what you said. You could do it as <code>cast (by subst c) f</code></p>

#### [ Simon Hudon (Aug 20 2018 at 17:21)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/convincing%20lean%20something%20is%20ok/near/132462161):
<p>I sometimes define local notations for this kind of cast: </p>
<div class="codehilite"><pre><span></span><span class="n">local</span> <span class="kn">prefix</span> <span class="bp">`</span><span class="err">♯</span><span class="bp">`</span><span class="o">:</span><span class="mi">0</span> <span class="o">:=</span> <span class="n">cast</span> <span class="o">(</span><span class="k">by</span> <span class="n">cc</span> <span class="bp">&lt;|&gt;</span> <span class="n">solve_by_elim</span><span class="o">)</span>
</pre></div>

#### [ Ned Summers (Aug 21 2018 at 11:48)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/convincing%20lean%20something%20is%20ok/near/132508506):
<p>Ah ok, thanks. I'm not familiar with using subst, how would I include a proof that b = c in this? Currently, I'm being told "subst tactic failed, given expression is not a local constant". Apologies, I am very much a beginning.</p>

#### [ Ned Summers (Aug 21 2018 at 12:21)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/convincing%20lean%20something%20is%20ok/near/132509682):
<p>Never mind, managed to get that sorted!</p>

#### [ Ned Summers (Aug 21 2018 at 12:39)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/convincing%20lean%20something%20is%20ok/near/132510322):
<p>I'm not sure if this is what you originally meant, Simon, but I ended up solving this with <code>λ x , cast( ... ) y</code>, using my proof in the brackets. However, if I also had properties previously expressed about y, how do I go about using these for the cast version?</p>
<p>For example (fairly close to what I'm doing), if y were in the center of a group, is it possible to prove that for some other member x, cast _ y * x = x * cast _ y? Or do we lose this information in casting?</p>

#### [ Kevin Buzzard (Aug 21 2018 at 15:31)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/convincing%20lean%20something%20is%20ok/near/132517275):
<p>Maybe you should take a look at <a href="https://leanprover.github.io/theorem_proving_in_lean/tactics.html#rewriting" target="_blank" title="https://leanprover.github.io/theorem_proving_in_lean/tactics.html#rewriting">https://leanprover.github.io/theorem_proving_in_lean/tactics.html#rewriting</a></p>


{% endraw %}
