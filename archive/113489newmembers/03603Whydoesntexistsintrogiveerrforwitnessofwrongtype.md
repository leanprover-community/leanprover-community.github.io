---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113489newmembers/03603Whydoesntexistsintrogiveerrforwitnessofwrongtype.html
---

## Stream: [new members](https://leanprover-community.github.io/archive/113489newmembers/index.html)
### Topic: [Why doesn't exists.intro give err for witness of wrong type](https://leanprover-community.github.io/archive/113489newmembers/03603Whydoesntexistsintrogiveerrforwitnessofwrongtype.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Kevin Sullivan (Oct 19 2018 at 16:31)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Why%20doesn%27t%20exists.intro%20give%20err%20for%20witness%20of%20wrong%20type/near/136115096):
<p>Here's a proof that 7 is even. Why does exists.intro accept 3.5 as an argument, given that m is declared to be of type nat?</p>
<div class="codehilite"><pre><span></span><span class="n">def</span> <span class="n">isEven</span> <span class="o">(</span><span class="n">n</span><span class="o">:</span> <span class="bp">ℕ</span><span class="o">)</span> <span class="o">:</span> <span class="kt">Prop</span> <span class="o">:=</span>
  <span class="bp">∃</span> <span class="n">m</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">,</span> <span class="n">n</span> <span class="bp">/</span> <span class="n">m</span> <span class="bp">=</span> <span class="mi">2</span>

<span class="kn">theorem</span> <span class="n">sevenIsEven</span> <span class="o">:</span> <span class="o">(</span><span class="n">isEven</span> <span class="mi">7</span><span class="o">)</span> <span class="o">:=</span>
<span class="k">begin</span>
<span class="n">unfold</span> <span class="n">isEven</span><span class="o">,</span>
<span class="n">apply</span> <span class="n">exists</span><span class="bp">.</span><span class="n">intro</span> <span class="mi">3</span><span class="bp">.</span><span class="mi">5</span><span class="o">,</span>
<span class="n">apply</span> <span class="n">rfl</span><span class="o">,</span>
<span class="kn">end</span>
</pre></div>

#### [ Johan Commelin (Oct 19 2018 at 16:33)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Why%20doesn%27t%20exists.intro%20give%20err%20for%20witness%20of%20wrong%20type/near/136115173):
<p>Try it with <code>3</code> instead. Should work.</p>

#### [ Johan Commelin (Oct 19 2018 at 16:33)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Why%20doesn%27t%20exists.intro%20give%20err%20for%20witness%20of%20wrong%20type/near/136115181):
<p>Probably <code>3.5</code> is coerced into <code>3 : nat</code> or something like that.</p>

#### [ Johan Commelin (Oct 19 2018 at 16:34)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Why%20doesn%27t%20exists.intro%20give%20err%20for%20witness%20of%20wrong%20type/near/136115244):
<p>Note that your definition of <code>isEven</code> is not what we usually mean with being even, because <code>n / m</code> is not what we usually mean with <code>n / m</code>.</p>

#### [ Simon Hudon (Oct 19 2018 at 16:36)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Why%20doesn%27t%20exists.intro%20give%20err%20for%20witness%20of%20wrong%20type/near/136115369):
<p>If you use <code>set_option pp.numerals false</code> you see that <code>3.5</code> gets encoded as <code>bit1 (bit1 (has_one.one ℕ)) / bit0 (has_one.one ℕ)</code>, which, as Johan points out, is a natural number because of rounded division.</p>

#### [ Simon Hudon (Oct 19 2018 at 16:37)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Why%20doesn%27t%20exists.intro%20give%20err%20for%20witness%20of%20wrong%20type/near/136115404):
<p>(<code>(bit1 (bit1 (has_one.one ℕ)) / bit0 (has_one.one ℕ))</code> is <code>7 / 2</code>)</p>

#### [ Johan Commelin (Oct 19 2018 at 16:42)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Why%20doesn%27t%20exists.intro%20give%20err%20for%20witness%20of%20wrong%20type/near/136115693):
<p>I must say that I would rather get a syntax error at this point.</p>

#### [ Simon Hudon (Oct 19 2018 at 16:46)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Why%20doesn%27t%20exists.intro%20give%20err%20for%20witness%20of%20wrong%20type/near/136115958):
<p>One way to make this happen is to look at one of <span class="user-mention" data-user-id="110038">@Kevin Buzzard</span> suggestions and distinguish between proper division (<code>/</code>) and integer division (<code>÷</code>) (and the same can be said for subtraction vs pointed subtraction) and make sure that integers and natural numbers are only equipped with integer division. This way, expressing fractional numbers as division wouldn't work when fractional numbers aren't available.</p>

#### [ Kevin Buzzard (Oct 19 2018 at 17:16)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Why%20doesn%27t%20exists.intro%20give%20err%20for%20witness%20of%20wrong%20type/near/136117906):
<blockquote>
<p>Here's a proof that 7 is even. </p>
</blockquote>
<p>Just to be clear, what's happening here is that division is maybe not what you think it is. <code>7 / 3 = 2</code>, because <code>7 / 3</code> is declared to be of type nat.</p>

#### [ Simon Hudon (Oct 19 2018 at 17:19)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Why%20doesn%27t%20exists.intro%20give%20err%20for%20witness%20of%20wrong%20type/near/136118086):
<p>Right. And somehow, integer division doesn't seem to mesh with fractional numbers. If we were to express integer division as <code>÷</code> and a separate type class, <code>3.5</code> would not be a valid natural number</p>

#### [ Kevin Sullivan (Oct 19 2018 at 17:58)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Why%20doesn%27t%20exists.intro%20give%20err%20for%20witness%20of%20wrong%20type/near/136120649):
<blockquote>
<p>Right. And somehow, integer division doesn't seem to mesh with fractional numbers. If we were to express integer division as <code>÷</code> and a separate type class, <code>3.5</code> would not be a valid natural number</p>
</blockquote>
<p>Ok. Yes. This is slightly disturbing, but I understand.</p>
<div class="codehilite"><pre><span></span><span class="n">def</span> <span class="n">x</span> <span class="o">:</span> <span class="n">nat</span> <span class="o">:=</span> <span class="mi">3</span><span class="bp">.</span><span class="mi">5</span>
</pre></div>


<p>x is now 3.</p>


{% endraw %}
