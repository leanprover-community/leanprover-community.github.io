---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/29713formalizingexactsequence.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [formalizing exact sequence](https://leanprover-community.github.io/archive/113488general/29713formalizingexactsequence.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Kenny Lau (Mar 27 2018 at 16:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124273688):
<p>How would you formalize exact sequences in Lean? Let's say they are R-modules for a commutative ring R.<br>
I have the following exact sequences in mind:</p>
<p>1. 0-&gt;A-&gt;B<br>
2. A-&gt;B-&gt;C<br>
3. A-&gt;B-&gt;C<br>
4. 0-&gt;A-&gt;B-&gt;C<br>
5. 0-&gt;A-&gt;B-&gt;C-&gt;0<br>
6. A-&gt;B-&gt;C-&gt;0<br>
7. ...-&gt;An-&gt;...-&gt;A3-&gt;A2-&gt;A1-&gt;A0</p>

#### [ Kenny Lau (Mar 27 2018 at 16:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124273698):
<p>0-&gt;A-&gt;B-&gt;C-&gt;D-&gt;0 is relatively rare but are still used</p>

#### [ Kenny Lau (Mar 27 2018 at 16:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124273706):
<p>short exact sequences could be a special case</p>

#### [ Simon Hudon (Mar 27 2018 at 16:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124273899):
<p>What is the difference between an exact sequence and a list?</p>

#### [ jmc (Mar 27 2018 at 16:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124274112):
<p><span class="user-mention" data-user-id="110026">@Simon Hudon</span>  The fact that you have morphisms f_n: A_n \to A_{n-1} that satisfy the condition im(f_n) = ker(f_{n-1}).</p>

#### [ Simon Hudon (Mar 27 2018 at 16:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124274177):
<p>So if you take A -&gt; B -&gt; C, that sequence has to have a morphism from A to B and from B to C? Is it meaningful to have an empty sequence?</p>

#### [ jmc (Mar 27 2018 at 16:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124274206):
<p>Hmmm, I guess one can give it meaning.</p>

#### [ jmc (Mar 27 2018 at 16:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124274253):
<p>But probably it is never used.</p>

#### [ jmc (Mar 27 2018 at 16:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124274256):
<p>I can't remember ever seeing it</p>

#### [ Kevin Buzzard (Mar 27 2018 at 16:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124274259):
<p>You have n&gt;=1 objects in a list, and n-1 morphisms from A[i] to A[i+1]</p>

#### [ Simon Hudon (Mar 27 2018 at 16:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124274261):
<p>Ok, let's leave it out if we have to</p>

#### [ Kevin Buzzard (Mar 27 2018 at 16:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124274268):
<p>and you demand that in the n-2 situations for which it makes sense,</p>

#### [ Simon Hudon (Mar 27 2018 at 16:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124274270):
<p>(the empty sequence that is)</p>

#### [ Kevin Buzzard (Mar 27 2018 at 16:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124274276):
<p>image of j'th map is kernel of (j+1)st</p>

#### [ Kevin Buzzard (Mar 27 2018 at 16:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124274285):
<p>It says nothing for n&lt;3</p>

#### [ Kevin Buzzard (Mar 27 2018 at 16:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124274293):
<p>and nobody ever uses it either (i.e. it's not a useful special case of anything, in contrast to sum(i=1,n,f(i)) which can be sensibly and usefully interpreted as zero when n=0)</p>

#### [ Simon Hudon (Mar 27 2018 at 16:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124274340):
<p>Ok, I have an idea, I'll just write up something and show it to you guys</p>

#### [ Kevin Buzzard (Mar 27 2018 at 16:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124274342):
<p>it's also a useful concept for Z_{&gt;=0} and Z_{&lt;=0} and Z</p>

#### [ Kevin Buzzard (Mar 27 2018 at 16:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124274346):
<p>i.e. A0-&gt;A1-&gt;A2-&gt;... being exact</p>

#### [ Kevin Buzzard (Mar 27 2018 at 16:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124274353):
<p>and ...-&gt;B2-&gt;B1-&gt;B0 being exact</p>

#### [ Kevin Buzzard (Mar 27 2018 at 16:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124274358):
<p>and ...-&gt;A_{n-1}-&gt;A_n-&gt;A_{n+1}-&gt;... being exact</p>

#### [ Kevin Buzzard (Mar 27 2018 at 16:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124274360):
<p>and I think that covers everything</p>

#### [ Kevin Buzzard (Mar 27 2018 at 16:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124274361):
<p>that I see in practice</p>

#### [ Simon Hudon (Mar 27 2018 at 16:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124274364):
<p>Thanks! What's the type of <code>im</code> and <code>ker</code>?</p>

#### [ jmc (Mar 27 2018 at 16:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124274425):
<p><span class="user-mention" data-user-id="110026">@Simon Hudon</span> so there are two conventions: either <code>target(f_n) = source(f_{n+1})</code>, or <code>source(f_n) = target(f_{n+1})</code></p>

#### [ jmc (Mar 27 2018 at 16:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124274432):
<p>im and ker are both also R-modules</p>

#### [ Kevin Buzzard (Mar 27 2018 at 16:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124274434):
<p>depending on whether you're doing homology or cohomology</p>

#### [ jmc (Mar 27 2018 at 16:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124274436):
<p>or maybe R-submodules of the object that they are a sub of</p>

#### [ jmc (Mar 27 2018 at 16:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124274496):
<p>Do you guys think it might be useful to first formalise complexes? That is <code>im(f_n) \subset ker(f_{n+1})</code> or equivalently <code>f_{n+1} \circ f_n = 0</code>.</p>

#### [ Simon Hudon (Mar 27 2018 at 16:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124274644):
<p>I have encoded something without the relationship between morphisms, I just want to check if that makes sense to you guys before encoding that condition</p>

#### [ Simon Hudon (Mar 27 2018 at 16:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124274648):
<div class="codehilite"><pre><span></span>universe u

constant morphism : Type u → Type u → Type u

inductive exact_seq : list (Type u) → Type (u+1)
 | nil (a : Type u) : exact_seq [a]
 | cons (a b : Type u) (tail : list (Type u)) :
   morphism a b →
   exact_seq (b :: tail) →
   exact_seq (a :: b :: tail)
</pre></div>

#### [ Johannes Hölzl (Mar 27 2018 at 16:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124274669):
<p>There are also exact sequences in HoTT Lean 2: <a href="https://github.com/cmu-phil/Spectral" target="_blank" title="https://github.com/cmu-phil/Spectral">https://github.com/cmu-phil/Spectral</a>, see <a href="https://github.com/cmu-phil/Spectral/blob/master/algebra/exactness.hlean" target="_blank" title="https://github.com/cmu-phil/Spectral/blob/master/algebra/exactness.hlean">https://github.com/cmu-phil/Spectral/blob/master/algebra/exactness.hlean</a> <br>
But this is HoTT Lean, so there are a lot of differences now to current Lean. Also the definitions might be very constructive...</p>

#### [ jmc (Mar 27 2018 at 16:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124274734):
<p><span class="user-mention" data-user-id="110026">@Simon Hudon</span> What is <code>constant morphism</code> supposed to do? Because I don't really get it...</p>

#### [ Simon Hudon (Mar 27 2018 at 16:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124274745):
<p>It's just a way of having morphisms in my definition without depending on any specific definition of morphism.</p>

#### [ jmc (Mar 27 2018 at 16:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124274801):
<p>I see, makes sense now</p>

#### [ Simon Hudon (Mar 27 2018 at 16:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124274867):
<p>You could actually make it a parameter of the whole thing</p>

#### [ jmc (Mar 27 2018 at 16:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124274875):
<p><span class="user-mention" data-user-id="110026">@Simon Hudon</span>  I think this works, but not for sequences indexed by Z, right?</p>

#### [ Simon Hudon (Mar 27 2018 at 16:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124274921):
<p>Meaning that instead of a list as the index of your sequence, you'd like a function from a contiguous interval of Z to the type in question?</p>

#### [ Simon Hudon (Mar 27 2018 at 16:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124274935):
<p>You could match this with a single Z which is an offset for every index of the N based indices of the list</p>

#### [ Simon Hudon (Mar 27 2018 at 16:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124274989):
<p>Otherwise, you could replace the list but such a sequence not being an inductive type might not be pretty when you pattern match on an <code>exact_seq</code></p>

#### [ jmc (Mar 27 2018 at 16:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124274993):
<p>yes, but you the interval need not be bounded</p>

#### [ Simon Hudon (Mar 27 2018 at 16:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124274998):
<p>Ah yes, I see</p>

#### [ jmc (Mar 27 2018 at 16:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124275003):
<p>so then it won't be inductive... probably</p>

#### [ jmc (Mar 27 2018 at 16:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124275007):
<p>So intuitively it is a function: Z -&gt; morphisms</p>

#### [ jmc (Mar 27 2018 at 16:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124275047):
<p>but the problem is that actually the target depends on the element n \in Z</p>

#### [ Simon Hudon (Mar 27 2018 at 16:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124275053):
<p>Yeah ... alternatively, I'm working on a construction for coinductive types. You could use that to make a possibly "doubly" infinite, Z indexed sequence</p>

#### [ Simon Hudon (Mar 27 2018 at 16:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124275127):
<p>At the moment, maybe the best thing to do is have an interval type and make functions from that interval to the types that your sequence contains</p>

#### [ Kenny Lau (Mar 27 2018 at 16:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124275459):
<p>so what's the verdict</p>

#### [ jmc (Mar 27 2018 at 16:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124275514):
<p><span class="user-mention" data-user-id="110064">@Kenny Lau</span> Do you want/need unbounded sequences?</p>

#### [ jmc (Mar 27 2018 at 16:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124275516):
<p>Or is finite enough?</p>

#### [ Kenny Lau (Mar 27 2018 at 16:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124275518):
<p>preferably</p>

#### [ Kenny Lau (Mar 27 2018 at 16:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124275522):
<p>indexing by N is good</p>

#### [ Simon Hudon (Mar 27 2018 at 16:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124275573):
<p>should finite and infinite sequences be the same type or would it be good enough to have separate constructions?</p>

#### [ jmc (Mar 27 2018 at 16:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124275574):
<p>then I guess the inductive definition that Simon proposed is the best option</p>

#### [ Kenny Lau (Mar 27 2018 at 16:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124275582):
<p>I can do with separate</p>

#### [ Kenny Lau (Mar 27 2018 at 16:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124275588):
<p>or just make finite a special case of infinite (with all objects being eventually 0)</p>

#### [ jmc (Mar 27 2018 at 16:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124275592):
<p><span class="user-mention" data-user-id="110026">@Simon Hudon</span> I think they can be different types, and then an <code>extend_with_zeros</code> function from the finite to infinite sequences</p>

#### [ Simon Hudon (Mar 27 2018 at 16:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124275594):
<p>Cool</p>

#### [ Simon Hudon (Mar 27 2018 at 16:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124275712):
<p>I have not covered the <code> im(f_n) \subset ker(f_{n+1}) </code> bit but I think an inductive predicate would be a nice way of asserting that</p>

#### [ Simon Hudon (Mar 27 2018 at 17:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124276058):
<p>Here's how I would build that predicate (I'm not sure for the type of <code>ker</code> and <code>im</code> but it seems to capture part of the idea at least)</p>
<div class="codehilite"><pre><span></span>universe u

constant morphism : Type u → Type u → Type u

constant ker : Π {a b : Type u}, morphism a b → a
constant im : Π {a b : Type u}, morphism a b → b

inductive exact_seq : list (Type u) → Type (u+1)
 | nil (a : Type u) : exact_seq [a]
 | cons {a b : Type u} {tail : list (Type u)} :
   morphism a b →
   exact_seq (b :: tail) →
   exact_seq (a :: b :: tail)

inductive is_exact : Π {s}, exact_seq s → Type (u+1)
 | nil {a b : Type u} (f : morphism a b) : is_exact (exact_seq.cons f $ exact_seq.nil b)
 | cons (a b c : Type u) (tail : list (Type u))
        (f : morphism a b) (g : morphism b c)
        (s : exact_seq (c :: tail)) :
   ker g = im f →
   is_exact (exact_seq.cons g s) →
   is_exact (exact_seq.cons f $ exact_seq.cons g s)
</pre></div>

#### [ Patrick Massot (Mar 27 2018 at 17:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124276259):
<p>Guys... you are really crazy about inductive types</p>

#### [ Simon Hudon (Mar 27 2018 at 17:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124276271):
<p>... in a bad way?</p>

#### [ Patrick Massot (Mar 27 2018 at 17:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124276277):
<p>I think this would be a nightmare to work with</p>

#### [ Patrick Massot (Mar 27 2018 at 17:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124276282):
<p>How are you going to define morphisms of complexes?</p>

#### [ Patrick Massot (Mar 27 2018 at 17:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124276294):
<p>Why do you need to complicate everything</p>

#### [ Patrick Massot (Mar 27 2018 at 17:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124276356):
<p>Why not defining a sequence to be a map C from I to R-mod (where I is an interval in integers) and a map d from I to linear maps from C i to C (i+1)?</p>

#### [ Patrick Massot (Mar 27 2018 at 17:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124276412):
<p>and then adding condition on d (i + 1) and d i  for all i</p>

#### [ Patrick Massot (Mar 27 2018 at 17:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124276417):
<p>to get either complexes or exact sequences</p>

#### [ Patrick Massot (Mar 27 2018 at 17:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124276433):
<p>Anyway, did anyone check whether <span class="user-mention" data-user-id="110087">@Scott Morrison</span> already did all that in his category lib, for arbitraray abelian categories?</p>

#### [ Simon Hudon (Mar 27 2018 at 17:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124276435):
<p>You mean a bit like this?</p>
<div class="codehilite"><pre><span></span>open nat
variable s : stream (Type u)

def inf_seq := Π n, morphism (s n) (s $ succ n)
variables {s} (x : inf_seq s)
def inf_exact_seq := Π n, im (x n) = ker (x _)
</pre></div>

#### [ Simon Hudon (Mar 27 2018 at 17:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124276442):
<p>I thought of doing that for intervals of integers too</p>

#### [ Patrick Massot (Mar 27 2018 at 17:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124276444):
<p>What is stream?</p>

#### [ Simon Hudon (Mar 27 2018 at 17:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124276493):
<p>What annoys me is the <code>+1</code> for which you need some tricks to make it type correct</p>

#### [ Simon Hudon (Mar 27 2018 at 17:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124276497):
<p><code>def stream (a) := ℕ -&gt; a</code></p>

#### [ Patrick Massot (Mar 27 2018 at 17:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124276512):
<p>What is this <code>+1</code> issue?</p>

#### [ Simon Hudon (Mar 27 2018 at 17:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124276565):
<p>If you use it directly, with <code>I</code> an interval on integers and <code>i : I</code>, <code>↑i + 1 : ℤ</code> so you need to feed in a proof that it's also part of the interval</p>

#### [ Simon Hudon (Mar 27 2018 at 17:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124276607):
<p>Actually, now that I write it out loud, it doesn't seem that bad</p>

#### [ Patrick Massot (Mar 27 2018 at 17:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124276611):
<p>Don't do that</p>

#### [ Simon Hudon (Mar 27 2018 at 17:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124276614):
<p>It's just going to be one ugly index</p>

#### [ Simon Hudon (Mar 27 2018 at 17:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124276618):
<p>What would you do?</p>

#### [ Patrick Massot (Mar 27 2018 at 17:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124276620):
<p>Define <code>C i</code> to be the zero module if <code>i</code> is not in the interval</p>

#### [ Patrick Massot (Mar 27 2018 at 17:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124276636):
<p>So all sequences are indexed by <code>ℤ</code></p>

#### [ Simon Hudon (Mar 27 2018 at 17:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124276683):
<p>Ok, so do you overload the function application operator or do you actually work with <code>ℤ → Type</code>? In the second case, you'll get into ugliness with defining extensionality</p>

#### [ Simon Hudon (Mar 27 2018 at 17:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124276691):
<p>But in the first case ... I think it can work</p>

#### [ Patrick Massot (Mar 27 2018 at 17:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124276702):
<p>What ugliness?</p>

#### [ Patrick Massot (Mar 27 2018 at 17:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124276709):
<p>what extensionality?</p>

#### [ Simon Hudon (Mar 27 2018 at 17:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124276753):
<p>If you want to prove the equality of two sequences ... <em>trail off</em></p>

#### [ Patrick Massot (Mar 27 2018 at 17:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124276757):
<p>I hope you're not about to write the c word</p>

#### [ Simon Hudon (Mar 27 2018 at 17:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124276769):
<p>I'm not sure what your c word is ... comparison?</p>

#### [ Patrick Massot (Mar 27 2018 at 17:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124276774):
<p>constructively</p>

#### [ Simon Hudon (Mar 27 2018 at 17:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124276828):
<p>Haha! I'm more into classical reasoning, relax <span class="emoji emoji-1f61d" title="stuck out tongue closed eyes">:stuck_out_tongue_closed_eyes:</span></p>

#### [ Simon Hudon (Mar 27 2018 at 17:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124277060):
<p>Here's what I would do then:</p>
<div class="codehilite"><pre><span></span>structure interval (left right : option ℤ) :=
  (val : ℤ)
  (left_bounded : ∀ h₀, @option.get _ left h₀ ≤ val)
  (right_bounded : ∀ h₀, val ≤ @option.get _ right h₀)

structure seq (x y : option ℤ) (a : Type u) :=
  (f : interval x y → a)

instance {x y : option ℤ} {a} [has_zero a] : has_coe_to_fun (seq x y a) :=
  { F := λ _, ℤ → a
  , coe := λ ⟨f⟩ i, if h : _ ∧ _ then f ⟨i,h.1,h.2⟩ else 0 }
</pre></div>

#### [ Kenny Lau (Mar 27 2018 at 17:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124277134):
<p><span class="user-mention" data-user-id="110031">@Patrick Massot</span> you really hate inductive definitions</p>

#### [ Patrick Massot (Mar 27 2018 at 17:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124277135):
<p>Nice. I need to go but I'm sure Kenny and Kevin will get something here</p>

#### [ Patrick Massot (Mar 27 2018 at 17:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124277143):
<p><span class="user-mention" data-user-id="110064">@Kenny Lau</span> I don't hate them, I try to formalize maths using the same kind of thinking used in real world maths</p>

#### [ Patrick Massot (Mar 27 2018 at 17:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124277145):
<p>This may be a mistake</p>

#### [ Patrick Massot (Mar 27 2018 at 17:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124277159):
<p>But I'd like to try that for a while before switching to an orthogonal way of thinking about maths</p>

#### [ Patrick Massot (Mar 27 2018 at 17:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124277161):
<p>And those days I have zero time for serious Lean <span class="emoji emoji-1f61e" title="disappointed">:disappointed:</span></p>

#### [ Patrick Massot (Mar 27 2018 at 17:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124277162):
<p>only a bit of Zulip chat</p>

#### [ Patrick Massot (Mar 27 2018 at 17:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124277209):
<p>And now I really need to go</p>

#### [ Kenny Lau (Mar 27 2018 at 17:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124277345):
<p><span class="user-mention" data-user-id="110026">@Simon Hudon</span> ok now I have two new things:<br>
1. exact sequences should be a subtype (not the {x // p x} kind of subtype) of sequences in general, where sequences in this context mean sequences with morphisms. to give more context, there's a type of sequences with im f_n subset ker f_(n+1) instead of equal, i.e. if I call the maps d we have d^2=0.<br>
2. we need to think about what our objects can be</p>

#### [ Simon Hudon (Mar 27 2018 at 17:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124277598):
<p>When you say <code> im f_n subset ker f_(n+1) </code>, is this strictly in the sense of sets or are you thinking about subsets of various structures like modules?</p>

#### [ Kenny Lau (Mar 27 2018 at 17:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124277791):
<p>well both would be subset of the object Cn</p>

#### [ Kenny Lau (Mar 27 2018 at 17:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124277797):
<p>and also I meant im f_(n+1) subset ker f_n</p>

#### [ Simon Hudon (Mar 27 2018 at 18:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124278160):
<p>So maybe this would help. If needed, we can change the <code>=</code> with <code>\subset</code></p>

#### [ Simon Hudon (Mar 27 2018 at 18:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124278162):
<div class="codehilite"><pre><span></span>structure exact_seq (x y : option ℤ) (A : Type u) [has_zero A] :=
  (f : seq x y A)
  (m : Π n, morphism (f n) (f $ n+1))
  (eq : Π n, ker (m $ n + 1) = im (m n))
</pre></div>

#### [ Simon Hudon (Mar 27 2018 at 18:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124278217):
<p>That would involve a morphism from the last object to 0 and from the first object to 0 of which I don't know if it makes sense</p>

#### [ Kenny Lau (Mar 27 2018 at 18:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124278222):
<p>hmm, it seems you're doing it very generally</p>

#### [ Kenny Lau (Mar 27 2018 at 18:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124278224):
<p>in regards to my second question</p>

#### [ Simon Hudon (Mar 27 2018 at 18:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124278226):
<p>Maybe we can choose a better constant than 0 to make it make sense</p>

#### [ Kenny Lau (Mar 27 2018 at 18:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124278237):
<p>no, 0 always makes sense</p>

#### [ Kenny Lau (Mar 27 2018 at 18:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124278241):
<p>but what do you mean from the last object to 0</p>

#### [ Simon Hudon (Mar 27 2018 at 18:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124278243):
<p>And morphisms to and from 0 make sense to?</p>

#### [ Kenny Lau (Mar 27 2018 at 18:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124278246):
<p>yes</p>

#### [ Kenny Lau (Mar 27 2018 at 18:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124278254):
<p>it's called the zero object in category theory</p>

#### [ Simon Hudon (Mar 27 2018 at 18:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124278305):
<p>Thanks, I'll read up on that</p>

#### [ Kenny Lau (Mar 27 2018 at 18:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124278307):
<p>it has a unique morphism to and from every object</p>

#### [ Simon Hudon (Mar 27 2018 at 18:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124278324):
<p>The morphisms have type <code>m : Π n : ℤ, morphism (f n) (f $ n+1)</code> which means that there exists a morphism for every integer even when your sequence is finite</p>

#### [ Kenny Lau (Mar 27 2018 at 18:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124278331):
<p>so your answer to my second question is basically any type with a zero object?</p>

#### [ Simon Hudon (Mar 27 2018 at 18:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124278333):
<p>Exactly</p>

#### [ Simon Hudon (Mar 27 2018 at 18:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124278375):
<p>Sorry, not quite</p>

#### [ Simon Hudon (Mar 27 2018 at 18:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124278381):
<p>I used <code>morphism</code> as a sort of place holder. Maybe you should have <code>A</code> be a category</p>

#### [ Simon Hudon (Mar 27 2018 at 18:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124278385):
<p>and take the morphism from there</p>

#### [ Kenny Lau (Mar 27 2018 at 18:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124278388):
<p>"there exists a morphism for every integer even when your sequence is finite" fits with the convention that short exact sequences are special cases of long exact sequences with objects being eventually zero</p>

#### [ Kenny Lau (Mar 27 2018 at 18:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124278392):
<p>so that makes sense</p>

#### [ Kenny Lau (Mar 27 2018 at 18:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124278397):
<p>in the category setting, exact sequences only make sense in abelian categories</p>

#### [ Kenny Lau (Mar 27 2018 at 18:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124278404):
<p>but i don't know whether it would be more useful to have any abelian categories, or just modules</p>

#### [ Simon Hudon (Mar 27 2018 at 18:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124278478):
<p>Are the Abelian categories where the 0 is defined?</p>

#### [ Kenny Lau (Mar 27 2018 at 18:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124278490):
<p>abelian categories have 0</p>

#### [ Kenny Lau (Mar 27 2018 at 18:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124278492):
<p>it has more things</p>

#### [ Simon Hudon (Mar 27 2018 at 18:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124278549):
<p>I'd be tempted to suggest to keep it a general definition with the Abelian category and use additional information (e.g. is a module) in the lemmas where it is relevant</p>

#### [ Kenny Lau (Mar 27 2018 at 18:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124278569):
<p>alright</p>

#### [ Simon Hudon (Mar 27 2018 at 18:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124278570):
<p>You might also want to layer the structure in such a way that you can vary on <code> Π n, ker (m $ n + 1) = im (m n)</code></p>

#### [ Kenny Lau (Mar 27 2018 at 18:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124278571):
<p>what do you mean?</p>

#### [ Simon Hudon (Mar 27 2018 at 18:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124278628):
<p>you were mentioning subsets relations so here is how I would encode the different flavors:</p>

#### [ Kenny Lau (Mar 27 2018 at 18:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124278650):
<p>oh and my first point means that maybe it can be a hierarchy, complex -&gt; exact sequences</p>

#### [ Simon Hudon (Mar 27 2018 at 18:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124278652):
<div class="codehilite"><pre><span></span>structure base_exact_seq (x y : option ℤ) (A : Type u) [has_zero A] :=
  (f : seq x y A)
  (m : Π n, morphism (f n) (f $ n+1))

structure exact_seq_eq (x y : option ℤ) (A : Type u) [has_zero A] extends base_exact_seq x y A :=
  (eq : Π n, ker (m $ n + 1) = im (m n))

structure exact_seq_sub (x y : option ℤ) (A : Type u) [has_zero A] extends base_exact_seq x y A :=
  (eq : Π n, ker (m $ n + 1) ⊆ im (m n))

structure exact_seq_super (x y : option ℤ) (A : Type u) [has_zero A] extends base_exact_seq x y A :=
  (eq : Π n, ker (m $ n + 1) ⊇ im (m n))
</pre></div>

#### [ Simon Hudon (Mar 27 2018 at 18:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124278714):
<blockquote>
<p>oh and my first point means that maybe it can be a hierarchy, complex -&gt; exact sequences</p>
</blockquote>
<p>I don't understand that. Are you saying that complex numbers are somehow a more general notion than exact sequences?</p>

#### [ Kenny Lau (Mar 27 2018 at 18:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124278782):
<p>complexes are instead of having im=ker, you have im subset ker</p>

#### [ Kenny Lau (Mar 27 2018 at 18:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124278783):
<p>more compactly, f_(n+1) f_n = 0</p>

#### [ Kenny Lau (Mar 27 2018 at 18:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124278785):
<p>even more compactly, f^2=0</p>

#### [ Simon Hudon (Mar 27 2018 at 18:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124278813):
<p>Ah! I see</p>

#### [ Simon Hudon (Mar 27 2018 at 18:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124278858):
<p>You might want instances of <code>has_coe</code> between those. Otherwise you'll hit the new structure constraint against repeated fields</p>

#### [ Simon Hudon (Mar 27 2018 at 18:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124278929):
<p>Alright, I'll need to sign off now and get some writing done. I hope this helped</p>

#### [ Kenny Lau (Mar 27 2018 at 18:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124278935):
<p>ok thanks</p>

#### [ Kenny Lau (Mar 27 2018 at 18:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124279770):
<p>I think I'm wrong. You can't just fill in zeroes to make a long exact sequence from a short one</p>

#### [ Kenny Lau (Mar 27 2018 at 18:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124279772):
<p>you can do that for complexes, not exact sequences</p>

#### [ Kenny Lau (Mar 27 2018 at 18:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124279775):
<p>oh well it's more troublesome</p>

#### [ Kenny Lau (Mar 27 2018 at 18:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124279782):
<p>if you have A-&gt;B-&gt;C</p>

#### [ Kenny Lau (Mar 27 2018 at 18:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124279784):
<p>you can encode it inside ...-&gt;0-&gt;0-&gt;ker f-&gt;A-&gt;B-&gt;C-&gt;coker g-&gt;0-&gt;0-&gt;...</p>

#### [ Kenny Lau (Mar 27 2018 at 18:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124279785):
<p>but that's troublesome</p>

#### [ Kenny Lau (Mar 27 2018 at 18:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124279786):
<p>but most short exact sequences end and start with zero</p>

#### [ Kenny Lau (Mar 27 2018 at 18:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124279790):
<p>but there are also those that do not, e.g. in dealing with tensors</p>

#### [ jmc (Mar 27 2018 at 19:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124280782):
<p>But Simon's proposal includes bounded sequences, right?</p>

#### [ Andrew Ashworth (Mar 27 2018 at 20:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124283973):
<p>maybe you could ask Floris about exact sequences, seeing as how they are working with spectral sequences in HoTT</p>

#### [ Andrew Ashworth (Mar 27 2018 at 20:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124284031):
<p>the sequences repository linked earlier is really quite extensive</p>

#### [ Simon Hudon (Mar 28 2018 at 20:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124331318):
<blockquote>
<p>But Simon's proposal includes bounded sequences, right?</p>
</blockquote>
<p>Yes exactly. The sequence has no information from outside its bounds except that you can still look beyond the bounds and get <code>0</code>. Right now, it requires you to provide morphisms even for (non-)elements outside the bounds of the sequence. We can probably change that</p>

#### [ Mario Carneiro (Mar 28 2018 at 20:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124331770):
<p>Although it's possible to represent N, Z, fin sequences all as special cases of the same thing, I'm not convinced it's worth it - when you want to work with it you will have a lot of redundant structure and it will be cumbersome to talk about the objects</p>

#### [ Mario Carneiro (Mar 28 2018 at 20:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124331815):
<p>Maybe you could have both the general structure and the special cases, with coercions or similar embeddings</p>

#### [ Simon Hudon (Mar 28 2018 at 20:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124332292):
<p>That was my first proposal but I got some push back because I was representing finite sequences as inductive types</p>

#### [ Mario Carneiro (Mar 28 2018 at 20:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124332552):
<p>I need to figure out how Patrick got traumatized by inductive types, because they are much easier in lean formalization than index arithmetic</p>

#### [ Simon Hudon (Mar 28 2018 at 20:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124332704):
<p>I'm wondering in this situation if having one construction instead of four might be easier to work with</p>

#### [ Mario Carneiro (Mar 28 2018 at 20:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124332730):
<p>I think it is important how the construction is to be used to answer that question</p>

#### [ Simon Hudon (Mar 28 2018 at 20:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124332813):
<p>Yeah, that makes sense.</p>

#### [ Mario Carneiro (Mar 28 2018 at 20:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124332827):
<p>One way to encode the +1 stuff is to have a graph relation predicate, so that it becomes closer to a diagram in the category theory sense</p>

#### [ Mario Carneiro (Mar 28 2018 at 20:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124332835):
<p>i.e. using <code>inductive P : I -&gt; I -&gt; Prop | mk (n) : P n (n+1)</code></p>

#### [ Simon Hudon (Mar 28 2018 at 20:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124332995):
<p>You would use that with the construction with intervals?</p>

#### [ Kevin Buzzard (Mar 28 2018 at 20:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124333093):
<p>The thing about inductive types is that whilst they're clearly a very cute computer science way to do things, especially if you want to prove things by induction,</p>

#### [ Kevin Buzzard (Mar 28 2018 at 20:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124333100):
<p>when a mathematician thinks of an exact sequence they really do not think of it as an "inductive gadget"</p>

#### [ Kevin Buzzard (Mar 28 2018 at 20:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124333110):
<p>and the same is true probably for lots of things like graphs or trees or something, which CS people seem to love constructing via inductive data types</p>

#### [ Kevin Buzzard (Mar 28 2018 at 20:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124333119):
<p>but which mathematicians just build in a completely different way.</p>

#### [ Kevin Buzzard (Mar 28 2018 at 20:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124333129):
<p>Probably because they rarely prove anything by induction, they're just interested in other questions.</p>

#### [ Kevin Buzzard (Mar 28 2018 at 20:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124333134):
<p>I mean, on things like trees or exact sequences</p>

#### [ Mario Carneiro (Mar 28 2018 at 20:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124333175):
<p>I think the mathematician is generally not worried about the particular representation, because they never go into the gory details anyway</p>

#### [ Kevin Buzzard (Mar 28 2018 at 20:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124333181):
<p>You might be right.</p>

#### [ Kevin Buzzard (Mar 28 2018 at 20:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124333184):
<p>I remember Patrick saying something like "this is so far from what I would write on the blackboard"</p>

#### [ Kevin Buzzard (Mar 28 2018 at 20:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124333204):
<p>but perhaps what he means by this is that the informal idea is so clear to a mathematician that they don't need to spell out such a recursive definition.</p>

#### [ Kevin Buzzard (Mar 28 2018 at 20:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124333218):
<p>Perhaps the natural numbers are a great example. They're just "the natural numbers, duh"</p>

#### [ Kevin Buzzard (Mar 28 2018 at 20:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124333222):
<p>and you learn them when you're 4 years old</p>

#### [ Kevin Buzzard (Mar 28 2018 at 20:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124333230):
<p>and you don't learn proof by induction until you're 17 (at least in the UK)</p>

#### [ Kevin Buzzard (Mar 28 2018 at 20:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124333238):
<p>So I define the natural numbers in my class as "N := {1,2,3,...}"</p>

#### [ Kevin Buzzard (Mar 28 2018 at 20:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124333281):
<p>and Patrick defines them as "N := {0,1,2,3,...}"</p>

#### [ Kevin Buzzard (Mar 28 2018 at 20:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124333289):
<p>and that's what gets written on the blackboard, forget about nat.succ etc</p>

#### [ Kevin Buzzard (Mar 28 2018 at 20:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124333356):
<p>I'm just reading the part about formal v informal proofs in Software Foundations. You might want to argue that mathematicians often give "informal definitions".</p>

#### [ Kevin Buzzard (Mar 28 2018 at 21:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124333447):
<p>Mathematicians use the word induction like this: "Theorem: <span class="katex"><span class="katex-mathml"><math><semantics><mrow><msubsup><mi mathvariant="normal">Σ</mi><mrow><mi>i</mi><mo>=</mo><mn>1</mn></mrow><mi>n</mi></msubsup><msup><mi>i</mi><mn>2</mn></msup><mo>=</mo><mi>n</mi><mo>(</mo><mi>n</mi><mo>+</mo><mn>1</mn><mo>)</mo><mo>(</mo><mn>2</mn><mi>n</mi><mo>+</mo><mn>1</mn><mo>)</mo><mi mathvariant="normal">/</mi><mn>6</mn><mi mathvariant="normal">.</mi></mrow><annotation encoding="application/x-tex">\Sigma_{i=1}^n i^2=n(n+1)(2n+1)/6.</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.8141079999999999em;"></span><span class="strut bottom" style="height:1.072772em;vertical-align:-0.258664em;"></span><span class="base"><span class="mord"><span class="mord mathrm">Σ</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.664392em;"><span style="top:-2.441336em;margin-left:0em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight"><span class="mord mathit mtight">i</span><span class="mrel mtight">=</span><span class="mord mathrm mtight">1</span></span></span></span><span style="top:-3.063em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mathit mtight">n</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.258664em;"></span></span></span></span></span><span class="mord"><span class="mord mathit">i</span><span class="msupsub"><span class="vlist-t"><span class="vlist-r"><span class="vlist" style="height:0.8141079999999999em;"><span style="top:-3.063em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mathrm mtight">2</span></span></span></span></span></span></span></span><span class="mrel">=</span><span class="mord mathit">n</span><span class="mopen">(</span><span class="mord mathit">n</span><span class="mbin">+</span><span class="mord mathrm">1</span><span class="mclose">)</span><span class="mopen">(</span><span class="mord mathrm">2</span><span class="mord mathit">n</span><span class="mbin">+</span><span class="mord mathrm">1</span><span class="mclose">)</span><span class="mord mathrm">/</span><span class="mord mathrm">6</span><span class="mord mathrm">.</span></span></span></span> Proof: induction. <span class="tex-error">$$\qed$$</span></p>

#### [ Kevin Buzzard (Mar 28 2018 at 21:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124333457):
<p>not "definition of natural numbers by induction"</p>

#### [ Mario Carneiro (Mar 28 2018 at 21:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124333579):
<p>I think we should encourage an agnosticism wrt representations in lean as well, by means of abstracting a construction into its important properties. Once you've done this the exact definition doesn't matter. CS people know about this by the name "interface", mathematicians know this in the big cases via structures like "ring" that abstract a bunch of properties, but I think they are less used to doing this with every construction</p>

#### [ Simon Hudon (Mar 28 2018 at 21:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124333581):
<p>I think even if they don't see natural numbers as Peano's construction, "by induction" assumes an inductive definition underneath, often a well-founded relation ... unless you define induction as "a thing natural numbers can do"</p>

#### [ Mario Carneiro (Mar 28 2018 at 21:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124333612):
<p>For example, once you have defined the addition and multiplication on C, it stops mattering that the definition was R x R as opposed to something else</p>

#### [ Kevin Buzzard (Mar 28 2018 at 21:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124333721):
<p>The projectors are super-important on C</p>

#### [ Kevin Buzzard (Mar 28 2018 at 21:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124333733):
<p>I don't think mathematicians see N as any different to R in some sense</p>

#### [ Kevin Buzzard (Mar 28 2018 at 21:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124333739):
<p>sure you can do induction on one but not the other</p>

#### [ Kevin Buzzard (Mar 28 2018 at 21:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124333743):
<p>but who cares about some random property like induction.</p>

#### [ Kevin Buzzard (Mar 28 2018 at 21:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124333748):
<p>You guys are putting it on some sort of pedestal</p>

#### [ Kevin Buzzard (Mar 28 2018 at 21:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124333751):
<p>N and R are just sets of numbers that you can do stuff with</p>

#### [ Kevin Buzzard (Mar 28 2018 at 21:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124333820):
<p>I think I might spend some time over the summer making stuff into interfaces somehow. I am still concerned about manipulating finite sums. I want <span class="katex"><span class="katex-mathml"><math><semantics><mrow><msubsup><mi mathvariant="normal">Σ</mi><mrow><mi>i</mi><mo>=</mo><mn>1</mn></mrow><mi>n</mi></msubsup><msub><mi>a</mi><mi>i</mi></msub><mo>=</mo><msubsup><mi mathvariant="normal">Σ</mi><mrow><mi>i</mi><mo>=</mo><mn>1</mn></mrow><mi>n</mi></msubsup><msub><mi>a</mi><mrow><mi>n</mi><mo>+</mo><mn>1</mn><mo>−</mo><mi>i</mi></mrow></msub></mrow><annotation encoding="application/x-tex">\Sigma_{i=1}^na_i = \Sigma_{i=1}^na_{n+1-i}</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.68333em;"></span><span class="strut bottom" style="height:0.941994em;vertical-align:-0.258664em;"></span><span class="base"><span class="mord"><span class="mord mathrm">Σ</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.664392em;"><span style="top:-2.441336em;margin-left:0em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight"><span class="mord mathit mtight">i</span><span class="mrel mtight">=</span><span class="mord mathrm mtight">1</span></span></span></span><span style="top:-3.063em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mathit mtight">n</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.258664em;"></span></span></span></span></span><span class="mord"><span class="mord mathit">a</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.31166399999999994em;"><span style="top:-2.5500000000000003em;margin-left:0em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mathit mtight">i</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.15em;"></span></span></span></span></span><span class="mrel">=</span><span class="mord"><span class="mord mathrm">Σ</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.664392em;"><span style="top:-2.441336em;margin-left:0em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight"><span class="mord mathit mtight">i</span><span class="mrel mtight">=</span><span class="mord mathrm mtight">1</span></span></span></span><span style="top:-3.063em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mathit mtight">n</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.258664em;"></span></span></span></span></span><span class="mord"><span class="mord mathit">a</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.311664em;"><span style="top:-2.5500000000000003em;margin-left:0em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight"><span class="mord mathit mtight">n</span><span class="mbin mtight">+</span><span class="mord mathrm mtight">1</span><span class="mbin mtight">−</span><span class="mord mathit mtight">i</span></span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.208331em;"></span></span></span></span></span></span></span></span> to be trivial</p>

#### [ Kevin Buzzard (Mar 28 2018 at 21:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124333824):
<p>or at least "something with a name you can guess"</p>

#### [ Kevin Buzzard (Mar 28 2018 at 21:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124333878):
<p>and <span class="katex"><span class="katex-mathml"><math><semantics><mrow><msubsup><mi mathvariant="normal">Σ</mi><mrow><mi>i</mi><mo>=</mo><mn>1</mn></mrow><mi>n</mi></msubsup><msubsup><mi mathvariant="normal">Σ</mi><mrow><mi>j</mi><mo>=</mo><mn>1</mn></mrow><mi>i</mi></msubsup><mi mathvariant="normal">.</mi><mi mathvariant="normal">.</mi><mi mathvariant="normal">.</mi><mo>=</mo><msubsup><mi mathvariant="normal">Σ</mi><mrow><mi>j</mi><mo>=</mo><mn>1</mn></mrow><mi>n</mi></msubsup><msubsup><mi mathvariant="normal">Σ</mi><mrow><mi>i</mi><mo>=</mo><mi>j</mi></mrow><mi>n</mi></msubsup><mi mathvariant="normal">.</mi><mi mathvariant="normal">.</mi><mi mathvariant="normal">.</mi></mrow><annotation encoding="application/x-tex">\Sigma_{i=1}^n\Sigma_{j=1}^i ... = \Sigma_{j=1}^n\Sigma_{i=j}^n ...</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.824664em;"></span><span class="strut bottom" style="height:1.219436em;vertical-align:-0.394772em;"></span><span class="base"><span class="mord"><span class="mord mathrm">Σ</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.664392em;"><span style="top:-2.441336em;margin-left:0em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight"><span class="mord mathit mtight">i</span><span class="mrel mtight">=</span><span class="mord mathrm mtight">1</span></span></span></span><span style="top:-3.063em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mathit mtight">n</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.258664em;"></span></span></span></span></span><span class="mord"><span class="mord mathrm">Σ</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.824664em;"><span style="top:-2.441336em;margin-left:0em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight"><span class="mord mathit mtight" style="margin-right:0.05724em;">j</span><span class="mrel mtight">=</span><span class="mord mathrm mtight">1</span></span></span></span><span style="top:-3.063em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mathit mtight">i</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.394772em;"></span></span></span></span></span><span class="mord mathrm">.</span><span class="mord mathrm">.</span><span class="mord mathrm">.</span><span class="mrel">=</span><span class="mord"><span class="mord mathrm">Σ</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.664392em;"><span style="top:-2.441336em;margin-left:0em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight"><span class="mord mathit mtight" style="margin-right:0.05724em;">j</span><span class="mrel mtight">=</span><span class="mord mathrm mtight">1</span></span></span></span><span style="top:-3.063em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mathit mtight">n</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.394772em;"></span></span></span></span></span><span class="mord"><span class="mord mathrm">Σ</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.664392em;"><span style="top:-2.441336em;margin-left:0em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight"><span class="mord mathit mtight">i</span><span class="mrel mtight">=</span><span class="mord mathit mtight" style="margin-right:0.05724em;">j</span></span></span></span><span style="top:-3.063em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mathit mtight">n</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.394772em;"></span></span></span></span></span><span class="mord mathrm">.</span><span class="mord mathrm">.</span><span class="mord mathrm">.</span></span></span></span></p>

#### [ Kevin Buzzard (Mar 28 2018 at 21:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124333885):
<p>because unfortunately for mathematicians this is "proof by obvious"</p>

#### [ Kevin Buzzard (Mar 28 2018 at 21:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124333887):
<p>and I'm well aware that in this world it's not</p>

#### [ Kenny Lau (Mar 28 2018 at 21:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124333888):
<p>there is real induction :P</p>

#### [ Kenny Lau (Mar 28 2018 at 21:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124333889):
<p>it is used to prove that [0,1] is compact and connected</p>

#### [ Kenny Lau (Mar 28 2018 at 21:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124333893):
<p>(both proofs use real induction)</p>

#### [ Kenny Lau (Mar 28 2018 at 21:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124333908):
<p>it can also be used to reason about differential equations</p>

#### [ Kevin Buzzard (Mar 28 2018 at 21:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124333912):
<p>Even <span class="katex"><span class="katex-mathml"><math><semantics><mrow><msubsup><mi mathvariant="normal">Σ</mi><mrow><mi>i</mi><mo>=</mo><mn>1</mn></mrow><mi>a</mi></msubsup><msubsup><mi mathvariant="normal">Σ</mi><mrow><mi>j</mi><mo>=</mo><mn>1</mn></mrow><mi>b</mi></msubsup><mi mathvariant="normal">.</mi><mi mathvariant="normal">.</mi><mi mathvariant="normal">.</mi><mo>=</mo><msubsup><mi mathvariant="normal">Σ</mi><mrow><mi>j</mi><mo>=</mo><mn>1</mn></mrow><mi>b</mi></msubsup><msubsup><mi mathvariant="normal">Σ</mi><mrow><mi>i</mi><mo>=</mo><mn>1</mn></mrow><mi>a</mi></msubsup><mi mathvariant="normal">.</mi><mi mathvariant="normal">.</mi><mi mathvariant="normal">.</mi></mrow><annotation encoding="application/x-tex">\Sigma_{i=1}^a\Sigma_{j=1}^b...=\Sigma_{j=1}^b\Sigma_{i=1}^a...</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.849108em;"></span><span class="strut bottom" style="height:1.2438799999999999em;vertical-align:-0.394772em;"></span><span class="base"><span class="mord"><span class="mord mathrm">Σ</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.664392em;"><span style="top:-2.441336em;margin-left:0em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight"><span class="mord mathit mtight">i</span><span class="mrel mtight">=</span><span class="mord mathrm mtight">1</span></span></span></span><span style="top:-3.063em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mathit mtight">a</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.258664em;"></span></span></span></span></span><span class="mord"><span class="mord mathrm">Σ</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.849108em;"><span style="top:-2.441336em;margin-left:0em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight"><span class="mord mathit mtight" style="margin-right:0.05724em;">j</span><span class="mrel mtight">=</span><span class="mord mathrm mtight">1</span></span></span></span><span style="top:-3.063em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mathit mtight">b</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.394772em;"></span></span></span></span></span><span class="mord mathrm">.</span><span class="mord mathrm">.</span><span class="mord mathrm">.</span><span class="mrel">=</span><span class="mord"><span class="mord mathrm">Σ</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.849108em;"><span style="top:-2.441336em;margin-left:0em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight"><span class="mord mathit mtight" style="margin-right:0.05724em;">j</span><span class="mrel mtight">=</span><span class="mord mathrm mtight">1</span></span></span></span><span style="top:-3.063em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mathit mtight">b</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.394772em;"></span></span></span></span></span><span class="mord"><span class="mord mathrm">Σ</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.664392em;"><span style="top:-2.441336em;margin-left:0em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight"><span class="mord mathit mtight">i</span><span class="mrel mtight">=</span><span class="mord mathrm mtight">1</span></span></span></span><span style="top:-3.063em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mathit mtight">a</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.258664em;"></span></span></span></span></span><span class="mord mathrm">.</span><span class="mord mathrm">.</span><span class="mord mathrm">.</span></span></span></span></p>

#### [ Kevin Buzzard (Mar 28 2018 at 21:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124333916):
<p>I'm not sure I'd call the <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mo>[</mo><mn>0</mn><mo separator="true">,</mo><mn>1</mn><mo>]</mo></mrow><annotation encoding="application/x-tex">[0,1]</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.75em;"></span><span class="strut bottom" style="height:1em;vertical-align:-0.25em;"></span><span class="base"><span class="mopen">[</span><span class="mord mathrm">0</span><span class="mpunct">,</span><span class="mord mathrm">1</span><span class="mclose">]</span></span></span></span> thing induction</p>

#### [ Kevin Buzzard (Mar 28 2018 at 21:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124333917):
<p>it's just the completeness axiom</p>

#### [ Kenny Lau (Mar 28 2018 at 21:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124333921):
<p>which one?</p>

#### [ Kenny Lau (Mar 28 2018 at 21:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124333962):
<p>oh and real induction is basically "every non-empty clopen subset of R is R itself"</p>

#### [ Kevin Buzzard (Mar 28 2018 at 21:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124333967):
<p>That's precisely the statement of connectedness.</p>

#### [ Kenny Lau (Mar 28 2018 at 21:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124333970):
<p>they're so intertwined that you can't distinguish them</p>

#### [ Kevin Buzzard (Mar 28 2018 at 21:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124333977):
<p>You might want to think of various things as induction but if you want to communicate with mathematicians you'd better know what they call these facts (and have called them for 100 years)</p>

#### [ Kenny Lau (Mar 28 2018 at 21:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124333982):
<p><a href="https://math.stackexchange.com/a/4204/328173" target="_blank" title="https://math.stackexchange.com/a/4204/328173">https://math.stackexchange.com/a/4204/328173</a></p>

#### [ Chris Hughes (Mar 28 2018 at 21:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124334035):
<blockquote>
<p>I think I might spend some time over the summer making stuff into interfaces somehow. I am still concerned about manipulating finite sums. I want <span class="katex"><span class="katex-mathml"><math><semantics><mrow><msubsup><mi mathvariant="normal">Σ</mi><mrow><mi>i</mi><mo>=</mo><mn>1</mn></mrow><mi>n</mi></msubsup><msub><mi>a</mi><mi>i</mi></msub><mo>=</mo><msubsup><mi mathvariant="normal">Σ</mi><mrow><mi>i</mi><mo>=</mo><mn>1</mn></mrow><mi>n</mi></msubsup><msub><mi>a</mi><mrow><mi>n</mi><mo>+</mo><mn>1</mn><mo>−</mo><mi>i</mi></mrow></msub></mrow><annotation encoding="application/x-tex">\Sigma_{i=1}^na_i = \Sigma_{i=1}^na_{n+1-i}</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.68333em;"></span><span class="strut bottom" style="height:0.941994em;vertical-align:-0.258664em;"></span><span class="base"><span class="mord"><span class="mord mathrm">Σ</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.664392em;"><span style="top:-2.441336em;margin-left:0em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight"><span class="mord mathit mtight">i</span><span class="mrel mtight">=</span><span class="mord mathrm mtight">1</span></span></span></span><span style="top:-3.063em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mathit mtight">n</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.258664em;"></span></span></span></span></span><span class="mord"><span class="mord mathit">a</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.31166399999999994em;"><span style="top:-2.5500000000000003em;margin-left:0em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mathit mtight">i</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.15em;"></span></span></span></span></span><span class="mrel">=</span><span class="mord"><span class="mord mathrm">Σ</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.664392em;"><span style="top:-2.441336em;margin-left:0em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight"><span class="mord mathit mtight">i</span><span class="mrel mtight">=</span><span class="mord mathrm mtight">1</span></span></span></span><span style="top:-3.063em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mathit mtight">n</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.258664em;"></span></span></span></span></span><span class="mord"><span class="mord mathit">a</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.311664em;"><span style="top:-2.5500000000000003em;margin-left:0em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight"><span class="mord mathit mtight">n</span><span class="mbin mtight">+</span><span class="mord mathrm mtight">1</span><span class="mbin mtight">−</span><span class="mord mathit mtight">i</span></span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.208331em;"></span></span></span></span></span></span></span></span> to be trivial</p>
</blockquote>
<p>It is trivial, because I proved it. Most of these "obvious things that aren't obvious in lean" problems are solved by proving a few lemmas.</p>

#### [ Kenny Lau (Mar 28 2018 at 21:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124334050):
<p>master of finite sums</p>

#### [ Kevin Buzzard (Mar 28 2018 at 21:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124334051):
<p>Chris -- we need an "obvious_sum_thing" tactic :-)</p>

#### [ Kevin Buzzard (Mar 28 2018 at 21:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124334102):
<p>it's probably defined as "apply thing_chris_proved &lt;|&gt; apply _other_thing_chris_proved &lt;|&gt; apply some_other_thing_chris_proved"</p>

#### [ Kevin Buzzard (Mar 28 2018 at 21:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124334122):
<p>My goal is to make Lean so that mathematicians can use it the way they do mathematics.</p>

#### [ Kevin Buzzard (Mar 28 2018 at 21:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124334126):
<p>I think this will be hard, but that's what I'm striving for.</p>

#### [ Kevin Buzzard (Mar 28 2018 at 21:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124334178):
<p>So when they are faced with some dumb sum re-arrangement they just look at the page on sums in some reference document and they see exactly the thing they want, spelt out.</p>

#### [ Kevin Buzzard (Mar 28 2018 at 21:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124334180):
<p>and if even that's too much, then we write a tactic</p>

#### [ Kevin Buzzard (Mar 28 2018 at 21:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124334190):
<p>Do you remember that Kenny you and I were talking about things being "maths hard" or "Lean hard" (i.e. "obvious" but a pain to formalise)</p>

#### [ Kenny Lau (Mar 28 2018 at 21:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124334193):
<p>I don't</p>

#### [ Kevin Buzzard (Mar 28 2018 at 21:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124334194):
<p>those are the bits I want to formalise, those last bits, and I hide them all in xena directory</p>

#### [ Kenny Lau (Mar 28 2018 at 21:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124334198):
<p>you want to formalize the property of being difficult to be formalized?</p>

#### [ Kevin Buzzard (Mar 28 2018 at 21:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124334206):
<p>I want to formalise all the instances that my students discover</p>

#### [ Kevin Buzzard (Mar 28 2018 at 21:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124334259):
<p>Maybe it was me and Chris and you. I think it was even you that coined the phrase "Lean hard" (which I interpreted informally as meaning "trivial for a mathematician but rfl doesn't work")</p>

#### [ Kevin Buzzard (Mar 28 2018 at 21:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124334268):
<p>Maybe it was Chris.</p>

#### [ Kenny Lau (Mar 28 2018 at 21:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124334269):
<p>how is "Kenny you and I" different from "me and Chris and you"</p>

#### [ Kevin Buzzard (Mar 28 2018 at 21:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124334312):
<p>Oh I just misread what I wrote so restated something I'd already stated</p>

#### [ Kenny Lau (Mar 28 2018 at 21:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124334320):
<p>lol</p>

#### [ Kenny Lau (Mar 28 2018 at 21:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124334322):
<p>simp [and_comm, and_assoc, and_left_comm]</p>

#### [ Kenny Lau (Mar 28 2018 at 21:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124334324):
<p>rfl</p>

#### [ Andrew Ashworth (Mar 28 2018 at 21:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124334401):
<blockquote>
<p>So when they are faced with some dumb sum re-arrangement they just look at the page on sums in some reference document and they see exactly the thing they want, spelt out.</p>
</blockquote>
<p>that would be an interesting project. formalizing a handbook on sequences, sums, integrals, and derivatives</p>

#### [ Andrew Ashworth (Mar 28 2018 at 21:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124334405):
<p>i have one such handbook sitting on my shelf, it's quite thick</p>

#### [ Kevin Buzzard (Mar 28 2018 at 21:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124334524):
<p>fortunately integrals and derivatives are not my problem</p>

#### [ Kevin Buzzard (Mar 28 2018 at 21:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124334530):
<p>at least not at the minute</p>

#### [ Kevin Buzzard (Mar 28 2018 at 21:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124334539):
<p>and I'm not worried about the mathematical content</p>

#### [ Kevin Buzzard (Mar 28 2018 at 21:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124334543):
<p>it's the trivial stuff that I want to make trivial</p>

#### [ Andrew Ashworth (Mar 28 2018 at 21:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124334651):
<p>i'm so uncomfortable with this word trivial</p>

#### [ Andrew Ashworth (Mar 28 2018 at 21:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124334704):
<p>i don't think under the hood these things are actually trivial</p>

#### [ Mario Carneiro (Mar 28 2018 at 21:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124334708):
<p>I think mathematicians are really good at fooling themselves here</p>

#### [ Mario Carneiro (Mar 28 2018 at 21:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124334729):
<p>But I think Chris was right. "Trivial" is a synonym for "proved"</p>

#### [ Andrew Ashworth (Mar 28 2018 at 21:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124334731):
<p>for example, you could ask any high schooler if real numbers are trivial... if they can rattle off the value of pi and know how to use e with logarithms... but they're in a shock if they ever figure out how they're built</p>

#### [ Andrew Ashworth (Mar 28 2018 at 21:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124334796):
<p>in a similar manner any programmer can use javascript and python to staple together a vast array of libraries to do anything under the sun</p>

#### [ Kenny Lau (Mar 28 2018 at 21:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124334810):
<p>to Kevin "trivial" means "things that are repeated 100 times and so have become part of the intuition"</p>

#### [ Andrew Ashworth (Mar 28 2018 at 21:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124334811):
<p>but using is not understanding</p>

#### [ Andrew Ashworth (Mar 28 2018 at 21:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124334895):
<p>i think a general tactic would be difficult to write</p>

#### [ Andrew Ashworth (Mar 28 2018 at 21:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124334900):
<p>but a library of common results is very feasible</p>

#### [ Andrew Ashworth (Mar 28 2018 at 21:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124334904):
<p>like the lemmas Chris has proved</p>

#### [ Kevin Buzzard (Mar 28 2018 at 21:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124334973):
<p>I've seen PhD students prove hard theorems and then claim that all their results are trivial.</p>

#### [ Kevin Buzzard (Mar 28 2018 at 21:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124334978):
<p>I've had to explain to them that everything is trivial once you fully understand the proof.</p>

#### [ Mario Carneiro (Mar 28 2018 at 21:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124335000):
<p>Right, that's exactly the point. A trivial fact need not be trivial to lean, until lean understands it, i.e. it is formally proven</p>

#### [ Mario Carneiro (Mar 28 2018 at 21:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124335152):
<p>Perhaps part of the issue is conflating meanings of "trivial". If "trivial" means "I understand it and there are no surprising things in it", then the PhD may well find their results to be trivial. But this is by no means the same as "an outsider would immediately see how to construct the proof"</p>

#### [ Simon Hudon (Mar 28 2018 at 21:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124335290):
<p>I agree. I find the word more obfuscating than enlightening. I usually take it to mean "I can't be bothered to elaborate"</p>

#### [ Simon Hudon (Mar 28 2018 at 21:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124335318):
<p>Already, if you say "by basic calculus" you're not giving a lot of details but the reader knows where to go if they don't want to take your word for it</p>

#### [ Kevin Buzzard (Mar 28 2018 at 21:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124335471):
<p>Another issue is that trained mathematicians become extremely proficient at their art. I would expect anyone at my university to see that once you've been told what the sum of the first n squares is, you can see that there will be a trivial proof by induction. However</p>

#### [ Kevin Buzzard (Mar 28 2018 at 21:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124335524):
<p>what happens later on is that you make assertions about more complex objects (or even classes of complex objects, like schemes) and you say "fact X is true, and the proof is just that you generalise the standard proof of theorem T to this situation"</p>

#### [ Kevin Buzzard (Mar 28 2018 at 21:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124335533):
<p>and in general mathematicians (in my experience at least) are _extremely_ good at processing this idea and coming up with an opinion on whether this proof strategy will work.</p>

#### [ Kevin Buzzard (Mar 28 2018 at 21:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124335552):
<p>The problem is that sometimes you see people getting this wrong: you can have conversations of the form "X will be true, you can prove it by using technique Y...and then probably you can finish the job by induction"</p>

#### [ Kevin Buzzard (Mar 28 2018 at 21:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124335554):
<p>and two people agree, but one other person goes very quiet</p>

#### [ Kevin Buzzard (Mar 28 2018 at 21:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124335560):
<p>and then 30 seconds later they say "what if pathology Z occurs?"</p>

#### [ Kevin Buzzard (Mar 28 2018 at 21:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124335607):
<p>and then all of a sudden the conversation gets very animated and perhaps 1 minute later they have either proved that Z can't occur and everyone is now convinced that the theorem is proved</p>

#### [ Kevin Buzzard (Mar 28 2018 at 21:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124335617):
<p>or someone has concocted an example of a scheme with pathology Z and all of a sudden X is an open question again, or perhaps even we have a counterexample.</p>

#### [ Kevin Buzzard (Mar 28 2018 at 21:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124335623):
<p>This is normal communication amongst mathematicians.</p>

#### [ Kevin Buzzard (Mar 28 2018 at 21:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124335655):
<p>In some sense what I am worried about in my area of mathematics is that this has now gone too far, and there are so many subtleties that one has to be aware of, and so few people that are on top of most or all of them, that the process actually produces inaccurate results.</p>

#### [ Kevin Buzzard (Mar 28 2018 at 21:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124335703):
<p>And what is frustrating is that in many cases, X is true, because there's a far more elaborate argument which deals with the pathology that everyone overlooked</p>

#### [ Chris Hughes (Mar 28 2018 at 21:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124335704):
<p>I think Kevin is right that there are some things that are "obvious", hard to prove, but don't come up often enough for them to be in the library. Here's an example</p>
<div class="codehilite"><pre><span></span><span class="kn">example</span> <span class="o">(</span><span class="n">n</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">)</span> <span class="o">(</span><span class="n">f</span> <span class="o">:</span> <span class="bp">ℕ</span> <span class="bp">→</span> <span class="bp">ℕ</span><span class="o">)</span> <span class="o">(</span><span class="n">g</span> <span class="o">:</span> <span class="n">fin</span> <span class="n">n</span> <span class="bp">→</span> <span class="bp">ℕ</span><span class="o">)</span> <span class="o">(</span><span class="n">h</span> <span class="o">:</span> <span class="bp">∀</span> <span class="n">i</span> <span class="o">:</span> <span class="n">fin</span> <span class="n">n</span><span class="o">,</span> <span class="n">f</span> <span class="n">i</span><span class="bp">.</span><span class="mi">1</span>  <span class="bp">=</span> <span class="n">g</span> <span class="n">i</span><span class="o">)</span> <span class="o">:</span> <span class="o">(</span><span class="n">range</span> <span class="n">n</span><span class="o">)</span><span class="bp">.</span><span class="n">sum</span> <span class="n">f</span> <span class="bp">=</span> <span class="n">univ</span><span class="bp">.</span><span class="n">sum</span> <span class="n">g</span>
</pre></div>

#### [ Kevin Buzzard (Mar 28 2018 at 21:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124335705):
<p>so you can't just say "your theorem is wrong, here is a counterexample"</p>

#### [ Kevin Buzzard (Mar 28 2018 at 21:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124335711):
<p>you have to just say "I don't understand this bit of the argument"</p>

#### [ Kevin Buzzard (Mar 28 2018 at 21:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124335720):
<p>to which the response is sometimes "oh yeah this needs clarification"</p>

#### [ Kevin Buzzard (Mar 28 2018 at 21:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124335722):
<p>and sometimes "you should just work harder then"</p>

#### [ Kevin Buzzard (Mar 28 2018 at 22:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124335787):
<p>Right -- to a mathematician Chris' statement is trivial.</p>

#### [ Kevin Buzzard (Mar 28 2018 at 22:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124335791):
<p>Now is that because the human brain is not a computer?</p>

#### [ Kevin Buzzard (Mar 28 2018 at 22:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124335793):
<p>Or is it because Lean is bad?</p>

#### [ Kevin Buzzard (Mar 28 2018 at 22:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124335795):
<p>Or is it because I am not thinking about the question in the right way?</p>

#### [ Kevin Buzzard (Mar 28 2018 at 22:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124335882):
<p>This seems to me to be a great example of "too many notions of finiteness". It's quite hard to actually even write down something a mathematician would understand which is not of the form "prove X = X" here. The issue is that range n is not fin n</p>

#### [ Kevin Buzzard (Mar 28 2018 at 22:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124335889):
<p>And I'm sure Mario could come up with a one-liner</p>

#### [ Kevin Buzzard (Mar 28 2018 at 22:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124335892):
<p>but I am not at all sure that my first year students could.</p>

#### [ Kevin Buzzard (Mar 28 2018 at 22:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124335983):
<p>The idea is that because this is a question only about f's values on range(n), f is somehow "mathematically equivalent" to g</p>

#### [ Kevin Buzzard (Mar 28 2018 at 22:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124336040):
<p><code> example (n : ℕ) (f : ℕ → ℕ) (g : fin n → ℕ) (h : ∀ i : fin n, f i.1  = g i) : (range n).sum (\lam x, (x + f x)^2) = univ.sum (\lam i, (g i + i.1)*(g i + i.1)</code></p>

#### [ Kevin Buzzard (Mar 28 2018 at 22:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124336048):
<p>You could imagine something like that happening in practice, and again the mathematician wants to invoke the "it's obvious" axiom.</p>

#### [ Kevin Buzzard (Mar 28 2018 at 22:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124336050):
<p>tactic.</p>

#### [ Mario Carneiro (Mar 28 2018 at 22:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124336052):
<p>Looking at Chris's problem, my first instinct is to see if it follows from appropriate compositions of theorems</p>

#### [ Kevin Buzzard (Mar 28 2018 at 22:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124336057):
<p>I'm sure you can prove it in one line.</p>

#### [ Kevin Buzzard (Mar 28 2018 at 22:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124336059):
<p>But the question is how to make so that any mathematician can prove it in one line.</p>

#### [ Mario Carneiro (Mar 28 2018 at 22:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124336100):
<p>Once you have the right theorems you can just chain them</p>

#### [ Chris Hughes (Mar 28 2018 at 22:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124336101):
<p>I'm struggling to prove it at all.</p>

#### [ Mario Carneiro (Mar 28 2018 at 22:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124336103):
<p>that's what a good library does for you</p>

#### [ Kevin Buzzard (Mar 28 2018 at 22:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124336105):
<p>Right.</p>

#### [ Kevin Buzzard (Mar 28 2018 at 22:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124336107):
<p>and then a good reference manual guides you through.</p>

#### [ Chris Hughes (Mar 28 2018 at 22:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124336112):
<p><code>sum_attach</code> almost does it</p>

#### [ Mario Carneiro (Mar 28 2018 at 22:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124336124):
<p>First of all, <code>g</code> is unnecessary</p>

#### [ Kevin Buzzard (Mar 28 2018 at 22:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124336129):
<p>yes</p>

#### [ Mario Carneiro (Mar 28 2018 at 22:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124336131):
<p>although it's probably nice for use in a lemma</p>

#### [ Mario Carneiro (Mar 28 2018 at 22:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124336191):
<p>Now how do we know <code>fin n</code> is finite, so that <code>univ</code> exists? It is surely a map of <code>finset.range n</code></p>

#### [ Mario Carneiro (Mar 28 2018 at 22:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124336223):
<p>Sure enough, it is defined from <code>list.pmap fin.mk (list.range n) (λ a, list.mem_range.1) </code></p>

#### [ Mario Carneiro (Mar 28 2018 at 22:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124336270):
<p>so you want a lemma about mapping over <code>list.pmap</code> or its finset equivalent</p>

#### [ Kevin Buzzard (Mar 28 2018 at 22:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124336505):
<p>An alternative approach is just to prove it by induction. Then you'd need four theorems</p>

#### [ Kevin Buzzard (Mar 28 2018 at 22:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124336515):
<p>Empty sums, and sums to n+1 being sum to n then one more</p>

#### [ Kevin Buzzard (Mar 28 2018 at 22:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124336663):
<p>This, by the way, is an even simpler example of the thing I was trying (but not really succeeding) to ask about a couple of weeks ago. If a mathematician wants to sum the first n squares in Lean, then I am very unclear about whether they should use the f approach or the g approach. In maths they are one and the same thing. The question I was trying to ask a couple of weeks ago is whether in situations like this there is "a correct Lean answer".</p>

#### [ Chris Hughes (Mar 28 2018 at 22:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124336669):
<p>Induction is quite difficult. I got stuck here.</p>
<div class="codehilite"><pre><span></span><span class="n">g</span> <span class="o">:</span> <span class="n">fin</span> <span class="o">(</span><span class="n">succ</span> <span class="n">n</span><span class="o">)</span> <span class="bp">→</span> <span class="bp">ℕ</span>
<span class="err">⊢</span> <span class="n">sum</span> <span class="n">univ</span> <span class="o">(</span><span class="bp">λ</span> <span class="o">(</span><span class="n">i</span> <span class="o">:</span> <span class="n">fin</span> <span class="n">n</span><span class="o">),</span> <span class="n">g</span> <span class="bp">⟨</span><span class="n">i</span><span class="bp">.</span><span class="n">val</span><span class="o">,</span> <span class="bp">_⟩</span><span class="o">)</span> <span class="bp">=</span> <span class="n">sum</span> <span class="o">(</span><span class="n">erase</span> <span class="n">univ</span> <span class="bp">⟨</span><span class="n">n</span><span class="o">,</span> <span class="bp">_⟩</span><span class="o">)</span> <span class="n">g</span>
</pre></div>

#### [ Kevin Buzzard (Mar 28 2018 at 22:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124336680):
<p>But it can just be a theorem in a library once Mario has written the one-liner</p>

#### [ Kevin Buzzard (Mar 28 2018 at 22:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124336732):
<p>You need some sum erase lemma Chris</p>

#### [ Chris Hughes (Mar 28 2018 at 22:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124336743):
<p>It's not as simple as that. My two finsets have different types.</p>

#### [ Kevin Buzzard (Mar 28 2018 at 22:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124336744):
<p>Yes</p>

#### [ Kevin Buzzard (Mar 28 2018 at 22:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124336748):
<p>It's always about the type changing</p>

#### [ Kevin Buzzard (Mar 28 2018 at 22:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124336787):
<p>Presumably it's much easier to do the range induction</p>

#### [ Kevin Buzzard (Mar 28 2018 at 22:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124336795):
<p>The issue is that mathematicians have a really powerful notion of equality</p>

#### [ Chris Hughes (Mar 28 2018 at 22:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124336807):
<p>I think you need to prove it for m \le n, for a finset of type fin n containing elements less than m.</p>

#### [ Kevin Buzzard (Mar 28 2018 at 22:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124336809):
<p>Where fin succ n "equals" fin n and then n</p>

#### [ Kevin Buzzard (Mar 28 2018 at 22:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124337090):
<p>The finset of type fin n defined as the elements whose value is less than m, is canonically isomorphic (and hence, in a mathematician's mind, equal) to fin m. Just like computer scientists can formulate the recursor for an inductive type, mathematicians have some sort of construction which enables them to pass effortlessly between canonically isomorphic objects. For me, range n and fin n are canonically isomorphic, and your result is an immediate application of some sort of theorem formalising the assertion that doing the same thing to two canonically isomorphic situations results in the same answer.</p>

#### [ Kevin Buzzard (Mar 28 2018 at 22:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124337115):
<p>It's a fact that fin n and range n are canonically isomorphic via the map sending i to i.1</p>

#### [ Kevin Buzzard (Mar 28 2018 at 22:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124337158):
<p>Chris' assumption <code> (h : ∀ i : fin n, f i.1  = g i) </code> is the statement that this canonical isomorphism extends to a canonical isomorphism between the pair (f restricted to range n,range n) and (g,fin n)</p>

#### [ Kevin Buzzard (Mar 28 2018 at 22:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124337173):
<p>and now a general "thing" analogous to a recursor says that any construction which spits out an object which is unique up to unique isomorphism (such as a natural number) will spit out the same object if it is applied to two canonically isomorphic situations.</p>

#### [ Kevin Buzzard (Mar 28 2018 at 22:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124337174):
<p>That is the way a mathematician thinks about this question.</p>

#### [ Kevin Buzzard (Mar 28 2018 at 22:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124337225):
<p>More generally g i could have been some group</p>

#### [ Kevin Buzzard (Mar 28 2018 at 22:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124337229):
<p>and f (i.1) could have been a canonically isomorphic group</p>

#### [ Kevin Buzzard (Mar 28 2018 at 22:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124337231):
<p>and then the product of the f(i.1) would only have been canonically isomorphic to the product of the g(i)</p>

#### [ Kevin Buzzard (Mar 28 2018 at 22:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124337296):
<p>Where are these notions in dependent type theory?</p>

#### [ Kevin Buzzard (Mar 28 2018 at 22:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124337530):
<p>I want a general theorem which takes an inputs (1) a bijection <code>fin n = range n</code> (mathematicians would even write this map as = ) and (2) a construction on the fin n side (such as the function sending <code>g : fin n -&gt; nat</code> to <code>univ.sum g</code>) and spits out (a) a function f from range n to nat (b) a proof of <code> ∀ i : fin n, f i.1  = g i </code> and (c) a proof of <code> (range n).sum f = univ.sum g </code>. All of this is internalised somehow in mathematics as being sufficiently obvious as to not need a proof. Unfortunately what I write somehow doesn't make sense because range n is not a type.</p>

#### [ Kevin Buzzard (Mar 28 2018 at 22:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124337580):
<p>I can't even formalise what I want.</p>

#### [ Chris Hughes (Mar 28 2018 at 22:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124337596):
<p>Finally proved it. Not pretty</p>
<div class="codehilite"><pre><span></span><span class="kn">example</span> <span class="o">(</span><span class="n">n</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">)</span> <span class="o">(</span><span class="n">f</span> <span class="o">:</span> <span class="bp">ℕ</span> <span class="bp">→</span> <span class="bp">ℕ</span><span class="o">)</span> <span class="o">(</span><span class="n">g</span> <span class="o">:</span> <span class="n">fin</span> <span class="n">n</span> <span class="bp">→</span> <span class="bp">ℕ</span><span class="o">)</span> <span class="o">(</span><span class="n">h</span> <span class="o">:</span> <span class="bp">∀</span> <span class="n">i</span> <span class="o">:</span> <span class="n">fin</span> <span class="n">n</span><span class="o">,</span> <span class="n">f</span> <span class="n">i</span><span class="bp">.</span><span class="mi">1</span>  <span class="bp">=</span> <span class="n">g</span> <span class="n">i</span><span class="o">)</span> <span class="o">:</span>
<span class="o">(</span><span class="n">range</span> <span class="n">n</span><span class="o">)</span><span class="bp">.</span><span class="n">sum</span> <span class="n">f</span> <span class="bp">=</span> <span class="n">univ</span><span class="bp">.</span><span class="n">sum</span> <span class="n">g</span> <span class="o">:=</span>
<span class="k">show</span> <span class="o">((</span><span class="n">range</span> <span class="n">n</span><span class="o">)</span><span class="bp">.</span><span class="mi">1</span><span class="bp">.</span><span class="n">map</span> <span class="n">f</span><span class="o">)</span><span class="bp">.</span><span class="n">sum</span> <span class="bp">=</span> <span class="o">(</span><span class="n">univ</span><span class="bp">.</span><span class="mi">1</span><span class="bp">.</span><span class="n">map</span> <span class="n">g</span><span class="o">)</span><span class="bp">.</span><span class="n">sum</span><span class="o">,</span>
<span class="k">from</span>
<span class="k">have</span> <span class="n">h₂</span> <span class="o">:</span> <span class="o">(</span><span class="n">univ</span> <span class="o">:</span> <span class="n">finset</span> <span class="o">(</span><span class="n">fin</span> <span class="n">n</span><span class="o">))</span><span class="bp">.</span><span class="mi">1</span>  <span class="bp">=</span> <span class="o">(</span><span class="n">range</span> <span class="n">n</span><span class="o">)</span><span class="bp">.</span><span class="mi">1</span><span class="bp">.</span><span class="n">pmap</span> <span class="o">(</span><span class="bp">λ</span> <span class="n">m</span> <span class="n">hm</span><span class="o">,</span> <span class="n">fin</span><span class="bp">.</span><span class="n">mk</span> <span class="n">m</span> <span class="n">hm</span><span class="o">)</span> <span class="o">(</span><span class="bp">λ</span> <span class="n">m</span><span class="o">,</span> <span class="o">(</span><span class="bp">@</span><span class="n">mem_range</span> <span class="bp">_</span> <span class="bp">_</span><span class="o">)</span><span class="bp">.</span><span class="mi">1</span><span class="o">)</span> <span class="o">:=</span>
  <span class="k">show</span> <span class="o">(</span><span class="err">↑</span><span class="o">(</span><span class="n">list</span><span class="bp">.</span><span class="n">pmap</span> <span class="n">fin</span><span class="bp">.</span><span class="n">mk</span> <span class="o">(</span><span class="n">list</span><span class="bp">.</span><span class="n">range</span> <span class="n">n</span><span class="o">)</span> <span class="bp">_</span><span class="o">)</span> <span class="o">:</span> <span class="n">multiset</span> <span class="bp">_</span><span class="o">)</span> <span class="bp">=</span> <span class="n">multiset</span><span class="bp">.</span><span class="n">pmap</span> <span class="n">fin</span><span class="bp">.</span><span class="n">mk</span> <span class="o">((</span><span class="n">range</span> <span class="n">n</span><span class="o">)</span><span class="bp">.</span><span class="n">val</span><span class="o">)</span> <span class="bp">_</span><span class="o">,</span>
  <span class="k">by</span> <span class="n">rw</span> <span class="err">←</span> <span class="n">multiset</span><span class="bp">.</span><span class="n">coe_pmap</span><span class="bp">;</span> <span class="n">refl</span><span class="o">,</span>
<span class="k">have</span> <span class="n">h₁</span> <span class="o">:</span> <span class="o">(</span><span class="n">range</span> <span class="n">n</span><span class="o">)</span><span class="bp">.</span><span class="mi">1</span><span class="bp">.</span><span class="n">map</span> <span class="n">f</span> <span class="bp">=</span> <span class="n">univ</span><span class="bp">.</span><span class="mi">1</span><span class="bp">.</span><span class="n">map</span> <span class="n">g</span> <span class="o">:=</span>
<span class="k">begin</span>
  <span class="n">rw</span> <span class="o">[</span><span class="n">h₂</span><span class="o">,</span> <span class="n">multiset</span><span class="bp">.</span><span class="n">map_pmap</span><span class="o">],</span>
  <span class="n">simp</span> <span class="n">only</span> <span class="o">[(</span><span class="n">h</span> <span class="bp">_</span><span class="o">)</span><span class="bp">.</span><span class="n">symm</span><span class="o">],</span>
  <span class="n">rw</span> <span class="n">multiset</span><span class="bp">.</span><span class="n">pmap_eq_map</span><span class="o">,</span>
<span class="kn">end</span><span class="o">,</span>
<span class="k">by</span> <span class="n">rw</span> <span class="n">h₁</span>
</pre></div>

#### [ Kevin Buzzard (Mar 28 2018 at 22:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124337657):
<p>I thought you were supposed to be revising mechanics?</p>

#### [ Kevin Buzzard (Mar 28 2018 at 22:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124337748):
<p>Chris if I now asked you to prove something like: if <code>f : nat -&gt; {2,4,6}</code> and <code>g : fin n -&gt; {2,4,6}</code> and h is the same, then max of f over range(n) equalled max of g over fin n, would the proof be "the same"?</p>

#### [ Kevin Buzzard (Mar 28 2018 at 22:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124337754):
<p>Or would you have to change some application of some theorem in the library to an application of another theorem?</p>

#### [ Kevin Buzzard (Mar 28 2018 at 22:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124337810):
<p>or if f : nat -&gt; bool and g : fin n -&gt; bool, and I asked you to prove that f(0) and f(1) and ... and f(n-1) = g(0) and g(1) and ... and g(n-1), would the proof be "the same"?</p>

#### [ Kevin Buzzard (Mar 28 2018 at 22:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124337823):
<p>(assuming the functions existed which and'd together a list of bools)</p>

#### [ Chris Hughes (Mar 28 2018 at 22:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124337836):
<p>More or less, but with fold instead of sum. I actually got a fair amount of revision done today, so I thought I'd treat myself to lean.</p>

#### [ Kevin Buzzard (Mar 28 2018 at 22:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124337837):
<p>(oh crap there would be two such functions? One for fin n and one for range(n)?</p>

#### [ Mario Carneiro (Mar 28 2018 at 22:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124337892):
<p>It is not true that <code>fin n</code> and <code>range n</code> are canonically isomorphic, because they aren't even the same kind of thing</p>

#### [ Kevin Buzzard (Mar 28 2018 at 22:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124337902):
<p>I know</p>

#### [ Kevin Buzzard (Mar 28 2018 at 22:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124337903):
<p>but they are</p>

#### [ Kevin Buzzard (Mar 28 2018 at 22:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124337913):
<p>it's impossible to decide either way because there is no definition of canonical</p>

#### [ Mario Carneiro (Mar 28 2018 at 22:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124337921):
<p><code>range n</code> is to be thought of as the LIST <code>[0,1,2,...,n-1]</code>, <code>fin n</code> is the SET of numbers less than n</p>

#### [ Mario Carneiro (Mar 28 2018 at 22:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124337926):
<p>What can be said is that <code>range n</code> enumerates <code>fin n</code></p>

#### [ Kevin Buzzard (Mar 28 2018 at 22:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124337927):
<p>and I completely understand that in type theory it doesn't make sense to write down a map from one to the other</p>

#### [ Mario Carneiro (Mar 28 2018 at 22:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124337935):
<p>and that's what <code>pmap</code> is doing</p>

#### [ Kevin Buzzard (Mar 28 2018 at 22:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124337952):
<p><code> unknown identifier 'pmap' </code></p>

#### [ Mario Carneiro (Mar 28 2018 at 22:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124337994):
<p><code>{list,multiset}.pmap</code></p>

#### [ Kevin Buzzard (Mar 28 2018 at 22:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124338005):
<p>It's really annoying that imports have to be on line 1. Is that just something that can never change?</p>

#### [ Mario Carneiro (Mar 28 2018 at 22:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124338018):
<p>I don't think it would be a good idea to change</p>

#### [ Kevin Buzzard (Mar 28 2018 at 22:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124338023):
<p>I don't think it's true in python</p>

#### [ Kevin Buzzard (Mar 28 2018 at 22:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124338024):
<p>that well-known functional language</p>

#### [ Mario Carneiro (Mar 28 2018 at 22:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124338025):
<p>The collection of imports allows you to easily see file-level dependencies</p>

#### [ Mario Carneiro (Mar 28 2018 at 22:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124338031):
<p>It's standard practice in C/C++/java</p>

#### [ Kevin Buzzard (Mar 28 2018 at 23:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124338115):
<p><code>#check multiset.pmap</code> (rolls eyes) <code>#check  @multiset.pmap</code></p>

#### [ Kevin Buzzard (Mar 28 2018 at 23:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124338165):
<p>How was I supposed to know that <code>?M_3</code> was a map from <code>?M_1</code> to <code>Prop</code>?</p>

#### [ Kevin Buzzard (Mar 28 2018 at 23:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124338245):
<p>Mario you're right, there is somehow a difference between objects which are superficially in bijection to a naive eye and types which really do biject. So one of the problems here is that this underlying set with size n is being modelled both as a type and as data, and one has to find a route from one to the other.</p>

#### [ Kevin Buzzard (Mar 28 2018 at 23:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124338337):
<p>So my "general principle" needs to be broken down into several specific instances. This is somehow what I was trying to ask a couple of weeks ago. I was asking a too high-powered question. I was asking "let's say someone proves Lagrange's theorem for some notion of a finite group. However are we now going to port this to a proof of Lagrange's theorem for some other notion of a finite group?" I am not sure anyone ever understood what I was asking.</p>

#### [ Kevin Buzzard (Mar 28 2018 at 23:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124338402):
<p>But Chris' question is much better. "Say I have formalised the notion of sum of f(i) for 0&lt;=i&lt;n in some way in dependent type theory. How am I going to prove that my sum equals the sum as formalised in a different way?"</p>

#### [ Kevin Buzzard (Mar 28 2018 at 23:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124338421):
<p>Let me stress and stress and stress that in mathematics there is only one way to formalise this, and it's <span class="katex"><span class="katex-mathml"><math><semantics><mrow><msubsup><mi mathvariant="normal">Σ</mi><mrow><mi>i</mi><mo>=</mo><mn>0</mn></mrow><mrow><mi>n</mi><mo>−</mo><mn>1</mn></mrow></msubsup><mi>f</mi><mo>(</mo><mi>i</mi><mo>)</mo><mi mathvariant="normal">.</mi></mrow><annotation encoding="application/x-tex">\Sigma_{i=0}^{n-1}f(i).</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.854239em;"></span><span class="strut bottom" style="height:1.131103em;vertical-align:-0.276864em;"></span><span class="base"><span class="mord"><span class="mord mathrm">Σ</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.854239em;"><span style="top:-2.4231360000000004em;margin-left:0em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight"><span class="mord mathit mtight">i</span><span class="mrel mtight">=</span><span class="mord mathrm mtight">0</span></span></span></span><span style="top:-3.1031310000000003em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight"><span class="mord mathit mtight">n</span><span class="mbin mtight">−</span><span class="mord mathrm mtight">1</span></span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.276864em;"></span></span></span></span></span><span class="mord mathit" style="margin-right:0.10764em;">f</span><span class="mopen">(</span><span class="mord mathit">i</span><span class="mclose">)</span><span class="mord mathrm">.</span></span></span></span></p>

#### [ Kevin Buzzard (Mar 28 2018 at 23:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124338491):
<p>You guys even might need to prove that if f and g are two functions nat -&gt; nat and f(i) = g(i) for all i &lt; n, then the sums are equal.</p>

#### [ Kevin Buzzard (Mar 28 2018 at 23:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124338505):
<p>The proof of this is not rfl. And yet it is manifestly obvious in some way.</p>

#### [ Kevin Buzzard (Mar 28 2018 at 23:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124338509):
<p>What is going on here?</p>

#### [ Kevin Buzzard (Mar 28 2018 at 23:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124338519):
<p>I have to prove it by induction on n.</p>

#### [ Kevin Buzzard (Mar 28 2018 at 23:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124338534):
<p>In Lean. But it wouldn't make it to the blackboard ;-)</p>

#### [ Chris Hughes (Mar 28 2018 at 23:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124338580):
<blockquote>
<p>You guys even might need to prove that if f and g are two functions nat -&gt; nat and f(i) = g(i) for all i &lt; n, then the sums are equal.</p>
</blockquote>
<p><code>finset.sum_congr</code> already does that.</p>

#### [ Kevin Buzzard (Mar 28 2018 at 23:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124338590):
<p>aah but only for finsets :-)</p>

#### [ Kevin Buzzard (Mar 28 2018 at 23:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124338597):
<p>What about if I make the sum over fin n?</p>

#### [ Kevin Buzzard (Mar 28 2018 at 23:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124338601):
<p>f(i.1) etc</p>

#### [ Kevin Buzzard (Mar 28 2018 at 23:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124338604):
<p>now you have to provide me with another lemma.</p>

#### [ Kevin Buzzard (Mar 28 2018 at 23:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124338647):
<p>And what if I then wanted it over the multiset {1,2,...,n}?</p>

#### [ Kevin Buzzard (Mar 28 2018 at 23:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124338659):
<p>And then over the list [1,2,...,n]?</p>

#### [ Kevin Buzzard (Mar 28 2018 at 23:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124338672):
<p>These are all different lemmas, right?</p>

#### [ Kevin Buzzard (Mar 28 2018 at 23:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124338680):
<p>all saying the same thing which 95% of mathematicians do not even realise needs a proof.</p>

#### [ Kevin Buzzard (Mar 28 2018 at 23:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124338729):
<p>"If your system doesn't do that automatically what kind of a stupid system is that?"</p>

#### [ Kevin Buzzard (Mar 28 2018 at 23:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124338730):
<p>I can hear the taunts now.</p>

#### [ Chris Hughes (Mar 28 2018 at 23:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124338750):
<p>Computers are stupid. People have been dealing with that fact forever, but it's okay, because they still do a lot of things better than people. The key is to persuade people that lean can do some things better than people.</p>

#### [ Kevin Buzzard (Mar 28 2018 at 23:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124338792):
<p>All of this stuff has to be collected up and curated in a good way. Sounds like Mario and his group have proved most (but possibly not quite all) the lemmas, and now we just need someone to write down their names. I have been carrying round some printouts of lean files for a while now. Did you know <code>multiset.lean</code> is 91k long?!</p>

#### [ Kevin Buzzard (Mar 28 2018 at 23:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124338796):
<p>I want Lean to do some things better than people, but as little as possible much much worse than people</p>

#### [ Kevin Buzzard (Mar 28 2018 at 23:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124338800):
<p>and by people I mean mathematicians</p>

#### [ Kevin Buzzard (Mar 28 2018 at 23:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124338802):
<p>obviously</p>

#### [ Kevin Buzzard (Mar 28 2018 at 23:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124338805):
<p>;-)</p>

#### [ Kevin Buzzard (Mar 28 2018 at 23:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124338812):
<p>over 2000 lines of multiset.lean. I read it in the bath occasionally.</p>

#### [ Kevin Buzzard (Mar 28 2018 at 23:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124338839):
<p>My copy is covered in comments.</p>

#### [ Mario Carneiro (Mar 28 2018 at 23:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124338876):
<p>I believe in comprehensive libraries - and that is an achievable goal</p>

#### [ Chris Hughes (Mar 28 2018 at 23:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124338878):
<p>The names already are written down in mathlib. Writing them in a different format won't make any difference. Mostly they don't need to much of an explanation, and mostly they're part of a manageably short list of lemmas with the right word in the name.</p>

#### [ Kevin Buzzard (Mar 28 2018 at 23:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124338893):
<p>I absolutely agree with you that comprehensive libraries are really important and that you are extremely good at providing them.</p>

#### [ Mario Carneiro (Mar 28 2018 at 23:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124338900):
<p>Those examples you gave are not different lemmas for the most part</p>

#### [ Mario Carneiro (Mar 28 2018 at 23:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124338902):
<p>most of it comes from <code>funext</code></p>

#### [ Kevin Buzzard (Mar 28 2018 at 23:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124338904):
<p>What I need to do is to somehow distill from these comprehensive libraries the results which are "so obvious that a mathematician needs to be told how to prove them in Lean"</p>

#### [ Mario Carneiro (Mar 28 2018 at 23:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124338946):
<p>All of it?</p>

#### [ Kevin Buzzard (Mar 28 2018 at 23:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124338949):
<p>Maybe.</p>

#### [ Kevin Buzzard (Mar 28 2018 at 23:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124338952):
<p>Or lots of it, at least.</p>

#### [ Kevin Buzzard (Mar 28 2018 at 23:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124338955):
<p>But somehow I wonder whether we can ignore much of the lower level stuff</p>

#### [ Mario Carneiro (Mar 28 2018 at 23:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124338962):
<p>You shouldn't need to consult the construction of R for work based on it, for example</p>

#### [ Kevin Buzzard (Mar 28 2018 at 23:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124338964):
<p>but I think I really need to concentrate on documenting the stuff which shows up in practice when people are manipulating finite types.</p>

#### [ Kevin Buzzard (Mar 28 2018 at 23:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124338969):
<p>Aah yes, R is a good example. People need to know the name of the theorem which says non-empty and bounded implies LUB</p>

#### [ Kevin Buzzard (Mar 28 2018 at 23:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124338970):
<p>and add_assoc etc</p>

#### [ Kevin Buzzard (Mar 28 2018 at 23:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124338972):
<p>but they should hopefully never have to open real.lean</p>

#### [ Kevin Buzzard (Mar 28 2018 at 23:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124339012):
<p>By people I mean mathematicians</p>

#### [ Mario Carneiro (Mar 28 2018 at 23:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124339013):
<p>I have a long postponed development of sums over nat (similar to Chris's earlier attempt)</p>

#### [ Kevin Buzzard (Mar 28 2018 at 23:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124339020):
<p>Over July and August I think I will be bombarded with people asking me how to do mathematics that they thought was trivial, in Lean.</p>

#### [ Kevin Buzzard (Mar 28 2018 at 23:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124339022):
<p>I will answer as best I can.</p>

#### [ Kevin Buzzard (Mar 28 2018 at 23:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124339032):
<p>I like Zulip. I know I've said this before but starring stuff really is useful. You star it, you forget it, you find the time a week later by which time you've forgotten the name of the topic, and there it is right there in your list of starred messages. Really helps my workflow. I have to go and clean a kitchen.</p>

#### [ Kevin Buzzard (Mar 28 2018 at 23:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124339071):
<p>Thanks to everyone as ever. This has been really instructive.</p>

#### [ Kenny Lau (Mar 29 2018 at 01:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124343487):
<p><span class="user-mention" data-user-id="110038">@Kevin Buzzard</span> what is it with you asking everyone to revise mechanics :P</p>

#### [ Kevin Buzzard (Mar 29 2018 at 08:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124355080):
<p>It's just what I'd be doing if I was your age.</p>

#### [ Kenny Lau (Mar 29 2018 at 08:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124355092):
<p><span class="user-mention" data-user-id="110038">@Kevin Buzzard</span> I mean, of course we need to revise</p>

#### [ Kenny Lau (Mar 29 2018 at 08:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124355094):
<p>but what is it with the obsession with mechanics</p>

#### [ Kevin Buzzard (Mar 29 2018 at 08:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124355291):
<p>It's just what I'd be doing if I was your age.</p>

#### [ Kevin Buzzard (Mar 29 2018 at 08:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124355298):
<p>Because that one was the course where there seemed to be no axioms :-)</p>

#### [ Kenny Lau (Mar 29 2018 at 08:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124355300):
<p>fair enough</p>

#### [ Kevin Buzzard (Mar 29 2018 at 08:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124355301):
<p>"Apply conservation of energy" -&gt; "contradiction" -&gt; "teacher says <code>obviously energy is lost to heat in this question</code></p>

#### [ Kevin Buzzard (Mar 29 2018 at 08:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124355341):
<p>My conclusion was that conservation of energy was an axiom which should only be applied if desperate.</p>

#### [ Kenny Lau (Mar 29 2018 at 08:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124355348):
<p>I thought conservation of energy isn't an axiom</p>

#### [ Kevin Buzzard (Mar 29 2018 at 09:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124355412):
<p>I'd better revise mechanics</p>

#### [ Kenny Lau (Mar 29 2018 at 09:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124355413):
<p><a href="https://en.wikipedia.org/wiki/Noether%27s_theorem" target="_blank" title="https://en.wikipedia.org/wiki/Noether%27s_theorem">https://en.wikipedia.org/wiki/Noether%27s_theorem</a></p>

#### [ Andrew Ashworth (Mar 29 2018 at 09:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124355459):
<p>+1 for anything that gets closer to formalizing the calculus of variations</p>

#### [ Chris Hughes (Mar 30 2018 at 20:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124422668):
<p>Shortest proof I can manage of the stupid lemma. More or less wrote itself once I saw <code>sum_bij</code> existed.</p>
<div class="codehilite"><pre><span></span><span class="kn">example</span> <span class="o">(</span><span class="n">n</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">)</span> <span class="o">(</span><span class="n">f</span> <span class="o">:</span> <span class="bp">ℕ</span> <span class="bp">→</span> <span class="bp">ℕ</span><span class="o">)</span> <span class="o">(</span><span class="n">g</span> <span class="o">:</span> <span class="n">fin</span> <span class="n">n</span> <span class="bp">→</span> <span class="bp">ℕ</span><span class="o">)</span> <span class="o">(</span><span class="n">h</span> <span class="o">:</span> <span class="bp">∀</span> <span class="n">i</span> <span class="o">:</span> <span class="n">fin</span> <span class="n">n</span><span class="o">,</span> <span class="n">f</span> <span class="n">i</span><span class="bp">.</span><span class="mi">1</span>  <span class="bp">=</span> <span class="n">g</span> <span class="n">i</span><span class="o">)</span> <span class="o">:</span>
    <span class="o">(</span><span class="n">range</span> <span class="n">n</span><span class="o">)</span><span class="bp">.</span><span class="n">sum</span> <span class="n">f</span> <span class="bp">=</span> <span class="n">univ</span><span class="bp">.</span><span class="n">sum</span> <span class="n">g</span> <span class="o">:=</span>
<span class="n">sum_bij</span> <span class="o">(</span><span class="bp">λ</span> <span class="n">i</span> <span class="n">h</span><span class="o">,</span> <span class="bp">⟨</span><span class="n">i</span><span class="o">,</span> <span class="n">mem_range</span><span class="bp">.</span><span class="mi">1</span> <span class="n">h</span><span class="bp">⟩</span><span class="o">)</span> <span class="o">(</span><span class="bp">λ</span> <span class="bp">_</span> <span class="bp">_</span><span class="o">,</span> <span class="n">mem_univ</span> <span class="bp">_</span><span class="o">)</span> <span class="o">(</span><span class="bp">λ</span> <span class="n">a</span> <span class="n">ha</span><span class="o">,</span> <span class="n">h</span> <span class="bp">⟨</span><span class="n">a</span><span class="o">,</span> <span class="n">mem_range</span><span class="bp">.</span><span class="mi">1</span> <span class="n">ha</span><span class="bp">⟩</span><span class="o">)</span>
<span class="o">(</span><span class="bp">λ</span> <span class="bp">_</span> <span class="bp">_</span> <span class="bp">_</span> <span class="bp">_</span><span class="o">,</span> <span class="n">fin</span><span class="bp">.</span><span class="n">veq_of_eq</span><span class="o">)</span> <span class="o">(</span><span class="bp">λ</span> <span class="bp">⟨</span><span class="n">b</span><span class="o">,</span> <span class="n">hb</span><span class="bp">⟩</span> <span class="bp">_</span><span class="o">,</span> <span class="bp">⟨</span><span class="n">b</span><span class="o">,</span> <span class="n">mem_range</span><span class="bp">.</span><span class="mi">2</span> <span class="n">hb</span><span class="o">,</span> <span class="n">rfl</span><span class="bp">⟩</span><span class="o">)</span>
</pre></div>

#### [ Kenny Lau (Mar 30 2018 at 20:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124422695):
<p>oh wow you proved it</p>

#### [ Kenny Lau (Mar 30 2018 at 20:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124422696):
<p>congratulations</p>

#### [ Kenny Lau (Mar 30 2018 at 20:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124422845):
<p><span class="user-mention" data-user-id="110044">@Chris Hughes</span> which modules did you import and which namespaces did you open?</p>

#### [ Chris Hughes (Mar 30 2018 at 20:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124422940):
<p><code>algebra.big_operators</code> and <code>data.fintype</code> and namespace <code>finset</code></p>

#### [ Kenny Lau (Mar 30 2018 at 20:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124423056):
<p>thanks</p>

#### [ Kenny Lau (Mar 30 2018 at 20:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124424620):
<div class="codehilite"><pre><span></span>tactic failed, there are unsolved goals
state:
summand : ℕ → ℕ,
n : ℕ
⊢ finset.sum finset.univ (λ (x : fin (succ n)), summand (x.val)) =
    summand n + finset.sum finset.univ (λ (x : fin n), summand (x.val))
</pre></div>

#### [ Kenny Lau (Mar 30 2018 at 20:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124424622):
<p>any guidance?</p>

#### [ Mario Carneiro (Mar 30 2018 at 20:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124424655):
<p>You shouldn't prove that by induction, you should use chris's lemma</p>

#### [ Kenny Lau (Mar 30 2018 at 20:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124424675):
<p>no that isn't the same thing</p>

#### [ Kenny Lau (Mar 30 2018 at 20:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124424677):
<p>and I need to prove that thing</p>

#### [ Mario Carneiro (Mar 30 2018 at 20:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124424736):
<p>it relates the univ sum to a sum over nat, which has good inductive properties</p>

#### [ Chris Hughes (Mar 30 2018 at 20:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124424761):
<p><code>rw \l sum_insert n</code> on the <code>succ n</code> univ.</p>

#### [ Chris Hughes (Mar 30 2018 at 20:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124424771):
<p>Then <code>sum_bij</code></p>

#### [ Kenny Lau (Mar 30 2018 at 20:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124424777):
<p>I see</p>

#### [ Chris Hughes (Mar 30 2018 at 20:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124425042):
<p><code>rw [← insert_erase (mem_univ (⟨n, lt_succ_self n⟩: fin (succ n))), sum_insert (not_mem_erase _ _)], </code> is a good start.</p>

#### [ Mario Carneiro (Mar 30 2018 at 20:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124425141):
<div class="codehilite"><pre><span></span>import algebra.big_operators data.fintype
open finset nat

theorem chris (n : ℕ) (f : ℕ → ℕ) (g : fin n → ℕ) (h : ∀ i : fin n, f i.1  = g i) :
    (range n).sum f = univ.sum g :=
sum_bij
  (λ i h, ⟨i, mem_range.1 h⟩)
  (λ i h, mem_univ _)
  (λ a ha, h ⟨a, _⟩)
  (λ _ _ _ _, fin.veq_of_eq)
  (λ ⟨b, hb⟩ _, ⟨b, mem_range.2 hb, rfl⟩)

example (summand : ℕ → ℕ) (n : ℕ) :
  finset.sum finset.univ (λ (x : fin (succ n)), summand (x.val)) =
    summand n + finset.sum finset.univ (λ (x : fin n), summand (x.val)) :=
by rw [← chris _ _ _ (λ _, rfl), ← chris _ _ _ (λ _, rfl)]; simp
</pre></div>

#### [ Chris Hughes (Mar 30 2018 at 21:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124425956):
<p>Don't know why I didn't think of that.</p>

#### [ Kenny Lau (Mar 30 2018 at 22:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124427350):
<p><span class="user-mention" data-user-id="110038">@Kevin Buzzard</span> in your blog you told us to <code>apply funext</code>, but actually you can just <code>funext</code></p>

#### [ Kevin Buzzard (Mar 30 2018 at 22:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124427917):
<p>I wouldn't believe anything I say :-)</p>

#### [ Kenny Lau (Mar 30 2018 at 22:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124427966):
<p><span class="user-mention" data-user-id="110038">@Kevin Buzzard</span> please moderate my comment</p>


{% endraw %}
