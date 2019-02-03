---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/67584automaticsimplemmas.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [automatic simp lemmas](https://leanprover-community.github.io/archive/113488general/67584automaticsimplemmas.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Reid Barton (Dec 15 2018 at 06:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/automatic%20simp%20lemmas/near/151823722):
<p>We have a lot of simp lemmas in category theory that describe the action of functors, natural isomorphisms, etc. on various things. Johan has a few open PRs adding more of these lemmas (eg <a href="https://github.com/leanprover/mathlib/issues/503" target="_blank" title="https://github.com/leanprover/mathlib/issues/503">#503</a>, <a href="https://github.com/leanprover/mathlib/issues/505" target="_blank" title="https://github.com/leanprover/mathlib/issues/505">#505</a>) and they prompted me to try to understand how to describe these lemmas systematically.</p>

#### [ Reid Barton (Dec 15 2018 at 06:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/automatic%20simp%20lemmas/near/151823896):
<p>I think we can build these rfl lemmas by applying the following algorithm.</p>
<ul>
<li>Start with the result type <code>LHS = RHS</code>, where LHS is the thing being defined and RHS is its definition (this is what just putting <code>@[simp]</code> on the definition would do).</li>
<li>If the RHS is a Prop, then just throw away the equation (do nothing).</li>
<li>Otherwise, if the RHS is a record constructor <code>{ f1 := R1, f2 := R2 }</code>, recursively produce lemmas of the form <code>LHS.f1 = R1</code>, <code>LHS.f2 = R2</code>.</li>
<li>Otherwise, if the RHS is a lambda <code>\lam x, R x</code>, recursively produce a lemma <code>LHS x = R x</code>.</li>
<li>Otherwise, output a simp lemma stating <code>LHS = RHS</code> by rfl.</li>
</ul>

#### [ Reid Barton (Dec 15 2018 at 06:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/automatic%20simp%20lemmas/near/151823958):
<p><span class="user-mention" data-user-id="110026">@Simon Hudon</span>, I guess we discussed something along these lines at some point</p>

#### [ Reid Barton (Dec 15 2018 at 06:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/automatic%20simp%20lemmas/near/151824107):
<p>But now I have a pseudo-spec</p>

#### [ Johan Commelin (Dec 15 2018 at 07:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/automatic%20simp%20lemmas/near/151825251):
<p>See also <a href="#narrow/stream/116395-maths/subject/sheaves.20and.20sites/near/148770849" title="#narrow/stream/116395-maths/subject/sheaves.20and.20sites/near/148770849">https://leanprover.zulipchat.com/#narrow/stream/116395-maths/subject/sheaves.20and.20sites/near/148770849</a> for something that might qualify as pre-semi-pseudo-spec.</p>

#### [ Johan Commelin (Dec 15 2018 at 07:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/automatic%20simp%20lemmas/near/151825291):
<p>My PR's are the result of following Mario's creed "just go for it". But I definitely wouldn't mind if this was automated away.</p>

#### [ Simon Hudon (Dec 15 2018 at 17:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/automatic%20simp%20lemmas/near/151842594):
<p>I remember this conversation. In my mind, that kind of feature might be about translating lemmas about specific definitions into lemmas referring to a type class instance.</p>

#### [ Johan Commelin (Dec 15 2018 at 18:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/automatic%20simp%20lemmas/near/151844113):
<p><span class="user-mention" data-user-id="110026">@Simon Hudon</span> I'm not sure I understand what you mean. Is it close to what Reid wrote down, or do you want something (slightly) different?</p>

#### [ Johan Commelin (Dec 15 2018 at 18:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/automatic%20simp%20lemmas/near/151844463):
<p>(deleted)</p>

#### [ Simon Hudon (Dec 15 2018 at 19:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/automatic%20simp%20lemmas/near/151846909):
<p>Actually, I have a hard time remembering the details of that idea. I'll try to find the conversation again</p>

#### [ Johan Commelin (Dec 15 2018 at 22:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/automatic%20simp%20lemmas/near/151851104):
<p><span class="user-mention" data-user-id="110026">@Simon Hudon</span> If you want a good showcase of what Reid and I mean, I think you should look at the file on comma categories: <a href="https://github.com/leanprover-community/mathlib/blob/over_under/category_theory/comma.lean" target="_blank" title="https://github.com/leanprover-community/mathlib/blob/over_under/category_theory/comma.lean">https://github.com/leanprover-community/mathlib/blob/over_under/category_theory/comma.lean</a><br>
I just started adding over categories to the mix (a special case of comma categories), and I'm restating all the simp lemmas. The signal-to-noise ratio is increasing rapidly.</p>

#### [ Simon Hudon (Dec 15 2018 at 22:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/automatic%20simp%20lemmas/near/151851170):
<p>Ah yes! That's also what I was going for I think. The way I was generalizing it is that we want to unfold specific projections. I think I had an idea of which ones to unfold but I'd have to get back into that mindset</p>

#### [ Simon Hudon (Dec 15 2018 at 22:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/automatic%20simp%20lemmas/near/151851331):
<p>The good news is that soon, I won't have to take care of finding an apartment and I will have only Lean and my dissertation to take care of.</p>

#### [ Keeley Hoek (Dec 21 2018 at 10:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/automatic%20simp%20lemmas/near/152319775):
<p>I'm sorry if I annoyingly keep coming on about this, but I have a command which does the constructor-half of this thing and has been tested on at least one (:D) category theory structure definition. It's called <code>rfl_lemma</code> (you use it on its own line like <code>rfl_lemma inverse_equivalence map</code>---which would tell you that an inverse equivalence of an equivalence has functor going the "forward way" equal to the functor going the "backward way" in the original equivalence), and is here:<br>
<a href="https://github.com/semorrison/lean-tidy/blob/master/src/tidy/command/rfl_lemma.lean" target="_blank" title="https://github.com/semorrison/lean-tidy/blob/master/src/tidy/command/rfl_lemma.lean">https://github.com/semorrison/lean-tidy/blob/master/src/tidy/command/rfl_lemma.lean</a></p>
<p>It took multiple iterations because it turned out that getting the types right for the lemma I needed to generate turned out to be really quite hard (at least for me). I can give some examples to elabourate this point if anyone is interested. Making it do this for every projection of a structure instead of just the specified one is trivial.</p>

#### [ Keeley Hoek (Dec 21 2018 at 10:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/automatic%20simp%20lemmas/near/152319830):
<p><code>rfl_lemma?</code> is meant to tell you what the code generated was, and <code>private rfl_lemma ...</code> makes a private definition.</p>

#### [ Johan Commelin (Dec 21 2018 at 10:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/automatic%20simp%20lemmas/near/152319847):
<p>How much does this depend on the <code>lean-tidy</code> repo?</p>

#### [ Johan Commelin (Dec 21 2018 at 10:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/automatic%20simp%20lemmas/near/152319851):
<p>Sounds cool btw!</p>

#### [ Keeley Hoek (Dec 21 2018 at 10:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/automatic%20simp%20lemmas/near/152319864):
<p>it depends on a few pieces of the <code>lib</code> folder in there, let me take a look</p>

#### [ Sebastian Ullrich (Dec 21 2018 at 10:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/automatic%20simp%20lemmas/near/152319870):
<div class="codehilite"><pre><span></span>tk &quot;private rfl_lemma&quot;
</pre></div>


<p>omg</p>

#### [ Kevin Buzzard (Dec 21 2018 at 10:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/automatic%20simp%20lemmas/near/152319928):
<p>Is that pushing the definition of "token" a bit far or something?</p>

#### [ Johan Commelin (Dec 21 2018 at 10:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/automatic%20simp%20lemmas/near/152319930):
<p>If it doesn't depend too much on <code>lean-tidy</code>, I'dd say: push it to a branch on the community repo. Then we can experiment with it.</p>

#### [ Sebastian Ullrich (Dec 21 2018 at 10:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/automatic%20simp%20lemmas/near/152319955):
<p><span class="user-mention" data-user-id="110038">@Kevin Buzzard</span> It is, but I guess it actually works. Though, <span class="user-mention" data-user-id="110111">@Keeley Hoek</span>, have you taken a look at the <code>decl_meta_info</code> parameter?</p>

#### [ Keeley Hoek (Dec 21 2018 at 11:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/automatic%20simp%20lemmas/near/152320028):
<p>No I haven't Sebastian, and thanks, now I have an idea about what it's for :D</p>

#### [ Sebastian Ullrich (Dec 21 2018 at 11:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/automatic%20simp%20lemmas/near/152320044):
<p>Yeah, I don't think your current code would have worked anyway. There is no such registered token.</p>

#### [ Keeley Hoek (Dec 21 2018 at 11:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/automatic%20simp%20lemmas/near/152320059):
<p>The thing is, I'm pretty sure it did work! I'll try...</p>

#### [ Keeley Hoek (Dec 21 2018 at 11:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/automatic%20simp%20lemmas/near/152320066):
<p>also it was before I knew I could do stuff like parse a question mark after a token, so please forgive me... :D</p>

#### [ Sebastian Ullrich (Dec 21 2018 at 11:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/automatic%20simp%20lemmas/near/152320116):
<p>It will be parsed successfully, but it will still call the regular definition with <code>private := tt</code> in the meta info</p>

#### [ Keeley Hoek (Dec 21 2018 at 11:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/automatic%20simp%20lemmas/near/152320210):
<p>Unless you've run it and can prove I'm crazy, I just did and I'm quiiite confident a different one of those <code>user_command</code>s is being called depending on private or not</p>

#### [ Keeley Hoek (Dec 21 2018 at 11:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/automatic%20simp%20lemmas/near/152320258):
<p>Does it have something to do with the fact that for <code>user_command</code>s, unlike <code>user_notation</code>s, you don't need to reserve tokens for them to work?</p>

#### [ Sebastian Ullrich (Dec 21 2018 at 11:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/automatic%20simp%20lemmas/near/152320261):
<p>Right... oops</p>

#### [ Keeley Hoek (Dec 21 2018 at 11:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/automatic%20simp%20lemmas/near/152320305):
<p>:D</p>

#### [ Keeley Hoek (Dec 21 2018 at 11:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/automatic%20simp%20lemmas/near/152320330):
<p>But no reason not to fix it up so it works properly... cheers! (and I only need a single definition now, not <code>2^2</code>)</p>

#### [ Keeley Hoek (Dec 21 2018 at 11:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/automatic%20simp%20lemmas/near/152320363):
<p>BTW, here's a "live demo"</p>

#### [ Keeley Hoek (Dec 21 2018 at 11:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/automatic%20simp%20lemmas/near/152320369):
<p>(RE: the original post)</p>
<div class="codehilite"><pre><span></span><span class="kn">structure</span> <span class="n">my_str</span> <span class="o">:=</span>
<span class="o">(</span><span class="n">a</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">)</span>

<span class="n">def</span> <span class="n">a_cnstr</span> <span class="o">(</span><span class="n">b</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">)</span> <span class="o">:</span> <span class="n">my_str</span> <span class="o">:=</span> <span class="bp">⟨</span><span class="n">b</span><span class="bp">⟩</span>
<span class="n">def</span> <span class="n">a_cnstr&#39;</span> <span class="o">(</span><span class="n">b</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">)</span> <span class="o">:</span> <span class="n">my_str</span> <span class="o">:=</span> <span class="bp">⟨</span><span class="n">b</span> <span class="bp">+</span> <span class="mi">1</span><span class="bp">⟩</span>

<span class="n">rfl_lemma</span><span class="err">?</span> <span class="n">a_cnstr</span> <span class="n">a</span>
<span class="kn">private</span> <span class="n">rfl_lemma</span><span class="err">?</span> <span class="n">a_cnstr&#39;</span> <span class="n">a</span>
</pre></div>

#### [ Sebastian Ullrich (Dec 21 2018 at 11:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/automatic%20simp%20lemmas/near/152320457):
<p>Nice. Any reason it's not an attribute?</p>

#### [ Keeley Hoek (Dec 21 2018 at 11:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/automatic%20simp%20lemmas/near/152320555):
<p>That's cool</p>

#### [ Keeley Hoek (Dec 21 2018 at 11:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/automatic%20simp%20lemmas/near/152320641):
<p><span class="user-mention" data-user-id="112680">@Johan Commelin</span> Based on the pieces of <code>lib</code> which have ended up in mathlib now, I just need the <code>lib.expr</code> support file. My only reluctance comes from the fact that I will have to check whether a few of the functions at the bottom of that file are already in mathlib---at the time it was less effort just to write them.</p>

#### [ Keeley Hoek (Dec 21 2018 at 11:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/automatic%20simp%20lemmas/near/152320981):
<p>One more thing if anyone doing maths actually uses it: it adds a prime to the projection name you supply, seeing if that works, before trying without. Hopefully that's convenient</p>

#### [ Reid Barton (Dec 21 2018 at 20:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/automatic%20simp%20lemmas/near/152351507):
<p>The interface I had in mind was that you'd write something like <code>@[simp_fields] def a_cnstr ... := ...</code>, and it would automatically generate all of the appropriate lemmas.</p>


{% endraw %}
