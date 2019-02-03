---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/55527whyisthishappening.html
---

## Stream: [general](index.html)
### Topic: [why is this happening](55527whyisthishappening.html)

---


{% raw %}
#### [ Koundinya Vajjha (Jan 16 2019 at 22:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/why%20is%20this%20happening/near/155291582):
<div class="codehilite"><pre><span></span><span class="kn">open</span> <span class="n">tactic</span> <span class="n">expr</span>

<span class="n">meta</span> <span class="n">def</span> <span class="n">wat</span> <span class="o">:</span> <span class="n">tactic</span> <span class="n">unit</span> <span class="o">:=</span>
<span class="n">do</span> <span class="n">ctx</span> <span class="err">←</span> <span class="n">local_context</span><span class="o">,</span>
  <span class="k">let</span> <span class="n">a</span> <span class="o">:=</span> <span class="n">app</span> <span class="n">ctx</span><span class="bp">.</span><span class="n">head</span> <span class="o">(</span><span class="n">list</span><span class="bp">.</span><span class="n">reverse</span> <span class="n">ctx</span><span class="o">)</span><span class="bp">.</span><span class="n">head</span><span class="o">,</span>
  <span class="n">type</span> <span class="err">←</span> <span class="n">infer_type</span> <span class="n">a</span><span class="o">,</span>
  <span class="n">trace</span> <span class="n">type</span><span class="o">,</span>
  <span class="n">skip</span>

<span class="kn">lemma</span> <span class="n">begins</span>  <span class="o">(</span><span class="n">f</span> <span class="o">:</span> <span class="bp">ℕ</span> <span class="bp">→</span> <span class="bp">ℕ</span><span class="o">)</span> <span class="o">(</span><span class="n">a</span> <span class="o">:</span> <span class="n">bool</span><span class="o">)</span> <span class="o">:</span> <span class="kt">Prop</span> <span class="o">:=</span>
<span class="k">begin</span>
<span class="n">wat</span><span class="o">,</span>  <span class="c1">-- returns ℕ</span>
<span class="kn">end</span>
</pre></div>


<p>But </p>
<div class="codehilite"><pre><span></span><span class="kn">variables</span> <span class="o">(</span><span class="n">a</span> <span class="o">:</span> <span class="n">bool</span><span class="o">)</span> <span class="o">(</span><span class="n">g</span> <span class="o">:</span> <span class="bp">ℕ</span>  <span class="bp">→</span> <span class="bp">ℕ</span> <span class="o">)</span>
<span class="bp">#</span><span class="kn">check</span> <span class="n">g</span> <span class="n">a</span>
</pre></div>


<p>returns a type mismatch error?</p>

#### [ Kenny Lau (Jan 16 2019 at 22:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/why%20is%20this%20happening/near/155291781):
<div class="codehilite"><pre><span></span><span class="kn">namespace</span> <span class="n">tactic</span><span class="bp">.</span><span class="n">interactive</span>
<span class="kn">open</span> <span class="n">tactic</span> <span class="n">lean</span><span class="bp">.</span><span class="n">parser</span> <span class="n">interactive</span> <span class="n">expr</span>
<span class="n">meta</span> <span class="n">def</span> <span class="n">wat</span> <span class="o">:</span> <span class="n">tactic</span> <span class="n">unit</span> <span class="o">:=</span>
<span class="n">do</span> <span class="n">ctx</span> <span class="err">←</span> <span class="n">local_context</span><span class="o">,</span>
  <span class="k">let</span> <span class="n">a</span> <span class="o">:=</span> <span class="n">app</span> <span class="n">ctx</span><span class="bp">.</span><span class="n">head</span> <span class="o">(</span><span class="n">list</span><span class="bp">.</span><span class="n">reverse</span> <span class="n">ctx</span><span class="o">)</span><span class="bp">.</span><span class="n">head</span><span class="o">,</span>
  <span class="n">type</span> <span class="err">←</span> <span class="n">infer_type</span> <span class="n">a</span><span class="o">,</span>
  <span class="n">trace</span> <span class="n">type</span><span class="o">,</span>
  <span class="n">skip</span>
<span class="kn">end</span> <span class="n">tactic</span><span class="bp">.</span><span class="n">interactive</span>

<span class="kn">lemma</span> <span class="n">begins</span>  <span class="o">(</span><span class="n">f</span> <span class="o">:</span> <span class="bp">ℕ</span> <span class="bp">→</span> <span class="bp">ℕ</span><span class="o">)</span> <span class="o">(</span><span class="n">a</span> <span class="o">:</span> <span class="n">bool</span><span class="o">)</span> <span class="o">:</span> <span class="kt">Prop</span> <span class="o">:=</span>
<span class="k">begin</span>
<span class="n">wat</span><span class="o">,</span>  <span class="c1">-- returns ℕ</span>
<span class="kn">end</span>
</pre></div>

#### [ Kenny Lau (Jan 16 2019 at 22:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/why%20is%20this%20happening/near/155291999):
<p>more info:</p>
<div class="codehilite"><pre><span></span><span class="kn">namespace</span> <span class="n">tactic</span><span class="bp">.</span><span class="n">interactive</span>
<span class="kn">open</span> <span class="n">tactic</span> <span class="n">lean</span><span class="bp">.</span><span class="n">parser</span> <span class="n">interactive</span> <span class="n">expr</span>
<span class="n">meta</span> <span class="n">def</span> <span class="n">wat</span> <span class="o">:</span> <span class="n">tactic</span> <span class="n">unit</span> <span class="o">:=</span>
<span class="n">do</span> <span class="n">ctx</span> <span class="err">←</span> <span class="n">local_context</span><span class="o">,</span>
  <span class="k">let</span> <span class="n">a</span> <span class="o">:=</span> <span class="n">app</span> <span class="n">ctx</span><span class="bp">.</span><span class="n">head</span> <span class="o">(</span><span class="n">list</span><span class="bp">.</span><span class="n">reverse</span> <span class="n">ctx</span><span class="o">)</span><span class="bp">.</span><span class="n">head</span><span class="o">,</span>
  <span class="n">type</span> <span class="err">←</span> <span class="n">infer_type</span> <span class="n">a</span><span class="o">,</span>
  <span class="n">tactic</span><span class="bp">.</span><span class="n">interactive</span><span class="bp">.</span><span class="k">let</span> <span class="n">none</span> <span class="n">none</span> <span class="bp">``</span><span class="o">(</span><span class="err">%%</span><span class="n">a</span><span class="o">),</span>
  <span class="n">skip</span>
<span class="kn">end</span> <span class="n">tactic</span><span class="bp">.</span><span class="n">interactive</span>

<span class="kn">lemma</span> <span class="n">begins</span>  <span class="o">(</span><span class="n">f</span> <span class="o">:</span> <span class="bp">ℕ</span> <span class="bp">→</span> <span class="bp">ℕ</span><span class="o">)</span> <span class="o">(</span><span class="n">a</span> <span class="o">:</span> <span class="n">bool</span><span class="o">)</span> <span class="o">:</span> <span class="kt">Prop</span> <span class="o">:=</span>
<span class="k">begin</span>
<span class="n">wat</span><span class="o">,</span>
<span class="n">sorry</span>
<span class="kn">end</span>
</pre></div>


<p>tactic state after <code>wat</code>:</p>
<div class="codehilite"><pre><span></span>f : ℕ → ℕ,
a : bool,
this : ℕ := f a
⊢ Prop
</pre></div>


<p>and error message of lemma after I put <code>sorry</code>:</p>
<div class="codehilite"><pre><span></span>type mismatch at application
  f a
term
  a
has type
  bool
but is expected to have type
  ℕ
</pre></div>

#### [ Reid Barton (Jan 16 2019 at 23:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/why%20is%20this%20happening/near/155292170):
<p>You manually built an <code>expr</code>= supposedly fully elaborated expression, but the <code>expr</code> you constructed is not actually valid. I guess that <code>infer_type</code> assumes the expression is valid and then according to the typing rules its type must be the return type of <code>f</code>. You didn't get an error because you didn't do anything with the <code>expr</code>.</p>

#### [ Rob Lewis (Jan 16 2019 at 23:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/why%20is%20this%20happening/near/155292366):
<p>Yeah, <code>infer_type</code> doesn't completely type check the expression, otherwise it would be very expensive. There's another tactic called <code>type_check</code> that should fail if you call it on <code>a</code>.</p>

#### [ Reid Barton (Jan 16 2019 at 23:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/why%20is%20this%20happening/near/155292374):
<p>If you used <code>tactic.exact a</code> (supposing you change the goal to <code>nat</code>) then I imagine the tactic would succeed but then you would get a type error at a later stage.</p>

#### [ Koundinya Vajjha (Jan 16 2019 at 23:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/why%20is%20this%20happening/near/155292406):
<p><span class="user-mention" data-user-id="110032">@Reid Barton</span>  yeah seems like that's what is happening.</p>

#### [ Kenny Lau (Jan 16 2019 at 23:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/why%20is%20this%20happening/near/155292507):
<p>well it's <code>meta</code> so it can be unsound anyway</p>

#### [ Koundinya Vajjha (Jan 16 2019 at 23:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/why%20is%20this%20happening/near/155292545):
<p><code>type_check</code> is exactly what I needed.</p>

#### [ Kenny Lau (Jan 16 2019 at 23:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/why%20is%20this%20happening/near/155292547):
<p>you aren't actually changing the partially generated proof by <code>trace</code></p>

#### [ Rob Lewis (Jan 16 2019 at 23:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/why%20is%20this%20happening/near/155292687):
<p>In general, making applications manually can be difficult. Do it if you're confident in what you're doing, since it will be more efficient. Otherwise <code>mk_app</code> and <code>mk_mapp</code> are your friends. In particular the error messages will be more helpful.</p>

#### [ Koundinya Vajjha (Jan 16 2019 at 23:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/why%20is%20this%20happening/near/155293217):
<p>I'm having trouble figuring out how to use <code>mk_app</code>.  I have <code>f : ℕ → ℝ</code> and <code>b : ℕ</code>. How do I use this to make the application <code>f b</code>?</p>

#### [ Kenny Lau (Jan 16 2019 at 23:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/why%20is%20this%20happening/near/155293421):
<div class="codehilite"><pre><span></span><span class="kn">namespace</span> <span class="n">tactic</span><span class="bp">.</span><span class="n">interactive</span>
<span class="kn">open</span> <span class="n">tactic</span> <span class="n">lean</span><span class="bp">.</span><span class="n">parser</span> <span class="n">interactive</span> <span class="n">expr</span>
<span class="n">meta</span> <span class="n">def</span> <span class="n">wat</span> <span class="o">:</span> <span class="n">tactic</span> <span class="n">unit</span> <span class="o">:=</span>
<span class="n">do</span> <span class="n">ctx</span> <span class="err">←</span> <span class="n">local_context</span><span class="o">,</span>
  <span class="k">let</span> <span class="n">a</span> <span class="o">:=</span> <span class="n">expr</span><span class="bp">.</span><span class="n">mk_app</span> <span class="n">ctx</span><span class="bp">.</span><span class="n">head</span> <span class="o">[</span><span class="n">ctx</span><span class="bp">.</span><span class="n">reverse</span><span class="bp">.</span><span class="n">head</span><span class="o">],</span>
  <span class="n">tactic</span><span class="bp">.</span><span class="n">type_check</span> <span class="n">a</span><span class="o">,</span>
  <span class="n">type</span> <span class="err">←</span> <span class="n">infer_type</span> <span class="n">a</span><span class="o">,</span>
  <span class="n">trace</span> <span class="n">type</span><span class="o">,</span>
  <span class="n">tactic</span><span class="bp">.</span><span class="n">interactive</span><span class="bp">.</span><span class="k">let</span> <span class="n">none</span> <span class="n">none</span> <span class="bp">``</span><span class="o">(</span><span class="err">%%</span><span class="n">a</span><span class="o">),</span>
  <span class="n">skip</span>
<span class="kn">end</span> <span class="n">tactic</span><span class="bp">.</span><span class="n">interactive</span>

<span class="kn">lemma</span> <span class="n">begins</span>  <span class="o">(</span><span class="n">f</span> <span class="o">:</span> <span class="bp">ℕ</span> <span class="bp">→</span> <span class="bp">ℕ</span><span class="o">)</span> <span class="o">(</span><span class="n">a</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">)</span> <span class="o">:</span> <span class="bp">ℕ</span> <span class="o">:=</span>
<span class="k">begin</span>
<span class="n">wat</span><span class="o">,</span>  <span class="c1">-- returns ℕ</span>
<span class="kn">end</span>
</pre></div>

#### [ Koundinya Vajjha (Jan 16 2019 at 23:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/why%20is%20this%20happening/near/155293593):
<p>Okay that was silly. Thanks <span class="user-mention" data-user-id="110064">@Kenny Lau</span></p>


{% endraw %}
