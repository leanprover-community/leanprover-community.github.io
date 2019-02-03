---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/76230withoutlossofadvertisement.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [without loss of advertisement](https://leanprover-community.github.io/archive/113488general/76230withoutlossofadvertisement.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Patrick Massot (Apr 21 2018 at 13:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/without%20loss%20of%20advertisement/near/125491146):
<p>Let me share my joy of using <span class="user-mention" data-user-id="110026">@Simon Hudon</span> recent contributions (not yet merged, see <a href="https://github.com/PatrickMassot/mathlib/tree/wlog_ext" target="_blank" title="https://github.com/PatrickMassot/mathlib/tree/wlog_ext">https://github.com/PatrickMassot/mathlib/tree/wlog_ext</a> for a version including both relevant PR if you want to play with it).</p>
<p>I defined homeomorphisms between topological spaces <code>X</code> and <code>Y</code>, and the support of a homeomorphism <code>f</code> from <code>X</code> to itself (if you don't know what this means, think <code>homeo X X</code> coerces to invertible functions from <code>X</code> to <code>X</code> and <code>supp f</code> is the set of <code>x</code> in <code>X</code> such that <code>f x ≠ x</code>, that's good enough approximation). I want to prove the trivial yet important fact that two homeos with disjoint support commute. I already had various proofs of that, some versions written with the help of Mario. But I'd like to show what the latest version looks like. So statement is:</p>
<div class="codehilite"><pre><span></span><span class="kn">example</span> <span class="o">{</span><span class="n">f</span> <span class="n">g</span> <span class="o">:</span> <span class="n">homeo</span> <span class="n">X</span> <span class="n">X</span><span class="o">}</span> <span class="o">(</span><span class="n">H</span> <span class="o">:</span> <span class="n">supp</span> <span class="n">f</span> <span class="err">∩</span> <span class="n">supp</span> <span class="n">g</span> <span class="bp">=</span> <span class="err">∅</span><span class="o">)</span> <span class="o">:</span> <span class="n">f</span> <span class="bp">*</span> <span class="n">g</span> <span class="bp">=</span> <span class="n">g</span> <span class="bp">*</span> <span class="n">f</span>
</pre></div>

#### [ Patrick Massot (Apr 21 2018 at 13:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/without%20loss%20of%20advertisement/near/125491159):
<p>First consider the pen and paper proof: We need to prove f (g x) = g (f x) for all x in X. If x is neither in supp f nor in supp g then it's obvious, so let's discard this case. WLOG x is in supp f since everything is obviously symmetric in f and g. By H, x is not in supp g. Also the support of f is stable under f (because its complement the fixed points set is obviously stable). So f x is also not in supp g. So g x = x and g (f x) = f x and we are done.</p>

#### [ Patrick Massot (Apr 21 2018 at 13:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/without%20loss%20of%20advertisement/near/125491165):
<p>Simon's work help with the first and third sentences. First "We need to prove f (g x) = g (f x) for all x in X". But actually <code>homeo X X</code> is not quite <code>X → X</code> so we can't do <code>funext x</code>. We only need a extensionality lemma for homeos, and tag it with the <code>[extensionality]</code> attribute to later write <code>ext x</code> in place of <code>funext x</code>. Same would work for sets etc. </p>
<p>Now the third sentence is much more spectacular: "WLOG x is in supp f since everything is obviously symmetric in f and g". I still cannot write this without sweating and thinking: Oh my god, Lean will disagree it's obvious. Simon's tactic turns this into: <code>wlog h : x ∈ supp f using f g</code>. Period. No disagrement. <span class="emoji emoji-1f60d" title="heart eyes">:heart_eyes:</span></p>

#### [ Patrick Massot (Apr 21 2018 at 13:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/without%20loss%20of%20advertisement/near/125491204):
<p>Here is what it looks like. Notice also liberal use of the finish tactic.</p>
<div class="codehilite"><pre><span></span><span class="kn">lemma</span> <span class="n">fundamental&#39;</span> <span class="o">{</span><span class="n">f</span> <span class="n">g</span> <span class="o">:</span> <span class="n">homeo</span> <span class="n">X</span> <span class="n">X</span><span class="o">}</span> <span class="o">(</span><span class="n">H</span> <span class="o">:</span> <span class="n">supp</span> <span class="n">f</span> <span class="err">∩</span> <span class="n">supp</span> <span class="n">g</span> <span class="bp">=</span> <span class="err">∅</span><span class="o">)</span> <span class="o">:</span> <span class="n">f</span> <span class="bp">*</span> <span class="n">g</span> <span class="bp">=</span> <span class="n">g</span> <span class="bp">*</span> <span class="n">f</span> <span class="o">:=</span>
<span class="k">begin</span>
  <span class="n">ext</span> <span class="n">x</span><span class="o">,</span>
  <span class="n">by_cases</span> <span class="n">H&#39;</span> <span class="o">:</span> <span class="n">x</span> <span class="err">∈</span> <span class="n">supp</span> <span class="n">f</span> <span class="bp">∨</span> <span class="n">x</span> <span class="err">∈</span> <span class="n">supp</span> <span class="n">g</span><span class="o">,</span>
  <span class="o">{</span> <span class="c1">-- Here we assume H&#39; : x ∈ supp f ∨ x ∈ supp g</span>
    <span class="n">wlog</span> <span class="n">h</span> <span class="o">:</span> <span class="n">x</span> <span class="err">∈</span> <span class="n">supp</span> <span class="n">f</span> <span class="kn">using</span> <span class="n">f</span> <span class="n">g</span><span class="o">,</span>
    <span class="k">have</span> <span class="n">x_not_supp_g</span> <span class="o">:</span> <span class="n">x</span> <span class="err">∉</span> <span class="n">supp</span> <span class="n">g</span> <span class="o">:=</span> <span class="o">(</span><span class="n">subset_compl_iff_disjoint</span><span class="bp">.</span><span class="mi">2</span> <span class="n">H</span><span class="o">)</span> <span class="n">h</span><span class="o">,</span>
    <span class="k">have</span> <span class="n">f_x_supp_f</span> <span class="o">:</span> <span class="n">f</span> <span class="n">x</span> <span class="err">∈</span> <span class="n">supp</span> <span class="n">f</span><span class="o">,</span>
    <span class="o">{</span> <span class="k">have</span> <span class="o">:</span> <span class="n">f</span> <span class="n">x</span> <span class="err">∈</span> <span class="n">f</span> <span class="err">&#39;&#39;</span> <span class="n">supp</span> <span class="n">f</span> <span class="o">:=</span> <span class="n">mem_image_of_mem</span> <span class="n">f</span> <span class="n">h</span><span class="o">,</span>
      <span class="n">finish</span> <span class="o">[</span><span class="n">stable_support</span> <span class="n">f</span><span class="o">]</span> <span class="o">},</span>
    <span class="k">have</span> <span class="o">:</span> <span class="n">f</span> <span class="n">x</span> <span class="err">∉</span> <span class="n">supp</span> <span class="n">g</span> <span class="o">:=</span> <span class="o">(</span><span class="n">subset_compl_iff_disjoint</span><span class="bp">.</span><span class="mi">2</span> <span class="n">H</span><span class="o">)</span> <span class="n">f_x_supp_f</span><span class="o">,</span>
    <span class="n">finish</span> <span class="o">[</span><span class="n">fix_of_not_in_supp</span><span class="o">]</span> <span class="o">},</span>
  <span class="o">{</span> <span class="c1">-- Now we assume H&#39; : ¬(x ∈ supp f ∨ x ∈ supp g)</span>
    <span class="n">rw</span> <span class="n">not_or_distrib</span> <span class="n">at</span> <span class="n">H&#39;</span><span class="o">,</span>
    <span class="n">finish</span> <span class="o">[</span><span class="n">fix_of_not_in_supp</span><span class="o">]</span> <span class="o">}</span>
<span class="kn">end</span>
</pre></div>

#### [ Patrick Massot (Apr 21 2018 at 13:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/without%20loss%20of%20advertisement/near/125491205):
<p>And a <code>calc</code> version for good measure.</p>
<div class="codehilite"><pre><span></span><span class="kn">lemma</span> <span class="n">fundamental&#39;&#39;</span> <span class="o">{</span><span class="n">f</span> <span class="n">g</span> <span class="o">:</span> <span class="n">homeo</span> <span class="n">X</span> <span class="n">X</span><span class="o">}</span> <span class="o">(</span><span class="n">H</span> <span class="o">:</span> <span class="n">supp</span> <span class="n">f</span> <span class="err">∩</span> <span class="n">supp</span> <span class="n">g</span> <span class="bp">=</span> <span class="err">∅</span><span class="o">)</span> <span class="o">:</span> <span class="n">f</span> <span class="bp">*</span> <span class="n">g</span> <span class="bp">=</span> <span class="n">g</span> <span class="bp">*</span> <span class="n">f</span> <span class="o">:=</span>
<span class="k">begin</span>
  <span class="n">ext</span> <span class="n">x</span><span class="o">,</span>
  <span class="n">by_cases</span> <span class="n">H&#39;</span> <span class="o">:</span> <span class="n">x</span> <span class="err">∈</span> <span class="n">supp</span> <span class="n">f</span> <span class="bp">∨</span> <span class="n">x</span> <span class="err">∈</span> <span class="n">supp</span> <span class="n">g</span><span class="o">,</span>
  <span class="o">{</span> <span class="c1">-- Here we assume H&#39; : x ∈ supp f ∨ x ∈ supp g</span>
    <span class="n">wlog</span> <span class="n">h</span> <span class="o">:</span> <span class="n">x</span> <span class="err">∈</span> <span class="n">supp</span> <span class="n">f</span> <span class="kn">using</span> <span class="n">f</span> <span class="n">g</span><span class="o">,</span>
    <span class="n">exact</span> <span class="k">calc</span>
    <span class="o">(</span><span class="n">f</span> <span class="bp">*</span> <span class="n">g</span><span class="o">)</span> <span class="n">x</span> <span class="bp">=</span> <span class="n">f</span> <span class="o">(</span><span class="n">g</span> <span class="n">x</span><span class="o">)</span> <span class="o">:</span> <span class="k">by</span> <span class="n">simp</span>
          <span class="bp">...</span> <span class="bp">=</span> <span class="n">f</span> <span class="n">x</span>     <span class="o">:</span> <span class="k">by</span> <span class="o">{</span> <span class="k">have</span> <span class="n">x_not_supp_g</span> <span class="o">:</span> <span class="n">x</span> <span class="err">∉</span> <span class="n">supp</span> <span class="n">g</span> <span class="o">:=</span> <span class="o">(</span><span class="n">subset_compl_iff_disjoint</span><span class="bp">.</span><span class="mi">2</span> <span class="n">H</span><span class="o">)</span> <span class="n">h</span><span class="o">,</span>
                               <span class="n">finish</span> <span class="o">[</span><span class="n">fix_of_not_in_supp</span><span class="o">]</span> <span class="o">}</span>
          <span class="bp">...</span> <span class="bp">=</span> <span class="n">g</span> <span class="o">(</span><span class="n">f</span> <span class="n">x</span><span class="o">)</span> <span class="o">:</span> <span class="k">by</span> <span class="o">{</span> <span class="k">have</span> <span class="n">f_x_supp_f</span> <span class="o">:</span> <span class="n">f</span> <span class="n">x</span> <span class="err">∈</span> <span class="n">supp</span> <span class="n">f</span><span class="o">,</span>
                               <span class="o">{</span> <span class="k">have</span> <span class="o">:</span> <span class="n">f</span> <span class="n">x</span> <span class="err">∈</span> <span class="n">f</span> <span class="err">&#39;&#39;</span> <span class="n">supp</span> <span class="n">f</span> <span class="o">:=</span> <span class="n">mem_image_of_mem</span> <span class="n">f</span> <span class="n">h</span><span class="o">,</span>
                                 <span class="n">finish</span> <span class="o">[</span><span class="n">stable_support</span> <span class="n">f</span><span class="o">]</span> <span class="o">},</span>
                               <span class="k">have</span> <span class="o">:</span> <span class="n">f</span> <span class="n">x</span> <span class="err">∉</span> <span class="n">supp</span> <span class="n">g</span> <span class="o">:=</span> <span class="o">(</span><span class="n">subset_compl_iff_disjoint</span><span class="bp">.</span><span class="mi">2</span> <span class="n">H</span><span class="o">)</span> <span class="n">f_x_supp_f</span><span class="o">,</span>
                               <span class="n">finish</span> <span class="o">[</span><span class="n">fix_of_not_in_supp</span><span class="o">]</span> <span class="o">}</span>
          <span class="bp">...</span> <span class="bp">=</span> <span class="o">(</span><span class="n">g</span> <span class="bp">*</span> <span class="n">f</span><span class="o">)</span> <span class="n">x</span> <span class="o">:</span> <span class="k">by</span> <span class="n">simp</span> <span class="o">},</span>
  <span class="o">{</span> <span class="c1">-- Now we assume H&#39; : ¬(x ∈ supp f ∨ x ∈ supp g)</span>
    <span class="n">rw</span> <span class="n">not_or_distrib</span> <span class="n">at</span> <span class="n">H&#39;</span><span class="o">,</span>
    <span class="n">finish</span> <span class="o">[</span><span class="n">fix_of_not_in_supp</span><span class="o">]</span> <span class="o">}</span>
<span class="kn">end</span>
</pre></div>

#### [ Patrick Massot (Apr 21 2018 at 13:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/without%20loss%20of%20advertisement/near/125491206):
<p>Term mode people will have a really hard time converting me.</p>

#### [ Simon Hudon (Apr 21 2018 at 14:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/without%20loss%20of%20advertisement/near/125491435):
<p>What a nice homage! Thank you! I'm so happy that you like those tools :)</p>

#### [ Kenny Lau (Apr 21 2018 at 14:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/without%20loss%20of%20advertisement/near/125491663):
<p>let's see how long we'll need to wait before they merge the PR</p>

#### [ Patrick Massot (Apr 21 2018 at 14:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/without%20loss%20of%20advertisement/near/125491898):
<blockquote>
<p>What a nice homage! Thank you! I'm so happy that you like those tools :)</p>
</blockquote>
<p>I'm not only the annoying user who can't code anything by himself, and keep reminding you to work on these tactics (and write tactic writing tutorials covering <code>pi_instance</code> and <code>wlog</code>). I also love using them, and documenting things.</p>

#### [ Patrick Massot (Apr 21 2018 at 14:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/without%20loss%20of%20advertisement/near/125492035):
<p>And I think the community is currently working really well. It seems to me we recently went from the pretty horrible situation where the main dev felt harassed by frustrated users to a pretty nice situation. Leo and Sebastian are peacefully working on Lean 4 while everybody else finds some place in the Lean 3 world. Clearly we don't want Leo to spend time writing tactics like <code>wlog</code>. We want power users like Mario, you, Scott... to write these. And then we have dumb users like me who can come up with examples finding bugs, suggests new tactics, write documentation... And everybody has fun, I think. And it seems Lean 4 will expose even more to Lean without touching C++ code or even PRing the main repo, so we are clearly going in the right direction.</p>

#### [ Patrick Massot (Apr 21 2018 at 14:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/without%20loss%20of%20advertisement/near/125492037):
<blockquote>
<p>let's see how long we'll need to wait before they merge the PR</p>
</blockquote>
<p>Ok, we still have some frustration...</p>

#### [ Patrick Massot (Apr 21 2018 at 14:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/without%20loss%20of%20advertisement/near/125492044):
<p>But I'm optimistic anyway.</p>

#### [ Patrick Massot (Apr 21 2018 at 14:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/without%20loss%20of%20advertisement/near/125492086):
<p>And I hope that writing an example non-trivially using <code>wlog</code> actually helps getting the PR merged more than complaining that reviewing PR takes time.</p>

#### [ Mario Carneiro (Apr 21 2018 at 14:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/without%20loss%20of%20advertisement/near/125492181):
<p>I always like to see a tool in use, that definitely brings it up the todo list</p>

#### [ Simon Hudon (Apr 21 2018 at 14:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/without%20loss%20of%20advertisement/near/125492500):
<blockquote>
<p>And I think the community is currently working really well.</p>
</blockquote>
<p>I've also had a very positive experience in the community with people eager to help and grateful when you give then a nudge. I was surprised and saddened that Leo described his experience as harassment.</p>

#### [ Simon Hudon (Apr 21 2018 at 14:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/without%20loss%20of%20advertisement/near/125492683):
<blockquote>
<p>And then we have dumb users like me who can come up with examples finding bugs, suggests new tactics, write documentation...</p>
</blockquote>
<p>Yeah! Darn those dumb users, leeching off the community and only proving important mathematical theorems!</p>
<p>But seriously, I'm really glad you decided to champion the cause of documentation. It's often neglected but it makes such a big difference!</p>

#### [ Moses Schönfinkel (Apr 21 2018 at 15:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/without%20loss%20of%20advertisement/near/125493169):
<p>Is lack of documentation why Coq hasn't been adopted widespreadly (ok this is not really English) after 30 years?</p>

#### [ Simon Hudon (Apr 21 2018 at 15:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/without%20loss%20of%20advertisement/near/125493254):
<p>Hard to say. To be fair, I found Coq much harder to pick up than Lean. I never actually ended up applying it to large problems. I think the standard library is ill-organized and much harder to use than Lean's.</p>

#### [ Moses Schönfinkel (Apr 21 2018 at 15:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/without%20loss%20of%20advertisement/near/125493319):
<p>That's because there is no organisation so to speak; no hierarchy either. You have, for example, two different versions for Z&lt;theroem&gt; and N&lt;theorem&gt;.</p>

#### [ Simon Hudon (Apr 21 2018 at 15:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/without%20loss%20of%20advertisement/near/125493359):
<p>Maybe you could summarize that as: when you're a beginner, you have to get over a lot humps before you can begin to try stuff on your own. It feels like with Lean, once you installed it, you start hacking and it progressively becomes harder as you get more ambitious</p>

#### [ Simon Hudon (Apr 21 2018 at 15:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/without%20loss%20of%20advertisement/near/125493361):
<p>Yeah, it looks a bit like a research project that just happened to be useful</p>

#### [ Simon Hudon (Apr 21 2018 at 15:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/without%20loss%20of%20advertisement/near/125493372):
<p>And I find it doesn't help that the library is built around ML modules more than around type classes. Type classes are really tremendous to make things simple to use.</p>

#### [ Kevin Buzzard (Apr 21 2018 at 22:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/without%20loss%20of%20advertisement/near/125505376):
<p>My 2 cents: I think that the Coq community, and the automated theorem proving community in general, have done a bad job of advertising to mathematicians. I remember the edition of the Notices of the AMS coming out a few years ago which concentrated on this stuff and wondering if it was the future, but somehow the jewels in the crown at the time were things like "yet another proof of the 4 colour theorem" and maybe this was just after the odd order theorem, which was something mathematicians had long moved on from.</p>

#### [ Kevin Buzzard (Apr 21 2018 at 22:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/without%20loss%20of%20advertisement/near/125505378):
<p>My gut feeling is that a different approach is needed</p>

#### [ Kevin Buzzard (Apr 21 2018 at 23:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/without%20loss%20of%20advertisement/near/125505426):
<p>so that's why I'm going to try concentrating on getting undergraduates in mathematics to prove a bunch of basic stuff, because I think it might have a different kind of outcome.</p>

#### [ Kevin Buzzard (Apr 21 2018 at 23:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/without%20loss%20of%20advertisement/near/125505430):
<p>Maybe a bunch of young people who know about this stuff will somehow integrate it into the maths community in a different way.</p>

#### [ Kevin Buzzard (Apr 21 2018 at 23:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/without%20loss%20of%20advertisement/near/125505485):
<p>Let me absolutely echo the opinions of the others in this thread -- I've had a really good time learning Lean here, I would never have got anywhere without this group, and now I feel like I actually understand certain aspects of the software well enough to be able to use it without being continually frustrated.</p>

#### [ Kevin Buzzard (Apr 21 2018 at 23:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/without%20loss%20of%20advertisement/near/125505489):
<p>The strategy of "if you don't get it, find out about it and then write some docs" also works really well for me.</p>

#### [ Kevin Buzzard (Apr 21 2018 at 23:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/without%20loss%20of%20advertisement/near/125505498):
<p>And also the idea of choosing a non-trivial thing to work on and then just working on it has taught me a huge amount. There are just over 5000 lines of code in the stacks project directory now.</p>

#### [ Patrick Massot (Apr 21 2018 at 23:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/without%20loss%20of%20advertisement/near/125505645):
<p>Roughly, how many lines are pure commutative algebra and how many use geometric language?</p>

#### [ Kevin Buzzard (Apr 21 2018 at 23:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/without%20loss%20of%20advertisement/near/125505821):
<p>it wouldn't surprise me if nearly 1000 lines were cut-and-pasted stacks project LaTeX :-)</p>

#### [ Kevin Buzzard (Apr 21 2018 at 23:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/without%20loss%20of%20advertisement/near/125505839):
<p>I guess it's almost all algebra at the minute</p>

#### [ Kevin Buzzard (Apr 21 2018 at 23:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/without%20loss%20of%20advertisement/near/125505885):
<p><span class="user-mention" data-user-id="112680">@Johan Commelin</span> pointed out a typo in my definition of scheme and I told him not to believe my definition until we had some proof of a lemma about schemes which was geometric</p>

#### [ Kevin Buzzard (Apr 21 2018 at 23:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/without%20loss%20of%20advertisement/near/125505886):
<p>and I am not sure how geometric you think this is</p>

#### [ Kevin Buzzard (Apr 21 2018 at 23:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/without%20loss%20of%20advertisement/near/125505887):
<p>but he suggested the Spec / Gamma duality, Hom(S,Spec(A)) = Hom(A,Gamma(S))</p>

#### [ Patrick Massot (Apr 21 2018 at 23:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/without%20loss%20of%20advertisement/near/125505888):
<p>I know the distinction is hard to make (Grothendieck did this on purpose!). Let's say: how many lines not containing "sheaf" or "presheaf"?</p>

#### [ Kevin Buzzard (Apr 21 2018 at 23:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/without%20loss%20of%20advertisement/near/125505890):
<p>which I think would be a true test</p>

#### [ Kevin Buzzard (Apr 21 2018 at 23:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/without%20loss%20of%20advertisement/near/125505898):
<p>Oh there are lots and lots of lines proving abstract stuff of the form "if I have a presheaf only defined on a basis of open sets for a topology, but it satisfies the sheaf axiom for a cofinal set of covers, then it extends uniquely to a sheaf on the whole space"</p>

#### [ Kevin Buzzard (Apr 21 2018 at 23:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/without%20loss%20of%20advertisement/near/125505943):
<p>I don't really know how to answer your questions precisely though</p>

#### [ Kevin Buzzard (Apr 21 2018 at 23:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/without%20loss%20of%20advertisement/near/125505944):
<p>There's a bunch of lemmas about rings</p>

#### [ Kevin Buzzard (Apr 21 2018 at 23:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/without%20loss%20of%20advertisement/near/125505948):
<p>and then a bunch of lemmas about presheaves and sheaves</p>

#### [ Kevin Buzzard (Apr 21 2018 at 23:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/without%20loss%20of%20advertisement/near/125505950):
<p>and then some actual mathematics saying that some sequence of rings is exact</p>

#### [ Kevin Buzzard (Apr 21 2018 at 23:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/without%20loss%20of%20advertisement/near/125505959):
<p>and I'm just in the process of writing the glue which will glue it all together.</p>

#### [ Patrick Massot (Apr 21 2018 at 23:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/without%20loss%20of%20advertisement/near/125505966):
<p>Did you try to separate nicely as much sheaf theory from ring theory as possible?</p>

#### [ Andrew Ashworth (Apr 21 2018 at 23:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/without%20loss%20of%20advertisement/near/125506367):
<p>so would you say it took you about a year of using lean before you felt confident in doing things in it?</p>

#### [ Andrew Ashworth (Apr 21 2018 at 23:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/without%20loss%20of%20advertisement/near/125506370):
<p>i wonder how much faster your summer undergraduates and fall students will learn lean</p>

#### [ Patrick Massot (Apr 21 2018 at 23:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/without%20loss%20of%20advertisement/near/125506407):
<p>I think he started less than a year ago</p>

#### [ Patrick Massot (Apr 21 2018 at 23:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/without%20loss%20of%20advertisement/near/125506410):
<p>Last July maybe?</p>

#### [ Patrick Massot (Apr 21 2018 at 23:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/without%20loss%20of%20advertisement/near/125506411):
<p>Maybe even August</p>

#### [ Andrew Ashworth (Apr 21 2018 at 23:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/without%20loss%20of%20advertisement/near/125506463):
<p>two semesters of focused effort sounds about right though</p>

#### [ Andrew Ashworth (Apr 21 2018 at 23:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/without%20loss%20of%20advertisement/near/125506465):
<p>coincidentally that's how long it takes to get through software foundations 1-3</p>

#### [ Andrew Ashworth (Apr 21 2018 at 23:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/without%20loss%20of%20advertisement/near/125506571):
<p>if i had to guess that right there is the reason it never took off in 30 years</p>

#### [ Andrew Ashworth (Apr 21 2018 at 23:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/without%20loss%20of%20advertisement/near/125506611):
<p>imagine if you had to spend two semesters before you could write latex or use a computer algebra system</p>

#### [ Patrick Massot (Apr 21 2018 at 23:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/without%20loss%20of%20advertisement/near/125506667):
<p>Also don't forget it's not like Coq was ready on year one and then waited for 30 years</p>

#### [ Kevin Buzzard (Apr 22 2018 at 01:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/without%20loss%20of%20advertisement/near/125509691):
<p>Yes I started when I was in MSRI in July/August 2017</p>

#### [ Kevin Buzzard (Apr 22 2018 at 01:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/without%20loss%20of%20advertisement/near/125509731):
<p>but I'm not entirely sure you can call my efforts focussed</p>

#### [ Kevin Buzzard (Apr 22 2018 at 01:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/without%20loss%20of%20advertisement/near/125509732):
<p>I was teaching a class of 220 students in one of the terms, and being head of pure maths and teaching a graduate course in the other one :-/</p>

#### [ Kevin Buzzard (Apr 22 2018 at 01:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/without%20loss%20of%20advertisement/near/125509733):
<p>On the other hand I pretty much gave up all of my other hobbies</p>


{% endraw %}
