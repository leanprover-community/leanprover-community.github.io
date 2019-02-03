---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/53478naturalnumberhell.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [natural number hell](https://leanprover-community.github.io/archive/113488general/53478naturalnumberhell.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Patrick Massot (May 15 2018 at 09:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/natural%20number%20hell/near/126580412):
<p>I want to use <code>big.map</code> once I have the <code>map</code></p>

#### [ Patrick Massot (May 15 2018 at 09:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/natural%20number%20hell/near/126580421):
<p>I should push something so that you can see the context</p>

#### [ Mario Carneiro (May 15 2018 at 09:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/natural%20number%20hell/near/126580423):
<p>and then the <code>f</code> will be applied to the functions P and F... then what?</p>

#### [ Patrick Massot (May 15 2018 at 09:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/natural%20number%20hell/near/126580473):
<p><a href="https://github.com/PatrickMassot/bigop/blob/master/src/bigop.lean#L343" target="_blank" title="https://github.com/PatrickMassot/bigop/blob/master/src/bigop.lean#L343">https://github.com/PatrickMassot/bigop/blob/master/src/bigop.lean#L343</a></p>

#### [ Mario Carneiro (May 15 2018 at 09:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/natural%20number%20hell/near/126580484):
<p>wait, so you want the function <code>f</code> to be <code>i |-&gt; a+b-i</code>?</p>

#### [ Mario Carneiro (May 15 2018 at 09:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/natural%20number%20hell/near/126580489):
<p>then why are you mapping with something else in the lemma?</p>

#### [ Patrick Massot (May 15 2018 at 10:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/natural%20number%20hell/near/126580551):
<p>The problem is <code>reverse_range'</code> is about your <code>range'</code>, with start and length, and my goal is to have the maths range', with start and end</p>

#### [ Mario Carneiro (May 15 2018 at 10:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/natural%20number%20hell/near/126580614):
<p>Think of the problem in reverse. You want the theorem to say <code>a+b-i</code> at the end, so you want <code>f</code> to be <code>\lam i, a+b-i</code> when you apply <code>big.map</code>; the reverse theorem just adds a <code>list.reverse</code> on the set. So you should be proving <code>reverse (range' a b) = map (λ i, a+b-i) (range' a b)</code></p>

#### [ Mario Carneiro (May 15 2018 at 10:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/natural%20number%20hell/near/126580663):
<p>that is, without any algebraic rearrangement this is exactly what you need to fill the gap in the proof. Right?</p>

#### [ Patrick Massot (May 15 2018 at 10:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/natural%20number%20hell/near/126580668):
<p>Maybe I did so many detours I forgot the goal on the road</p>

#### [ Patrick Massot (May 15 2018 at 10:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/natural%20number%20hell/near/126580776):
<p>It seems I still need <code>a + (b + 1 - a) - i = a + b - i</code> (still assuming <code>i ∈ range' a (b + 1 - a)</code>)</p>

#### [ Mario Carneiro (May 15 2018 at 10:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/natural%20number%20hell/near/126580783):
<p>that's easy though, it is one of the <code>add_sub</code> theorems</p>

#### [ Patrick Massot (May 15 2018 at 10:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/natural%20number%20hell/near/126580785):
<p>I think we already saw that one</p>

#### [ Mario Carneiro (May 15 2018 at 10:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/natural%20number%20hell/near/126580824):
<p><code>nat.add_sub_cancel'</code>, which requires <code>a &lt;= b + 1</code></p>

#### [ Mario Carneiro (May 15 2018 at 10:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/natural%20number%20hell/near/126580852):
<p>Note that your assumption is sufficient to prove this, but only in a circuitous fashion, do you have any more direct evidence that <code>a &lt;= b+1</code>?</p>

#### [ Patrick Massot (May 15 2018 at 10:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/natural%20number%20hell/near/126580897):
<p>wait</p>

#### [ Mario Carneiro (May 15 2018 at 10:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/natural%20number%20hell/near/126580898):
<p>wait</p>

#### [ Mario Carneiro (May 15 2018 at 10:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/natural%20number%20hell/near/126580899):
<p>your theorem is nonsense</p>

#### [ Patrick Massot (May 15 2018 at 10:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/natural%20number%20hell/near/126580904):
<p>your theorem is nonsense</p>

#### [ Patrick Massot (May 15 2018 at 10:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/natural%20number%20hell/near/126580905):
<p><code>reverse (range' a b) = map (λ i, a+b-i) (range' a b)</code> is not true</p>

#### [ Patrick Massot (May 15 2018 at 10:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/natural%20number%20hell/near/126580910):
<p>I changed all statements so many times...</p>

#### [ Mario Carneiro (May 15 2018 at 10:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/natural%20number%20hell/near/126580927):
<p>I'm rather confused by the dual use of <code>range'</code> btw, could you give it another name? <code>range''</code> maybe?</p>

#### [ Patrick Massot (May 15 2018 at 10:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/natural%20number%20hell/near/126580953):
<p>You mean in the name of <code>reverse_range'</code>?</p>

#### [ Mario Carneiro (May 15 2018 at 10:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/natural%20number%20hell/near/126580963):
<p>I mean <code>range' a b = [a, ..., b]</code> vs <code>range' a b = [a, ..., a+b]</code></p>

#### [ Mario Carneiro (May 15 2018 at 10:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/natural%20number%20hell/near/126580968):
<p>pretty sure both functions are being called <code>range'</code></p>

#### [ Patrick Massot (May 15 2018 at 10:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/natural%20number%20hell/near/126580970):
<p>I don't redefine range'</p>

#### [ Mario Carneiro (May 15 2018 at 10:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/natural%20number%20hell/near/126580973):
<p>What is your definition?</p>

#### [ Patrick Massot (May 15 2018 at 10:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/natural%20number%20hell/near/126580974):
<p>I use your range'</p>

#### [ Mario Carneiro (May 15 2018 at 10:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/natural%20number%20hell/near/126581016):
<p>oh I see</p>

#### [ Patrick Massot (May 15 2018 at 10:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/natural%20number%20hell/near/126581018):
<p>But always in <code>range' a (b+1-a)</code></p>

#### [ Mario Carneiro (May 15 2018 at 10:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/natural%20number%20hell/near/126581019):
<p>In that case I need to state the theorem above with your bounds</p>

#### [ Mario Carneiro (May 15 2018 at 10:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/natural%20number%20hell/near/126581022):
<p><code>reverse (range' a (b+1-a)) = map (λ i, a+b-i) (range' a (b+1-a))</code></p>

#### [ Patrick Massot (May 15 2018 at 10:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/natural%20number%20hell/near/126581026):
<p>yes, this is correct</p>

#### [ Patrick Massot (May 15 2018 at 10:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/natural%20number%20hell/near/126581030):
<p>(not that I can prove it, but I can check it on examples)</p>

#### [ Patrick Massot (May 15 2018 at 10:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/natural%20number%20hell/near/126581093):
<p>But I wanted to deduce it from a version involving only  <code>range' a b</code> in LHS</p>

#### [ Patrick Massot (May 15 2018 at 10:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/natural%20number%20hell/near/126581097):
<p>hence the "arithmetic" trouble</p>

#### [ Patrick Massot (May 15 2018 at 10:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/natural%20number%20hell/near/126581150):
<p>But indeed this is the statement which makes <code>big.range_anti_mph</code> trivial to prove from the previous results</p>

#### [ Mario Carneiro (May 15 2018 at 10:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/natural%20number%20hell/near/126581152):
<p>Well, there are a lot of free endpoints in the reverse theorem, maybe you need to generalize it?</p>

#### [ Patrick Massot (May 15 2018 at 10:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/natural%20number%20hell/near/126581159):
<p>what reverse theorem?</p>

#### [ Mario Carneiro (May 15 2018 at 10:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/natural%20number%20hell/near/126581276):
<p>I'm thinking:</p>
<div class="codehilite"><pre><span></span>reverse (range&#39; a (n + 1)) = map (λ i, c-i) (range&#39; b (n + 1))
</pre></div>


<p>subject to an equation relating a,b,c</p>

#### [ Mario Carneiro (May 15 2018 at 10:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/natural%20number%20hell/near/126581305):
<p>Actually I think we need another generalization of <code>range'</code> that varies the step too</p>

#### [ Mario Carneiro (May 15 2018 at 10:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/natural%20number%20hell/near/126581346):
<p>that would make this easy</p>

#### [ Patrick Massot (May 15 2018 at 10:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/natural%20number%20hell/near/126581425):
<p>I need to go to my office, but the situation improved a lot: <a href="https://github.com/PatrickMassot/bigop/blob/master/src/bigop.lean#L335-L341" target="_blank" title="https://github.com/PatrickMassot/bigop/blob/master/src/bigop.lean#L335-L341">https://github.com/PatrickMassot/bigop/blob/master/src/bigop.lean#L335-L341</a> Thank you very much</p>

#### [ Patrick Massot (May 15 2018 at 10:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/natural%20number%20hell/near/126581440):
<p>I hope I'll be able to prove that last missing lemma later if you don't have time to do it properly</p>

#### [ Mario Carneiro (May 15 2018 at 11:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/natural%20number%20hell/near/126582724):
<p>I did it properly. Here are the lemmas I added:</p>
<div class="codehilite"><pre><span></span>theorem map_add_range&#39; (a) : ∀ s n : ℕ, map ((+) a) (range&#39; s n) = range&#39; (a + s) n
| s 0     := rfl
| s (n+1) := congr_arg (cons _) (map_add_range&#39; (s+1) n)

theorem range_succ_eq_map (n : ℕ) : range (n + 1) = 0 :: map succ (range n) :=
by rw [range_eq_range&#39;, range_eq_range&#39;, range&#39;,
       add_comm, ← map_add_range&#39;];
   congr; exact funext one_add

theorem reverse_range&#39; : ∀ s n : ℕ,
  reverse (range&#39; s n) = map (λ i, s + n - 1 - i) (range n)
| s 0     := rfl
| s (n+1) := by rw [range&#39;_concat, reverse_append, range_succ_eq_map];
  simpa [show s + (n + 1) - 1 = s + n, from rfl, (∘),
    λ a i, show a - 1 - i = a - succ i,
    by rw [nat.sub_sub, add_comm]; refl]
  using reverse_range&#39; s n
</pre></div>

#### [ Patrick Massot (May 15 2018 at 11:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/natural%20number%20hell/near/126584480):
<p>Thank you Mario! I already had the first one at <a href="https://github.com/PatrickMassot/bigop/blob/master/src/bigop.lean#L126" target="_blank" title="https://github.com/PatrickMassot/bigop/blob/master/src/bigop.lean#L126">https://github.com/PatrickMassot/bigop/blob/master/src/bigop.lean#L126</a></p>

#### [ Patrick Massot (May 15 2018 at 11:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/natural%20number%20hell/near/126584495):
<p>Maybe I should learn to do induction using pattern matching</p>

#### [ Patrick Massot (May 15 2018 at 19:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/natural%20number%20hell/near/126602871):
<p>I read too quickly, I thought you proved the lemma I needed</p>

#### [ Patrick Massot (May 15 2018 at 19:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/natural%20number%20hell/near/126602882):
<p>But your RHS doesn't even contains <code>range'</code></p>

#### [ Patrick Massot (May 15 2018 at 19:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/natural%20number%20hell/near/126602935):
<p>Proving the lemma I stated from what you proved seems to be as much work as a direct proof, no?</p>

#### [ Mario Carneiro (May 15 2018 at 22:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/natural%20number%20hell/near/126610298):
<p>You still have some algebra before you get to the exact version you need, but you can put <code>reverse_range'</code>, <code>range_eq_range'</code>, <code>map_add_range'</code> and <code>map_map</code> together and then do some algebra</p>

#### [ Mario Carneiro (May 15 2018 at 22:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/natural%20number%20hell/near/126610881):
<div class="codehilite"><pre><span></span>theorem range&#39;_eq_map_range (s n : ℕ) : range&#39; s n = map ((+) s) (range n) :=
by rw [range_eq_range&#39;, map_add_range&#39;]; refl

example (a b : ℕ) : reverse (range&#39; a (b+1-a)) = map (λ i, a+b-i) (range&#39; a (b+1-a)) :=
begin
  rw [reverse_range&#39;, range&#39;_eq_map_range, map_map],
  apply map_congr, intros i H,
  simp at *,
  rw [nat.add_sub_add_left, nat.add_sub_cancel&#39;], {refl},
  refine (le_total _ _).resolve_left (λ h, _),
  rw sub_eq_zero_of_le h at H,
  exact not_lt_zero _ H
end
</pre></div>

#### [ Patrick Massot (May 15 2018 at 23:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/natural%20number%20hell/near/126613014):
<p>Thank you very much Mario! I'm still not convinced this is simpler than a direct attack on this lemma, but I very much relieved to have it.</p>

#### [ Patrick Massot (May 15 2018 at 23:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/natural%20number%20hell/near/126613022):
<p>What is this <code>resolve_left</code> thing?</p>

#### [ Patrick Massot (May 15 2018 at 23:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/natural%20number%20hell/near/126613109):
<p>The state at the point where you write this, <code>a b i : ℕ,
H : i &lt; b + 1 - a
⊢ b + 1 ≥ a</code> is typically something that could have led me to harm my computer.</p>

#### [ Patrick Massot (May 15 2018 at 23:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/natural%20number%20hell/near/126613166):
<p>I also note that you used <code>simp at *</code> in the middle of a proof. Isn't this frowned upon according to mathlib's docs?</p>

#### [ Mario Carneiro (May 15 2018 at 23:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/natural%20number%20hell/near/126613168):
<p>That's actually a really subtle thing, it wouldn't work if it was <code>i &lt;= b+1-a</code></p>

#### [ Patrick Massot (May 15 2018 at 23:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/natural%20number%20hell/near/126613248):
<p>What do you mean it wouldn't work? The statement would still be true, right?</p>

#### [ Mario Carneiro (May 15 2018 at 23:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/natural%20number%20hell/near/126613250):
<p>no</p>

#### [ Patrick Massot (May 15 2018 at 23:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/natural%20number%20hell/near/126613267):
<p>This is crazy</p>

#### [ Mario Carneiro (May 15 2018 at 23:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/natural%20number%20hell/near/126613279):
<p>if i is zero then b+1 could be less than a</p>

#### [ Patrick Massot (May 15 2018 at 23:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/natural%20number%20hell/near/126613341):
<p>Did I mentioned I hate this substraction?</p>

#### [ Mario Carneiro (May 15 2018 at 23:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/natural%20number%20hell/near/126613362):
<p>the argument is basically that when you subtract small minus large you get 0, so since i is less than the subtraction it isn't zero so it is in the proper domain</p>

#### [ Mario Carneiro (May 15 2018 at 23:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/natural%20number%20hell/near/126613460):
<p>You could also have taken a &lt;= b+1 as an assumption to the theorem if you like</p>

#### [ Patrick Massot (May 15 2018 at 23:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/natural%20number%20hell/near/126613497):
<p>I still don't know what <code>resolve_left</code> stands for</p>

#### [ Mario Carneiro (May 15 2018 at 23:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/natural%20number%20hell/near/126613508):
<p><code>or.resolve_left</code></p>

#### [ Kenny Lau (May 15 2018 at 23:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/natural%20number%20hell/near/126613559):
<p><span class="user-mention" data-user-id="110031">@Patrick Massot</span> The type of <code>le_total _ _</code> is <code>or _ _</code></p>

#### [ Kenny Lau (May 15 2018 at 23:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/natural%20number%20hell/near/126613569):
<p>So <code>(le_total _ _).resolve_left</code> means <code>or.resolve_left (le_total _ _)</code></p>

#### [ Patrick Massot (May 15 2018 at 23:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/natural%20number%20hell/near/126613577):
<p>Thanks</p>

#### [ Patrick Massot (May 15 2018 at 23:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/natural%20number%20hell/near/126613580):
<p>to both of you</p>

#### [ Patrick Massot (May 15 2018 at 23:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/natural%20number%20hell/near/126613601):
<p>So the strategy here is some variation on a case disjunction, right?</p>

#### [ Patrick Massot (May 15 2018 at 23:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/natural%20number%20hell/near/126613632):
<p>Is it possible to use <code>by_cases</code> instead? (I only try to understand, I don't really want to use <code>by_cases</code>)</p>

#### [ Kenny Lau (May 15 2018 at 23:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/natural%20number%20hell/near/126613653):
<p><code>by_cases</code> uses <code>p or not p</code> instead of any arbitrary <code>p or q</code></p>

#### [ Patrick Massot (May 15 2018 at 23:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/natural%20number%20hell/near/126613672):
<p>It's true that <code>le_total</code> is almost but not quite like this</p>

#### [ Kenny Lau (May 15 2018 at 23:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/natural%20number%20hell/near/126613749):
<p>however I don't see the difference between <code>or.resolve_left (le_total _ _)</code> and <code>le_of_not_le</code></p>

#### [ Patrick Massot (May 15 2018 at 23:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/natural%20number%20hell/near/126613805):
<p>I still don't understand why the goal after this <code>refine</code> is <code>false</code></p>

#### [ Kenny Lau (May 15 2018 at 23:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/natural%20number%20hell/near/126613808):
<p><code>refine (le_total _ _).resolve_left (λ h, _)</code></p>

#### [ Kenny Lau (May 15 2018 at 23:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/natural%20number%20hell/near/126613820):
<p>the expected type of <code>(λ h, _)</code> is <code>not (le _ _)</code></p>

#### [ Kenny Lau (May 15 2018 at 23:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/natural%20number%20hell/near/126613832):
<p>so <code>h</code> has type <code>le _ _</code></p>

#### [ Kenny Lau (May 15 2018 at 23:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/natural%20number%20hell/near/126613837):
<p>so <code>_</code> has type <code>false</code></p>

#### [ Patrick Massot (May 15 2018 at 23:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/natural%20number%20hell/near/126613899):
<p>Indeed the mysterious line has the same effect as <code>apply le_of_not_le,
  by_contradiction h,</code></p>

#### [ Kenny Lau (May 15 2018 at 23:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/natural%20number%20hell/near/126613905):
<p>try <code>refine le_of_not_le (λ h, _)</code></p>

#### [ Mario Carneiro (May 15 2018 at 23:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/natural%20number%20hell/near/126613910):
<p><code>le_of_not_le</code> would also have worked</p>

#### [ Kenny Lau (May 15 2018 at 23:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/natural%20number%20hell/near/126613915):
<p><span class="user-mention" data-user-id="110049">@Mario Carneiro</span> entao eu ganho?</p>

#### [ Mario Carneiro (May 15 2018 at 23:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/natural%20number%20hell/near/126613925):
<p>vc ganhou</p>

#### [ Kenny Lau (May 15 2018 at 23:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/natural%20number%20hell/near/126613971):
<p>:D</p>

#### [ Patrick Massot (May 15 2018 at 23:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/natural%20number%20hell/near/126614006):
<p>The proof of <code>le_of_not_le</code> is exactly this <code>or.resolve_left le_total</code></p>

#### [ Patrick Massot (May 15 2018 at 23:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/natural%20number%20hell/near/126614057):
<p>But indeed Kenny's solution will probably be easier to remember for me</p>

#### [ Patrick Massot (May 15 2018 at 23:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/natural%20number%20hell/near/126614194):
<p>So, what should we do with all those lemmas we discussed in the last few days. Do you want me to prepare a PR? Are you doing it yourself?</p>

#### [ Mario Carneiro (May 15 2018 at 23:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/natural%20number%20hell/near/126614274):
<p>I've got a pot brewing, you can hold onto them locally until then</p>

#### [ Patrick Massot (May 15 2018 at 23:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/natural%20number%20hell/near/126614284):
<p>No problem</p>

#### [ Patrick Massot (May 15 2018 at 23:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/natural%20number%20hell/near/126614634):
<p>I extracted everything from my bigop file. It's now all in <a href="https://github.com/PatrickMassot/bigop/blob/master/src/pending_lemmas.lean" target="_blank" title="https://github.com/PatrickMassot/bigop/blob/master/src/pending_lemmas.lean">https://github.com/PatrickMassot/bigop/blob/master/src/pending_lemmas.lean</a> if you want to make sure you have everything that was discussed here</p>

#### [ Patrick Massot (May 15 2018 at 23:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/natural%20number%20hell/near/126614653):
<p>It's bedtime now. Thank you very much again!</p>

#### [ Patrick Massot (May 16 2018 at 11:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/natural%20number%20hell/near/126636219):
<p>I have three substractions now <span class="emoji emoji-1f628" title="fearful">:fearful:</span> <code>H : N ≥ 1, hyp : 0 ≤ i ∧ i &lt; N ⊢ N - (N - 1 - i) = i + 1</code></p>

#### [ Patrick Massot (May 16 2018 at 11:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/natural%20number%20hell/near/126636280):
<p>Isn't it a way to first prove that we would get the same result in Z, because each substraction comes with its relevant inequality, and then <code>ring</code>?</p>

#### [ Mario Carneiro (May 16 2018 at 11:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/natural%20number%20hell/near/126636450):
<p>yes, of course</p>

#### [ Mario Carneiro (May 16 2018 at 11:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/natural%20number%20hell/near/126636462):
<p>just use <code>int.cast_sub</code></p>

#### [ Patrick Massot (May 16 2018 at 11:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/natural%20number%20hell/near/126636524):
<p>how does that work?</p>

#### [ Mario Carneiro (May 16 2018 at 11:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/natural%20number%20hell/near/126636528):
<p>that is, use <code>int.cast_inj</code> to convert the natural number equality to a Z equality, and then use <code>int.cast_add</code>, <code>int.cast_sub</code> etc lemmas to move the arrows down to the bottom</p>

#### [ Patrick Massot (May 16 2018 at 11:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/natural%20number%20hell/near/126636531):
<p>Looking at the statement is pretty puzzling</p>

#### [ Mario Carneiro (May 16 2018 at 11:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/natural%20number%20hell/near/126636540):
<p>simp will do the latter part</p>

#### [ Chris Hughes (May 16 2018 at 11:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/natural%20number%20hell/near/126636541):
<div class="codehilite"><pre><span></span><span class="kn">example</span> <span class="o">{</span><span class="n">i</span> <span class="n">N</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">}</span> <span class="o">(</span><span class="n">H</span> <span class="o">:</span> <span class="n">N</span> <span class="bp">≥</span> <span class="mi">1</span><span class="o">)</span> <span class="o">(</span><span class="n">hyp</span> <span class="o">:</span> <span class="mi">0</span> <span class="bp">≤</span> <span class="n">i</span> <span class="bp">∧</span> <span class="n">i</span> <span class="bp">&lt;</span> <span class="n">N</span><span class="o">)</span> <span class="o">:</span> <span class="n">N</span> <span class="bp">-</span> <span class="o">(</span><span class="n">N</span> <span class="bp">-</span> <span class="mi">1</span> <span class="bp">-</span> <span class="n">i</span><span class="o">)</span> <span class="bp">=</span> <span class="n">i</span> <span class="bp">+</span> <span class="mi">1</span> <span class="o">:=</span>
<span class="k">have</span> <span class="mi">1</span> <span class="bp">+</span> <span class="n">i</span> <span class="bp">≤</span> <span class="n">N</span><span class="o">,</span> <span class="k">by</span> <span class="n">rw</span> <span class="n">add_comm</span><span class="bp">;</span> <span class="n">exact</span> <span class="n">hyp</span><span class="bp">.</span><span class="mi">2</span><span class="o">,</span>
<span class="k">by</span> <span class="n">rw</span> <span class="o">[</span><span class="n">nat</span><span class="bp">.</span><span class="n">sub_sub</span><span class="o">,</span> <span class="n">nat</span><span class="bp">.</span><span class="n">sub_sub_self</span> <span class="n">this</span><span class="o">,</span> <span class="n">add_comm</span><span class="o">]</span>
</pre></div>

#### [ Kenny Lau (May 16 2018 at 11:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/natural%20number%20hell/near/126636544):
<p>and the winner is...</p>

#### [ Mario Carneiro (May 16 2018 at 11:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/natural%20number%20hell/near/126636547):
<p>^ or just prove it directly</p>

#### [ Patrick Massot (May 16 2018 at 11:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/natural%20number%20hell/near/126636600):
<p>Thanks Chris, but I'm really tired of those direct proofs</p>

#### [ Patrick Massot (May 16 2018 at 11:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/natural%20number%20hell/near/126636603):
<p>I want a systematic method</p>

#### [ Mario Carneiro (May 16 2018 at 11:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/natural%20number%20hell/near/126636607):
<div class="codehilite"><pre><span></span>example {i N : ℕ} (H : N ≥ 1) (hyp : 0 ≤ i ∧ i &lt; N) : N - (N - 1 - i) = i + 1 :=
by rw [nat.sub_sub, add_comm, nat.sub_sub_self hyp.2]
</pre></div>

#### [ Kenny Lau (May 16 2018 at 11:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/natural%20number%20hell/near/126636616):
<p>and the winner is...</p>

#### [ Chris Hughes (May 16 2018 at 11:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/natural%20number%20hell/near/126636619):
<p>Is it poor form to use <code>exact hyp.2</code> instead of <code>exact nat.succ_le_of_lt hyp.2</code>?</p>

#### [ Mario Carneiro (May 16 2018 at 11:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/natural%20number%20hell/near/126636625):
<p>meh</p>

#### [ Kenny Lau (May 16 2018 at 11:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/natural%20number%20hell/near/126636629):
<p>maybe you should replace <code>exact hyp.2</code> with <code>cc</code></p>

#### [ Kenny Lau (May 16 2018 at 11:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/natural%20number%20hell/near/126636671):
<p>I mean, it isn't like you can't prove <code>H</code> from <code>hyp</code>...</p>

#### [ Mario Carneiro (May 16 2018 at 11:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/natural%20number%20hell/near/126636673):
<p>in general you should minimize your implicit definitional unfolding, but some things are too foundational to change at this point and I assume it will stay that way</p>

#### [ Patrick Massot (May 16 2018 at 11:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/natural%20number%20hell/near/126636676):
<p>I don't know how to use <code>int.cast_inj</code></p>

#### [ Mario Carneiro (May 16 2018 at 11:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/natural%20number%20hell/near/126636746):
<p>oops, I mean <code>int.coe_nat_inj'</code></p>

#### [ Mario Carneiro (May 16 2018 at 11:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/natural%20number%20hell/near/126636832):
<div class="codehilite"><pre><span></span>example {i N : ℕ} (H : N ≥ 1) (hyp : 0 ≤ i ∧ i &lt; N) : N - (N - 1 - i) = i + 1 :=
by rw [← int.coe_nat_inj&#39;, int.coe_nat_sub, int.coe_nat_sub, int.coe_nat_sub]
</pre></div>


<p>produces a bunch of side conditions about less equal stuff</p>

#### [ Mario Carneiro (May 16 2018 at 11:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/natural%20number%20hell/near/126636880):
<p>actually it's a bit messy since the side conditions themselves involve natural number subtraction, so you need to rewrite them too or else prove them directly</p>

#### [ Mario Carneiro (May 16 2018 at 11:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/natural%20number%20hell/near/126636937):
<p>If you want to take this route I would suggest not writing natural number subtraction at all when you can help it, so that you don't need to deal with nested subtractions and the like</p>

#### [ Mario Carneiro (May 16 2018 at 11:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/natural%20number%20hell/near/126636946):
<p>that is, just use integer subtraction and convert back to natural numbers at the end with <code>int.to_nat</code> if necessary</p>

#### [ Patrick Massot (May 16 2018 at 11:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/natural%20number%20hell/near/126637007):
<p>"not writing natural number subtraction at all" is my greatest Lean dream</p>

#### [ Mario Carneiro (May 16 2018 at 11:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/natural%20number%20hell/near/126637069):
<p>A simple way to actually do that is to replace <code>m - n</code> everywhere with <code>int.to_nat (m - n)</code> (where the subtraction there is actually integer subtraction now)</p>

#### [ Patrick Massot (May 16 2018 at 11:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/natural%20number%20hell/near/126637078):
<p>I need to go, I'll try tonight. Thanks you!</p>

#### [ Mario Carneiro (May 16 2018 at 11:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/natural%20number%20hell/near/126637080):
<p>That way the funky zero saturation operator is explicit</p>

#### [ Kevin Buzzard (May 16 2018 at 14:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/natural%20number%20hell/near/126643379):
<blockquote>
<p>I want a systematic method</p>
</blockquote>
<p>How about this: replace every occurrence of <code>X &lt;= Y</code> with <code>Y = X + c</code> and replace every occurrence of <code>X &lt; Y </code> with <code>Y = X + c + 1</code>, and then just use <code>add_sub_cancel</code> or whatever it's called -- <code>a + b - b = a</code>. It would not surprise me if this algorithm worked every time.</p>

#### [ Kevin Buzzard (May 16 2018 at 14:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/natural%20number%20hell/near/126643448):
<p>Example: you know <code>i &lt; N</code> and you want to prove <code>N - (N - 1 - i) = i + 1</code>, well, write <code>N = i + 1 + j</code> and -- oh -- you also need <code>X - (Y + Z) = X- Y - Z</code> -- you get <code>N - (j + 1 + i - (1 + i))</code> which is <code>N - j</code> which is <code>i + 1 + j - j</code> which is <code>i + 1</code></p>

#### [ Kevin Buzzard (May 16 2018 at 14:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/natural%20number%20hell/near/126643465):
<p>I am assuming that your mathematician's goals never actually rely on the fact that a - b = 0 if b&gt;a</p>

#### [ Kevin Buzzard (May 16 2018 at 14:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/natural%20number%20hell/near/126643674):
<p>This should reduce everything to <code>nat.sub_sub</code> (if memory serves -- is it called that?) and <code>add_sub_cancel</code> or whatever it's called (not in front of Lean right now).</p>

#### [ Kevin Buzzard (May 16 2018 at 14:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/natural%20number%20hell/near/126643689):
<p>oh and associativity and commutativity of course</p>

#### [ Kevin Buzzard (May 16 2018 at 14:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/natural%20number%20hell/near/126643699):
<p>Make them simp lemmas and see if simp can do it after you make the substitutions</p>

#### [ Kevin Buzzard (May 16 2018 at 14:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/natural%20number%20hell/near/126643713):
<p>(if they're not simp lemmas already)</p>

#### [ Kevin Buzzard (May 16 2018 at 14:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/natural%20number%20hell/near/126643719):
<p>Might not be the optimal approach but it looks pretty systematic to me</p>

#### [ Chris Hughes (May 16 2018 at 14:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/natural%20number%20hell/near/126643809):
<blockquote>
<p>replace every occurrence of <code>X &lt;= Y</code> with `Y = X + c</p>
</blockquote>
<p>This bit sounds hard to do with <code>simp</code>, since it involves casing on exists.</p>

#### [ Kevin Buzzard (May 16 2018 at 14:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/natural%20number%20hell/near/126643817):
<p>you just introduce another variable</p>

#### [ Kevin Buzzard (May 16 2018 at 14:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/natural%20number%20hell/near/126643823):
<p>you do all that before you start the simp</p>


{% endraw %}
