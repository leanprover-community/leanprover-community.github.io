---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/68171generalizinganunpackedstructure.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [generalizing an unpacked structure](https://leanprover-community.github.io/archive/113488general/68171generalizinganunpackedstructure.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Moses Schönfinkel (Oct 25 2018 at 09:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generalizing%20an%20unpacked%20structure/near/136460837):
<p>I have something like <code>{to_structure := {x := X, y := Y}}</code> in my goal's conclusion. Is it possible to express <code>generalize h : {to_structure := {x := X, y := Y}} = a</code> somehow? (This particular formulation errors with <code>invalid structure instance, identifier expected</code>.)</p>

#### [ Simon Hudon (Oct 25 2018 at 12:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generalizing%20an%20unpacked%20structure/near/136468338):
<p>You may need to give the name of each structure as <code>generalize h : {foo . to_structure := {bar . x := X, y := Y}} = a</code></p>

#### [ Moses Schönfinkel (Oct 25 2018 at 21:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generalizing%20an%20unpacked%20structure/near/136502451):
<p>Oh. Thanks. That's going to be a little painful.</p>


{% endraw %}
