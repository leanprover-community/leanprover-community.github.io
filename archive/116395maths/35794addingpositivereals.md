---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/35794addingpositivereals.html
---

## Stream: [maths](https://leanprover-community.github.io/archive/116395maths/index.html)
### Topic: [adding positive reals](https://leanprover-community.github.io/archive/116395maths/35794addingpositivereals.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Joseph Corneli (Jan 26 2019 at 19:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/adding%20positive%20reals/near/156936354):
<div class="codehilite"><pre><span></span><span class="n">def</span> <span class="n">nzreal</span> <span class="o">:=</span> <span class="o">{</span><span class="n">r</span> <span class="o">:</span> <span class="n">ℝ</span> <span class="bp">//</span> <span class="n">r</span> <span class="bp">≠</span> <span class="mi">0</span><span class="o">}</span>
<span class="kn">notation</span> <span class="bp">`</span><span class="n">ℝ</span><span class="bp">*`</span> <span class="o">:=</span> <span class="n">nzreal</span>
<span class="kn">constants</span> <span class="n">nzc</span> <span class="n">nzd</span> <span class="o">:</span> <span class="n">nzreal</span>
<span class="bp">#</span><span class="kn">check</span> <span class="n">nzc</span><span class="bp">+</span><span class="n">nzd</span>
</pre></div>


<blockquote>
<p>failed to synthesize type class instance for<br>
⊢ has_add ℝ*</p>
</blockquote>
<p>Is this a place to use the canonical structures that Assia and Cyril told us about in Amsterdam?  Seems to me like the kind of thing that would be a match for that sort of thinking. </p>
<p>Oh, that's <code>nzreal</code>s but it's more or less the same question for <code>posreal</code>s.</p>

#### [ Johan Commelin (Jan 26 2019 at 20:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/adding%20positive%20reals/near/156937069):
<p>Well, you just defined a new type. So you will have to explain what addition should mean. Also, what should <code>x + -x</code> be?</p>

#### [ Joseph Corneli (Jan 26 2019 at 20:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/adding%20positive%20reals/near/156937125):
<p>If I have learned correctly it should be 37</p>

#### [ Joseph Corneli (Jan 26 2019 at 20:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/adding%20positive%20reals/near/156937136):
<p>actually a moderately useful idea in this setting</p>

#### [ Joseph Corneli (Jan 26 2019 at 20:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/adding%20positive%20reals/near/156937138):
<p>though I suspect there are some downsides...</p>

#### [ Joseph Corneli (Jan 26 2019 at 20:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/adding%20positive%20reals/near/156937336):
<div class="codehilite"><pre><span></span><span class="kn">namespace</span> <span class="n">nzreal</span>

<span class="n">def</span> <span class="n">nzreal</span> <span class="o">:=</span> <span class="o">{</span><span class="n">r</span> <span class="o">:</span> <span class="n">ℝ</span> <span class="bp">//</span> <span class="n">r</span> <span class="bp">≠</span> <span class="mi">0</span><span class="o">}</span>
<span class="kn">notation</span> <span class="bp">`</span><span class="n">ℝ</span><span class="bp">*`</span> <span class="o">:=</span> <span class="n">nzreal</span>
<span class="kn">constants</span> <span class="n">nzc</span> <span class="n">nzd</span> <span class="o">:</span> <span class="n">nzreal</span>
<span class="bp">#</span><span class="kn">check</span> <span class="n">nzc</span><span class="bp">+</span><span class="n">nzd</span>

<span class="n">def</span> <span class="n">add</span> <span class="o">:</span> <span class="n">nzreal</span> <span class="bp">→</span> <span class="n">nzreal</span> <span class="bp">→</span> <span class="n">ℝ</span>
<span class="bp">|</span> <span class="n">x</span> <span class="n">y</span> <span class="o">:=</span> <span class="n">subtype</span><span class="bp">.</span><span class="n">val</span> <span class="n">x</span> <span class="bp">+</span> <span class="n">subtype</span><span class="bp">.</span><span class="n">val</span> <span class="n">y</span>

<span class="c1">-- except this doesn&#39;t work</span>
<span class="kn">instance</span> <span class="o">:</span> <span class="n">has_add</span> <span class="n">nzreal</span> <span class="o">:=</span> <span class="bp">⟨</span><span class="n">nzreal</span><span class="bp">.</span><span class="n">add</span><span class="bp">⟩</span>
<span class="kn">end</span> <span class="n">nzreal</span>
</pre></div>

#### [ Neil Strickland (Jan 26 2019 at 20:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/adding%20positive%20reals/near/156937385):
<p>The following works:</p>
<div class="codehilite"><pre><span></span><span class="kn">import</span> <span class="n">data</span><span class="bp">.</span><span class="n">rat</span> <span class="n">data</span><span class="bp">.</span><span class="n">real</span><span class="bp">.</span><span class="n">basic</span>

<span class="n">def</span> <span class="n">pos_rat</span> <span class="o">:=</span> <span class="o">{</span> <span class="n">q</span> <span class="o">:</span> <span class="n">ℚ</span> <span class="bp">//</span> <span class="n">q</span> <span class="bp">&gt;</span> <span class="mi">0</span><span class="o">}</span>

<span class="kn">instance</span> <span class="n">pos_rat</span><span class="bp">.</span><span class="n">add</span> <span class="o">:</span> <span class="n">has_add</span> <span class="n">pos_rat</span> <span class="o">:=</span>
 <span class="bp">⟨λ</span> <span class="n">q</span> <span class="n">r</span><span class="o">,</span><span class="bp">⟨</span><span class="n">q</span><span class="bp">.</span><span class="n">val</span> <span class="bp">+</span> <span class="n">r</span><span class="bp">.</span><span class="n">val</span><span class="o">,</span><span class="n">add_lt_add</span> <span class="n">q</span><span class="bp">.</span><span class="n">property</span> <span class="n">r</span><span class="bp">.</span><span class="n">property</span><span class="bp">⟩⟩</span>

<span class="n">def</span> <span class="n">pos_real</span> <span class="o">:=</span> <span class="o">{</span> <span class="n">q</span> <span class="o">:</span> <span class="n">ℝ</span> <span class="bp">//</span> <span class="n">q</span> <span class="bp">&gt;</span> <span class="mi">0</span><span class="o">}</span>

<span class="kn">instance</span> <span class="n">pos_real</span><span class="bp">.</span><span class="n">add</span> <span class="o">:</span> <span class="n">has_add</span> <span class="n">pos_real</span> <span class="o">:=</span>
 <span class="bp">⟨λ</span> <span class="n">q</span> <span class="n">r</span><span class="o">,</span><span class="bp">⟨</span><span class="n">q</span><span class="bp">.</span><span class="n">val</span> <span class="bp">+</span> <span class="n">r</span><span class="bp">.</span><span class="n">val</span><span class="o">,</span>
  <span class="bp">@</span><span class="n">eq</span><span class="bp">.</span><span class="n">subst</span> <span class="n">ℝ</span> <span class="o">(</span><span class="bp">λ</span> <span class="n">z</span><span class="o">,</span> <span class="n">z</span> <span class="bp">&lt;</span> <span class="n">q</span><span class="bp">.</span><span class="n">val</span> <span class="bp">+</span> <span class="n">r</span><span class="bp">.</span><span class="n">val</span><span class="o">)</span> <span class="o">(</span><span class="mi">0</span> <span class="bp">+</span> <span class="mi">0</span><span class="o">)</span> <span class="mi">0</span> <span class="o">(</span><span class="n">zero_add</span> <span class="mi">0</span><span class="o">)</span> <span class="o">(</span><span class="n">add_lt_add</span> <span class="n">q</span><span class="bp">.</span><span class="n">property</span> <span class="n">r</span><span class="bp">.</span><span class="n">property</span><span class="o">)</span><span class="bp">⟩⟩</span>
</pre></div>


<p>I am sure that the version for <code>ℝ</code> is suboptimal;  I hope that someone more expert will clean it up.</p>

#### [ Kevin Buzzard (Jan 26 2019 at 20:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/adding%20positive%20reals/near/156937452):
<blockquote>
<div class="codehilite"><pre><span></span><span class="c1">-- except this doesn&#39;t work</span>
<span class="kn">instance</span> <span class="o">:</span> <span class="n">has_add</span> <span class="n">nzreal</span> <span class="o">:=</span> <span class="bp">⟨</span><span class="n">nzreal</span><span class="bp">.</span><span class="n">add</span><span class="bp">⟩</span>
</pre></div>


</blockquote>
<p>This doesn't work because to make an instance of <code>has_add X</code> you have to supply a map <code>X -&gt; X -&gt; X</code>, and your map <code>nzreal.add</code> has type <code>nzreal -&gt; nzreal -&gt; real</code>.</p>

#### [ Joseph Corneli (Jan 26 2019 at 20:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/adding%20positive%20reals/near/156937466):
<p>yeah, so this one isn't going to work without partial functions</p>

#### [ Joseph Corneli (Jan 26 2019 at 20:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/adding%20positive%20reals/near/156937542):
<p>positives should be OK per <span class="user-mention" data-user-id="130308">@Neil Strickland</span> (I will have to take some time to understand that code)</p>

#### [ Kevin Buzzard (Jan 26 2019 at 20:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/adding%20positive%20reals/near/156937546):
<p><span class="user-mention" data-user-id="130308">@Neil Strickland</span> you need <code>a &gt; 0 -&gt; b &gt; 0 -&gt; a + b &gt; 0</code>. My instinct now (which was not at all my instinct a year ago) is that this result should be in any reasonable API for totally ordered abelian groups.</p>

#### [ Kevin Buzzard (Jan 26 2019 at 20:16)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/adding%20positive%20reals/near/156937585):
<p>So the issue is finding the result. And until we have better search the best way to find the result is to guess the name. I guessed <code>add_pos</code> and <code>pos_add</code> and I hit tab a few times, and eventually I found it.</p>

#### [ Kevin Buzzard (Jan 26 2019 at 20:16)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/adding%20positive%20reals/near/156937607):
<div class="codehilite"><pre><span></span><span class="kn">instance</span> <span class="n">pos_real</span><span class="bp">.</span><span class="n">add</span> <span class="o">:</span> <span class="n">has_add</span> <span class="n">pos_real</span> <span class="o">:=</span>
 <span class="bp">⟨λ</span> <span class="n">q</span> <span class="n">r</span><span class="o">,</span><span class="bp">⟨</span><span class="n">q</span><span class="bp">.</span><span class="n">val</span> <span class="bp">+</span> <span class="n">r</span><span class="bp">.</span><span class="n">val</span><span class="o">,</span><span class="n">add_pos</span> <span class="n">q</span><span class="bp">.</span><span class="n">property</span> <span class="n">r</span><span class="bp">.</span><span class="n">property</span><span class="bp">⟩⟩</span>
</pre></div>


<p>The reason you get away with this for the rationals, I suspect, is that <code>0 + 0</code> is definitionally equal to <code>0</code>, but perhaps not for the reals.</p>

#### [ Kevin Buzzard (Jan 26 2019 at 20:17)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/adding%20positive%20reals/near/156937623):
<div class="codehilite"><pre><span></span><span class="kn">example</span> <span class="o">:</span> <span class="o">(</span><span class="mi">0</span> <span class="o">:</span> <span class="n">ℚ</span><span class="o">)</span> <span class="bp">+</span> <span class="mi">0</span> <span class="bp">=</span> <span class="mi">0</span> <span class="o">:=</span> <span class="n">rfl</span> <span class="c1">-- works</span>
<span class="kn">example</span> <span class="o">:</span> <span class="o">(</span><span class="mi">0</span> <span class="o">:</span> <span class="n">ℝ</span><span class="o">)</span> <span class="bp">+</span> <span class="mi">0</span> <span class="bp">=</span> <span class="mi">0</span> <span class="o">:=</span> <span class="n">rfl</span> <span class="c1">-- fails</span>
</pre></div>

#### [ Kevin Buzzard (Jan 26 2019 at 20:17)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/adding%20positive%20reals/near/156937625):
<p>The joys of decidable equality.</p>

#### [ Kevin Buzzard (Jan 26 2019 at 20:20)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/adding%20positive%20reals/near/156937754):
<p>So when I was solving my first year undergraduate example sheets just over a year ago, I would run into things like this and think "oh I need to prove a,b&gt;0 implies a+b&gt;0, I know about <code>add_lt_add</code>, and I can definitely do it from there, so let's go" and I would write code like yours. Since then I have understood Mario's philosophy for mathlib, which perhaps came from his extensive use of metamath beforehand, which is that libraries should be <em>really thorough</em>. Anything which looks like a standard thing which a mathematician would assume without comment -- such a thing should be in the library already. Once you realise this, you stop trying to prove stuff for yourself and start looking for it instead.</p>

#### [ Joseph Corneli (Jan 26 2019 at 20:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/adding%20positive%20reals/near/156937898):
<p>Thanks for these pointers.  This seems to be a very sensible philosophy.</p>

#### [ Neil Strickland (Jan 26 2019 at 20:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/adding%20positive%20reals/near/156938744):
<p>That makes sense, thanks.  But I'm also interested in whether there is a better way to deal with the <code>eq.subst</code> thing.  The following seems quite mysterious to me:</p>
<div class="codehilite"><pre><span></span><span class="n">def</span> <span class="n">pos_real</span> <span class="o">:=</span> <span class="o">{</span> <span class="n">q</span> <span class="o">:</span> <span class="n">ℝ</span> <span class="bp">//</span> <span class="mi">0</span> <span class="bp">&lt;</span> <span class="n">q</span><span class="o">}</span>

<span class="kn">instance</span> <span class="n">pos_real</span><span class="bp">.</span><span class="n">add</span> <span class="o">:</span> <span class="n">has_add</span> <span class="n">pos_real</span> <span class="o">:=</span>
 <span class="bp">⟨λ</span> <span class="n">q</span> <span class="n">r</span><span class="o">,</span><span class="bp">⟨</span><span class="n">q</span><span class="bp">.</span><span class="n">val</span> <span class="bp">+</span> <span class="n">r</span><span class="bp">.</span><span class="n">val</span><span class="o">,</span>
  <span class="k">begin</span>
   <span class="k">let</span> <span class="n">h0</span> <span class="o">:=</span> <span class="n">zero_add</span> <span class="o">(</span><span class="mi">0</span> <span class="o">:</span> <span class="n">ℝ</span><span class="o">),</span>
   <span class="k">let</span> <span class="n">h1</span> <span class="o">:=</span> <span class="o">(</span><span class="n">add_lt_add</span> <span class="n">q</span><span class="bp">.</span><span class="n">property</span> <span class="n">r</span><span class="bp">.</span><span class="n">property</span><span class="o">),</span>
   <span class="k">let</span> <span class="n">h2</span> <span class="o">:</span> <span class="mi">0</span> <span class="bp">&lt;</span> <span class="n">q</span><span class="bp">.</span><span class="n">val</span> <span class="bp">+</span> <span class="n">r</span><span class="bp">.</span><span class="n">val</span> <span class="o">:=</span> <span class="n">eq</span><span class="bp">.</span><span class="n">subst</span> <span class="n">h0</span> <span class="n">h1</span><span class="o">,</span>
   <span class="k">let</span> <span class="n">h3</span> <span class="o">:</span> <span class="mi">0</span> <span class="bp">&lt;</span> <span class="n">q</span><span class="bp">.</span><span class="n">val</span> <span class="bp">+</span> <span class="n">r</span><span class="bp">.</span><span class="n">val</span> <span class="o">:=</span> <span class="n">eq</span><span class="bp">.</span><span class="n">subst</span> <span class="n">h0</span> <span class="o">(</span><span class="n">add_lt_add</span> <span class="n">q</span><span class="bp">.</span><span class="n">property</span> <span class="n">r</span><span class="bp">.</span><span class="n">property</span><span class="o">),</span>
   <span class="n">exact</span> <span class="n">h3</span><span class="o">,</span>
  <span class="kn">end</span>
  <span class="bp">⟩⟩</span>
</pre></div>


<p>Note that I changed <code>q &gt; 0</code> to <code>0 &lt; q</code>, which eliminates some issues.  But still Lean accepts <code>h2</code> and rejects <code>h3</code>, even though <code>h3</code> is just the result of inlining the definition of <code>h1</code> in <code>h2</code>.  The error message says:</p>
<div class="codehilite"><pre><span></span><span class="n">term</span>
  <span class="n">q</span><span class="bp">.</span><span class="n">property</span>
<span class="n">has</span> <span class="n">type</span>
  <span class="mi">0</span> <span class="bp">&lt;</span> <span class="bp">@</span><span class="n">subtype</span><span class="bp">.</span><span class="n">val</span> <span class="n">ℝ</span> <span class="o">(</span><span class="bp">λ</span> <span class="o">(</span><span class="n">q</span> <span class="o">:</span> <span class="n">ℝ</span><span class="o">),</span> <span class="mi">0</span> <span class="bp">&lt;</span> <span class="n">q</span><span class="o">)</span> <span class="n">q</span>
<span class="n">but</span> <span class="n">is</span> <span class="n">expected</span> <span class="n">to</span> <span class="k">have</span> <span class="n">type</span>
  <span class="mi">0</span> <span class="bp">&lt;</span> <span class="bp">@</span><span class="n">subtype</span><span class="bp">.</span><span class="n">val</span> <span class="n">ℝ</span> <span class="o">(</span><span class="bp">λ</span> <span class="o">(</span><span class="n">q</span> <span class="o">:</span> <span class="n">ℝ</span><span class="o">),</span> <span class="mi">0</span> <span class="bp">+</span> <span class="mi">0</span> <span class="bp">&lt;</span> <span class="n">q</span><span class="o">)</span> <span class="n">q</span>
</pre></div>


<p>I guess I could probably work out why that arises if I really had to.  But I would be more interested to hear about any general strategies to avoid this kind of thing.</p>

#### [ Neil Strickland (Jan 26 2019 at 21:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/adding%20positive%20reals/near/156939239):
<p>It's also interesting that Lean has no problem with this:</p>
<div class="codehilite"><pre><span></span><span class="kn">lemma</span> <span class="n">real_add_pos</span> <span class="o">{</span><span class="n">q</span> <span class="n">r</span> <span class="o">:</span> <span class="n">ℝ</span><span class="o">}</span> <span class="o">(</span><span class="n">hq</span> <span class="o">:</span> <span class="n">q</span> <span class="bp">&gt;</span> <span class="mi">0</span><span class="o">)</span> <span class="o">(</span><span class="n">hr</span> <span class="o">:</span> <span class="n">r</span> <span class="bp">&gt;</span> <span class="mi">0</span><span class="o">)</span> <span class="o">:</span> <span class="n">q</span> <span class="bp">+</span> <span class="n">r</span> <span class="bp">&gt;</span> <span class="mi">0</span> <span class="o">:=</span>
 <span class="n">eq</span><span class="bp">.</span><span class="n">subst</span> <span class="o">(</span><span class="n">add_zero</span> <span class="o">(</span><span class="mi">0</span> <span class="o">:</span> <span class="n">ℝ</span><span class="o">))</span> <span class="o">(</span><span class="n">add_lt_add</span> <span class="n">hq</span> <span class="n">hr</span><span class="o">)</span>
</pre></div>


<p>So I guess that the problem with my <code>pos_real.add</code> is just with the implicit arguments to <code>subtype.val</code>, somehow.</p>

#### [ Mario Carneiro (Jan 26 2019 at 21:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/adding%20positive%20reals/near/156939423):
<p>You should basically always use <code>rw</code> to write <code>eq.subst</code> terms like this</p>

#### [ Mario Carneiro (Jan 26 2019 at 21:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/adding%20positive%20reals/near/156939439):
<p>the motive making is too messy to do by hand unless absolutely necessary</p>

#### [ Kevin Buzzard (Jan 26 2019 at 21:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/adding%20positive%20reals/near/156939504):
<p>The rule of thumb is: "eq.subst never works".</p>

#### [ Kevin Buzzard (Jan 26 2019 at 21:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/adding%20positive%20reals/near/156939553):
<p>There are countless threads with me moaning about the stupid triangle, which is <code>▸</code>, or <code>\t</code>, the notation for <code>eq.subst</code>. I can never get it to work.</p>

#### [ Kevin Buzzard (Jan 26 2019 at 21:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/adding%20positive%20reals/near/156939567):
<p>That's why they wrote <code>rw</code>, which works great.</p>

#### [ Kenny Lau (Jan 26 2019 at 21:19)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/adding%20positive%20reals/near/156939788):
<div class="codehilite"><pre><span></span><span class="n">universes</span> <span class="n">u</span>

<span class="n">def</span> <span class="n">pos_of</span> <span class="o">(</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">)</span> <span class="o">[</span><span class="n">has_lt</span> <span class="n">α</span><span class="o">]</span> <span class="o">[</span><span class="n">has_zero</span> <span class="n">α</span><span class="o">]</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span> <span class="o">:=</span>
<span class="o">{</span> <span class="n">x</span> <span class="o">:</span> <span class="n">α</span> <span class="bp">//</span> <span class="mi">0</span> <span class="bp">&lt;</span> <span class="n">x</span> <span class="o">}</span>

<span class="kn">namespace</span> <span class="n">pos_of</span>

<span class="kn">variables</span> <span class="o">(</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">)</span>

<span class="kn">instance</span> <span class="o">[</span><span class="n">ordered_cancel_comm_monoid</span> <span class="n">α</span><span class="o">]</span> <span class="o">:</span> <span class="n">add_semigroup</span> <span class="o">(</span><span class="n">pos_of</span> <span class="n">α</span><span class="o">)</span> <span class="o">:=</span>
<span class="o">{</span> <span class="n">add</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">x</span> <span class="n">y</span><span class="o">,</span> <span class="bp">⟨</span><span class="n">x</span><span class="bp">.</span><span class="mi">1</span> <span class="bp">+</span> <span class="n">y</span><span class="bp">.</span><span class="mi">1</span><span class="o">,</span> <span class="n">add_pos</span> <span class="n">x</span><span class="bp">.</span><span class="mi">2</span> <span class="n">y</span><span class="bp">.</span><span class="mi">2</span><span class="bp">⟩</span><span class="o">,</span>
  <span class="n">add_assoc</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">x</span> <span class="n">y</span> <span class="n">z</span><span class="o">,</span> <span class="n">subtype</span><span class="bp">.</span><span class="n">eq</span> <span class="err">$</span> <span class="n">add_assoc</span> <span class="bp">_</span> <span class="bp">_</span> <span class="bp">_</span> <span class="o">}</span>

<span class="kn">instance</span> <span class="o">[</span><span class="n">ordered_semiring</span> <span class="n">α</span><span class="o">]</span> <span class="o">:</span> <span class="n">semigroup</span> <span class="o">(</span><span class="n">pos_of</span> <span class="n">α</span><span class="o">)</span> <span class="o">:=</span>
<span class="o">{</span> <span class="n">mul</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">x</span> <span class="n">y</span><span class="o">,</span> <span class="bp">⟨</span><span class="n">x</span><span class="bp">.</span><span class="mi">1</span> <span class="bp">*</span> <span class="n">y</span><span class="bp">.</span><span class="mi">1</span><span class="o">,</span> <span class="n">mul_pos</span> <span class="n">x</span><span class="bp">.</span><span class="mi">2</span> <span class="n">y</span><span class="bp">.</span><span class="mi">2</span><span class="bp">⟩</span><span class="o">,</span>
  <span class="n">mul_assoc</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">x</span> <span class="n">y</span> <span class="n">z</span><span class="o">,</span> <span class="n">subtype</span><span class="bp">.</span><span class="n">eq</span> <span class="err">$</span> <span class="n">mul_assoc</span> <span class="bp">_</span> <span class="bp">_</span> <span class="bp">_</span> <span class="o">}</span>

<span class="kn">instance</span> <span class="o">[</span><span class="n">linear_ordered_semiring</span> <span class="n">α</span><span class="o">]</span> <span class="o">:</span> <span class="n">monoid</span> <span class="o">(</span><span class="n">pos_of</span> <span class="n">α</span><span class="o">)</span> <span class="o">:=</span>
<span class="o">{</span> <span class="n">one</span> <span class="o">:=</span> <span class="bp">⟨</span><span class="mi">1</span><span class="o">,</span> <span class="n">zero_lt_one</span><span class="bp">⟩</span><span class="o">,</span>
  <span class="n">one_mul</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">x</span><span class="o">,</span> <span class="n">subtype</span><span class="bp">.</span><span class="n">eq</span> <span class="err">$</span> <span class="n">one_mul</span> <span class="bp">_</span><span class="o">,</span>
  <span class="n">mul_one</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">x</span><span class="o">,</span> <span class="n">subtype</span><span class="bp">.</span><span class="n">eq</span> <span class="err">$</span> <span class="n">mul_one</span> <span class="bp">_</span><span class="o">,</span>
  <span class="bp">..</span> <span class="n">pos_of</span><span class="bp">.</span><span class="n">semigroup</span> <span class="n">α</span> <span class="o">}</span>

<span class="kn">end</span> <span class="n">pos_of</span>
</pre></div>

#### [ Kevin Buzzard (Jan 26 2019 at 21:19)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/adding%20positive%20reals/near/156939792):
<p>Kenny can you see why Neil gets that weird error?</p>

#### [ Kenny Lau (Jan 26 2019 at 21:20)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/adding%20positive%20reals/near/156939840):
<p>Mario said it already</p>

#### [ Kenny Lau (Jan 26 2019 at 21:20)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/adding%20positive%20reals/near/156939841):
<p>"Mario Carneiro: the motive making is too messy to do by hand unless absolutely necessary"</p>

#### [ Kevin Buzzard (Jan 26 2019 at 21:20)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/adding%20positive%20reals/near/156939842):
<p>What's a motive?</p>

#### [ Kevin Buzzard (Jan 26 2019 at 21:20)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/adding%20positive%20reals/near/156939844):
<p>I literally can't see the difference between his h2 and h3 strategies</p>

#### [ Kenny Lau (Jan 26 2019 at 21:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/adding%20positive%20reals/near/156939853):
<p>Lean needs to guess what you are substituting with</p>

#### [ Kevin Buzzard (Jan 26 2019 at 21:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/adding%20positive%20reals/near/156939858):
<p>sure, but they are literally the same</p>

#### [ Kenny Lau (Jan 26 2019 at 21:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/adding%20positive%20reals/near/156939859):
<p>anyway see my mathlib-grade <span aria-label="tm" class="emoji emoji-2122" role="img" title="tm">:tm:</span> revamp</p>

#### [ Kevin Buzzard (Jan 26 2019 at 21:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/adding%20positive%20reals/near/156939905):
<p>yes but you cheated, you used <code>add_pos</code></p>

#### [ Kenny Lau (Jan 26 2019 at 21:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/adding%20positive%20reals/near/156939998):
<div class="codehilite"><pre><span></span><span class="n">universes</span> <span class="n">u</span>

<span class="n">def</span> <span class="n">pos_of</span> <span class="o">(</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">)</span> <span class="o">[</span><span class="n">has_lt</span> <span class="n">α</span><span class="o">]</span> <span class="o">[</span><span class="n">has_zero</span> <span class="n">α</span><span class="o">]</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span> <span class="o">:=</span>
<span class="o">{</span> <span class="n">x</span> <span class="o">:</span> <span class="n">α</span> <span class="bp">//</span> <span class="mi">0</span> <span class="bp">&lt;</span> <span class="n">x</span> <span class="o">}</span>

<span class="kn">namespace</span> <span class="n">pos_of</span>

<span class="kn">variables</span> <span class="o">(</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">)</span>

<span class="kn">instance</span> <span class="o">[</span><span class="n">ordered_cancel_comm_monoid</span> <span class="n">α</span><span class="o">]</span> <span class="o">:</span> <span class="n">add_semigroup</span> <span class="o">(</span><span class="n">pos_of</span> <span class="n">α</span><span class="o">)</span> <span class="o">:=</span>
<span class="o">{</span> <span class="n">add</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">x</span> <span class="n">y</span><span class="o">,</span> <span class="bp">⟨</span><span class="n">x</span><span class="bp">.</span><span class="mi">1</span> <span class="bp">+</span> <span class="n">y</span><span class="bp">.</span><span class="mi">1</span><span class="o">,</span> <span class="n">add_pos</span> <span class="n">x</span><span class="bp">.</span><span class="mi">2</span> <span class="n">y</span><span class="bp">.</span><span class="mi">2</span><span class="bp">⟩</span><span class="o">,</span>
  <span class="n">add_assoc</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">x</span> <span class="n">y</span> <span class="n">z</span><span class="o">,</span> <span class="n">subtype</span><span class="bp">.</span><span class="n">eq</span> <span class="err">$</span> <span class="n">add_assoc</span> <span class="bp">_</span> <span class="bp">_</span> <span class="bp">_</span> <span class="o">}</span>

<span class="kn">instance</span> <span class="o">[</span><span class="n">ordered_semiring</span> <span class="n">α</span><span class="o">]</span> <span class="o">:</span> <span class="n">semigroup</span> <span class="o">(</span><span class="n">pos_of</span> <span class="n">α</span><span class="o">)</span> <span class="o">:=</span>
<span class="o">{</span> <span class="n">mul</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">x</span> <span class="n">y</span><span class="o">,</span> <span class="bp">⟨</span><span class="n">x</span><span class="bp">.</span><span class="mi">1</span> <span class="bp">*</span> <span class="n">y</span><span class="bp">.</span><span class="mi">1</span><span class="o">,</span> <span class="n">mul_pos</span> <span class="n">x</span><span class="bp">.</span><span class="mi">2</span> <span class="n">y</span><span class="bp">.</span><span class="mi">2</span><span class="bp">⟩</span><span class="o">,</span>
  <span class="n">mul_assoc</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">x</span> <span class="n">y</span> <span class="n">z</span><span class="o">,</span> <span class="n">subtype</span><span class="bp">.</span><span class="n">eq</span> <span class="err">$</span> <span class="n">mul_assoc</span> <span class="bp">_</span> <span class="bp">_</span> <span class="bp">_</span> <span class="o">}</span>

<span class="kn">instance</span> <span class="o">[</span><span class="n">linear_ordered_semiring</span> <span class="n">α</span><span class="o">]</span> <span class="o">:</span> <span class="n">monoid</span> <span class="o">(</span><span class="n">pos_of</span> <span class="n">α</span><span class="o">)</span> <span class="o">:=</span>
<span class="o">{</span> <span class="n">one</span> <span class="o">:=</span> <span class="bp">⟨</span><span class="mi">1</span><span class="o">,</span> <span class="n">zero_lt_one</span><span class="bp">⟩</span><span class="o">,</span>
  <span class="n">one_mul</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">x</span><span class="o">,</span> <span class="n">subtype</span><span class="bp">.</span><span class="n">eq</span> <span class="err">$</span> <span class="n">one_mul</span> <span class="bp">_</span><span class="o">,</span>
  <span class="n">mul_one</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">x</span><span class="o">,</span> <span class="n">subtype</span><span class="bp">.</span><span class="n">eq</span> <span class="err">$</span> <span class="n">mul_one</span> <span class="bp">_</span><span class="o">,</span>
  <span class="bp">..</span> <span class="n">pos_of</span><span class="bp">.</span><span class="n">semigroup</span> <span class="n">α</span> <span class="o">}</span>

<span class="kn">instance</span> <span class="o">[</span><span class="n">linear_ordered_field</span> <span class="n">α</span><span class="o">]</span> <span class="o">:</span> <span class="n">group</span> <span class="o">(</span><span class="n">pos_of</span> <span class="n">α</span><span class="o">)</span> <span class="o">:=</span>
<span class="o">{</span> <span class="n">inv</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">x</span><span class="o">,</span> <span class="bp">⟨</span><span class="n">x</span><span class="bp">.</span><span class="mi">1</span><span class="bp">⁻¹</span><span class="o">,</span> <span class="o">(</span><span class="n">inv_eq_one_div</span> <span class="n">x</span><span class="bp">.</span><span class="mi">1</span><span class="o">)</span><span class="bp">.</span><span class="n">symm</span> <span class="bp">▸</span> <span class="n">one_div_pos_of_pos</span> <span class="n">x</span><span class="bp">.</span><span class="mi">2</span><span class="bp">⟩</span><span class="o">,</span>
  <span class="n">mul_left_inv</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">x</span><span class="o">,</span> <span class="n">subtype</span><span class="bp">.</span><span class="n">eq</span> <span class="err">$</span> <span class="n">inv_mul_cancel</span> <span class="err">$</span> <span class="n">ne_of_gt</span> <span class="n">x</span><span class="bp">.</span><span class="mi">2</span><span class="o">,</span>
  <span class="bp">..</span> <span class="n">pos_of</span><span class="bp">.</span><span class="n">monoid</span> <span class="n">α</span> <span class="o">}</span>

<span class="kn">end</span> <span class="n">pos_of</span>
</pre></div>

#### [ Kenny Lau (Jan 26 2019 at 21:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/adding%20positive%20reals/near/156939999):
<p>why can't I use add_pos?</p>

#### [ Kevin Buzzard (Jan 26 2019 at 21:26)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/adding%20positive%20reals/near/156940039):
<p>because this whole thread started because Neil didn't know about <code>add_pos</code> and we're still stuck trying to work around it.</p>

#### [ Kenny Lau (Jan 26 2019 at 21:26)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/adding%20positive%20reals/near/156940043):
<p>just copy the proof of add_pos then</p>

#### [ Kevin Buzzard (Jan 26 2019 at 21:26)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/adding%20positive%20reals/near/156940047):
<div class="codehilite"><pre><span></span><span class="kn">import</span> <span class="n">data</span><span class="bp">.</span><span class="n">real</span><span class="bp">.</span><span class="n">basic</span>

<span class="n">def</span> <span class="n">pos_real</span> <span class="o">:=</span> <span class="o">{</span> <span class="n">q</span> <span class="o">:</span> <span class="n">ℝ</span> <span class="bp">//</span> <span class="mi">0</span> <span class="bp">&lt;</span> <span class="n">q</span><span class="o">}</span>

<span class="kn">instance</span> <span class="n">pos_real</span><span class="bp">.</span><span class="n">add</span> <span class="o">:</span> <span class="n">has_add</span> <span class="n">pos_real</span> <span class="o">:=</span>
 <span class="bp">⟨λ</span> <span class="n">q</span> <span class="n">r</span><span class="o">,</span><span class="bp">⟨</span><span class="n">q</span><span class="bp">.</span><span class="n">val</span> <span class="bp">+</span> <span class="n">r</span><span class="bp">.</span><span class="n">val</span><span class="o">,</span>
  <span class="k">begin</span>
   <span class="k">let</span> <span class="n">h0</span> <span class="o">:=</span> <span class="n">zero_add</span> <span class="o">(</span><span class="mi">0</span> <span class="o">:</span> <span class="n">ℝ</span><span class="o">),</span>
   <span class="n">exact</span> <span class="o">(</span><span class="n">eq</span><span class="bp">.</span><span class="n">subst</span> <span class="n">h0</span> <span class="o">(</span><span class="n">add_lt_add</span> <span class="n">q</span><span class="bp">.</span><span class="n">property</span> <span class="n">r</span><span class="bp">.</span><span class="n">property</span><span class="o">)</span> <span class="o">:</span> <span class="mi">0</span> <span class="bp">&lt;</span> <span class="n">q</span><span class="bp">.</span><span class="n">val</span> <span class="bp">+</span> <span class="n">r</span><span class="bp">.</span><span class="n">val</span><span class="o">),</span> <span class="c1">-- stupid triangle doesn&#39;t work</span>
  <span class="kn">end</span>
  <span class="bp">⟩⟩</span>
</pre></div>

#### [ Kenny Lau (Jan 26 2019 at 21:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/adding%20positive%20reals/near/156940116):
<div class="codehilite"><pre><span></span><span class="n">universes</span> <span class="n">u</span>
<span class="kn">example</span> <span class="o">(</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">)</span> <span class="o">[</span><span class="n">ordered_cancel_comm_monoid</span> <span class="n">α</span><span class="o">]</span> <span class="o">{</span><span class="n">x</span> <span class="n">y</span> <span class="o">:</span> <span class="n">α</span><span class="o">}</span> <span class="o">(</span><span class="n">hx</span> <span class="o">:</span> <span class="mi">0</span> <span class="bp">&lt;</span> <span class="n">x</span><span class="o">)</span> <span class="o">(</span><span class="n">hy</span> <span class="o">:</span> <span class="mi">0</span> <span class="bp">&lt;</span> <span class="n">y</span><span class="o">)</span> <span class="o">:</span> <span class="mi">0</span> <span class="bp">&lt;</span> <span class="n">x</span> <span class="bp">+</span> <span class="n">y</span> <span class="o">:=</span>
<span class="n">zero_add</span> <span class="o">(</span><span class="mi">0</span><span class="o">:</span><span class="n">α</span><span class="o">)</span> <span class="bp">▸</span> <span class="n">add_lt_add</span> <span class="n">hx</span> <span class="n">hy</span>
</pre></div>

#### [ Kevin Buzzard (Jan 26 2019 at 21:29)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/adding%20positive%20reals/near/156940129):
<p>Right, so Neil got it to work with h2, the question is why what I wrote doesn't work.</p>

#### [ Kenny Lau (Jan 26 2019 at 21:30)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/adding%20positive%20reals/near/156940180):
<div class="codehilite"><pre><span></span><span class="n">universes</span> <span class="n">u</span>
<span class="kn">example</span> <span class="o">(</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">)</span> <span class="o">[</span><span class="n">ordered_cancel_comm_monoid</span> <span class="n">α</span><span class="o">]</span> <span class="o">{</span><span class="n">x</span> <span class="n">y</span> <span class="o">:</span> <span class="n">α</span><span class="o">}</span> <span class="o">(</span><span class="n">hx</span> <span class="o">:</span> <span class="mi">0</span> <span class="bp">&lt;</span> <span class="n">x</span><span class="o">)</span> <span class="o">(</span><span class="n">hy</span> <span class="o">:</span> <span class="mi">0</span> <span class="bp">&lt;</span> <span class="n">y</span><span class="o">)</span> <span class="o">:</span> <span class="mi">0</span> <span class="bp">&lt;</span> <span class="n">x</span> <span class="bp">+</span> <span class="n">y</span> <span class="o">:=</span>
<span class="k">have</span> <span class="n">h0</span> <span class="o">:</span> <span class="bp">_</span> <span class="o">:=</span> <span class="n">zero_add</span> <span class="o">(</span><span class="mi">0</span><span class="o">:</span><span class="n">α</span><span class="o">),</span>
<span class="n">eq</span><span class="bp">.</span><span class="n">subst</span> <span class="n">h0</span> <span class="err">$</span> <span class="n">add_lt_add</span> <span class="n">hx</span> <span class="n">hy</span>
</pre></div>

#### [ Kenny Lau (Jan 26 2019 at 21:30)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/adding%20positive%20reals/near/156940181):
<p>this works</p>

#### [ Kenny Lau (Jan 26 2019 at 21:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/adding%20positive%20reals/near/156940261):
<p>just follow standard procedures and you won't get into trouble :P</p>

#### [ Kevin Buzzard (Jan 26 2019 at 21:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/adding%20positive%20reals/near/156940306):
<p>Maybe it's just some higher order unification issue. Oh, I just remembered what a motive is. Oh so in fact that's exactly what Mario said.</p>

#### [ Kevin Buzzard (Jan 26 2019 at 21:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/adding%20positive%20reals/near/156940327):
<p>Neil -- the issue with <code>eq.subst</code> is that Lean has to guess this implicit argument <code>P</code> which in general is impossible. Oh Ok so in fact I'm now there.</p>

#### [ Neil Strickland (Jan 26 2019 at 21:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/adding%20positive%20reals/near/156940331):
<p>The library <code>add_pos</code> is just the obvious generalisation of my <code>real_add_pos</code>, so it is just a tiny proof term.  The only issues are (a) why the elaborater gets confused in the subtype context, but not if we write <code>add_pos</code> as a separate definition, and (b) how should you find <code>add_pos</code> if you do not already know about it?</p>
<p>For (b), I tried <code>#print ordered_semiring</code> and <code>#print ordered_ring</code> and <code>#print prefix ordered_semiring</code> and <code>#print ordered_monoid</code> (but <code>ordered_monoid</code> does not exist).  I did not try <code>#find</code> or <code>#print ordered_group</code>.  I don't know if one can learn anything from that history.</p>

#### [ Kenny Lau (Jan 26 2019 at 21:36)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/adding%20positive%20reals/near/156940378):
<p><span class="user-mention" data-user-id="110038">@Kevin Buzzard</span> we all know that a motive is a smooth projective variety with extra structures :P</p>

#### [ Kevin Buzzard (Jan 26 2019 at 21:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/adding%20positive%20reals/near/156940393):
<p>You're saying "I want the answer to be something like <code>0 &lt; x -&gt; 0 &lt; y -&gt; 0 &lt; x + y</code> and I want it to be this after we've taken all the <code>0+0</code>'s and replaced them with <code>0</code>s. Now guess <code>P</code>."</p>

#### [ Kevin Buzzard (Jan 26 2019 at 21:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/adding%20positive%20reals/near/156940407):
<p>And Lean guesses <code>0 + 0 &lt; x -&gt; 0 + 0 &lt; y -&gt; 0 + 0 &lt; x + y</code> because that's one of many valid guesses.</p>

#### [ Kevin Buzzard (Jan 26 2019 at 21:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/adding%20positive%20reals/near/156940461):
<p>and then it checks that <code>q.property</code> is <code>0 + 0 &lt; q.val</code> and it isn't, so it gives up. I think the CS guys call this "higher order unification" and they've proved that the general problem is undecidable. So Leo has to write some algorithm which works in as many simple cases as possible, but it can't be perfect.</p>

#### [ Kevin Buzzard (Jan 26 2019 at 21:39)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/adding%20positive%20reals/near/156940472):
<p>Kenny, it's the cohomology of a smooth projective variety.</p>

#### [ Kevin Buzzard (Jan 26 2019 at 21:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/adding%20positive%20reals/near/156940526):
<p>[NB by <code>P</code> I mean the <code>P</code> in <code>#check @eq.subst</code>]</p>

#### [ Kevin Buzzard (Jan 26 2019 at 21:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/adding%20positive%20reals/near/156940544):
<p>and CS people call <code>P</code> the motive.</p>

#### [ Kevin Buzzard (Jan 26 2019 at 21:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/adding%20positive%20reals/near/156940595):
<p><a href="https://leanprover.github.io/theorem_proving_in_lean/interacting_with_lean.html#elaboration-hints" target="_blank" title="https://leanprover.github.io/theorem_proving_in_lean/interacting_with_lean.html#elaboration-hints">https://leanprover.github.io/theorem_proving_in_lean/interacting_with_lean.html#elaboration-hints</a></p>

#### [ Kevin Buzzard (Jan 26 2019 at 21:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/adding%20positive%20reals/near/156940605):
<p>I think this stuff is hard to do well.</p>

#### [ Kevin Buzzard (Jan 26 2019 at 21:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/adding%20positive%20reals/near/156940900):
<div class="codehilite"><pre><span></span><span class="kn">import</span> <span class="n">data</span><span class="bp">.</span><span class="n">real</span><span class="bp">.</span><span class="n">basic</span>

<span class="n">def</span> <span class="n">pos_real</span> <span class="o">:=</span> <span class="o">{</span> <span class="n">q</span> <span class="o">:</span> <span class="n">ℝ</span> <span class="bp">//</span> <span class="mi">0</span> <span class="bp">&lt;</span> <span class="n">q</span><span class="o">}</span>

<span class="kn">instance</span> <span class="n">pos_real</span><span class="bp">.</span><span class="n">add</span> <span class="o">:</span> <span class="n">has_add</span> <span class="n">pos_real</span> <span class="o">:=</span>
 <span class="bp">⟨λ</span> <span class="n">q</span> <span class="n">r</span><span class="o">,</span><span class="bp">⟨</span><span class="n">q</span><span class="bp">.</span><span class="n">val</span> <span class="bp">+</span> <span class="n">r</span><span class="bp">.</span><span class="n">val</span><span class="o">,</span>
  <span class="k">begin</span>
   <span class="k">let</span> <span class="n">h0</span> <span class="o">:=</span> <span class="n">zero_add</span> <span class="o">(</span><span class="mi">0</span> <span class="o">:</span> <span class="n">ℝ</span><span class="o">),</span>
   <span class="n">exact</span> <span class="bp">@</span><span class="n">eq</span><span class="bp">.</span><span class="n">subst</span> <span class="n">ℝ</span> <span class="o">(</span><span class="bp">λ</span> <span class="n">x</span><span class="o">,</span> <span class="n">x</span> <span class="bp">&lt;</span> <span class="n">q</span><span class="bp">.</span><span class="n">val</span> <span class="bp">+</span> <span class="n">r</span><span class="bp">.</span><span class="n">val</span><span class="o">)</span> <span class="bp">_</span> <span class="bp">_</span> <span class="n">h0</span> <span class="o">(</span><span class="n">add_lt_add</span> <span class="n">q</span><span class="bp">.</span><span class="n">property</span> <span class="n">r</span><span class="bp">.</span><span class="n">property</span><span class="o">)</span>
  <span class="kn">end</span>
  <span class="bp">⟩⟩</span>
</pre></div>


<p>There's how to do with <code>eq.subst</code>. I had to tell it <code>P</code> explicitly, because it has an algorithm which produces a <code>P</code> and it produces the wrong <code>P</code> and now you're doomed. Elaboration and unification are thorny issues -- there was a thread about them yesterday. I can't tell you why one works and another doesn't. Lean has to solve a puzzle -- "fill in all the <code>{ ... }</code> stuff" -- and this is harder than it looks, I don't understand the arguments they use, and in higher order situations like this it's not surprising that they sometimes fail.</p>

#### [ Kevin Buzzard (Jan 26 2019 at 22:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/adding%20positive%20reals/near/156941555):
<p>Neil -- the best way to find lemmas is to learn the knack. I found this very frustrating at first, but the algorithm is first to learn all the three letter acronyms for everything eg add, sub, div, dvd, neg, pos, lt, nonneg etc (ok so they're not all three letters) and all the tricks like symm, comm, antisymm etc, then guess what your lemma is called, or at least part of it, then make sure you've imported the file where the lemma might be if necessary, then type in the parts of the name that you guessed and then mash <del>tab</del>ctrl-space and esc (at least in VS Code) and hope you find it in the list that appears (press ctrl-space to expand the definitions of the theorems which appear in the list).</p>

#### [ Kevin Buzzard (Jan 26 2019 at 22:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/adding%20positive%20reals/near/156941570):
<p>The lemma should be called <code>add_pos_of_pos_of_pos</code> but for things that come up a lot they tend to abbreviate them.</p>

#### [ Kevin Buzzard (Jan 27 2019 at 01:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/adding%20positive%20reals/near/156947546):
<p>For example, the triangle inequality is called <code>abs_add</code>.</p>

#### [ Kevin Buzzard (Jan 27 2019 at 01:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/adding%20positive%20reals/near/156947559):
<p>and the binomial theorem is called <code>add_pow</code> :-)</p>

#### [ Joseph Corneli (Jan 28 2019 at 14:29)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/adding%20positive%20reals/near/157024710):
<blockquote>
<p>anyway see my mathlib-grade <span aria-label="tm" class="emoji emoji-2122" role="img" title="tm">:tm:</span> revamp</p>
</blockquote>
<p><span class="user-mention" data-user-id="110064">@Kenny Lau</span> that looks great but I'm not sure how to use it properly.  Would you please tell me how I should adjust my example below to use your definitions?</p>
<div class="codehilite"><pre><span></span><span class="c1">-- ...</span>
<span class="kn">open</span> <span class="n">pos_of</span>

<span class="n">def</span> <span class="n">posreal</span> <span class="o">:=</span> <span class="n">pos_of</span> <span class="n">ℝ</span>

<span class="kn">notation</span> <span class="bp">`</span><span class="n">ℝ</span><span class="err">₊</span><span class="bp">`</span> <span class="o">:=</span> <span class="n">posreal</span>

<span class="c1">-- the following `instance` proofs seem superfluous given the definitions you created in the pos_of namespace, but how can I use your definitions?</span>
<span class="kn">instance</span> <span class="n">posreal</span><span class="bp">.</span><span class="n">add</span> <span class="o">:</span> <span class="n">has_add</span> <span class="n">posreal</span> <span class="o">:=</span>
 <span class="bp">⟨λ</span> <span class="n">q</span> <span class="n">r</span><span class="o">,</span> <span class="bp">⟨</span><span class="n">q</span><span class="bp">.</span><span class="n">val</span> <span class="bp">+</span> <span class="n">r</span><span class="bp">.</span><span class="n">val</span><span class="o">,</span> <span class="n">add_pos</span> <span class="n">q</span><span class="bp">.</span><span class="n">property</span> <span class="n">r</span><span class="bp">.</span><span class="n">property</span><span class="bp">⟩⟩</span>

<span class="kn">instance</span> <span class="n">posreal</span><span class="bp">.</span><span class="n">one</span> <span class="o">:</span> <span class="n">has_one</span> <span class="n">posreal</span> <span class="o">:=</span> <span class="bp">⟨⟨</span><span class="o">(</span><span class="mi">1</span><span class="o">:</span><span class="n">ℝ</span><span class="o">),</span> <span class="n">zero_lt_one</span><span class="bp">⟩⟩</span>

<span class="kn">example</span> <span class="o">:</span> <span class="n">ℝ</span><span class="err">₊</span> <span class="o">:=</span> <span class="o">(</span><span class="mi">2</span> <span class="o">:</span> <span class="n">ℝ</span><span class="err">₊</span><span class="o">)</span> <span class="bp">+</span> <span class="o">(</span><span class="mi">3</span><span class="o">:</span><span class="n">ℝ</span><span class="err">₊</span><span class="o">)</span>
</pre></div>

#### [ Kenny Lau (Jan 28 2019 at 14:30)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/adding%20positive%20reals/near/157024787):
<p>by unfold posreal; apply_instance</p>

#### [ Joseph Corneli (Jan 28 2019 at 14:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/adding%20positive%20reals/near/157025062):
<p>thanks!</p>


{% endraw %}
