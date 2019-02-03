---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/57659anonymousrecursivefunctions.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [anonymous recursive functions](https://leanprover-community.github.io/archive/113488general/57659anonymousrecursivefunctions.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Andrew Ashworth (Jun 17 2018 at 06:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/anonymous%20recursive%20functions/near/128191984):
<p>is it possible to define an anonymous recursive function? so for I've been making auxiliary defs as needed, but I'm copying a development from coq that uses them a lot</p>

#### [ Andrew Ashworth (Jun 17 2018 at 06:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/anonymous%20recursive%20functions/near/128192028):
<p>something like this from CPDT</p>
<div class="codehilite"><pre><span></span><span class="kn">Definition</span> <span class="n">check_even</span> <span class="o">:</span> <span class="k">forall</span> <span class="n">n</span> <span class="o">:</span> <span class="kt">nat</span><span class="o">,</span> <span class="o">[</span><span class="n">isEven</span> <span class="n">n</span><span class="o">].</span>
  <span class="kn">Hint</span> <span class="n">Constructors</span> <span class="n">isEven</span><span class="o">.</span>

  <span class="k">refine</span> <span class="o">(</span><span class="k">fix</span> <span class="n">F</span> <span class="o">(</span><span class="n">n</span> <span class="o">:</span> <span class="kt">nat</span><span class="o">)</span> <span class="o">:</span> <span class="o">[</span><span class="n">isEven</span> <span class="n">n</span><span class="o">]</span> <span class="o">:=</span>
    <span class="k">match</span> <span class="n">n</span> <span class="k">with</span>
      <span class="o">|</span> <span class="mi">0</span> <span class="o">=&gt;</span> <span class="n">Yes</span>
      <span class="o">|</span> <span class="mi">1</span> <span class="o">=&gt;</span> <span class="n">No</span>
      <span class="o">|</span> <span class="n">S</span> <span class="o">(</span><span class="n">S</span> <span class="n">n&#39;</span><span class="o">)</span> <span class="o">=&gt;</span> <span class="n">Reduce</span> <span class="o">(</span><span class="n">F</span> <span class="n">n&#39;</span><span class="o">)</span>
    <span class="k">end</span><span class="o">);</span> <span class="k">auto</span><span class="o">.</span>
<span class="kn">Defined</span><span class="o">.</span>
</pre></div>

#### [ Mario Carneiro (Jun 17 2018 at 07:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/anonymous%20recursive%20functions/near/128193830):
<p>Unfortunately no, at least not in term mode. As a workaround you can use <code>induction</code>,  but the only way to get the full power of the equation compiler is to have an auxiliary def, and this is what I usually do.</p>

#### [ Simon Hudon (Jun 17 2018 at 15:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/anonymous%20recursive%20functions/near/128204616):
<p>You could write </p>
<div class="codehilite"><pre><span></span><span class="n">nat</span><span class="bp">.</span><span class="n">rec</span> <span class="n">Yes</span> <span class="o">(</span><span class="bp">λ</span> <span class="n">f</span> <span class="n">n</span><span class="o">,</span> <span class="k">match</span> <span class="n">n</span> <span class="k">with</span>
                    <span class="bp">|</span> <span class="mi">0</span> <span class="o">:=</span> <span class="n">No</span>
                    <span class="bp">|</span> <span class="o">(</span><span class="n">succ</span> <span class="n">n&#39;</span><span class="o">)</span> <span class="o">:=</span> <span class="n">Reduce</span> <span class="o">(</span><span class="n">f</span> <span class="n">n&#39;</span><span class="o">)</span>
                   <span class="kn">end</span> <span class="o">)</span>
</pre></div>

#### [ Mario Carneiro (Jun 17 2018 at 19:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/anonymous%20recursive%20functions/near/128211341):
<p>There is also a somewhat hackish way. Did you ever wonder about those <code>_match</code> and <code>_let_match</code> variables in the context sometimes? Those are the same mechanism used to support recursive definitions using the equation compiler, and if you refer to them it will get compiled to a recursive function just like a recursive def. For example:</p>
<div class="codehilite"><pre><span></span>def fib (n : ℕ) : ℕ :=
match n with
| 0 := 0
| 1 := 1
| n+2 := by rename _match fib; exact fib n + fib (n+1)
end
</pre></div>


<p>This doesn't work in term mode though:</p>
<div class="codehilite"><pre><span></span>def fib (n : ℕ) : ℕ :=
match n with
| 0 := 0
| 1 := 1
| n+2 := _match n + _match (n+1)
end
</pre></div>


<p>fails unless you insert <code>by exact</code> on the last line.</p>

#### [ Mario Carneiro (Jun 17 2018 at 19:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/anonymous%20recursive%20functions/near/128211656):
<p>I guess the main reason this isn't already supported officially is because there is no obvious place in match notation to put the name of the defined function</p>

#### [ Mario Carneiro (Jun 17 2018 at 19:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/anonymous%20recursive%20functions/near/128211859):
<p>Examples of the other two match types:</p>
<div class="codehilite"><pre><span></span>inductive tree : Type
| mk : ∀ n, (fin n → tree) → tree

def path : tree → Type :=
λ ⟨n, t⟩, by exact Σ n, _fun_match (t n)

def path&#39; (T : tree) : Type :=
let ⟨n, t⟩ := T in
by exact Σ n, _let_match (t n)
</pre></div>

#### [ Simon Hudon (Jun 17 2018 at 19:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/anonymous%20recursive%20functions/near/128211909):
<p>Cool hack <span class="emoji emoji-1f601" title="grin">:grin:</span></p>


{% endraw %}
