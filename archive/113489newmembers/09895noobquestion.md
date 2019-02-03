---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113489newmembers/09895noobquestion.html
---

## Stream: [new members](https://leanprover-community.github.io/archive/113489newmembers/index.html)
### Topic: [noob question](https://leanprover-community.github.io/archive/113489newmembers/09895noobquestion.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Wojciech Nawrocki (Sep 04 2018 at 17:02)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/noob%20question/near/133315850):
<p>Hello! Very new to Lean and logic in general;  i'm interested in how i can find the function names that i might need for various deduction steps (e.g. <code>and.intro</code>), since the std/maths library sections of "theorem proving in lean" are empty <span class="emoji emoji-1f627" title="anguished">:anguished:</span> in particular, i want to go from <code>¬p → false</code> to <code>p</code></p>

#### [ Patrick Massot (Sep 04 2018 at 17:04)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/noob%20question/near/133316001):
<p><a href="https://github.com/leanprover/lean/blob/master/library/init/classical.lean#L160" target="_blank" title="https://github.com/leanprover/lean/blob/master/library/init/classical.lean#L160">https://github.com/leanprover/lean/blob/master/library/init/classical.lean#L160</a></p>

#### [ Patrick Massot (Sep 04 2018 at 17:05)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/noob%20question/near/133316038):
<p>This is in directory init of the core library, so you don't have to import anything, but it's in namespace <code>classical</code> so you need either open the namespace or use the full name</p>

#### [ Johan Commelin (Sep 04 2018 at 17:05)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/noob%20question/near/133316044):
<p>Welcome to Lean! Figuring out the names of lemmas etc is still a bit of a dark art. Most of us are learning by asking lots of questions here. So feel free to ask more <span class="emoji emoji-1f603" title="smiley">:smiley:</span></p>

#### [ Patrick Massot (Sep 04 2018 at 17:06)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/noob%20question/near/133316100):
<p>Yes, welcome, and don't let constructivist Kenny scare you!</p>

#### [ Johan Commelin (Sep 04 2018 at 17:06)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/noob%20question/near/133316111):
<p>Also, don't mind about Kenny. He doesn't like the stuff in <code>classical.lean</code>. But he's a nice guy if you ignore that bit <span class="emoji emoji-1f923" title="rolling on the floor laughing">:rolling_on_the_floor_laughing:</span></p>

#### [ Bryan Gin-ge Chen (Sep 04 2018 at 17:08)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/noob%20question/near/133316199):
<p>See also <a href="http://avigad.github.io/logic_and_proof/classical_reasoning.html" target="_blank" title="http://avigad.github.io/logic_and_proof/classical_reasoning.html">this discussion in the book "Logic and Proof"</a>.</p>

#### [ Johan Commelin (Sep 04 2018 at 17:12)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/noob%20question/near/133316422):
<p>There's a subtle difference between constructive mathematics and constructive pedagogy.</p>

#### [ Rob Lewis (Sep 04 2018 at 17:16)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/noob%20question/near/133316638):
<p>But more generally, if you're looking for theorems that follow a particular pattern, you can try the <code>#find</code> command. e.g. </p>
<div class="codehilite"><pre><span></span><span class="kn">import</span> <span class="n">tactic</span><span class="bp">.</span><span class="n">find</span>
<span class="bp">#</span><span class="n">find</span>  <span class="o">(</span><span class="bp">¬</span> <span class="bp">_</span> <span class="bp">→</span> <span class="n">false</span><span class="o">)</span> <span class="bp">→</span> <span class="bp">_</span>
</pre></div>

#### [ Wojciech Nawrocki (Sep 04 2018 at 17:16)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/noob%20question/near/133316668):
<p>Oh, that book looks great, maybe it should also be visible in the "Documentation" section of <a href="http://leanprover.github.io" target="_blank" title="http://leanprover.github.io">leanprover.github.io</a> . I'll definitely give it a go! I came across this while trying to prove de morgan both ways, and turns out classical is indeed required :) <a href="https://math.stackexchange.com/questions/120187/do-de-morgans-laws-hold-in-propositional-intuitionistic-logic" target="_blank" title="https://math.stackexchange.com/questions/120187/do-de-morgans-laws-hold-in-propositional-intuitionistic-logic">https://math.stackexchange.com/questions/120187/do-de-morgans-laws-hold-in-propositional-intuitionistic-logic</a></p>

#### [ Johan Commelin (Sep 04 2018 at 17:17)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/noob%20question/near/133316690):
<p>You can PR that book to the documentation of mathlib, if you want (-;</p>

#### [ Wojciech Nawrocki (Sep 04 2018 at 17:56)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/noob%20question/near/133319056):
<p>How horrible is this proof? <span class="emoji emoji-1f61b" title="mischievous">:mischievous:</span></p>
<div class="codehilite"><pre><span></span><span class="kn">variables</span> <span class="n">p</span> <span class="n">q</span> <span class="o">:</span> <span class="kt">Prop</span>

<span class="kn">theorem</span> <span class="n">de_morgan_1_a</span> <span class="o">(</span><span class="n">hnpnq</span><span class="o">:</span> <span class="bp">¬</span><span class="n">p</span> <span class="bp">∨</span> <span class="bp">¬</span><span class="n">q</span><span class="o">):</span> <span class="bp">¬</span><span class="o">(</span><span class="n">p</span> <span class="bp">∧</span> <span class="n">q</span><span class="o">)</span> <span class="o">:=</span>
  <span class="k">assume</span> <span class="o">(</span><span class="n">hpq</span><span class="o">:</span> <span class="n">p</span> <span class="bp">∧</span> <span class="n">q</span><span class="o">),</span>
  <span class="n">or</span><span class="bp">.</span><span class="n">elim</span> <span class="n">hnpnq</span>
    <span class="o">(</span><span class="k">assume</span> <span class="n">hnp</span><span class="o">:</span> <span class="bp">¬</span><span class="n">p</span><span class="o">,</span>
      <span class="k">show</span> <span class="n">false</span><span class="o">,</span> <span class="k">from</span> <span class="n">hnp</span> <span class="n">hpq</span><span class="bp">.</span><span class="n">left</span><span class="o">)</span>
    <span class="o">(</span><span class="k">assume</span> <span class="n">hnq</span><span class="o">:</span> <span class="bp">¬</span><span class="n">q</span><span class="o">,</span>
      <span class="k">show</span> <span class="n">false</span><span class="o">,</span> <span class="k">from</span> <span class="n">hnq</span> <span class="n">hpq</span><span class="bp">.</span><span class="n">right</span><span class="o">)</span>

<span class="c1">-- only provable within classical logic!</span>
<span class="kn">theorem</span> <span class="n">de_morgan_1_b</span> <span class="o">(</span><span class="n">hnpq</span><span class="o">:</span> <span class="bp">¬</span><span class="o">(</span><span class="n">p</span> <span class="bp">∧</span> <span class="n">q</span><span class="o">)):</span> <span class="bp">¬</span><span class="n">p</span> <span class="bp">∨</span> <span class="bp">¬</span><span class="n">q</span> <span class="o">:=</span>
  <span class="n">classical</span><span class="bp">.</span><span class="n">by_contradiction</span>
    <span class="o">(</span><span class="k">assume</span> <span class="n">not_conclusion</span><span class="o">:</span> <span class="bp">¬</span><span class="o">(</span><span class="bp">¬</span><span class="n">p</span> <span class="bp">∨</span> <span class="bp">¬</span><span class="n">q</span><span class="o">),</span>
      <span class="k">have</span> <span class="n">hpq</span><span class="o">:</span> <span class="n">p</span> <span class="bp">∧</span> <span class="n">q</span><span class="o">,</span> <span class="k">from</span> <span class="n">and</span><span class="bp">.</span><span class="n">intro</span>
        <span class="o">(</span><span class="k">show</span> <span class="n">p</span><span class="o">,</span> <span class="k">from</span> <span class="n">classical</span><span class="bp">.</span><span class="n">by_contradiction</span>
          <span class="o">(</span><span class="k">assume</span> <span class="n">hnp</span><span class="o">:</span> <span class="bp">¬</span><span class="n">p</span><span class="o">,</span>
            <span class="n">not_conclusion</span> <span class="o">(</span><span class="k">show</span> <span class="bp">¬</span><span class="n">p</span> <span class="bp">∨</span> <span class="bp">¬</span><span class="n">q</span><span class="o">,</span> <span class="k">from</span> <span class="n">or</span><span class="bp">.</span><span class="n">intro_left</span> <span class="o">(</span><span class="bp">¬</span><span class="n">q</span><span class="o">)</span> <span class="n">hnp</span><span class="o">)))</span>
        <span class="o">(</span><span class="k">show</span> <span class="n">q</span><span class="o">,</span> <span class="k">from</span> <span class="n">classical</span><span class="bp">.</span><span class="n">by_contradiction</span>
          <span class="o">(</span><span class="k">assume</span> <span class="n">hnq</span><span class="o">:</span> <span class="bp">¬</span><span class="n">q</span><span class="o">,</span>
            <span class="n">not_conclusion</span> <span class="o">(</span><span class="k">show</span> <span class="bp">¬</span><span class="n">p</span> <span class="bp">∨</span> <span class="bp">¬</span><span class="n">q</span><span class="o">,</span> <span class="k">from</span> <span class="n">or</span><span class="bp">.</span><span class="n">intro_right</span> <span class="o">(</span><span class="bp">¬</span><span class="n">p</span><span class="o">)</span> <span class="n">hnq</span><span class="o">))),</span>
      <span class="k">show</span> <span class="n">false</span><span class="o">,</span> <span class="k">from</span> <span class="n">hnpq</span> <span class="n">hpq</span><span class="o">)</span>

<span class="kn">theorem</span> <span class="n">de_morgan_1</span><span class="o">:</span> <span class="bp">¬</span><span class="o">(</span><span class="n">p</span> <span class="bp">∧</span> <span class="n">q</span><span class="o">)</span> <span class="bp">↔</span> <span class="bp">¬</span><span class="n">p</span> <span class="bp">∨</span> <span class="bp">¬</span><span class="n">q</span> <span class="o">:=</span>
  <span class="c1">-- annpoying having to specify p and q</span>
  <span class="n">iff</span><span class="bp">.</span><span class="n">intro</span> <span class="o">(</span><span class="n">de_morgan_1_b</span> <span class="n">p</span> <span class="n">q</span><span class="o">)</span> <span class="o">(</span><span class="n">de_morgan_1_a</span> <span class="n">p</span> <span class="n">q</span><span class="o">)</span>
</pre></div>

#### [ Kenny Lau (Sep 04 2018 at 18:03)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/noob%20question/near/133319479):
<p>it's alright</p>

#### [ Bryan Gin-ge Chen (Sep 04 2018 at 18:05)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/noob%20question/near/133319596):
<p>In the last theorem, you can use underscores instead of p's and q's if you want.</p>

#### [ Kevin Buzzard (Sep 04 2018 at 18:06)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/noob%20question/near/133319665):
<p>It's so much easier and nicer to do it in tactic mode if you're going to spell it all out like this:</p>
<div class="codehilite"><pre><span></span><span class="kn">variables</span> <span class="n">p</span> <span class="n">q</span> <span class="o">:</span> <span class="kt">Prop</span>

<span class="kn">theorem</span> <span class="n">de_morgan_1_a</span> <span class="o">(</span><span class="n">hnpnq</span><span class="o">:</span> <span class="bp">¬</span><span class="n">p</span> <span class="bp">∨</span> <span class="bp">¬</span><span class="n">q</span><span class="o">):</span> <span class="bp">¬</span><span class="o">(</span><span class="n">p</span> <span class="bp">∧</span> <span class="n">q</span><span class="o">)</span> <span class="o">:=</span>
<span class="k">begin</span>
  <span class="n">intro</span> <span class="n">hpq</span><span class="o">,</span>
  <span class="n">cases</span> <span class="n">hnpnq</span> <span class="k">with</span> <span class="n">hnp</span> <span class="n">hnq</span><span class="o">,</span>
  <span class="o">{</span> <span class="n">apply</span> <span class="n">hnp</span><span class="o">,</span>
    <span class="n">exact</span> <span class="n">hpq</span><span class="bp">.</span><span class="n">left</span><span class="o">},</span>
  <span class="o">{</span> <span class="n">apply</span> <span class="n">hnq</span><span class="o">,</span>
    <span class="n">exact</span> <span class="n">hpq</span><span class="bp">.</span><span class="n">right</span><span class="o">}</span>
<span class="kn">end</span>
</pre></div>

#### [ Kevin Buzzard (Sep 04 2018 at 18:06)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/noob%20question/near/133319673):
<p>You can see where you're going!</p>

#### [ Kevin Buzzard (Sep 04 2018 at 18:08)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/noob%20question/near/133319764):
<p>If you're going to do it in term mode you may as well just do</p>
<div class="codehilite"><pre><span></span><span class="kn">variables</span> <span class="n">p</span> <span class="n">q</span> <span class="o">:</span> <span class="kt">Prop</span>

<span class="kn">theorem</span> <span class="n">de_morgan_1_a</span> <span class="o">(</span><span class="n">hnpnq</span><span class="o">:</span> <span class="bp">¬</span><span class="n">p</span> <span class="bp">∨</span> <span class="bp">¬</span><span class="n">q</span><span class="o">):</span> <span class="bp">¬</span><span class="o">(</span><span class="n">p</span> <span class="bp">∧</span> <span class="n">q</span><span class="o">)</span> <span class="o">:=</span>
<span class="bp">λ</span> <span class="n">hpq</span><span class="o">,</span> <span class="n">or</span><span class="bp">.</span><span class="n">elim</span> <span class="n">hnpnq</span> <span class="o">(</span><span class="bp">λ</span> <span class="n">hnp</span><span class="o">,</span> <span class="n">hnp</span> <span class="n">hpq</span><span class="bp">.</span><span class="mi">1</span><span class="o">)</span> <span class="o">(</span><span class="bp">λ</span> <span class="n">hnq</span><span class="o">,</span> <span class="n">hnq</span> <span class="n">hpq</span><span class="bp">.</span><span class="mi">2</span><span class="o">)</span>
</pre></div>

#### [ Kenny Lau (Sep 04 2018 at 18:09)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/noob%20question/near/133319796):
<p>yeah but you've already known Lean for a year</p>

#### [ Kevin Buzzard (Sep 04 2018 at 18:11)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/noob%20question/near/133319938):
<p>Kenny can you golf <code>de_morgan_1_b</code>?</p>

#### [ Kevin Buzzard (Sep 04 2018 at 18:11)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/noob%20question/near/133319954):
<p>oh it will already be in mathlib I guess</p>

#### [ Wojciech Nawrocki (Sep 04 2018 at 18:15)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/noob%20question/near/133320201):
<p>Thanks for the feedback! Haven't quite grasped tactics yet, so doing things explicitly for now</p>

#### [ Kevin Buzzard (Sep 04 2018 at 18:17)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/noob%20question/near/133320295):
<p>tactics are the bomb if you're a learner. I don't know why they leave them so late in TPIL.</p>

#### [ Kevin Buzzard (Sep 04 2018 at 18:17)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/noob%20question/near/133320299):
<div class="codehilite"><pre><span></span><span class="kn">theorem</span> <span class="n">de_morgan_1_a</span> <span class="o">(</span><span class="n">hnpnq</span><span class="o">:</span> <span class="bp">¬</span><span class="n">p</span> <span class="bp">∨</span> <span class="bp">¬</span><span class="n">q</span><span class="o">):</span> <span class="bp">¬</span><span class="o">(</span><span class="n">p</span> <span class="bp">∧</span> <span class="n">q</span><span class="o">)</span>
<span class="bp">|</span> <span class="bp">⟨</span><span class="n">hp</span><span class="o">,</span> <span class="n">hq</span><span class="bp">⟩</span> <span class="o">:=</span> <span class="n">or</span><span class="bp">.</span><span class="n">elim</span> <span class="n">hnpnq</span> <span class="o">(</span><span class="n">absurd</span> <span class="n">hp</span><span class="o">)</span> <span class="o">(</span><span class="n">absurd</span> <span class="n">hq</span><span class="o">)</span>
</pre></div>


<p>Mathlib's proof.</p>

#### [ Kevin Buzzard (Sep 04 2018 at 18:17)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/noob%20question/near/133320304):
<p>Absolutely terrifying for beginners :-)</p>

#### [ Kevin Buzzard (Sep 04 2018 at 18:19)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/noob%20question/near/133320377):
<p>The theorem is supposed to be constructing a proof of false from a proof of <code>p and q</code>, so the equation compiler matches the proof of <code>p and q</code> with a proof of p and a proof of q and then it's pretty much the same as before.</p>

#### [ Kevin Buzzard (Sep 04 2018 at 18:21)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/noob%20question/near/133320508):
<p>re: specifying p and q. How about this?</p>
<div class="codehilite"><pre><span></span><span class="kn">variables</span> <span class="o">{</span><span class="n">p</span> <span class="n">q</span> <span class="o">:</span> <span class="kt">Prop</span><span class="o">}</span> <span class="c1">-- trick for making variables implicit</span>

<span class="kn">theorem</span> <span class="n">de_morgan_1_a</span> <span class="o">(</span><span class="n">hnpnq</span><span class="o">:</span> <span class="bp">¬</span><span class="n">p</span> <span class="bp">∨</span> <span class="bp">¬</span><span class="n">q</span><span class="o">):</span> <span class="bp">¬</span><span class="o">(</span><span class="n">p</span> <span class="bp">∧</span> <span class="n">q</span><span class="o">)</span> <span class="o">:=</span>
  <span class="k">assume</span> <span class="o">(</span><span class="n">hpq</span><span class="o">:</span> <span class="n">p</span> <span class="bp">∧</span> <span class="n">q</span><span class="o">),</span>
  <span class="n">or</span><span class="bp">.</span><span class="n">elim</span> <span class="n">hnpnq</span>
    <span class="o">(</span><span class="k">assume</span> <span class="n">hnp</span><span class="o">:</span> <span class="bp">¬</span><span class="n">p</span><span class="o">,</span>
      <span class="k">show</span> <span class="n">false</span><span class="o">,</span> <span class="k">from</span> <span class="n">hnp</span> <span class="n">hpq</span><span class="bp">.</span><span class="n">left</span><span class="o">)</span>
    <span class="o">(</span><span class="k">assume</span> <span class="n">hnq</span><span class="o">:</span> <span class="bp">¬</span><span class="n">q</span><span class="o">,</span>
      <span class="k">show</span> <span class="n">false</span><span class="o">,</span> <span class="k">from</span> <span class="n">hnq</span> <span class="n">hpq</span><span class="bp">.</span><span class="n">right</span><span class="o">)</span>

<span class="c1">-- only provable within classical logic!</span>
<span class="kn">theorem</span> <span class="n">de_morgan_1_b</span> <span class="o">(</span><span class="n">hnpq</span><span class="o">:</span> <span class="bp">¬</span><span class="o">(</span><span class="n">p</span> <span class="bp">∧</span> <span class="n">q</span><span class="o">)):</span> <span class="bp">¬</span><span class="n">p</span> <span class="bp">∨</span> <span class="bp">¬</span><span class="n">q</span> <span class="o">:=</span>
  <span class="n">classical</span><span class="bp">.</span><span class="n">by_contradiction</span>
    <span class="o">(</span><span class="k">assume</span> <span class="n">not_conclusion</span><span class="o">:</span> <span class="bp">¬</span><span class="o">(</span><span class="bp">¬</span><span class="n">p</span> <span class="bp">∨</span> <span class="bp">¬</span><span class="n">q</span><span class="o">),</span>
      <span class="k">have</span> <span class="n">hpq</span><span class="o">:</span> <span class="n">p</span> <span class="bp">∧</span> <span class="n">q</span><span class="o">,</span> <span class="k">from</span> <span class="n">and</span><span class="bp">.</span><span class="n">intro</span>
        <span class="o">(</span><span class="k">show</span> <span class="n">p</span><span class="o">,</span> <span class="k">from</span> <span class="n">classical</span><span class="bp">.</span><span class="n">by_contradiction</span>
          <span class="o">(</span><span class="k">assume</span> <span class="n">hnp</span><span class="o">:</span> <span class="bp">¬</span><span class="n">p</span><span class="o">,</span>
            <span class="n">not_conclusion</span> <span class="o">(</span><span class="k">show</span> <span class="bp">¬</span><span class="n">p</span> <span class="bp">∨</span> <span class="bp">¬</span><span class="n">q</span><span class="o">,</span> <span class="k">from</span> <span class="n">or</span><span class="bp">.</span><span class="n">intro_left</span> <span class="o">(</span><span class="bp">¬</span><span class="n">q</span><span class="o">)</span> <span class="n">hnp</span><span class="o">)))</span>
        <span class="o">(</span><span class="k">show</span> <span class="n">q</span><span class="o">,</span> <span class="k">from</span> <span class="n">classical</span><span class="bp">.</span><span class="n">by_contradiction</span>
          <span class="o">(</span><span class="k">assume</span> <span class="n">hnq</span><span class="o">:</span> <span class="bp">¬</span><span class="n">q</span><span class="o">,</span>
            <span class="n">not_conclusion</span> <span class="o">(</span><span class="k">show</span> <span class="bp">¬</span><span class="n">p</span> <span class="bp">∨</span> <span class="bp">¬</span><span class="n">q</span><span class="o">,</span> <span class="k">from</span> <span class="n">or</span><span class="bp">.</span><span class="n">intro_right</span> <span class="o">(</span><span class="bp">¬</span><span class="n">p</span><span class="o">)</span> <span class="n">hnq</span><span class="o">))),</span>
      <span class="k">show</span> <span class="n">false</span><span class="o">,</span> <span class="k">from</span> <span class="n">hnpq</span> <span class="n">hpq</span><span class="o">)</span>

<span class="kn">theorem</span> <span class="n">de_morgan_1</span><span class="o">:</span> <span class="bp">¬</span><span class="o">(</span><span class="n">p</span> <span class="bp">∧</span> <span class="n">q</span><span class="o">)</span> <span class="bp">↔</span> <span class="bp">¬</span><span class="n">p</span> <span class="bp">∨</span> <span class="bp">¬</span><span class="n">q</span> <span class="o">:=</span>
  <span class="c1">-- no longer annpoying</span>
  <span class="n">iff</span><span class="bp">.</span><span class="n">intro</span> <span class="o">(</span><span class="n">de_morgan_1_b</span><span class="o">)</span> <span class="o">(</span><span class="n">de_morgan_1_a</span><span class="o">)</span>
</pre></div>

#### [ Wojciech Nawrocki (Sep 04 2018 at 18:29)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/noob%20question/near/133320865):
<p>Oh, that's nice! I missed that they can be made implicit globally<br>
re: mathlib, i'll just quote TPIL: "Once again, you should exercise judgment as to whether such abbreviations enhance or diminish readability."</p>

#### [ Kevin Buzzard (Sep 04 2018 at 18:29)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/noob%20question/near/133320883):
<p>Instead of assuming classical logic, mathlib (in <code>logic/basic.lean</code>) just assumes decidability of <code>p</code>:</p>
<div class="codehilite"><pre><span></span><span class="kn">theorem</span> <span class="n">de_morgan_1_b</span> <span class="o">(</span><span class="n">hnpq</span><span class="o">:</span> <span class="bp">¬</span><span class="o">(</span><span class="n">p</span> <span class="bp">∧</span> <span class="n">q</span><span class="o">))</span> <span class="o">[</span><span class="n">decidable</span> <span class="n">p</span><span class="o">]</span> <span class="o">:</span> <span class="bp">¬</span><span class="n">p</span> <span class="bp">∨</span> <span class="bp">¬</span><span class="n">q</span> <span class="o">:=</span>
<span class="k">if</span> <span class="n">hp</span> <span class="o">:</span> <span class="n">p</span> <span class="k">then</span> <span class="n">or</span><span class="bp">.</span><span class="n">inr</span> <span class="o">(</span><span class="bp">λ</span> <span class="n">hq</span><span class="o">,</span> <span class="n">hnpq</span> <span class="bp">⟨</span><span class="n">hp</span><span class="o">,</span> <span class="n">hq</span><span class="bp">⟩</span><span class="o">)</span> <span class="k">else</span> <span class="n">or</span><span class="bp">.</span><span class="n">inl</span> <span class="n">hp</span>
</pre></div>

#### [ Kevin Buzzard (Sep 04 2018 at 18:29)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/noob%20question/near/133320908):
<p>my impression is that mathlib is not meant to be readable, they are looking for speed and breadth</p>

#### [ Wojciech Nawrocki (Sep 04 2018 at 18:41)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/noob%20question/near/133321554):
<p>Hm, more noob questions, what's the difference between classical logic and "decidable p"? Since LEM states that p is either true or false, isn't that effectively "p is decidable"?</p>

#### [ Kevin Buzzard (Sep 04 2018 at 18:42)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/noob%20question/near/133321628):
<p>Here's a classical proof.</p>
<div class="codehilite"><pre><span></span><span class="kn">theorem</span> <span class="n">de_morgan_1_b</span> <span class="o">(</span><span class="n">hnpq</span><span class="o">:</span> <span class="bp">¬</span><span class="o">(</span><span class="n">p</span> <span class="bp">∧</span> <span class="n">q</span><span class="o">))</span> <span class="o">:</span> <span class="bp">¬</span><span class="n">p</span> <span class="bp">∨</span> <span class="bp">¬</span><span class="n">q</span> <span class="o">:=</span>
<span class="n">or</span><span class="bp">.</span><span class="n">elim</span> <span class="o">(</span><span class="n">classical</span><span class="bp">.</span><span class="n">em</span> <span class="n">p</span><span class="o">)</span> <span class="o">(</span><span class="bp">λ</span> <span class="n">hp</span><span class="o">,</span> <span class="n">or</span><span class="bp">.</span><span class="n">inr</span> <span class="err">$</span> <span class="bp">λ</span> <span class="n">hq</span><span class="o">,</span> <span class="n">hnpq</span> <span class="bp">⟨</span><span class="n">hp</span><span class="o">,</span> <span class="n">hq</span><span class="bp">⟩</span><span class="o">)</span> <span class="n">or</span><span class="bp">.</span><span class="n">inl</span>
</pre></div>

#### [ Chris Hughes (Sep 04 2018 at 18:42)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/noob%20question/near/133321649):
<p>Not quite, em means you know p is either true or false, decidable means you know which one.</p>

#### [ Kevin Buzzard (Sep 04 2018 at 18:43)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/noob%20question/near/133321663):
<p>The classical proof gives this:</p>
<div class="codehilite"><pre><span></span><span class="bp">#</span><span class="kn">print</span> <span class="n">axioms</span> <span class="n">de_morgan_1_b</span>
<span class="c">/-</span><span class="cm"></span>
<span class="cm">classical.choice</span>
<span class="cm">quot.sound</span>
<span class="cm">propext</span>
<span class="cm">-/</span>
</pre></div>


<p>The decidable proof uses no "maths axioms"</p>

#### [ Kevin Buzzard (Sep 04 2018 at 18:44)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/noob%20question/near/133321725):
<p>As Chris says, assuming decidability is slightly stronger.  But to a mathematician like me they're all the same.</p>

#### [ Kevin Buzzard (Sep 04 2018 at 18:44)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/noob%20question/near/133321740):
<p>Furthermore they're all assumable without any worries :-)</p>

#### [ Kevin Buzzard (Sep 04 2018 at 18:45)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/noob%20question/near/133321778):
<p>Johannes Hoelzl once argued that trying to write as small proofs as possible was a good exercise.</p>

#### [ zaa (Sep 29 2018 at 22:35)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/noob%20question/near/134895335):
<p>Hello! Is there some way to use Lean without emacs or VisualStudio? Asking for CoqIde-like editor would be probably too much, but maybe there's some way to use Notepad or command line?</p>

#### [ Patrick Massot (Sep 29 2018 at 22:37)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/noob%20question/near/134895390):
<p>Sure, you can use command line, after editing your file in any editor you like</p>

#### [ Kenny Lau (Sep 29 2018 at 22:38)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/noob%20question/near/134895434):
<p>you can always use any editor to edit the file and then <code>lean --make</code> the file, although you won't be able to interact easilier</p>

#### [ Scott Olson (Sep 29 2018 at 22:38)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/noob%20question/near/134895437):
<p>In case you're not familiar, the Lean reference manual recommends use with Visual Studio Code, which is actually a completely separate IDE from Visual Studio, which is cross platform, simpler, etc. I personally find the experience using Lean in VSCode similar to using CoqIde</p>

#### [ Kenny Lau (Sep 29 2018 at 22:38)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/noob%20question/near/134895439):
<p>(why isn't easilier a word?)</p>

#### [ zaa (Sep 29 2018 at 22:40)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/noob%20question/near/134895493):
<p>Ok, then I will both try  Visual Studio Code and get used to <code>lean --make</code>.<br>
Thank you!</p>

#### [ Kevin Buzzard (Sep 29 2018 at 22:56)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/noob%20question/near/134895899):
<p>I'm not sure lean --make will be much fun, but I could imagine it would work. Two other possibilities are the Lean Web Editor, and CoCalc; these are both web-based ways to run Lean. I use unix and am quite anti-MS software in general (and they typically don't target my platform anyway) but actually I've had a very positive experience using VS code in linux. Emacs runs in a terminal window.</p>

#### [ zaa (Sep 29 2018 at 23:24)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/noob%20question/near/134896721):
<blockquote>
<p>Lean: Error: Command failed: lean --version 'lean' is not recognized as an internal or external command, operable program or batch file.</p>
</blockquote>
<p>Trying to run Lean extension in VSCode. I have added both necessary paths to PATH, but, it seems, i'm missing something else.</p>

#### [ Kenny Lau (Sep 29 2018 at 23:30)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/noob%20question/near/134896868):
<p>maybe you have a space in your path</p>

#### [ zaa (Sep 29 2018 at 23:41)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/noob%20question/near/134897137):
<p>It's working now, yay. I just closed and reopened VSCode.</p>

#### [ Chris Hughes (Sep 30 2018 at 00:08)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/noob%20question/near/134897811):
<blockquote>
<p>(why isn't easilier a word?)</p>
</blockquote>
<p>I think it's because it's an adverb not an adjective. Off the top of my head, I can't think of any English adverbs that can be suffixed with -er.</p>

#### [ zaa (Sep 30 2018 at 12:58)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/noob%20question/near/134918464):
<p>Does Lean have a tactic similar to Omega in coq?</p>

#### [ Kevin Buzzard (Sep 30 2018 at 13:01)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/noob%20question/near/134918538):
<p>I believe the answer is "not yet". I know nothing about Coq but I've heard people talk about Omega. Can you briefly describe what it does? Another noob question :-)</p>

#### [ Kevin Buzzard (Sep 30 2018 at 13:02)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/noob%20question/near/134918579):
<p>We have <code>linarith</code> and <code>cc</code>.</p>

#### [ Mario Carneiro (Sep 30 2018 at 13:05)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/noob%20question/near/134918645):
<p>I think omega is <code>cooper</code></p>

#### [ zaa (Sep 30 2018 at 13:07)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/noob%20question/near/134918695):
<p>It solves goals in Presburger arithmetic. Equalities containing only addition and substraction (and multiplication by constant, ofc).</p>
<p>For example: 8n = 4m+3 -&gt; False</p>

#### [ Mario Carneiro (Sep 30 2018 at 13:09)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/noob%20question/near/134918764):
<p>what do you use it for? is it just divisibility goals like that one?</p>

#### [ zaa (Sep 30 2018 at 13:11)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/noob%20question/near/134918822):
<p>Oh, it seems to work with inequalities too. Will test on Coq a bit, as I have already forgotten things.</p>

#### [ Mario Carneiro (Sep 30 2018 at 13:13)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/noob%20question/near/134918871):
<p>no, my question is when do you think "I should use omega"</p>

#### [ Mario Carneiro (Sep 30 2018 at 13:14)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/noob%20question/near/134918911):
<p>I know about presburger arithmetic but I think it's probably a bit too wide a target - I doubt people really need the crazy quantifier complexity part</p>

#### [ zaa (Sep 30 2018 at 13:17)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/noob%20question/near/134918966):
<p><a href="https://coq.inria.fr/refman/addendum/omega.html" target="_blank" title="https://coq.inria.fr/refman/addendum/omega.html">https://coq.inria.fr/refman/addendum/omega.html</a> - found the documentation.<br>
There's an example:<br>
z &gt; 0 -&gt; 2 * z + 1 &gt; z</p>
<p>As far as i can remember, I mostly used it for goals like<br>
[inequality/equality] -&gt; [another one] -&gt; x = something<br>
or A &lt;= x &lt;= B<br>
or maybe False</p>

#### [ Mario Carneiro (Sep 30 2018 at 13:18)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/noob%20question/near/134919013):
<p><code>cooper</code> is a tactic for presburger arithmetic written in lean by Seul Baek, but I don't think it is ready for production</p>

#### [ Kevin Buzzard (Sep 30 2018 at 14:12)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/noob%20question/near/134920434):
<blockquote>
<p><a href="https://coq.inria.fr/refman/addendum/omega.html" target="_blank" title="https://coq.inria.fr/refman/addendum/omega.html">https://coq.inria.fr/refman/addendum/omega.html</a> - found the documentation.</p>
</blockquote>
<p>Oh thank you! I know nothing about Coq or where to look for this stuff.</p>

#### [ zaa (Sep 30 2018 at 23:36)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/noob%20question/near/134936881):
<p>Yes, that's the website where it lives. I had fun with Coq for some time but paused it some year ago (will return to it soon, probably simultaneously to more serious lean learning).</p>

#### [ zaa (Sep 30 2018 at 23:51)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/noob%20question/near/134937308):
<p>Next noob question:<br>
Is there some simple example/tutorial of quotient types - how to define and use them?</p>

#### [ Reid Barton (Oct 01 2018 at 00:01)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/noob%20question/near/134937617):
<p>There is a section in TPIL: <a href="https://leanprover.github.io/theorem_proving_in_lean/axioms_and_computation.html#quotients" target="_blank" title="https://leanprover.github.io/theorem_proving_in_lean/axioms_and_computation.html#quotients">https://leanprover.github.io/theorem_proving_in_lean/axioms_and_computation.html#quotients</a></p>

#### [ Reid Barton (Oct 01 2018 at 00:05)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/noob%20question/near/134937730):
<p>For a real-world example you can take a look at <code>linear_algebra.quotient_module</code></p>

#### [ zaa (Oct 01 2018 at 00:06)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/noob%20question/near/134937793):
<p>Thank you!</p>

#### [ Kevin Buzzard (Oct 01 2018 at 01:00)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/noob%20question/near/134939308):
<p><a href="#narrow/stream/116395-maths/topic/teaching.20use.20of.20quotients.20in.20Lean" title="#narrow/stream/116395-maths/topic/teaching.20use.20of.20quotients.20in.20Lean">https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/teaching.20use.20of.20quotients.20in.20Lean</a></p>

#### [ Kevin Buzzard (Oct 01 2018 at 01:01)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/noob%20question/near/134939327):
<p>I wrote <a href="https://github.com/kbuzzard/xena/blob/master/xenalib/m1f/zmod37.lean" target="_blank" title="https://github.com/kbuzzard/xena/blob/master/xenalib/m1f/zmod37.lean">https://github.com/kbuzzard/xena/blob/master/xenalib/m1f/zmod37.lean</a> specifically to help some of my students to learn about using quotients in Lean.</p>

#### [ Wojciech Nawrocki (Oct 24 2018 at 20:40)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/noob%20question/near/136428236):
<p>Using my old thread for more noob questions:<br>
Can I use something like <code>cases</code> but without stating the hypothesis name? Namely, I'd like a tactic that splits conjunctions into two hypotheses and disjunctions into two goals. More generally, how does one go about searching for tactics that do something?</p>

#### [ Johan Commelin (Oct 24 2018 at 20:44)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/noob%20question/near/136428440):
<p><code>split</code> will split goals.</p>

#### [ Wojciech Nawrocki (Oct 24 2018 at 20:45)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/noob%20question/near/136428479):
<p>Yep, sorry I should've specified - I want to split hypotheses.</p>

#### [ Johan Commelin (Oct 24 2018 at 20:45)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/noob%20question/near/136428496):
<p>Like <code>have h1 := h.left, have h2 := h.right</code>?</p>

#### [ Johan Commelin (Oct 24 2018 at 20:46)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/noob%20question/near/136428503):
<p>And now you want to do that automatically for all hypotheses, recursively?</p>

#### [ Reid Barton (Oct 24 2018 at 20:46)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/noob%20question/near/136428549):
<p><code>cases</code> does both of those things already, so I guess you mean something that applies <code>cases</code> automatically?</p>

#### [ Wojciech Nawrocki (Oct 24 2018 at 20:46)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/noob%20question/near/136428563):
<p>Yep, that would be for ANDs, but without stating what the name is, and also do it for ORs (in which case two  or more goals would appear). Yep, automatically and recursively.</p>

#### [ Reid Barton (Oct 24 2018 at 20:47)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/noob%20question/near/136428584):
<p>I think the answer to the more general question is "read through <a href="https://github.com/leanprover/mathlib/blob/master/docs/tactics.md" target="_blank" title="https://github.com/leanprover/mathlib/blob/master/docs/tactics.md">https://github.com/leanprover/mathlib/blob/master/docs/tactics.md</a>, and then look through <code>tactic.interactive</code> in mathlib and more generally the rest of <code>tactic.*</code> to find more things"</p>

#### [ Reid Barton (Oct 24 2018 at 20:48)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/noob%20question/near/136428667):
<p><code>tidy</code> does things like this; it tries a bunch of different tactics in a loop, one of which is <code>auto_cases</code></p>

#### [ Wojciech Nawrocki (Oct 24 2018 at 20:51)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/noob%20question/near/136428862):
<p>That looks about right, thanks!</p>

#### [ Rob Lewis (Oct 24 2018 at 20:55)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/noob%20question/near/136429144):
<p><code>safe</code> will do this, and a bit more. I think it should be less aggressive than <code>tidy</code>.</p>

#### [ Wojciech Nawrocki (Oct 24 2018 at 21:25)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/noob%20question/near/136430875):
<p>Oh damn, it just solves everything by itself O.o</p>

#### [ Keeley Hoek (Oct 26 2018 at 09:54)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/noob%20question/near/136531665):
<p>c.f. <code>auto_cases</code></p>

#### [ Wojciech Nawrocki (Nov 03 2018 at 02:35)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/noob%20question/near/137094276):
<p>More questions!<br>
What's the syntax for matching on inductive constructors by name? E.g. for list, something like <code>Nil =&gt; 0, Cons(hd, tl) =&gt; 1 + (len tl)</code> would be a Rust way to define <code>len</code> recursively</p>

#### [ Bryan Gin-ge Chen (Nov 03 2018 at 02:56)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/noob%20question/near/137094949):
<p>Do you mean something like this?</p>
<div class="codehilite"><pre><span></span><span class="n">def</span> <span class="n">len</span> <span class="o">:</span> <span class="n">list</span> <span class="n">α</span> <span class="bp">→</span> <span class="bp">ℕ</span>
<span class="bp">|</span> <span class="n">list</span><span class="bp">.</span><span class="n">nil</span> <span class="o">:=</span> <span class="mi">0</span>
<span class="bp">|</span> <span class="o">(</span><span class="n">list</span><span class="bp">.</span><span class="n">cons</span> <span class="n">a</span> <span class="n">b</span><span class="o">)</span> <span class="o">:=</span> <span class="mi">1</span> <span class="bp">+</span> <span class="n">len</span> <span class="n">b</span>
</pre></div>

#### [ Wojciech Nawrocki (Nov 03 2018 at 03:00)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/noob%20question/near/137095066):
<p>Yep that's it - thanks!</p>

#### [ Wojciech Nawrocki (Nov 03 2018 at 18:16)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/noob%20question/near/137121205):
<p>Ignore me, mixed up my languages.</p>

#### [ Wojciech Nawrocki (Nov 03 2018 at 19:37)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/noob%20question/near/137123573):
<p>Is there any reason why <code>fin</code> and <code>multiset</code> don't support the <code>{1, 2, 3}</code> notation that <code>set</code> does? What's the best way to construct concrete <code>finset</code>s?</p>

#### [ Johan Commelin (Nov 03 2018 at 19:38)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/noob%20question/near/137123629):
<p>Do you want a type or a set?</p>

#### [ Chris Hughes (Nov 03 2018 at 19:40)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/noob%20question/near/137123686):
<p>You need <code>decidable_eq α</code> to use that notation for <code>finset α</code>.</p>

#### [ Chris Hughes (Nov 03 2018 at 19:41)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/noob%20question/near/137123713):
<p>For multisets this works for me without any decidability assumptions</p>
<div class="codehilite"><pre><span></span><span class="kn">example</span> <span class="o">{</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span><span class="bp">*</span><span class="o">}</span> <span class="o">(</span><span class="n">a</span> <span class="n">b</span> <span class="n">c</span> <span class="o">:</span> <span class="n">α</span><span class="o">)</span> <span class="o">:</span> <span class="n">multiset</span> <span class="n">α</span> <span class="o">:=</span> <span class="o">{</span><span class="n">a</span><span class="o">,</span><span class="n">b</span><span class="o">,</span><span class="n">c</span><span class="o">}</span>
</pre></div>

#### [ Wojciech Nawrocki (Nov 03 2018 at 19:42)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/noob%20question/near/137123720):
<p><span class="user-mention" data-user-id="112680">@Johan Commelin</span> a concrete set, say <code>{v}</code> for some given <code>v: \a</code><br>
<span class="user-mention" data-user-id="110044">@Chris Hughes</span> ah indeed, why does <code>set</code> not require it then?</p>

#### [ Chris Hughes (Nov 03 2018 at 19:45)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/noob%20question/near/137123840):
<p>They notation is for <code>has_insert.insert</code> <br>
For sets <code>insert a s := {b : α | b = a ∨ b ∈ s}</code>, and there's no decidable equality required.</p>
<p>For finsets, there has to be an underlying list with no duplicates, so it has to check whether <code>a</code> is already in the set, which requires <code>decidable_eq</code></p>

#### [ Wojciech Nawrocki (Nov 03 2018 at 20:33)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/noob%20question/near/137125503):
<p>Then given a singleton set, how can I extract the element? I tried folding it into a list to grab the first element, but <code>fold</code> requires commutativity and <code>list.append</code> is not commutative.</p>

#### [ Chris Hughes (Nov 03 2018 at 20:40)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/noob%20question/near/137125773):
<p>Do you have a proof that it's a singleton? I think there's a PR about finite unique computable choice.</p>

#### [ Wojciech Nawrocki (Nov 03 2018 at 20:42)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/noob%20question/near/137125848):
<p>Yeah, i'm grabbing it under the assumption that <code>card vals = 1</code>.</p>

#### [ Chris Hughes (Nov 03 2018 at 20:50)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/noob%20question/near/137126149):
<p>do you need it to be computable? You can use <code>finset.exists_mem_of_ne_empty</code> if you don't. Do you need the fact that everything in the singleton is equal?</p>

#### [ Wojciech Nawrocki (Nov 03 2018 at 21:09)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/noob%20question/near/137126804):
<p>I think <code>exists_mem_of_ne_empty</code> will work. thx!</p>

#### [ Wojciech Nawrocki (Nov 03 2018 at 21:29)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/noob%20question/near/137127553):
<p>So now i'm seeing a really strange error when trying to decompose the <code>Exists</code>:</p>
<div class="codehilite"><pre><span></span><span class="kn">constant</span> <span class="n">α</span><span class="o">:</span> <span class="kt">Type</span>
<span class="kn">constant</span> <span class="n">a</span><span class="o">:</span> <span class="n">α</span>
<span class="kn">constant</span> <span class="n">as</span><span class="o">:</span> <span class="n">finset</span> <span class="n">α</span>
<span class="bp">#</span><span class="kn">check</span> <span class="n">a</span> <span class="err">∈</span> <span class="n">as</span> <span class="c1">-- Prop</span>
<span class="kn">constant</span> <span class="n">ex</span> <span class="o">:</span> <span class="bp">∃</span> <span class="o">(</span><span class="n">a</span> <span class="o">:</span> <span class="n">α</span><span class="o">),</span> <span class="n">a</span> <span class="err">∈</span> <span class="n">as</span>
<span class="n">def</span> <span class="n">test</span> <span class="o">:=</span> <span class="k">match</span> <span class="n">ex</span> <span class="k">with</span> <span class="bp">⟨</span><span class="n">a</span><span class="o">,</span> <span class="n">b</span><span class="bp">⟩</span> <span class="o">:=</span> <span class="c1">-- induction tactic failed, recursor &#39;Exists.dcases_on&#39; can only eliminate into Prop</span>
  <span class="mi">0</span>
<span class="kn">end</span>
</pre></div>

#### [ Kevin Buzzard (Nov 03 2018 at 22:04)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/noob%20question/near/137128633):
<p>The recursor only eliminates into prop and your goal is a type</p>

#### [ Kevin Buzzard (Nov 03 2018 at 22:04)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/noob%20question/near/137128637):
<p>so the recursor cannot be applied</p>

#### [ Wojciech Nawrocki (Nov 03 2018 at 22:05)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/noob%20question/near/137128659):
<p>Yep, I just realised this. Basically, i'm trying to extract a concrete value of the type <code>\a</code> from a proof of existence. But I guess this could only work in purely constructionist logic?</p>

#### [ Kevin Buzzard (Nov 03 2018 at 22:06)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/noob%20question/near/137128709):
<p>There are tools in the classical namespace which should let you do this</p>

#### [ Kevin Buzzard (Nov 03 2018 at 22:07)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/noob%20question/near/137128711):
<p>You shouldn't use constants by the way, you should use variables -- they work a bit better and there's less risk</p>

#### [ Wojciech Nawrocki (Nov 03 2018 at 22:08)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/noob%20question/near/137128760):
<p>Oh yeah, that was just to make the example code short</p>

#### [ Chris Hughes (Nov 03 2018 at 22:09)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/noob%20question/near/137128774):
<p>It should be possible to define the function you want constructively, but it hasn't been done yet.</p>

#### [ Kevin Buzzard (Nov 03 2018 at 22:10)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/noob%20question/near/137128815):
<div class="codehilite"><pre><span></span><span class="kn">import</span> <span class="n">data</span><span class="bp">.</span><span class="n">finset</span>
<span class="kn">variable</span> <span class="o">{</span><span class="n">α</span><span class="o">:</span> <span class="kt">Type</span><span class="o">}</span>
<span class="kn">variable</span> <span class="o">{</span><span class="n">a</span><span class="o">:</span> <span class="n">α</span><span class="o">}</span>
<span class="kn">variable</span> <span class="o">{</span><span class="n">as</span><span class="o">:</span> <span class="n">finset</span> <span class="n">α</span><span class="o">}</span>
<span class="bp">#</span><span class="kn">check</span> <span class="n">a</span> <span class="err">∈</span> <span class="n">as</span> <span class="c1">-- Prop</span>
<span class="kn">variable</span> <span class="n">ex</span> <span class="o">:</span> <span class="bp">∃</span> <span class="o">(</span><span class="n">a</span> <span class="o">:</span> <span class="n">α</span><span class="o">),</span> <span class="n">a</span> <span class="err">∈</span> <span class="n">as</span>
<span class="n">noncomputable</span> <span class="n">def</span> <span class="n">test</span> <span class="o">:</span> <span class="n">α</span> <span class="o">:=</span> <span class="n">classical</span><span class="bp">.</span><span class="n">some</span> <span class="n">ex</span>
</pre></div>

#### [ Kevin Buzzard (Nov 03 2018 at 22:11)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/noob%20question/near/137128832):
<p>Right -- this noncomputable approach works for any existence statement. But I now understand that in the specific case of finsets you might be able to do better.</p>

#### [ Bryan Gin-ge Chen (Nov 03 2018 at 22:11)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/noob%20question/near/137128834):
<p><a href="https://github.com/leanprover/mathlib/pull/421" target="_blank" title="https://github.com/leanprover/mathlib/pull/421">This is the relevant PR</a>, right?</p>

#### [ Kevin Buzzard (Nov 03 2018 at 22:12)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/noob%20question/near/137128879):
<div class="codehilite"><pre><span></span><span class="kn">import</span> <span class="n">data</span><span class="bp">.</span><span class="n">finset</span>

<span class="kn">variables</span> <span class="o">{</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span><span class="o">}</span> <span class="o">{</span><span class="n">a</span> <span class="o">:</span> <span class="n">α</span><span class="o">}</span> <span class="o">{</span><span class="n">as</span> <span class="o">:</span> <span class="n">finset</span> <span class="n">α</span><span class="o">}</span> <span class="o">(</span><span class="n">ex</span> <span class="o">:</span> <span class="bp">∃</span> <span class="o">(</span><span class="n">a</span> <span class="o">:</span> <span class="n">α</span><span class="o">),</span> <span class="n">a</span> <span class="err">∈</span> <span class="n">as</span><span class="o">)</span>

<span class="n">noncomputable</span> <span class="n">def</span> <span class="n">test</span> <span class="o">:</span> <span class="n">α</span> <span class="o">:=</span> <span class="n">classical</span><span class="bp">.</span><span class="n">some</span> <span class="n">ex</span>
</pre></div>


<p>Shorter and no constants ;-)</p>

#### [ Wojciech Nawrocki (Nov 03 2018 at 22:17)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/noob%20question/near/137129014):
<p>Also works with <code>constants</code>, but fair enough :)<br>
Anyhow, I need it to be computable because I want to extract concrete elements from concrete sets and do things with them</p>

#### [ Kenny Lau (Nov 03 2018 at 22:39)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/noob%20question/near/137129717):
<p>something that almost works:</p>

#### [ Kenny Lau (Nov 03 2018 at 22:39)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/noob%20question/near/137129718):
<div class="codehilite"><pre><span></span><span class="kn">import</span> <span class="n">data</span><span class="bp">.</span><span class="n">finset</span>

<span class="kn">lemma</span> <span class="n">list</span><span class="bp">.</span><span class="n">perm_singleton</span> <span class="o">{</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span><span class="bp">*</span><span class="o">}</span> <span class="o">{</span><span class="n">L</span> <span class="o">:</span> <span class="n">list</span> <span class="n">α</span><span class="o">}</span> <span class="o">{</span><span class="n">x</span> <span class="o">:</span> <span class="n">α</span><span class="o">}</span> <span class="o">(</span><span class="n">H</span> <span class="o">:</span> <span class="n">L</span> <span class="bp">~</span> <span class="o">[</span><span class="n">x</span><span class="o">])</span> <span class="o">:</span> <span class="n">L</span> <span class="bp">=</span> <span class="o">[</span><span class="n">x</span><span class="o">]</span> <span class="o">:=</span>
<span class="k">begin</span>
  <span class="n">generalize_hyp</span> <span class="n">hs</span> <span class="o">:</span> <span class="o">[</span><span class="n">x</span><span class="o">]</span> <span class="bp">=</span> <span class="n">S</span> <span class="n">at</span> <span class="n">H</span> <span class="err">⊢</span><span class="o">,</span>
  <span class="n">induction</span> <span class="n">H</span><span class="o">,</span>
  <span class="n">case</span> <span class="n">list</span><span class="bp">.</span><span class="n">perm</span><span class="bp">.</span><span class="n">nil</span> <span class="o">{</span> <span class="n">refl</span> <span class="o">},</span>
  <span class="n">case</span> <span class="n">list</span><span class="bp">.</span><span class="n">perm</span><span class="bp">.</span><span class="n">skip</span> <span class="o">:</span> <span class="n">y</span> <span class="n">L₁</span> <span class="n">L₂</span> <span class="n">H</span> <span class="n">ih</span> <span class="o">{</span>
    <span class="n">cases</span> <span class="n">hs</span><span class="o">,</span> <span class="n">cases</span> <span class="n">list</span><span class="bp">.</span><span class="n">perm_nil</span><span class="bp">.</span><span class="mi">1</span> <span class="n">H</span><span class="o">,</span> <span class="n">refl</span>
  <span class="o">},</span>
  <span class="n">case</span> <span class="n">list</span><span class="bp">.</span><span class="n">perm</span><span class="bp">.</span><span class="n">swap</span> <span class="o">{</span> <span class="n">injections</span> <span class="o">},</span>
  <span class="n">case</span> <span class="n">list</span><span class="bp">.</span><span class="n">perm</span><span class="bp">.</span><span class="n">trans</span> <span class="o">:</span> <span class="n">L₁</span> <span class="n">L₂</span> <span class="n">L₃</span> <span class="n">H12</span> <span class="n">H23</span> <span class="n">ih1</span> <span class="n">ih2</span> <span class="o">{</span>
    <span class="n">cases</span> <span class="n">hs</span><span class="o">,</span> <span class="n">cases</span> <span class="n">ih2</span> <span class="n">rfl</span><span class="o">,</span> <span class="n">cases</span> <span class="n">ih1</span> <span class="n">rfl</span><span class="o">,</span> <span class="n">refl</span>
  <span class="o">}</span>
<span class="kn">end</span>

<span class="n">def</span> <span class="n">extract</span> <span class="o">{</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span><span class="bp">*</span><span class="o">}</span> <span class="o">(</span><span class="n">s</span> <span class="o">:</span> <span class="n">finset</span> <span class="n">α</span><span class="o">)</span> <span class="o">(</span><span class="n">hs</span> <span class="o">:</span> <span class="n">s</span><span class="bp">.</span><span class="n">card</span> <span class="bp">=</span> <span class="mi">1</span><span class="o">)</span> <span class="o">:</span> <span class="n">α</span> <span class="o">:=</span>
<span class="n">finset</span><span class="bp">.</span><span class="n">rec_on</span> <span class="n">s</span>
  <span class="o">(</span><span class="bp">λ</span> <span class="n">m</span><span class="o">,</span> <span class="n">quotient</span><span class="bp">.</span><span class="n">hrec_on</span> <span class="n">m</span>
    <span class="o">(</span><span class="bp">λ</span> <span class="n">L</span> <span class="bp">_</span><span class="o">,</span> <span class="n">list</span><span class="bp">.</span><span class="n">cases_on</span> <span class="n">L</span>
      <span class="o">(</span><span class="k">assume</span> <span class="n">hcard</span> <span class="o">:</span> <span class="mi">0</span> <span class="bp">=</span> <span class="mi">1</span><span class="o">,</span> <span class="n">absurd</span> <span class="n">hcard</span> <span class="n">dec_trivial</span><span class="o">)</span>
      <span class="o">(</span><span class="bp">λ</span> <span class="n">hd</span> <span class="n">tl</span> <span class="n">hcard</span><span class="o">,</span> <span class="n">hd</span><span class="o">))</span>
    <span class="o">(</span><span class="bp">λ</span> <span class="n">L₁</span> <span class="n">L₂</span> <span class="n">HL</span><span class="o">,</span> <span class="n">function</span><span class="bp">.</span><span class="n">hfunext</span> <span class="o">(</span><span class="n">congr_arg</span> <span class="bp">_</span> <span class="err">$</span> <span class="n">quotient</span><span class="bp">.</span><span class="n">sound</span> <span class="n">HL</span><span class="o">)</span> <span class="err">$</span>
    <span class="bp">λ</span> <span class="n">hnd1</span> <span class="n">hnd2</span> <span class="n">hheq</span><span class="o">,</span> <span class="k">begin</span>
  <span class="n">cases</span> <span class="n">L₂</span><span class="o">,</span>
  <span class="n">case</span> <span class="n">list</span><span class="bp">.</span><span class="n">nil</span> <span class="o">{</span> <span class="n">cases</span> <span class="n">list</span><span class="bp">.</span><span class="n">perm_nil</span><span class="bp">.</span><span class="mi">1</span> <span class="n">HL</span><span class="o">,</span> <span class="n">refl</span> <span class="o">},</span>
  <span class="n">case</span> <span class="n">list</span><span class="bp">.</span><span class="n">cons</span> <span class="o">:</span> <span class="n">hd₂</span> <span class="n">tl₂</span> <span class="o">{</span>
    <span class="n">cases</span> <span class="n">L₁</span><span class="o">,</span>
    <span class="n">case</span> <span class="n">list</span><span class="bp">.</span><span class="n">nil</span> <span class="o">{</span> <span class="n">cases</span> <span class="n">list</span><span class="bp">.</span><span class="n">perm_nil</span><span class="bp">.</span><span class="mi">1</span> <span class="o">(</span><span class="n">list</span><span class="bp">.</span><span class="n">perm</span><span class="bp">.</span><span class="n">symm</span> <span class="n">HL</span><span class="o">)</span> <span class="o">},</span>
    <span class="n">case</span> <span class="n">list</span><span class="bp">.</span><span class="n">cons</span> <span class="o">:</span> <span class="n">hd₁</span> <span class="n">tl₁</span> <span class="o">{</span>
      <span class="n">apply</span> <span class="n">function</span><span class="bp">.</span><span class="n">hfunext</span><span class="o">,</span>
      <span class="o">{</span> <span class="n">simp</span> <span class="n">only</span> <span class="o">[</span><span class="n">finset</span><span class="bp">.</span><span class="n">card_def</span><span class="o">,</span> <span class="n">multiset</span><span class="bp">.</span><span class="n">card</span><span class="o">],</span>
        <span class="n">rw</span> <span class="n">quotient</span><span class="bp">.</span><span class="n">sound</span> <span class="n">HL</span> <span class="o">},</span>
      <span class="n">intros</span> <span class="n">hcard₁</span> <span class="n">hcard₂</span> <span class="n">hheq</span><span class="o">,</span>
      <span class="n">cases</span> <span class="n">multiset</span><span class="bp">.</span><span class="n">card_eq_one</span><span class="bp">.</span><span class="mi">1</span> <span class="n">hcard₁</span> <span class="k">with</span> <span class="n">x₁</span> <span class="n">hx₁</span><span class="o">,</span>
      <span class="n">cases</span> <span class="n">multiset</span><span class="bp">.</span><span class="n">card_eq_one</span><span class="bp">.</span><span class="mi">1</span> <span class="n">hcard₂</span> <span class="k">with</span> <span class="n">x₂</span> <span class="n">hx₂</span><span class="o">,</span>
      <span class="n">cases</span> <span class="n">list</span><span class="bp">.</span><span class="n">perm_singleton</span> <span class="o">(</span><span class="n">quotient</span><span class="bp">.</span><span class="n">exact</span> <span class="n">hx₁</span><span class="o">),</span>
      <span class="n">cases</span> <span class="n">list</span><span class="bp">.</span><span class="n">perm_singleton</span> <span class="o">(</span><span class="n">quotient</span><span class="bp">.</span><span class="n">exact</span> <span class="n">hx₂</span><span class="o">),</span>
      <span class="n">cases</span> <span class="n">list</span><span class="bp">.</span><span class="n">perm_singleton</span> <span class="n">HL</span><span class="o">,</span>
      <span class="n">refl</span>
    <span class="o">}</span>
  <span class="o">}</span>
<span class="kn">end</span><span class="o">))</span> <span class="n">hs</span>
</pre></div>

#### [ Kenny Lau (Nov 03 2018 at 22:39)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/noob%20question/near/137129720):
<p><span class="user-mention" data-user-id="110044">@Chris Hughes</span> can you fix this?</p>

#### [ Chris Hughes (Nov 03 2018 at 22:49)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/noob%20question/near/137130012):
<div class="codehilite"><pre><span></span><span class="kn">example</span> <span class="o">{</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span><span class="bp">*</span><span class="o">}</span> <span class="o">(</span><span class="n">s</span> <span class="o">:</span> <span class="n">finset</span> <span class="n">α</span><span class="o">)</span> <span class="o">:</span> <span class="n">s</span><span class="bp">.</span><span class="n">card</span> <span class="bp">=</span> <span class="mi">1</span> <span class="bp">→</span> <span class="o">{</span><span class="n">a</span> <span class="o">:</span> <span class="n">α</span> <span class="bp">//</span> <span class="n">s</span> <span class="bp">=</span> <span class="n">finset</span><span class="bp">.</span><span class="n">singleton</span> <span class="n">a</span><span class="o">}</span> <span class="o">:=</span>
<span class="n">finset</span><span class="bp">.</span><span class="n">rec_on</span> <span class="n">s</span> <span class="o">(</span><span class="bp">λ</span> <span class="n">s</span><span class="o">,</span> <span class="bp">@</span><span class="n">quotient</span><span class="bp">.</span><span class="n">rec_on_subsingleton</span> <span class="bp">_</span> <span class="bp">_</span>
  <span class="o">(</span><span class="bp">λ</span> <span class="n">t</span> <span class="o">:</span> <span class="n">multiset</span> <span class="n">α</span><span class="o">,</span> <span class="bp">Π</span> <span class="o">(</span><span class="n">nodup</span> <span class="o">:</span> <span class="n">multiset</span><span class="bp">.</span><span class="n">nodup</span> <span class="n">t</span><span class="o">),</span>
    <span class="n">finset</span><span class="bp">.</span><span class="n">card</span> <span class="o">{</span><span class="n">val</span> <span class="o">:=</span> <span class="n">t</span><span class="o">,</span> <span class="n">nodup</span> <span class="o">:=</span> <span class="n">nodup</span><span class="o">}</span> <span class="bp">=</span> <span class="mi">1</span> <span class="bp">→</span> <span class="o">{</span><span class="n">a</span> <span class="bp">//</span> <span class="n">finset</span><span class="bp">.</span><span class="n">mk</span> <span class="n">t</span> <span class="n">nodup</span> <span class="bp">=</span> <span class="n">finset</span><span class="bp">.</span><span class="n">singleton</span> <span class="n">a</span><span class="o">})</span>
      <span class="o">(</span><span class="bp">λ</span> <span class="n">l</span><span class="o">,</span> <span class="bp">⟨λ</span> <span class="n">a</span> <span class="n">b</span><span class="o">,</span> <span class="n">funext</span> <span class="o">(</span><span class="bp">λ</span> <span class="n">x</span><span class="o">,</span> <span class="n">funext</span> <span class="o">(</span><span class="bp">λ</span> <span class="n">y</span><span class="o">,</span> <span class="n">subtype</span><span class="bp">.</span><span class="n">eq</span> <span class="err">$</span> <span class="n">finset</span><span class="bp">.</span><span class="n">singleton_inj</span><span class="bp">.</span><span class="mi">1</span> <span class="err">$</span>
        <span class="k">by</span> <span class="n">rw</span> <span class="o">[</span><span class="err">←</span> <span class="o">(</span><span class="n">a</span> <span class="n">x</span> <span class="n">y</span><span class="o">)</span><span class="bp">.</span><span class="mi">2</span><span class="o">,</span> <span class="err">←</span> <span class="o">(</span><span class="n">b</span> <span class="n">x</span> <span class="n">y</span><span class="o">)</span><span class="bp">.</span><span class="mi">2</span><span class="o">]))</span><span class="bp">⟩</span><span class="o">)</span> <span class="n">s</span>
  <span class="o">(</span><span class="bp">λ</span> <span class="n">l</span><span class="o">,</span> <span class="n">list</span><span class="bp">.</span><span class="n">rec_on</span> <span class="n">l</span> <span class="o">(</span><span class="bp">λ</span> <span class="bp">_</span> <span class="n">h</span><span class="o">,</span> <span class="n">nat</span><span class="bp">.</span><span class="n">no_confusion</span> <span class="n">h</span><span class="o">)</span>
    <span class="o">(</span><span class="bp">λ</span> <span class="n">a</span> <span class="n">l</span> <span class="bp">_</span> <span class="bp">_</span> <span class="n">h</span><span class="o">,</span> <span class="k">have</span> <span class="n">l</span><span class="bp">.</span><span class="n">length</span> <span class="bp">=</span> <span class="mi">0</span><span class="o">,</span> <span class="k">from</span> <span class="n">nat</span><span class="bp">.</span><span class="n">succ_inj</span> <span class="n">h</span><span class="o">,</span>
      <span class="bp">⟨</span><span class="n">a</span><span class="o">,</span> <span class="n">finset</span><span class="bp">.</span><span class="n">eq_of_veq</span> <span class="err">$</span> <span class="k">by</span> <span class="n">dsimp</span><span class="bp">;</span> <span class="n">rw</span> <span class="o">[</span><span class="n">list</span><span class="bp">.</span><span class="n">length_eq_zero</span><span class="bp">.</span><span class="mi">1</span> <span class="n">this</span><span class="o">]</span><span class="bp">;</span> <span class="n">refl</span><span class="bp">⟩</span><span class="o">))</span> <span class="o">)</span>
</pre></div>

#### [ Chris Hughes (Nov 03 2018 at 22:50)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/noob%20question/near/137130013):
<p>Not very pretty</p>

#### [ Kenny Lau (Nov 03 2018 at 22:50)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/noob%20question/near/137130057):
<div class="codehilite"><pre><span></span><span class="kn">import</span> <span class="n">data</span><span class="bp">.</span><span class="n">finset</span>

<span class="kn">lemma</span> <span class="n">list</span><span class="bp">.</span><span class="n">perm_singleton</span> <span class="o">{</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span><span class="bp">*</span><span class="o">}</span> <span class="o">{</span><span class="n">L</span> <span class="o">:</span> <span class="n">list</span> <span class="n">α</span><span class="o">}</span> <span class="o">{</span><span class="n">x</span> <span class="o">:</span> <span class="n">α</span><span class="o">}</span> <span class="o">(</span><span class="n">H</span> <span class="o">:</span> <span class="n">L</span> <span class="bp">~</span> <span class="o">[</span><span class="n">x</span><span class="o">])</span> <span class="o">:</span> <span class="n">L</span> <span class="bp">=</span> <span class="o">[</span><span class="n">x</span><span class="o">]</span> <span class="o">:=</span>
<span class="k">begin</span>
  <span class="n">generalize_hyp</span> <span class="n">hs</span> <span class="o">:</span> <span class="o">[</span><span class="n">x</span><span class="o">]</span> <span class="bp">=</span> <span class="n">S</span> <span class="n">at</span> <span class="n">H</span> <span class="err">⊢</span><span class="o">,</span>
  <span class="n">induction</span> <span class="n">H</span><span class="o">,</span>
  <span class="n">case</span> <span class="n">list</span><span class="bp">.</span><span class="n">perm</span><span class="bp">.</span><span class="n">nil</span> <span class="o">{</span> <span class="n">refl</span> <span class="o">},</span>
  <span class="n">case</span> <span class="n">list</span><span class="bp">.</span><span class="n">perm</span><span class="bp">.</span><span class="n">skip</span> <span class="o">:</span> <span class="n">y</span> <span class="n">L₁</span> <span class="n">L₂</span> <span class="n">H</span> <span class="n">ih</span> <span class="o">{</span>
    <span class="n">cases</span> <span class="n">hs</span><span class="o">,</span> <span class="n">cases</span> <span class="n">list</span><span class="bp">.</span><span class="n">perm_nil</span><span class="bp">.</span><span class="mi">1</span> <span class="n">H</span><span class="o">,</span> <span class="n">refl</span>
  <span class="o">},</span>
  <span class="n">case</span> <span class="n">list</span><span class="bp">.</span><span class="n">perm</span><span class="bp">.</span><span class="n">swap</span> <span class="o">{</span> <span class="n">injections</span> <span class="o">},</span>
  <span class="n">case</span> <span class="n">list</span><span class="bp">.</span><span class="n">perm</span><span class="bp">.</span><span class="n">trans</span> <span class="o">:</span> <span class="n">L₁</span> <span class="n">L₂</span> <span class="n">L₃</span> <span class="n">H12</span> <span class="n">H23</span> <span class="n">ih1</span> <span class="n">ih2</span> <span class="o">{</span>
    <span class="n">cases</span> <span class="n">hs</span><span class="o">,</span> <span class="n">cases</span> <span class="n">ih2</span> <span class="n">rfl</span><span class="o">,</span> <span class="n">cases</span> <span class="n">ih1</span> <span class="n">rfl</span><span class="o">,</span> <span class="n">refl</span>
  <span class="o">}</span>
<span class="kn">end</span>

<span class="n">def</span> <span class="n">extract</span> <span class="o">{</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span><span class="bp">*</span><span class="o">}</span> <span class="o">(</span><span class="n">s</span> <span class="o">:</span> <span class="n">finset</span> <span class="n">α</span><span class="o">)</span> <span class="o">(</span><span class="n">hs</span> <span class="o">:</span> <span class="n">s</span><span class="bp">.</span><span class="n">card</span> <span class="bp">=</span> <span class="mi">1</span><span class="o">)</span> <span class="o">:</span> <span class="n">α</span> <span class="o">:=</span>
<span class="n">finset</span><span class="bp">.</span><span class="n">rec_on</span> <span class="n">s</span>
  <span class="o">(</span><span class="bp">λ</span> <span class="n">m</span><span class="o">,</span> <span class="n">quotient</span><span class="bp">.</span><span class="n">rec_on</span> <span class="n">m</span>
    <span class="o">(</span><span class="bp">λ</span> <span class="n">L</span> <span class="bp">_</span><span class="o">,</span> <span class="k">show</span> <span class="n">L</span><span class="bp">.</span><span class="n">length</span> <span class="bp">=</span> <span class="mi">1</span> <span class="bp">→</span> <span class="n">α</span><span class="o">,</span> <span class="k">from</span> <span class="n">list</span><span class="bp">.</span><span class="n">cases_on</span> <span class="n">L</span>
      <span class="o">(</span><span class="bp">λ</span> <span class="n">H</span><span class="o">,</span> <span class="n">absurd</span> <span class="n">H</span> <span class="n">dec_trivial</span><span class="o">)</span>
      <span class="o">(</span><span class="bp">λ</span> <span class="n">hd</span> <span class="n">tl</span> <span class="n">H</span><span class="o">,</span> <span class="n">hd</span><span class="o">))</span>
    <span class="o">(</span><span class="bp">λ</span> <span class="n">L₁</span> <span class="n">L₂</span> <span class="n">HL</span><span class="o">,</span> <span class="k">begin</span>
  <span class="n">ext</span> <span class="n">H1</span> <span class="n">H2</span><span class="o">,</span> <span class="n">rcases</span> <span class="n">list</span><span class="bp">.</span><span class="n">length_eq_one</span><span class="bp">.</span><span class="mi">1</span> <span class="n">H2</span> <span class="k">with</span> <span class="bp">⟨</span><span class="n">x₂</span><span class="o">,</span> <span class="n">rfl</span><span class="bp">⟩</span><span class="o">,</span>
  <span class="n">cases</span> <span class="n">list</span><span class="bp">.</span><span class="n">perm_singleton</span> <span class="n">HL</span><span class="o">,</span> <span class="n">refl</span>
<span class="kn">end</span><span class="o">))</span> <span class="n">hs</span>
</pre></div>


<p>my version</p>

#### [ Kenny Lau (Nov 03 2018 at 22:50)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/noob%20question/near/137130058):
<p>well yours is much shorter</p>

#### [ Kenny Lau (Nov 03 2018 at 22:50)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/noob%20question/near/137130070):
<p>clever use of subsingleton...</p>

#### [ Kenny Lau (Nov 03 2018 at 22:52)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/noob%20question/near/137130125):
<div class="codehilite"><pre><span></span><span class="kn">theorem</span> <span class="n">extract_mem</span> <span class="o">{</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span><span class="bp">*</span><span class="o">}</span> <span class="o">(</span><span class="n">s</span> <span class="o">:</span> <span class="n">finset</span> <span class="n">α</span><span class="o">)</span> <span class="o">(</span><span class="n">hs</span> <span class="o">:</span> <span class="n">s</span><span class="bp">.</span><span class="n">card</span> <span class="bp">=</span> <span class="mi">1</span><span class="o">)</span> <span class="o">:</span>
  <span class="n">extract</span> <span class="n">s</span> <span class="n">hs</span> <span class="err">∈</span> <span class="n">s</span> <span class="o">:=</span>
<span class="k">begin</span>
  <span class="n">induction</span> <span class="n">s</span> <span class="k">with</span> <span class="n">m</span> <span class="bp">_</span><span class="o">,</span>
  <span class="n">rcases</span> <span class="n">m</span> <span class="k">with</span> <span class="n">L</span><span class="o">,</span>
  <span class="n">cases</span> <span class="n">L</span> <span class="k">with</span> <span class="n">hd</span> <span class="n">tl</span><span class="o">,</span> <span class="o">{</span> <span class="n">cases</span> <span class="n">hs</span> <span class="o">},</span>
  <span class="n">left</span><span class="o">,</span> <span class="n">refl</span>
<span class="kn">end</span>
</pre></div>

#### [ Kenny Lau (Nov 03 2018 at 22:53)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/noob%20question/near/137130137):
<p><span class="user-mention" data-user-id="128280">@Wojciech Nawrocki</span> so we have 2 solutions now</p>

#### [ Kenny Lau (Nov 03 2018 at 22:53)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/noob%20question/near/137130139):
<p>(i.e. mine and Chris's solution)</p>

#### [ Wojciech Nawrocki (Nov 03 2018 at 22:55)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/noob%20question/near/137130206):
<p>Oh wow, these are quite complex! I wonder if i should have just used lists instead :P but thanks a lot</p>

#### [ Kenny Lau (Nov 06 2018 at 02:37)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/noob%20question/near/146838268):
<p>related: <a href="https://github.com/leanprover/mathlib/pull/421" target="_blank" title="https://github.com/leanprover/mathlib/pull/421">https://github.com/leanprover/mathlib/pull/421</a></p>

#### [ Wojciech Nawrocki (Nov 09 2018 at 14:16)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/noob%20question/near/147370525):
<p>When a goal contains a reducible definition, how can i expand it to work with the internals? Namely, in here:</p>
<div class="codehilite"><pre><span></span>  <span class="bp">@</span><span class="o">[</span><span class="kn">reducible</span><span class="o">]</span>
  <span class="n">def</span> <span class="n">compose_partial</span> <span class="o">(</span><span class="n">f₁</span><span class="o">:</span> <span class="n">α</span> <span class="bp">→</span> <span class="n">option</span> <span class="n">β</span><span class="o">)</span> <span class="o">(</span><span class="n">f₂</span><span class="o">:</span> <span class="n">β</span> <span class="bp">→</span> <span class="n">option</span> <span class="n">γ</span><span class="o">)</span>
    <span class="o">:</span> <span class="n">α</span> <span class="bp">→</span> <span class="n">option</span> <span class="n">γ</span> <span class="o">:=</span>
  <span class="o">(</span><span class="bp">λ</span> <span class="n">a</span><span class="o">:</span> <span class="n">α</span><span class="o">,</span> <span class="n">option</span><span class="bp">.</span><span class="n">cases_on</span> <span class="o">(</span><span class="n">f₁</span> <span class="n">a</span><span class="o">)</span> <span class="n">none</span> <span class="o">(</span><span class="bp">λ</span> <span class="n">x</span><span class="o">,</span> <span class="n">f₂</span> <span class="n">x</span><span class="o">))</span>

  <span class="kn">notation</span> <span class="o">[</span><span class="n">parsing_only</span><span class="o">]</span> <span class="n">a</span> <span class="bp">`⬝</span><span class="err">ₚ</span><span class="bp">`</span> <span class="n">b</span> <span class="o">:=</span> <span class="n">compose_partial</span> <span class="n">b</span> <span class="n">a</span>

  <span class="kn">theorem</span> <span class="n">compose_none</span> <span class="o">(</span><span class="n">f₁</span><span class="o">:</span> <span class="n">α</span> <span class="bp">→</span> <span class="n">option</span> <span class="n">β</span><span class="o">)</span> <span class="o">(</span><span class="n">f₂</span><span class="o">:</span> <span class="n">β</span> <span class="bp">→</span> <span class="n">option</span> <span class="n">γ</span><span class="o">)</span> <span class="o">(</span><span class="n">x</span><span class="o">:</span> <span class="n">α</span><span class="o">)</span> <span class="o">(</span><span class="n">h</span><span class="o">:</span> <span class="n">f₁</span> <span class="n">x</span> <span class="bp">=</span> <span class="n">none</span><span class="o">)</span>
    <span class="o">:</span> <span class="o">(</span><span class="n">f₂</span> <span class="bp">⬝</span><span class="err">ₚ</span> <span class="n">f₁</span><span class="o">)</span> <span class="n">x</span> <span class="bp">=</span> <span class="n">none</span> <span class="o">:=</span>
  <span class="k">begin</span>
    <span class="n">sorry</span>
  <span class="kn">end</span>
</pre></div>


<p>I would like to expand <code>compose_partial</code> to carry through the <code>none</code> and get back a <code>none</code>.</p>

#### [ Rob Lewis (Nov 09 2018 at 14:22)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/noob%20question/near/147370813):
<p>You can use <code>unfold compose_partial</code>. <code>simp [compose_partial]</code> or <code>dsimp [compose_partial]</code> can also be useful.</p>

#### [ Wojciech Nawrocki (Nov 09 2018 at 14:23)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/noob%20question/near/147370896):
<p>Ah, <code>unfold</code>. Thanks!</p>

#### [ Kenny Lau (Nov 09 2018 at 15:32)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/noob%20question/near/147375089):
<p><code>@[reducible]</code> means that the typeclass system will automatically unfold it</p>

#### [ Kenny Lau (Nov 09 2018 at 15:32)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/noob%20question/near/147375094):
<p>but only the typeclass system</p>

#### [ Wojciech Nawrocki (Nov 17 2018 at 21:09)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/noob%20question/near/147889775):
<p>How can I make an instance of a dependent product <code>(x, p x)</code> where <code>p</code> is some proposition depending on <code>x</code>? Lean complains about impredicativity:</p>
<div class="codehilite"><pre><span></span><span class="n">type</span> <span class="n">mismatch</span> <span class="n">at</span> <span class="n">application</span>
  <span class="o">(</span><span class="n">n</span><span class="o">,</span> <span class="n">h</span><span class="o">)</span>
<span class="n">term</span>
  <span class="n">h</span>
<span class="n">has</span> <span class="n">type</span>
  <span class="n">n</span> <span class="bp">=</span> <span class="mi">4</span> <span class="o">:</span> <span class="kt">Prop</span>
<span class="n">but</span> <span class="n">is</span> <span class="n">expected</span> <span class="n">to</span> <span class="k">have</span> <span class="n">type</span>
  <span class="err">?</span><span class="n">m_1</span> <span class="o">:</span> <span class="kt">Type</span> <span class="err">?</span>
</pre></div>

#### [ Chris Hughes (Nov 17 2018 at 21:10)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/noob%20question/near/147889850):
<p>use <code>subtype</code></p>

#### [ Chris Hughes (Nov 17 2018 at 21:11)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/noob%20question/near/147889862):
<p>If you're using <code>prod</code>, it won't work because it's non dependent and it doesn't accept Propositions.</p>

#### [ Reid Barton (Nov 17 2018 at 21:11)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/noob%20question/near/147889863):
<p>Parentheses are only for <code>prod</code>, yeah</p>

#### [ Wojciech Nawrocki (Nov 17 2018 at 21:20)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/noob%20question/near/147890136):
<p>Oh I see, thanks!</p>

#### [ Kenny Lau (Nov 17 2018 at 21:27)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/noob%20question/near/147890301):
<p><code>prod</code> is non-dependent <code>sigma</code></p>

#### [ Kenny Lau (Nov 17 2018 at 21:27)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/noob%20question/near/147890303):
<p>but if it's proposition then you're better off using <code>subtype</code> which is a sort of specialize <code>sigma</code></p>

#### [ Wojciech Nawrocki (Nov 18 2018 at 22:56)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/noob%20question/near/147932778):
<p>Given an inductive type with some variants that take arguments, e.g.</p>
<div class="codehilite"><pre><span></span><span class="kn">inductive</span> <span class="n">Foo</span><span class="o">:</span> <span class="kt">Type</span>
<span class="bp">|</span> <span class="n">A</span> <span class="o">:</span> <span class="n">nat</span> <span class="bp">-&gt;</span> <span class="n">Foo</span>
<span class="bp">|</span> <span class="n">B</span><span class="o">:</span> <span class="n">Foo</span>
</pre></div>


<p>Is there a better way of saying that a particular <code>x: Foo</code> was constructed by <code>A</code> regardless of what the argument was than <code>\ex n: nat, x = A n</code>?</p>

#### [ Kevin Buzzard (Nov 18 2018 at 23:15)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/noob%20question/near/147933315):
<p>I don't think so. "x was constructed by A and I don't know what the argument was" is <em>exactly</em> <code>\ex n: nat, x = A n</code>, right? What's wrong with this way of saying it?</p>

#### [ Chris Hughes (Nov 18 2018 at 23:19)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/noob%20question/near/147933417):
<p>Other approaches</p>
<div class="codehilite"><pre><span></span><span class="n">def</span> <span class="n">p</span> <span class="o">:</span> <span class="n">foo</span> <span class="bp">→</span> <span class="kt">Prop</span>
<span class="bp">|</span> <span class="o">(</span><span class="n">A</span> <span class="n">n</span><span class="o">)</span> <span class="o">:=</span> <span class="n">true</span>
<span class="bp">|</span> <span class="n">B</span>     <span class="o">:=</span> <span class="n">false</span>

<span class="kn">inductive</span> <span class="n">p</span> <span class="o">:</span> <span class="n">foo</span> <span class="bp">→</span> <span class="kt">Prop</span>
<span class="bp">|</span> <span class="n">bar</span> <span class="o">:</span> <span class="n">p</span> <span class="o">(</span><span class="n">A</span> <span class="n">n</span><span class="o">)</span>
</pre></div>

#### [ Kevin Buzzard (Nov 18 2018 at 23:21)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/noob%20question/near/147933471):
<p>That first one is a much better way :-) I don't understand the second one!</p>

#### [ Wojciech Nawrocki (Nov 18 2018 at 23:22)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/noob%20question/near/147933521):
<p>Hm, I guess it might just be nice to have a shorthand like <code>p</code> in Chris's example for when the constructor is unwieldy, e.g. has lots of arguments. <code>p</code> would sound better as e.g. <code>is_A</code></p>

#### [ Rob Lewis (Nov 18 2018 at 23:22)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/noob%20question/near/147933522):
<p>The second one is an inductive proposition. I think you need <code>inductive</code> instead of <code>def</code>. This seems like the "canonical" way to me, and you can easily prove it equivalent to one using exists.</p>

#### [ Chris Hughes (Nov 18 2018 at 23:25)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/noob%20question/near/147933585):
<p>The inductive one gives you a nice recursor.</p>

#### [ Bryan Gin-ge Chen (Nov 18 2018 at 23:42)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/noob%20question/near/147934065):
<p>Is there another typo in the second one? I'm trying to figure out how to use it and I'm getting <code>unknown identifier 'n'</code></p>

#### [ Rob Lewis (Nov 18 2018 at 23:48)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/noob%20question/near/147934438):
<p>It should look like</p>
<div class="codehilite"><pre><span></span><span class="kn">inductive</span> <span class="n">Foo</span> <span class="o">:</span> <span class="kt">Type</span>
<span class="bp">|</span> <span class="n">A</span> <span class="o">:</span> <span class="n">nat</span> <span class="bp">-&gt;</span> <span class="n">Foo</span>
<span class="bp">|</span> <span class="n">B</span><span class="o">:</span> <span class="n">Foo</span>

<span class="kn">inductive</span> <span class="n">Foo</span><span class="bp">.</span><span class="n">is_A</span> <span class="o">:</span> <span class="n">Foo</span> <span class="bp">→</span> <span class="kt">Prop</span>
<span class="bp">|</span> <span class="n">of_A</span> <span class="o">(</span><span class="n">n</span><span class="o">)</span> <span class="o">:</span> <span class="n">Foo</span><span class="bp">.</span><span class="n">is_A</span> <span class="o">(</span><span class="n">Foo</span><span class="bp">.</span><span class="n">A</span> <span class="n">n</span><span class="o">)</span>
</pre></div>

#### [ Rob Lewis (Nov 18 2018 at 23:49)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/noob%20question/near/147934446):
<p>The idea being, <code>Foo.is_A</code> is a family of propositions. For any <code>n : nat</code>, <code>Foo.is_A.of_A n</code> is a proof of <code>Foo.is_A (Foo.A n)</code>.</p>

#### [ Bryan Gin-ge Chen (Nov 18 2018 at 23:51)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/noob%20question/near/147934510):
<p>Thanks! I'd tried adding <code>n</code> after <code>bar</code> and I forgot that the parentheses were necessary.</p>


{% endraw %}
