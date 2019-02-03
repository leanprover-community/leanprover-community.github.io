---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/67662notationgimmick.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [notation gimmick](https://leanprover-community.github.io/archive/113488general/67662notationgimmick.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Kevin Buzzard (Jun 02 2018 at 03:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notation%20gimmick/near/127447537):
<p>If I have a family of rings <code>{gamma : Type} (R : gamma -&gt; Type) [forall i, ring (R i)]</code></p>

#### [ Kevin Buzzard (Jun 02 2018 at 03:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notation%20gimmick/near/127447541):
<p>For a mathematician it would look clearer if I could write <code>forall i, ring R_i</code></p>

#### [ Kevin Buzzard (Jun 02 2018 at 03:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notation%20gimmick/near/127447585):
<p>can i make R an instance of some notation typeclass or use some other notation gimmick to do this?</p>

#### [ Kenny Lau (Jun 02 2018 at 03:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notation%20gimmick/near/127447591):
<p>madness</p>

#### [ Kevin Buzzard (Jun 02 2018 at 03:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notation%20gimmick/near/127447595):
<p>you're such a pessimist</p>

#### [ Kevin Buzzard (Jun 02 2018 at 03:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notation%20gimmick/near/127447597):
<p>just because it could be another valid variable name</p>

#### [ Kevin Buzzard (Jun 02 2018 at 03:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notation%20gimmick/near/127447606):
<p>what about some weird unicode underline that's not valid</p>

#### [ Mario Carneiro (Jun 02 2018 at 03:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notation%20gimmick/near/127447664):
<p>This was a proposal on core lean a while back</p>

#### [ Simon Hudon (Jun 02 2018 at 03:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notation%20gimmick/near/127447665):
<p>That's a terrible idea.</p>

#### [ Mario Carneiro (Jun 02 2018 at 03:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notation%20gimmick/near/127447666):
<p>oh wait I misunderstood</p>

#### [ Mario Carneiro (Jun 02 2018 at 03:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notation%20gimmick/near/127447670):
<p>I thought you wanted to avoid the <code>gamma</code> and <code>R</code> decls</p>

#### [ Kevin Buzzard (Jun 02 2018 at 03:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notation%20gimmick/near/127447712):
<p>it's the underscore I want</p>

#### [ Kevin Buzzard (Jun 02 2018 at 03:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notation%20gimmick/near/127447715):
<p>sorry</p>

#### [ Mario Carneiro (Jun 02 2018 at 03:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notation%20gimmick/near/127447716):
<p><code>R_i</code> parsed as nonatomic is a terrible idea, underscores are used <em>gratuitously</em> in lean as spaces that don't break the identifier</p>

#### [ Kevin Buzzard (Jun 02 2018 at 03:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notation%20gimmick/near/127447718):
<p>We would always talk about a family <span class="katex"><span class="katex-mathml"><math><semantics><mrow><msub><mi>R</mi><mi>i</mi></msub></mrow><annotation encoding="application/x-tex">R_i</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.68333em;"></span><span class="strut bottom" style="height:0.83333em;vertical-align:-0.15em;"></span><span class="base"><span class="mord"><span class="mord mathit" style="margin-right:0.00773em;">R</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.31166399999999994em;"><span style="top:-2.5500000000000003em;margin-left:-0.00773em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mathit mtight">i</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.15em;"></span></span></span></span></span></span></span></span> of rings</p>

#### [ Kevin Buzzard (Jun 02 2018 at 03:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notation%20gimmick/near/127447722):
<p>how about subscript i?</p>

#### [ Mario Carneiro (Jun 02 2018 at 03:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notation%20gimmick/near/127447728):
<p>That's actually been discussed before too</p>

#### [ Kevin Buzzard (Jun 02 2018 at 03:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notation%20gimmick/near/127447730):
<p>proper subscript would be brilliant</p>

#### [ Mario Carneiro (Jun 02 2018 at 03:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notation%20gimmick/near/127447731):
<p>Did you know there is a subscript for every letter except q?</p>

#### [ Kevin Buzzard (Jun 02 2018 at 03:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notation%20gimmick/near/127447734):
<p>sometimes I know that</p>

#### [ Kevin Buzzard (Jun 02 2018 at 03:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notation%20gimmick/near/127447776):
<p>I have been browsing that file</p>

#### [ Kevin Buzzard (Jun 02 2018 at 03:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notation%20gimmick/near/127447778):
<p>I was looking for cool curly sheaf notation :-)</p>

#### [ Mario Carneiro (Jun 02 2018 at 03:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notation%20gimmick/near/127447796):
<p>Anyway I suggest you don't try too hard to perfectly replicate all the inconsistencies in math notation</p>

#### [ Simon Hudon (Jun 02 2018 at 03:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notation%20gimmick/near/127447893):
<p>As an additional note, I believe an identifier followed by a subscript (like <code>fooₐ</code>) is treated as one big identifier, not as <code>foo</code> followed by <code>ₐ</code></p>

#### [ Kevin Buzzard (Jun 02 2018 at 03:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notation%20gimmick/near/127448374):
<p>Yes I'm sure you're right. It would just look less nerdy</p>

#### [ Simon Hudon (Jun 02 2018 at 03:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notation%20gimmick/near/127448450):
<p>Hmmm, a mathematician complaining about looking too nerdy ...</p>


{% endraw %}
