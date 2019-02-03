---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/05461subtypesvsets.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [subtypes v sets](https://leanprover-community.github.io/archive/113488general/05461subtypesvsets.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Kevin Buzzard (Mar 04 2018 at 01:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subtypes%20v%20sets/near/123245378):
<p>I have <code>U : set alpha</code> and I want to make a Pi type which morally is <code>\Pi P : U, (some function of P)</code></p>

#### [ Kevin Buzzard (Mar 04 2018 at 02:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subtypes%20v%20sets/near/123245429):
<p>I went for <code>\Pi P : {u : alpha // U u}, ...</code></p>

#### [ Kevin Buzzard (Mar 04 2018 at 02:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subtypes%20v%20sets/near/123245440):
<p>and now I am constantly running into <code>v \in U</code> which I want to do my Pi<br>
 stuff to</p>

#### [ Kevin Buzzard (Mar 04 2018 at 02:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subtypes%20v%20sets/near/123245535):
<p>meh I guess I just shouldn't be considering "elements of U" I should just be avoiding the set notation completely now</p>

#### [ Andrew Ashworth (Mar 04 2018 at 02:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subtypes%20v%20sets/near/123246309):
<p>if you want to stay with sets, you could use the set image lemmas</p>

#### [ Andrew Ashworth (Mar 04 2018 at 02:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subtypes%20v%20sets/near/123246397):
<p>but definitely type theory notation is more natural to work in</p>

#### [ Mario Carneiro (Mar 04 2018 at 07:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subtypes%20v%20sets/near/123253942):
<blockquote>
<p>I have <code>U : set alpha</code> and I want to make a Pi type which morally is <code>\Pi P : U, (some function of P)</code></p>
</blockquote>
<p>Did you actually try <code>\Pi P : U, (some function of P)</code>? That should work because of coercions</p>

#### [ Kevin Buzzard (Mar 04 2018 at 13:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subtypes%20v%20sets/near/123261361):
<p>No I didn't :-) I know that if I'd tried this, I would have ended up not knowing what the type of P actually was, at least initially. Probably what you're saying is that if I'd tried it, it would have unfolded into what I actually used. More and more I am deciding not to use coercions or type classes because I realise that rather than using them and then struggling later it is easier for me to just do all the work myself. I guess what I'm saying is that initially things like coercions and the type class system were complete mysteries to me and I could see them working in simple cases and failing in more complex ones and didn't really understand enough to know how to make them work for me. Now I've decided to do all coercions myself, and of course now I understand what's going on much better. The next phrase will be me attempting to use these tools again, but this time knowing how to use them properly.</p>

#### [ Chris Hughes (Mar 04 2018 at 15:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subtypes%20v%20sets/near/123264655):
<p><span class="user-mention" data-user-email="k.buzzard@imperial.ac.uk" data-user-id="110038">@Kevin Buzzard</span> I just wrote some docs about this, which I PRed to your WIP docs.</p>

#### [ Patrick Massot (Mar 04 2018 at 18:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subtypes%20v%20sets/near/123268965):
<p><span class="user-mention" data-user-email="chrishughes24@gmail.com" data-user-id="110044">@Chris Hughes</span> your doc on set-like stuff is awesome. I added some comments (but I guess Kevin needs to allow them before you can see them). Then I think this should go straight to mathlib in the theories folder (with a link in <a href="https://github.com/leanprover/mathlib/blob/master/docs/theories.md" target="_blank" title="https://github.com/leanprover/mathlib/blob/master/docs/theories.md">https://github.com/leanprover/mathlib/blob/master/docs/theories.md</a>)</p>

#### [ Chris Hughes (Mar 04 2018 at 20:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subtypes%20v%20sets/near/123271485):
<p>The main downside I can see to the Pi version, is if you ever wanted to prove the function is injective or has an inverse. No idea if you'd ever want to do that.</p>

#### [ Kevin Buzzard (Mar 04 2018 at 21:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subtypes%20v%20sets/near/123273900):
<p>In my context I don't think I'll ever want to do this.</p>


{% endraw %}
