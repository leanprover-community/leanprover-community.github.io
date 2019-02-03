---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/26591palindromes.html
---

## Stream: [general](index.html)
### Topic: [palindromes](26591palindromes.html)

---


{% raw %}
#### [ Kevin Buzzard (Apr 03 2018 at 22:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/palindromes/near/124591860):
<p>For recreational reasons I was interested in working with lists which were palindromes, i.e. lists <code>G</code> satisfying <code>G = list.reverse G</code>. I wanted to prove a bunch of stuff about these things but I couldn't prove anything by induction because lists don't decompose like that. I wanted to write a general <code>G</code> of length 2 or more as <code>G=[head G] ++ middle G ++ [head G]</code> and have a recursor of the form <code>C [] -&gt; C [x] -&gt; forall palindromes H, C H -&gt; C ([a] ++ H ++ [a]) -&gt; forall palindromes G, C G</code></p>

#### [ Kevin Buzzard (Apr 03 2018 at 22:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/palindromes/near/124591884):
<p>What is the idiomatic way to do this in Lean? I am at the stage now where I could probably get several methods to go through</p>

#### [ Kevin Buzzard (Apr 03 2018 at 22:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/palindromes/near/124591886):
<p>but I would like to choose the one with the least pain.</p>

#### [ Kevin Buzzard (Apr 03 2018 at 22:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/palindromes/near/124591890):
<p>Should I actually make a new inductive type?</p>

#### [ Mario Carneiro (Apr 03 2018 at 22:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/palindromes/near/124593010):
<p>You should look at <code>list.reverse_rec_on</code> for a similar eliminator. You could encode it as an inductive predicate, and then prove that it is equivalent to <code>g = list.reverse g</code>, or you could prove the eliminator you wrote with <code>palindromes</code> defined using reverse</p>

#### [ Chris Hughes (Apr 03 2018 at 22:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/palindromes/near/124593011):
<p>I stopped as soon as it got hard</p>
<div class="codehilite"><pre><span></span><span class="kn">inductive</span>  <span class="n">palindrome</span> <span class="o">:</span> <span class="n">list</span> <span class="n">α</span> <span class="bp">→</span>  <span class="kt">Prop</span>
<span class="bp">|</span> <span class="n">nil</span> <span class="o">:</span> <span class="n">palindrome</span> <span class="o">[]</span>
<span class="bp">|</span> <span class="n">singleton</span> <span class="o">:</span> <span class="bp">∀</span> <span class="n">a</span><span class="o">,</span> <span class="n">palindrome</span> <span class="o">[</span><span class="n">a</span><span class="o">]</span>
<span class="bp">|</span> <span class="n">cons</span> <span class="o">:</span> <span class="bp">∀</span> <span class="o">(</span><span class="n">a</span><span class="o">)</span> <span class="o">(</span><span class="n">l</span><span class="o">),</span> <span class="n">palindrome</span> <span class="n">l</span> <span class="bp">→</span> <span class="n">palindrome</span> <span class="o">([</span><span class="n">a</span><span class="o">]</span> <span class="bp">++</span> <span class="n">l</span> <span class="bp">++</span> <span class="o">[</span><span class="n">a</span><span class="o">])</span>

<span class="kn">lemma</span>  <span class="n">palindrome_iff_eq_reverse</span> <span class="o">{</span><span class="n">l</span> <span class="o">:</span> <span class="n">list</span> <span class="n">α</span><span class="o">}</span> <span class="o">:</span> <span class="n">palindrome</span> <span class="n">l</span> <span class="bp">↔</span> <span class="n">l</span> <span class="bp">=</span> <span class="n">list</span><span class="bp">.</span><span class="n">reverse</span> <span class="n">l</span> <span class="o">:=</span>
<span class="bp">⟨λ</span> <span class="n">h</span><span class="o">,</span> <span class="n">palindrome</span><span class="bp">.</span><span class="n">rec_on</span> <span class="n">h</span> <span class="n">rfl</span> <span class="o">(</span><span class="bp">λ</span> <span class="n">a</span><span class="o">,</span> <span class="n">rfl</span><span class="o">)</span> <span class="o">(</span><span class="bp">λ</span> <span class="n">a</span> <span class="n">l</span> <span class="n">h₁</span> <span class="n">h₂</span><span class="o">,</span>
<span class="k">begin</span>
<span class="n">conv</span> <span class="o">{</span><span class="n">to_lhs</span><span class="o">,</span> <span class="n">rw</span> <span class="n">h₂</span><span class="o">},</span>
<span class="n">rw</span> <span class="err">←</span> <span class="n">list</span><span class="bp">.</span><span class="n">reverse_singleton</span> <span class="n">a</span><span class="o">,</span>
<span class="n">simp</span><span class="o">,</span>
<span class="kn">end</span><span class="o">),</span> <span class="n">list</span><span class="bp">.</span><span class="n">rec_on</span> <span class="n">l</span> <span class="o">(</span><span class="bp">λ</span> <span class="n">h</span><span class="o">,</span> <span class="n">palindrome</span><span class="bp">.</span><span class="n">nil</span><span class="o">)</span>
<span class="o">(</span><span class="bp">λ</span> <span class="n">a</span> <span class="n">l</span> <span class="n">h</span><span class="o">,</span> <span class="k">begin</span> <span class="n">apply</span> <span class="n">list</span><span class="bp">.</span><span class="n">reverse_rec_on</span> <span class="n">l</span><span class="o">,</span> <span class="kn">end</span><span class="o">)</span><span class="bp">⟩</span>
</pre></div>

#### [ Mario Carneiro (Apr 03 2018 at 22:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/palindromes/near/124593343):
<p>In the cons case you have <code>a::l = list.reverse (a::l) = l.reverse ++ [a]</code>. By cases on <code>l.reverse</code>, if <code>l.reverse = []</code> then <code>a::l = [a]</code> is a palindrome, and if <code>l.reverse = b::l'</code> then <code>a::l = b::l'++[a]</code> so <code>a = b</code> and <code>l = l' ++ [a]</code>, so <code>a :: l'.reverse = l.reverse = a::l'</code> and hence <code>l' = l'.reverse</code>, so <code>l'</code> is a palindrome by IH and hence <code>a::l</code> is a palindrome</p>

#### [ Chris Hughes (Apr 03 2018 at 23:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/palindromes/near/124594253):
<p>Is there a lemma saying <code>a :: l = b :: m -&gt; a = b</code>?</p>

#### [ Kevin Buzzard (Apr 03 2018 at 23:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/palindromes/near/124594260):
<p>no_confusion</p>

#### [ Kevin Buzzard (Apr 03 2018 at 23:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/palindromes/near/124594271):
<p>or cons_inj or whatever</p>

#### [ Chris Hughes (Apr 03 2018 at 23:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/palindromes/near/124594377):
<p>cons_inj tells me about the lists being equal.</p>

#### [ Sebastian Ullrich (Apr 03 2018 at 23:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/palindromes/near/124594398):
<p>or the <code>injection</code> tactic</p>

#### [ Chris Hughes (Apr 03 2018 at 23:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/palindromes/near/124594462):
<p>Thanks <span class="user-mention" data-user-id="110024">@Sebastian Ullrich</span> I'd never used injection successfully before.</p>

#### [ Kevin Buzzard (Apr 03 2018 at 23:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/palindromes/near/124595081):
<p><code>example {β : Type*} (a b : β) (l m : list β) : a :: l = b :: m -&gt; a = b :=  λ H, (list.cons.inj H).1</code></p>

#### [ Kevin Buzzard (Apr 03 2018 at 23:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/palindromes/near/124595142):
<p>I feel confident with this sort of stuff now I've seen how it all works.</p>

#### [ Kevin Buzzard (Apr 03 2018 at 23:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/palindromes/near/124595241):
<p><code>example {β : Type*} (a b : β) (l m : list β) : a :: l = b :: m -&gt; a = b := λ H, @list.no_confusion _ _ (a::l) (b::m) H (λ x y,x)</code></p>

#### [ Kevin Buzzard (Apr 03 2018 at 23:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/palindromes/near/124595265):
<p>Chris, it was your questioning a week last Thurs which pushed me to learn this stuff. We didn't quite go as far as we should have done. We looked at no_confusion for bool and nat, but if you look at it for list you see how all the terms involved in the constructors are used.</p>

#### [ Kevin Buzzard (Apr 03 2018 at 23:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/palindromes/near/124595342):
<div class="codehilite"><pre><span></span>variables {a b : β} {L M : list β} {P : Type}
#reduce list.no_confusion_type P (a::L) (b::M) -- (a = b → L = M → P) → P
</pre></div>

#### [ Kevin Buzzard (Apr 03 2018 at 23:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/palindromes/near/124595391):
<p>You use no_confusion to make an instance of that type.</p>

#### [ Kevin Buzzard (Apr 03 2018 at 23:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/palindromes/near/124595732):
<blockquote>
<p>In the cons case you have <code>a::l = list.reverse (a::l) = l.reverse ++ [a]</code>. By cases on <code>l.reverse</code>, if <code>l.reverse = []</code> then <code>a::l = [a]</code> is a palindrome, and if <code>l.reverse = b::l'</code> then <code>a::l = b::l'++[a]</code> so <code>a = b</code> and <code>l = l' ++ [a]</code>, so <code>a :: l'.reverse = l.reverse = a::l'</code> and hence <code>l' = l'.reverse</code>, so <code>l'</code> is a palindrome by IH and hence <code>a::l</code> is a palindrome</p>
</blockquote>
<p>For me, I can prove l' = l'.reverse but the inductive hypothesis doesn't let me conclude l' is a palindrome, the inductive hypothesis the way I've set it up says at this point that if (a::l') is its own reverse then (a::l') is a palindrome.</p>

#### [ Kevin Buzzard (Apr 03 2018 at 23:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/palindromes/near/124595764):
<p>Somehow this is exactly the issue I keep running into: list has the wrong recursor for me.</p>

#### [ Kevin Buzzard (Apr 03 2018 at 23:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/palindromes/near/124595820):
<p>I can see that because I have <code>list.rec_on</code> and <code>list.reverse_rec_on</code> I should have all I need, but I don't know what <code>C</code> should be in some sense (what is <code>C</code> called? The motive?)</p>

#### [ Chris Hughes (Apr 04 2018 at 00:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/palindromes/near/124596524):
<p>I've been struggling with this too. I think the best would be some sort of strong induction on the list.</p>

#### [ Mario Carneiro (Apr 04 2018 at 00:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/palindromes/near/124597147):
<p>You should do strong induction on the length of the list</p>

#### [ Kenny Lau (Apr 04 2018 at 00:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/palindromes/near/124597485):
<p><span class="user-mention" data-user-id="110038">@Kevin Buzzard</span> you could use a custom recursor</p>

#### [ Kenny Lau (Apr 04 2018 at 00:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/palindromes/near/124597486):
<p>see <a href="https://github.com/kckennylau/Lean/blob/master/recursion.lean" target="_blank" title="https://github.com/kckennylau/Lean/blob/master/recursion.lean">https://github.com/kckennylau/Lean/blob/master/recursion.lean</a></p>

#### [ Kenny Lau (Apr 04 2018 at 00:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/palindromes/near/124597487):
<p>for an example</p>

#### [ Ching-Tsun Chou (Apr 04 2018 at 01:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/palindromes/near/124599343):
<p>The trick to prove the lemma Chris wants to prove is to consider the two cases (a) length l = 2<em>n and (b) length l = 2</em>n + 1 separately and then use induction on n in each case.</p>

#### [ Kenny Lau (Apr 04 2018 at 01:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/palindromes/near/124599350):
<p>omg someone from hong kong</p>

#### [ Chris Hughes (Apr 04 2018 at 21:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/palindromes/near/124638255):
<p>Finally did it. </p>
<div class="codehilite"><pre><span></span><span class="kn">inductive</span> <span class="n">palindrome</span> <span class="o">:</span> <span class="n">list</span> <span class="n">α</span> <span class="bp">→</span> <span class="kt">Prop</span>
<span class="bp">|</span> <span class="n">nil</span>       <span class="o">:</span> <span class="n">palindrome</span> <span class="o">[]</span>
<span class="bp">|</span> <span class="n">singleton</span> <span class="o">:</span> <span class="bp">∀</span> <span class="n">a</span><span class="o">,</span> <span class="n">palindrome</span> <span class="o">[</span><span class="n">a</span><span class="o">]</span>
<span class="bp">|</span> <span class="n">cons</span>      <span class="o">:</span> <span class="bp">∀</span> <span class="o">(</span><span class="n">a</span><span class="o">)</span> <span class="o">(</span><span class="n">l</span><span class="o">),</span> <span class="n">palindrome</span> <span class="n">l</span> <span class="bp">→</span> <span class="n">palindrome</span> <span class="o">([</span><span class="n">a</span><span class="o">]</span> <span class="bp">++</span> <span class="n">l</span> <span class="bp">++</span> <span class="o">[</span><span class="n">a</span><span class="o">])</span>

<span class="kn">lemma</span> <span class="n">eq_reverse_of_palindrome</span> <span class="o">{</span><span class="n">l</span> <span class="o">:</span> <span class="n">list</span> <span class="n">α</span><span class="o">}</span> <span class="o">:</span> <span class="n">palindrome</span> <span class="n">l</span> <span class="bp">→</span> <span class="n">l</span> <span class="bp">=</span> <span class="n">list</span><span class="bp">.</span><span class="n">reverse</span> <span class="n">l</span> <span class="o">:=</span>
<span class="bp">λ</span> <span class="n">h</span><span class="o">,</span> <span class="n">palindrome</span><span class="bp">.</span><span class="n">rec_on</span> <span class="n">h</span> <span class="n">rfl</span> <span class="o">(</span><span class="bp">λ</span> <span class="n">a</span><span class="o">,</span> <span class="n">rfl</span><span class="o">)</span> <span class="o">(</span><span class="bp">λ</span> <span class="n">a</span> <span class="n">l</span> <span class="n">h₁</span> <span class="n">h₂</span><span class="o">,</span>
<span class="k">begin</span>
  <span class="n">conv</span> <span class="o">{</span><span class="n">to_lhs</span><span class="o">,</span> <span class="n">rw</span> <span class="n">h₂</span><span class="o">},</span>
  <span class="n">rw</span> <span class="err">←</span> <span class="n">list</span><span class="bp">.</span><span class="n">reverse_singleton</span> <span class="n">a</span><span class="o">,</span>
  <span class="n">simp</span><span class="o">,</span>
<span class="kn">end</span><span class="o">)</span>

<span class="kn">open</span> <span class="n">list</span>
<span class="kn">lemma</span> <span class="n">palindrome_of_eq_reverse</span>  <span class="o">:</span> <span class="bp">∀</span> <span class="o">{</span><span class="n">l</span> <span class="o">:</span> <span class="n">list</span> <span class="n">α</span><span class="o">},</span> <span class="n">l</span> <span class="bp">=</span> <span class="n">list</span><span class="bp">.</span><span class="n">reverse</span> <span class="n">l</span> <span class="bp">→</span> <span class="n">palindrome</span> <span class="n">l</span>
<span class="bp">|</span> <span class="n">list</span><span class="bp">.</span><span class="n">nil</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="bp">_</span><span class="o">,</span> <span class="n">palindrome</span><span class="bp">.</span><span class="n">nil</span>
<span class="bp">|</span> <span class="o">(</span><span class="n">a</span> <span class="bp">::</span> <span class="n">l</span><span class="o">)</span> <span class="o">:=</span> <span class="k">begin</span>
  <span class="n">rw</span> <span class="n">reverse_cons&#39;</span><span class="o">,</span>
  <span class="n">generalize</span> <span class="n">hl&#39;</span> <span class="o">:</span> <span class="n">l</span><span class="bp">.</span><span class="n">reverse</span> <span class="bp">=</span> <span class="n">l&#39;</span><span class="o">,</span>
  <span class="n">cases</span> <span class="n">l&#39;</span>  <span class="k">with</span> <span class="n">b</span> <span class="n">l&#39;</span><span class="o">,</span>
  <span class="o">{</span> <span class="k">assume</span> <span class="n">h</span><span class="o">,</span>
    <span class="n">rw</span> <span class="n">h</span><span class="o">,</span>
    <span class="n">exact</span> <span class="n">palindrome</span><span class="bp">.</span><span class="n">singleton</span> <span class="bp">_</span>  <span class="o">},</span>
  <span class="o">{</span> <span class="k">assume</span> <span class="n">h</span><span class="o">,</span>
    <span class="k">have</span> <span class="o">:</span> <span class="n">a</span> <span class="bp">=</span> <span class="n">b</span> <span class="o">:=</span> <span class="k">by</span> <span class="n">injection</span> <span class="n">h</span><span class="o">,</span>
    <span class="n">rw</span> <span class="n">this</span> <span class="n">at</span> <span class="bp">*</span><span class="o">,</span>
    <span class="k">have</span> <span class="n">h₁</span> <span class="o">:</span> <span class="n">l</span> <span class="bp">=</span> <span class="n">l&#39;</span> <span class="bp">++</span> <span class="o">[</span><span class="n">b</span><span class="o">]</span> <span class="o">:=</span> <span class="k">by</span> <span class="n">injection</span> <span class="n">h</span><span class="o">,</span>
    <span class="k">have</span> <span class="n">h₂</span> <span class="o">:</span>  <span class="n">b</span> <span class="bp">::</span> <span class="n">l&#39;</span> <span class="bp">=</span> <span class="n">reverse</span> <span class="o">[</span><span class="n">b</span><span class="o">]</span> <span class="bp">++</span> <span class="n">reverse</span> <span class="n">l&#39;</span> <span class="o">:=</span>
      <span class="k">by</span> <span class="n">rwa</span>  <span class="o">[</span><span class="err">←</span> <span class="n">reverse_inj</span><span class="o">,</span> <span class="n">hl&#39;</span><span class="o">,</span> <span class="n">reverse_append</span><span class="o">]</span> <span class="n">at</span> <span class="n">h₁</span><span class="o">,</span>
    <span class="k">have</span> <span class="o">:</span> <span class="n">l&#39;</span> <span class="bp">=</span> <span class="n">l&#39;</span><span class="bp">.</span><span class="n">reverse</span> <span class="o">:=</span> <span class="k">by</span> <span class="n">injection</span> <span class="n">h₂</span><span class="o">,</span>
    <span class="n">rw</span> <span class="n">h</span><span class="o">,</span>
    <span class="n">exact</span> <span class="k">have</span> <span class="n">h₂</span> <span class="o">:</span> <span class="n">length</span> <span class="n">l&#39;</span> <span class="bp">&lt;</span> <span class="mi">1</span> <span class="bp">+</span> <span class="n">length</span> <span class="n">l</span> <span class="o">:=</span>
      <span class="k">by</span> <span class="n">rw</span> <span class="o">[</span><span class="n">h₁</span><span class="o">,</span> <span class="n">add_comm</span><span class="o">,</span> <span class="n">length_append</span><span class="o">]</span><span class="bp">;</span>
        <span class="n">exact</span> <span class="n">lt_trans</span> <span class="o">(</span><span class="n">lt_succ_self</span> <span class="bp">_</span><span class="o">)</span> <span class="o">(</span><span class="n">lt_succ_self</span> <span class="bp">_</span><span class="o">),</span>
      <span class="n">palindrome</span><span class="bp">.</span><span class="n">cons</span> <span class="bp">_</span> <span class="bp">_</span> <span class="o">(</span><span class="n">palindrome_of_eq_reverse</span> <span class="n">this</span><span class="o">)</span> <span class="o">}</span>
<span class="kn">end</span>
<span class="n">using_well_founded</span> <span class="o">{</span><span class="n">rel_tac</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="bp">_</span> <span class="bp">_</span><span class="o">,</span> <span class="bp">`</span><span class="o">[</span><span class="n">exact</span> <span class="bp">⟨_</span><span class="o">,</span> <span class="n">measure_wf</span> <span class="n">length</span><span class="bp">⟩</span><span class="o">]}</span>
</pre></div>

#### [ Kevin Buzzard (Apr 04 2018 at 21:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/palindromes/near/124638434):
<p>Yes, I did it too. Here's the reason I was asking: Q1(c) of <a href="http://www.olympiad.org.uk/papers/2015/bio/round_one.html" target="_blank" title="http://www.olympiad.org.uk/papers/2015/bio/round_one.html">http://www.olympiad.org.uk/papers/2015/bio/round_one.html</a></p>

#### [ Kevin Buzzard (Apr 04 2018 at 21:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/palindromes/near/124638445):
<p>My son wrote code to do Q1(a) so I thought I'd write code to do Q1(c) because I thought that the idea of writing code to do 1c would be interesting to him.</p>

#### [ Kevin Buzzard (Apr 04 2018 at 22:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/palindromes/near/124639841):
<p>FWIW:</p>
<div class="codehilite"><pre><span></span><span class="kn">import</span> <span class="n">data</span><span class="bp">.</span><span class="n">list</span>
<span class="kn">open</span> <span class="n">list</span>
<span class="n">universes</span> <span class="n">u</span> <span class="n">v</span>
<span class="kn">variables</span> <span class="o">{</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">}</span> <span class="o">{</span><span class="n">β</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">v</span><span class="o">}</span>
<span class="kn">inductive</span> <span class="n">palindrome</span> <span class="o">:</span> <span class="n">list</span> <span class="n">α</span> <span class="bp">→</span> <span class="kt">Prop</span>
<span class="bp">|</span> <span class="n">nil</span> <span class="o">:</span> <span class="n">palindrome</span> <span class="o">[]</span>
<span class="bp">|</span> <span class="n">one</span> <span class="o">:</span> <span class="bp">∀</span> <span class="n">a</span><span class="o">,</span> <span class="n">palindrome</span> <span class="o">[</span><span class="n">a</span><span class="o">]</span>
<span class="bp">|</span> <span class="n">cons</span> <span class="o">:</span> <span class="bp">∀</span> <span class="n">a</span> <span class="n">L</span><span class="o">,</span> <span class="n">palindrome</span> <span class="n">L</span> <span class="bp">→</span> <span class="n">palindrome</span> <span class="o">((</span><span class="n">a</span> <span class="bp">::</span> <span class="n">L</span><span class="o">)</span> <span class="bp">++</span> <span class="o">[</span><span class="n">a</span><span class="o">])</span>

<span class="kn">namespace</span> <span class="n">palindrome</span>
<span class="kn">open</span> <span class="n">palindrome</span>

<span class="n">def</span> <span class="n">is_rev_self</span> <span class="o">(</span><span class="n">L</span> <span class="o">:</span> <span class="n">list</span> <span class="n">β</span><span class="o">)</span> <span class="o">:</span> <span class="kt">Prop</span> <span class="o">:=</span> <span class="n">L</span> <span class="bp">=</span> <span class="n">reverse</span> <span class="n">L</span>

<span class="kn">lemma</span> <span class="n">rev_aux</span> <span class="o">(</span><span class="n">a</span> <span class="n">b</span> <span class="o">:</span> <span class="n">β</span><span class="o">)</span> <span class="o">(</span><span class="n">L</span> <span class="o">:</span> <span class="n">list</span> <span class="n">β</span><span class="o">)</span> <span class="o">:</span> <span class="n">is_rev_self</span> <span class="o">(</span><span class="n">a</span> <span class="bp">::</span> <span class="o">(</span><span class="n">L</span> <span class="bp">++</span> <span class="o">[</span><span class="n">b</span><span class="o">]))</span> <span class="bp">→</span> <span class="n">a</span> <span class="bp">=</span> <span class="n">b</span> <span class="bp">∧</span> <span class="n">is_rev_self</span> <span class="n">L</span> <span class="o">:=</span>
<span class="k">begin</span>
<span class="n">unfold</span> <span class="n">is_rev_self</span><span class="o">,</span><span class="n">intro</span> <span class="n">H</span><span class="o">,</span>
<span class="n">rw</span> <span class="n">reverse_cons&#39;</span> <span class="n">at</span> <span class="n">H</span><span class="o">,</span>
<span class="n">rw</span> <span class="n">reverse_append</span> <span class="n">at</span> <span class="n">H</span><span class="o">,</span>
<span class="k">have</span> <span class="n">H2</span> <span class="o">:</span> <span class="n">a</span> <span class="bp">=</span> <span class="n">b</span> <span class="bp">∧</span> <span class="n">L</span> <span class="bp">++</span> <span class="o">[</span><span class="n">b</span><span class="o">]</span> <span class="bp">=</span> <span class="n">reverse</span> <span class="n">L</span> <span class="bp">++</span> <span class="o">[</span><span class="n">a</span><span class="o">],</span>
  <span class="n">simpa</span> <span class="kn">using</span> <span class="n">H</span><span class="o">,</span>
<span class="n">split</span><span class="o">,</span><span class="n">exact</span> <span class="n">H2</span><span class="bp">.</span><span class="mi">1</span><span class="o">,</span>
<span class="n">rw</span> <span class="n">H2</span><span class="bp">.</span><span class="mi">1</span> <span class="n">at</span> <span class="n">H2</span><span class="o">,</span>
<span class="k">have</span> <span class="n">H3</span> <span class="o">:=</span> <span class="n">H2</span><span class="bp">.</span><span class="mi">2</span><span class="o">,</span>
<span class="n">rw</span> <span class="n">H2</span><span class="bp">.</span><span class="mi">1</span> <span class="n">at</span> <span class="n">H3</span><span class="o">,</span>
<span class="n">exact</span> <span class="n">append_inj_left&#39;</span> <span class="n">H3</span> <span class="n">rfl</span><span class="o">,</span>
<span class="kn">end</span>


<span class="kn">theorem</span> <span class="n">palindrome_of_is_rev_self</span><span class="bp">.</span><span class="n">aux</span> <span class="o">(</span><span class="n">n</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">)</span> <span class="o">:</span> <span class="bp">∀</span> <span class="n">L</span> <span class="o">:</span> <span class="n">list</span> <span class="n">β</span><span class="o">,</span> <span class="n">L</span><span class="bp">.</span><span class="n">length</span> <span class="bp">=</span> <span class="n">n</span> <span class="bp">→</span> <span class="n">is_rev_self</span> <span class="n">L</span> <span class="bp">→</span> <span class="n">palindrome</span> <span class="n">L</span> <span class="o">:=</span>
<span class="k">begin</span>
  <span class="n">unfold</span> <span class="n">is_rev_self</span><span class="o">,</span>
  <span class="n">apply</span> <span class="n">nat</span><span class="bp">.</span><span class="n">strong_induction_on</span> <span class="n">n</span><span class="o">,</span>
  <span class="n">clear</span> <span class="n">n</span><span class="o">,</span><span class="n">intro</span> <span class="n">n</span><span class="o">,</span>
  <span class="n">intro</span> <span class="n">IH</span><span class="o">,</span>
  <span class="n">intro</span> <span class="n">L</span><span class="o">,</span>
  <span class="n">cases</span> <span class="n">L</span> <span class="k">with</span> <span class="n">a</span> <span class="n">M</span><span class="o">,</span>
  <span class="o">{</span> <span class="n">intros</span> <span class="bp">_</span> <span class="bp">_</span><span class="o">,</span><span class="n">exact</span> <span class="n">nil</span> <span class="o">},</span>
  <span class="n">apply</span> <span class="n">list</span><span class="bp">.</span><span class="n">reverse_rec_on</span> <span class="n">M</span><span class="o">,</span>
  <span class="o">{</span> <span class="n">intros</span> <span class="bp">_</span> <span class="bp">_</span><span class="o">,</span> <span class="n">exact</span> <span class="n">one</span> <span class="n">a</span><span class="o">},</span>
  <span class="n">intros</span> <span class="n">L</span> <span class="n">b</span> <span class="n">X</span><span class="o">,</span><span class="n">clear</span> <span class="n">X</span><span class="o">,</span>
  <span class="n">intros</span> <span class="n">HLL</span> <span class="n">HRL</span><span class="o">,</span>
  <span class="k">have</span> <span class="n">H2</span> <span class="o">:=</span> <span class="n">rev_aux</span> <span class="n">a</span> <span class="n">b</span> <span class="n">L</span> <span class="n">HRL</span><span class="o">,</span>
  <span class="n">rw</span> <span class="err">←</span><span class="n">cons_append</span><span class="o">,</span>
  <span class="n">rw</span> <span class="n">H2</span><span class="bp">.</span><span class="mi">1</span><span class="o">,</span>
  <span class="n">apply</span> <span class="n">cons</span><span class="o">,</span>
  <span class="k">have</span> <span class="n">H3</span> <span class="o">:</span> <span class="mi">1</span> <span class="bp">+</span> <span class="o">(</span><span class="mi">1</span> <span class="bp">+</span> <span class="n">length</span> <span class="n">L</span><span class="o">)</span> <span class="bp">=</span> <span class="n">n</span><span class="o">,</span>
    <span class="n">simpa</span> <span class="kn">using</span> <span class="n">HLL</span><span class="o">,</span>
  <span class="n">rw</span> <span class="o">[</span><span class="err">←</span><span class="n">add_assoc</span><span class="o">,</span><span class="n">add_comm</span><span class="o">]</span> <span class="n">at</span> <span class="n">H3</span><span class="o">,</span>
  <span class="k">have</span> <span class="n">H4</span> <span class="o">:</span> <span class="n">length</span> <span class="n">L</span> <span class="bp">&lt;</span> <span class="n">n</span><span class="o">,</span>
  <span class="n">rw</span> <span class="err">←</span><span class="n">H3</span><span class="o">,</span><span class="n">exact</span> <span class="n">nat</span><span class="bp">.</span><span class="n">lt_add_of_zero_lt_left</span> <span class="o">(</span><span class="n">length</span> <span class="n">L</span><span class="o">)</span> <span class="mi">2</span> <span class="n">dec_trivial</span><span class="o">,</span>
  <span class="n">exact</span> <span class="n">IH</span> <span class="o">(</span><span class="n">length</span> <span class="n">L</span><span class="o">)</span> <span class="n">H4</span> <span class="n">L</span> <span class="n">rfl</span> <span class="n">H2</span><span class="bp">.</span><span class="mi">2</span><span class="o">,</span>
<span class="kn">end</span>

<span class="kn">theorem</span> <span class="n">palindrome_of_rev_self</span> <span class="o">(</span><span class="n">L</span> <span class="o">:</span> <span class="n">list</span> <span class="n">α</span><span class="o">)</span> <span class="o">:</span> <span class="n">is_rev_self</span> <span class="n">L</span> <span class="bp">→</span> <span class="n">palindrome</span> <span class="n">L</span> <span class="o">:=</span>
  <span class="n">palindrome_of_is_rev_self</span><span class="bp">.</span><span class="n">aux</span> <span class="o">(</span><span class="n">length</span> <span class="n">L</span><span class="o">)</span> <span class="n">L</span> <span class="n">rfl</span>

<span class="kn">theorem</span> <span class="n">is_rev_self_of_palindrome</span> <span class="o">(</span><span class="n">L</span> <span class="o">:</span> <span class="n">list</span> <span class="n">α</span><span class="o">)</span> <span class="o">:</span> <span class="n">palindrome</span> <span class="n">L</span> <span class="bp">→</span> <span class="n">is_rev_self</span> <span class="n">L</span> <span class="o">:=</span>
<span class="k">begin</span>
  <span class="n">intro</span> <span class="n">H</span><span class="o">,</span>
  <span class="n">induction</span> <span class="n">H</span> <span class="k">with</span> <span class="n">a</span> <span class="n">b</span> <span class="n">M</span> <span class="n">HPM</span> <span class="n">HRM</span><span class="o">,</span>
  <span class="o">{</span> <span class="n">unfold</span> <span class="n">is_rev_self</span><span class="o">,</span><span class="n">refl</span><span class="o">},</span>
  <span class="o">{</span> <span class="n">unfold</span> <span class="n">is_rev_self</span><span class="o">,</span><span class="n">refl</span><span class="o">},</span>
  <span class="o">{</span> <span class="n">unfold</span> <span class="n">is_rev_self</span><span class="o">,</span><span class="n">unfold</span> <span class="n">is_rev_self</span> <span class="n">at</span> <span class="n">HRM</span><span class="o">,</span>
    <span class="n">rw</span> <span class="n">reverse_append</span><span class="o">,</span>
    <span class="n">rw</span> <span class="n">reverse_singleton</span><span class="o">,</span>
    <span class="n">rw</span> <span class="n">cons_append</span><span class="o">,</span>
    <span class="n">rw</span> <span class="n">reverse_cons&#39;</span><span class="o">,</span>
    <span class="n">rw</span> <span class="err">←</span><span class="n">HRM</span><span class="o">,</span>
    <span class="n">simp</span><span class="o">,</span>
  <span class="o">}</span>
<span class="kn">end</span>
<span class="kn">end</span> <span class="n">palindrome</span>
</pre></div>

#### [ Kevin Buzzard (Apr 04 2018 at 22:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/palindromes/near/124639896):
<p>My code didn't get highlighted. Possibly because the FWIW was in the same post.</p>

#### [ Kevin Buzzard (Apr 04 2018 at 22:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/palindromes/near/124639900):
<p>No wait Chris also didn't post a pure code post</p>

#### [ Kevin Buzzard (Apr 04 2018 at 22:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/palindromes/near/124639914):
<p>Aah got it, you have to write <code>lean</code> after the three backticks</p>

#### [ Kevin Buzzard (Apr 04 2018 at 22:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/palindromes/near/124640132):
<p>Oh Chris you didn't use strong induction for the main theorem! (<code>palindrome_of_eq_reverse</code>). I made an aux lemma saying "forall n, if list length is n then blah" and applied strong induction to n, and then deduced the statement we wanted as a trivial corollary.</p>

#### [ Chris Hughes (Apr 04 2018 at 22:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/palindromes/near/124640484):
<p>I did use strong induction, note <code> using_well_founded {rel_tac := λ _ _, ``[exact ⟨_, measure_wf length⟩]} </code></p>
<p>I also did question 1a, although in 2^(2^n) time, so I might lose some points for that.</p>
<div class="codehilite"><pre><span></span><span class="kn">instance</span> <span class="o">[</span><span class="n">decidable_eq</span> <span class="n">α</span><span class="o">]</span> <span class="o">(</span><span class="n">l</span> <span class="o">:</span> <span class="n">list</span> <span class="n">α</span><span class="o">)</span> <span class="o">:</span> <span class="n">decidable</span> <span class="o">(</span><span class="n">palindrome</span> <span class="n">l</span><span class="o">)</span> <span class="o">:=</span>
<span class="n">decidable_of_iff</span> <span class="o">(</span><span class="n">l</span> <span class="bp">=</span> <span class="n">l</span><span class="bp">.</span><span class="n">reverse</span><span class="o">)</span> <span class="bp">⟨λ</span> <span class="n">h</span><span class="o">,</span> <span class="n">palindrome_of_eq_reverse</span> <span class="n">h</span><span class="o">,</span> <span class="bp">λ</span> <span class="n">h</span><span class="o">,</span> <span class="n">eq_reverse_of_palindrome</span> <span class="n">h</span><span class="bp">⟩</span>

<span class="n">def</span>  <span class="n">block_palindromes</span> <span class="o">(</span><span class="n">l</span> <span class="o">:</span> <span class="n">list</span> <span class="n">α</span><span class="o">)</span> <span class="o">[</span><span class="n">decidable_eq</span> <span class="n">α</span><span class="o">]</span> <span class="o">:=</span> <span class="o">(</span><span class="n">sublists</span> <span class="o">(</span><span class="n">sublists</span> <span class="n">l</span><span class="o">))</span><span class="bp">.</span><span class="n">filter</span>
<span class="o">(</span><span class="bp">λ</span> <span class="n">m</span> <span class="o">:</span> <span class="n">list</span> <span class="o">(</span><span class="n">list</span> <span class="n">α</span><span class="o">),</span> <span class="n">palindrome</span> <span class="n">m</span> <span class="bp">∧</span> <span class="n">m</span><span class="bp">.</span><span class="n">foldl</span> <span class="o">(</span><span class="bp">++</span><span class="o">)</span> <span class="n">nil</span> <span class="bp">=</span> <span class="n">l</span><span class="o">)</span>
</pre></div>

#### [ Mario Carneiro (Apr 04 2018 at 23:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/palindromes/near/124641990):
<p>haha that solution</p>

#### [ Mario Carneiro (Apr 04 2018 at 23:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/palindromes/near/124642031):
<p>You should write the deterministic bogosort, which enumerates permutations until it finds the sorted one</p>

#### [ Kevin Buzzard (Apr 04 2018 at 23:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/palindromes/near/124642035):
<p>The mark scheme is just a bunch of tests, and you have to pass each one in under a second to get the marks.</p>

#### [ Kevin Buzzard (Apr 05 2018 at 00:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/palindromes/near/124644819):
<p>So I finished the proof that the word has to have an even number of letters.</p>

#### [ Kevin Buzzard (Apr 05 2018 at 00:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/palindromes/near/124644823):
<p>My proof was 240 lines, longer than my son's program to do 1(a).</p>

#### [ Kevin Buzzard (Apr 05 2018 at 00:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/palindromes/near/124644873):
<p>But I had to develop some concepts from scratch; in a parallel universe they would have already been in some library.</p>

#### [ Kevin Buzzard (Apr 05 2018 at 00:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/palindromes/near/124644889):
<p>It was quite an interesting task. The question is about the following definition:</p>

#### [ Kevin Buzzard (Apr 05 2018 at 00:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/palindromes/near/124644891):
<div class="codehilite"><pre><span></span><span class="kn">definition</span>  <span class="n">listunfold</span> <span class="o">:</span> <span class="n">list</span> <span class="o">(</span><span class="n">list</span> <span class="n">α</span><span class="o">)</span> <span class="bp">→</span> <span class="n">list</span> <span class="n">α</span>
<span class="bp">|</span> <span class="o">[]</span> <span class="o">:=</span> <span class="o">[]</span>
<span class="bp">|</span> <span class="o">(</span><span class="n">a</span> <span class="bp">::</span> <span class="n">L</span><span class="o">)</span> <span class="o">:=</span> <span class="n">a</span> <span class="bp">++</span> <span class="o">(</span><span class="n">listunfold</span> <span class="n">L</span><span class="o">)</span>
</pre></div>

#### [ Kevin Buzzard (Apr 05 2018 at 00:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/palindromes/near/124644939):
<p>but then I had to write <code>listunfold_append : listunfold (G1 ++ G2) = listunfold G1 ++ listunfold G2</code> and <code>listunfold_singleton</code>and so on</p>

#### [ Kevin Buzzard (Apr 05 2018 at 00:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/palindromes/near/124644960):
<p>And similarly for <code>palindrome</code> (the inductive prop) I had to prove palindrome iff L = reverse L</p>

#### [ Chris Hughes (Apr 05 2018 at 00:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/palindromes/near/124644967):
<p>Listunfold could also be defined as a fold. Then those two lemmas are probably there already because of associativity</p>

#### [ Kevin Buzzard (Apr 05 2018 at 00:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/palindromes/near/124645013):
<p>Is that right?</p>

#### [ Kevin Buzzard (Apr 05 2018 at 00:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/palindromes/near/124645022):
<p>I feel like if I defined it as a fold then I would then have to prove the two things I've used for my definition immediately afterwards</p>

#### [ Chris Hughes (Apr 05 2018 at 00:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/palindromes/near/124645024):
<p>Not in that exact form, but they'd be quite easy.</p>

#### [ Kevin Buzzard (Apr 05 2018 at 00:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/palindromes/near/124645025):
<p>and then the same proof for my append and singleton :-)</p>

#### [ Kevin Buzzard (Apr 05 2018 at 00:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/palindromes/near/124645031):
<p>Oh everything was easy, but of course because this was recreational I did it all in tactic mode so my proofs go on for ages :-)</p>

#### [ Chris Hughes (Apr 05 2018 at 00:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/palindromes/near/124645032):
<p>Those two things are lemmas about fold probably</p>

#### [ Kevin Buzzard (Apr 05 2018 at 00:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/palindromes/near/124645079):
<p>You might well be right. I feel like I know enough Lean to write the definitions and basic properties of these new concepts like listunfold or palindrome</p>

#### [ Kevin Buzzard (Apr 05 2018 at 00:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/palindromes/near/124645080):
<p>but</p>

#### [ Kevin Buzzard (Apr 05 2018 at 00:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/palindromes/near/124645084):
<p>I feel like if I really knew everything that was already there, properly, then I would write things far more efficiently.</p>

#### [ Chris Hughes (Apr 05 2018 at 00:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/palindromes/near/124645097):
<p>It's not about knowing what's there, it's knowing what's probably there.</p>

#### [ Mario Carneiro (Apr 05 2018 at 03:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/palindromes/near/124650234):
<p>Your <code>listunfold</code> is defined in core and proven in mathlib, by the name <code>list.join</code>. It is the monad "flattening" operation for lists</p>


{% endraw %}
