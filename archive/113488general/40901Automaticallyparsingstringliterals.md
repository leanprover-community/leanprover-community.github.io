---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/40901Automaticallyparsingstringliterals.html
---

## Stream: [general](index.html)
### Topic: [Automatically parsing string literals](40901Automaticallyparsingstringliterals.html)

---


{% raw %}
#### [ Joe Hendrix (Dec 12 2018 at 01:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Automatically%20parsing%20string%20literals/near/151491800):
I have a type A and a partial function `parseA : string -> except string A`, is there an easy way to get Lean to automatically call `parseA` parser when I have a literal `("foo" : A)`? If `parseA "foo"` returns `except.ok r` then I'd like `r` to be used, and if it fails I'd like Lean to report the error.
I'm starting down the path of a coercion with a custom tactic, and realized somebody may have done this before.   It's for a library for s-expression parsing/generation.

#### [ Joe Hendrix (Dec 12 2018 at 08:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Automatically%20parsing%20string%20literals/near/151508277):
I ended up with writing a `coerce` tactic that allowed this:

```
meta def to_expr : sexpr → tactic expr := sorry

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
#eval (by coerce "abc")
-- This reports a suitable error message when the tactic runs
#eval (by coerce "def))")
```

I couldn't see a way to introduce a coercion to hide the tactic call, but I suppose I could introduce notation to make the syntax more concise..

#### [ Sebastian Ullrich (Dec 12 2018 at 09:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Automatically%20parsing%20string%20literals/near/151510322):
@**Joe Hendrix** Right, there isn't much more you can do there without some kind of user-definable coercions. One alternative is to make it a custom parser with some prefix token, like we already have with `format! "{x} {y}"`. This _mostly_ works already in Lean 3.

#### [ Joe Hendrix (Dec 12 2018 at 10:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Automatically%20parsing%20string%20literals/near/151513721):
Thanks for the pointer.  Is there any chance that I'd be able to query the environment with that to allow quasi quoting (e.g. `sexpr! "(_ Bitvec %%w)"`) ?  I'd also be interested in synthesizing patterns, but it's not an immediate need.

#### [ Joe Hendrix (Dec 12 2018 at 10:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Automatically%20parsing%20string%20literals/near/151513808):
I just realized that should be doable given that expressions can reference variables.

#### [ Sebastian Ullrich (Dec 12 2018 at 11:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Automatically%20parsing%20string%20literals/near/151514468):
You can't access the parser's set of local variables directly, but you can call it recursively to parse arbitrary expressions like `format!` does. After that you could even analyze or transform the returned pre-term.

#### [ Simon Hudon (Dec 12 2018 at 16:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Automatically%20parsing%20string%20literals/near/151532602):
@**Joe Hendrix**  Actually, you can access the environment and even add variables inside the parser. If I remember correctly, it's a bit confusing because there is a `lean.parser.set_env` as well as `tactic.set_env`. If all you need is reading the environment, `tactic.get_env` should do.

#### [ Joe Hendrix (Dec 12 2018 at 18:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Automatically%20parsing%20string%20literals/near/151541375):
@**Simon Hudon** @**Sebastian Ullrich** Thanks for the pointers.  I have to work on something else for a bit, but will get back to this soon.


{% endraw %}
