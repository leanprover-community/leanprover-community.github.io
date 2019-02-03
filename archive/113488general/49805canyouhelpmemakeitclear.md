---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/49805canyouhelpmemakeitclear.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [can you help me make it clear](https://leanprover-community.github.io/archive/113488general/49805canyouhelpmemakeitclear.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Truong Nguyen (Sep 10 2018 at 16:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20you%20help%20me%20make%20it%20clear/near/133665638):
<p>I read the book about lean prover. There is some code like this:</p>
<div class="codehilite"><pre><span></span><span class="n">def</span> <span class="n">nat</span><span class="bp">.</span><span class="n">dvd</span> <span class="o">(</span><span class="n">m</span> <span class="n">n</span><span class="o">:</span> <span class="bp">ℕ</span> <span class="o">):</span> <span class="kt">Prop</span> <span class="o">:=</span> <span class="bp">∃</span> <span class="n">k</span><span class="o">,</span> <span class="n">n</span> <span class="bp">=</span> <span class="n">m</span> <span class="bp">*</span> <span class="n">k</span>
<span class="kn">instance</span> <span class="o">:</span> <span class="n">has_dvd</span> <span class="n">nat</span> <span class="o">:=</span> <span class="bp">⟨</span><span class="n">nat</span><span class="bp">.</span><span class="n">dvd</span> <span class="bp">⟩</span>
<span class="kn">theorem</span> <span class="n">nat</span><span class="bp">.</span><span class="n">dvd_refl</span> <span class="o">(</span><span class="n">n</span><span class="o">:</span> <span class="bp">ℕ</span> <span class="o">)</span> <span class="o">:</span> <span class="n">n</span> <span class="err">∣</span> <span class="n">n</span> <span class="o">:=</span> <span class="bp">⟨</span><span class="mi">1</span><span class="o">,</span> <span class="k">by</span> <span class="n">simp</span> <span class="bp">⟩</span>
</pre></div>


<p>I don't know why this theorem can be proved by &lt;1, simp&gt;. What does number 1 mean?<br>
Thank you for making it clear,</p>

#### [ Johan Commelin (Sep 10 2018 at 16:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20you%20help%20me%20make%20it%20clear/near/133665724):
<p>You see the <code>k</code> on the first line?</p>

#### [ Johan Commelin (Sep 10 2018 at 16:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20you%20help%20me%20make%20it%20clear/near/133665742):
<p>To prove <code>n | n</code>, you have to provide a <code>k</code>. And this proof provides <code>1</code>.</p>

#### [ Johan Commelin (Sep 10 2018 at 16:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20you%20help%20me%20make%20it%20clear/near/133665778):
<p>Afterwards, you have to prove <code>n = m * k</code>. And in your theorem <code>m</code> is <code>n</code>, and you just provided <code>k</code> is <code>1</code>.</p>

#### [ Johan Commelin (Sep 10 2018 at 16:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20you%20help%20me%20make%20it%20clear/near/133665788):
<p>The proof is then <code>by simp</code>.</p>

#### [ Truong Nguyen (Sep 10 2018 at 16:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20you%20help%20me%20make%20it%20clear/near/133665890):
<p>Ok, thanks. I see it is trivial now.</p>

#### [ Truong Nguyen (Sep 10 2018 at 16:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20you%20help%20me%20make%20it%20clear/near/133666052):
<p>By the way, is there any other way. I mean how can we write the code clearer.</p>

#### [ Johan Commelin (Sep 10 2018 at 16:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20you%20help%20me%20make%20it%20clear/near/133666084):
<p>Yes. This is called tactic mode.</p>

#### [ Johan Commelin (Sep 10 2018 at 16:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20you%20help%20me%20make%20it%20clear/near/133666101):
<div class="codehilite"><pre><span></span><span class="n">def</span> <span class="n">nat</span><span class="bp">.</span><span class="n">dvd</span> <span class="o">(</span><span class="n">m</span> <span class="n">n</span><span class="o">:</span> <span class="bp">ℕ</span> <span class="o">):</span> <span class="kt">Prop</span> <span class="o">:=</span> <span class="bp">∃</span> <span class="n">k</span><span class="o">,</span> <span class="n">n</span> <span class="bp">=</span> <span class="n">m</span> <span class="bp">*</span> <span class="n">k</span>
<span class="kn">instance</span> <span class="o">:</span> <span class="n">has_dvd</span> <span class="n">nat</span> <span class="o">:=</span> <span class="bp">⟨</span><span class="n">nat</span><span class="bp">.</span><span class="n">dvd</span> <span class="bp">⟩</span>
<span class="kn">theorem</span> <span class="n">nat</span><span class="bp">.</span><span class="n">dvd_refl</span> <span class="o">(</span><span class="n">n</span><span class="o">:</span> <span class="bp">ℕ</span> <span class="o">)</span> <span class="o">:</span> <span class="n">n</span> <span class="err">∣</span> <span class="n">n</span> <span class="o">:=</span>
<span class="k">begin</span>
  <span class="n">existsi</span> <span class="mi">1</span><span class="o">,</span>
  <span class="n">simp</span>
<span class="kn">end</span>
</pre></div>

#### [ Truong Nguyen (Sep 10 2018 at 16:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20you%20help%20me%20make%20it%20clear/near/133666288):
<p>Oh, ok. How can we unfold the definition of "|", to make it appear like: </p>
<div class="codehilite"><pre><span></span><span class="err">\</span><span class="n">exists</span> <span class="n">k</span><span class="o">,</span> <span class="n">n</span> <span class="bp">=</span> <span class="n">m</span> <span class="bp">*</span> <span class="n">k</span>
</pre></div>

#### [ Truong Nguyen (Sep 10 2018 at 16:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20you%20help%20me%20make%20it%20clear/near/133666491):
<p>I mean, to make it look like this:</p>
<div class="codehilite"><pre><span></span><span class="kn">example</span> <span class="o">(</span><span class="n">n</span><span class="o">:</span> <span class="bp">ℕ</span> <span class="o">):</span> <span class="bp">∃</span> <span class="n">k</span><span class="o">,</span> <span class="n">n</span> <span class="bp">=</span> <span class="n">n</span> <span class="bp">*</span> <span class="n">k</span> <span class="o">:=</span> <span class="bp">_</span>
</pre></div>

#### [ Reid Barton (Sep 10 2018 at 16:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20you%20help%20me%20make%20it%20clear/near/133666552):
<p>Do you mean you want to change what the goal looks like, inside the tactic block?</p>

#### [ Truong Nguyen (Sep 10 2018 at 16:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20you%20help%20me%20make%20it%20clear/near/133666565):
<p>Oh, yes</p>

#### [ Reid Barton (Sep 10 2018 at 16:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20you%20help%20me%20make%20it%20clear/near/133666643):
<p>Two ways. One is that you can use <code>change</code> to change the goal to something definitionally equivalent, like</p>
<div class="codehilite"><pre><span></span>  <span class="n">change</span> <span class="bp">∃</span> <span class="n">k</span><span class="o">,</span> <span class="n">n</span> <span class="bp">=</span> <span class="n">n</span> <span class="bp">*</span> <span class="n">k</span><span class="o">,</span>
</pre></div>


<p>Of course, that depends on knowing what the unfolded form should be</p>

#### [ Truong Nguyen (Sep 10 2018 at 16:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20you%20help%20me%20make%20it%20clear/near/133666803):
<p>WHat is the second way</p>

#### [ Reid Barton (Sep 10 2018 at 16:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20you%20help%20me%20make%20it%20clear/near/133666817):
<p>The other way is to use <code>unfold</code> or <code>dsimp</code> or related tactics to unfold the <code>∣</code> operation, but because it is notation in this case, you need to know the actual name of the operator, which is <code>has_dvd.dvd</code></p>

#### [ Reid Barton (Sep 10 2018 at 16:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20you%20help%20me%20make%20it%20clear/near/133666938):
<p>Then <code>has_dvd</code> is a class, so you also need to unfold the actual instance for <code>nat</code>. If you start with</p>
<div class="codehilite"><pre><span></span>  <span class="n">unfold</span> <span class="n">has_dvd</span><span class="bp">.</span><span class="n">dvd</span><span class="o">,</span>
</pre></div>


<p>then you'll see what the actual operation is in the goal window -- it's <code>nat.dvd</code></p>

#### [ Truong Nguyen (Sep 10 2018 at 16:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20you%20help%20me%20make%20it%20clear/near/133666955):
<p>I tried this:</p>
<div class="codehilite"><pre><span></span><span class="kn">theorem</span> <span class="n">nat</span><span class="bp">.</span><span class="n">dvd_refl</span> <span class="o">(</span><span class="n">n</span><span class="o">:</span> <span class="bp">ℕ</span> <span class="o">)</span> <span class="o">:</span> <span class="n">n</span> <span class="err">∣</span> <span class="n">n</span> <span class="o">:=</span>
<span class="k">begin</span>
<span class="n">unfold</span> <span class="n">nat</span><span class="bp">.</span><span class="n">dvd</span><span class="o">,</span>
<span class="kn">end</span>
</pre></div>


<p>But, I got error</p>

#### [ Reid Barton (Sep 10 2018 at 16:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20you%20help%20me%20make%20it%20clear/near/133666979):
<p>So then you can unfold both at once with</p>
<div class="codehilite"><pre><span></span>  <span class="n">unfold</span> <span class="n">has_dvd</span><span class="bp">.</span><span class="n">dvd</span> <span class="n">nat</span><span class="bp">.</span><span class="n">dvd</span><span class="o">,</span>
</pre></div>

#### [ Reid Barton (Sep 10 2018 at 16:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20you%20help%20me%20make%20it%20clear/near/133667037):
<p>Yep, because you have to unfold <code>has_dvd.dvd</code> first.<br>
If you write <code>set_option pp.notation false</code> before your theorem, you can see what the notation really represents.</p>

#### [ Truong Nguyen (Sep 10 2018 at 17:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20you%20help%20me%20make%20it%20clear/near/133667112):
<p>Oh, I made it works now.<br>
It run fine</p>
<div class="codehilite"><pre><span></span><span class="kn">theorem</span> <span class="n">nat</span><span class="bp">.</span><span class="n">dvd_refl</span> <span class="o">(</span><span class="n">n</span><span class="o">:</span> <span class="bp">ℕ</span> <span class="o">)</span> <span class="o">:</span> <span class="n">n</span> <span class="err">∣</span> <span class="n">n</span> <span class="o">:=</span>
<span class="k">begin</span>
<span class="n">unfold</span> <span class="n">has_dvd</span><span class="bp">.</span><span class="n">dvd</span> <span class="n">nat</span><span class="bp">.</span><span class="n">dvd</span><span class="o">,</span>
<span class="kn">end</span>
</pre></div>

#### [ Mario Carneiro (Sep 10 2018 at 17:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20you%20help%20me%20make%20it%20clear/near/133669697):
<p>you can write <code>dsimp [(∣)]</code> too</p>


{% endraw %}
