---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/85855poormanshintdatabase.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [poor man's hint database](https://leanprover-community.github.io/archive/113488general/85855poormanshintdatabase.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Moses Schönfinkel (Nov 19 2018 at 09:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/poor%20man%27s%20hint%20database/near/147951801):
<p>Is there a way to simulate Coq's hint database? For example, I often find myself writing <code>simp [x₁, x₂, x₃, x₄]</code>, which I would like to replace with <code>simp [x_lemmas]</code> where <code>x_lemmas</code> is a sort of a "hint database" for lack of better term. (Do note that I don't want to designate <code>xₙ</code> to be simp lemmas.)</p>

#### [ Mario Carneiro (Nov 19 2018 at 09:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/poor%20man%27s%20hint%20database/near/147951920):
<p>there are simp sets, but we don't use them very often</p>

#### [ Mario Carneiro (Nov 19 2018 at 09:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/poor%20man%27s%20hint%20database/near/147951926):
<p>you can write <code>simp with x_lemmas</code></p>

#### [ Moses Schönfinkel (Nov 19 2018 at 09:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/poor%20man%27s%20hint%20database/near/147951950):
<p>Where <code>x_lemmas</code> is a "simp set"? Would it be weird for you to encounter that somewhere in Lean code - is that something to avoid?</p>

#### [ Mario Carneiro (Nov 19 2018 at 09:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/poor%20man%27s%20hint%20database/near/147951992):
<p>The "default" simp set is not necessarily a superset of other simp sets, so it should be fine</p>

#### [ Mario Carneiro (Nov 19 2018 at 09:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/poor%20man%27s%20hint%20database/near/147951997):
<p>It would be unusual, but not unheard of</p>

#### [ Moses Schönfinkel (Nov 19 2018 at 09:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/poor%20man%27s%20hint%20database/near/147952001):
<p>good enough, thanks</p>

#### [ Mario Carneiro (Nov 19 2018 at 09:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/poor%20man%27s%20hint%20database/near/147952005):
<p>It forms part of the public interface, so I don't use it for one off things</p>

#### [ Kenny Lau (Nov 19 2018 at 10:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/poor%20man%27s%20hint%20database/near/147953651):
<blockquote>
<p>The "default" simp set is not necessarily a superset of other simp sets, so it should be fine</p>
</blockquote>
<p>No. We have demonstrated more than once that using a simp set speeds things up.</p>

#### [ Kenny Lau (Nov 19 2018 at 10:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/poor%20man%27s%20hint%20database/near/147953658):
<p>I don’t know why you don’t like it.</p>

#### [ Mario Carneiro (Nov 19 2018 at 10:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/poor%20man%27s%20hint%20database/near/147953898):
<p>?</p>

#### [ Mario Carneiro (Nov 19 2018 at 10:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/poor%20man%27s%20hint%20database/near/147953956):
<p>what does that have to do with my quote</p>

#### [ Kenny Lau (Nov 19 2018 at 10:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/poor%20man%27s%20hint%20database/near/147954062):
<p>well that means the default simp set is much bigger</p>

#### [ Mario Carneiro (Nov 19 2018 at 10:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/poor%20man%27s%20hint%20database/near/147954155):
<p>I said it is <em>not</em> a superset</p>


{% endraw %}
