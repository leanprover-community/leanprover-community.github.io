---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/09475Shamelesslean4request.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [Shameless lean 4 request](https://leanprover-community.github.io/archive/113488general/09475Shamelesslean4request.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Keeley Hoek (Nov 23 2018 at 02:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Shameless%20lean%204%20request/near/148202175):
<p>In Lean 4 could we please please please have something like Haskell's <code>error</code>, just a pure function which takes a <code>string</code> or <code>format</code> or something and otherwise acts just like <code>sorry</code> (but gives no <code>sorry</code> used warnings). Of course, it would have to be meta.</p>
<p>It would be a really big aid to metaprogramming, since right now every time I want to define a pure function used in a program which has some invalid arguments I have to make it fail silently for that invalid input, instead of returning a nice warning---or more likely from a practical perspective, make everything tactic for absolutely no reason and corrupt my entire program with <code>tactic</code>.</p>

#### [ Reid Barton (Nov 23 2018 at 02:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Shameless%20lean%204%20request/near/148202217):
<p>I thought there was something like this already. <code>undefined_core</code>?</p>

#### [ Keeley Hoek (Nov 23 2018 at 02:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Shameless%20lean%204%20request/near/148202274):
<p>Praise be! weird name</p>

#### [ Reid Barton (Nov 23 2018 at 02:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Shameless%20lean%204%20request/near/148202315):
<p>Haha, yes</p>


{% endraw %}
