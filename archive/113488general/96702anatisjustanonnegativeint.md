---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/96702anatisjustanonnegativeint.html
---

## Stream: [general](index.html)
### Topic: [a nat is just a non-negative int](96702anatisjustanonnegativeint.html)

---


{% raw %}
#### [ Kevin Buzzard (Sep 18 2018 at 11:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/a%20nat%20is%20just%20a%20non-negative%20int/near/134155954):
<p>Over the summer I watched students struggling with easy number theory for the wrong reasons. They were asked questions about <code>nat</code> but their solutions involve dabbling with <code>int</code>. First they had to realise that subtraction was broken in <code>nat</code>. Then they had to coerce everything. And then they ended up with random goals like <code>of_nat x &lt; \u y</code> where they knew <code>x &lt; y</code> but didn't know how to finish. Any attempt to use induction in tactic mode produced goals mentioning terms of the form <code>-[1+ succ e]</code> or some such thing, and again they didn't by default know what to do with such terms. The fact that <code>-[1+ e]</code> is not defeq to the coercion of <code>-(1+e)</code> did not help either (it turns out to be defeq to <code>-(e+1)</code>, which in some sense indicates that the notation is not great, but I don't know if there are technical problems with changing it). </p>
<p>I talked about this with Chris. He said that number theory was much harder than one might naively think, for beginners, because of these issues. I suggested that I just told them all to work with <code>int</code> at all times, because at least then the basic ring operations <code>+ - *</code> all do what the students think they will do, but Chris was not convinced that this was a good approach, because then you lose access to all the structure built on <code>nat</code>, for example primes. I did note that after a few weeks someone had defined <code>int.prime</code> and the students were using that. But I am asking if we can have more.</p>
<p>The structures <code>nat</code> and <code>{z : int // z &gt;= 0}</code> are canonically isomorphic, if you forget the subtraction on <code>nat</code> which no end user should be touching anyway if they're doing mathematics. Hence every definition or construction or theorem about nat should have a corresponding definition or construction or theorem if you have an int <code>z</code> in your list of hypotheses and also a proof that <code>z&gt;=0</code>. What I want the students to be able to do is to seamlessly get at all these definitions and constructions and theorems by perhaps using a tactic or perhaps using some clever tagging machinery (results about nat which transfer to int correctly because they don't mention subtraction, should be transferrable. For example one should be able to talk about <code>z</code> being prime, and it should realise that we just mean <code>nat.prime</code> for the corresponding <code>nat</code>). </p>
<p>How feasible is this?</p>

#### [ Johan Commelin (Sep 18 2018 at 12:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/a%20nat%20is%20just%20a%20non-negative%20int/near/134156545):
<p>I agree that we need better tooling here.<br>
Any solution to this should preferably also allow to show that every int is just a rat with denominator 1, and every real is just a complex with imaginary part 0, etc... etc...</p>

#### [ Kevin Buzzard (Sep 18 2018 at 12:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/a%20nat%20is%20just%20a%20non-negative%20int/near/134158536):
<p>Actually we also ran into problems with dividing integers because we weren't in rat. In the division case I told the student to bite the bullet and stick with rat and use division and remainder and just pretend the rational was there. But I think you're right really -- to let mathematicians use the software naturally something like the following should happen: whenever someone in "mathematician mode" (a mode which people like Mario would always have switched off) attempts to divide a nat by another nat a little paperclip should pop up and say "I see you're trying to divide naturals. Would you like to coerce every single thing into rat? That way you'll get the right answer!" and then every nat is replaced by a rat plus proof that the denominator is 1 and the numerator is non-negative. Why not! To the mathematician all that has happened is that a structure has been replaced with a canonically isomorphic structure -- or, in other words, nothing has happened at all, but their division now works correctly. I don't see any disadvantages in this. At the end of it we were supposed to prove that n = 3, and we've actually proved n_rat = 3 : Q, but Lean is smart enough to figure out that we're done because n_rat := (n : Q) and simp knows about the lemma which the mathematician is too blind to see that they need.</p>

#### [ Kevin Buzzard (Sep 18 2018 at 12:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/a%20nat%20is%20just%20a%20non-negative%20int/near/134158586):
<p>I really think that is how it should work. That's how maths packages work, and that's what we're used to.</p>

#### [ Johan Commelin (Sep 18 2018 at 13:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/a%20nat%20is%20just%20a%20non-negative%20int/near/134158669):
<p><span class="user-mention" data-user-id="110038">@Kevin Buzzard</span> You might be interested in the last chapter of Mohan's thesis. It deals with this concept of "unification". I think it is one of the main gaps that lies between mathematicians and theorem provers.</p>

#### [ Kevin Buzzard (Sep 18 2018 at 13:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/a%20nat%20is%20just%20a%20non-negative%20int/near/134158676):
<p>pari-gp:</p>
<div class="codehilite"><pre><span></span>$ gp
Reading GPRC: /etc/gprc ...Done.

                  GP/PARI CALCULATOR Version 2.7.5 (released)
          amd64 running linux (x86-64/GMP-6.0.0 kernel) 64-bit version
  compiled: Nov 10 2015, gcc version 5.2.1 20151028 (Ubuntu 5.2.1-23ubuntu1)
                           threading engine: pthread
                 (readline v6.3 enabled, extended help enabled)

                     Copyright (C) 2000-2015 The PARI Group

PARI/GP is free software, covered by the GNU General Public License, and comes
WITHOUT ANY WARRANTY WHATSOEVER.

Type ? for help, \q to quit.
Type ?12 for how to get moral (and possibly technical) support.

parisize = 8000000, primelimit = 500000
? x=4
%1 = 4
? type(x)
%2 = &quot;t_INT&quot;
? x
%3 = 4
? y=6/2
%4 = 3
? type(y)
%5 = &quot;t_INT&quot;
? z=x/y
%6 = 4/3
? type(z)
%7 = &quot;t_FRAC&quot;
? w=z*y
%8 = 4
? type(w)
%9 = &quot;t_INT&quot;
?
</pre></div>


<p>All happening seamlessly behind the user's back.</p>

#### [ Patrick Massot (Sep 18 2018 at 13:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/a%20nat%20is%20just%20a%20non-negative%20int/near/134158749):
<p>Of course I agree. We have fun with perfectoid spaces, but the sad truth is that Lean is not usable because you cannot manipulate school numbers.</p>

#### [ Johan Commelin (Sep 18 2018 at 13:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/a%20nat%20is%20just%20a%20non-negative%20int/near/134158776):
<p>Mohan discusses several solutions, including coercions etc. And he makes fair points about them. I'm not sure if his solution will ever be adaptable to computers, because he ends up using an extremely weak type system.</p>

#### [ Johan Commelin (Sep 18 2018 at 13:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/a%20nat%20is%20just%20a%20non-negative%20int/near/134158779):
<p>But it is a good read anyway.</p>

#### [ Johan Commelin (Sep 18 2018 at 13:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/a%20nat%20is%20just%20a%20non-negative%20int/near/134158845):
<p>Right, manipulating "numbers" should be trivial. By now I've learned to just avoid them. Seems like a bad solution.</p>

#### [ Kevin Buzzard (Sep 18 2018 at 13:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/a%20nat%20is%20just%20a%20non-negative%20int/near/134159314):
<p>Here's an example of the problem. Say we take the standard undergraduate proof that if p is prime and p divides ab then it divides a or b. Here p, a, b are all positive nats say (because the person setting the question is sloppy, which is fine, there is no drive in mathematics to make the absolute most general statement here, we're not adding to mathlib). So the student chooses nat for p,a,b, which is a reasonable-looking choice, and then we assume p does not divide a, and we have to use this somehow, and the way we use it is some lemma saying that if p doesn't divide a then the gcd of p and a is 1. Now we use the standard fact that the gcd is a linear combination of the numbers in question, write <code>1=l*p+m*a</code> with <code>l</code> and <code>m</code> now ints, all these random up-arrows start appearing, we multiply both sides by b, prove that p divides both factors and try to deduce that p divides b but we've only deduced \u p divides \u b. What happened? What would be really nice is that when <code>gcd = l p + m a</code> is invoked <em>everything</em> becomes and int, and a tactic changes our goal to the corresponding statement about ints, and the user barely notices.</p>

#### [ Kevin Buzzard (Sep 18 2018 at 13:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/a%20nat%20is%20just%20a%20non-negative%20int/near/134159412):
<p>Kicking around in the background is a proof that the new int-valued a and b and p are &gt;= 0, so if the user ever wants to switch back and it's safe to, they can.</p>

#### [ Kevin Buzzard (Sep 18 2018 at 13:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/a%20nat%20is%20just%20a%20non-negative%20int/near/134159421):
<p><span class="user-mention" data-user-id="110026">@Simon Hudon</span> Is this sort of thing feasible or am I asking for magic? Someone once told me that Lean does not do magic.</p>

#### [ Simon Hudon (Sep 18 2018 at 13:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/a%20nat%20is%20just%20a%20non-negative%20int/near/134161382):
<p>I taught you well, young man :) I think there are a few things we could try. We could have a tactic <code>to_int</code> to find all the local constants of type <code>nat</code> and replace them with a constant of the same name but of type <code>int</code> with an added assumption saying that it's non-negative.</p>

#### [ Simon Hudon (Sep 18 2018 at 14:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/a%20nat%20is%20just%20a%20non-negative%20int/near/134161403):
<p>The remaining problem would be to rewrite the assumptions to remove <code>\u</code> occurrences and use integer related functions / operators</p>

#### [ Simon Hudon (Sep 18 2018 at 14:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/a%20nat%20is%20just%20a%20non-negative%20int/near/134161468):
<p>The short answer is yes if the above is satisfactory to you</p>

#### [ Simon Hudon (Sep 18 2018 at 14:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/a%20nat%20is%20just%20a%20non-negative%20int/near/134161508):
<p>We could have a more elaborate tactic language to solve that problem but I'm thinking it might be overkill</p>

#### [ Kevin Buzzard (Sep 18 2018 at 14:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/a%20nat%20is%20just%20a%20non-negative%20int/near/134161837):
<p>It could fail if the int version of the goal didn't imply the nat version.</p>

#### [ Simon Hudon (Sep 18 2018 at 14:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/a%20nat%20is%20just%20a%20non-negative%20int/near/134162045):
<p>The way I'm thinking of it, if that was the case, you'd be left with some <code>\u</code>. But we can also make it fail if you prefer that.</p>

#### [ Simon Hudon (Sep 18 2018 at 14:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/a%20nat%20is%20just%20a%20non-negative%20int/near/134162484):
<p>The easiest way to implement it would be to use <code>simp</code> to rewrite all the propositions into equivalent ones. This is stronger than required but it has the benefit of being simple to do.</p>

#### [ Simon Hudon (Sep 18 2018 at 16:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/a%20nat%20is%20just%20a%20non-negative%20int/near/134170146):
<p>I just wrote a tactic to see if it could be done. I used it in the following example:</p>
<div class="codehilite"><pre><span></span><span class="kn">example</span> <span class="o">(</span><span class="n">a</span> <span class="n">b</span> <span class="n">c</span> <span class="n">d</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">)</span>
  <span class="o">(</span><span class="n">h</span> <span class="o">:</span> <span class="n">a</span> <span class="bp">+</span> <span class="n">b</span> <span class="bp">≥</span> <span class="n">c</span><span class="o">)</span>
  <span class="o">(</span><span class="n">h₀</span> <span class="o">:</span> <span class="n">a</span> <span class="err">∣</span> <span class="n">c</span><span class="o">)</span>
  <span class="o">(</span><span class="n">h&#39;</span> <span class="o">:</span> <span class="n">a</span> <span class="bp">+</span> <span class="n">c</span> <span class="bp">+</span> <span class="mi">17</span> <span class="bp">≥</span> <span class="n">d</span><span class="o">)</span> <span class="o">:</span>
  <span class="n">a</span> <span class="bp">*</span> <span class="n">c</span> <span class="bp">≤</span> <span class="n">b</span> <span class="bp">+</span> <span class="n">d</span> <span class="bp">*</span> <span class="n">c</span> <span class="o">:=</span>
<span class="k">begin</span>
  <span class="n">to_int</span><span class="o">,</span>
    <span class="c1">-- a : ℤ,</span>
    <span class="c1">-- a_nneg : a ≥ 0,</span>
    <span class="c1">-- b : ℤ,</span>
    <span class="c1">-- b_nneg : b ≥ 0,</span>
    <span class="c1">-- c : ℤ,</span>
    <span class="c1">-- c_nneg : c ≥ 0,</span>
    <span class="c1">-- d : ℤ,</span>
    <span class="c1">-- d_nneg : d ≥ 0,</span>
    <span class="c1">-- h : a + b ≥ c,</span>
    <span class="c1">-- h₀ : a ∣ c,</span>
    <span class="c1">-- h&#39; : a + c + 17 ≥ d</span>
    <span class="c1">-- ⊢ a * c ≤ b + d * c</span>
<span class="kn">end</span>
</pre></div>


<p>Does that look like what you're looking for?</p>

#### [ Simon Hudon (Sep 18 2018 at 16:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/a%20nat%20is%20just%20a%20non-negative%20int/near/134171190):
<p>I just pushed it to <code>mathlib-nursery</code>. To use it, <code>import tactic.to_int</code></p>

#### [ Simon Hudon (Sep 18 2018 at 16:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/a%20nat%20is%20just%20a%20non-negative%20int/near/134171215):
<p>I'm hopeful that any oversight of the current version can be fixed by tagging lemmas with <code>@[to_int]</code></p>

#### [ Mario Carneiro (Sep 18 2018 at 16:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/a%20nat%20is%20just%20a%20non-negative%20int/near/134171547):
<p>The version I'm thinking of here would be a tactic like <code>cast ℤ at h1 h2</code>, which would try to convert any equalities or inequalities in the given target(s) to the specified type using cast theorems</p>

#### [ Mario Carneiro (Sep 18 2018 at 17:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/a%20nat%20is%20just%20a%20non-negative%20int/near/134171631):
<p>Applied to <code>h'</code> above it would produce <code>(↑a + ↑c + 17 : ℤ) ≥ ↑d</code></p>

#### [ Simon Hudon (Sep 18 2018 at 17:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/a%20nat%20is%20just%20a%20non-negative%20int/near/134172005):
<p>I decided to go one step further and eliminate all arrows if possible just so Kevin's student don't have to think about them.</p>

#### [ Chris Hughes (Sep 18 2018 at 17:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/a%20nat%20is%20just%20a%20non-negative%20int/near/134172093):
<p>I think hiding too much information might cause more problems than it solves.</p>

#### [ Mario Carneiro (Sep 18 2018 at 17:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/a%20nat%20is%20just%20a%20non-negative%20int/near/134172119):
<p>I'm also worried about losing the link to the original variables, which may be involved in other things that can't be cast</p>

#### [ Simon Hudon (Sep 18 2018 at 17:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/a%20nat%20is%20just%20a%20non-negative%20int/near/134172222):
<p>I agree that it can be the case but in this situation, removing the arrows can take a number of lines that aren't too enlightening with regards to what you're trying to prove</p>

#### [ Mario Carneiro (Sep 18 2018 at 17:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/a%20nat%20is%20just%20a%20non-negative%20int/near/134172299):
<p>that's the part that a <code>cast</code> tactic would solve</p>

#### [ Simon Hudon (Sep 18 2018 at 17:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/a%20nat%20is%20just%20a%20non-negative%20int/near/134172301):
<p>The other thing is that, if we keep the arrows, you end up working with two kinds of addition, two kinds of multiplication ... etc. I thought I'd try to remove that hurdle</p>

#### [ Mario Carneiro (Sep 18 2018 at 17:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/a%20nat%20is%20just%20a%20non-negative%20int/near/134172432):
<p><code>cast</code> would also solve that</p>

#### [ Simon Hudon (Sep 18 2018 at 17:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/a%20nat%20is%20just%20a%20non-negative%20int/near/134172456):
<p>What part of <code>to_int</code> would you not put in <code>cast</code>?</p>

#### [ Mario Carneiro (Sep 18 2018 at 17:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/a%20nat%20is%20just%20a%20non-negative%20int/near/134172534):
<p>the part about eliminating the original variables in favor of arbitrary nonnegative integers</p>

#### [ Mario Carneiro (Sep 18 2018 at 17:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/a%20nat%20is%20just%20a%20non-negative%20int/near/134172548):
<p>and also allowing for more targeting to particular hypotheses</p>

#### [ Simon Hudon (Sep 18 2018 at 17:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/a%20nat%20is%20just%20a%20non-negative%20int/near/134172746):
<p>I can see the point of that. Actually, I can see a case for both removing the original variables and keeping them.</p>

#### [ Mario Carneiro (Sep 18 2018 at 17:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/a%20nat%20is%20just%20a%20non-negative%20int/near/134174523):
<p>besides the mental load of having arrows in your goal, I don't see any harm in keeping them, meaning that unless you are being specifically pedagogical and you are before the chapter on coercion or whatever it seems like a bad idea to remove them</p>

#### [ Mario Carneiro (Sep 18 2018 at 17:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/a%20nat%20is%20just%20a%20non-negative%20int/near/134174601):
<p>That is, they shouldn't get in your way for the rest of the proof once they have been moved down to the atoms</p>

#### [ Simon Hudon (Sep 18 2018 at 18:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/a%20nat%20is%20just%20a%20non-negative%20int/near/134176929):
<p>I agree that it's useful for pedagogical reasons and to lift a mental burden but I wouldn't say that those are mere goodies. I think that limiting the size of the relevant vocabulary (int vs nat) can make solutions more obvious both for a human prover and for an automated prover. If every natural number in your goal occurs with <code>\u</code> right next to it, most likely, natural numbers are not relevant for that part of the proof so let's not look for <code>nat.</code> lemmas.</p>

#### [ Mario Carneiro (Sep 18 2018 at 19:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/a%20nat%20is%20just%20a%20non-negative%20int/near/134179372):
<p>It is true that if a natural number <code>n</code> only ever appears in the form <code>\u n</code> in hypotheses and the goal, then it is "safe" to replace it with a nonnegative integer variable. But this only works in certain cases; I don't see an analogous argument for <code>Q -&gt; R</code> coercion for example.</p>

#### [ Simon Hudon (Sep 18 2018 at 19:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/a%20nat%20is%20just%20a%20non-negative%20int/near/134179785):
<p>That can be optional behavior. It can a useful thing to do in other cases too. But in the case of nat / int, the knowledge we have of the situation allows us to assume <code>i ≥ 0</code></p>

#### [ Nicholas Scheel (Sep 20 2018 at 20:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/a%20nat%20is%20just%20a%20non-negative%20int/near/134326214):
<p>I was playing around with a tactic that I think does similar things: <a href="https://github.com/MonoidMusician/MATH361/blob/lean-3.4.1/src/naturally.lean" target="_blank" title="https://github.com/MonoidMusician/MATH361/blob/lean-3.4.1/src/naturally.lean">https://github.com/MonoidMusician/MATH361/blob/lean-3.4.1/src/naturally.lean</a></p>

#### [ Nicholas Scheel (Sep 20 2018 at 20:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/a%20nat%20is%20just%20a%20non-negative%20int/near/134326321):
<p>some usages: <a href="https://github.com/MonoidMusician/MATH361/blob/lean-3.4.1/src/hw/hw2.lean#L520" target="_blank" title="https://github.com/MonoidMusician/MATH361/blob/lean-3.4.1/src/hw/hw2.lean#L520">https://github.com/MonoidMusician/MATH361/blob/lean-3.4.1/src/hw/hw2.lean#L520</a></p>

#### [ Nicholas Scheel (Sep 20 2018 at 20:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/a%20nat%20is%20just%20a%20non-negative%20int/near/134326426):
<p>at the end I use it to squash all of these at once, after applying <code>div_nonneg</code> as appropriate:</p>
<div class="codehilite"><pre><span></span><span class="mi">9</span> <span class="n">goals</span>
<span class="err">⊢</span> <span class="mi">0</span> <span class="bp">≤</span> <span class="mi">81</span>
<span class="err">⊢</span> <span class="mi">0</span> <span class="bp">&lt;</span> <span class="mi">64</span>
<span class="err">⊢</span> <span class="mi">0</span> <span class="bp">≤</span> <span class="mi">2</span>
<span class="err">⊢</span> <span class="mi">0</span> <span class="bp">≤</span> <span class="mi">9</span>
<span class="err">⊢</span> <span class="mi">0</span> <span class="bp">&lt;</span> <span class="mi">8</span>
<span class="err">⊢</span> <span class="mi">0</span> <span class="bp">≤</span> <span class="mi">9</span>
<span class="err">⊢</span> <span class="mi">0</span> <span class="bp">&lt;</span> <span class="mi">4</span>
<span class="err">⊢</span> <span class="mi">0</span> <span class="bp">≤</span> <span class="mi">3</span>
<span class="err">⊢</span> <span class="mi">0</span> <span class="bp">&lt;</span> <span class="mi">2</span>
</pre></div>

#### [ Nicholas Scheel (Sep 20 2018 at 20:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/a%20nat%20is%20just%20a%20non-negative%20int/near/134326444):
<p>(those statements are all in ℝ)</p>

#### [ Mario Carneiro (Sep 20 2018 at 20:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/a%20nat%20is%20just%20a%20non-negative%20int/near/134326914):
<p><code>norm_num</code>?</p>


{% endraw %}
