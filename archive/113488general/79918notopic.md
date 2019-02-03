---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/79918notopic.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [(no topic)](https://leanprover-community.github.io/archive/113488general/79918notopic.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Kevin Buzzard (Feb 26 2018 at 19:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%28no%20topic%29/near/123008190):
<p>So general chatter goes in "archives" topic?</p>

#### [ Kevin Buzzard (Feb 26 2018 at 19:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%28no%20topic%29/near/123008198):
<p>oh no I have made (no topic). Do I have to have a topic?</p>

#### [ Andrew Ashworth (Feb 26 2018 at 19:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%28no%20topic%29/near/123008201):
<p>no topic necessary for off-topic conversation</p>

#### [ Kevin Buzzard (Feb 26 2018 at 19:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%28no%20topic%29/near/123008205):
<p>I don't understand how to have off-topic conversation</p>

#### [ Kevin Buzzard (Feb 27 2018 at 09:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%28no%20topic%29/near/123033113):
<p>Chris has already observed that mathematicians frequently want to sum from 0 to n, or 1 to n, and have a bunch of basic facts about such sums available to them. I know there are finsets and fintypes or whatever, but this case of summing from 0 to n or 1 to n is such a common usage case in maths. Is there already a specialised type for dealing specifically with such sums, which is easier to handle than dealing with general finsets? I am thinking about teaching induction to mathematicians without having to fill their heads with what I would call "specialised types" such as finset.</p>

#### [ Kevin Buzzard (Feb 27 2018 at 09:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%28no%20topic%29/near/123033117):
<p>If not I might be tempted to build such things myself but I don't want to reinvent the wheel.</p>

#### [ Simon Hudon (Feb 27 2018 at 09:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%28no%20topic%29/near/123033165):
<p>I was faced with a similar situation last year. The formulation of <code>sum</code> I find is less than conducive to reasoning. I'm not sure if my lemmas about <code>foldl</code> and <code>foldr</code> are still around (I think they are now in mathlib) but your best bet I think is to prove <code>sum (xs ++ ys) = sum xs + sum ys</code>. That should get you started at least</p>

#### [ Mario Carneiro (Feb 27 2018 at 09:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%28no%20topic%29/near/123033218):
<p>DId you try <code>by simp</code>? I think this is the consequence of several lemmas</p>

#### [ Mario Carneiro (Feb 27 2018 at 09:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%28no%20topic%29/near/123033225):
<p>But I'm also working on a definition of sums over natural numbers to make this sort of thing easier</p>

#### [ Kevin Buzzard (Feb 27 2018 at 09:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%28no%20topic%29/near/123033478):
<p>I didn't try simp because I was writing teaching materials and for some reason I wanted to be "explicit" about what was happening -- e.g. "this lemma with this name shows the fundamental fact which we will need, namely that the sum to n+1 is related to the sum to n in this obvious way". There is a danger with the sort of stuff I was doing that simp would just clear the goal completely and I know I can target it with (have blah, by simp) or whatever, but my goal was not to prove the lemma, it was to show math undergraduates how to use induction in Lean without any extra bells and whistles.</p>

#### [ Kevin Buzzard (Feb 27 2018 at 09:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%28no%20topic%29/near/123033519):
<p>I suspect that in general as my thoughts about teaching progress I will want access to lemmas with possibly names that Mario disapproves of and which state things which he does not want in mathlib (e.g. because they can be done with a fold in one line or some such thing). Things like folds are what I am trying to avoid currently because I do not want to teach them any functional programming.</p>

#### [ Kevin Buzzard (Feb 27 2018 at 09:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%28no%20topic%29/near/123033527):
<p>You CS guys might think this is mad, but look at Chris Hughes -- he showed up knowing a bit of matlab and had no idea what a functional program was, and I got him doing mathematics in Lean very quickly because of tactic mode. The more tactics / lemmas there are, the more mathematicians are able to stay away from the whole functional thing, and they can just get into it later when it all begins to make more sense.</p>

#### [ Sean Leather (Feb 27 2018 at 09:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%28no%20topic%29/near/123033576):
<p><span class="user-mention" data-user-email="k.buzzard@imperial.ac.uk" data-user-id="110038">@Kevin Buzzard</span> Not mad at all. Tactics are great for incrementally proving theorems.</p>

#### [ Simon Hudon (Feb 27 2018 at 09:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%28no%20topic%29/near/123033577):
<p>I think that will limit how much you can do but there must still be interesting fragments</p>

#### [ Sean Leather (Feb 27 2018 at 09:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%28no%20topic%29/near/123033619):
<p>... and this is coming from a CS guy, though, again, I'm not sure why that matters. <span class="emoji emoji-1f609" title="wink">:wink:</span></p>

#### [ Kevin Buzzard (Feb 27 2018 at 09:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%28no%20topic%29/near/123033630):
<p>I think that you can get through a whole bunch of my introduction to proof course in Lean without really knowing too much about functional programming. I've seen it happen.</p>

#### [ Kevin Buzzard (Feb 27 2018 at 09:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%28no%20topic%29/near/123033635):
<p>My job is not to teach functional programming, it is to teach rigorous thinking.</p>

#### [ Simon Hudon (Feb 27 2018 at 09:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%28no%20topic%29/near/123033666):
<p>I think functional programming is especially hard to avoid as you're scaling up your proof efforts which often doesn't really come up in introductions</p>

#### [ Sean Leather (Feb 27 2018 at 09:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%28no%20topic%29/near/123033679):
<p><span class="user-mention" data-user-email="k.buzzard@imperial.ac.uk" data-user-id="110038">@Kevin Buzzard</span>  I'm sure you're right. Why do you feel the need to defend that idea?</p>

#### [ Mario Carneiro (Feb 27 2018 at 09:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%28no%20topic%29/near/123033683):
<p>If that's the kind of teaching you are going for, I recommend giving a direct inductive definition like it is done in TPIL</p>

#### [ Kevin Buzzard (Feb 27 2018 at 09:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%28no%20topic%29/near/123033685):
<p>I would be interested to hear <span class="user-mention" data-user-email="chrishughes24@gmail.com" data-user-id="110044">@Chris Hughes</span> 's take on the issue. I am not sure he knows what a fold is but he has proved the fundamental theorem of arithmetic and much more in Lean.</p>

#### [ Mario Carneiro (Feb 27 2018 at 09:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%28no%20topic%29/near/123033691):
<p>then you can give all the natural lemmas and prove basic properties and there is no hidden magic</p>

#### [ Chris Hughes (Feb 27 2018 at 14:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%28no%20topic%29/near/123042606):
<p>I totally agree that tactics is the way to teach lean to maths students. I proved the fundamental theorem of arithmetic without even knowing what lambda did, and this gave me enough proficiency very quickly, that I've probably learnt a fair amount about functional programming, whatever that is, without really thinking about trying to learn functional programming.</p>

#### [ Kevin Buzzard (Feb 27 2018 at 23:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%28no%20topic%29/near/123061458):
<p>Hey Patrick did you make an arbitrary product of rings a ring recently?</p>

#### [ Kevin Buzzard (Feb 27 2018 at 23:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%28no%20topic%29/near/123061860):
<p><span class="user-mention" data-user-email="patrickmassot@free.fr" data-user-id="110031">@Patrick Massot</span> I need that now! But it's in gitter chat and it'll be hard to find :-/</p>

#### [ Kevin Buzzard (Feb 27 2018 at 23:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%28no%20topic%29/near/123061930):
<p>Aah I've found it by looking through your github repos until I found the right commit :-)</p>

#### [ Patrick Massot (Feb 28 2018 at 01:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%28no%20topic%29/near/123066299):
<p>Yes: <a href="https://github.com/PatrickMassot/lean-differential-topology/blob/master/src/indexed_product.lean" target="_blank" title="https://github.com/PatrickMassot/lean-differential-topology/blob/master/src/indexed_product.lean">https://github.com/PatrickMassot/lean-differential-topology/blob/master/src/indexed_product.lean</a> I will make a PR at some point</p>

#### [ Kevin Buzzard (May 01 2018 at 22:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%28no%20topic%29/near/125960052):
<p><a href="/user_uploads/3121/AwppWERsWgYQlkaoTxtLAKL-/pic1.png" target="_blank" title="pic1.png">pic1.png</a></p>
<div class="message_inline_image"><a href="/user_uploads/3121/AwppWERsWgYQlkaoTxtLAKL-/pic1.png" target="_blank" title="pic1.png"><img src="/user_uploads/3121/AwppWERsWgYQlkaoTxtLAKL-/pic1.png"></a></div>

#### [ Kevin Buzzard (May 01 2018 at 22:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%28no%20topic%29/near/125960056):
<p>he made that</p>

#### [ Kevin Buzzard (May 01 2018 at 22:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%28no%20topic%29/near/125960075):
<p>it's the syntax tree for my proof that sqrt(3) is irrational</p>

#### [ Kevin Buzzard (May 01 2018 at 22:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%28no%20topic%29/near/125960087):
<p>it's like <code>set_option pp.all</code></p>

#### [ Kevin Buzzard (May 01 2018 at 22:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%28no%20topic%29/near/125960160):
<p>In fact we made it from the output of <code>set_option pp.all</code> and some emacs trickery and some python code</p>

#### [ Kevin Buzzard (May 01 2018 at 22:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%28no%20topic%29/near/125960168):
<p>and then he made that in blender</p>

#### [ Kevin Buzzard (May 01 2018 at 22:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%28no%20topic%29/near/125960195):
<p>red dots are functions, blue are evaluated terms</p>

#### [ Chris Hughes (May 01 2018 at 22:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%28no%20topic%29/near/125960445):
<p>I proved it for non integer nth roots of integers.</p>
<div class="codehilite"><pre><span></span><span class="kn">import</span> <span class="n">data</span><span class="bp">.</span><span class="n">nat</span><span class="bp">.</span><span class="n">gcd</span> <span class="n">algebra</span><span class="bp">.</span><span class="n">group_power</span> <span class="n">data</span><span class="bp">.</span><span class="n">rat</span>

<span class="kn">open</span> <span class="n">nat</span> <span class="n">int</span>
<span class="kn">lemma</span> <span class="n">nat</span><span class="bp">.</span><span class="n">mul_pow</span> <span class="o">(</span><span class="n">a</span> <span class="n">b</span> <span class="n">n</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">)</span> <span class="o">:</span> <span class="o">(</span><span class="n">a</span> <span class="bp">*</span> <span class="n">b</span><span class="o">)</span> <span class="err">^</span> <span class="n">n</span> <span class="bp">=</span> <span class="n">a</span> <span class="err">^</span> <span class="n">n</span> <span class="bp">*</span> <span class="n">b</span> <span class="err">^</span> <span class="n">n</span> <span class="o">:=</span>
<span class="k">by</span> <span class="n">induction</span> <span class="n">n</span><span class="bp">;</span> <span class="n">simp</span> <span class="o">[</span><span class="bp">*</span><span class="o">,</span> <span class="n">nat</span><span class="bp">.</span><span class="n">pow_succ</span><span class="o">,</span> <span class="n">mul_comm</span><span class="o">,</span> <span class="n">mul_assoc</span><span class="o">,</span> <span class="n">mul_left_comm</span><span class="o">]</span>

<span class="kn">lemma</span> <span class="n">nat</span><span class="bp">.</span><span class="n">dvd_of_pow_dvd_pow</span> <span class="o">:</span> <span class="bp">∀</span> <span class="o">{</span><span class="n">a</span> <span class="n">b</span> <span class="n">n</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">},</span> <span class="mi">0</span> <span class="bp">&lt;</span> <span class="n">n</span> <span class="bp">→</span> <span class="n">a</span> <span class="err">^</span> <span class="n">n</span> <span class="err">∣</span> <span class="n">b</span> <span class="err">^</span> <span class="n">n</span> <span class="bp">→</span> <span class="n">a</span> <span class="err">∣</span> <span class="n">b</span>
<span class="bp">|</span> <span class="n">a</span> <span class="mi">0</span>     <span class="o">:=</span> <span class="bp">λ</span> <span class="n">n</span> <span class="n">hn</span> <span class="n">h</span><span class="o">,</span> <span class="n">dvd_zero</span> <span class="bp">_</span>
<span class="bp">|</span> <span class="n">a</span> <span class="o">(</span><span class="n">b</span><span class="bp">+</span><span class="mi">1</span><span class="o">)</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">n</span> <span class="n">hn</span> <span class="n">h</span><span class="o">,</span>
<span class="k">let</span> <span class="n">d</span> <span class="o">:=</span> <span class="n">nat</span><span class="bp">.</span><span class="n">gcd</span> <span class="n">a</span> <span class="o">(</span><span class="n">b</span> <span class="bp">+</span> <span class="mi">1</span><span class="o">)</span> <span class="k">in</span>
<span class="k">have</span> <span class="n">hd</span> <span class="o">:</span> <span class="n">nat</span><span class="bp">.</span><span class="n">gcd</span> <span class="n">a</span> <span class="o">(</span><span class="n">b</span> <span class="bp">+</span> <span class="mi">1</span><span class="o">)</span> <span class="bp">=</span> <span class="n">d</span> <span class="o">:=</span> <span class="n">rfl</span><span class="o">,</span>
  <span class="k">match</span> <span class="n">d</span><span class="o">,</span> <span class="n">hd</span> <span class="k">with</span>
  <span class="bp">|</span> <span class="mi">0</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">hd</span><span class="o">,</span> <span class="o">(</span><span class="n">eq_zero_of_gcd_eq_zero_right</span> <span class="n">hd</span><span class="o">)</span><span class="bp">.</span><span class="n">symm</span> <span class="bp">▸</span> <span class="n">dvd_zero</span> <span class="bp">_</span>
  <span class="bp">|</span> <span class="mi">1</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">hd</span><span class="o">,</span>
    <span class="k">begin</span>
      <span class="k">have</span> <span class="n">h₁</span> <span class="o">:</span> <span class="n">a</span> <span class="err">^</span> <span class="n">n</span> <span class="bp">=</span> <span class="mi">1</span> <span class="o">:=</span> <span class="n">coprime</span><span class="bp">.</span><span class="n">eq_one_of_dvd</span> <span class="o">(</span><span class="n">coprime</span><span class="bp">.</span><span class="n">pow</span> <span class="n">n</span> <span class="n">n</span> <span class="n">hd</span><span class="o">)</span> <span class="n">h</span><span class="o">,</span>
      <span class="k">have</span> <span class="o">:=</span> <span class="n">pow_dvd_pow</span> <span class="n">a</span> <span class="n">hn</span><span class="o">,</span>
      <span class="n">rw</span> <span class="o">[</span><span class="n">nat</span><span class="bp">.</span><span class="n">pow_one</span><span class="o">,</span> <span class="n">h₁</span><span class="o">]</span> <span class="n">at</span> <span class="n">this</span><span class="o">,</span>
      <span class="n">exact</span> <span class="n">dvd</span><span class="bp">.</span><span class="n">trans</span> <span class="n">this</span> <span class="o">(</span><span class="n">one_dvd</span> <span class="bp">_</span><span class="o">),</span>
    <span class="kn">end</span>
  <span class="bp">|</span> <span class="o">(</span><span class="n">d</span><span class="bp">+</span><span class="mi">2</span><span class="o">)</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">hd</span><span class="o">,</span>
    <span class="k">have</span> <span class="o">(</span><span class="n">b</span><span class="bp">+</span><span class="mi">1</span><span class="o">)</span> <span class="bp">/</span> <span class="o">(</span><span class="n">d</span><span class="bp">+</span><span class="mi">2</span><span class="o">)</span> <span class="bp">&lt;</span> <span class="o">(</span><span class="n">b</span><span class="bp">+</span><span class="mi">1</span><span class="o">)</span> <span class="o">:=</span> <span class="n">div_lt_self</span> <span class="n">dec_trivial</span> <span class="n">dec_trivial</span><span class="o">,</span>
    <span class="k">have</span> <span class="n">ha</span> <span class="o">:</span> <span class="n">a</span> <span class="bp">=</span> <span class="o">(</span><span class="n">d</span><span class="bp">+</span><span class="mi">2</span><span class="o">)</span> <span class="bp">*</span> <span class="o">(</span><span class="n">a</span> <span class="bp">/</span> <span class="o">(</span><span class="n">d</span><span class="bp">+</span><span class="mi">2</span><span class="o">))</span> <span class="o">:=</span>
      <span class="k">by</span> <span class="n">rw</span> <span class="o">[</span><span class="err">←</span> <span class="n">hd</span><span class="o">,</span> <span class="n">nat</span><span class="bp">.</span><span class="n">mul_div_cancel&#39;</span> <span class="o">(</span><span class="n">gcd_dvd_left</span> <span class="bp">_</span> <span class="bp">_</span><span class="o">)],</span>
    <span class="k">have</span> <span class="n">hb</span> <span class="o">:</span> <span class="o">(</span><span class="n">b</span><span class="bp">+</span><span class="mi">1</span><span class="o">)</span> <span class="bp">=</span> <span class="o">(</span><span class="n">d</span><span class="bp">+</span><span class="mi">2</span><span class="o">)</span> <span class="bp">*</span> <span class="o">((</span><span class="n">b</span><span class="bp">+</span><span class="mi">1</span><span class="o">)</span> <span class="bp">/</span> <span class="o">(</span><span class="n">d</span><span class="bp">+</span><span class="mi">2</span><span class="o">))</span> <span class="o">:=</span>
      <span class="k">by</span> <span class="n">rw</span> <span class="o">[</span><span class="err">←</span> <span class="n">hd</span><span class="o">,</span> <span class="n">nat</span><span class="bp">.</span><span class="n">mul_div_cancel&#39;</span> <span class="o">(</span><span class="n">gcd_dvd_right</span> <span class="bp">_</span> <span class="bp">_</span><span class="o">)],</span>
    <span class="k">have</span> <span class="n">a</span> <span class="bp">/</span> <span class="o">(</span><span class="n">d</span><span class="bp">+</span><span class="mi">2</span><span class="o">)</span> <span class="err">∣</span> <span class="o">(</span><span class="n">b</span><span class="bp">+</span><span class="mi">1</span><span class="o">)</span> <span class="bp">/</span> <span class="o">(</span><span class="n">d</span><span class="bp">+</span><span class="mi">2</span><span class="o">)</span> <span class="o">:=</span> <span class="n">nat</span><span class="bp">.</span><span class="n">dvd_of_pow_dvd_pow</span> <span class="n">hn</span> <span class="err">$</span> <span class="n">dvd_of_mul_dvd_mul_left</span>
      <span class="o">(</span><span class="k">show</span> <span class="o">(</span><span class="n">d</span> <span class="bp">+</span> <span class="mi">2</span><span class="o">)</span> <span class="err">^</span> <span class="n">n</span> <span class="bp">&gt;</span> <span class="mi">0</span><span class="o">,</span> <span class="k">from</span> <span class="n">pos_pow_of_pos</span> <span class="bp">_</span> <span class="o">(</span><span class="n">dec_trivial</span><span class="o">))</span>
      <span class="o">(</span><span class="k">by</span> <span class="n">rwa</span> <span class="o">[</span><span class="err">←</span> <span class="n">nat</span><span class="bp">.</span><span class="n">mul_pow</span><span class="o">,</span> <span class="err">←</span> <span class="n">nat</span><span class="bp">.</span><span class="n">mul_pow</span><span class="o">,</span> <span class="err">←</span> <span class="n">ha</span><span class="o">,</span> <span class="err">←</span> <span class="n">hb</span><span class="o">]),</span>
    <span class="k">by</span> <span class="n">rw</span> <span class="o">[</span><span class="n">ha</span><span class="o">,</span> <span class="n">hb</span><span class="o">]</span><span class="bp">;</span>
      <span class="n">exact</span> <span class="n">mul_dvd_mul_left</span> <span class="bp">_</span> <span class="n">this</span>
  <span class="kn">end</span>
<span class="n">using_well_founded</span> <span class="o">{</span><span class="n">rel_tac</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="bp">_</span> <span class="bp">_</span><span class="o">,</span> <span class="bp">`</span><span class="o">[</span><span class="n">exact</span> <span class="bp">⟨_</span><span class="o">,</span> <span class="n">measure_wf</span> <span class="n">psigma</span><span class="bp">.</span><span class="n">snd</span><span class="bp">⟩</span><span class="o">]}</span>

<span class="kn">lemma</span> <span class="n">int</span><span class="bp">.</span><span class="n">nat_abs_pow</span> <span class="o">(</span><span class="n">a</span> <span class="o">:</span> <span class="bp">ℤ</span><span class="o">)</span> <span class="o">(</span><span class="n">n</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">)</span> <span class="o">:</span> <span class="n">a</span><span class="bp">.</span><span class="n">nat_abs</span> <span class="err">^</span> <span class="n">n</span> <span class="bp">=</span> <span class="o">(</span><span class="n">a</span> <span class="err">^</span> <span class="n">n</span><span class="o">)</span><span class="bp">.</span><span class="n">nat_abs</span> <span class="o">:=</span>
<span class="k">by</span> <span class="n">induction</span> <span class="n">n</span><span class="bp">;</span> <span class="n">simp</span> <span class="o">[</span><span class="bp">*</span><span class="o">,</span> <span class="n">nat</span><span class="bp">.</span><span class="n">pow_succ</span><span class="o">,</span> <span class="bp">_</span><span class="n">root_</span><span class="bp">.</span><span class="n">pow_succ</span><span class="o">,</span> <span class="n">nat_abs_mul</span><span class="o">,</span> <span class="n">mul_comm</span><span class="o">]</span>

<span class="kn">lemma</span> <span class="n">int</span><span class="bp">.</span><span class="n">dvd_of_pow_dvd_pow</span> <span class="o">{</span><span class="n">a</span> <span class="n">b</span> <span class="o">:</span> <span class="bp">ℤ</span><span class="o">}</span> <span class="o">{</span><span class="n">n</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">}</span> <span class="o">(</span><span class="n">hn</span> <span class="o">:</span> <span class="mi">0</span> <span class="bp">&lt;</span> <span class="n">n</span><span class="o">)</span> <span class="o">(</span><span class="n">h</span> <span class="o">:</span> <span class="n">a</span> <span class="err">^</span> <span class="n">n</span> <span class="err">∣</span> <span class="n">b</span> <span class="err">^</span> <span class="n">n</span><span class="o">)</span> <span class="o">:</span> <span class="n">a</span> <span class="err">∣</span> <span class="n">b</span> <span class="o">:=</span>
<span class="k">begin</span>
  <span class="n">rw</span> <span class="o">[</span><span class="err">←</span> <span class="n">nat_abs_dvd</span><span class="o">,</span> <span class="err">←</span> <span class="n">dvd_nat_abs</span><span class="o">,</span> <span class="err">←</span> <span class="n">int</span><span class="bp">.</span><span class="n">nat_abs_pow</span><span class="o">,</span> <span class="err">←</span> <span class="n">int</span><span class="bp">.</span><span class="n">nat_abs_pow</span><span class="o">,</span> <span class="n">int</span><span class="bp">.</span><span class="n">coe_nat_dvd</span><span class="o">]</span> <span class="n">at</span> <span class="n">h</span><span class="o">,</span>
  <span class="n">rw</span> <span class="o">[</span><span class="err">←</span> <span class="n">nat_abs_dvd</span><span class="o">,</span> <span class="err">←</span> <span class="n">dvd_nat_abs</span><span class="o">,</span> <span class="n">int</span><span class="bp">.</span><span class="n">coe_nat_dvd</span><span class="o">],</span>
  <span class="n">exact</span> <span class="n">nat</span><span class="bp">.</span><span class="n">dvd_of_pow_dvd_pow</span> <span class="n">hn</span> <span class="n">h</span>
<span class="kn">end</span>

<span class="kn">lemma</span> <span class="n">int</span><span class="bp">.</span><span class="n">cast_pow</span> <span class="o">{</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span><span class="bp">*</span><span class="o">}</span> <span class="o">[</span><span class="n">ring</span> <span class="n">α</span><span class="o">]</span> <span class="o">(</span><span class="n">a</span> <span class="o">:</span> <span class="bp">ℤ</span><span class="o">)</span> <span class="o">(</span><span class="n">n</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">)</span> <span class="o">:</span> <span class="o">((</span><span class="n">a</span> <span class="err">^</span> <span class="n">n</span> <span class="o">:</span> <span class="bp">ℤ</span><span class="o">)</span> <span class="o">:</span> <span class="n">α</span><span class="o">)</span> <span class="bp">=</span> <span class="o">(</span><span class="n">a</span> <span class="o">:</span> <span class="n">α</span><span class="o">)</span> <span class="err">^</span> <span class="n">n</span> <span class="o">:=</span>
<span class="k">by</span> <span class="n">induction</span> <span class="n">n</span><span class="bp">;</span> <span class="n">simp</span> <span class="o">[</span><span class="bp">*</span><span class="o">,</span> <span class="bp">_</span><span class="n">root_</span><span class="bp">.</span><span class="n">pow_succ</span><span class="o">]</span>

<span class="n">def</span> <span class="n">nth_root_irrational</span> <span class="o">{</span><span class="n">x</span> <span class="o">:</span> <span class="bp">ℤ</span><span class="o">}</span> <span class="o">{</span><span class="n">a</span> <span class="o">:</span> <span class="n">ℚ</span><span class="o">}</span> <span class="o">{</span><span class="n">n</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">}</span> <span class="o">(</span><span class="n">hn</span> <span class="o">:</span> <span class="mi">0</span> <span class="bp">&lt;</span> <span class="n">n</span><span class="o">)</span> <span class="o">(</span><span class="n">h</span> <span class="o">:</span> <span class="n">a</span> <span class="err">^</span> <span class="n">n</span> <span class="bp">=</span> <span class="n">x</span><span class="o">)</span> <span class="o">:</span> <span class="o">{</span><span class="n">a&#39;</span> <span class="o">:</span> <span class="bp">ℤ</span> <span class="bp">//</span> <span class="n">a</span> <span class="bp">=</span> <span class="n">a&#39;</span><span class="o">}</span> <span class="o">:=</span>
<span class="k">have</span> <span class="n">had</span> <span class="o">:</span> <span class="o">((</span><span class="n">a</span><span class="bp">.</span><span class="n">denom</span> <span class="o">:</span> <span class="bp">ℤ</span><span class="o">)</span> <span class="o">:</span> <span class="n">ℚ</span><span class="o">)</span> <span class="bp">≠</span> <span class="mi">0</span> <span class="o">:=</span> <span class="n">int</span><span class="bp">.</span><span class="n">cast_ne_zero</span><span class="bp">.</span><span class="mi">2</span> <span class="o">(</span><span class="n">ne_of_lt</span> <span class="o">(</span><span class="n">int</span><span class="bp">.</span><span class="n">coe_nat_lt</span><span class="bp">.</span><span class="mi">2</span> <span class="n">a</span><span class="bp">.</span><span class="mi">3</span><span class="o">))</span><span class="bp">.</span><span class="n">symm</span><span class="o">,</span>
<span class="bp">⟨</span><span class="n">a</span><span class="bp">.</span><span class="n">num</span><span class="o">,</span>
<span class="k">begin</span>
  <span class="n">rw</span> <span class="o">[</span><span class="n">rat</span><span class="bp">.</span><span class="n">num_denom</span> <span class="n">a</span><span class="o">,</span> <span class="n">rat</span><span class="bp">.</span><span class="n">mk_eq_div</span><span class="o">,</span> <span class="n">div_pow</span> <span class="bp">_</span> <span class="n">had</span><span class="o">,</span> <span class="n">div_eq_iff_mul_eq</span> <span class="o">(</span><span class="n">pow_ne_zero</span> <span class="bp">_</span> <span class="n">had</span><span class="o">),</span>
    <span class="err">←</span> <span class="n">int</span><span class="bp">.</span><span class="n">cast_pow</span><span class="o">,</span> <span class="err">←</span> <span class="n">int</span><span class="bp">.</span><span class="n">cast_mul</span><span class="o">,</span> <span class="err">←</span> <span class="n">int</span><span class="bp">.</span><span class="n">cast_pow</span><span class="o">,</span> <span class="n">int</span><span class="bp">.</span><span class="n">cast_inj</span><span class="o">]</span> <span class="n">at</span> <span class="n">h</span><span class="o">,</span>
  <span class="k">have</span> <span class="o">:=</span> <span class="n">int</span><span class="bp">.</span><span class="n">coe_nat_dvd</span><span class="bp">.</span><span class="mi">1</span> <span class="o">(</span><span class="n">dvd_nat_abs</span><span class="bp">.</span><span class="mi">2</span> <span class="o">(</span><span class="n">int</span><span class="bp">.</span><span class="n">dvd_of_pow_dvd_pow</span> <span class="n">hn</span> <span class="o">(</span><span class="n">dvd_of_mul_left_eq</span> <span class="bp">_</span> <span class="n">h</span><span class="o">))),</span>
  <span class="k">have</span> <span class="o">:=</span> <span class="n">coprime</span><span class="bp">.</span><span class="n">eq_one_of_dvd</span> <span class="n">a</span><span class="bp">.</span><span class="mi">4</span><span class="bp">.</span><span class="n">symm</span> <span class="n">this</span><span class="o">,</span>
  <span class="n">rw</span> <span class="o">[</span><span class="n">rat</span><span class="bp">.</span><span class="n">num_denom</span> <span class="n">a</span><span class="o">,</span> <span class="n">rat</span><span class="bp">.</span><span class="n">mk_eq_div</span><span class="o">,</span> <span class="n">this</span><span class="o">],</span>
  <span class="n">simp</span><span class="o">,</span>
<span class="kn">end</span><span class="bp">⟩</span>
</pre></div>

#### [ Kenny Lau (May 01 2018 at 22:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%28no%20topic%29/near/125960579):
<div class="codehilite"><pre><span></span><span class="n">def</span> <span class="n">nth_root_irrational</span> <span class="o">{</span><span class="n">x</span> <span class="o">:</span> <span class="bp">ℤ</span><span class="o">}</span> <span class="o">{</span><span class="n">a</span> <span class="o">:</span> <span class="n">ℚ</span><span class="o">}</span> <span class="o">{</span><span class="n">n</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">}</span> <span class="o">(</span><span class="n">hn</span> <span class="o">:</span> <span class="mi">0</span> <span class="bp">&lt;</span> <span class="n">n</span><span class="o">)</span> <span class="o">(</span><span class="n">h</span> <span class="o">:</span> <span class="n">a</span> <span class="err">^</span> <span class="n">n</span> <span class="bp">=</span> <span class="n">x</span><span class="o">)</span> <span class="o">:</span> <span class="o">{</span><span class="n">a&#39;</span> <span class="o">:</span> <span class="bp">ℤ</span> <span class="bp">//</span> <span class="n">a</span> <span class="bp">=</span> <span class="n">a&#39;</span><span class="o">}</span> <span class="o">:=</span>
</pre></div>

#### [ Kenny Lau (May 01 2018 at 22:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%28no%20topic%29/near/125960583):
<p>yay you made it constructive :D</p>

#### [ Kenny Lau (May 01 2018 at 22:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%28no%20topic%29/near/125960586):
<blockquote>
<p>he made that</p>
</blockquote>
<p>who?</p>

#### [ Simon Hudon (May 01 2018 at 22:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%28no%20topic%29/near/125960829):
<p>His son I believe</p>

#### [ Kenny Lau (May 01 2018 at 22:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%28no%20topic%29/near/125960845):
<p>oh</p>

#### [ Mario Carneiro (May 02 2018 at 11:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%28no%20topic%29/near/125984628):
<blockquote>
<p>yay you made it constructive :D</p>
</blockquote>
<p>Actually, it makes no difference since if a rational number is an integer, then you can obtain its value using <code>rat.num</code>, or <code>rat.floor</code></p>

#### [ Mario Carneiro (May 02 2018 at 11:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%28no%20topic%29/near/125984672):
<p>(which is to say, that theorem would still be constructive with <code>exists</code>)</p>

#### [ gary (Jul 25 2018 at 22:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%28no%20topic%29/near/130300533):
<p>Hi all,</p>
<p>I'm working on applying formal methods to cryptocurrency protocols. We're a well funded startup (recently raised $20 million) and pay competetively. </p>
<p>If anyone has interest, please message me.</p>
<p>Thanks!</p>

#### [ Jason Dagit (Aug 16 2018 at 18:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%28no%20topic%29/near/132250941):
<p>I have an expression that uses a type class instance. Is there a command to that prints out which instance was inferred?</p>

#### [ Simon Hudon (Aug 16 2018 at 18:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%28no%20topic%29/near/132250998):
<p>Before the code printing the expression, use <code>set_option pp.implicit true</code> so that the pretty printer shows more parts of your expression, namely, implicit parameters (which include class instances)</p>

#### [ Jason Dagit (Aug 16 2018 at 18:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%28no%20topic%29/near/132251070):
<p>Thanks</p>

#### [ Keeley Hoek (Aug 18 2018 at 13:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%28no%20topic%29/near/132357521):
<p>(deleted)</p>

#### [ Nicholas Scheel (Dec 16 2018 at 05:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%28no%20topic%29/near/151864889):
<p>(deleted)</p>

#### [ Namdak Tonpa (Jan 07 2019 at 17:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%28no%20topic%29/near/154581476):
<p>I know I'm flooding, but here is IRC bot written in pure Lean 3.4.1 (someone asked me in lounge)<br>
<a href="https://github.com/forked-from-1kasper/leanbot" target="_blank" title="https://github.com/forked-from-1kasper/leanbot">https://github.com/forked-from-1kasper/leanbot</a><br>
Can't wait to write WebSocket binary protocol for Lean4!</p>

#### [ Moses Schönfinkel (Jan 07 2019 at 18:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%28no%20topic%29/near/154584968):
<p>This is the kind of flooding that is appreciated. By all means do continue to flood.</p>


{% endraw %}
