---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/77786Modules.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [Modules](https://leanprover-community.github.io/archive/113488general/77786Modules.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Morenikeji Neri (Jul 26 2018 at 00:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Modules/near/130306693):
<p>Why is is_linear_map not a class?</p>

#### [ Patrick Massot (Jul 26 2018 at 00:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Modules/near/130306882):
<p>I think it's for historical reasons</p>

#### [ Morenikeji Neri (Jul 26 2018 at 00:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Modules/near/130307142):
<p>care to explain further?</p>

#### [ Kevin Buzzard (Jul 26 2018 at 01:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Modules/near/130308302):
<p>Here's a related question -- would a PR which made it a class be appreciated? It's in <code>algebra/module.lean</code> -- oh -- I see that file was written back in 2015! Wow! It's a prop so there are presumably no diamond issues. It seems an ideal thing to be a class. What am I missing?</p>

#### [ Chris Hughes (Jul 26 2018 at 01:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Modules/near/130308409):
<p>I'm guessing the reason might be something to do with the type class inference problems with modules, meaning it doesn't get inferred.</p>

#### [ Patrick Massot (Jul 26 2018 at 09:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Modules/near/130327984):
<blockquote>
<p>care to explain further?</p>
</blockquote>
<p>I mean this was written before we started to use classes for such things, and it was not changed since then. So the relevant question is indeed Kevin's one.</p>

#### [ Patrick Massot (Jul 26 2018 at 09:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Modules/near/130328041):
<p>And of course Chris' worry is also relevant, modules are <a href="https://github.com/leanprover/mathlib/issues/210" target="_blank" title="https://github.com/leanprover/mathlib/issues/210">tricky for the type class inference system</a>.</p>

#### [ Kevin Buzzard (Jul 26 2018 at 09:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Modules/near/130328045):
<blockquote>
<p>I'm guessing the reason might be something to do with the type class inference problems with modules, meaning it doesn't get inferred.</p>
</blockquote>
<p>What are these issues? I used modules yesterday and they worked fine....ooh! A link!</p>

#### [ Kevin Buzzard (Jul 26 2018 at 09:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Modules/near/130328062):
<p>Wait, that link tells me nothing. I wanted to add to it but I'm hoping that someone other than me adds to it. I am adding something now.</p>


{% endraw %}
