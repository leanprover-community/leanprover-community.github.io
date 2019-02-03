---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/89956quotindinmetatheorypaper.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [quot.ind in metatheory paper](https://leanprover-community.github.io/archive/113488general/89956quotindinmetatheorypaper.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Floris van Doorn (Oct 29 2018 at 17:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quot.ind%20in%20metatheory%20paper/near/136716513):
<p>In Section 2.7 of Mario's metatheory of Lean paper, I'm missing the fact that <code>quot.ind</code> is a axiom in Lean. Is this an omission, or is there an implicit claim here that <code>quot.ind</code> is derivable from the other constants/axioms?</p>

#### [ Gabriel Ebner (Oct 29 2018 at 17:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quot.ind%20in%20metatheory%20paper/near/136717438):
<p>I'm pretty sure that <code>quot.ind</code> is only derivable if the underlying type α is empty.</p>

#### [ Floris van Doorn (Oct 29 2018 at 17:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quot.ind%20in%20metatheory%20paper/near/136718421):
<p>That is too strong. You can at least prove it for <code>unit</code> by using that <code>x = unit.star</code> for every <code>x : unit</code> (and therefore <code>quot.mk x = quot.mk unit.star</code>). And I suspect that (classically) you might be able to do something when <code>α</code> is <code>fin n</code>, for example.</p>

#### [ Floris van Doorn (Oct 29 2018 at 17:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quot.ind%20in%20metatheory%20paper/near/136718605):
<p>oh wait, maybe I'm mentally already using <code>quot.ind</code>here.</p>

#### [ Floris van Doorn (Oct 29 2018 at 17:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quot.ind%20in%20metatheory%20paper/near/136718915):
<p>Oh yes, you're right. If <code>α</code> is nonempty, say <code>z : α</code>, and <code>r : α -&gt; α -&gt; Prop</code> then I can define </p>
<div class="codehilite"><pre><span></span>quot&#39; α r := option (quot α r)
quot&#39;.mk r x := some (quot.mk r x)
quot&#39;.lift β f h (some x) := quot.lift β f h x
quot&#39;.lift β f h none := f z
</pre></div>


<p>and then <code>quot'</code> satisfies the same rules as <code>quot</code>, including the reduction rule, but excluding <code>quot.ind</code></p>

#### [ Floris van Doorn (Oct 29 2018 at 18:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quot.ind%20in%20metatheory%20paper/near/136720482):
<p>Also, the paper claims/proves that using only the inductive types <code>empty psigma psum ulift nonempty W eq acc</code> we can construct all others. If we remove <code>acc</code> from this list, so we only have the other 7 inductive types, do we know whether the ("ideal") definitional equality in the resulting system decidable?</p>

#### [ Mario Carneiro (Oct 29 2018 at 21:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quot.ind%20in%20metatheory%20paper/near/136733168):
<p><span class="user-mention" data-user-id="111080">@Floris van Doorn</span> The reasoning behind only considering <code>quot.sound</code> an axiom and ignoring the others is that the others taken together are conservative, because we can take <code>quot A = A</code> and then all the axioms are valid except <code>quot.sound</code>. <code>quot.ind</code> is valid because <code>id</code> is surjective</p>

#### [ Mario Carneiro (Oct 29 2018 at 21:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quot.ind%20in%20metatheory%20paper/near/136733213):
<p>That said, I don't think this is common practice in logic, I should probably just call them all axioms</p>

#### [ Mario Carneiro (Oct 29 2018 at 21:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quot.ind%20in%20metatheory%20paper/near/136733320):
<p>I don't know if removing <code>acc</code> makes defeq decidable, but my guess is yes. Of course the counterexample in the paper uses <code>acc</code> essentially</p>

#### [ Floris van Doorn (Oct 29 2018 at 22:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quot.ind%20in%20metatheory%20paper/near/136736293):
<p><span class="user-mention" data-user-id="110049">@Mario Carneiro</span> I don't care about which of them you call constants and which you call axioms, my point is that you forgot to mention <code>quot.ind</code> in the paper (in the latest release and on the master branch). You only mention <code>quot.lift</code> as elimination principle.</p>

#### [ Mario Carneiro (Oct 29 2018 at 22:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quot.ind%20in%20metatheory%20paper/near/136736324):
<p>Now I forget if <code>quot.rec</code> or <code>quot.lift</code> + <code>quot.ind</code> were used internally by lean</p>

#### [ Floris van Doorn (Oct 29 2018 at 22:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quot.ind%20in%20metatheory%20paper/near/136736397):
<p><code>quot.rec</code> is defined in terms of <code>quot.lift</code> + <code>quot.ind</code>.</p>

#### [ Mario Carneiro (Oct 29 2018 at 22:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quot.ind%20in%20metatheory%20paper/near/136736414):
<p>ok, I'll update the paper</p>

#### [ Floris van Doorn (Oct 29 2018 at 22:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quot.ind%20in%20metatheory%20paper/near/136736688):
<p>The issue with the nontransitivity of algorithmic definitional equality using <code>quot</code> is only because if <code>α : Sort u</code> then <code>@quot α r : Sort u</code>, right? If we alternatively defined <code>@quot α r</code> to be in <code>Sort (max u 1)</code> (which would make more sense, compared to inductive types), then the nontransitivity using quotients goes away, right?</p>

#### [ Floris van Doorn (Oct 29 2018 at 22:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quot.ind%20in%20metatheory%20paper/near/136736701):
<p>thanks!</p>

#### [ Mario Carneiro (Oct 29 2018 at 22:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quot.ind%20in%20metatheory%20paper/near/136736801):
<p>yes</p>

#### [ Mario Carneiro (Oct 29 2018 at 22:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quot.ind%20in%20metatheory%20paper/near/136737064):
<p>All of the known examples of failure of transitivity involve some kind of subsingleton elimination, where an inductive type in Prop recurses over Type. So it is reasonable to conjecture that without <code>acc</code> and with <code>quot</code> out of <code>Prop</code> the algorithmic equality becomes transitive, and so coincides with ideal defeq which becomes decidable.</p>


{% endraw %}
