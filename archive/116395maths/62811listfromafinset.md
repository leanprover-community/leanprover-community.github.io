---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/62811listfromafinset.html
---

## Stream: [maths](https://leanprover-community.github.io/archive/116395maths/index.html)
### Topic: [list from a finset](https://leanprover-community.github.io/archive/116395maths/62811listfromafinset.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Sean Leather (Apr 13 2018 at 14:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/list%20from%20a%20finset/near/125032331):
<p>Is there a way to get a <code>list</code> from a <code>finset</code> without using <code>finset.sort</code> or writing my own recursive function on <code>finset</code>?</p>

#### [ Kenny Lau (Apr 13 2018 at 14:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/list%20from%20a%20finset/near/125032374):
<p>but <code>finset</code> is a subquotient of <code>list</code></p>

#### [ Kenny Lau (Apr 13 2018 at 14:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/list%20from%20a%20finset/near/125032377):
<p>and quotients can't be reversed</p>

#### [ Sean Leather (Apr 13 2018 at 14:39)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/list%20from%20a%20finset/near/125032390):
<p>That's right, so I couldn't use a recursive function anyway.</p>

#### [ Sean Leather (Apr 13 2018 at 14:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/list%20from%20a%20finset/near/125032522):
<p>Well, I suppose I could follow the <code>sort</code> example:</p>
<div class="codehilite"><pre><span></span><span class="n">def</span> <span class="n">finset</span><span class="bp">.</span><span class="n">sort</span> <span class="o">(</span><span class="n">s</span> <span class="o">:</span> <span class="n">finset</span> <span class="n">α</span><span class="o">)</span> <span class="o">:</span> <span class="n">list</span> <span class="n">α</span> <span class="o">:=</span> <span class="n">multiset</span><span class="bp">.</span><span class="n">sort</span> <span class="n">r</span> <span class="n">s</span><span class="bp">.</span><span class="mi">1</span>

<span class="n">def</span> <span class="n">multiset</span><span class="bp">.</span><span class="n">sort</span> <span class="o">(</span><span class="n">s</span> <span class="o">:</span> <span class="n">multiset</span> <span class="n">α</span><span class="o">)</span> <span class="o">:</span> <span class="n">list</span> <span class="n">α</span> <span class="o">:=</span>
<span class="n">quot</span><span class="bp">.</span><span class="n">lift_on</span> <span class="n">s</span> <span class="o">(</span><span class="n">merge_sort</span> <span class="n">r</span><span class="o">)</span> <span class="err">$</span> <span class="bp">λ</span> <span class="n">a</span> <span class="n">b</span> <span class="n">h</span><span class="o">,</span>
<span class="n">eq_of_sorted_of_perm</span> <span class="n">tr</span><span class="bp">.</span><span class="n">trans</span> <span class="n">an</span><span class="bp">.</span><span class="n">antisymm</span>
  <span class="o">((</span><span class="n">perm_merge_sort</span> <span class="bp">_</span> <span class="bp">_</span><span class="o">)</span><span class="bp">.</span><span class="n">trans</span> <span class="err">$</span> <span class="n">h</span><span class="bp">.</span><span class="n">trans</span> <span class="o">(</span><span class="n">perm_merge_sort</span> <span class="bp">_</span> <span class="bp">_</span><span class="o">)</span><span class="bp">.</span><span class="n">symm</span><span class="o">)</span>
  <span class="o">(</span><span class="n">sorted_merge_sort</span> <span class="n">r</span> <span class="n">to</span><span class="bp">.</span><span class="n">total</span> <span class="n">tr</span><span class="bp">.</span><span class="n">trans</span> <span class="bp">_</span><span class="o">)</span>
  <span class="o">(</span><span class="n">sorted_merge_sort</span> <span class="n">r</span> <span class="n">to</span><span class="bp">.</span><span class="n">total</span> <span class="n">tr</span><span class="bp">.</span><span class="n">trans</span> <span class="bp">_</span><span class="o">)</span>
</pre></div>

#### [ Sean Leather (Apr 13 2018 at 14:48)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/list%20from%20a%20finset/near/125032728):
<p>Ah, <code>fold</code>?</p>

#### [ Simon Hudon (Apr 13 2018 at 14:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/list%20from%20a%20finset/near/125032788):
<p>Why do you not want to sort it?</p>

#### [ Sean Leather (Apr 13 2018 at 14:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/list%20from%20a%20finset/near/125032790):
<p>Because I don't need a particular order.</p>

#### [ Kenny Lau (Apr 13 2018 at 14:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/list%20from%20a%20finset/near/125032791):
<p>then it's uncomputable</p>

#### [ Simon Hudon (Apr 13 2018 at 14:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/list%20from%20a%20finset/near/125032857):
<p>Right but them being in a particular order can't be harmful, is it? Is it that you care about the performances?</p>

#### [ Sean Leather (Apr 13 2018 at 14:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/list%20from%20a%20finset/near/125032874):
<p>It requires adding an ordering constraint to the elements that I don't need or want.</p>

#### [ Simon Hudon (Apr 13 2018 at 14:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/list%20from%20a%20finset/near/125032878):
<p>What you could do is compute on the list before taking it out of the quotient and proving that the result is independent of order</p>

#### [ Sean Leather (Apr 13 2018 at 14:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/list%20from%20a%20finset/near/125032951):
<div class="codehilite"><pre><span></span><span class="n">def</span> <span class="n">multiset</span><span class="bp">.</span><span class="n">foldr</span> <span class="o">(</span><span class="n">f</span> <span class="o">:</span> <span class="n">α</span> <span class="bp">→</span> <span class="n">β</span> <span class="bp">→</span> <span class="n">β</span><span class="o">)</span> <span class="o">(</span><span class="n">H</span> <span class="o">:</span> <span class="n">left_commutative</span> <span class="n">f</span><span class="o">)</span> <span class="o">(</span><span class="n">b</span> <span class="o">:</span> <span class="n">β</span><span class="o">)</span> <span class="o">(</span><span class="n">s</span> <span class="o">:</span> <span class="n">multiset</span> <span class="n">α</span><span class="o">)</span> <span class="o">:</span> <span class="n">β</span> <span class="o">:=</span>
<span class="n">quot</span><span class="bp">.</span><span class="n">lift_on</span> <span class="n">s</span> <span class="o">(</span><span class="bp">λ</span> <span class="n">l</span><span class="o">,</span> <span class="n">foldr</span> <span class="n">f</span> <span class="n">b</span> <span class="n">l</span><span class="o">)</span> <span class="o">(</span><span class="bp">λ</span> <span class="n">l₁</span> <span class="n">l₂</span> <span class="n">p</span><span class="o">,</span> <span class="n">foldr_eq_of_perm</span> <span class="n">H</span> <span class="n">p</span> <span class="n">b</span><span class="o">)</span>
</pre></div>

#### [ Kenny Lau (Apr 13 2018 at 14:56)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/list%20from%20a%20finset/near/125033001):
<blockquote>
<p>It requires adding an ordering constraint to the elements that I don't need or want.</p>
</blockquote>
<p>otherwise it won't be a well-defined function</p>

#### [ Simon Hudon (Apr 13 2018 at 15:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/list%20from%20a%20finset/near/125033199):
<blockquote>
<div class="codehilite"><pre><span></span><span class="n">def</span> <span class="n">multiset</span><span class="bp">.</span><span class="n">foldr</span> <span class="o">(</span><span class="n">f</span> <span class="o">:</span> <span class="n">α</span> <span class="bp">→</span> <span class="n">β</span> <span class="bp">→</span> <span class="n">β</span><span class="o">)</span> <span class="o">(</span><span class="n">H</span> <span class="o">:</span> <span class="n">left_commutative</span> <span class="n">f</span><span class="o">)</span> <span class="o">(</span><span class="n">b</span> <span class="o">:</span> <span class="n">β</span><span class="o">)</span> <span class="o">(</span><span class="n">s</span> <span class="o">:</span> <span class="n">multiset</span> <span class="n">α</span><span class="o">)</span> <span class="o">:</span> <span class="n">β</span> <span class="o">:=</span>
<span class="n">quot</span><span class="bp">.</span><span class="n">lift_on</span> <span class="n">s</span> <span class="o">(</span><span class="bp">λ</span> <span class="n">l</span><span class="o">,</span> <span class="n">foldr</span> <span class="n">f</span> <span class="n">b</span> <span class="n">l</span><span class="o">)</span> <span class="o">(</span><span class="bp">λ</span> <span class="n">l₁</span> <span class="n">l₂</span> <span class="n">p</span><span class="o">,</span> <span class="n">foldr_eq_of_perm</span> <span class="n">H</span> <span class="n">p</span> <span class="n">b</span><span class="o">)</span>
</pre></div>


</blockquote>
<p>Exactly. What are you trying to compute?</p>

#### [ Sean Leather (Apr 13 2018 at 15:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/list%20from%20a%20finset/near/125033557):
<p>So, <code>finset.fold</code> doesn't work because it requires the append operator to be commutative, which it is not:</p>
<div class="codehilite"><pre><span></span><span class="n">def</span> <span class="n">to_list</span> <span class="o">:</span> <span class="n">finset</span> <span class="n">α</span> <span class="bp">→</span> <span class="n">list</span> <span class="n">α</span> <span class="o">:=</span>
  <span class="n">fold</span> <span class="o">(</span><span class="bp">++</span><span class="o">)</span> <span class="o">[]</span> <span class="o">(</span><span class="bp">λ</span> <span class="n">a</span><span class="o">,</span> <span class="o">[</span><span class="n">a</span><span class="o">])</span>

<span class="err">⊢</span> <span class="n">is_commutative</span> <span class="o">(</span><span class="n">list</span> <span class="n">α</span><span class="o">)</span> <span class="n">append</span>
</pre></div>

#### [ Kenny Lau (Apr 13 2018 at 15:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/list%20from%20a%20finset/near/125033566):
<p>right, because the function you're trying to define isn't well-defined</p>

#### [ Sean Leather (Apr 13 2018 at 15:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/list%20from%20a%20finset/near/125033577):
<p>Since <code>finset</code> is a quotient on list permutations, is it not possible to choose an arbitrary permutation?</p>

#### [ Kenny Lau (Apr 13 2018 at 15:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/list%20from%20a%20finset/near/125033582):
<p>no, that's what quotient is</p>

#### [ Kenny Lau (Apr 13 2018 at 15:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/list%20from%20a%20finset/near/125033583):
<p>it needs to work for any permutation</p>

#### [ Kenny Lau (Apr 13 2018 at 15:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/list%20from%20a%20finset/near/125033643):
<p>your functions need to be well-defined</p>

#### [ Kenny Lau (Apr 13 2018 at 15:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/list%20from%20a%20finset/near/125033652):
<p>if {2,1,3} gives [2,1,3] and {1,2,3} gives [1,2,3], then it isn't a well-defined function</p>

#### [ Chris Hughes (Apr 13 2018 at 15:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/list%20from%20a%20finset/near/125033654):
<p><code>quotient.out</code> works, but that's noncomputable</p>

#### [ Chris Hughes (Apr 13 2018 at 15:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/list%20from%20a%20finset/near/125033665):
<p><code>quot.unquot</code> also works, but you can't use that in a proof, because it implies false.</p>

#### [ Kenny Lau (Apr 13 2018 at 15:14)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/list%20from%20a%20finset/near/125033708):
<p>in fact, if your function did that, then I can prove false</p>

#### [ Kenny Lau (Apr 13 2018 at 15:14)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/list%20from%20a%20finset/near/125033714):
<p>because {2,1,3} and {1,2,3} are equal</p>

#### [ Sean Leather (Apr 13 2018 at 15:17)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/list%20from%20a%20finset/near/125033803):
<p><span class="user-mention" data-user-id="110064">@Kenny Lau</span> Right, so your point is that the function has to produce the same permutation for any set, and that's why sorting is necessary.</p>

#### [ Simon Hudon (Apr 13 2018 at 15:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/list%20from%20a%20finset/near/125034441):
<p>Right. But the other idea is: what are you going to do with that list? If the function that uses the list works the same for all permutation, you don't need to care about sorting the list. You just need to make sure that when you use the list, you produce the same results regardless of order</p>

#### [ Sean Leather (Apr 13 2018 at 15:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/list%20from%20a%20finset/near/125034446):
<p>In the end, I want a list with certain properties. I thought using a finset to construct it would be simpler (since that function is easier), but it appears that I should just construct the list directly. I'm going to try using <code>list.to_finset</code> to simplify the property testing during construction in an auxiliary function and then extract the list-specific properties from the finset properties in a wrapper.</p>

#### [ Simon Hudon (Apr 13 2018 at 15:36)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/list%20from%20a%20finset/near/125034447):
<p>Instead of going inside the <code>quot</code> to extract a list, go inside to do more of your computations</p>

#### [ Kevin Buzzard (Apr 13 2018 at 15:48)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/list%20from%20a%20finset/near/125034894):
<p>Sean -- you want your function to be computable?</p>

#### [ Sean Leather (Apr 19 2018 at 08:30)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/list%20from%20a%20finset/near/125291437):
<p>To catch up on this thread, I was trying to figure out how to use</p>
<div class="codehilite"><pre><span></span><span class="n">def</span> <span class="n">fresh_finset</span> <span class="o">(</span><span class="n">s₁</span> <span class="o">:</span> <span class="n">finset</span> <span class="n">α</span><span class="o">)</span> <span class="o">:</span> <span class="bp">∀</span> <span class="n">n</span><span class="o">,</span> <span class="err">Σ&#39;</span> <span class="o">(</span><span class="n">s₂</span> <span class="o">:</span> <span class="n">finset</span> <span class="n">α</span><span class="o">),</span> <span class="n">card</span> <span class="n">s₂</span> <span class="bp">=</span> <span class="n">n</span> <span class="bp">∧</span> <span class="n">s₂</span> <span class="err">∩</span> <span class="n">s₁</span> <span class="bp">=</span> <span class="err">∅</span>
</pre></div>


<p>in the definition of</p>
<div class="codehilite"><pre><span></span><span class="n">def</span> <span class="n">fresh_list</span> <span class="o">(</span><span class="n">s</span> <span class="o">:</span> <span class="n">finset</span> <span class="n">α</span><span class="o">)</span> <span class="o">:</span> <span class="bp">∀</span> <span class="n">n</span><span class="o">,</span> <span class="err">Σ&#39;</span> <span class="o">(</span><span class="n">l</span> <span class="o">:</span> <span class="n">list</span> <span class="n">α</span><span class="o">),</span> <span class="n">l</span><span class="bp">.</span><span class="n">length</span> <span class="bp">=</span> <span class="n">n</span> <span class="bp">∧</span> <span class="n">l</span><span class="bp">.</span><span class="n">nodup</span> <span class="bp">∧</span> <span class="n">l</span><span class="bp">.</span><span class="n">to_finset</span> <span class="err">∩</span> <span class="n">s</span> <span class="bp">=</span> <span class="err">∅</span>
</pre></div>


<p>but, as has been pointed out to me, this is not possible without adding an additional constraint on <code>α</code>. In the end, I wrote <code>fresh_list</code> from scratch. It wasn't as difficult as I thought, and it shares a proof structure with <code>fresh_finset</code>.</p>
<p>See the <a href="https://github.com/spl/tts/blob/010faf776c4fda5a376994a06cd76dd0784f3faf/src/data/finset/fresh.lean#L19-L50" target="_blank" title="https://github.com/spl/tts/blob/010faf776c4fda5a376994a06cd76dd0784f3faf/src/data/finset/fresh.lean#L19-L50">source</a> for the definitions.</p>
<p>Kevin: Yes, I want a computable definition.</p>

#### [ Mario Carneiro (Apr 19 2018 at 08:36)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/list%20from%20a%20finset/near/125291609):
<p>I agree that it is best to write the list definition directly in this case. I think it would be better to have the fresh list separate from the properties though</p>

#### [ Sean Leather (Apr 19 2018 at 08:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/list%20from%20a%20finset/near/125291625):
<p>How so?</p>

#### [ Mario Carneiro (Apr 19 2018 at 08:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/list%20from%20a%20finset/near/125291630):
<p>It makes the code path a bit more obvious</p>

#### [ Mario Carneiro (Apr 19 2018 at 08:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/list%20from%20a%20finset/near/125291682):
<p>I always worry that the match and such will add extra overhead</p>

#### [ Mario Carneiro (Apr 19 2018 at 08:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/list%20from%20a%20finset/near/125291688):
<p>it's not clear to me whether it is in fact optimized away</p>

#### [ Sean Leather (Apr 19 2018 at 08:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/list%20from%20a%20finset/near/125291689):
<p>What type signature would you want?</p>

#### [ Mario Carneiro (Apr 19 2018 at 08:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/list%20from%20a%20finset/near/125291854):
<div class="codehilite"><pre><span></span>class has_fresh (α : Type*) :=
(fresh : finset α → α)
(fresh_not_mem : ∀ s, fresh s ∉ s)

def fresh_list (s : finset α) : nat → list α
| 0 := []
| (n+1) := let l := fresh_list n in fresh (l.to_finset ∪ s) :: l

theorem fresh_list_length (s : finset α) : ∀ n, (fresh_list s n).length = n

theorem fresh_list_nodup_disjoint (s : finset α) :
  ∀ n, (fresh_list s n).nodup ∧ (fresh_list s n).to_finset ∩ s = ∅
</pre></div>


<p>I conjoin the last two only because I think the proof is by mutual recursion</p>

#### [ Sean Leather (Apr 19 2018 at 08:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/list%20from%20a%20finset/near/125291994):
<p>Ah, I see what you mean. You're talking about splitting the methods of the <code>class</code>. Yeah, that seems fine, assuming it works.</p>

#### [ Mario Carneiro (Apr 19 2018 at 08:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/list%20from%20a%20finset/near/125292003):
<p>By the way, it is conceivable that <code>fresh</code> in the typeclass will be difficult to define, since it enforces that the fresh element not depend on the order of the input list</p>

#### [ Sean Leather (Apr 19 2018 at 09:36)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/list%20from%20a%20finset/near/125293488):
<blockquote>
<p>By the way, it is conceivable that <code>fresh</code> in the typeclass will be difficult to define, since it enforces that the fresh element not depend on the order of the input list</p>
</blockquote>
<p><span class="user-mention" data-user-id="110049">@Mario Carneiro</span> I don't follow. I'm guessing you mean it's difficult to define <code>fresh</code> for instances of <code>has_fresh</code>. But what “input list”? <code>has_fresh</code> only depends on the element of the <code>finset</code>.</p>
<p>You could, of course, define different functions to produce a fresh element from a <code>list</code> or a fresh element from a <code>finset</code> with a required ordering to the element. Nonetheless, it is possible to define a <code>has_fresh</code> instance for <code>nat</code> and other infinite types for which it is possible to find an extreme, and <code>has_fresh</code> does not impose an ordering constraint that is not always needed.</p>

#### [ Mario Carneiro (Apr 19 2018 at 09:39)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/list%20from%20a%20finset/near/125293581):
<p>I mean that to implement <code>fresh</code> on a type <code>A</code>, you need to define a function <code>list A -&gt; A</code>, and then lift it to a function <code>finset A -&gt; A</code>, meaning that the original function must map <code>[a, b]</code> and <code>[b, a]</code> to the same fresh value <code>c</code>. Depending on <code>A</code>, that may not be convenient to do, for example if you hash the list or something to generate a disambiguator</p>

#### [ Sean Leather (Apr 19 2018 at 13:31)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/list%20from%20a%20finset/near/125301276):
<blockquote>
<p>I think it would be better to have the fresh list separate from the properties though</p>
</blockquote>
<p><span class="user-mention" data-user-id="110049">@Mario Carneiro</span> This was a good suggestion. The <a href="https://github.com/spl/tts/blob/84267eb8dac118884ffb8de2f77fa3cfb3c397cd/src/data/finset/fresh.lean" target="_blank" title="https://github.com/spl/tts/blob/84267eb8dac118884ffb8de2f77fa3cfb3c397cd/src/data/finset/fresh.lean">result</a> is much cleaner now.</p>
<blockquote>
<p>I mean that to implement <code>fresh</code> on a type <code>A</code>, you need to define a function <code>list A -&gt; A</code>, and then lift it to a function <code>finset A -&gt; A</code> [...]</p>
</blockquote>
<p>This is the part I don't follow. Why does one need to define a function <code>list A -&gt; A</code>? For <a href="https://github.com/spl/tts/blob/84267eb8dac118884ffb8de2f77fa3cfb3c397cd/src/data/finset/fresh.lean#L89-L142" target="_blank" title="https://github.com/spl/tts/blob/84267eb8dac118884ffb8de2f77fa3cfb3c397cd/src/data/finset/fresh.lean#L89-L142"><code>nat</code></a>, this isn't necessary. I conjecture that the same is true for other types.</p>

#### [ Mario Carneiro (Apr 19 2018 at 13:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/list%20from%20a%20finset/near/125301322):
<p>every function on <code>finset</code> is ultimately the <code>lift</code> of a function on <code>list</code></p>

#### [ Mario Carneiro (Apr 19 2018 at 13:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/list%20from%20a%20finset/near/125301327):
<p>I assume you used <code>finset.fold</code> or something to define the nat function</p>

#### [ Sean Leather (Apr 19 2018 at 13:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/list%20from%20a%20finset/near/125301330):
<p>True, but that doesn't mean I have to write the <code>list</code> function itself.</p>


{% endraw %}
