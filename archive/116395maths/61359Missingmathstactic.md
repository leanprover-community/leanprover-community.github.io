---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/61359Missingmathstactic.html
---

## Stream: [maths](https://leanprover-community.github.io/archive/116395maths/index.html)
### Topic: [Missing maths tactic?](https://leanprover-community.github.io/archive/116395maths/61359Missingmathstactic.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Kevin Buzzard (Nov 23 2018 at 22:39)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Missing%20maths%20tactic%3F/near/148250605):
<p><code>example (a b c d : ℤ) (H : a - b = c * d) : b - a = c * (-d) := by simp [H] -- fails</code>.</p>
<p>Is this one of those instances when someone familiar with Coq says "oh, it would work if you had &lt;insert name of tactic which I don't know what it does, but it turns out it does this&gt;"? I'm teaching equivalence relations shortly, and this stuff comes up with congruences; I want to give Lean a big push if possible but I want to make it look slick, ideally.</p>
<p>I remark that <code>example (a b c d : ℤ) (H : a - b = c * d) : b - a = c * (-d) := by simp [H.symm]</code> works! But I am stuck with having it this way round because it's how <code>has_dvd.dvd</code> unfolds on int :-( [I'm trying to prove congruence mod c is symmetric in a completely transparent way]</p>

#### [ Kevin Buzzard (Nov 23 2018 at 23:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Missing%20maths%20tactic%3F/near/148251400):
<p>heh:</p>
<div class="codehilite"><pre><span></span><span class="kn">example</span> <span class="o">(</span><span class="n">a</span> <span class="n">b</span> <span class="n">c</span> <span class="o">:</span> <span class="bp">ℤ</span><span class="o">)</span> <span class="o">:</span> <span class="n">a</span> <span class="bp">-</span> <span class="n">c</span> <span class="bp">=</span> <span class="n">a</span> <span class="bp">-</span> <span class="n">b</span> <span class="bp">+</span> <span class="o">(</span><span class="n">b</span> <span class="bp">-</span> <span class="n">c</span><span class="o">)</span> <span class="o">:=</span> <span class="k">by</span> <span class="n">simp</span> <span class="c1">-- fails</span>
</pre></div>


<div class="codehilite"><pre><span></span><span class="kn">import</span> <span class="n">tactic</span><span class="bp">.</span><span class="n">ring</span>

<span class="kn">example</span> <span class="o">(</span><span class="n">a</span> <span class="n">b</span> <span class="n">c</span> <span class="o">:</span> <span class="bp">ℤ</span><span class="o">)</span> <span class="o">:</span> <span class="n">a</span> <span class="bp">-</span> <span class="n">c</span> <span class="bp">=</span> <span class="n">a</span> <span class="bp">-</span> <span class="n">b</span> <span class="bp">+</span> <span class="o">(</span><span class="n">b</span> <span class="bp">-</span> <span class="n">c</span><span class="o">)</span> <span class="o">:=</span> <span class="k">by</span> <span class="n">ring</span> <span class="c1">-- works (of course)</span>
</pre></div>


<p>but the surprise is</p>
<div class="codehilite"><pre><span></span><span class="kn">import</span> <span class="n">tactic</span><span class="bp">.</span><span class="n">ring</span>

<span class="kn">example</span> <span class="o">(</span><span class="n">a</span> <span class="n">b</span> <span class="n">c</span> <span class="o">:</span> <span class="bp">ℤ</span><span class="o">)</span> <span class="o">:</span> <span class="n">a</span> <span class="bp">-</span> <span class="n">c</span> <span class="bp">=</span> <span class="n">a</span> <span class="bp">-</span> <span class="n">b</span> <span class="bp">+</span> <span class="o">(</span><span class="n">b</span> <span class="bp">-</span> <span class="n">c</span><span class="o">)</span> <span class="o">:=</span> <span class="k">by</span> <span class="n">simp</span> <span class="c1">-- works!</span>
</pre></div>


<p>For this one I knew the tactic, but then I realised I didn't need it.</p>

#### [ Patrick Massot (Nov 23 2018 at 23:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Missing%20maths%20tactic%3F/near/148251450):
<p>I think last year we had an extended discussion about how to define this equivalence relation in order to get an easy proof</p>

#### [ Kevin Buzzard (Nov 23 2018 at 23:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Missing%20maths%20tactic%3F/near/148251456):
<p>But I really want a one-liner for this if possible:</p>
<div class="codehilite"><pre><span></span><span class="kn">example</span> <span class="o">(</span><span class="n">m</span> <span class="n">a</span> <span class="n">b</span> <span class="n">c</span> <span class="n">j</span> <span class="n">k</span> <span class="o">:</span> <span class="bp">ℤ</span><span class="o">)</span> <span class="o">(</span><span class="n">Hj</span> <span class="o">:</span> <span class="n">a</span> <span class="bp">-</span> <span class="n">b</span> <span class="bp">=</span> <span class="n">m</span> <span class="bp">*</span> <span class="n">j</span><span class="o">)</span> <span class="o">(</span><span class="n">Hk</span> <span class="o">:</span> <span class="n">b</span> <span class="bp">-</span> <span class="n">c</span> <span class="bp">=</span> <span class="n">m</span> <span class="bp">*</span> <span class="n">k</span><span class="o">)</span> <span class="o">:</span>
<span class="n">a</span> <span class="bp">-</span> <span class="n">c</span> <span class="bp">=</span> <span class="n">m</span> <span class="bp">*</span> <span class="o">(</span><span class="n">j</span> <span class="bp">+</span> <span class="n">k</span><span class="o">)</span> <span class="o">:=</span>
<span class="k">begin</span>
  <span class="n">rw</span> <span class="o">[</span><span class="n">mul_add</span><span class="o">],</span>
  <span class="n">rw</span> <span class="o">[</span><span class="err">←</span><span class="n">Hj</span><span class="o">,</span><span class="err">←</span><span class="n">Hk</span><span class="o">],</span>
  <span class="c1">-- ⊢ a - c = a - b + (b - c)</span>
  <span class="n">simp</span><span class="o">,</span> <span class="c1">-- works if tactic.ring imported</span>
<span class="kn">end</span>
</pre></div>


<p>I want to do ring [Hj,Hk] or something, but I'm well aware that life isn't so easy.</p>

#### [ Kevin Buzzard (Nov 23 2018 at 23:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Missing%20maths%20tactic%3F/near/148251513):
<blockquote>
<p>I think last year we had an extended discussion about how to define this equivalence relation in order to get an easy proof</p>
</blockquote>
<p>Yes, the trick is to define congruence mod m (it was mod 37 last time) in a different way -- the order matters. But unfortunately in my lectures I defined congruence mod m to mean <code>m | (a - b)</code> so now I'm stuck with it and it unfolds to something which is not in the optimal order.</p>

#### [ Kevin Buzzard (Nov 23 2018 at 23:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Missing%20maths%20tactic%3F/near/148251525):
<p>Is this one of those things which is done by omega or cooper or something -- these tactics that I have no idea what they are?</p>

#### [ Andrew Ashworth (Nov 23 2018 at 23:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Missing%20maths%20tactic%3F/near/148251577):
<p>Omega only handles presburger arithmetic, ie no multiplication.</p>

#### [ Kevin Buzzard (Nov 23 2018 at 23:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Missing%20maths%20tactic%3F/near/148251584):
<p>Hmm. I suspect <code>by Groebner_basis</code> might do it.</p>

#### [ Andrew Ashworth (Nov 23 2018 at 23:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Missing%20maths%20tactic%3F/near/148251585):
<p>Cooper might do it, but I don't have lean in front of me to try it</p>

#### [ Kevin Buzzard (Nov 23 2018 at 23:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Missing%20maths%20tactic%3F/near/148251588):
<p>I have Lean in front of me -- how do I get cooper working?</p>

#### [ Reid Barton (Nov 23 2018 at 23:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Missing%20maths%20tactic%3F/near/148251643):
<p>Maybe you can add <a href="https://github.com/skbaek/qe" target="_blank" title="https://github.com/skbaek/qe">https://github.com/skbaek/qe</a> as a dependency now</p>

#### [ Kenny Lau (Nov 23 2018 at 23:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Missing%20maths%20tactic%3F/near/148251707):
<div class="codehilite"><pre><span></span><span class="kn">example</span> <span class="o">(</span><span class="n">m</span> <span class="n">a</span> <span class="n">b</span> <span class="n">c</span> <span class="n">j</span> <span class="n">k</span> <span class="o">:</span> <span class="bp">ℤ</span><span class="o">)</span> <span class="o">(</span><span class="n">Hj</span> <span class="o">:</span> <span class="n">a</span> <span class="bp">-</span> <span class="n">b</span> <span class="bp">=</span> <span class="n">m</span> <span class="bp">*</span> <span class="n">j</span><span class="o">)</span> <span class="o">(</span><span class="n">Hk</span> <span class="o">:</span> <span class="n">b</span> <span class="bp">-</span> <span class="n">c</span> <span class="bp">=</span> <span class="n">m</span> <span class="bp">*</span> <span class="n">k</span><span class="o">)</span> <span class="o">:</span>
  <span class="n">a</span> <span class="bp">-</span> <span class="n">c</span> <span class="bp">=</span> <span class="n">m</span> <span class="bp">*</span> <span class="o">(</span><span class="n">j</span> <span class="bp">+</span> <span class="n">k</span><span class="o">)</span> <span class="o">:=</span>
<span class="k">by</span> <span class="n">rw</span> <span class="o">[</span><span class="n">mul_add</span><span class="o">,</span> <span class="err">←</span> <span class="n">Hj</span><span class="o">,</span> <span class="err">←</span> <span class="n">Hk</span><span class="o">,</span> <span class="n">sub_add</span><span class="o">,</span> <span class="n">sub_sub_self</span><span class="o">]</span>
</pre></div>

#### [ Reid Barton (Nov 23 2018 at 23:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Missing%20maths%20tactic%3F/near/148251708):
<p>(but I don't know how to actually <em>use</em> it)</p>

#### [ Andrew Ashworth (Nov 23 2018 at 23:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Missing%20maths%20tactic%3F/near/148251711):
<p>I think the examples in <a href="https://github.com/skbaek/qe/blob/master/src/examples.lean" target="_blank" title="https://github.com/skbaek/qe/blob/master/src/examples.lean">https://github.com/skbaek/qe/blob/master/src/examples.lean</a> are self explanatory</p>

#### [ Kevin Buzzard (Nov 23 2018 at 23:16)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Missing%20maths%20tactic%3F/near/148251716):
<div class="codehilite"><pre><span></span><span class="kn">definition</span> <span class="n">cong_mod_37</span> <span class="o">(</span><span class="n">a</span> <span class="n">b</span> <span class="o">:</span> <span class="bp">ℤ</span><span class="o">)</span> <span class="o">:=</span> <span class="bp">∃</span> <span class="n">k</span> <span class="o">:</span> <span class="bp">ℤ</span><span class="o">,</span> <span class="mi">37</span> <span class="bp">*</span> <span class="n">k</span> <span class="bp">=</span> <span class="n">a</span> <span class="bp">-</span> <span class="n">b</span>

<span class="kn">example</span> <span class="o">(</span><span class="n">a</span> <span class="o">:</span> <span class="bp">ℤ</span><span class="o">)</span> <span class="o">:</span> <span class="n">cong_mod_37</span> <span class="n">a</span> <span class="n">a</span> <span class="o">:=</span>
<span class="k">begin</span>
  <span class="n">use</span> <span class="mi">0</span><span class="o">,</span>
  <span class="n">simp</span><span class="o">,</span>
<span class="kn">end</span>

<span class="kn">example</span> <span class="o">(</span><span class="n">a</span> <span class="n">b</span> <span class="o">:</span> <span class="bp">ℤ</span><span class="o">)</span> <span class="o">(</span><span class="n">H</span> <span class="o">:</span> <span class="n">cong_mod_37</span> <span class="n">a</span> <span class="n">b</span><span class="o">)</span> <span class="o">:</span> <span class="n">cong_mod_37</span> <span class="n">b</span> <span class="n">a</span> <span class="o">:=</span>
<span class="k">begin</span>
  <span class="n">cases</span> <span class="n">H</span> <span class="k">with</span> <span class="n">k</span> <span class="n">Hk</span><span class="o">,</span>
  <span class="n">use</span> <span class="bp">-</span><span class="n">k</span><span class="o">,</span>
  <span class="n">simp</span> <span class="o">[</span><span class="n">Hk</span><span class="o">],</span>
<span class="kn">end</span>

<span class="kn">example</span> <span class="o">(</span><span class="n">a</span> <span class="n">b</span> <span class="n">c</span> <span class="o">:</span> <span class="bp">ℤ</span><span class="o">)</span> <span class="o">(</span><span class="n">H1</span> <span class="o">:</span> <span class="n">cong_mod_37</span> <span class="n">a</span> <span class="n">b</span><span class="o">)</span> <span class="o">(</span><span class="n">H2</span> <span class="o">:</span> <span class="n">cong_mod_37</span> <span class="n">b</span> <span class="n">c</span><span class="o">)</span> <span class="o">:</span> <span class="n">cong_mod_37</span> <span class="n">a</span> <span class="n">c</span> <span class="o">:=</span>
<span class="k">begin</span>
  <span class="n">cases</span> <span class="n">H1</span> <span class="k">with</span> <span class="n">j</span> <span class="n">Hj</span><span class="o">,</span>
  <span class="n">cases</span> <span class="n">H2</span> <span class="k">with</span> <span class="n">k</span> <span class="n">Hk</span><span class="o">,</span>
  <span class="n">use</span> <span class="o">(</span><span class="n">j</span><span class="bp">+</span><span class="n">k</span><span class="o">),</span>
  <span class="n">simp</span> <span class="o">[</span><span class="n">mul_add</span><span class="o">,</span><span class="n">Hj</span><span class="o">,</span><span class="n">Hk</span><span class="o">],</span>
<span class="kn">end</span>
</pre></div>

#### [ Kevin Buzzard (Nov 23 2018 at 23:16)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Missing%20maths%20tactic%3F/near/148251753):
<p><span class="user-mention" data-user-id="110064">@Kenny Lau</span> I know how to do it, but the problem is that your proof is a great example of how to put first year undergraduates off Lean.</p>

#### [ Kevin Buzzard (Nov 23 2018 at 23:16)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Missing%20maths%20tactic%3F/near/148251754):
<p>Compare with my 37 proofs, where everything is just simp.</p>

#### [ Patrick Massot (Nov 23 2018 at 23:30)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Missing%20maths%20tactic%3F/near/148252152):
<p><span class="user-mention" data-user-id="110038">@Kevin Buzzard</span> about <code>example (m a b c j k : ℤ) (Hj : a - b = m * j) (Hk : b - c = m * k) : a - c = m * (j + k)</code>. For students I think a two-liner is good enough. The proof you would tell them is: "add equations Hj and Hk, then compute". Having a tactic <code>add_eq Hk Hj</code> is clearly within reach (actually we should both know how to do that by now). It would replace the first line in:</p>
<div class="codehilite"><pre><span></span><span class="kn">example</span> <span class="o">(</span><span class="n">m</span> <span class="n">a</span> <span class="n">b</span> <span class="n">c</span> <span class="n">j</span> <span class="n">k</span> <span class="o">:</span> <span class="bp">ℤ</span><span class="o">)</span> <span class="o">(</span><span class="n">Hj</span> <span class="o">:</span> <span class="n">a</span> <span class="bp">-</span> <span class="n">b</span> <span class="bp">=</span> <span class="n">m</span> <span class="bp">*</span> <span class="n">j</span><span class="o">)</span> <span class="o">(</span><span class="n">Hk</span> <span class="o">:</span> <span class="n">b</span> <span class="bp">-</span> <span class="n">c</span> <span class="bp">=</span> <span class="n">m</span> <span class="bp">*</span> <span class="n">k</span><span class="o">)</span> <span class="o">:</span>
<span class="n">a</span> <span class="bp">-</span> <span class="n">c</span> <span class="bp">=</span> <span class="n">m</span> <span class="bp">*</span> <span class="o">(</span><span class="n">j</span> <span class="bp">+</span> <span class="n">k</span><span class="o">)</span> <span class="o">:=</span>
<span class="k">begin</span>
  <span class="k">have</span> <span class="o">:</span> <span class="o">(</span><span class="n">a</span> <span class="bp">-</span> <span class="n">b</span><span class="o">)</span> <span class="bp">+</span> <span class="o">(</span><span class="n">b</span> <span class="bp">-</span> <span class="n">c</span><span class="o">)</span> <span class="bp">=</span> <span class="o">(</span><span class="n">m</span> <span class="bp">*</span> <span class="n">j</span><span class="o">)</span> <span class="bp">+</span> <span class="o">(</span><span class="n">m</span> <span class="bp">*</span> <span class="n">k</span><span class="o">)</span> <span class="o">:=</span> <span class="n">congr</span> <span class="o">(</span><span class="n">congr_arg</span> <span class="n">int</span><span class="bp">.</span><span class="n">add</span> <span class="n">Hj</span><span class="o">)</span> <span class="n">Hk</span><span class="o">,</span>
  <span class="n">ring</span> <span class="n">at</span> <span class="bp">*</span><span class="o">,</span>
  <span class="n">assumption</span>
<span class="kn">end</span>
</pre></div>

#### [ Kenny Lau (Nov 23 2018 at 23:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Missing%20maths%20tactic%3F/near/148252226):
<p>... can someone teach me how to write tactics</p>

#### [ Patrick Massot (Nov 23 2018 at 23:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Missing%20maths%20tactic%3F/near/148252241):
<p>Yes</p>

#### [ Patrick Massot (Nov 23 2018 at 23:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Missing%20maths%20tactic%3F/near/148252248):
<p>Johannes, Mario, Simon, Rob, Scott...</p>

#### [ Andrew Ashworth (Nov 23 2018 at 23:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Missing%20maths%20tactic%3F/near/148252389):
<p>The textbook everyone recommends is Handbook of Practical Logic and Automated Reasoning</p>

#### [ Andrew Ashworth (Nov 23 2018 at 23:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Missing%20maths%20tactic%3F/near/148252503):
<p>Term rewriting and all that is good too, so is Modern Computer Algebra, depending on what you want your tactics to do</p>

#### [ Patrick Massot (Nov 23 2018 at 23:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Missing%20maths%20tactic%3F/near/148252856):
<p>Andrew, our problem stops us before needing anything from these books. It's about Lean meta programming (especially parsing arguments in our case).</p>

#### [ Patrick Massot (Nov 23 2018 at 23:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Missing%20maths%20tactic%3F/near/148252902):
<p>Our only immediate hope is <span class="user-mention" data-user-id="110026">@Simon Hudon</span> will pity us, and we'll wake up with a <code>add_eq</code> tactic PR'ed to mathlib.</p>

#### [ Simon Hudon (Nov 23 2018 at 23:56)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Missing%20maths%20tactic%3F/near/148252955):
<p>How can you be sure that he heard you?</p>

#### [ Patrick Massot (Nov 23 2018 at 23:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Missing%20maths%20tactic%3F/near/148252971):
<p>That's the magic of Zulip's notification</p>

#### [ Patrick Massot (Nov 23 2018 at 23:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Missing%20maths%20tactic%3F/near/148252974):
<p>And it's midnight here, so I'm allowed to dream</p>

#### [ Simon Hudon (Nov 23 2018 at 23:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Missing%20maths%20tactic%3F/near/148252975):
<p>You sure are</p>

#### [ Simon Hudon (Nov 23 2018 at 23:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Missing%20maths%20tactic%3F/near/148253023):
<p>What's the gist of this <code>add_eq</code> that you're looking for?</p>

#### [ Patrick Massot (Nov 23 2018 at 23:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Missing%20maths%20tactic%3F/near/148253036):
<p>It replaces</p>
<div class="codehilite"><pre><span></span><span class="kn">example</span> <span class="o">(</span><span class="n">m</span> <span class="n">a</span> <span class="n">b</span> <span class="n">c</span> <span class="n">j</span> <span class="n">k</span> <span class="o">:</span> <span class="bp">ℤ</span><span class="o">)</span> <span class="o">(</span><span class="n">Hj</span> <span class="o">:</span> <span class="n">a</span> <span class="bp">-</span> <span class="n">b</span> <span class="bp">=</span> <span class="n">m</span> <span class="bp">*</span> <span class="n">j</span><span class="o">)</span> <span class="o">(</span><span class="n">Hk</span> <span class="o">:</span> <span class="n">b</span> <span class="bp">-</span> <span class="n">c</span> <span class="bp">=</span> <span class="n">m</span> <span class="bp">*</span> <span class="n">k</span><span class="o">)</span> <span class="o">:</span>
<span class="n">a</span> <span class="bp">-</span> <span class="n">c</span> <span class="bp">=</span> <span class="n">m</span> <span class="bp">*</span> <span class="o">(</span><span class="n">j</span> <span class="bp">+</span> <span class="n">k</span><span class="o">)</span> <span class="o">:=</span>
<span class="k">begin</span>
  <span class="k">have</span> <span class="o">:</span> <span class="o">(</span><span class="n">a</span> <span class="bp">-</span> <span class="n">b</span><span class="o">)</span> <span class="bp">+</span> <span class="o">(</span><span class="n">b</span> <span class="bp">-</span> <span class="n">c</span><span class="o">)</span> <span class="bp">=</span> <span class="o">(</span><span class="n">m</span> <span class="bp">*</span> <span class="n">j</span><span class="o">)</span> <span class="bp">+</span> <span class="o">(</span><span class="n">m</span> <span class="bp">*</span> <span class="n">k</span><span class="o">)</span> <span class="o">:=</span> <span class="n">congr</span> <span class="o">(</span><span class="n">congr_arg</span> <span class="n">int</span><span class="bp">.</span><span class="n">add</span> <span class="n">Hj</span><span class="o">)</span> <span class="n">Hk</span><span class="o">,</span>
  <span class="n">ring</span> <span class="n">at</span> <span class="bp">*</span><span class="o">,</span>
  <span class="n">assumption</span>
<span class="kn">end</span>
</pre></div>


<p>by</p>
<div class="codehilite"><pre><span></span><span class="kn">example</span> <span class="o">(</span><span class="n">m</span> <span class="n">a</span> <span class="n">b</span> <span class="n">c</span> <span class="n">j</span> <span class="n">k</span> <span class="o">:</span> <span class="bp">ℤ</span><span class="o">)</span> <span class="o">(</span><span class="n">Hj</span> <span class="o">:</span> <span class="n">a</span> <span class="bp">-</span> <span class="n">b</span> <span class="bp">=</span> <span class="n">m</span> <span class="bp">*</span> <span class="n">j</span><span class="o">)</span> <span class="o">(</span><span class="n">Hk</span> <span class="o">:</span> <span class="n">b</span> <span class="bp">-</span> <span class="n">c</span> <span class="bp">=</span> <span class="n">m</span> <span class="bp">*</span> <span class="n">k</span><span class="o">)</span> <span class="o">:</span>
<span class="n">a</span> <span class="bp">-</span> <span class="n">c</span> <span class="bp">=</span> <span class="n">m</span> <span class="bp">*</span> <span class="o">(</span><span class="n">j</span> <span class="bp">+</span> <span class="n">k</span><span class="o">)</span> <span class="o">:=</span>
<span class="k">begin</span>
  <span class="n">add_eq</span> <span class="n">Hj</span> <span class="n">Hk</span><span class="o">,</span>
  <span class="n">ring</span> <span class="n">at</span> <span class="bp">*</span><span class="o">,</span>
  <span class="n">assumption</span>
<span class="kn">end</span>
</pre></div>

#### [ Patrick Massot (Nov 24 2018 at 00:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Missing%20maths%20tactic%3F/near/148253099):
<p>It's similar in spirit to the <code>mul_left</code> tactic that we never finished writing</p>

#### [ Simon Hudon (Nov 24 2018 at 00:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Missing%20maths%20tactic%3F/near/148253117):
<p>Wouldn't a lemma work just as well?</p>

#### [ Patrick Massot (Nov 24 2018 at 00:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Missing%20maths%20tactic%3F/near/148253233):
<p>I don't understand how you can miss such opportunities to save the world with a new tactic</p>

#### [ Patrick Massot (Nov 24 2018 at 00:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Missing%20maths%20tactic%3F/near/148253234):
<div class="codehilite"><pre><span></span><span class="kn">lemma</span> <span class="n">add_eq</span> <span class="o">{</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span><span class="bp">*</span><span class="o">}</span> <span class="o">[</span><span class="n">has_add</span> <span class="n">α</span><span class="o">]</span> <span class="o">{</span><span class="n">b</span> <span class="n">c</span> <span class="n">d</span> <span class="n">e</span> <span class="o">:</span> <span class="n">α</span><span class="o">}</span> <span class="o">(</span><span class="n">H</span> <span class="o">:</span> <span class="n">b</span> <span class="bp">=</span> <span class="n">c</span><span class="o">)</span> <span class="o">(</span><span class="n">H&#39;</span> <span class="o">:</span> <span class="n">d</span> <span class="bp">=</span> <span class="n">e</span><span class="o">)</span> <span class="o">:</span>
  <span class="n">b</span> <span class="bp">+</span> <span class="n">d</span> <span class="bp">=</span> <span class="n">c</span> <span class="bp">+</span> <span class="n">e</span> <span class="o">:=</span> <span class="n">congr</span> <span class="o">(</span><span class="n">congr_arg</span> <span class="n">has_add</span><span class="bp">.</span><span class="n">add</span> <span class="n">H</span><span class="o">)</span> <span class="n">H&#39;</span>

<span class="kn">example</span> <span class="o">(</span><span class="n">m</span> <span class="n">a</span> <span class="n">b</span> <span class="n">c</span> <span class="n">j</span> <span class="n">k</span> <span class="o">:</span> <span class="bp">ℤ</span><span class="o">)</span> <span class="o">(</span><span class="n">Hj</span> <span class="o">:</span> <span class="n">a</span> <span class="bp">-</span> <span class="n">b</span> <span class="bp">=</span> <span class="n">m</span> <span class="bp">*</span> <span class="n">j</span><span class="o">)</span> <span class="o">(</span><span class="n">Hk</span> <span class="o">:</span> <span class="n">b</span> <span class="bp">-</span> <span class="n">c</span> <span class="bp">=</span> <span class="n">m</span> <span class="bp">*</span> <span class="n">k</span><span class="o">)</span> <span class="o">:</span>
<span class="n">a</span> <span class="bp">-</span> <span class="n">c</span> <span class="bp">=</span> <span class="n">m</span> <span class="bp">*</span> <span class="o">(</span><span class="n">j</span> <span class="bp">+</span> <span class="n">k</span><span class="o">)</span> <span class="o">:=</span>
<span class="k">begin</span>
  <span class="k">have</span> <span class="o">:=</span> <span class="n">add_eq</span> <span class="n">Hj</span> <span class="n">Hk</span><span class="o">,</span>
  <span class="n">ring</span> <span class="n">at</span> <span class="bp">*</span><span class="o">,</span>
  <span class="n">assumption</span><span class="o">,</span>
<span class="kn">end</span>
</pre></div>

#### [ Simon Hudon (Nov 24 2018 at 00:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Missing%20maths%20tactic%3F/near/148253274):
<p>My favorite tactics are those I don't have to write :P</p>

#### [ Simon Hudon (Nov 24 2018 at 00:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Missing%20maths%20tactic%3F/near/148253283):
<p>(btw, you type faster than I do, I was about to write that!)</p>

#### [ Patrick Massot (Nov 24 2018 at 00:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Missing%20maths%20tactic%3F/near/148253285):
<p>I wonder whether this lemma is already in mathlib, the hypothesis <code>has_add α</code> is really weak</p>

#### [ Reid Barton (Nov 24 2018 at 00:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Missing%20maths%20tactic%3F/near/148253331):
<p>Maybe a two-argument <code>congr_arg₂</code> would be nice?</p>

#### [ Patrick Massot (Nov 24 2018 at 00:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Missing%20maths%20tactic%3F/near/148253333):
<p>Yes, I also thought about that when writing the first version of the proof</p>

#### [ Kenny Lau (Nov 24 2018 at 00:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Missing%20maths%20tactic%3F/near/148253445):
<blockquote>
<p>Maybe a two-argument <code>congr_arg₂</code> would be nice?</p>
</blockquote>
<p><a href="https://github.com/leanprover/mathlib/pull/118#discussion_r183841541" target="_blank" title="https://github.com/leanprover/mathlib/pull/118#discussion_r183841541">https://github.com/leanprover/mathlib/pull/118#discussion_r183841541</a></p>

#### [ Patrick Massot (Nov 24 2018 at 00:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Missing%20maths%20tactic%3F/near/148253449):
<p>But for students I would still prefer to have the <code>add_eq</code> lemma and its friends that the abstract version</p>

#### [ Patrick Massot (Nov 24 2018 at 00:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Missing%20maths%20tactic%3F/near/148253515):
<p>Same story as ever: an impressive proof from Kenny</p>
<div class="codehilite"><pre><span></span><span class="kn">theorem</span> <span class="n">congr_arg₂</span> <span class="o">{</span><span class="n">α</span> <span class="n">β</span> <span class="n">γ</span> <span class="o">:</span> <span class="kt">Type</span><span class="bp">*</span><span class="o">}</span> <span class="o">(</span><span class="n">f</span> <span class="o">:</span> <span class="n">α</span> <span class="bp">→</span> <span class="n">β</span> <span class="bp">→</span> <span class="n">γ</span><span class="o">)</span> <span class="o">{</span><span class="n">x₁</span> <span class="n">x₂</span> <span class="o">:</span> <span class="n">α</span><span class="o">}</span> <span class="o">{</span><span class="n">y₁</span> <span class="n">y₂</span> <span class="o">:</span> <span class="n">β</span><span class="o">}</span>
  <span class="o">(</span><span class="n">Hx</span> <span class="o">:</span> <span class="n">x₁</span> <span class="bp">=</span> <span class="n">x₂</span><span class="o">)</span> <span class="o">(</span><span class="n">Hy</span> <span class="o">:</span> <span class="n">y₁</span> <span class="bp">=</span> <span class="n">y₂</span><span class="o">)</span> <span class="o">:</span> <span class="n">f</span> <span class="n">x₁</span> <span class="n">y₁</span> <span class="bp">=</span> <span class="n">f</span> <span class="n">x₂</span> <span class="n">y₂</span> <span class="o">:=</span>
<span class="n">eq</span><span class="bp">.</span><span class="n">drec</span> <span class="o">(</span><span class="n">eq</span><span class="bp">.</span><span class="n">drec</span> <span class="n">rfl</span> <span class="n">Hy</span><span class="o">)</span> <span class="n">Hx</span>

<span class="kn">lemma</span> <span class="n">add_eq</span> <span class="o">{</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span><span class="bp">*</span><span class="o">}</span> <span class="o">[</span><span class="n">has_add</span> <span class="n">α</span><span class="o">]</span> <span class="o">{</span><span class="n">b</span> <span class="n">c</span> <span class="n">d</span> <span class="n">e</span> <span class="o">:</span> <span class="n">α</span><span class="o">}</span> <span class="o">(</span><span class="n">H</span> <span class="o">:</span> <span class="n">b</span> <span class="bp">=</span> <span class="n">c</span><span class="o">)</span> <span class="o">(</span><span class="n">H&#39;</span> <span class="o">:</span> <span class="n">d</span> <span class="bp">=</span> <span class="n">e</span><span class="o">)</span> <span class="o">:</span>
  <span class="n">b</span> <span class="bp">+</span> <span class="n">d</span> <span class="bp">=</span> <span class="n">c</span> <span class="bp">+</span> <span class="n">e</span> <span class="o">:=</span> <span class="n">congr_arg₂</span> <span class="n">has_add</span><span class="bp">.</span><span class="n">add</span> <span class="n">H</span> <span class="n">H&#39;</span>
</pre></div>


<p>and then Mario wins:</p>
<div class="codehilite"><pre><span></span><span class="kn">lemma</span> <span class="n">add_eq</span> <span class="o">{</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span><span class="bp">*</span><span class="o">}</span> <span class="o">[</span><span class="n">has_add</span> <span class="n">α</span><span class="o">]</span> <span class="o">{</span><span class="n">b</span> <span class="n">c</span> <span class="n">d</span> <span class="n">e</span> <span class="o">:</span> <span class="n">α</span><span class="o">}</span> <span class="o">(</span><span class="n">H</span> <span class="o">:</span> <span class="n">b</span> <span class="bp">=</span> <span class="n">c</span><span class="o">)</span> <span class="o">(</span><span class="n">H&#39;</span> <span class="o">:</span> <span class="n">d</span> <span class="bp">=</span> <span class="n">e</span><span class="o">)</span> <span class="o">:</span>
  <span class="n">b</span> <span class="bp">+</span> <span class="n">d</span> <span class="bp">=</span> <span class="n">c</span> <span class="bp">+</span> <span class="n">e</span> <span class="o">:=</span> <span class="k">by</span> <span class="n">congr&#39;</span>
</pre></div>

#### [ Patrick Massot (Nov 24 2018 at 00:17)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Missing%20maths%20tactic%3F/near/148253565):
<p>I still think all versions deserve to be in mathlib: <code>congr_arg₂</code> and <code>add_eq</code> with its one-word proof</p>

#### [ Patrick Massot (Nov 24 2018 at 00:17)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Missing%20maths%20tactic%3F/near/148253595):
<p>And now, I really go to sleep</p>

#### [ Kenny Lau (Nov 24 2018 at 01:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Missing%20maths%20tactic%3F/near/148256302):
<p>man these 10 lines took me 1.5 hours to write:</p>
<div class="codehilite"><pre><span></span><span class="kn">import</span> <span class="n">tactic</span><span class="bp">.</span><span class="n">ring</span>

<span class="kn">namespace</span> <span class="n">tactic</span><span class="bp">.</span><span class="n">interactive</span>
<span class="kn">open</span> <span class="n">lean</span><span class="bp">.</span><span class="n">parser</span> <span class="n">tactic</span> <span class="n">interactive</span>
<span class="n">meta</span> <span class="n">def</span> <span class="n">add_eq</span> <span class="o">(</span><span class="n">h1</span> <span class="o">:</span> <span class="n">parse</span> <span class="n">ident</span><span class="o">)</span> <span class="o">(</span><span class="n">h2</span> <span class="o">:</span> <span class="n">parse</span> <span class="n">ident</span><span class="o">)</span>
  <span class="o">(</span><span class="n">h</span> <span class="o">:</span> <span class="n">parse</span> <span class="o">(</span><span class="n">optional</span> <span class="o">(</span><span class="n">tk</span> <span class="s2">&quot;with&quot;</span> <span class="bp">*&gt;</span> <span class="n">ident</span><span class="o">)))</span> <span class="o">:</span> <span class="n">tactic</span> <span class="n">unit</span> <span class="o">:=</span>
<span class="n">do</span>
<span class="n">e1</span> <span class="err">←</span> <span class="n">get_local</span> <span class="n">h1</span><span class="o">,</span> <span class="n">e2</span> <span class="err">←</span> <span class="n">get_local</span> <span class="n">h2</span><span class="o">,</span>
<span class="n">e</span> <span class="err">←</span> <span class="n">to_expr</span> <span class="bp">```</span><span class="o">(</span><span class="bp">_</span><span class="n">root_</span><span class="bp">.</span><span class="n">congr</span> <span class="o">(</span><span class="n">congr_arg</span> <span class="n">has_add</span><span class="bp">.</span><span class="n">add</span> <span class="err">%%</span><span class="n">e1</span><span class="o">)</span> <span class="err">%%</span><span class="n">e2</span><span class="o">),</span>
<span class="n">tactic</span><span class="bp">.</span><span class="n">note</span> <span class="o">(</span><span class="n">h</span><span class="bp">.</span><span class="n">get_or_else</span> <span class="bp">`</span><span class="n">this</span><span class="o">)</span> <span class="n">none</span> <span class="n">e</span>
<span class="bp">&gt;&gt;</span> <span class="n">skip</span>
<span class="kn">end</span> <span class="n">tactic</span><span class="bp">.</span><span class="n">interactive</span>

<span class="kn">example</span> <span class="o">(</span><span class="n">m</span> <span class="n">a</span> <span class="n">b</span> <span class="n">c</span> <span class="n">j</span> <span class="n">k</span> <span class="o">:</span> <span class="bp">ℤ</span><span class="o">)</span> <span class="o">(</span><span class="n">Hj</span> <span class="o">:</span> <span class="n">a</span> <span class="bp">-</span> <span class="n">b</span> <span class="bp">=</span> <span class="n">m</span> <span class="bp">*</span> <span class="n">j</span><span class="o">)</span> <span class="o">(</span><span class="n">Hk</span> <span class="o">:</span> <span class="n">b</span> <span class="bp">-</span> <span class="n">c</span> <span class="bp">=</span> <span class="n">m</span> <span class="bp">*</span> <span class="n">k</span><span class="o">)</span> <span class="o">:</span>
  <span class="n">a</span> <span class="bp">-</span> <span class="n">c</span> <span class="bp">=</span> <span class="n">m</span> <span class="bp">*</span> <span class="o">(</span><span class="n">j</span> <span class="bp">+</span> <span class="n">k</span><span class="o">)</span> <span class="o">:=</span>
<span class="k">begin</span>
  <span class="n">add_eq</span> <span class="n">Hj</span> <span class="n">Hk</span><span class="o">,</span>
  <span class="n">ring</span> <span class="n">at</span> <span class="bp">*</span><span class="o">,</span>
  <span class="n">assumption</span>
<span class="kn">end</span>
</pre></div>

#### [ Kenny Lau (Nov 24 2018 at 01:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Missing%20maths%20tactic%3F/near/148256304):
<p><span class="user-mention" data-user-id="110038">@Kevin Buzzard</span> I wrote my first tactic just by browsing through core / mathlib</p>

#### [ Kenny Lau (Nov 24 2018 at 01:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Missing%20maths%20tactic%3F/near/148256360):
<p><span class="user-mention" data-user-id="110049">@Mario Carneiro</span> are you going to replace my 5-line tactic with 1 line now?</p>

#### [ Kenny Lau (Nov 24 2018 at 02:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Missing%20maths%20tactic%3F/near/148256569):
<p>golfed:</p>
<div class="codehilite"><pre><span></span><span class="kn">import</span> <span class="n">tactic</span><span class="bp">.</span><span class="n">ring</span>

<span class="kn">namespace</span> <span class="n">tactic</span><span class="bp">.</span><span class="n">interactive</span>
<span class="kn">open</span> <span class="n">lean</span><span class="bp">.</span><span class="n">parser</span> <span class="n">tactic</span> <span class="n">interactive</span>
<span class="n">meta</span> <span class="n">def</span> <span class="n">add_eq</span> <span class="o">(</span><span class="n">h1</span> <span class="o">:</span> <span class="n">parse</span> <span class="n">ident</span><span class="o">)</span> <span class="o">(</span><span class="n">h2</span> <span class="o">:</span> <span class="n">parse</span> <span class="n">ident</span><span class="o">)</span>
  <span class="o">(</span><span class="n">h</span> <span class="o">:</span> <span class="n">parse</span> <span class="o">(</span><span class="n">optional</span> <span class="o">(</span><span class="n">tk</span> <span class="s2">&quot;with&quot;</span> <span class="bp">*&gt;</span> <span class="n">ident</span><span class="o">)))</span> <span class="o">:</span> <span class="n">tactic</span> <span class="n">unit</span> <span class="o">:=</span>
<span class="n">do</span> <span class="n">e1</span> <span class="err">←</span> <span class="n">get_local</span> <span class="n">h1</span><span class="o">,</span> <span class="n">e2</span> <span class="err">←</span> <span class="n">get_local</span> <span class="n">h2</span><span class="o">,</span>
   <span class="err">«</span><span class="k">have</span><span class="err">»</span> <span class="n">h</span> <span class="n">none</span> <span class="bp">```</span><span class="o">(</span><span class="bp">_</span><span class="n">root_</span><span class="bp">.</span><span class="n">congr</span> <span class="o">(</span><span class="n">congr_arg</span> <span class="n">has_add</span><span class="bp">.</span><span class="n">add</span> <span class="err">%%</span><span class="n">e1</span><span class="o">)</span> <span class="err">%%</span><span class="n">e2</span><span class="o">)</span>
<span class="kn">end</span> <span class="n">tactic</span><span class="bp">.</span><span class="n">interactive</span>

<span class="kn">example</span> <span class="o">(</span><span class="n">m</span> <span class="n">a</span> <span class="n">b</span> <span class="n">c</span> <span class="n">j</span> <span class="n">k</span> <span class="o">:</span> <span class="bp">ℤ</span><span class="o">)</span> <span class="o">(</span><span class="n">Hj</span> <span class="o">:</span> <span class="n">a</span> <span class="bp">-</span> <span class="n">b</span> <span class="bp">=</span> <span class="n">m</span> <span class="bp">*</span> <span class="n">j</span><span class="o">)</span> <span class="o">(</span><span class="n">Hk</span> <span class="o">:</span> <span class="n">b</span> <span class="bp">-</span> <span class="n">c</span> <span class="bp">=</span> <span class="n">m</span> <span class="bp">*</span> <span class="n">k</span><span class="o">)</span> <span class="o">:</span>
  <span class="n">a</span> <span class="bp">-</span> <span class="n">c</span> <span class="bp">=</span> <span class="n">m</span> <span class="bp">*</span> <span class="o">(</span><span class="n">j</span> <span class="bp">+</span> <span class="n">k</span><span class="o">)</span> <span class="o">:=</span>
<span class="k">begin</span>
  <span class="n">add_eq</span> <span class="n">Hj</span> <span class="n">Hk</span><span class="o">,</span>
  <span class="n">ring</span> <span class="n">at</span> <span class="bp">*</span><span class="o">,</span>
  <span class="n">assumption</span>
<span class="kn">end</span>
</pre></div>

#### [ Scott Morrison (Nov 24 2018 at 02:20)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Missing%20maths%20tactic%3F/near/148256983):
<p><span class="user-mention" data-user-id="110064">@Kenny Lau</span>, why not reuse the lemma, and save yourself constructing the expression by hand:</p>
<div class="codehilite"><pre><span></span>import tactic.ring

lemma add_eq {α : Type*} [has_add α] {b c d e : α} (H : b = c) (H&#39; : d = e) :
  b + d = c + e := by congr&#39;

namespace tactic.interactive
open lean.parser tactic interactive
meta def add_eq (h1 : parse ident) (h2 : parse ident)
  (h : parse (optional (tk &quot;with&quot; *&gt; ident))) : tactic unit :=
do e1 ← get_local h1,
   e2 ← get_local h2,
   «have» h none ```(add_eq %%e1 %%e2)
end tactic.interactive

example (m a b c j k : ℤ) (Hj : a - b = m * j) (Hk : b - c = m * k) :
  a - c = m * (j + k) :=
begin
  add_eq Hj Hk,
  ring at *,
  assumption
end
</pre></div>

#### [ Kenny Lau (Nov 24 2018 at 02:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Missing%20maths%20tactic%3F/near/148256990):
<p>fair enough</p>

#### [ Scott Morrison (Nov 24 2018 at 02:23)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Missing%20maths%20tactic%3F/near/148257035):
<p>Quotations are your friend, both for constructing <code>expr</code> instances and pattern matching on them.</p>

#### [ Johan Commelin (Nov 24 2018 at 07:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Missing%20maths%20tactic%3F/near/148265264):
<p>Doesn't this mean that we should provide <code>instance {A : Type*} [has_add A] : has_add (eq A)</code>? And then prove that it is associative and commutative in the appropriate cases...</p>

#### [ Johan Commelin (Nov 24 2018 at 07:29)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Missing%20maths%20tactic%3F/near/148265271):
<p><span class="user-mention" data-user-id="110049">@Mario Carneiro</span> Is it possible to do <code>ring at * using [foo,bar]</code>?</p>

#### [ Kevin Buzzard (Nov 24 2018 at 08:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Missing%20maths%20tactic%3F/near/148267312):
<p>This sounds unlikely as it sounds like you're asking Lean to figure out if an element of a ring is in the ideal generated by the inputs, which is surely well beyond the ring tactic</p>

#### [ Mario Carneiro (Nov 24 2018 at 09:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Missing%20maths%20tactic%3F/near/148268834):
<p>Right. As you have identified this needs groebner bases, which could be a future generalization of <code>ring</code> but is a completely different algorithm</p>

#### [ Mario Carneiro (Nov 24 2018 at 09:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Missing%20maths%20tactic%3F/near/148268884):
<p><span class="user-mention" data-user-id="110064">@Kenny Lau</span> , be careful golfing tactic code. Because we don't have the same assurances on correctness of meta code, it's much more like conventional programming, and it is important to be clear rather than compact, for maintainability</p>

#### [ Rob Lewis (Nov 24 2018 at 11:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Missing%20maths%20tactic%3F/near/148271134):
<p>FYI, a student of ours who just started his BS thesis project is interested in Grobner basis algorithms. I'm not sure exactly which direction his project will go. Hopefully we'll get the core of an algorithm for this kind of thing, and then either he or we will turn it into a tactic.</p>

#### [ Johan Commelin (Nov 24 2018 at 16:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Missing%20maths%20tactic%3F/near/148280564):
<p>Wouldn't it be faster (both  development, and user experience) to piggyback on some other CAS? You already have the Mathematica interface. I guess a pari or sage interface would also be helpful. And we would get grobner basis tactics "for free"...</p>

#### [ Kevin Buzzard (Nov 24 2018 at 16:26)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Missing%20maths%20tactic%3F/near/148281161):
<p>Oh! It's just like the matrix inverse isn't it! You ask magma or whatever for a proof that the element is in the ideal, it supplies an explicit linear combination claiming to prove this but which hasn't been formally verified, and then you formally verify it in Lean with the <code>ring</code> tactic.</p>

#### [ Rob Lewis (Nov 24 2018 at 16:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Missing%20maths%20tactic%3F/near/148281219):
<p>Sure, but there are upsides to implementing the algorithm natively too. Our student will learn how it works, of course. And it would be portable, so the tactic would be usable in mathlib without external dependencies. There's also theoretical interest in implementing the algorithm in non-meta Lean and proving it correct, even if it can't be efficiently executed in the kernel. And any tactic built on this should be modular enough to use an external oracle too.</p>

#### [ Johan Commelin (Nov 24 2018 at 18:14)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Missing%20maths%20tactic%3F/near/148284554):
<p>By the way, I think my question about <code>ring using [foo,bar]</code> was misunderstood. I didn't want it to find relations on its own. I wanted to be able to type something like</p>
<div class="codehilite"><pre><span></span><span class="n">ring</span> <span class="kn">using</span> <span class="o">[</span><span class="n">add_eq</span> <span class="n">H1</span> <span class="n">H2</span><span class="o">]</span>
</pre></div>

#### [ Johan Commelin (Nov 24 2018 at 18:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Missing%20maths%20tactic%3F/near/148284566):
<p>And using notation, that might be improved to <code>ring using [H1 + H2]</code></p>

#### [ Mario Carneiro (Nov 25 2018 at 01:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Missing%20maths%20tactic%3F/near/148296295):
<p>that seems more reasonable. You give some linear combination of hypotheses, like <code>a * h1 + x^2 * h2</code>, and it checks that <code>goal - (a*h1 + x^2 * h2)</code> is an equality of ring expressions</p>


{% endraw %}
