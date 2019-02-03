---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/03459convexample.html
---

## Stream: [general](index.html)
### Topic: [conv example](03459convexample.html)

---


{% raw %}
#### [ Kevin Buzzard (Mar 13 2018 at 12:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/conv%20example/near/123651407):
<p>I was trying to write an example to illustrate the power of <code>conv</code>, by finding an example where the entire goal was difficult to work with because it contained implicit proofs. I realised that there were two things I didn't understand properly. Here's some code.</p>

#### [ Kevin Buzzard (Mar 13 2018 at 12:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/conv%20example/near/123651409):
<div class="codehilite"><pre><span></span>@[elab_simple] def subtypeadd {m : ℕ} {n : ℕ} (A : fin m) (B : fin n) : fin (m+n) :=
  ⟨A.val+B.val,add_lt_add A.is_lt B.is_lt⟩

definition phi {m n : ℕ} : fin (m + n) → fin (n + m) := λ ⟨i,Hi⟩, ⟨i,add_comm m n ▸ Hi⟩

example {m n : ℕ} (A : fin m) (B : fin n) : phi (subtypeadd A B) = subtypeadd B A :=
begin
  have H : A.val + B.val = B.val + A.val := add_comm _ _,
  -- unfold subtypeadd using show
  show phi ⟨A.val + B.val, _⟩ = ⟨B.val + A.val, _⟩,
  rw H -- fails
end
</pre></div>

#### [ Kevin Buzzard (Mar 13 2018 at 12:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/conv%20example/near/123651451):
<p>I wanted to make the example hard for one reason, but it somehow turned out to be hard for another reason :-/</p>

#### [ Kevin Buzzard (Mar 13 2018 at 12:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/conv%20example/near/123651460):
<p>My first question is why does the <code>show</code> command succeed? I assumed that what <code>show X</code> did was that it first checked that <code>X</code> made sense, and then checked that it was defeq to the goal.</p>

#### [ Kevin Buzzard (Mar 13 2018 at 12:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/conv%20example/near/123651464):
<p>But I thought I had explicitly rigged it here so that <code>X</code> wouldn't be able to be elaborated, because of the missing proofs.</p>

#### [ Kevin Buzzard (Mar 13 2018 at 12:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/conv%20example/near/123651506):
<p>My second question is why does <code>rw</code> fail. I have heard rumours that <code>rw</code> will not work inside a lambda (although I don't really understand why -- why is this?) but this is not a lambda and I think the reason for failure is something else.</p>

#### [ Kevin Buzzard (Mar 13 2018 at 12:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/conv%20example/near/123651512):
<p>The error message is</p>
<div class="codehilite"><pre><span></span>rewrite tactic failed, motive is not type correct
nested exception message:
check failed, application type mismatch (use &#39;set_option trace.check true&#39; for additional details)
state:
m n : ℕ,
A : fin m,
B : fin n,
H : A.val + B.val = B.val + A.val
⊢ phi ⟨A.val + B.val, _⟩ = ⟨B.val + A.val, _⟩
</pre></div>

#### [ Kevin Buzzard (Mar 13 2018 at 12:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/conv%20example/near/123651515):
<p>and if I <code>set_option trace.check true</code> then I get an exciting helpful extra hint:</p>

#### [ Kevin Buzzard (Mar 13 2018 at 12:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/conv%20example/near/123651516):
<div class="codehilite"><pre><span></span>[check] application type mismatch at
  ⟨_a, _⟩
argument type
  A.val + B.val &lt; m + n
expected type
  _a &lt; m + n
</pre></div>

#### [ Kevin Buzzard (Mar 13 2018 at 12:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/conv%20example/near/123651557):
<p>which makes no sense to me...oh! Is it rewriting too many A.val + B.val's?</p>

#### [ Kevin Buzzard (Mar 13 2018 at 12:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/conv%20example/near/123651559):
<p>I am still a bit bewildered about why this is a type mismatch I guess.</p>

#### [ Kevin Buzzard (Mar 13 2018 at 12:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/conv%20example/near/123651565):
<p>(deleted)</p>

#### [ Kevin Buzzard (Mar 13 2018 at 12:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/conv%20example/near/123651618):
<p>(deleted)</p>

#### [ Kevin Buzzard (Mar 13 2018 at 12:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/conv%20example/near/123651680):
<p>For the first question I guess an underlying question is "which option do you switch on so you can see how Lean is filling in <code>_</code>s?"</p>

#### [ Mario Carneiro (Mar 13 2018 at 13:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/conv%20example/near/123652795):
<blockquote>
<p>My first question is why does the show command succeed? I assumed that what show X did was that it first checked that X made sense, and then checked that it was defeq to the goal.</p>
</blockquote>
<p>I was going to mention this before with your <code>X = Y</code> into <code>X' = Y</code> problem - you could have just written <code>show X' = _</code>. The reason this works is because the checking is done in a weak mode that tolerates metavariable generation, and the second defeq step is not just checking defeq, it is unifying with the target. This means that the first stage will create metavariables and the second stage will unfold stuff as needed to figure out the metavariables. If it can't completely solve the metavariables, you will get new goals instead of an error.</p>
<div class="codehilite"><pre><span></span>example : tt = tt :=
begin
  show (λ x, tt) _ = tt,
  -- ⊢ (λ (x : ?m_1), tt) ?m_2 = tt
end

example : tt = tt :=
begin
  change (λ x, tt) _ = tt,
  -- ⊢ (λ (x : ?m_1), tt) ?m_2 = tt
  -- ⊢ Sort ?
  -- ⊢ ?m_1
end
</pre></div>


<p>As you can see, <code>show</code> differs slightly in that it doesn't change the number of goals while <code>change</code> will add all those unsolved metavariables as new goals, just like <code>refine</code> would.</p>

#### [ Mario Carneiro (Mar 13 2018 at 13:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/conv%20example/near/123652855):
<p>By the way, goals that look like your <code>phi ⟨A.val + B.val, _⟩ = ⟨B.val + A.val, _⟩</code> often don't work (they fail in the first stage of parsing), because the anonymous constructor can't be solved outright. In this case it works because <code>phi</code> is sufficient to deduce that both constructors are <code>fin</code>.</p>

#### [ Mario Carneiro (Mar 13 2018 at 13:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/conv%20example/near/123653214):
<blockquote>
<p>My second question is why does rw fail. I have heard rumours that rw will not work inside a lambda (although I don't really understand why -- why is this?) but this is not a lambda and I think the reason for failure is something else.</p>
</blockquote>
<p><code>rw</code> is very sensitive to dependencies. (Or more accurately, it is sufficiently <em>insensitive</em> to dependencies that it will generally fail in their presence.) Both <code>rw</code> and <code>generalize</code> are built on the same basic underlying internal tactic <code>kabstract</code>, which is supposed to take a term <code>P[T]</code> containing a subterm <code>T</code>, and replace it with a variable <code>x</code>. This is needed to construct the motive of the <code>eq.rec</code> application that goes in the proof term when using <code>rw</code>, and it's what you see directly if you use <code>generalize</code>.</p>
<p>The strategy is very simple: look through the term for any subterms that match <code>T</code> (up to some very light unfolding), and replace them with <code>x</code>. It should be obvious that this can get you into trouble when you have dependencies. For example, if <code>two_pos : 0 &lt; 2</code> then <code>&lt;2, two_pos&gt;</code> is a well typed element of <code>fin 2</code>, but if you simply replace 2 with x you get <code>&lt;x, two_pos&gt;</code> which is not in either <code>fin x</code> or <code>fin 2</code>, it's just malformed. It is actually really difficult to do this correctly in general; in this case you would probably want to generalize the proof of <code>two_pos</code> first so that it will "ride the wave" of 2 -&gt; x renaming rather than being stuck talking about the fixed number 2.</p>
<p>As it pertains to your example, the error message is fairly clear, although it would be more obvious with <code>set_option pp.proofs true</code>. The left argument to the <code>fin</code> constructor has been generalized from <code>A.val + B.val</code> to <code>_a</code>, but the right argument, the proof, is still a proof of <code>A.val + B.val &lt; m + n</code> (namely <code>add_lt_add A.is_lt B.is_lt</code>, what you ended up with after the unfolding), and this is not a correct proof of <code>_a &lt; m + n</code>.</p>
<p>The other major rewrite engine in lean is <code>simp</code>, which does not use <code>kabstract</code>. It operates by using congruence lemmas to recurse into subterms, and this strategy makes it much more reliably type-correct when it comes to rewriting under dependencies. If you try to use <code>simp</code> to rewrite here, it will work, and the proof argument will change to a cast of some sort to accommodate the new type.</p>

#### [ Kevin Buzzard (Mar 13 2018 at 13:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/conv%20example/near/123653217):
<p>Is it possible for me to watch all this unification taking place explicitly? i.e. some set_option?</p>

#### [ Kevin Buzzard (Mar 13 2018 at 13:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/conv%20example/near/123653282):
<p>[that was about the show / change stuff]</p>

#### [ Mario Carneiro (Mar 13 2018 at 13:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/conv%20example/near/123653325):
<p>I think <code>set_option trace.type_context.is_def_eq true</code> is what you want</p>

#### [ Kevin Buzzard (Mar 13 2018 at 13:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/conv%20example/near/123653332):
<p>Earlier on I realised that I didn't really know what rw did, so I've just spent 20 minutes doing edge cases and now I can understand the rw issue. I found that <code>rw</code> doesn't commute with <code>eq.symm</code> in general :-)</p>

#### [ Sebastian Ullrich (Mar 13 2018 at 13:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/conv%20example/near/123653334):
<p>Plus <code>...is_def_eq_detail</code>, probably</p>

#### [ Kevin Buzzard (Mar 13 2018 at 13:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/conv%20example/near/123653381):
<div class="codehilite"><pre><span></span>example (a b: ℕ) : b + a = b + a + a + b := begin
rw add_comm, -- a + b = a + b + a + b
end
</pre></div>

#### [ Kevin Buzzard (Mar 13 2018 at 13:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/conv%20example/near/123653455):
<p>Are the <code>set_option</code> options documented anywhere?</p>

#### [ Mario Carneiro (Mar 13 2018 at 14:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/conv%20example/near/123653753):
<p><code>#help options</code> seems to do the trick. (I had to search the code to find that gem. <code>#help</code> is such a rarely used command for me, I'm not even really sure what's there...)</p>

#### [ Kevin Buzzard (Mar 13 2018 at 14:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/conv%20example/near/123654932):
<p>I am not even sure if I knew <code>#help</code> existed. I thought the help command in Lean was <code>#print</code></p>

#### [ Mario Carneiro (Mar 13 2018 at 14:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/conv%20example/near/123654973):
<p>it certainly does seem to be a large overlap of duties</p>

#### [ Kevin Buzzard (Mar 13 2018 at 14:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/conv%20example/near/123654990):
<p>I can use conv to rewrite <code>A.val + B.val</code> in that earlier example.</p>

#### [ Kevin Buzzard (Mar 13 2018 at 14:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/conv%20example/near/123654994):
<div class="codehilite"><pre><span></span>@[elab_simple] def subtypeadd {m : ℕ} {n : ℕ} (A : fin m) (B : fin n) : fin (m+n) :=
  ⟨A.val+B.val,add_lt_add A.is_lt B.is_lt⟩

definition phi {m n : ℕ} : fin (m + n) → fin (n + m) := λ ⟨i,Hi⟩, ⟨i,add_comm m n ▸ Hi⟩

example {m n : ℕ} (A : fin m) (B : fin n) : phi (subtypeadd A B) = subtypeadd B A :=
begin
  have H : A.val + B.val = B.val + A.val := add_comm _ _,
  -- unfold subtypeadd using show
  show phi ⟨A.val + B.val, _⟩ = ⟨B.val + A.val, _⟩,
  conv
  begin
  congr,
  congr,
  congr,
  rw H,
  end, -- is the term on the left OK??
  admit
end
</pre></div>

#### [ Kevin Buzzard (Mar 13 2018 at 14:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/conv%20example/near/123654999):
<p>conv is doing all sorts of funny things here</p>

#### [ Kevin Buzzard (Mar 13 2018 at 14:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/conv%20example/near/123655000):
<p>It seems to forget some terms</p>

#### [ Kevin Buzzard (Mar 13 2018 at 14:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/conv%20example/near/123655002):
<p>and I managed to do a rewrite which earlier on was impossible for a good reason</p>

#### [ Kevin Buzzard (Mar 13 2018 at 14:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/conv%20example/near/123655052):
<p>or was it impossible for a bad reason?</p>

#### [ Kevin Buzzard (Mar 13 2018 at 14:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/conv%20example/near/123655114):
<p>Oh maybe conv doesn't care about the terms it forgets.</p>

#### [ Mario Carneiro (Mar 13 2018 at 14:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/conv%20example/near/123655119):
<p>I would be in support of moving all "auxiliary" <code>#print</code> stuff to <code>#help</code>; it is a little confusing to have namespace overlapping between <code>#print options</code> (which prints lean cmdline options), <code>#print option</code> (which prints the <code>option</code> type) and <code>#print pp.all</code> (which prints info on the <code>pp.all</code> option)</p>

#### [ Kevin Buzzard (Mar 13 2018 at 14:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/conv%20example/near/123655120):
<p>Does conv not bother with subsingletons?</p>

#### [ Kevin Buzzard (Mar 13 2018 at 14:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/conv%20example/near/123655126):
<p>I lost a proof</p>

#### [ Kevin Buzzard (Mar 13 2018 at 14:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/conv%20example/near/123655197):
<p>I see. So <code>fin</code> is a structure so I can build things of type <code>fin n</code> and they will be of the form <code>&lt;value,proof that this value is less than n&gt;</code></p>

#### [ Kevin Buzzard (Mar 13 2018 at 14:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/conv%20example/near/123655205):
<p>but there's nothing stopping me from deviously changing the value without changing the proof</p>

#### [ Mario Carneiro (Mar 13 2018 at 14:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/conv%20example/near/123655213):
<p>By the way, if you are actually interested in this theorem, a short proof is <code>fin.eq_of_veq (add_comm _ _)</code></p>

#### [ Kevin Buzzard (Mar 13 2018 at 14:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/conv%20example/near/123655278):
<p>I don't need the theorem, I was experimenting with trying to build goals which the prettyprinter wouldn't let me use show with ("show &lt;what the pretty printer says the goal is&gt;" failing)</p>

#### [ Mario Carneiro (Mar 13 2018 at 14:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/conv%20example/near/123655280):
<p><code>conv</code> uses congrence lemmas, like <code>simp</code>, to traverse the term, certainly if you are using the <code>congr</code> tactic</p>

#### [ Mario Carneiro (Mar 13 2018 at 14:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/conv%20example/near/123655286):
<p>so it will succeed for the same reason that simp does</p>

#### [ Kevin Buzzard (Mar 13 2018 at 14:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/conv%20example/near/123655290):
<p>conv is really useful for a learner like me.</p>

#### [ Kevin Buzzard (Mar 13 2018 at 14:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/conv%20example/near/123655342):
<p>It enables to you really zoom in to parts of complicated things which beginners have trouble manipulating</p>

#### [ Mario Carneiro (Mar 13 2018 at 14:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/conv%20example/near/123655343):
<p>You should turn on <code>pp.proofs</code> while working with this</p>

#### [ Kevin Buzzard (Mar 13 2018 at 14:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/conv%20example/near/123655346):
<p>oh that's a cool option</p>

#### [ Mario Carneiro (Mar 13 2018 at 14:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/conv%20example/near/123655358):
<p>lol I remember the days when it was the only option. It's like 80% a good idea to hide proofs</p>

#### [ Kevin Buzzard (Mar 13 2018 at 14:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/conv%20example/near/123655359):
<p>is there a command which just changes the state of every option that is available?</p>

#### [ Kevin Buzzard (Mar 13 2018 at 14:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/conv%20example/near/123655364):
<p>then I could easily see all the other things I'm missing</p>

#### [ Mario Carneiro (Mar 13 2018 at 14:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/conv%20example/near/123655365):
<p>lol that would be bedlam</p>

#### [ Kevin Buzzard (Mar 13 2018 at 14:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/conv%20example/near/123655368):
<p>Imagine how much I'd learn</p>

#### [ Mario Carneiro (Mar 13 2018 at 14:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/conv%20example/near/123655417):
<p>If you care about printing, look at completions for <code>set_option pp.</code></p>

#### [ Kevin Buzzard (Mar 13 2018 at 14:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/conv%20example/near/123655428):
<p>I remember getting really confused early on because of those <code>_</code>s in goals which I'd completely forgotten what they stood for</p>

#### [ Kevin Buzzard (Mar 13 2018 at 14:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/conv%20example/near/123655438):
<p>It would be even better if it said what they were a proof of</p>

#### [ Mario Carneiro (Mar 13 2018 at 14:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/conv%20example/near/123655455):
<p>That was proposed; but it would make things even harder for the copy-pasters</p>

#### [ Kevin Buzzard (Mar 13 2018 at 14:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/conv%20example/near/123655497):
<p>why not make it an option?</p>

#### [ Mario Carneiro (Mar 13 2018 at 14:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/conv%20example/near/123655502):
<p>I don't want to have to edit all those types out</p>

#### [ Mario Carneiro (Mar 13 2018 at 14:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/conv%20example/near/123655505):
<p>to make it compile</p>

#### [ Kevin Buzzard (Mar 13 2018 at 14:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/conv%20example/near/123655512):
<p>Oh wooah if I set proofs on, then does "show (goal)" always succeed?</p>

#### [ Mario Carneiro (Mar 13 2018 at 14:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/conv%20example/near/123655514):
<p>no, silly</p>

#### [ Kevin Buzzard (Mar 13 2018 at 14:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/conv%20example/near/123655515):
<p>:-)</p>

#### [ Kevin Buzzard (Mar 13 2018 at 14:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/conv%20example/near/123655524):
<p>does that solve the halting problem or something?</p>

#### [ Mario Carneiro (Mar 13 2018 at 14:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/conv%20example/near/123655526):
<p>there are a thousand and one edge cases that cause bad printing</p>

#### [ Kevin Buzzard (Mar 13 2018 at 14:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/conv%20example/near/123655528):
<p>Oh OK.</p>

#### [ Mario Carneiro (Mar 13 2018 at 14:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/conv%20example/near/123655529):
<p>even <code>pp.all</code> sometimes fails</p>

#### [ Kevin Buzzard (Mar 13 2018 at 14:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/conv%20example/near/123655530):
<p>o_O</p>

#### [ Mario Carneiro (Mar 13 2018 at 15:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/conv%20example/near/123655728):
<p>Here's an example:</p>
<div class="codehilite"><pre><span></span>theorem T : nat.zero = nat.zero :=
by have f := (λ {x}, eq.refl x); exact f

set_option pp.all true
#print T
theorem T&#39; : @eq.{1} nat nat.zero nat.zero :=
@(λ {x : nat}, @eq.refl.{1} nat x) nat.zero --parse error
</pre></div>

#### [ Kevin Buzzard (Mar 13 2018 at 15:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/conv%20example/near/123655807):
<p>Oh maybe we're talking at cross purposes.</p>

#### [ Kevin Buzzard (Mar 13 2018 at 15:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/conv%20example/near/123655814):
<div class="codehilite"><pre><span></span>theorem T&#39; : @eq.{1} nat nat.zero nat.zero :=
begin
show @eq.{1} nat nat.zero nat.zero -- succeeds
end
</pre></div>

#### [ Kevin Buzzard (Mar 13 2018 at 15:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/conv%20example/near/123655864):
<p>I was wondering if one could be in tactic mode in a situation where the goal is represented by some string S, and then <code>show S</code> fails</p>

#### [ Kevin Buzzard (Mar 13 2018 at 15:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/conv%20example/near/123655937):
<p>I am pretty sure I've done that before, but I am less sure about having done it with pp.all true</p>

#### [ Mario Carneiro (Mar 13 2018 at 15:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/conv%20example/near/123656284):
<p>It's easiest to demonstrate by using <code>#print</code> to view proof terms, but this affects all printing, and you can make it work with target printing as well by a similar mechanism.</p>
<div class="codehilite"><pre><span></span>--set_option pp.all true
theorem T : nat.le nat.zero (by have f := (λ {x:ℕ}, 0); exact @f nat.zero) :=
begin
  -- ⊢ nat.le 0 (λ {x : ℕ}, 0)
  change nat.le 0 (λ {x : ℕ}, 0), --fail
  change nat.le nat.zero (@(λ {x : nat}, @has_zero.zero.{0} nat nat.has_zero) nat.zero) -- parse error
end
</pre></div>

#### [ Kevin Buzzard (Mar 13 2018 at 15:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/conv%20example/near/123656605):
<p>Are these bugs in the prettyprinter? Or just interesting features?</p>

#### [ Kevin Buzzard (Mar 13 2018 at 15:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/conv%20example/near/123656620):
<p>Or should <code>@(lam {x},...)</code> actually work?</p>

#### [ Sebastian Ullrich (Mar 13 2018 at 15:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/conv%20example/near/123656672):
<p>It's the pretty printer wishing for a feature the parser hasn't implemented yet</p>

#### [ Sebastian Ullrich (Mar 13 2018 at 15:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/conv%20example/near/123656731):
<p>Slightly passive-agressive behavior</p>

#### [ Kevin Buzzard (Mar 13 2018 at 15:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/conv%20example/near/123657305):
<p>I see. The pretty printer is somehow the anti-parser isn't it.</p>

#### [ Kevin Buzzard (Mar 13 2018 at 15:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/conv%20example/near/123657312):
<p>in fact it's a one-sided inverse, in a perfect world.</p>

#### [ Patrick Massot (Mar 13 2018 at 15:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/conv%20example/near/123657314):
<p>See <a href="https://github.com/leanprover/lean/issues/1900" target="_blank" title="https://github.com/leanprover/lean/issues/1900">#1900</a></p>

#### [ Kevin Buzzard (Mar 13 2018 at 17:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/conv%20example/near/123661013):
<p>I am still unclear about one thing in this thread.</p>

#### [ Kevin Buzzard (Mar 13 2018 at 17:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/conv%20example/near/123661014):
<div class="codehilite"><pre><span></span>example (a b c N : ℕ) (H1 : a = b) (H2 : a &lt; N) (H3 : b &lt; N) :
 (⟨a,H2⟩:fin N) = ⟨b,H3⟩ :=
begin
-- rw H1 fails
conv begin
  to_lhs,congr, -- goal now | a
  rw H1, -- succeeds
  end,
end
</pre></div>

#### [ Kevin Buzzard (Mar 13 2018 at 17:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/conv%20example/near/123661095):
<p>The first rw fails and my understanding is that it fails because it gives rise to a term which is malformed (copying from Mario's comments above). However it seems to be only as malformed as the term I successfully construct using the conv trick.</p>

#### [ Kevin Buzzard (Mar 14 2018 at 22:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/conv%20example/near/123723050):
<p>I am still none the wiser about this. One conclusion which I've not yet ruled out is simply that whoever wrote <code>rw</code> could have done better, and made that first <code>rw H1</code> above succeed, because there is nothing in type theory stopping it from succeeding, as we see from the conv approach. Is the reason that <code>rw H1</code> fails simply that the <code>rw</code> code just doesn't cover this use case?</p>

#### [ Mario Carneiro (Mar 14 2018 at 22:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/conv%20example/near/123723190):
<p>I think you are missing that the <code>conv</code> version isn't using just <code>rw</code>, it's using <code>rw</code> + <code>congr</code>, and it is applying <code>congr</code> in the place where dependency matters. Once the goal is <code>| a</code>, there is no longer a dependency to worry about, and <code>rw</code> has no problems.</p>

#### [ Kevin Buzzard (Mar 14 2018 at 23:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/conv%20example/near/123723911):
<p>But there is nothing stopping someone from beefing up rw so that it works without using conv? It's just some tactic, right?</p>

#### [ Kevin Buzzard (Mar 14 2018 at 23:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/conv%20example/near/123724107):
<p>Initially when I heard that rw couldn't rewrite in certain circumstances I thought that this was because of some theoretical type theory issue which was beyond me, but now I am more inclined to believe that it's just beyond rw.</p>

#### [ Kevin Buzzard (Mar 14 2018 at 23:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/conv%20example/near/123724117):
<p>This typechecks:</p>
<div class="codehilite"><pre><span></span>example (a b c N : ℕ) (H1 : a = b) (H2 : a &lt; N) (H3 : b &lt; N) :
 (⟨a,H2⟩:fin N) = ⟨b,H3⟩ := sorry
</pre></div>

#### [ Kevin Buzzard (Mar 14 2018 at 23:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/conv%20example/near/123724133):
<p>but if I replace <code>sorry</code> with <code>eq.subst H1 _</code> then all of a sudden I get a type mismatch in the statement (not the proof) of the example.</p>

#### [ Mario Carneiro (Mar 14 2018 at 23:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/conv%20example/near/123724136):
<p>Yes and no. <code>rw</code> does exactly what we want it to, which is to produce an <code>eq.rec</code> term with a well chosen motive. <code>congr</code> applies an appropriate congruence lemma. There are theoretical limitations on what you can prove using <code>eq.rec</code>, and this is why one wouldn't want to change <code>rw</code> for this</p>

#### [ Mario Carneiro (Mar 14 2018 at 23:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/conv%20example/near/123724181):
<p>I opened an issue on dependent <code>rw</code> a while ago, I think it was closed by "use <code>simp</code> instead"</p>

#### [ Kevin Buzzard (Mar 14 2018 at 23:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/conv%20example/near/123724194):
<p>I now know from experience that this is not a satisfactory response</p>

#### [ Kevin Buzzard (Mar 14 2018 at 23:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/conv%20example/near/123724201):
<p>The reason I got interested in this use of conv was that I had a situation where simp simplified too much</p>

#### [ Kevin Buzzard (Mar 14 2018 at 23:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/conv%20example/near/123724245):
<p>so I had to be super-accurate with my rw</p>

#### [ Kevin Buzzard (Mar 14 2018 at 23:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/conv%20example/near/123724246):
<p>conv saved me</p>

#### [ Mario Carneiro (Mar 14 2018 at 23:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/conv%20example/near/123724250):
<p>I mean the <code>simp</code> engine, not necessarily <code>simp</code> on its own</p>

#### [ Kevin Buzzard (Mar 14 2018 at 23:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/conv%20example/near/123724253):
<p>How do you use the simp engine??</p>

#### [ Simon Hudon (Mar 14 2018 at 23:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/conv%20example/near/123724256):
<p>Did it simplify too much even when you called <code>simp only [your rules here]</code>?</p>

#### [ Mario Carneiro (Mar 14 2018 at 23:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/conv%20example/near/123724259):
<p>You know that <code>simp</code> has a bazillion options, right?</p>

#### [ Kevin Buzzard (Mar 14 2018 at 23:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/conv%20example/near/123724265):
<p>Oh that's a good point Simon, I didn't try this</p>

#### [ Mario Carneiro (Mar 14 2018 at 23:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/conv%20example/near/123724279):
<p>Remember when you discovered that <code>unfold</code> is really <code>simp</code>?</p>

#### [ Kevin Buzzard (Mar 14 2018 at 23:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/conv%20example/near/123724280):
<p>Are those bazillion options documented? If not, then no I don't know and I don't know how to find out.</p>

#### [ Kevin Buzzard (Mar 14 2018 at 23:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/conv%20example/near/123724289):
<p>other than random looking through changelogs and source code</p>

#### [ Kevin Buzzard (Mar 14 2018 at 23:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/conv%20example/near/123724290):
<p>which I find about as pleasant as looking through trash cans</p>

#### [ Simon Hudon (Mar 14 2018 at 23:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/conv%20example/near/123724327):
<p>That would deserve a good amount of documentation, that's true.</p>

#### [ Mario Carneiro (Mar 14 2018 at 23:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/conv%20example/near/123724335):
<p><code>simp only [h] {single_pass := tt}</code> is pretty close to <code>rw</code>-like rewriting</p>

#### [ Kevin Buzzard (Mar 14 2018 at 23:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/conv%20example/near/123724349):
<p>I did know about simp only from TPIL but somehow it's one of those options which I would never use in practice because my initial reaction when I read TPIL was "whyever would you want to use simp only?"</p>

#### [ Simon Hudon (Mar 14 2018 at 23:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/conv%20example/near/123724352):
<p>And if you identify the lemmas that cause trouble you can disable it specifically with <code>simp [my_rule, - naughty]</code></p>

#### [ Kevin Buzzard (Mar 14 2018 at 23:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/conv%20example/near/123724358):
<p>and it's only more recently as I have become more experienced that I realise I need it, by which time I have forgotten about it</p>

#### [ Kevin Buzzard (Mar 14 2018 at 23:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/conv%20example/near/123724366):
<p>and the simp docs which I PR'ed have explanations of how to find out which lemmas are causing trouble</p>

#### [ Mario Carneiro (Mar 14 2018 at 23:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/conv%20example/near/123724367):
<p>And to identify naughty lemmas you can use <code>set_option trace.simplify.rewrite true</code></p>

#### [ Kevin Buzzard (Mar 14 2018 at 23:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/conv%20example/near/123724370):
<p>yeah, I read that in the docs</p>

#### [ Kevin Buzzard (Mar 14 2018 at 23:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/conv%20example/near/123724371):
<p>which I wrote</p>

#### [ Kevin Buzzard (Mar 14 2018 at 23:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/conv%20example/near/123724376):
<p>because I cannot manage without docs</p>

#### [ Kevin Buzzard (Mar 14 2018 at 23:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/conv%20example/near/123724383):
<p>because I am an old man</p>

#### [ Kevin Buzzard (Mar 14 2018 at 23:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/conv%20example/near/123724420):
<p>so no I don't know about the bazillion simp options</p>

#### [ Kevin Buzzard (Mar 14 2018 at 23:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/conv%20example/near/123724424):
<p>if you just rattled a few off now I might add them to the docs</p>

#### [ Kevin Buzzard (Mar 14 2018 at 23:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/conv%20example/near/123724426):
<p>I am in my late 40s :-)</p>

#### [ Mario Carneiro (Mar 14 2018 at 23:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/conv%20example/near/123724430):
<div class="codehilite"><pre><span></span>structure simp_config :=
(max_steps : nat           := simp.default_max_steps)
(contextual : bool         := ff)
(lift_eq : bool            := tt)
(canonize_instances : bool := tt)
(canonize_proofs : bool    := ff)
(use_axioms : bool         := tt)
(zeta : bool               := tt)
(beta : bool               := tt)
(eta  : bool               := tt)
(proj : bool               := tt) -- reduce projections
(iota : bool               := tt)
(iota_eqn : bool           := ff) -- reduce using all equation lemmas generated by equation/pattern-matching compiler
(constructor_eq : bool     := tt)
(single_pass : bool        := ff)
(fail_if_unchanged         := tt)
(memoize                   := tt)
</pre></div>

#### [ Mario Carneiro (Mar 14 2018 at 23:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/conv%20example/near/123724441):
<p>as you can see, leo is hard at work with those docstrings :)</p>

#### [ Kevin Buzzard (Mar 14 2018 at 23:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/conv%20example/near/123724688):
<p>two out of 16 ain't bad, as Meat Loaf once said</p>

#### [ Kevin Buzzard (Mar 14 2018 at 23:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/conv%20example/near/123724692):
<p>I am now going to have to rewrite some of my updated simp docs which I was editing as this post arrived.</p>

#### [ Kevin Buzzard (Mar 14 2018 at 23:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/conv%20example/near/123724735):
<p>About to be deleted: <code>It is well-known that there are a bazillion simp options, although most are known only to the Lean Inner Circle. Examples which mere mortals know about are those documented in the reference manual and Theorem Proving In Lean.</code></p>

#### [ Mario Carneiro (Mar 14 2018 at 23:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/conv%20example/near/123724966):
<p>That's not even all of it - there is also the underlying command <code>ext_simplify_core</code> with lots of space for configurability. And <code>dsimp</code> has its own variants on all of this.</p>

#### [ Kevin Buzzard (Mar 14 2018 at 23:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/conv%20example/near/123725306):
<p>There are more options somehow:</p>

#### [ Kevin Buzzard (Mar 14 2018 at 23:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/conv%20example/near/123725311):
<p><code>simp tactics in interactive mode have a new configuration parameter (discharger : tactic unit) a tactic for discharging subgoals created by the simplifier. If the tactic fails, the simplifier tries to discharge the subgoal by reducing it to true. Example: simp {discharger := assumption}.</code></p>

#### [ Kevin Buzzard (Mar 14 2018 at 23:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/conv%20example/near/123725317):
<p>from the changelog</p>

#### [ Kevin Buzzard (Mar 14 2018 at 23:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/conv%20example/near/123725379):
<p>I can't get this to work though</p>

#### [ Kevin Buzzard (Mar 14 2018 at 23:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/conv%20example/near/123725587):
<p>OK I added some stuff about simp config options and added it to my PR</p>

#### [ Mario Carneiro (Mar 14 2018 at 23:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/conv%20example/near/123725662):
<p>the <code>discharger</code>is a <code>tactic unit</code>, so you have to write it in non-interactive mode (or else have <code>tactic</code> open, which is I think what Leo did in that quote). <code>simp {discharger := `[assumption]}</code> should work</p>

#### [ Mario Carneiro (Mar 14 2018 at 23:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/conv%20example/near/123725719):
<p>but it's not that useful compared to <code>simp *</code></p>


{% endraw %}
