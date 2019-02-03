---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/13048substathyp.html
---

## Stream: [general](index.html)
### Topic: [subst at hyp](13048substathyp.html)

---


{% raw %}
#### [ Johan Commelin (Sep 07 2018 at 10:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subst%20at%20hyp/near/133497289):
<p>Could we have <code>subst foobar at hyp</code> for substituting in the hypotheses of the local context? Currently I am using <code>repeat {rw foobar at hyp}</code> which feels a bit verbose...</p>

#### [ Kenny Lau (Sep 07 2018 at 10:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subst%20at%20hyp/near/133497352):
<p><code>subst foobar</code></p>

#### [ Chris Hughes (Sep 07 2018 at 10:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subst%20at%20hyp/near/133497411):
<p>What about <code>simp only [foobar] at hyp</code></p>

#### [ Johan Commelin (Sep 07 2018 at 10:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subst%20at%20hyp/near/133497450):
<p>aah never mind. <code>subst</code> is only for local constants. I wanted to substitute <code>x = y</code> where <code>x = y</code> was the result of some proposition.</p>

#### [ Johan Commelin (Sep 07 2018 at 10:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subst%20at%20hyp/near/133497493):
<p><code>simp only</code> works!</p>

#### [ Kenny Lau (Sep 07 2018 at 10:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subst%20at%20hyp/near/133497565):
<p>MWE?</p>

#### [ Johan Commelin (Sep 07 2018 at 10:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subst%20at%20hyp/near/133497570):
<p><a href="https://gist.github.com/jcommelin/2e031b5446ca54089576ea9f66f12abf" target="_blank" title="https://gist.github.com/jcommelin/2e031b5446ca54089576ea9f66f12abf">https://gist.github.com/jcommelin/2e031b5446ca54089576ea9f66f12abf</a></p>

#### [ Kenny Lau (Sep 07 2018 at 10:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subst%20at%20hyp/near/133497619):
<p>?</p>

#### [ Johan Commelin (Sep 07 2018 at 10:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subst%20at%20hyp/near/133497678):
<p>Right, so now you only see the <code>simp</code>s. For the <code>repeat {rw ...}</code> you have to look in the history.</p>

#### [ Johan Commelin (Sep 07 2018 at 10:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subst%20at%20hyp/near/133497681):
<p>Basically I'm challenging you to golf it <span class="emoji emoji-1f606" title="lol">:lol:</span></p>

#### [ Kenny Lau (Sep 07 2018 at 10:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subst%20at%20hyp/near/133497852):
<p>what import is allowed?</p>

#### [ Johan Commelin (Sep 07 2018 at 10:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subst%20at%20hyp/near/133497883):
<p>I don't really care</p>

#### [ Johan Commelin (Sep 07 2018 at 10:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subst%20at%20hyp/near/133497892):
<p>What would you want to use? <code>tidy</code>?</p>

#### [ Kenny Lau (Sep 07 2018 at 10:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subst%20at%20hyp/near/133497943):
<p>you didn't import any file from mathlib, so I can't use any mathlib tactic</p>

#### [ Johan Commelin (Sep 07 2018 at 10:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subst%20at%20hyp/near/133497962):
<p>Wasnt <code>have ... simp at this ... exact this</code> some sort of idiom that can be golfed into a <code>simpa</code>-oneliner? I tried but failed.</p>

#### [ Reid Barton (Sep 07 2018 at 10:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subst%20at%20hyp/near/133498111):
<p><code>simpa using this</code></p>

#### [ Reid Barton (Sep 07 2018 at 10:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subst%20at%20hyp/near/133498115):
<p>Or rather <code>simpa using ...</code></p>

#### [ Johan Commelin (Sep 07 2018 at 10:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subst%20at%20hyp/near/133498231):
<p>And what do I need to import to get <code>simpa</code>?</p>

#### [ Reid Barton (Sep 07 2018 at 10:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subst%20at%20hyp/near/133498273):
<p>My attempt: <a href="https://gist.github.com/rwbarton/b79b804e4bff300a5aa2a4ec2951c55e" target="_blank" title="https://gist.github.com/rwbarton/b79b804e4bff300a5aa2a4ec2951c55e">https://gist.github.com/rwbarton/b79b804e4bff300a5aa2a4ec2951c55e</a></p>

#### [ Reid Barton (Sep 07 2018 at 10:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subst%20at%20hyp/near/133498276):
<p>Anything in mathlib, but say <code>tactic.interactive</code></p>

#### [ Kenny Lau (Sep 07 2018 at 10:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subst%20at%20hyp/near/133498303):
<div class="codehilite"><pre><span></span><span class="kn">import</span> <span class="n">tactic</span><span class="bp">.</span><span class="n">interactive</span>

<span class="kn">universe</span> <span class="n">u</span>

<span class="kn">namespace</span> <span class="n">eckmann_hilton</span>
<span class="kn">variables</span> <span class="o">(</span><span class="n">X</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">)</span>

<span class="n">local</span> <span class="kn">notation</span> <span class="n">a</span> <span class="bp">`&lt;`</span><span class="n">m</span><span class="bp">`&gt;`</span> <span class="n">b</span> <span class="o">:=</span> <span class="bp">@</span><span class="n">has_mul</span><span class="bp">.</span><span class="n">mul</span> <span class="n">X</span> <span class="n">m</span> <span class="n">a</span> <span class="n">b</span>

<span class="n">class</span> <span class="n">is_unital</span> <span class="o">[</span><span class="n">m</span> <span class="o">:</span> <span class="n">has_mul</span> <span class="n">X</span><span class="o">]</span> <span class="o">[</span><span class="n">e</span> <span class="o">:</span> <span class="n">has_one</span> <span class="n">X</span><span class="o">]</span> <span class="o">:</span> <span class="kt">Prop</span> <span class="o">:=</span>
<span class="o">(</span><span class="n">one_mul</span> <span class="o">:</span> <span class="bp">∀</span> <span class="n">x</span> <span class="o">:</span> <span class="n">X</span><span class="o">,</span> <span class="o">(</span><span class="n">e</span><span class="bp">.</span><span class="n">one</span> <span class="bp">&lt;</span><span class="n">m</span><span class="bp">&gt;</span> <span class="n">x</span><span class="o">)</span> <span class="bp">=</span> <span class="n">x</span><span class="o">)</span>
<span class="o">(</span><span class="n">mul_one</span> <span class="o">:</span> <span class="bp">∀</span> <span class="n">x</span> <span class="o">:</span> <span class="n">X</span><span class="o">,</span> <span class="o">(</span><span class="n">x</span> <span class="bp">&lt;</span><span class="n">m</span><span class="bp">&gt;</span> <span class="n">e</span><span class="bp">.</span><span class="n">one</span><span class="o">)</span> <span class="bp">=</span> <span class="n">x</span><span class="o">)</span>

<span class="n">attribute</span> <span class="o">[</span><span class="n">simp</span><span class="o">]</span> <span class="n">is_unital</span><span class="bp">.</span><span class="n">one_mul</span> <span class="n">is_unital</span><span class="bp">.</span><span class="n">mul_one</span>

<span class="kn">variables</span> <span class="o">{</span><span class="n">X</span><span class="o">}</span> <span class="o">{</span><span class="n">m₁</span> <span class="o">:</span> <span class="n">has_mul</span> <span class="n">X</span><span class="o">}</span> <span class="o">{</span><span class="n">e₁</span> <span class="o">:</span> <span class="n">has_one</span> <span class="n">X</span><span class="o">}</span> <span class="o">{</span><span class="n">m₂</span> <span class="o">:</span> <span class="n">has_mul</span> <span class="n">X</span><span class="o">}</span> <span class="o">{</span><span class="n">e₂</span> <span class="o">:</span> <span class="n">has_one</span> <span class="n">X</span><span class="o">}</span>
<span class="kn">variables</span> <span class="o">(</span><span class="n">h₁</span> <span class="o">:</span> <span class="bp">@</span><span class="n">is_unital</span> <span class="n">X</span> <span class="n">m₁</span> <span class="n">e₁</span><span class="o">)</span> <span class="o">(</span><span class="n">h₂</span> <span class="o">:</span> <span class="bp">@</span><span class="n">is_unital</span> <span class="n">X</span> <span class="n">m₂</span> <span class="n">e₂</span><span class="o">)</span>
<span class="kn">variables</span> <span class="o">(</span><span class="n">distrib</span> <span class="o">:</span> <span class="bp">∀</span> <span class="n">a</span> <span class="n">b</span> <span class="n">c</span> <span class="n">d</span><span class="o">,</span> <span class="o">((</span><span class="n">a</span> <span class="bp">&lt;</span><span class="n">m₂</span><span class="bp">&gt;</span> <span class="n">b</span><span class="o">)</span> <span class="bp">&lt;</span><span class="n">m₁</span><span class="bp">&gt;</span> <span class="o">(</span><span class="n">c</span> <span class="bp">&lt;</span><span class="n">m₂</span><span class="bp">&gt;</span> <span class="n">d</span><span class="o">))</span> <span class="bp">=</span> <span class="o">((</span><span class="n">a</span> <span class="bp">&lt;</span><span class="n">m₁</span><span class="bp">&gt;</span> <span class="n">c</span><span class="o">)</span> <span class="bp">&lt;</span><span class="n">m₂</span><span class="bp">&gt;</span> <span class="o">(</span><span class="n">b</span> <span class="bp">&lt;</span><span class="n">m₁</span><span class="bp">&gt;</span> <span class="n">d</span><span class="o">)))</span>
<span class="n">include</span> <span class="n">h₁</span> <span class="n">h₂</span> <span class="n">distrib</span>

<span class="kn">lemma</span> <span class="n">one</span> <span class="o">:</span> <span class="o">(</span><span class="n">e₁</span><span class="bp">.</span><span class="n">one</span> <span class="bp">=</span> <span class="n">e₂</span><span class="bp">.</span><span class="n">one</span><span class="o">)</span> <span class="o">:=</span>
<span class="k">by</span> <span class="n">simpa</span> <span class="kn">using</span> <span class="n">distrib</span> <span class="n">e₂</span><span class="bp">.</span><span class="n">one</span> <span class="n">e₁</span><span class="bp">.</span><span class="n">one</span> <span class="n">e₁</span><span class="bp">.</span><span class="n">one</span> <span class="n">e₂</span><span class="bp">.</span><span class="n">one</span>

<span class="kn">lemma</span> <span class="n">mul</span> <span class="o">:</span> <span class="o">(</span><span class="n">m₁</span><span class="bp">.</span><span class="n">mul</span> <span class="bp">=</span> <span class="n">m₂</span><span class="bp">.</span><span class="n">mul</span><span class="o">)</span> <span class="o">:=</span>
<span class="k">by</span> <span class="n">funext</span> <span class="n">a</span> <span class="n">b</span><span class="bp">;</span> <span class="k">have</span> <span class="o">:=</span> <span class="n">distrib</span> <span class="n">a</span> <span class="n">e₁</span><span class="bp">.</span><span class="n">one</span> <span class="n">e₁</span><span class="bp">.</span><span class="n">one</span> <span class="n">b</span><span class="bp">;</span>
<span class="n">simp</span> <span class="n">at</span> <span class="n">this</span><span class="bp">;</span> <span class="n">simpa</span> <span class="o">[</span><span class="n">one</span> <span class="n">h₁</span> <span class="n">h₂</span> <span class="n">distrib</span><span class="o">]</span> <span class="kn">using</span> <span class="n">this</span>

<span class="kn">lemma</span> <span class="n">mul_comm</span> <span class="o">:</span> <span class="n">is_commutative</span> <span class="bp">_</span> <span class="n">m₂</span><span class="bp">.</span><span class="n">mul</span> <span class="o">:=</span>
<span class="bp">⟨λ</span> <span class="n">a</span> <span class="n">b</span><span class="o">,</span> <span class="k">by</span> <span class="n">simpa</span> <span class="o">[</span><span class="n">mul</span> <span class="n">h₁</span> <span class="n">h₂</span> <span class="n">distrib</span><span class="o">]</span> <span class="kn">using</span> <span class="n">distrib</span> <span class="n">e₂</span><span class="bp">.</span><span class="n">one</span> <span class="n">a</span> <span class="n">b</span> <span class="n">e₂</span><span class="bp">.</span><span class="n">one</span><span class="bp">⟩</span>

<span class="kn">lemma</span> <span class="n">mul_assoc</span> <span class="o">:</span> <span class="n">is_associative</span> <span class="bp">_</span> <span class="n">m₂</span><span class="bp">.</span><span class="n">mul</span> <span class="o">:=</span>
<span class="bp">⟨λ</span> <span class="n">a</span> <span class="n">b</span> <span class="n">c</span><span class="o">,</span> <span class="k">by</span> <span class="n">simpa</span> <span class="o">[</span><span class="n">mul</span> <span class="n">h₁</span> <span class="n">h₂</span> <span class="n">distrib</span><span class="o">]</span> <span class="kn">using</span> <span class="n">distrib</span> <span class="n">a</span> <span class="n">b</span> <span class="n">e₂</span><span class="bp">.</span><span class="n">one</span> <span class="n">c</span><span class="bp">⟩</span>

<span class="kn">instance</span> <span class="o">:</span> <span class="n">comm_monoid</span> <span class="n">X</span> <span class="o">:=</span>
<span class="o">{</span> <span class="n">mul_comm</span> <span class="o">:=</span> <span class="o">(</span><span class="n">mul_comm</span> <span class="n">h₁</span> <span class="n">h₂</span> <span class="n">distrib</span><span class="o">)</span><span class="bp">.</span><span class="n">comm</span><span class="o">,</span>
  <span class="n">mul_assoc</span> <span class="o">:=</span> <span class="o">(</span><span class="n">mul_assoc</span> <span class="n">h₁</span> <span class="n">h₂</span> <span class="n">distrib</span><span class="o">)</span><span class="bp">.</span><span class="n">assoc</span><span class="o">,</span>
  <span class="bp">..</span><span class="n">m₂</span><span class="o">,</span> <span class="bp">..</span><span class="n">e₂</span><span class="o">,</span> <span class="bp">..</span><span class="n">h₂</span> <span class="o">}</span>

<span class="kn">end</span> <span class="n">eckmann_hilton</span>
</pre></div>

#### [ Johan Commelin (Sep 07 2018 at 11:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subst%20at%20hyp/near/133498562):
<p>Well done!</p>

#### [ Johan Commelin (Sep 07 2018 at 11:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subst%20at%20hyp/near/133498636):
<p><span class="user-mention" data-user-id="110064">@Kenny Lau</span> <a href="https://gist.github.com/jcommelin/2e031b5446ca54089576ea9f66f12abf" target="_blank" title="https://gist.github.com/jcommelin/2e031b5446ca54089576ea9f66f12abf">https://gist.github.com/jcommelin/2e031b5446ca54089576ea9f66f12abf</a><br>
I added your name.</p>

#### [ Kenny Lau (Sep 07 2018 at 11:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subst%20at%20hyp/near/133498642):
<p>lol</p>


{% endraw %}
