---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113489newmembers/68806Replacingrwwithterms.html
---

## Stream: [new members](https://leanprover-community.github.io/archive/113489newmembers/index.html)
### Topic: [Replacing rw with terms](https://leanprover-community.github.io/archive/113489newmembers/68806Replacingrwwithterms.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Andreas Swerdlow (Sep 15 2018 at 15:37)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Replacing%20rw%20with%20terms/near/134012592):
<p>I have some proofs written in tactic mode that contain a lot of rewrites, including rewrites of hypotheses. Is there a way to easily convert such proofs into term mode. I know about eq.subst but can’t see a way to do this that won’t take aeons. </p>
<p>Apologies in advance I’m away so won’t be replying quickly.</p>

#### [ Kevin Buzzard (Sep 15 2018 at 15:40)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Replacing%20rw%20with%20terms/near/134012702):
<p>The term mode version of <code>rw</code> is the rather harder to use <code>\t</code>, which is notation for <code>eq.subst</code>, which you already know about. In special cases you can be lucky -- e.g. if your goal is <code>X</code> and you want to rewrite <code>H : X &lt;-&gt; Y</code> then you can just apply <code>H.2</code>. But if it's a more complicated rewrite then you either briefly drop into tactic mode with <code>by rw [A,B,C]</code> or grit your teeth and wrestle with the triangle (which is far more picky about metavariables for some reason; giving things explicit types sometimes helps).</p>

#### [ Chris Hughes (Sep 15 2018 at 15:41)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Replacing%20rw%20with%20terms/near/134012725):
<p>Generally <code>rw</code>'s should be done in tactic mode, but often you can replace a bunch of rewrites with a <code>simp</code>, with carefully chosen lemmas in the <code>[]</code></p>

#### [ Kevin Buzzard (Sep 15 2018 at 15:41)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Replacing%20rw%20with%20terms/near/134012728):
<p><a href="https://github.com/leanprover-community/mathlib/blob/fb1a93300ab05e86835f154e2b6156ef2ceaf77d/commutative_algebra/hilbert_basis.lean#L22" target="_blank" title="https://github.com/leanprover-community/mathlib/blob/fb1a93300ab05e86835f154e2b6156ef2ceaf77d/commutative_algebra/hilbert_basis.lean#L22">https://github.com/leanprover-community/mathlib/blob/fb1a93300ab05e86835f154e2b6156ef2ceaf77d/commutative_algebra/hilbert_basis.lean#L22</a></p>

#### [ Kevin Buzzard (Sep 15 2018 at 15:42)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Replacing%20rw%20with%20terms/near/134012773):
<p>I was working on that today. Originally all proofs were in tactic mode. I then managed to turn most stuff into term mode, but failed on that last line so left the rewrite in.</p>

#### [ Andreas Swerdlow (Sep 15 2018 at 17:01)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Replacing%20rw%20with%20terms/near/134015438):
<p>Is there any advantage to term mode in a case like this?</p>

#### [ Kevin Buzzard (Sep 15 2018 at 18:55)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Replacing%20rw%20with%20terms/near/134019185):
<p>I think term mode proofs are less likely to break, or perhaps they break in very predictable ways. But I honestly don't know. I just get the feeling that the mathlib people like term mode better if possible, so that's what I'm working towards. I don't have any maintainer experience.</p>


{% endraw %}
