---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/44550Projectionaftermkstructure.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [Projection after mk-structure](https://leanprover-community.github.io/archive/113488general/44550Projectionaftermkstructure.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Keeley Hoek (Sep 16 2018 at 18:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Projection%20after%20mk-structure/near/134060550):
<p>Say I've got a function <code>mk_struct</code> which takes some arguments and produces something of type <code>struct</code>. The function <code>mk_struct</code> needn't be the <code>struct.mk</code> constructor---maybe it takes some arguments, proves some stuff about them, and then packages it all up by calling the constructor <code>struct.mk</code> (the point is that the arguments of <code>mk_struct</code> can be totally different).</p>

#### [ Keeley Hoek (Sep 16 2018 at 18:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Projection%20after%20mk-structure/near/134060552):
<p>Now say <code>struct</code> has a projection <code>struct.foo</code>. There is a single unambiguous way to construct a function <code>mk_struct.foo</code>, which forgets all of the components of whatever <code>mk_struct</code> outputs except for <code>foo</code>. I'd like to programmatically obtain the <em>type</em> of this function <code>mk_struct.foo</code>.</p>
<p>Actually, I've essentially done this, but it was incredibly stupid: I directly built everything over <code>expr.xxx</code>'s and manually wrote code to unify the arguments of the projection and the output-type of <code>mk_struct</code>, and in the end it wasn't robust enough to deal with universe parameters.</p>

#### [ Keeley Hoek (Sep 16 2018 at 18:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Projection%20after%20mk-structure/near/134060594):
<p>But I'm sure this was all crazy---I'm sure I can exploit lean's facilities (at the very least <code>unify</code>) to do the resolution which I need. Perhaps I'm looking for a suped-up <code>tactic.mk_app</code> that can unroll the quantifiers from the argument I want to apply? What's the canonical way to go about <code>expr</code> fiddling like this?</p>

#### [ Mario Carneiro (Sep 16 2018 at 22:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Projection%20after%20mk-structure/near/134066795):
<p>I'm confused why this is different from <code>struct.foo ∘ mk_struct</code>. Can't you just figure out the type of this?</p>

#### [ Keeley Hoek (Sep 17 2018 at 06:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Projection%20after%20mk-structure/near/134079723):
<p><span class="user-mention" data-user-id="110049">@Mario Carneiro</span>  Thanks for taking a look. Here's a concrete example:</p>
<div class="codehilite"><pre><span></span>structure struct (n : ℤ) :=
(foo : ℕ)

def mk_struct (m : ℕ) : struct m := ⟨m, 2 * m⟩

#check struct.foo ∘ mk_struct
#check λ m, (mk_struct m).foo
</pre></div>


<p>The second-to-bottom line fails to typecheck, since <code>mk_struct</code> takes a (possibly a few) potentially random arguments. I'd really like to be able to compose to essentially do what the last line does, without having to know the arguments of <code>mk_struct</code> in advance.</p>

#### [ Mario Carneiro (Sep 17 2018 at 06:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Projection%20after%20mk-structure/near/134080030):
<p>do you know the arguments of <code>struct.foo</code>?</p>

#### [ Mario Carneiro (Sep 17 2018 at 06:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Projection%20after%20mk-structure/near/134080101):
<p>this function in <code>tactic/alias.lean</code> seems similar:</p>
<div class="codehilite"><pre><span></span>meta def mk_iff_mp_app (iffmp : name) : expr → (nat → expr) → tactic expr
| (expr.pi n bi e t) f := expr.lam n bi e &lt;$&gt; mk_iff_mp_app t (λ n, f (n+1) (expr.var n))
| `(%%a ↔ %%b) f := pure $ @expr.const tt iffmp [] a b (f 0)
| _ f := fail &quot;Target theorem must have the form `Π x y z, a ↔ b`&quot;
</pre></div>


<p>it constructs the term <code>\lam x y z, iff.mp (f x y z)</code></p>


{% endraw %}
