---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/24753buildingextensionalitylemmasforstructures.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [building @[extensionality] lemmas for structures](https://leanprover-community.github.io/archive/113488general/24753buildingextensionalitylemmasforstructures.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Scott Morrison (Aug 13 2018 at 15:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/building%20%40%5Bextensionality%5D%20lemmas%20for%20structures/near/132045472):
<p>Hi <span class="user-mention" data-user-id="110026">@Simon Hudon</span>, I'm wondering if you've thought recently about building <code>@[extensionality]</code> lemmas for structures automatically. I know we had some discussion about this a long time ago (gitter?), and some attempts at a <code>congr_struct</code> tactic.</p>

#### [ Simon Hudon (Aug 13 2018 at 15:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/building%20%40%5Bextensionality%5D%20lemmas%20for%20structures/near/132046891):
<p>Hi Scott! No, I haven't thought of it but I think it shouldn't be hard. We could invoke it with <code>@[make_extentionality]</code> to distinguish from the lemma itself.</p>

#### [ Mario Carneiro (Aug 13 2018 at 15:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/building%20%40%5Bextensionality%5D%20lemmas%20for%20structures/near/132046948):
<p>shouldn't that obviously be a derive handler?</p>

#### [ Scott Morrison (Aug 13 2018 at 15:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/building%20%40%5Bextensionality%5D%20lemmas%20for%20structures/near/132046968):
<p>From memory the problems quickly arose when there were dependent fields. First there's the question of whether to use rewrites or heqs.</p>

#### [ Scott Morrison (Aug 13 2018 at 15:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/building%20%40%5Bextensionality%5D%20lemmas%20for%20structures/near/132047029):
<p>But I think correctly building the statements for later fields, in either approach, seemed hardish.</p>

#### [ Mario Carneiro (Aug 13 2018 at 15:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/building%20%40%5Bextensionality%5D%20lemmas%20for%20structures/near/132047037):
<p>can't you just use <code>congr</code> to generate the lemma?</p>

#### [ Scott Morrison (Aug 13 2018 at 15:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/building%20%40%5Bextensionality%5D%20lemmas%20for%20structures/near/132047051):
<p>At the time I knew almost nothing about writing tactics, and haven't thought much about it since, however. :-)</p>

#### [ Mario Carneiro (Aug 13 2018 at 15:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/building%20%40%5Bextensionality%5D%20lemmas%20for%20structures/near/132047080):
<p>However, I don't usually find that extensionality lemmas are automatable</p>

#### [ Mario Carneiro (Aug 13 2018 at 15:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/building%20%40%5Bextensionality%5D%20lemmas%20for%20structures/near/132047104):
<p>since they are often mathematically nontrivial, e.g. <code>units A</code> only depends on the first component</p>

#### [ Simon Hudon (Aug 13 2018 at 15:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/building%20%40%5Bextensionality%5D%20lemmas%20for%20structures/near/132047105):
<p><span class="user-mention" data-user-id="110049">@Mario Carneiro</span> I also thought about making it a derive handler but I think it has to be a type class for that, no?</p>

#### [ Mario Carneiro (Aug 13 2018 at 15:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/building%20%40%5Bextensionality%5D%20lemmas%20for%20structures/near/132047165):
<p>I thought the thing after <code>derive</code> was just a label</p>

#### [ Scott Morrison (Aug 13 2018 at 15:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/building%20%40%5Bextensionality%5D%20lemmas%20for%20structures/near/132047194):
<p>You mean ... make a metavariable of type <code>a = b</code>, actually run the <code>cases a, cases b, congr</code> tactic, then inspect the goals, take those as arguments for your declaration, and have the proof by <code>cases a, cases b, congr ; assumption</code>?</p>

#### [ Mario Carneiro (Aug 13 2018 at 15:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/building%20%40%5Bextensionality%5D%20lemmas%20for%20structures/near/132047240):
<p>yes</p>

#### [ Mario Carneiro (Aug 13 2018 at 15:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/building%20%40%5Bextensionality%5D%20lemmas%20for%20structures/near/132047277):
<p>or more directly, just generate the <code>congr_lemma</code> and inspect its type</p>

#### [ Scott Morrison (Aug 13 2018 at 15:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/building%20%40%5Bextensionality%5D%20lemmas%20for%20structures/near/132047460):
<p>I see. We'd need a cleanup phase that decides when fields are propositional and omits those <code>heq</code>s.</p>

#### [ Mario Carneiro (Aug 13 2018 at 15:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/building%20%40%5Bextensionality%5D%20lemmas%20for%20structures/near/132047519):
<p>no, that's why I am suggesting you use the <code>congr_lemma</code></p>

#### [ Mario Carneiro (Aug 13 2018 at 15:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/building%20%40%5Bextensionality%5D%20lemmas%20for%20structures/near/132047521):
<p>it does that already</p>

#### [ Simon Hudon (Aug 13 2018 at 15:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/building%20%40%5Bextensionality%5D%20lemmas%20for%20structures/near/132047629):
<p>Looking at the code for <code>derive_attr</code>, I think you're right Mario and it is of course a much better way</p>

#### [ Scott Morrison (Aug 13 2018 at 15:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/building%20%40%5Bextensionality%5D%20lemmas%20for%20structures/near/132047635):
<p>oh, okay: why doesn't <code>congr</code> do that then?</p>

#### [ Simon Hudon (Aug 13 2018 at 15:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/building%20%40%5Bextensionality%5D%20lemmas%20for%20structures/near/132047661):
<p>Doesn't it?</p>

#### [ Scott Morrison (Aug 13 2018 at 15:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/building%20%40%5Bextensionality%5D%20lemmas%20for%20structures/near/132047751):
<p>I just tried on <code>category_theory.functor</code>, and got goals for the propositional fields.</p>

#### [ Simon Hudon (Aug 13 2018 at 15:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/building%20%40%5Bextensionality%5D%20lemmas%20for%20structures/near/132047967):
<p>I'm surprised. You can clean them up I think using <code>match_eq</code> / <code>match_heq</code> and then using <code>is_proof</code> on the results.</p>

#### [ Simon Hudon (Aug 13 2018 at 15:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/building%20%40%5Bextensionality%5D%20lemmas%20for%20structures/near/132048418):
<p><span class="user-mention" data-user-id="110049">@Mario Carneiro</span> The annoying thing with <code>derive</code> is that it parses a <code>pexpr</code> and does some basic name resolution. We may get around it by defining a dummy like <code>def extensionality := ()</code></p>

#### [ Simon Hudon (Aug 14 2018 at 20:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/building%20%40%5Bextensionality%5D%20lemmas%20for%20structures/near/132126240):
<p><span class="user-mention" data-user-id="110087">@Scott Morrison</span> Any luck in building it?</p>

#### [ Scott Morrison (Aug 15 2018 at 00:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/building%20%40%5Bextensionality%5D%20lemmas%20for%20structures/near/132141380):
<p>Sorry, haven't got back to it. Writing <code>ext</code> lemmas by hand is annoying but not critical. :-)</p>


{% endraw %}
