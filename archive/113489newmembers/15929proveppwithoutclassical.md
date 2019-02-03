---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113489newmembers/15929proveppwithoutclassical.html
---

## Stream: [new members](index.html)
### Topic: [prove ¬(p ↔ ¬p) without classical](15929proveppwithoutclassical.html)

---


{% raw %}
#### [ Andrew Skiba (Aug 31 2018 at 09:07)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/prove%20%C2%AC%28p%20%E2%86%94%20%C2%ACp%29%20without%20classical/near/133107905):
<p>The examples at the end of chapter 3 of tutorial "Theorem proving in Lean" are very easy, except the one in subj. If I try to construct it as is, I have to construct false from two functions, which I can get by <a href="http://iff.mp" target="_blank" title="http://iff.mp">iff.mp</a> and iff.mpr - but I have no objects to apply these functions. I found propext constant, which allowed me to convert iff to an equality of p = ¬p, but I don't see how to prove (p = ¬p) → false. In Idris language such proofs are built by "impossible" keyword, but I cannot find anything similar in Lean. Am I missing something basic?</p>

#### [ Sean Leather (Aug 31 2018 at 09:19)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/prove%20%C2%AC%28p%20%E2%86%94%20%C2%ACp%29%20without%20classical/near/133108380):
<p>Here's what I came up with:</p>
<div class="codehilite"><pre><span></span><span class="kn">example</span> <span class="o">{</span><span class="n">p</span> <span class="o">:</span> <span class="kt">Prop</span><span class="o">}</span> <span class="o">[</span><span class="n">h</span> <span class="o">:</span> <span class="n">decidable</span> <span class="n">p</span><span class="o">]</span> <span class="o">(</span><span class="n">q</span> <span class="o">:</span> <span class="n">p</span> <span class="bp">↔</span> <span class="bp">¬</span><span class="n">p</span><span class="o">)</span> <span class="o">:</span> <span class="n">false</span> <span class="o">:=</span>
<span class="k">match</span> <span class="n">h</span> <span class="k">with</span>
<span class="bp">|</span> <span class="n">is_true</span>  <span class="n">p</span>  <span class="o">:=</span> <span class="n">iff</span><span class="bp">.</span><span class="n">mp</span> <span class="n">q</span> <span class="n">p</span> <span class="n">p</span>
<span class="bp">|</span> <span class="n">is_false</span> <span class="n">np</span> <span class="o">:=</span> <span class="n">np</span> <span class="o">(</span><span class="n">iff</span><span class="bp">.</span><span class="n">mpr</span> <span class="n">q</span> <span class="n">np</span><span class="o">)</span>
<span class="kn">end</span>
</pre></div>

#### [ Sean Leather (Aug 31 2018 at 09:26)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/prove%20%C2%AC%28p%20%E2%86%94%20%C2%ACp%29%20without%20classical/near/133108711):
<p>Perhaps the key to remember here is that <code>¬ p</code> means <code>p → false</code>, so both <code>iff.mp q p : p → false</code> and <code>np : p → false</code>. Then you just have to fill in the <code>p</code>.</p>

#### [ Andrew Skiba (Aug 31 2018 at 09:28)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/prove%20%C2%AC%28p%20%E2%86%94%20%C2%ACp%29%20without%20classical/near/133108794):
<p>Is not the idea of not using classical that I cannot prove by cases? I'm still at the beginning of the tutorial and did not learn what is decidable, but it looks too similar to excluded middle. I suppose it should also allow to prove ¬¬p  → p which should not work in constructive reasoning.</p>

#### [ Patrick Massot (Aug 31 2018 at 09:36)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/prove%20%C2%AC%28p%20%E2%86%94%20%C2%ACp%29%20without%20classical/near/133109087):
<p><a href="https://github.com/leanprover/lean/blob/master/library/init/logic.lean#L343" target="_blank" title="https://github.com/leanprover/lean/blob/master/library/init/logic.lean#L343">https://github.com/leanprover/lean/blob/master/library/init/logic.lean#L343</a></p>

#### [ Kenny Lau (Aug 31 2018 at 09:42)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/prove%20%C2%AC%28p%20%E2%86%94%20%C2%ACp%29%20without%20classical/near/133109264):
<p><span class="user-mention" data-user-id="110045">@Sean Leather</span> if you use decidable you might as well use classical</p>

#### [ Sean Leather (Aug 31 2018 at 09:43)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/prove%20%C2%AC%28p%20%E2%86%94%20%C2%ACp%29%20without%20classical/near/133109327):
<p>True. Attempt # 2:</p>
<div class="codehilite"><pre><span></span><span class="kn">example</span> <span class="o">{</span><span class="n">p</span> <span class="o">:</span> <span class="kt">Prop</span><span class="o">}</span> <span class="o">(</span><span class="n">q</span> <span class="o">:</span> <span class="n">p</span> <span class="bp">↔</span> <span class="bp">¬</span><span class="n">p</span><span class="o">)</span> <span class="o">:</span> <span class="n">false</span> <span class="o">:=</span>
<span class="k">have</span> <span class="n">h&#39;</span> <span class="o">:</span> <span class="bp">¬</span><span class="n">p</span><span class="o">,</span> <span class="k">from</span> <span class="bp">λ</span> <span class="n">h</span><span class="o">,</span> <span class="o">(</span><span class="n">iff</span><span class="bp">.</span><span class="n">mp</span> <span class="n">q</span> <span class="n">h</span><span class="o">)</span> <span class="n">h</span><span class="o">,</span>
<span class="n">h&#39;</span> <span class="o">(</span><span class="n">iff</span><span class="bp">.</span><span class="n">mpr</span> <span class="n">q</span> <span class="n">h&#39;</span><span class="o">)</span>
</pre></div>

#### [ Patrick Massot (Aug 31 2018 at 09:43)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/prove%20%C2%AC%28p%20%E2%86%94%20%C2%ACp%29%20without%20classical/near/133109343):
<p>Why don't you like my solution?</p>

#### [ Johan Commelin (Aug 31 2018 at 09:43)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/prove%20%C2%AC%28p%20%E2%86%94%20%C2%ACp%29%20without%20classical/near/133109344):
<blockquote>
<p>you might as well use classical</p>
</blockquote>
<p>This conclusion doesn't need any hypotheses.</p>

#### [ Kenny Lau (Aug 31 2018 at 09:44)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/prove%20%C2%AC%28p%20%E2%86%94%20%C2%ACp%29%20without%20classical/near/133109401):
<div class="codehilite"><pre><span></span><span class="kn">example</span> <span class="o">{</span><span class="n">p</span> <span class="o">:</span> <span class="kt">Prop</span><span class="o">}</span> <span class="o">(</span><span class="n">q</span> <span class="o">:</span> <span class="n">p</span> <span class="bp">↔</span> <span class="bp">¬</span><span class="n">p</span><span class="o">)</span> <span class="o">:</span> <span class="n">false</span> <span class="o">:=</span>
<span class="n">q</span><span class="bp">.</span><span class="mi">1</span> <span class="o">(</span><span class="n">q</span><span class="bp">.</span><span class="mi">2</span> <span class="err">$</span> <span class="bp">λ</span> <span class="n">H</span><span class="o">,</span> <span class="n">q</span><span class="bp">.</span><span class="mi">1</span> <span class="n">H</span> <span class="n">H</span><span class="o">)</span> <span class="o">(</span><span class="n">q</span><span class="bp">.</span><span class="mi">2</span> <span class="err">$</span> <span class="bp">λ</span> <span class="n">H</span><span class="o">,</span> <span class="n">q</span><span class="bp">.</span><span class="mi">1</span> <span class="n">H</span> <span class="n">H</span><span class="o">)</span>

<span class="kn">example</span> <span class="o">{</span><span class="n">p</span> <span class="o">:</span> <span class="kt">Prop</span><span class="o">}</span> <span class="o">(</span><span class="n">q</span> <span class="o">:</span> <span class="n">p</span> <span class="bp">↔</span> <span class="bp">¬</span><span class="n">p</span><span class="o">)</span> <span class="o">:</span> <span class="n">false</span> <span class="o">:=</span>
<span class="o">(</span><span class="bp">λ</span> <span class="n">H</span><span class="o">,</span> <span class="n">q</span><span class="bp">.</span><span class="mi">1</span> <span class="n">H</span> <span class="n">H</span><span class="o">)</span> <span class="err">$</span> <span class="n">q</span><span class="bp">.</span><span class="mi">2</span> <span class="err">$</span> <span class="bp">λ</span> <span class="n">H</span><span class="o">,</span> <span class="n">q</span><span class="bp">.</span><span class="mi">1</span> <span class="n">H</span> <span class="n">H</span>
</pre></div>

#### [ Sean Leather (Aug 31 2018 at 09:46)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/prove%20%C2%AC%28p%20%E2%86%94%20%C2%ACp%29%20without%20classical/near/133109467):
<p><span class="user-mention" data-user-id="110064">@Kenny Lau</span> I was trying to avoid “shortcuts” like <code>.1</code> and <code>$</code>,  which may not have been covered, yet.</p>

#### [ Andrew Skiba (Aug 31 2018 at 09:48)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/prove%20%C2%AC%28p%20%E2%86%94%20%C2%ACp%29%20without%20classical/near/133109539):
<p>Thanks, guys! Excellent examples, will try to understand where did I miss the point.</p>

#### [ Kenny Lau (Aug 31 2018 at 09:48)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/prove%20%C2%AC%28p%20%E2%86%94%20%C2%ACp%29%20without%20classical/near/133109541):
<div class="codehilite"><pre><span></span><span class="kn">example</span> <span class="o">{</span><span class="n">p</span> <span class="o">:</span> <span class="kt">Prop</span><span class="o">}</span> <span class="o">:</span> <span class="bp">¬</span><span class="o">(</span><span class="n">p</span> <span class="bp">↔</span> <span class="bp">¬</span><span class="n">p</span><span class="o">)</span> <span class="o">:=</span>
<span class="bp">λ</span> <span class="n">q</span><span class="o">,</span> <span class="n">iff</span><span class="bp">.</span><span class="n">rec_on</span> <span class="n">q</span> <span class="o">(</span><span class="bp">λ</span> <span class="n">h1</span> <span class="n">h2</span><span class="o">,</span> <span class="n">h1</span> <span class="o">(</span><span class="n">h2</span> <span class="o">(</span><span class="bp">λ</span> <span class="n">H</span><span class="o">,</span> <span class="n">h1</span> <span class="n">H</span> <span class="n">H</span><span class="o">))</span> <span class="o">(</span><span class="n">h2</span> <span class="o">(</span><span class="bp">λ</span> <span class="n">H</span><span class="o">,</span> <span class="n">h1</span> <span class="n">H</span> <span class="n">H</span><span class="o">)))</span>
</pre></div>

#### [ Kenny Lau (Aug 31 2018 at 09:51)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/prove%20%C2%AC%28p%20%E2%86%94%20%C2%ACp%29%20without%20classical/near/133109629):
<div class="codehilite"><pre><span></span><span class="kn">example</span> <span class="o">{</span><span class="n">p</span> <span class="o">:</span> <span class="kt">Prop</span><span class="o">}</span> <span class="o">:</span> <span class="bp">¬</span><span class="o">(</span><span class="n">p</span> <span class="bp">↔</span> <span class="bp">¬</span><span class="n">p</span><span class="o">)</span> <span class="o">:=</span>
<span class="k">assume</span> <span class="n">q</span> <span class="o">:</span> <span class="n">p</span> <span class="bp">↔</span> <span class="bp">¬</span><span class="n">p</span><span class="o">,</span> <span class="n">iff</span><span class="bp">.</span><span class="n">rec_on</span> <span class="n">q</span>
<span class="o">(</span><span class="k">assume</span> <span class="n">h1</span> <span class="o">:</span> <span class="n">p</span> <span class="bp">→</span> <span class="bp">¬</span><span class="n">p</span><span class="o">,</span>
 <span class="k">assume</span> <span class="n">h2</span> <span class="o">:</span> <span class="bp">¬</span><span class="n">p</span> <span class="bp">→</span> <span class="n">p</span><span class="o">,</span>
 <span class="n">h1</span> <span class="o">(</span><span class="n">h2</span> <span class="o">(</span><span class="bp">λ</span> <span class="n">H</span><span class="o">,</span> <span class="n">h1</span> <span class="n">H</span> <span class="n">H</span><span class="o">))</span> <span class="o">(</span><span class="n">h2</span> <span class="o">(</span><span class="bp">λ</span> <span class="n">H</span><span class="o">,</span> <span class="n">h1</span> <span class="n">H</span> <span class="n">H</span><span class="o">)))</span>
</pre></div>

#### [ Sean Leather (Aug 31 2018 at 09:52)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/prove%20%C2%AC%28p%20%E2%86%94%20%C2%ACp%29%20without%20classical/near/133109671):
<p>Are these cries for <code>hhhhhh</code>elp, Kenny? <span class="emoji emoji-1f609" title="wink">:wink:</span></p>

#### [ Kenny Lau (Aug 31 2018 at 09:52)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/prove%20%C2%AC%28p%20%E2%86%94%20%C2%ACp%29%20without%20classical/near/133109676):
<p>I just like to name my hypotheses <code>h</code></p>

#### [ Sean Leather (Aug 31 2018 at 09:53)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/prove%20%C2%AC%28p%20%E2%86%94%20%C2%ACp%29%20without%20classical/near/133109689):
<p>Too bad there's only one <code>h</code> in the Latin alphabet.</p>

#### [ Andrew Skiba (Aug 31 2018 at 10:01)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/prove%20%C2%AC%28p%20%E2%86%94%20%C2%ACp%29%20without%20classical/near/133109997):
<p><span class="user-mention" data-user-id="110031">@Patrick Massot</span> I did like your solution, because the tutorial only states that there are implementations of these proofs in the standard library, but does not mention where to find them. But the easiest to follow is Sean's one, because I can see what I missed: although it's impossible to construct a p, it is still possible to construct ¬p, and the last line is trivial. I still did not completely understand, how it's done by λ h, (<a href="http://iff.mp" target="_blank" title="http://iff.mp">iff.mp</a> q h) h, but it's a small piece to resolve already.</p>

#### [ Sean Leather (Aug 31 2018 at 10:06)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/prove%20%C2%AC%28p%20%E2%86%94%20%C2%ACp%29%20without%20classical/near/133110240):
<p><span class="user-mention" data-user-id="127891">@Andrew Skiba</span> You know that <code>λ</code> and <code>assume</code> are the same?</p>

#### [ Sean Leather (Aug 31 2018 at 10:09)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/prove%20%C2%AC%28p%20%E2%86%94%20%C2%ACp%29%20without%20classical/near/133110323):
<p>When looking again at Theorem Proving in Lean, I realized that it mostly used <code>assume</code>. I use <code>λ</code> more myself, since it's shorter.</p>

#### [ Andrew Skiba (Aug 31 2018 at 11:52)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/prove%20%C2%AC%28p%20%E2%86%94%20%C2%ACp%29%20without%20classical/near/133114894):
<blockquote>
<p><span class="user-mention" data-user-id="127891">@Andrew Skiba</span> You know that <code>λ</code> and <code>assume</code> are the same?</p>
</blockquote>
<p>Sure, this one is clear. I missed another point: although it's impossible to construct p from ¬¬p without em, it is easy to construct ¬p from ¬¬¬p. This is the key to solving this exercise.</p>

#### [ Patrick Massot (Aug 31 2018 at 11:53)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/prove%20%C2%AC%28p%20%E2%86%94%20%C2%ACp%29%20without%20classical/near/133114912):
<p>constructive math is crazy...</p>

#### [ Bryan Gin-ge Chen (Aug 31 2018 at 15:39)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/prove%20%C2%AC%28p%20%E2%86%94%20%C2%ACp%29%20without%20classical/near/133124674):
<p>This problem seems to be a fairly popular question here <a href="#narrow/stream/113488-general/subject/Logic.20.26.20Proof/near/127708058" title="#narrow/stream/113488-general/subject/Logic.20.26.20Proof/near/127708058">1</a> <a href="#narrow/stream/113489-new-members/subject/(no.20topic)/near/132923537" title="#narrow/stream/113489-new-members/subject/(no.20topic)/near/132923537">2</a>.</p>

#### [ Kevin Buzzard (Aug 31 2018 at 15:53)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/prove%20%C2%AC%28p%20%E2%86%94%20%C2%ACp%29%20without%20classical/near/133125379):
<p>Yeah, for some reason it's tripping up a lot of people working through TPIL. We need a FAQ!</p>


{% endraw %}
