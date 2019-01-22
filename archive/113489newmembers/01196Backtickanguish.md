---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113489newmembers/01196Backtickanguish.html
---

## [new members](index.html)
### [Backtick anguish](01196Backtickanguish.html)

#### [Edward Ayers (Aug 17 2018 at 00:35)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Backtick%20anguish/near/132269318):
What am I doing wrong here?
```lean
meta def my_tactic (q : Prop) : tactic unit := 
  do
  define `qq `(q)
```

```lean
failed to synthesize type class instance for
q : Prop,
my_tactic : tactic unit
⊢ reflected q
```

#### [Edward Ayers (Aug 17 2018 at 00:38)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Backtick%20anguish/near/132269450):
Alternatively:
```lean
open tactic
def my_lemma (q : Prop) : q := 
begin 
  define_core `qq `(q),
  sorry
end
```
```lean
unknown identifier 'q'
```

#### [Simon Hudon (Aug 17 2018 at 00:39)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Backtick%20anguish/near/132269475):
`` `(q) `` is used to build `expr` values but its type is actually `reflected q`. This is a long way of saying that Lean is trying to convert a known value into an expression. Because `q` is a local variable, its value is not know and cannot be reflected. You need to go through ``` to_expr ``(q) ```

#### [Edward Ayers (Aug 17 2018 at 00:39)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Backtick%20anguish/near/132269478):
I want to pass the `local_const` with the pretty name `"q"` as the type arg to `define_core`

#### [Simon Hudon (Aug 17 2018 at 00:41)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Backtick%20anguish/near/132269547):
Your code could be adapted into the following:

```lean
open tactic
def my_lemma (q : Prop) : q :=
begin
  (do my_q <- to_expr ``(q), define_core `qq my_q),
  sorry
end
```

or, more concisely:

```lean
open tactic
def my_lemma (q : Prop) : q :=
begin
  (to_expr ``(q) >>= define_core `qq),
  sorry
end
```

#### [Edward Ayers (Aug 17 2018 at 00:44)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Backtick%20anguish/near/132269677):
This code still errors for me

#### [Edward Ayers (Aug 17 2018 at 00:45)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Backtick%20anguish/near/132269696):
`unknown identifier 'q'`

#### [Edward Ayers (Aug 17 2018 at 00:46)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Backtick%20anguish/near/132269755):
```lean
invalid define tactic, expression is not a type
  ⁇
state:
2 goals
q : Prop
⊢ q

q : Prop
⊢ Sort ?
```

#### [Simon Hudon (Aug 17 2018 at 00:47)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Backtick%20anguish/near/132269770):
Oh! I see why. Use ````(to_expr ```(q) >>= define_core `qq)````: `q` is not available in the scope of your tactic code. With three ticks, you're disabling scope checking when compiling that tactic. Equivalently, you can do ``(get_local `q >>= define_core `qq)``.

