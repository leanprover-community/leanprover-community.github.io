---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/40901Automaticallyparsingstringliterals.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [Automatically parsing string literals](https://leanprover-community.github.io/archive/113488general/40901Automaticallyparsingstringliterals.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Joe Hendrix (Dec 12 2018 at 01:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Automatically%20parsing%20string%20literals/near/151491800):
<p>I have a type A and a partial function <code>parseA : string -&gt; except string A</code>, is there an easy way to get Lean to automatically call <code>parseA</code> parser when I have a literal <code>("foo" : A)</code>? If <code>parseA "foo"</code> returns <code>except.ok r</code> then I'd like <code>r</code> to be used, and if it fails I'd like Lean to report the error.<br>
I'm starting down the path of a coercion with a custom tactic, and realized somebody may have done this before.   It's for a library for s-expression parsing/generation.</p>

#### [ Joe Hendrix (Dec 12 2018 at 08:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Automatically%20parsing%20string%20literals/near/151508277):
<p>I ended up with writing a <code>coerce</code> tactic that allowed this:</p>
<div class="codehilite"><pre><span></span>meta def to_expr : sexpr → tactic expr := sorry

-- This tries to prove a property by just running the evaluator.
meta def coerce (s:string) : tactic unit := do
  match parse s with
  | (except.ok r) := do
    e ← to_expr r,
    tactic.exact e
  | (except.error msg) := do
    tactic.fail msg
  end

-- This works
#eval (by coerce &quot;abc&quot;)
-- This reports a suitable error message when the tactic runs
#eval (by coerce &quot;def))&quot;)
</pre></div>


<p>I couldn't see a way to introduce a coercion to hide the tactic call, but I suppose I could introduce notation to make the syntax more concise..</p>

#### [ Sebastian Ullrich (Dec 12 2018 at 09:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Automatically%20parsing%20string%20literals/near/151510322):
<p><span class="user-mention" data-user-id="110994">@Joe Hendrix</span> Right, there isn't much more you can do there without some kind of user-definable coercions. One alternative is to make it a custom parser with some prefix token, like we already have with <code>format! "{x} {y}"</code>. This _mostly_ works already in Lean 3.</p>

#### [ Joe Hendrix (Dec 12 2018 at 10:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Automatically%20parsing%20string%20literals/near/151513721):
<p>Thanks for the pointer.  Is there any chance that I'd be able to query the environment with that to allow quasi quoting (e.g. <code>sexpr! "(_ Bitvec %%w)"</code>) ?  I'd also be interested in synthesizing patterns, but it's not an immediate need.</p>

#### [ Joe Hendrix (Dec 12 2018 at 10:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Automatically%20parsing%20string%20literals/near/151513808):
<p>I just realized that should be doable given that expressions can reference variables.</p>

#### [ Sebastian Ullrich (Dec 12 2018 at 11:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Automatically%20parsing%20string%20literals/near/151514468):
<p>You can't access the parser's set of local variables directly, but you can call it recursively to parse arbitrary expressions like <code>format!</code> does. After that you could even analyze or transform the returned pre-term.</p>

#### [ Simon Hudon (Dec 12 2018 at 16:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Automatically%20parsing%20string%20literals/near/151532602):
<p><span class="user-mention" data-user-id="110994">@Joe Hendrix</span>  Actually, you can access the environment and even add variables inside the parser. If I remember correctly, it's a bit confusing because there is a <code>lean.parser.set_env</code> as well as <code>tactic.set_env</code>. If all you need is reading the environment, <code>tactic.get_env</code> should do.</p>

#### [ Joe Hendrix (Dec 12 2018 at 18:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Automatically%20parsing%20string%20literals/near/151541375):
<p><span class="user-mention" data-user-id="110026">@Simon Hudon</span> <span class="user-mention" data-user-id="110024">@Sebastian Ullrich</span> Thanks for the pointers.  I have to work on something else for a bit, but will get back to this soon.</p>


{% endraw %}
