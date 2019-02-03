---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/19443proofofthefivelemma.html
---

## Stream: [general](index.html)
### Topic: [proof of the five lemma](19443proofofthefivelemma.html)

---


{% raw %}
#### [ Johan Commelin (Apr 24 2018 at 14:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proof%20of%20the%20five%20lemma/near/125618074):
<p>Yoohoo, I'm done.<br>
<a href="https://gist.github.com/jcommelin/9ea76f7a1356ed8dd9499e765f580ef8" target="_blank" title="https://gist.github.com/jcommelin/9ea76f7a1356ed8dd9499e765f580ef8">https://gist.github.com/jcommelin/9ea76f7a1356ed8dd9499e765f580ef8</a><br>
It's pretty long and ugly.</p>

#### [ Johan Commelin (Apr 24 2018 at 14:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proof%20of%20the%20five%20lemma/near/125618084):
<p>Feel free to start golfing on this one (-;</p>

#### [ Johan Commelin (Apr 24 2018 at 14:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proof%20of%20the%20five%20lemma/near/125618094):
<p>I feel that a computer should almost be able to find the proof alone</p>

#### [ Johan Commelin (Apr 24 2018 at 14:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proof%20of%20the%20five%20lemma/near/125618132):
<p>But my tactic-fu is small and my tactic-writing-fu is nonexistent</p>

#### [ Sean Leather (Apr 24 2018 at 14:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proof%20of%20the%20five%20lemma/near/125618139):
<p>But how would the computer know how many times to <code>apply_assumption</code>? <span class="emoji emoji-1f635" title="dizzy face">:dizzy_face:</span> <span class="emoji emoji-1f606" title="laughing">:laughing:</span></p>

#### [ Johan Commelin (Apr 24 2018 at 14:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proof%20of%20the%20five%20lemma/near/125618157):
<p>Yeah, agreed... but still... every line I really just follow my nose...</p>

#### [ Sean Leather (Apr 24 2018 at 14:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proof%20of%20the%20five%20lemma/near/125618160):
<p>The nice thing about your proof is that it is clearly step-by-step.</p>

#### [ Johan Commelin (Apr 24 2018 at 14:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proof%20of%20the%20five%20lemma/near/125618162):
<p>And I guess already with the existing tactics I think it can be reasonably shortened</p>

#### [ Johan Commelin (Apr 24 2018 at 14:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proof%20of%20the%20five%20lemma/near/125618203):
<p>Because using commutativity or computations in a group takes pretty long atm</p>

#### [ Johan Commelin (Apr 24 2018 at 14:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proof%20of%20the%20five%20lemma/near/125618223):
<p>I feel like the lines with <code>\ex bla : Group, condition</code> are the only place that Lean should get my help.</p>

#### [ Johan Commelin (Apr 24 2018 at 14:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proof%20of%20the%20five%20lemma/near/125618224):
<p>The rest it should figure out alone...</p>

#### [ Johan Commelin (Apr 24 2018 at 16:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proof%20of%20the%20five%20lemma/near/125622862):
<p>/me updated the proof of the five lemma: <a href="https://gist.github.com/jcommelin/9ea76f7a1356ed8dd9499e765f580ef8" target="_blank" title="https://gist.github.com/jcommelin/9ea76f7a1356ed8dd9499e765f580ef8">https://gist.github.com/jcommelin/9ea76f7a1356ed8dd9499e765f580ef8</a></p>

#### [ Johan Commelin (Apr 24 2018 at 16:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proof%20of%20the%20five%20lemma/near/125622867):
<p>It is now refactored to first prove two four-lemmas</p>

#### [ Johan Commelin (Apr 24 2018 at 16:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proof%20of%20the%20five%20lemma/near/125622871):
<p>These then combine to prove the five lemma</p>

#### [ Kenny Lau (Apr 24 2018 at 16:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proof%20of%20the%20five%20lemma/near/125622956):
<div class="codehilite"><pre><span></span><span class="k">begin</span>
 <span class="n">split</span><span class="o">,</span>
 <span class="n">apply</span> <span class="n">four_lemma₁</span> <span class="n">com₁</span> <span class="n">com₂</span> <span class="n">com₃</span> <span class="n">eB₁</span> <span class="n">eC₁</span> <span class="n">eB₂</span> <span class="n">eC₂</span> <span class="n">hj</span> <span class="n">hk</span><span class="bp">.</span><span class="mi">1</span> <span class="n">hm</span><span class="bp">.</span><span class="mi">1</span><span class="o">,</span>
 <span class="n">apply</span> <span class="n">four_lemma₂</span> <span class="n">com₂</span> <span class="n">com₃</span> <span class="n">com₄</span> <span class="n">eC₁</span> <span class="n">eD₁</span> <span class="n">eC₂</span> <span class="n">eD₂</span> <span class="n">hk</span><span class="bp">.</span><span class="mi">2</span> <span class="n">hm</span><span class="bp">.</span><span class="mi">2</span> <span class="n">hn</span><span class="o">,</span>
<span class="kn">end</span>
</pre></div>

#### [ Kenny Lau (Apr 24 2018 at 16:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proof%20of%20the%20five%20lemma/near/125622957):
<p>now I would write this in term mode lol</p>

#### [ Kenny Lau (Apr 24 2018 at 16:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proof%20of%20the%20five%20lemma/near/125622973):
<div class="codehilite"><pre><span></span><span class="bp">⟨</span><span class="n">four_lemma₁</span> <span class="n">com₁</span> <span class="n">com₂</span> <span class="n">com₃</span> <span class="n">eB₁</span> <span class="n">eC₁</span> <span class="n">eB₂</span> <span class="n">eC₂</span> <span class="n">hj</span> <span class="n">hk</span><span class="bp">.</span><span class="mi">1</span> <span class="n">hm</span><span class="bp">.</span><span class="mi">1</span><span class="o">,</span> <span class="n">four_lemma₂</span> <span class="n">com₂</span> <span class="n">com₃</span> <span class="n">com₄</span> <span class="n">eC₁</span> <span class="n">eD₁</span> <span class="n">eC₂</span> <span class="n">eD₂</span> <span class="n">hk</span><span class="bp">.</span><span class="mi">2</span> <span class="n">hm</span><span class="bp">.</span><span class="mi">2</span> <span class="n">hn</span><span class="bp">⟩</span>
</pre></div>

#### [ Johan Commelin (Apr 24 2018 at 16:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proof%20of%20the%20five%20lemma/near/125622974):
<p>Aah, yes. I should have done that</p>

#### [ Johan Commelin (Apr 24 2018 at 16:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proof%20of%20the%20five%20lemma/near/125623014):
<p>Also, can I use some <code>_</code> business to let it figure out the hypotheses itself?</p>

#### [ Kenny Lau (Apr 24 2018 at 16:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proof%20of%20the%20five%20lemma/near/125623020):
<p>yes</p>

#### [ Johan Commelin (Apr 24 2018 at 16:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proof%20of%20the%20five%20lemma/near/125623026):
<p>I tried... and failed <span class="emoji emoji-1f61e" title="disappointed">:disappointed:</span></p>

#### [ Kenny Lau (Apr 24 2018 at 16:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proof%20of%20the%20five%20lemma/near/125623032):
<p>you removed the wrong things :P</p>

#### [ Kenny Lau (Apr 24 2018 at 16:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proof%20of%20the%20five%20lemma/near/125623035):
<p><code>_</code> does not find the value from assumptions</p>

#### [ Kenny Lau (Apr 24 2018 at 16:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proof%20of%20the%20five%20lemma/near/125623036):
<p><code>_</code> only does unification</p>

#### [ Kenny Lau (Apr 24 2018 at 16:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proof%20of%20the%20five%20lemma/near/125623044):
<p>and only first order (and zeroth order) unification</p>

#### [ Johan Commelin (Apr 24 2018 at 16:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proof%20of%20the%20five%20lemma/near/125623109):
<p>Hmm, ok... But it should be able to figure out everything alone</p>

#### [ Johan Commelin (Apr 24 2018 at 16:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proof%20of%20the%20five%20lemma/near/125623111):
<p>I will need to learn at some point how to do that</p>

#### [ Kenny Lau (Apr 24 2018 at 16:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proof%20of%20the%20five%20lemma/near/125623112):
<p>it does <strong>not</strong> find the appropriate proofs from the asumptions</p>

#### [ Johan Commelin (Apr 24 2018 at 16:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proof%20of%20the%20five%20lemma/near/125623116):
<p>No, but I mean the <code>com₁ com₂ com₃ eB₁ eC₁ eB₂ eC₂ hj hk.1 hm.1</code> stuff</p>

#### [ Kenny Lau (Apr 24 2018 at 16:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proof%20of%20the%20five%20lemma/near/125623127):
<p>why would it be able to figure them out?</p>

#### [ Kenny Lau (Apr 24 2018 at 16:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proof%20of%20the%20five%20lemma/near/125623130):
<p>the goal is <code>bijective l</code></p>

#### [ Kenny Lau (Apr 24 2018 at 16:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proof%20of%20the%20five%20lemma/near/125623131):
<p>it does not contain any of those things you mentioned</p>

#### [ Kenny Lau (Apr 24 2018 at 16:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proof%20of%20the%20five%20lemma/near/125623137):
<p>they have to be found from the assumption list</p>

#### [ Kenny Lau (Apr 24 2018 at 16:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proof%20of%20the%20five%20lemma/near/125623139):
<p>which <code>_</code> does not do</p>

#### [ Kenny Lau (Apr 24 2018 at 16:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proof%20of%20the%20five%20lemma/near/125623142):
<p><code>_</code> only unifies types</p>

#### [ Johan Commelin (Apr 24 2018 at 16:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proof%20of%20the%20five%20lemma/near/125623144):
<p>Yes, and the type of <code>l</code> is <code>C_1 \to C_2</code></p>

#### [ Johan Commelin (Apr 24 2018 at 16:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proof%20of%20the%20five%20lemma/near/125623187):
<p>and those are mentioned in the statement, and there are requirements (e.g. a group <code>B_1</code> with a map to <code>C_1</code></p>

#### [ Kenny Lau (Apr 24 2018 at 16:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proof%20of%20the%20five%20lemma/near/125623188):
<p>but if you replace <code>com₁</code> with <code>_</code>, the compiler would have to find <code>com₁</code> from the assumptions</p>

#### [ Johan Commelin (Apr 24 2018 at 16:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proof%20of%20the%20five%20lemma/near/125623197):
<p>...), and those are also in the context, etcc...</p>

#### [ Kenny Lau (Apr 24 2018 at 16:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proof%20of%20the%20five%20lemma/near/125623204):
<p>it is not in the type of the goal</p>

#### [ Kenny Lau (Apr 24 2018 at 16:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proof%20of%20the%20five%20lemma/near/125623205):
<p>it is not in the type of any component of the goal</p>

#### [ Kenny Lau (Apr 24 2018 at 16:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proof%20of%20the%20five%20lemma/near/125623209):
<p><code>_</code> does not find things from the local context</p>

#### [ Kenny Lau (Apr 24 2018 at 16:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proof%20of%20the%20five%20lemma/near/125623211):
<p>(that is what I meant by assumption)</p>

#### [ Kenny Lau (Apr 24 2018 at 16:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proof%20of%20the%20five%20lemma/near/125623221):
<div class="codehilite"><pre><span></span><span class="n">H1</span> <span class="o">:</span> <span class="n">something</span>
<span class="n">H2</span> <span class="o">:</span> <span class="n">something</span>
<span class="bp">|-</span> <span class="n">goal</span>
</pre></div>

#### [ Kenny Lau (Apr 24 2018 at 16:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proof%20of%20the%20five%20lemma/near/125623222):
<p><code>_</code> does not match against <code>H1</code> and <code>H2</code></p>

#### [ Kenny Lau (Apr 24 2018 at 16:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proof%20of%20the%20five%20lemma/near/125623223):
<p>unless the <code>goal</code> contains them</p>

#### [ Johan Commelin (Apr 24 2018 at 16:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proof%20of%20the%20five%20lemma/near/125623228):
<p>I see</p>

#### [ Johan Commelin (Apr 24 2018 at 16:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proof%20of%20the%20five%20lemma/near/125623235):
<p>So, maybe I should not have done <code>apply ...</code>, but <code>simp [four_lemma_1]</code></p>

#### [ Johan Commelin (Apr 24 2018 at 16:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proof%20of%20the%20five%20lemma/near/125623238):
<p>or something like that?</p>

#### [ Kenny Lau (Apr 24 2018 at 16:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proof%20of%20the%20five%20lemma/near/125623278):
<p>does that work?</p>

#### [ Kenny Lau (Apr 24 2018 at 16:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proof%20of%20the%20five%20lemma/near/125623282):
<p>I doubt that works</p>

#### [ Kenny Lau (Apr 24 2018 at 16:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proof%20of%20the%20five%20lemma/near/125623284):
<p>try <code>apply four_lemma₁, repeat { assumption }</code></p>

#### [ Kenny Lau (Apr 24 2018 at 16:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proof%20of%20the%20five%20lemma/near/125623306):
<p>alternatively <code>apply four_lemma₁; try { assumption }</code></p>

#### [ Johan Commelin (Apr 24 2018 at 16:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proof%20of%20the%20five%20lemma/near/125623366):
<p>hmm, doesn't make it shorter... because it can't figure out <code>hk.1</code> on it's own...</p>

#### [ Kenny Lau (Apr 24 2018 at 16:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proof%20of%20the%20five%20lemma/near/125623369):
<p>right</p>

#### [ Johan Commelin (Apr 24 2018 at 16:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proof%20of%20the%20five%20lemma/near/125623373):
<p>never mind, I learned something (-;</p>

#### [ Kenny Lau (Apr 24 2018 at 16:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proof%20of%20the%20five%20lemma/near/125623377):
<p>:)</p>

#### [ Johan Commelin (Apr 24 2018 at 16:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proof%20of%20the%20five%20lemma/near/125623394):
<p>Next up: the snake lemma ???</p>

#### [ Kenny Lau (Apr 24 2018 at 16:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proof%20of%20the%20five%20lemma/near/125623399):
<p>I heard one of them follows from the other</p>

#### [ Johan Commelin (Apr 24 2018 at 16:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proof%20of%20the%20five%20lemma/near/125623443):
<p>I guess the snake lemma is stronger</p>

#### [ Kenny Lau (Apr 24 2018 at 16:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proof%20of%20the%20five%20lemma/near/125623451):
<p>maybe we should have proved the snake lemma first :P</p>

#### [ Johan Commelin (Apr 24 2018 at 16:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proof%20of%20the%20five%20lemma/near/125623455):
<p>lol</p>

#### [ Johan Commelin (Apr 24 2018 at 16:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proof%20of%20the%20five%20lemma/near/125623461):
<p>There is also the salamander lemma</p>

#### [ Johan Commelin (Apr 24 2018 at 16:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proof%20of%20the%20five%20lemma/near/125623470):
<p>And you can apply it 4 times to get the snake lemma</p>

#### [ Kenny Lau (Apr 24 2018 at 16:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proof%20of%20the%20five%20lemma/near/125623475):
<p>then perhaps we should prove that first</p>

#### [ Johan Commelin (Apr 24 2018 at 16:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proof%20of%20the%20five%20lemma/near/125623485):
<p><a href="https://ncatlab.org/nlab/show/salamander+lemma" target="_blank" title="https://ncatlab.org/nlab/show/salamander+lemma">https://ncatlab.org/nlab/show/salamander+lemma</a></p>

#### [ Johan Commelin (Apr 24 2018 at 16:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proof%20of%20the%20five%20lemma/near/125623491):
<p>My eyes always glaze over when I read that page</p>

#### [ Kenny Lau (Apr 24 2018 at 16:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proof%20of%20the%20five%20lemma/near/125623536):
<p>:P</p>

#### [ Kenny Lau (Apr 24 2018 at 16:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proof%20of%20the%20five%20lemma/near/125623572):
<p>really, prove the strongest theorem, and your work will be minimized</p>

#### [ Kevin Buzzard (Apr 27 2018 at 09:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proof%20of%20the%20five%20lemma/near/125762769):
<p>I need the three lemma</p>

#### [ Kevin Buzzard (Apr 27 2018 at 09:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proof%20of%20the%20five%20lemma/near/125762772):
<p>I need that if A,B,C,A',B',C' are abelian groups</p>

#### [ Kevin Buzzard (Apr 27 2018 at 09:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proof%20of%20the%20five%20lemma/near/125762773):
<p>and A -&gt; B -&gt; C is exact</p>

#### [ Kevin Buzzard (Apr 27 2018 at 09:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proof%20of%20the%20five%20lemma/near/125762776):
<p>and A is isomorphic to A'</p>

#### [ Kevin Buzzard (Apr 27 2018 at 09:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proof%20of%20the%20five%20lemma/near/125762777):
<p>and B to B'</p>

#### [ Kevin Buzzard (Apr 27 2018 at 09:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proof%20of%20the%20five%20lemma/near/125762778):
<p>and C to C'</p>

#### [ Kevin Buzzard (Apr 27 2018 at 09:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proof%20of%20the%20five%20lemma/near/125762780):
<p>and we have maps A' -&gt; B' -&gt; C'</p>

#### [ Kevin Buzzard (Apr 27 2018 at 09:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proof%20of%20the%20five%20lemma/near/125762782):
<p>with both squares commuting</p>

#### [ Kevin Buzzard (Apr 27 2018 at 09:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proof%20of%20the%20five%20lemma/near/125762821):
<p>then A' -&gt; B' -&gt; C' is exact</p>

#### [ Kevin Buzzard (Apr 27 2018 at 09:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proof%20of%20the%20five%20lemma/near/125762824):
<p>As a mathematician my instinct is to do surgery on the first sequence</p>

#### [ Kevin Buzzard (Apr 27 2018 at 09:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proof%20of%20the%20five%20lemma/near/125762825):
<p>i.e. simply replace A with A', B with B' and C with C' and then say we're done</p>

#### [ Kevin Buzzard (Apr 27 2018 at 09:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proof%20of%20the%20five%20lemma/near/125762832):
<p>I am trying to work out if there is a general principle here</p>

#### [ Kevin Buzzard (Apr 27 2018 at 09:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proof%20of%20the%20five%20lemma/near/125762873):
<p>but if there is, I don't think I can formulate it well in Lean yet.</p>

#### [ Kevin Buzzard (Apr 27 2018 at 09:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proof%20of%20the%20five%20lemma/near/125762884):
<p>It says something like "if there is a commutative diagram, and you do some computation like image of this over kernel of this"</p>

#### [ Kevin Buzzard (Apr 27 2018 at 09:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proof%20of%20the%20five%20lemma/near/125762891):
<p>"and then you take a term in the commutative diagram and replace it with an isomorphic term such that all the diagrams commute"</p>

#### [ Kevin Buzzard (Apr 27 2018 at 09:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proof%20of%20the%20five%20lemma/near/125762893):
<p>"then the computation changes in the same way"</p>

#### [ Kevin Buzzard (Apr 27 2018 at 09:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proof%20of%20the%20five%20lemma/near/125762899):
<p>but I fear that I am going to have to use three lemmas to prove the three lemma</p>

#### [ Kevin Buzzard (Apr 27 2018 at 09:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proof%20of%20the%20five%20lemma/near/125762900):
<p>one for replacing A</p>

#### [ Kevin Buzzard (Apr 27 2018 at 09:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proof%20of%20the%20five%20lemma/near/125762901):
<p>one for B</p>

#### [ Kevin Buzzard (Apr 27 2018 at 09:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proof%20of%20the%20five%20lemma/near/125762902):
<p>and one for C</p>

#### [ Kevin Buzzard (Apr 27 2018 at 09:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proof%20of%20the%20five%20lemma/near/125762955):
<p>or just prove it by brute force in one go</p>

#### [ Kevin Buzzard (Apr 27 2018 at 09:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proof%20of%20the%20five%20lemma/near/125762956):
<p>and then deal with the fact that I'll need another trivial lemma of this form tomorrow, tomorrow</p>

#### [ Kevin Buzzard (Apr 27 2018 at 09:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proof%20of%20the%20five%20lemma/near/125762958):
<p>I want more of this abstract nonsense in Lean</p>

#### [ Kevin Buzzard (Apr 27 2018 at 09:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proof%20of%20the%20five%20lemma/near/125762959):
<p>either for abelian groups</p>

#### [ Kevin Buzzard (Apr 27 2018 at 09:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proof%20of%20the%20five%20lemma/near/125762999):
<p>or for abelian categories</p>

#### [ Johan Commelin (Apr 27 2018 at 09:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proof%20of%20the%20five%20lemma/near/125763020):
<p>Hmm, I'm sorry that my five lemma doesn't help <span class="emoji emoji-1f641" title="slightly frowning face">:slightly_frowning_face:</span></p>

#### [ Kevin Buzzard (Apr 27 2018 at 09:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proof%20of%20the%20five%20lemma/near/125763021):
<p>yes, it's too strong :-)</p>

#### [ Kevin Buzzard (Apr 27 2018 at 09:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proof%20of%20the%20five%20lemma/near/125763023):
<p>it proves something non-trivial</p>

#### [ Johan Commelin (Apr 27 2018 at 09:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proof%20of%20the%20five%20lemma/near/125763028):
<p>Haha</p>

#### [ Johan Commelin (Apr 27 2018 at 09:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proof%20of%20the%20five%20lemma/near/125763070):
<p>We need a very good way of substituting isomorphic things</p>

#### [ Kevin Buzzard (Apr 27 2018 at 09:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proof%20of%20the%20five%20lemma/near/125763071):
<p><code>rw</code> :-)</p>

#### [ Johan Commelin (Apr 27 2018 at 09:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proof%20of%20the%20five%20lemma/near/125763072):
<p>I don't know much about HoTT, but I think this is what Voevodsky was after as well</p>

#### [ Kevin Buzzard (Apr 27 2018 at 09:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proof%20of%20the%20five%20lemma/near/125763073):
<p>yes</p>

#### [ Kevin Buzzard (Apr 27 2018 at 09:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proof%20of%20the%20five%20lemma/near/125763074):
<p>I wrote some vague mumblings about that in some other thread a week or so ago</p>

#### [ Kevin Buzzard (Apr 27 2018 at 09:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proof%20of%20the%20five%20lemma/near/125763075):
<p>after reading some of his work</p>

#### [ Kevin Buzzard (Apr 27 2018 at 09:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proof%20of%20the%20five%20lemma/near/125763081):
<p>but he redefined =</p>

#### [ Johan Commelin (Apr 27 2018 at 09:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proof%20of%20the%20five%20lemma/near/125763085):
<p>Well, if you're changing from ZFC to type theory, might as well change '='</p>

#### [ Johan Commelin (Apr 27 2018 at 09:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proof%20of%20the%20five%20lemma/near/125763124):
<p>Anyway, I guess that you are not saved by 5 <code>rw</code>s</p>

#### [ Johan Commelin (Apr 27 2018 at 09:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proof%20of%20the%20five%20lemma/near/125763137):
<p>So we need <span class="user-mention" data-user-id="110524">@Scott Morrison</span> 's category theory, and then some strong tactics that know about commutative diagrams</p>

#### [ Johan Commelin (Apr 27 2018 at 09:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proof%20of%20the%20five%20lemma/near/125763339):
<p>Or are you just going for a temporary brute force approach?</p>

#### [ Kenny Lau (Apr 27 2018 at 12:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proof%20of%20the%20five%20lemma/near/125767661):
<div class="codehilite"><pre><span></span><span class="kn">import</span> <span class="n">algebra</span><span class="bp">.</span><span class="n">group</span> <span class="n">data</span><span class="bp">.</span><span class="n">set</span> <span class="n">data</span><span class="bp">.</span><span class="n">equiv</span>

<span class="n">def</span> <span class="n">is_add_group_hom</span> <span class="o">{</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span><span class="bp">*</span><span class="o">}</span> <span class="o">{</span><span class="n">β</span> <span class="o">:</span> <span class="kt">Type</span><span class="bp">*</span><span class="o">}</span> <span class="o">[</span><span class="n">add_group</span> <span class="n">α</span><span class="o">]</span> <span class="o">[</span><span class="n">add_group</span> <span class="n">β</span><span class="o">]</span> <span class="o">(</span><span class="n">f</span> <span class="o">:</span> <span class="n">α</span> <span class="bp">→</span> <span class="n">β</span><span class="o">)</span> <span class="o">:</span> <span class="kt">Prop</span> <span class="o">:=</span>
<span class="bp">@</span><span class="n">is_group_hom</span> <span class="o">(</span><span class="n">multiplicative</span> <span class="n">α</span><span class="o">)</span> <span class="o">(</span><span class="n">multiplicative</span> <span class="n">β</span><span class="o">)</span> <span class="bp">_</span> <span class="bp">_</span> <span class="n">f</span>

<span class="n">attribute</span> <span class="o">[</span><span class="n">class</span><span class="o">]</span> <span class="n">is_add_group_hom</span>

<span class="kn">namespace</span> <span class="n">is_add_group_hom</span>

<span class="kn">variables</span> <span class="o">{</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span><span class="bp">*</span><span class="o">}</span> <span class="o">{</span><span class="n">β</span> <span class="o">:</span> <span class="kt">Type</span><span class="bp">*</span><span class="o">}</span> <span class="o">[</span><span class="n">add_group</span> <span class="n">α</span><span class="o">]</span> <span class="o">[</span><span class="n">add_group</span> <span class="n">β</span><span class="o">]</span> <span class="o">(</span><span class="n">f</span> <span class="o">:</span> <span class="n">α</span> <span class="bp">→</span> <span class="n">β</span><span class="o">)</span> <span class="o">[</span><span class="n">hf</span> <span class="o">:</span> <span class="n">is_add_group_hom</span> <span class="n">f</span><span class="o">]</span>

<span class="kn">theorem</span> <span class="n">mk</span> <span class="o">(</span><span class="n">H</span> <span class="o">:</span> <span class="bp">∀</span> <span class="n">x</span> <span class="n">y</span><span class="o">,</span> <span class="n">f</span> <span class="o">(</span><span class="n">x</span> <span class="bp">+</span> <span class="n">y</span><span class="o">)</span> <span class="bp">=</span> <span class="n">f</span> <span class="n">x</span> <span class="bp">+</span> <span class="n">f</span> <span class="n">y</span><span class="o">)</span> <span class="o">:</span> <span class="n">is_add_group_hom</span> <span class="n">f</span> <span class="o">:=</span>
<span class="bp">⟨</span><span class="n">H</span><span class="bp">⟩</span>

<span class="kn">theorem</span> <span class="n">add</span> <span class="o">(</span><span class="n">x</span> <span class="n">y</span><span class="o">)</span> <span class="o">:</span> <span class="n">f</span> <span class="o">(</span><span class="n">x</span> <span class="bp">+</span> <span class="n">y</span><span class="o">)</span> <span class="bp">=</span> <span class="n">f</span> <span class="n">x</span> <span class="bp">+</span> <span class="n">f</span> <span class="n">y</span> <span class="o">:=</span>
<span class="bp">@</span><span class="n">is_group_hom</span><span class="bp">.</span><span class="n">mul</span> <span class="o">(</span><span class="n">multiplicative</span> <span class="n">α</span><span class="o">)</span> <span class="o">(</span><span class="n">multiplicative</span> <span class="n">β</span><span class="o">)</span> <span class="bp">_</span> <span class="bp">_</span> <span class="n">f</span> <span class="n">hf</span> <span class="n">x</span> <span class="n">y</span>

<span class="kn">theorem</span> <span class="n">zero</span> <span class="o">:</span> <span class="n">f</span> <span class="mi">0</span> <span class="bp">=</span> <span class="mi">0</span> <span class="o">:=</span>
<span class="bp">@</span><span class="n">is_group_hom</span><span class="bp">.</span><span class="n">one</span> <span class="o">(</span><span class="n">multiplicative</span> <span class="n">α</span><span class="o">)</span> <span class="o">(</span><span class="n">multiplicative</span> <span class="n">β</span><span class="o">)</span> <span class="bp">_</span> <span class="bp">_</span> <span class="n">f</span> <span class="n">hf</span>

<span class="kn">theorem</span> <span class="n">neg</span> <span class="o">(</span><span class="n">x</span><span class="o">)</span> <span class="o">:</span> <span class="n">f</span> <span class="o">(</span><span class="bp">-</span><span class="n">x</span><span class="o">)</span> <span class="bp">=</span> <span class="bp">-</span><span class="n">f</span> <span class="n">x</span> <span class="o">:=</span>
<span class="bp">@</span><span class="n">is_group_hom</span><span class="bp">.</span><span class="n">inv</span> <span class="o">(</span><span class="n">multiplicative</span> <span class="n">α</span><span class="o">)</span> <span class="o">(</span><span class="n">multiplicative</span> <span class="n">β</span><span class="o">)</span> <span class="bp">_</span> <span class="bp">_</span> <span class="n">f</span> <span class="n">hf</span> <span class="n">x</span>

<span class="n">def</span> <span class="n">ker</span> <span class="o">:</span> <span class="n">set</span> <span class="n">α</span> <span class="o">:=</span>
<span class="o">{</span> <span class="n">x</span> <span class="bp">|</span> <span class="n">f</span> <span class="n">x</span> <span class="bp">=</span> <span class="mi">0</span> <span class="o">}</span>

<span class="kn">end</span> <span class="n">is_add_group_hom</span>

<span class="kn">theorem</span> <span class="n">three</span> <span class="o">(</span><span class="n">A</span> <span class="n">B</span> <span class="n">C</span> <span class="n">A&#39;</span> <span class="n">B&#39;</span> <span class="n">C&#39;</span> <span class="o">:</span> <span class="kt">Type</span><span class="bp">*</span><span class="o">)</span>
  <span class="o">[</span><span class="n">add_comm_group</span> <span class="n">A</span><span class="o">]</span> <span class="o">[</span><span class="n">add_comm_group</span> <span class="n">A&#39;</span><span class="o">]</span>
  <span class="o">[</span><span class="n">add_comm_group</span> <span class="n">B</span><span class="o">]</span> <span class="o">[</span><span class="n">add_comm_group</span> <span class="n">B&#39;</span><span class="o">]</span>
  <span class="o">[</span><span class="n">add_comm_group</span> <span class="n">C</span><span class="o">]</span> <span class="o">[</span><span class="n">add_comm_group</span> <span class="n">C&#39;</span><span class="o">]</span>
  <span class="o">(</span><span class="n">ab</span> <span class="o">:</span> <span class="n">A</span> <span class="bp">→</span> <span class="n">B</span><span class="o">)</span> <span class="o">[</span><span class="n">is_add_group_hom</span> <span class="n">ab</span><span class="o">]</span>
  <span class="o">(</span><span class="n">bc</span> <span class="o">:</span> <span class="n">B</span> <span class="bp">→</span> <span class="n">C</span><span class="o">)</span> <span class="o">[</span><span class="n">is_add_group_hom</span> <span class="n">bc</span><span class="o">]</span>
  <span class="o">(</span><span class="n">Habc</span> <span class="o">:</span> <span class="n">set</span><span class="bp">.</span><span class="n">range</span> <span class="n">ab</span> <span class="bp">=</span> <span class="n">is_add_group_hom</span><span class="bp">.</span><span class="n">ker</span> <span class="n">bc</span><span class="o">)</span>
  <span class="o">(</span><span class="n">fa</span> <span class="o">:</span> <span class="n">A</span> <span class="err">≃</span> <span class="n">A&#39;</span><span class="o">)</span> <span class="o">[</span><span class="n">is_add_group_hom</span> <span class="n">fa</span><span class="o">]</span>
  <span class="o">(</span><span class="n">fb</span> <span class="o">:</span> <span class="n">B</span> <span class="err">≃</span> <span class="n">B&#39;</span><span class="o">)</span> <span class="o">[</span><span class="n">is_add_group_hom</span> <span class="n">fb</span><span class="o">]</span>
  <span class="o">(</span><span class="n">fc</span> <span class="o">:</span> <span class="n">C</span> <span class="err">≃</span> <span class="n">C&#39;</span><span class="o">)</span> <span class="o">[</span><span class="n">is_add_group_hom</span> <span class="n">fc</span><span class="o">]</span>

  <span class="o">(</span><span class="n">ab&#39;</span> <span class="o">:</span> <span class="n">A&#39;</span> <span class="bp">→</span> <span class="n">B&#39;</span><span class="o">)</span> <span class="o">[</span><span class="n">is_add_group_hom</span> <span class="n">ab&#39;</span><span class="o">]</span>
  <span class="o">(</span><span class="n">bc&#39;</span> <span class="o">:</span> <span class="n">B&#39;</span> <span class="bp">→</span> <span class="n">C&#39;</span><span class="o">)</span> <span class="o">[</span><span class="n">is_add_group_hom</span> <span class="n">bc&#39;</span><span class="o">]</span>
  <span class="o">(</span><span class="n">H1</span> <span class="o">:</span> <span class="n">fb</span> <span class="err">∘</span> <span class="n">ab</span> <span class="bp">=</span> <span class="n">ab&#39;</span> <span class="err">∘</span> <span class="n">fa</span><span class="o">)</span>
  <span class="o">(</span><span class="n">H2</span> <span class="o">:</span> <span class="n">fc</span> <span class="err">∘</span> <span class="n">bc</span> <span class="bp">=</span> <span class="n">bc&#39;</span> <span class="err">∘</span> <span class="n">fb</span><span class="o">)</span> <span class="o">:</span>

  <span class="n">set</span><span class="bp">.</span><span class="n">range</span> <span class="n">ab&#39;</span> <span class="bp">=</span> <span class="n">is_add_group_hom</span><span class="bp">.</span><span class="n">ker</span> <span class="n">bc&#39;</span> <span class="o">:=</span>
<span class="k">begin</span>
  <span class="n">apply</span> <span class="n">set</span><span class="bp">.</span><span class="n">ext</span><span class="o">,</span>
  <span class="n">intro</span> <span class="n">b&#39;</span><span class="o">,</span>
  <span class="n">split</span><span class="o">,</span>
  <span class="o">{</span> <span class="n">intro</span> <span class="n">hb&#39;</span><span class="o">,</span>
    <span class="n">cases</span> <span class="n">hb&#39;</span> <span class="k">with</span> <span class="n">a&#39;</span> <span class="n">ha&#39;</span><span class="o">,</span>
    <span class="n">simp</span> <span class="o">[</span><span class="n">is_add_group_hom</span><span class="bp">.</span><span class="n">ker</span><span class="o">],</span>
    <span class="k">let</span> <span class="n">a</span> <span class="o">:=</span> <span class="n">fa</span><span class="bp">.</span><span class="n">symm</span> <span class="n">a&#39;</span><span class="o">,</span>
    <span class="k">have</span> <span class="n">ha</span> <span class="o">:</span> <span class="n">fa</span> <span class="n">a</span> <span class="bp">=</span> <span class="n">a&#39;</span><span class="o">,</span>
    <span class="o">{</span> <span class="n">simp</span> <span class="o">[</span><span class="n">a</span><span class="o">]</span> <span class="o">},</span>
    <span class="n">rw</span> <span class="o">[</span><span class="err">←</span> <span class="n">ha&#39;</span><span class="o">,</span> <span class="err">←</span> <span class="n">ha</span><span class="o">],</span>
    <span class="n">change</span> <span class="n">bc&#39;</span> <span class="o">((</span><span class="n">ab&#39;</span> <span class="err">∘</span> <span class="n">fa</span><span class="o">)</span> <span class="n">a</span><span class="o">)</span> <span class="bp">=</span> <span class="mi">0</span><span class="o">,</span>
    <span class="n">rw</span> <span class="err">←</span> <span class="n">H1</span><span class="o">,</span>
    <span class="n">change</span> <span class="o">(</span><span class="n">bc&#39;</span> <span class="err">∘</span> <span class="n">fb</span><span class="o">)</span> <span class="o">(</span><span class="n">ab</span> <span class="n">a</span><span class="o">)</span> <span class="bp">=</span> <span class="mi">0</span><span class="o">,</span>
    <span class="n">rw</span> <span class="err">←</span> <span class="n">H2</span><span class="o">,</span>
    <span class="k">have</span> <span class="n">H3</span> <span class="o">:</span> <span class="n">ab</span> <span class="n">a</span> <span class="err">∈</span> <span class="n">is_add_group_hom</span><span class="bp">.</span><span class="n">ker</span> <span class="n">bc</span><span class="o">,</span>
    <span class="o">{</span> <span class="n">rw</span> <span class="err">←</span> <span class="n">Habc</span><span class="o">,</span> <span class="n">existsi</span> <span class="n">a</span><span class="o">,</span> <span class="n">simp</span> <span class="o">},</span>
    <span class="n">simp</span> <span class="o">[</span><span class="n">is_add_group_hom</span><span class="bp">.</span><span class="n">ker</span><span class="o">]</span> <span class="n">at</span> <span class="n">H3</span> <span class="err">⊢</span><span class="o">,</span>
    <span class="n">rw</span> <span class="n">H3</span><span class="o">,</span>
    <span class="n">apply</span> <span class="n">is_add_group_hom</span><span class="bp">.</span><span class="n">zero</span> <span class="o">},</span>
  <span class="o">{</span> <span class="n">intro</span> <span class="n">hb&#39;</span><span class="o">,</span>
    <span class="k">let</span> <span class="n">b</span> <span class="o">:=</span> <span class="n">fb</span><span class="bp">.</span><span class="n">symm</span> <span class="n">b&#39;</span><span class="o">,</span>
    <span class="k">have</span> <span class="n">hb</span> <span class="o">:</span> <span class="n">fb</span> <span class="n">b</span> <span class="bp">=</span> <span class="n">b&#39;</span><span class="o">,</span>
    <span class="o">{</span> <span class="n">simp</span> <span class="o">[</span><span class="n">b</span><span class="o">]</span> <span class="o">},</span>
    <span class="n">simp</span> <span class="o">[</span><span class="n">is_add_group_hom</span><span class="bp">.</span><span class="n">ker</span><span class="o">]</span> <span class="n">at</span> <span class="n">hb&#39;</span><span class="o">,</span>
    <span class="n">rw</span> <span class="err">←</span> <span class="n">hb</span> <span class="n">at</span> <span class="n">hb&#39;</span><span class="o">,</span>
    <span class="n">change</span> <span class="o">(</span><span class="n">bc&#39;</span> <span class="err">∘</span> <span class="n">fb</span><span class="o">)</span> <span class="n">b</span> <span class="bp">=</span> <span class="mi">0</span> <span class="n">at</span> <span class="n">hb&#39;</span><span class="o">,</span>
    <span class="n">rw</span> <span class="err">←</span> <span class="n">H2</span> <span class="n">at</span> <span class="n">hb&#39;</span><span class="o">,</span>
    <span class="n">rw</span> <span class="err">←</span> <span class="n">is_add_group_hom</span><span class="bp">.</span><span class="n">zero</span> <span class="n">fc</span> <span class="n">at</span> <span class="n">hb&#39;</span><span class="o">,</span>
    <span class="n">replace</span> <span class="n">hb&#39;</span> <span class="o">:=</span> <span class="n">congr_arg</span> <span class="n">fc</span><span class="bp">.</span><span class="n">symm</span> <span class="n">hb&#39;</span><span class="o">,</span>
    <span class="n">simp</span> <span class="n">at</span> <span class="n">hb&#39;</span><span class="o">,</span>
    <span class="k">have</span> <span class="n">H3</span> <span class="o">:</span> <span class="n">b</span> <span class="err">∈</span> <span class="n">set</span><span class="bp">.</span><span class="n">range</span> <span class="n">ab</span><span class="o">,</span>
    <span class="o">{</span> <span class="n">rwa</span> <span class="n">Habc</span> <span class="o">},</span>
    <span class="n">cases</span> <span class="n">H3</span> <span class="k">with</span> <span class="n">a</span> <span class="n">ha</span><span class="o">,</span>
    <span class="n">existsi</span> <span class="n">fa</span> <span class="n">a</span><span class="o">,</span>
    <span class="n">change</span> <span class="o">(</span><span class="n">ab&#39;</span> <span class="err">∘</span> <span class="n">fa</span><span class="o">)</span> <span class="n">a</span> <span class="bp">=</span> <span class="n">b&#39;</span><span class="o">,</span>
    <span class="n">rw</span> <span class="err">←</span> <span class="n">H1</span><span class="o">,</span>
    <span class="n">simp</span> <span class="o">[</span><span class="n">ha</span><span class="o">]</span> <span class="o">}</span>
<span class="kn">end</span>
</pre></div>

#### [ Kenny Lau (Apr 27 2018 at 12:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proof%20of%20the%20five%20lemma/near/125767698):
<p><span class="user-mention" data-user-id="110038">@Kevin Buzzard</span></p>

#### [ Kenny Lau (Apr 27 2018 at 12:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proof%20of%20the%20five%20lemma/near/125768067):
<p>that's why I don't like stating equality with function composition</p>

#### [ Kenny Lau (Apr 27 2018 at 12:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proof%20of%20the%20five%20lemma/near/125768238):
<div class="codehilite"><pre><span></span><span class="kn">import</span> <span class="n">algebra</span><span class="bp">.</span><span class="n">group</span> <span class="n">data</span><span class="bp">.</span><span class="n">set</span> <span class="n">data</span><span class="bp">.</span><span class="n">equiv</span>

<span class="n">def</span> <span class="n">is_add_group_hom</span> <span class="o">{</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span><span class="bp">*</span><span class="o">}</span> <span class="o">{</span><span class="n">β</span> <span class="o">:</span> <span class="kt">Type</span><span class="bp">*</span><span class="o">}</span> <span class="o">[</span><span class="n">add_group</span> <span class="n">α</span><span class="o">]</span> <span class="o">[</span><span class="n">add_group</span> <span class="n">β</span><span class="o">]</span> <span class="o">(</span><span class="n">f</span> <span class="o">:</span> <span class="n">α</span> <span class="bp">→</span> <span class="n">β</span><span class="o">)</span> <span class="o">:</span> <span class="kt">Prop</span> <span class="o">:=</span>
<span class="bp">@</span><span class="n">is_group_hom</span> <span class="o">(</span><span class="n">multiplicative</span> <span class="n">α</span><span class="o">)</span> <span class="o">(</span><span class="n">multiplicative</span> <span class="n">β</span><span class="o">)</span> <span class="bp">_</span> <span class="bp">_</span> <span class="n">f</span>

<span class="n">attribute</span> <span class="o">[</span><span class="n">class</span><span class="o">]</span> <span class="n">is_add_group_hom</span>

<span class="kn">namespace</span> <span class="n">is_add_group_hom</span>

<span class="kn">variables</span> <span class="o">{</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span><span class="bp">*</span><span class="o">}</span> <span class="o">{</span><span class="n">β</span> <span class="o">:</span> <span class="kt">Type</span><span class="bp">*</span><span class="o">}</span> <span class="o">[</span><span class="n">add_group</span> <span class="n">α</span><span class="o">]</span> <span class="o">[</span><span class="n">add_group</span> <span class="n">β</span><span class="o">]</span> <span class="o">(</span><span class="n">f</span> <span class="o">:</span> <span class="n">α</span> <span class="bp">→</span> <span class="n">β</span><span class="o">)</span> <span class="o">[</span><span class="n">hf</span> <span class="o">:</span> <span class="n">is_add_group_hom</span> <span class="n">f</span><span class="o">]</span>

<span class="kn">theorem</span> <span class="n">mk</span> <span class="o">(</span><span class="n">H</span> <span class="o">:</span> <span class="bp">∀</span> <span class="n">x</span> <span class="n">y</span><span class="o">,</span> <span class="n">f</span> <span class="o">(</span><span class="n">x</span> <span class="bp">+</span> <span class="n">y</span><span class="o">)</span> <span class="bp">=</span> <span class="n">f</span> <span class="n">x</span> <span class="bp">+</span> <span class="n">f</span> <span class="n">y</span><span class="o">)</span> <span class="o">:</span> <span class="n">is_add_group_hom</span> <span class="n">f</span> <span class="o">:=</span>
<span class="bp">⟨</span><span class="n">H</span><span class="bp">⟩</span>

<span class="kn">theorem</span> <span class="n">add</span> <span class="o">(</span><span class="n">x</span> <span class="n">y</span><span class="o">)</span> <span class="o">:</span> <span class="n">f</span> <span class="o">(</span><span class="n">x</span> <span class="bp">+</span> <span class="n">y</span><span class="o">)</span> <span class="bp">=</span> <span class="n">f</span> <span class="n">x</span> <span class="bp">+</span> <span class="n">f</span> <span class="n">y</span> <span class="o">:=</span>
<span class="bp">@</span><span class="n">is_group_hom</span><span class="bp">.</span><span class="n">mul</span> <span class="o">(</span><span class="n">multiplicative</span> <span class="n">α</span><span class="o">)</span> <span class="o">(</span><span class="n">multiplicative</span> <span class="n">β</span><span class="o">)</span> <span class="bp">_</span> <span class="bp">_</span> <span class="n">f</span> <span class="n">hf</span> <span class="n">x</span> <span class="n">y</span>

<span class="kn">theorem</span> <span class="n">zero</span> <span class="o">:</span> <span class="n">f</span> <span class="mi">0</span> <span class="bp">=</span> <span class="mi">0</span> <span class="o">:=</span>
<span class="bp">@</span><span class="n">is_group_hom</span><span class="bp">.</span><span class="n">one</span> <span class="o">(</span><span class="n">multiplicative</span> <span class="n">α</span><span class="o">)</span> <span class="o">(</span><span class="n">multiplicative</span> <span class="n">β</span><span class="o">)</span> <span class="bp">_</span> <span class="bp">_</span> <span class="n">f</span> <span class="n">hf</span>

<span class="kn">theorem</span> <span class="n">neg</span> <span class="o">(</span><span class="n">x</span><span class="o">)</span> <span class="o">:</span> <span class="n">f</span> <span class="o">(</span><span class="bp">-</span><span class="n">x</span><span class="o">)</span> <span class="bp">=</span> <span class="bp">-</span><span class="n">f</span> <span class="n">x</span> <span class="o">:=</span>
<span class="bp">@</span><span class="n">is_group_hom</span><span class="bp">.</span><span class="n">inv</span> <span class="o">(</span><span class="n">multiplicative</span> <span class="n">α</span><span class="o">)</span> <span class="o">(</span><span class="n">multiplicative</span> <span class="n">β</span><span class="o">)</span> <span class="bp">_</span> <span class="bp">_</span> <span class="n">f</span> <span class="n">hf</span> <span class="n">x</span>

<span class="n">def</span> <span class="n">ker</span> <span class="o">:</span> <span class="n">set</span> <span class="n">α</span> <span class="o">:=</span>
<span class="o">{</span> <span class="n">x</span> <span class="bp">|</span> <span class="n">f</span> <span class="n">x</span> <span class="bp">=</span> <span class="mi">0</span> <span class="o">}</span>

<span class="kn">end</span> <span class="n">is_add_group_hom</span>

<span class="kn">theorem</span> <span class="n">three</span> <span class="o">(</span><span class="n">A</span> <span class="n">B</span> <span class="n">C</span> <span class="n">A&#39;</span> <span class="n">B&#39;</span> <span class="n">C&#39;</span> <span class="o">:</span> <span class="kt">Type</span><span class="bp">*</span><span class="o">)</span>
  <span class="o">[</span><span class="n">add_comm_group</span> <span class="n">A</span><span class="o">]</span> <span class="o">[</span><span class="n">add_comm_group</span> <span class="n">A&#39;</span><span class="o">]</span>
  <span class="o">[</span><span class="n">add_comm_group</span> <span class="n">B</span><span class="o">]</span> <span class="o">[</span><span class="n">add_comm_group</span> <span class="n">B&#39;</span><span class="o">]</span>
  <span class="o">[</span><span class="n">add_comm_group</span> <span class="n">C</span><span class="o">]</span> <span class="o">[</span><span class="n">add_comm_group</span> <span class="n">C&#39;</span><span class="o">]</span>
  <span class="o">(</span><span class="n">ab</span> <span class="o">:</span> <span class="n">A</span> <span class="bp">→</span> <span class="n">B</span><span class="o">)</span> <span class="o">[</span><span class="n">is_add_group_hom</span> <span class="n">ab</span><span class="o">]</span>
  <span class="o">(</span><span class="n">bc</span> <span class="o">:</span> <span class="n">B</span> <span class="bp">→</span> <span class="n">C</span><span class="o">)</span> <span class="o">[</span><span class="n">is_add_group_hom</span> <span class="n">bc</span><span class="o">]</span>
  <span class="o">(</span><span class="n">Habc</span> <span class="o">:</span> <span class="n">set</span><span class="bp">.</span><span class="n">range</span> <span class="n">ab</span> <span class="bp">=</span> <span class="n">is_add_group_hom</span><span class="bp">.</span><span class="n">ker</span> <span class="n">bc</span><span class="o">)</span>
  <span class="o">(</span><span class="n">fa</span> <span class="o">:</span> <span class="n">A</span> <span class="err">≃</span> <span class="n">A&#39;</span><span class="o">)</span> <span class="o">[</span><span class="n">is_add_group_hom</span> <span class="n">fa</span><span class="o">]</span>
  <span class="o">(</span><span class="n">fb</span> <span class="o">:</span> <span class="n">B</span> <span class="err">≃</span> <span class="n">B&#39;</span><span class="o">)</span> <span class="o">[</span><span class="n">is_add_group_hom</span> <span class="n">fb</span><span class="o">]</span>
  <span class="o">(</span><span class="n">fc</span> <span class="o">:</span> <span class="n">C</span> <span class="err">≃</span> <span class="n">C&#39;</span><span class="o">)</span> <span class="o">[</span><span class="n">is_add_group_hom</span> <span class="n">fc</span><span class="o">]</span>

  <span class="o">(</span><span class="n">ab&#39;</span> <span class="o">:</span> <span class="n">A&#39;</span> <span class="bp">→</span> <span class="n">B&#39;</span><span class="o">)</span> <span class="o">[</span><span class="n">is_add_group_hom</span> <span class="n">ab&#39;</span><span class="o">]</span>
  <span class="o">(</span><span class="n">bc&#39;</span> <span class="o">:</span> <span class="n">B&#39;</span> <span class="bp">→</span> <span class="n">C&#39;</span><span class="o">)</span> <span class="o">[</span><span class="n">is_add_group_hom</span> <span class="n">bc&#39;</span><span class="o">]</span>
  <span class="o">(</span><span class="n">H1</span> <span class="o">:</span> <span class="bp">∀</span> <span class="n">a</span><span class="o">,</span> <span class="n">fb</span> <span class="o">(</span><span class="n">ab</span> <span class="n">a</span><span class="o">)</span> <span class="bp">=</span> <span class="n">ab&#39;</span> <span class="o">(</span><span class="n">fa</span> <span class="n">a</span><span class="o">))</span>
  <span class="o">(</span><span class="n">H2</span> <span class="o">:</span> <span class="bp">∀</span> <span class="n">b</span><span class="o">,</span> <span class="n">fc</span> <span class="o">(</span><span class="n">bc</span> <span class="n">b</span><span class="o">)</span> <span class="bp">=</span> <span class="n">bc&#39;</span> <span class="o">(</span><span class="n">fb</span> <span class="n">b</span><span class="o">))</span> <span class="o">:</span>

  <span class="n">set</span><span class="bp">.</span><span class="n">range</span> <span class="n">ab&#39;</span> <span class="bp">=</span> <span class="n">is_add_group_hom</span><span class="bp">.</span><span class="n">ker</span> <span class="n">bc&#39;</span> <span class="o">:=</span>
<span class="k">begin</span>
  <span class="n">apply</span> <span class="n">set</span><span class="bp">.</span><span class="n">ext</span><span class="o">,</span>
  <span class="n">intro</span> <span class="n">b&#39;</span><span class="o">,</span>
  <span class="n">split</span><span class="o">,</span>
  <span class="o">{</span> <span class="n">intro</span> <span class="n">hb&#39;</span><span class="o">,</span>
    <span class="n">cases</span> <span class="n">hb&#39;</span> <span class="k">with</span> <span class="n">a&#39;</span> <span class="n">ha&#39;</span><span class="o">,</span>
    <span class="n">simp</span> <span class="o">[</span><span class="n">is_add_group_hom</span><span class="bp">.</span><span class="n">ker</span><span class="o">],</span>
    <span class="k">let</span> <span class="n">a</span> <span class="o">:=</span> <span class="n">fa</span><span class="bp">.</span><span class="n">symm</span> <span class="n">a&#39;</span><span class="o">,</span>
    <span class="k">have</span> <span class="n">ha</span> <span class="o">:</span> <span class="n">fa</span> <span class="n">a</span> <span class="bp">=</span> <span class="n">a&#39;</span><span class="o">,</span>
    <span class="o">{</span> <span class="n">simp</span> <span class="o">[</span><span class="n">a</span><span class="o">]</span> <span class="o">},</span>
    <span class="n">rw</span> <span class="o">[</span><span class="err">←</span> <span class="n">ha&#39;</span><span class="o">,</span> <span class="err">←</span> <span class="n">ha</span><span class="o">,</span> <span class="err">←</span> <span class="n">H1</span><span class="o">,</span> <span class="err">←</span> <span class="n">H2</span><span class="o">],</span>
    <span class="k">have</span> <span class="n">H3</span> <span class="o">:</span> <span class="n">ab</span> <span class="n">a</span> <span class="err">∈</span> <span class="n">is_add_group_hom</span><span class="bp">.</span><span class="n">ker</span> <span class="n">bc</span><span class="o">,</span>
    <span class="o">{</span> <span class="n">rw</span> <span class="err">←</span> <span class="n">Habc</span><span class="o">,</span> <span class="n">existsi</span> <span class="n">a</span><span class="o">,</span> <span class="n">simp</span> <span class="o">},</span>
    <span class="n">simp</span> <span class="o">[</span><span class="n">is_add_group_hom</span><span class="bp">.</span><span class="n">ker</span><span class="o">]</span> <span class="n">at</span> <span class="n">H3</span> <span class="err">⊢</span><span class="o">,</span>
    <span class="n">rw</span> <span class="n">H3</span><span class="o">,</span>
    <span class="n">apply</span> <span class="n">is_add_group_hom</span><span class="bp">.</span><span class="n">zero</span> <span class="o">},</span>
  <span class="o">{</span> <span class="n">intro</span> <span class="n">hb&#39;</span><span class="o">,</span>
    <span class="k">let</span> <span class="n">b</span> <span class="o">:=</span> <span class="n">fb</span><span class="bp">.</span><span class="n">symm</span> <span class="n">b&#39;</span><span class="o">,</span>
    <span class="k">have</span> <span class="n">hb</span> <span class="o">:</span> <span class="n">fb</span> <span class="n">b</span> <span class="bp">=</span> <span class="n">b&#39;</span><span class="o">,</span>
    <span class="o">{</span> <span class="n">simp</span> <span class="o">[</span><span class="n">b</span><span class="o">]</span> <span class="o">},</span>
    <span class="n">simp</span> <span class="o">[</span><span class="n">is_add_group_hom</span><span class="bp">.</span><span class="n">ker</span><span class="o">]</span> <span class="n">at</span> <span class="n">hb&#39;</span><span class="o">,</span>
    <span class="n">rw</span> <span class="o">[</span><span class="err">←</span> <span class="n">hb</span><span class="o">,</span> <span class="err">←</span> <span class="n">H2</span><span class="o">,</span> <span class="err">←</span> <span class="n">is_add_group_hom</span><span class="bp">.</span><span class="n">zero</span> <span class="n">fc</span><span class="o">]</span> <span class="n">at</span> <span class="n">hb&#39;</span><span class="o">,</span>
    <span class="n">replace</span> <span class="n">hb&#39;</span> <span class="o">:=</span> <span class="n">congr_arg</span> <span class="n">fc</span><span class="bp">.</span><span class="n">symm</span> <span class="n">hb&#39;</span><span class="o">,</span>
    <span class="n">simp</span> <span class="n">at</span> <span class="n">hb&#39;</span><span class="o">,</span>
    <span class="k">have</span> <span class="n">H3</span> <span class="o">:</span> <span class="n">b</span> <span class="err">∈</span> <span class="n">set</span><span class="bp">.</span><span class="n">range</span> <span class="n">ab</span><span class="o">,</span>
    <span class="o">{</span> <span class="n">rwa</span> <span class="n">Habc</span> <span class="o">},</span>
    <span class="n">cases</span> <span class="n">H3</span> <span class="k">with</span> <span class="n">a</span> <span class="n">ha</span><span class="o">,</span>
    <span class="n">existsi</span> <span class="n">fa</span> <span class="n">a</span><span class="o">,</span>
    <span class="n">rw</span> <span class="err">←</span> <span class="n">H1</span><span class="o">,</span>
    <span class="n">simp</span> <span class="o">[</span><span class="n">ha</span><span class="o">]</span> <span class="o">}</span>
<span class="kn">end</span>
</pre></div>

#### [ Kenny Lau (Apr 27 2018 at 12:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proof%20of%20the%20five%20lemma/near/125768242):
<p>this is much better</p>

#### [ Reid Barton (Apr 27 2018 at 19:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proof%20of%20the%20five%20lemma/near/125785178):
<p>How about proving some lemmas like this one, and combining them into what you want.</p>
<div class="codehilite"><pre><span></span><span class="kn">import</span> <span class="n">data</span><span class="bp">.</span><span class="n">equiv</span>

<span class="kn">open</span> <span class="n">set</span>

<span class="kn">lemma</span> <span class="n">equiv_range</span> <span class="o">{</span><span class="n">α</span> <span class="n">β</span> <span class="o">:</span> <span class="kt">Type</span><span class="bp">*</span><span class="o">}</span> <span class="o">(</span><span class="n">f</span> <span class="o">:</span> <span class="n">α</span> <span class="bp">→</span> <span class="n">β</span><span class="o">)</span> <span class="o">{</span><span class="n">α&#39;</span> <span class="n">β&#39;</span> <span class="o">:</span> <span class="kt">Type</span><span class="bp">*</span><span class="o">}</span> <span class="o">(</span><span class="n">f&#39;</span> <span class="o">:</span> <span class="n">α&#39;</span> <span class="bp">→</span> <span class="n">β&#39;</span><span class="o">)</span>
  <span class="o">(</span><span class="n">eα</span> <span class="o">:</span> <span class="n">α</span> <span class="err">≃</span> <span class="n">α&#39;</span><span class="o">)</span> <span class="o">(</span><span class="n">eβ</span> <span class="o">:</span> <span class="n">β</span> <span class="err">≃</span> <span class="n">β&#39;</span><span class="o">)</span> <span class="o">(</span><span class="n">h</span> <span class="o">:</span> <span class="n">f&#39;</span> <span class="err">∘</span> <span class="n">eα</span> <span class="bp">=</span> <span class="n">eβ</span> <span class="err">∘</span> <span class="n">f</span><span class="o">)</span> <span class="o">:</span>
  <span class="n">range</span> <span class="n">f&#39;</span> <span class="bp">=</span> <span class="n">eβ</span> <span class="err">&#39;&#39;</span> <span class="n">range</span> <span class="n">f</span> <span class="o">:=</span>
<span class="k">calc</span> <span class="n">range</span> <span class="n">f&#39;</span> <span class="bp">=</span> <span class="n">f&#39;</span> <span class="err">&#39;&#39;</span> <span class="n">univ</span>         <span class="o">:</span> <span class="k">by</span> <span class="n">rw</span> <span class="n">image_univ</span>
     <span class="bp">...</span>      <span class="bp">=</span> <span class="n">f&#39;</span> <span class="err">&#39;&#39;</span> <span class="o">(</span><span class="n">range</span> <span class="n">eα</span><span class="o">)</span>   <span class="o">:</span> <span class="k">by</span> <span class="n">rw</span> <span class="n">range_iff_surjective</span><span class="bp">.</span><span class="n">mpr</span> <span class="n">eα</span><span class="bp">.</span><span class="n">bijective</span><span class="bp">.</span><span class="mi">2</span>
     <span class="bp">...</span>      <span class="bp">=</span> <span class="n">f&#39;</span> <span class="err">&#39;&#39;</span> <span class="o">(</span><span class="n">eα</span> <span class="err">&#39;&#39;</span> <span class="n">univ</span><span class="o">)</span> <span class="o">:</span> <span class="k">by</span> <span class="n">rw</span> <span class="n">image_univ</span>
     <span class="bp">...</span>      <span class="bp">=</span> <span class="o">(</span><span class="n">f&#39;</span> <span class="err">∘</span> <span class="n">eα</span><span class="o">)</span> <span class="err">&#39;&#39;</span> <span class="n">univ</span>  <span class="o">:</span> <span class="k">by</span> <span class="n">rw</span> <span class="err">←</span><span class="n">image_comp</span>
     <span class="bp">...</span>      <span class="bp">=</span> <span class="o">(</span><span class="n">eβ</span> <span class="err">∘</span> <span class="n">f</span><span class="o">)</span> <span class="err">&#39;&#39;</span> <span class="n">univ</span>   <span class="o">:</span> <span class="k">by</span> <span class="n">rw</span> <span class="n">h</span>
     <span class="bp">...</span>      <span class="bp">=</span> <span class="n">eβ</span> <span class="err">&#39;&#39;</span> <span class="o">(</span><span class="n">f</span> <span class="err">&#39;&#39;</span> <span class="n">univ</span><span class="o">)</span>  <span class="o">:</span> <span class="k">by</span> <span class="n">rw</span> <span class="n">image_comp</span>
     <span class="bp">...</span>      <span class="bp">=</span> <span class="n">eβ</span> <span class="err">&#39;&#39;</span> <span class="n">range</span> <span class="n">f</span>      <span class="o">:</span> <span class="k">by</span> <span class="n">rw</span> <span class="n">image_univ</span>
</pre></div>

#### [ Reid Barton (Apr 27 2018 at 20:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proof%20of%20the%20five%20lemma/near/125786306):
<p>(Now I see that Patrick said much the same thing about a half hour earlier.)</p>

#### [ Johan Commelin (Apr 27 2018 at 21:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proof%20of%20the%20five%20lemma/near/125788582):
<p>I should have used <code>calc</code> in my proof of the five lemma...</p>

#### [ Kevin Buzzard (Apr 27 2018 at 22:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proof%20of%20the%20five%20lemma/near/125791112):
<p>You live and learn in this game</p>

#### [ Kevin Buzzard (Apr 27 2018 at 22:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proof%20of%20the%20five%20lemma/near/125791117):
<p>Your levels were really helpful for me today. Do you know some abstract type theory?</p>

#### [ Kevin Buzzard (Apr 27 2018 at 22:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proof%20of%20the%20five%20lemma/near/125791127):
<p>You understood what Scott was saying</p>


{% endraw %}
