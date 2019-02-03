---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/54140gettingPRsmerged.html
---

## Stream: [general](index.html)
### Topic: [getting PRs merged](54140gettingPRsmerged.html)

---


{% raw %}
#### [ Johan Commelin (Dec 17 2018 at 14:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/getting%20PRs%20merged/near/152025635):
<p><span class="user-mention" data-user-id="110049">@Mario Carneiro</span> <span class="user-mention" data-user-id="110294">@Johannes Hölzl</span> Is there anything we can do so that a bunch of PRs get merged before the Christmas break? Merging these PRs would mean that we can spend our Christmas holidays on interesting maths stuff, instead of boring parties with food and fire crackers...</p>

#### [ Johan Commelin (Dec 17 2018 at 15:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/getting%20PRs%20merged/near/152030063):
<p>Yuchai! We're down to 29!</p>

#### [ Kenny Lau (Dec 17 2018 at 15:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/getting%20PRs%20merged/near/152030287):
<p>:o</p>

#### [ Mario Carneiro (Dec 17 2018 at 15:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/getting%20PRs%20merged/near/152030337):
<p>...and now mathlib is broken</p>

#### [ Kenny Lau (Dec 17 2018 at 15:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/getting%20PRs%20merged/near/152030342):
<p>:o</p>

#### [ Mario Carneiro (Dec 17 2018 at 15:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/getting%20PRs%20merged/near/152030494):
<p>oh, I think it was the <code>squeeze_simp</code> PR</p>

#### [ Mario Carneiro (Dec 17 2018 at 15:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/getting%20PRs%20merged/near/152030509):
<p><span class="user-mention" data-user-id="112680">@Johan Commelin</span> did you actually check that your import works?</p>

#### [ Johan Commelin (Dec 17 2018 at 15:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/getting%20PRs%20merged/near/152030593):
<p>Hmm, it looked like it, but I didn't do a full compile.</p>

#### [ Johan Commelin (Dec 17 2018 at 15:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/getting%20PRs%20merged/near/152030604):
<p>Can you revert that commit?</p>

#### [ Johan Commelin (Dec 17 2018 at 15:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/getting%20PRs%20merged/near/152030611):
<p>Then I will do a more careful check.</p>

#### [ Johan Commelin (Dec 17 2018 at 15:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/getting%20PRs%20merged/near/152030618):
<p>Sorry for the mess.</p>

#### [ Chris Hughes (Dec 17 2018 at 15:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/getting%20PRs%20merged/near/152030659):
<p>I think it's a cyclic import</p>

#### [ Chris Hughes (Dec 17 2018 at 15:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/getting%20PRs%20merged/near/152030670):
<p>Maybe two PRs added imports somewhere</p>

#### [ Mario Carneiro (Dec 17 2018 at 15:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/getting%20PRs%20merged/near/152030803):
<p><code>tactic.squeeze</code> imports <code>meta.rb_map</code> which imports <code>data.option</code> which imports <code>tactic.interactive</code></p>

#### [ Kenny Lau (Dec 17 2018 at 15:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/getting%20PRs%20merged/near/152030821):
<p>where's the cycle?</p>

#### [ Chris Hughes (Dec 17 2018 at 15:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/getting%20PRs%20merged/near/152030930):
<p><code>tactic.interactive</code> imports <code>tactic.squeeze</code></p>

#### [ Kenny Lau (Dec 17 2018 at 15:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/getting%20PRs%20merged/near/152030940):
<p>why would it...</p>

#### [ Johan Commelin (Dec 17 2018 at 15:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/getting%20PRs%20merged/near/152031077):
<p>Because then it makes it a lot easier for mere mortals to squeeze their simps. Would save you a lot of work.</p>

#### [ Johan Commelin (Dec 17 2018 at 15:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/getting%20PRs%20merged/near/152032030):
<p><span class="user-mention" data-user-id="110049">@Mario Carneiro</span> Do you want me to PR a reverting commit?</p>

#### [ Mario Carneiro (Dec 17 2018 at 15:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/getting%20PRs%20merged/near/152032040):
<p>no, I'm working on it</p>

#### [ Kenny Lau (Dec 17 2018 at 15:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/getting%20PRs%20merged/near/152032050):
<p>thanks <span class="user-mention" data-user-id="110049">@Mario Carneiro</span></p>

#### [ Johan Commelin (Dec 17 2018 at 15:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/getting%20PRs%20merged/near/152032234):
<p>I can make <code>data.option</code> work without <code>tactic.interactive</code>, it just used two <code>simpa</code>s</p>

#### [ Johan Commelin (Dec 17 2018 at 15:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/getting%20PRs%20merged/near/152032244):
<p>But there is another cycle.</p>

#### [ Johan Commelin (Dec 17 2018 at 15:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/getting%20PRs%20merged/near/152032277):
<p><code>category.traversable.instances</code> imports <code>-- import data.list.basic data.set.lattice</code></p>

#### [ Johan Commelin (Dec 17 2018 at 15:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/getting%20PRs%20merged/near/152032305):
<p>It needs those for</p>
<div class="codehilite"><pre><span></span><span class="kn">lemma</span> <span class="n">mem_traverse</span> <span class="o">{</span><span class="n">f</span> <span class="o">:</span> <span class="n">α&#39;</span> <span class="bp">→</span> <span class="n">set</span> <span class="n">β&#39;</span><span class="o">}</span> <span class="o">:</span>
  <span class="bp">∀</span><span class="o">(</span><span class="n">l</span> <span class="o">:</span> <span class="n">list</span> <span class="n">α&#39;</span><span class="o">)</span> <span class="o">(</span><span class="n">n</span> <span class="o">:</span> <span class="n">list</span> <span class="n">β&#39;</span><span class="o">),</span> <span class="n">n</span> <span class="err">∈</span> <span class="n">traverse</span> <span class="n">f</span> <span class="n">l</span> <span class="bp">↔</span> <span class="n">forall₂</span> <span class="o">(</span><span class="bp">λ</span><span class="n">b</span> <span class="n">a</span><span class="o">,</span> <span class="n">b</span> <span class="err">∈</span> <span class="n">f</span> <span class="n">a</span><span class="o">)</span> <span class="n">n</span> <span class="n">l</span>
<span class="bp">|</span> <span class="o">[]</span>      <span class="o">[]</span>      <span class="o">:=</span> <span class="k">by</span> <span class="n">simp</span>
<span class="bp">|</span> <span class="o">(</span><span class="n">a</span><span class="bp">::</span><span class="n">as</span><span class="o">)</span> <span class="o">[]</span>      <span class="o">:=</span> <span class="k">by</span> <span class="n">simp</span><span class="bp">;</span> <span class="n">exact</span> <span class="k">assume</span> <span class="n">h</span><span class="o">,</span> <span class="k">match</span> <span class="n">h</span> <span class="k">with</span> <span class="kn">end</span>
<span class="bp">|</span> <span class="o">[]</span>      <span class="o">(</span><span class="n">b</span><span class="bp">::</span><span class="n">bs</span><span class="o">)</span> <span class="o">:=</span> <span class="k">by</span> <span class="n">simp</span>
<span class="bp">|</span> <span class="o">(</span><span class="n">a</span><span class="bp">::</span><span class="n">as</span><span class="o">)</span> <span class="o">(</span><span class="n">b</span><span class="bp">::</span><span class="n">bs</span><span class="o">)</span> <span class="o">:=</span>
  <span class="n">suffices</span> <span class="o">(</span><span class="n">b</span> <span class="bp">::</span> <span class="n">bs</span> <span class="o">:</span> <span class="n">list</span> <span class="n">β&#39;</span><span class="o">)</span> <span class="err">∈</span> <span class="n">traverse</span> <span class="n">f</span> <span class="o">(</span><span class="n">a</span> <span class="bp">::</span> <span class="n">as</span><span class="o">)</span> <span class="bp">↔</span> <span class="n">b</span> <span class="err">∈</span> <span class="n">f</span> <span class="n">a</span> <span class="bp">∧</span> <span class="n">bs</span> <span class="err">∈</span> <span class="n">traverse</span> <span class="n">f</span> <span class="n">as</span><span class="o">,</span>
    <span class="k">by</span> <span class="n">simpa</span> <span class="o">[</span><span class="n">mem_traverse</span> <span class="n">as</span> <span class="n">bs</span><span class="o">],</span>
  <span class="n">iff</span><span class="bp">.</span><span class="n">intro</span>
    <span class="o">(</span><span class="k">assume</span> <span class="bp">⟨_</span><span class="o">,</span> <span class="bp">⟨</span><span class="n">b</span><span class="o">,</span> <span class="n">hb</span><span class="o">,</span> <span class="n">rfl</span><span class="bp">⟩</span><span class="o">,</span> <span class="bp">_</span><span class="o">,</span> <span class="n">hl</span><span class="o">,</span> <span class="n">rfl</span><span class="bp">⟩</span><span class="o">,</span> <span class="bp">⟨</span><span class="n">hb</span><span class="o">,</span> <span class="n">hl</span><span class="bp">⟩</span><span class="o">)</span>
    <span class="o">(</span><span class="k">assume</span> <span class="bp">⟨</span><span class="n">hb</span><span class="o">,</span> <span class="n">hl</span><span class="bp">⟩</span><span class="o">,</span> <span class="bp">⟨_</span><span class="o">,</span> <span class="bp">⟨</span><span class="n">b</span><span class="o">,</span> <span class="n">hb</span><span class="o">,</span> <span class="n">rfl</span><span class="bp">⟩</span><span class="o">,</span> <span class="bp">_</span><span class="o">,</span> <span class="n">hl</span><span class="o">,</span> <span class="n">rfl</span><span class="bp">⟩</span><span class="o">)</span>
</pre></div>

#### [ Johan Commelin (Dec 17 2018 at 15:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/getting%20PRs%20merged/near/152032361):
<p>If we kick that to another file, it seems that the world would be happy again.</p>

#### [ Johan Commelin (Dec 17 2018 at 15:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/getting%20PRs%20merged/near/152032457):
<p>Once again, I apologize for breaking stuff. I'll take this as a lesson that I shouldn't lightly PR things that are low in the dependency chain...</p>

#### [ Johan Commelin (Dec 17 2018 at 15:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/getting%20PRs%20merged/near/152032612):
<p>Aahrg... it's even worse. <code>tactic.squeeze</code> depends on <code>simpa</code> (of course <span class="emoji emoji-1f926" title="face palm">:face_palm:</span>).</p>

#### [ Johan Commelin (Dec 17 2018 at 18:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/getting%20PRs%20merged/near/152044631):
<p><span class="user-mention" data-user-id="110049">@Mario Carneiro</span> Thanks for all the merges! And thanks for fixing what I broke. <span class="emoji emoji-1f64f" title="thank you">:thank_you:</span> <span class="emoji emoji-1f44d" title="thumbs up">:thumbs_up:</span> <span class="emoji emoji-1f389" title="tada">:tada:</span></p>


{% endraw %}
