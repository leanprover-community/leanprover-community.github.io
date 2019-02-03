---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/144837PRreviews/58383495multiplicity.html
---

## Stream: [PR reviews](https://leanprover-community.github.io/archive/144837PRreviews/index.html)
### Topic: [#495 multiplicity](https://leanprover-community.github.io/archive/144837PRreviews/58383495multiplicity.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Chris Hughes (Nov 29 2018 at 20:18)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23495%20multiplicity/near/148810765):
<p><code>multiplicity</code> requires a decidable dvd argument currently. However there are applications where we don't have decidable dvd in general but we do for particular elements, in particular, for multiplicities of roots of polynomials over a comm ring, it is decidable whether or not <code>X - C a</code> divides a polynomial but not easily in general - the divisor needs to be monic. What's the best way of dealing with this?</p>

#### [ Johan Commelin (Nov 30 2018 at 12:18)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23495%20multiplicity/near/148855628):
<p>This is probably a noobie question, but why is it decidable whether <code>(X - C a)</code> divides some polynomial? Are you assuming that <code>a</code> comes from a ring with decidable eq?<br>
Anyway, I would personally just ignore the problem. If some lemma doesn't work in generality without decidability, just assume it as an argument.</p>

#### [ Chris Hughes (Nov 30 2018 at 12:19)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23495%20multiplicity/near/148855644):
<p>I am assuming decidable equality</p>

#### [ Kevin Buzzard (Nov 30 2018 at 12:19)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23495%20multiplicity/near/148855656):
<p>I guess they're equivalent, because <code>a = b</code> iff <code>X - C a</code> divides <code>X - C b</code></p>

#### [ Johan Commelin (Nov 30 2018 at 12:22)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23495%20multiplicity/near/148855790):
<blockquote>
<p>I am assuming decidable equality</p>
</blockquote>
<p>So then, what is the problem?</p>

#### [ Johan Commelin (Nov 30 2018 at 12:22)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23495%20multiplicity/near/148855802):
<p>Aaah, wait.... This is of course not the same as being classical.</p>

#### [ Chris Hughes (Nov 30 2018 at 12:23)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23495%20multiplicity/near/148855811):
<p>That divisibility of polynomials is not decidable in general even with decidable equality</p>

#### [ Johan Commelin (Nov 30 2018 at 12:23)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23495%20multiplicity/near/148855813):
<p>I should stop thinking about this stuff. I've got enough "real-math" problems <span class="emoji emoji-1f923" title="rolling on the floor laughing">:rolling_on_the_floor_laughing:</span></p>

#### [ Mario Carneiro (Nov 30 2018 at 12:23)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23495%20multiplicity/near/148855816):
<p>is that true? it's not clear to me</p>

#### [ Johan Commelin (Nov 30 2018 at 12:24)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23495%20multiplicity/near/148855866):
<p>What? That I have enough problems? <span class="emoji emoji-1f643" title="upside down">:upside_down:</span> <span class="emoji emoji-1f601" title="grinning face with smiling eyes">:grinning_face_with_smiling_eyes:</span>  I do</p>

#### [ Mario Carneiro (Nov 30 2018 at 12:24)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23495%20multiplicity/near/148855876):
<p>divisibility by <code>X - C a</code> is decidable because it's true iff the polynomial is zero when evaluated at <code>a</code></p>

#### [ Mario Carneiro (Nov 30 2018 at 12:24)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23495%20multiplicity/near/148855896):
<p>but I could imagine a more complicated polynomial factoring algorithm that decides divisibility</p>

#### [ Chris Hughes (Nov 30 2018 at 12:25)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23495%20multiplicity/near/148855921):
<p>You'd need decidable divisibility over the base ring at least</p>

#### [ Chris Hughes (Nov 30 2018 at 12:25)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23495%20multiplicity/near/148855932):
<p>Divisbility by monic polynomials is easily decidable the way I have it set up.</p>

#### [ Chris Hughes (Nov 30 2018 at 12:31)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23495%20multiplicity/near/148856160):
<p>Over a semiring you'd also need decidable additive divisibility.</p>

#### [ Kevin Buzzard (Nov 30 2018 at 13:03)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23495%20multiplicity/near/148857274):
<blockquote>
<p>Over a semiring you'd also need decidable additive divisibility.</p>
</blockquote>
<p>You mean decidable addibility?</p>

#### [ Kenny Lau (Nov 30 2018 at 13:03)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23495%20multiplicity/near/148857281):
<p>he means that this needs to be decidable: whether there is c with a+c=b</p>

#### [ Chris Hughes (Nov 30 2018 at 13:04)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23495%20multiplicity/near/148857325):
<p>I think the name consistent with convention is probably decidable subtractibility.</p>

#### [ Kevin Buzzard (Nov 30 2018 at 13:05)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23495%20multiplicity/near/148857344):
<p>You remove axioms and this is what you get :-)</p>

#### [ Mario Carneiro (Nov 30 2018 at 13:06)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23495%20multiplicity/near/148857403):
<p>maybe it is possible to work in the splitting field of the ring, and check if the roots match up there</p>

#### [ Mario Carneiro (Nov 30 2018 at 13:07)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23495%20multiplicity/near/148857445):
<p>I guess it should be decidable by some analogue of algebraic numbers, although strange ideal quotients may make things harder than in Q</p>

#### [ Chris Hughes (Nov 30 2018 at 13:24)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23495%20multiplicity/near/148858045):
<p>The splitting field won't have decidable equality though.</p>

#### [ Kevin Buzzard (Dec 01 2018 at 12:01)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23495%20multiplicity/near/150679435):
<blockquote>
<p>but I could imagine a more complicated polynomial factoring algorithm that decides divisibility</p>
</blockquote>
<p>Factoring is thorny over a general ring. For example <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mo>(</mo><mi>x</mi><mo>+</mo><mn>1</mn><mo>)</mo><mo>(</mo><mi>x</mi><mo>−</mo><mn>1</mn><mo>)</mo></mrow><annotation encoding="application/x-tex">(x+1)(x-1)</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.75em;"></span><span class="strut bottom" style="height:1em;vertical-align:-0.25em;"></span><span class="base"><span class="mopen">(</span><span class="mord mathit">x</span><span class="mbin">+</span><span class="mord mathrm">1</span><span class="mclose">)</span><span class="mopen">(</span><span class="mord mathit">x</span><span class="mbin">−</span><span class="mord mathrm">1</span><span class="mclose">)</span></span></span></span> and <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mo>(</mo><mi>x</mi><mo>+</mo><mn>3</mn><mo>)</mo><mo>(</mo><mi>x</mi><mo>−</mo><mn>3</mn><mo>)</mo></mrow><annotation encoding="application/x-tex">(x+3)(x-3)</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.75em;"></span><span class="strut bottom" style="height:1em;vertical-align:-0.25em;"></span><span class="base"><span class="mopen">(</span><span class="mord mathit">x</span><span class="mbin">+</span><span class="mord mathrm">3</span><span class="mclose">)</span><span class="mopen">(</span><span class="mord mathit">x</span><span class="mbin">−</span><span class="mord mathrm">3</span><span class="mclose">)</span></span></span></span> are both equal to <span class="katex"><span class="katex-mathml"><math><semantics><mrow><msup><mi>x</mi><mn>2</mn></msup><mo>−</mo><mn>1</mn></mrow><annotation encoding="application/x-tex">x^2-1</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.8141079999999999em;"></span><span class="strut bottom" style="height:0.897438em;vertical-align:-0.08333em;"></span><span class="base"><span class="mord"><span class="mord mathit">x</span><span class="msupsub"><span class="vlist-t"><span class="vlist-r"><span class="vlist" style="height:0.8141079999999999em;"><span style="top:-3.063em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mathrm mtight">2</span></span></span></span></span></span></span></span><span class="mbin">−</span><span class="mord mathrm">1</span></span></span></span> over <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mrow><mi mathvariant="double-struck">Z</mi></mrow><mi mathvariant="normal">/</mi><mn>8</mn><mrow><mi mathvariant="double-struck">Z</mi></mrow></mrow><annotation encoding="application/x-tex">\mathbb{Z}/8\mathbb{Z}</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.75em;"></span><span class="strut bottom" style="height:1em;vertical-align:-0.25em;"></span><span class="base"><span class="mord"><span class="mord mathbb">Z</span></span><span class="mord mathrm">/</span><span class="mord mathrm">8</span><span class="mord"><span class="mord mathbb">Z</span></span></span></span></span>. It's a bit terrifying -- again over <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mrow><mi mathvariant="double-struck">Z</mi></mrow><mi mathvariant="normal">/</mi><mn>8</mn><mrow><mi mathvariant="double-struck">Z</mi></mrow></mrow><annotation encoding="application/x-tex">\mathbb{Z}/8\mathbb{Z}</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.75em;"></span><span class="strut bottom" style="height:1em;vertical-align:-0.25em;"></span><span class="base"><span class="mord"><span class="mord mathbb">Z</span></span><span class="mord mathrm">/</span><span class="mord mathrm">8</span><span class="mord"><span class="mord mathbb">Z</span></span></span></span></span>, <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mn>4</mn><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mi>x</mi></mrow><annotation encoding="application/x-tex">4x^2+x</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.8141079999999999em;"></span><span class="strut bottom" style="height:0.897438em;vertical-align:-0.08333em;"></span><span class="base"><span class="mord mathrm">4</span><span class="mord"><span class="mord mathit">x</span><span class="msupsub"><span class="vlist-t"><span class="vlist-r"><span class="vlist" style="height:0.8141079999999999em;"><span style="top:-3.063em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mathrm mtight">2</span></span></span></span></span></span></span></span><span class="mbin">+</span><span class="mord mathit">x</span></span></span></span> divides <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mn>2</mn><msup><mi>x</mi><mn>2</mn></msup></mrow><annotation encoding="application/x-tex">2x^2</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.8141079999999999em;"></span><span class="strut bottom" style="height:0.8141079999999999em;vertical-align:0em;"></span><span class="base"><span class="mord mathrm">2</span><span class="mord"><span class="mord mathit">x</span><span class="msupsub"><span class="vlist-t"><span class="vlist-r"><span class="vlist" style="height:0.8141079999999999em;"><span style="top:-3.063em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mathrm mtight">2</span></span></span></span></span></span></span></span></span></span></span> even though 4 doesn't divide 2.</p>

#### [ Johan Commelin (Dec 17 2018 at 15:06)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23495%20multiplicity/near/152029219):
<p><span class="user-mention" data-user-id="110044">@Chris Hughes</span> Would it be possible to split this PR into smaller pieces? For example: 1 PR that adds <code>enat</code>; 1 PR that makes lots of little changes in several files; 1 PR that adds the notion <code>multiplicity</code>; and finally 1 PR that replaces <code>padic_val</code> with <code>multiplicity</code>.</p>


{% endraw %}
