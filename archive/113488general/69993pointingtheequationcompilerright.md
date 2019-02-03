---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/69993pointingtheequationcompilerright.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [pointing the equation compiler right](https://leanprover-community.github.io/archive/113488general/69993pointingtheequationcompilerright.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ James Wood (May 13 2018 at 13:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pointing%20the%20equation%20compiler%20right/near/126495867):
<p>Hi, I'm new to Lean. I'm trying to write the following, but termination checking fails for <code>weaken_term</code> in the second recursive call for <code>app</code> and the recursive call for <code>lam</code>. Each time, the reported problem is that <code>m</code> does not decrease, but that should be irrelevant because the induction is on the term. How can I give Lean this hint? Or is the Lean termination checker not sufficiently Foetus-like, so I have to do something else?</p>
<div class="codehilite"><pre><span></span>open nat

inductive fin&#39; : nat → Type
| zero {n} : fin&#39; (succ n)
| succ {n} : fin&#39; n → fin&#39; (succ n)
open fin&#39;

inductive dir : Type
| syn : dir
| chk : dir
open dir

inductive term : nat → dir → Type
| var {n} (i : fin&#39; n)                      : term n syn
| app {n} (e : term n syn) (s : term n chk) : term n syn
| lam {n} (s : term (succ n) chk)           : term n chk
open term

def plus : nat → nat → nat
| zero n := n
| (succ m) n := succ (plus m n)

def weaken_fin&#39; {n} : ∀ m, fin&#39; (plus m n) → fin&#39; (plus m (succ n))
| zero i := succ i
| (succ m) zero := zero
| (succ m) (succ i) := succ (weaken_fin&#39; m i)

def weaken_term {n} : ∀ m {d}, term (plus m n) d → term (plus m (succ n)) d
| m syn (var i) := var (weaken_fin&#39; m i)
| m syn (app e s) := app (weaken_term m e) (weaken_term m s)
| m chk (lam s) := lam (weaken_term (succ m) s)
</pre></div>

#### [ Mario Carneiro (May 13 2018 at 14:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pointing%20the%20equation%20compiler%20right/near/126496313):
<p>It can't be done directly by induction on <code>term</code>, since you would forget the relation to m and n</p>

#### [ Mario Carneiro (May 13 2018 at 14:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pointing%20the%20equation%20compiler%20right/near/126496355):
<p>Here's a way to write that you want to do induction explicitly with the equation compiler:</p>
<div class="codehilite"><pre><span></span>def weaken_term&#39; {n} : ∀ {k d}, term k d → ∀ m, plus m n = k → term (plus m (succ n)) d
| _ syn (var i) m rfl := var (weaken_fin&#39; m i)
| _ syn (app e s) m rfl := app (weaken_term&#39; e m rfl) (weaken_term&#39; s m rfl)
| _ chk (lam s) m rfl := lam (weaken_term&#39; s (succ m) rfl)

def weaken_term {n} (m) {d} (s : term (plus m n) d) : term (plus m (succ n)) d :=
weaken_term&#39; s m rfl
</pre></div>

#### [ James Wood (May 13 2018 at 14:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pointing%20the%20equation%20compiler%20right/near/126496552):
<p>Thanks! Where exactly is the relation to <code>m</code> and <code>n</code> being lost? I can't quite pick out why the term is allowed to depend on the index <code>d</code> like it does.</p>

#### [ Mario Carneiro (May 13 2018 at 14:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pointing%20the%20equation%20compiler%20right/near/126496755):
<p>It might help to try using the <code>induction</code> tactic to get a sense of what lean is doing under the hood</p>

#### [ Mario Carneiro (May 13 2018 at 14:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pointing%20the%20equation%20compiler%20right/near/126497036):
<div class="codehilite"><pre><span></span>def weaken_term {n} : ∀ m {d}, term (plus m n) d → term (plus m (succ n)) d :=
begin
  intros m d s,
  induction s with n&#39; i n&#39; e s IH1 IH2 n&#39; s IH,
  exact var (weaken_fin&#39; m i), --fail
end.
</pre></div>


<p>Notice that you won't be able to prove the first goal because the type is <code>fin' n'</code> instead of <code>fin' (plus m n)</code>. This is where the equality assumption comes in</p>

#### [ Mario Carneiro (May 13 2018 at 14:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pointing%20the%20equation%20compiler%20right/near/126497123):
<p>You can actually prove this directly in tactic mode by starting with</p>
<div class="codehilite"><pre><span></span>  intros m d s,
  generalize h : plus m n = k,
  induction s with n&#39; i n&#39; e s IH1 IH2 n&#39; s IH generalizing k; subst k,
</pre></div>


<p>which has the effect of introducing the equality before doing the induction</p>

#### [ James Wood (May 13 2018 at 14:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pointing%20the%20equation%20compiler%20right/near/126497175):
<p>Can the problem be restated in terms of induction principles, rather than tactics? If so, I think I can work that out.</p>

#### [ Mario Carneiro (May 13 2018 at 14:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pointing%20the%20equation%20compiler%20right/near/126497229):
<p>Look at the proof produced by the naive induction tactic approach:</p>
<div class="codehilite"><pre><span></span>def weaken_term {n} : ∀ m {d}, term (plus m n) d → term (plus m (succ n)) d :=
begin
  intros m d s,
  induction s; admit
end
set_option pp.implicit true
#print weaken_term
</pre></div>


<div class="codehilite"><pre><span></span>def weaken_term : Π {n : ℕ} (m : ℕ) {d : dir}, term (plus m n) d → term (plus m (succ n)) d :=
λ {n : ℕ} (m : ℕ) (d : dir) (s : term (plus m n) d),
  (λ (s : term (plus m n) d),
     @term.rec (λ (_x : ℕ) {d : dir} (s : term _x d), term (plus m (succ n)) d)
       (λ {s_n : ℕ} (s_i : fin&#39; s_n), sorry)
       (λ {s_n : ℕ} (s_e : term s_n syn) (s_s : term s_n chk) (s_ih_e : term (plus m (succ n)) syn)
        (s_ih_s : term (plus m (succ n)) chk), sorry)
       (λ {s_n : ℕ} (s_s : term (succ s_n) chk) (s_ih : term (plus m (succ n)) chk), sorry)
       (plus m n)
       d
       s)
    s
</pre></div>

#### [ Mario Carneiro (May 13 2018 at 14:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pointing%20the%20equation%20compiler%20right/near/126497230):
<p>Notice that the motive to the <code>term.rec</code> is <code>λ (_x : ℕ) {d : dir} (s : term _x d), term (plus m (succ n)) d</code></p>

#### [ Mario Carneiro (May 13 2018 at 14:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pointing%20the%20equation%20compiler%20right/near/126497271):
<p>In other words, it has assumed you are trying to prove <code>def not_true {n} : ∀ m {d} k, term k d → term (plus m (succ n)) d</code></p>

#### [ Mario Carneiro (May 13 2018 at 14:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pointing%20the%20equation%20compiler%20right/near/126497278):
<p>where it has "forgotten" that the <code>k</code> there is actually <code>plus m n</code></p>

#### [ Mario Carneiro (May 13 2018 at 15:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pointing%20the%20equation%20compiler%20right/near/126497464):
<p>By the way, something seems off about your inductive:</p>
<div class="codehilite"><pre><span></span>theorem no_chk {n} : term n chk → false :=
begin
  generalize h : chk = d,
  intro s,
  induction s generalizing h; injection h,
  exact s_ih rfl
end
</pre></div>

#### [ James Wood (May 13 2018 at 15:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pointing%20the%20equation%20compiler%20right/near/126497469):
<p>That's fixed now.</p>

#### [ James Wood (May 13 2018 at 15:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pointing%20the%20equation%20compiler%20right/near/126497994):
<blockquote>
<p>You can actually prove this directly in tactic mode by starting with<br>
...<br>
which has the effect of introducing the equality before doing the induction</p>
</blockquote>
<p>I tried doing this, but I get a lot of weird-looking errors, like “vm check failed”, “invalid 'begin-end' expression, ',' expected”, and “sync”.</p>

#### [ James Wood (May 13 2018 at 15:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pointing%20the%20equation%20compiler%20right/near/126497995):
<p>Code (supporting definitions have changed a bit):</p>
<div class="codehilite"><pre><span></span>def weaken_term&#39; {m} : ∀ n {d}, term&#39; (m + n) d → term&#39; ((m + 1) + n) d :=
begin
  intros n d t,
  generalize h : m + n = k
  induction t with n&#39; i n&#39; e s ihe ihs n&#39; s ih generalizing k; subst k,
  { _ },
  { _ },
  { _ },
  { _ },
  { _ }
end
</pre></div>

#### [ Mario Carneiro (May 13 2018 at 15:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pointing%20the%20equation%20compiler%20right/near/126498056):
<p>You shouldn't use <code>{ _ }</code> as a tactic. Lean doesn't like being asked to run tactics that are not yet determined</p>

#### [ Mario Carneiro (May 13 2018 at 15:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pointing%20the%20equation%20compiler%20right/near/126498057):
<p>instead you can just write <code>{ }</code></p>

#### [ Mario Carneiro (May 13 2018 at 15:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pointing%20the%20equation%20compiler%20right/near/126498058):
<p>meaning "run no tactic", and then it will fail at the right bracket because you aren't done yet</p>

#### [ James Wood (May 13 2018 at 15:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pointing%20the%20equation%20compiler%20right/near/126498099):
<p>Aah, thanks.</p>

#### [ James Wood (May 13 2018 at 15:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pointing%20the%20equation%20compiler%20right/near/126498100):
<p>The problem seemed to be a missing comma, so that's sorted.</p>

#### [ James Wood (May 13 2018 at 15:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pointing%20the%20equation%20compiler%20right/near/126498155):
<p>Is <code>_</code> the best way to leave a hole in a pattern-matching definition?</p>

#### [ James Wood (May 13 2018 at 15:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pointing%20the%20equation%20compiler%20right/near/126498157):
<p>Or is there some way to introduce an interactive hole?</p>

#### [ Mario Carneiro (May 13 2018 at 15:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pointing%20the%20equation%20compiler%20right/near/126498199):
<p>I don't quite understand what you mean</p>

#### [ Mario Carneiro (May 13 2018 at 15:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pointing%20the%20equation%20compiler%20right/near/126498204):
<p>I can't think of what an interactive hole is, but <code>_</code> is useful as a wildcard in patterns</p>

#### [ James Wood (May 13 2018 at 15:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pointing%20the%20equation%20compiler%20right/near/126498247):
<p>Hole à la Agda (or Idris, to some extent).</p>

#### [ James Wood (May 13 2018 at 15:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pointing%20the%20equation%20compiler%20right/near/126498303):
<p>Maybe it's not necessary with the way lean-mode works, though I still feels like a hack to use the “this should be inferrable by unification” thing to mean “I'm going to write something here”.</p>

#### [ Mario Carneiro (May 13 2018 at 15:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pointing%20the%20equation%20compiler%20right/near/126498349):
<p>Lean actually has holes in term mode, <code>{! !}</code>, but they are not well developed at all and never made it past alpha</p>

#### [ Mario Carneiro (May 13 2018 at 15:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pointing%20the%20equation%20compiler%20right/near/126498354):
<p>for the most part you can use <code>begin end</code> or <code>_</code> where stuff is expected</p>


{% endraw %}
