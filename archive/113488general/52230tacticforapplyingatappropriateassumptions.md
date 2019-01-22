---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/52230tacticforapplyingatappropriateassumptions.html
---

## [general](index.html)
### [tactic for applying at appropriate assumptions](52230tacticforapplyingatappropriateassumptions.html)

#### [Sean Leather (May 03 2018 at 10:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tactic for applying at appropriate assumptions/near/126035144):
I've got a theorem:

```lean
theorem lc_value : ∀ {e : exp V}, e.value → e.lc
```

Is there a tactical way to apply this theorem to all assumptions matching `_.value` to produce more assumptions `_.lc`?

#### [Sean Leather (May 03 2018 at 14:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tactic for applying at appropriate assumptions/near/126043003):
How's this for my first attempt at writing a tactic? It can be improved, of course.

```lean
meta def apply_matching (p : parse texpr) : tactic expr :=
  do e ← to_expr p,
     et ← infer_type e,
     guard et.is_arrow <|> fail format!"'apply_matching' expected a function, got '{et}'",
     any_hyp $ λ h, do
       ht ← infer_type h,
       unify ht et.binding_domain,
       n ← mk_fresh_name,
       note n none (expr.mk_app e [h])
```

#### [Sean Leather (May 03 2018 at 14:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tactic for applying at appropriate assumptions/near/126043088):
That is, I know some ways in which it can be improved, but comments to that effect are most welcome.

#### [Sean Leather (May 03 2018 at 14:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tactic for applying at appropriate assumptions/near/126043239):
I believe I've jumped into the rabbit hole now.

#### [Simon Hudon (May 03 2018 at 19:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tactic for applying at appropriate assumptions/near/126055842):
If I understand correctly, given a rule `r : p -> q` (where you call my `r` `p`) you're looking for an assumption `h : p` which would allow you to add an assumption `h' : q`. 

First question: do you expect the user to see the name of that new assumption? If so, I doubt `mk_fresh_name` will give you appealing names. Maybe you should give at least the option of specifying the name.

#### [Simon Hudon (May 03 2018 at 19:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tactic for applying at appropriate assumptions/near/126055958):
Second question: is there a reason that your rule wouldn't be desirable if you had a pi type where the bound variable occurs in the term?

#### [Simon Hudon (May 03 2018 at 19:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tactic for applying at appropriate assumptions/near/126056021):
Third question:  could it not be useful to repeat the process a certain number of times (if the user provides a list of names for the new assumptions, repeat until you run out of names; otherwise, repeat as many times as you can).

#### [Sean Leather (May 04 2018 at 08:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tactic for applying at appropriate assumptions/near/126083155):
@**Simon Hudon** Thanks for looking at it!

```quote
If I understand correctly, given a rule `r : p -> q` (where you call my `r` `p`) you're looking for an assumption `h : p` which would allow you to add an assumption `h' : q`. 
```

That's almost correct. My current thinking is to look for all assumptions `h_i : p` and create all possible new assumptions `h_i' : q` where `h_i' = r h_i`.

```quote
First question: do you expect the user to see the name of that new assumption? If so, I doubt `mk_fresh_name` will give you appealing names. Maybe you should give at least the option of specifying the name.
```

In general, I would expect the new assumptions to be used in something like `tauto` or possibly just `assumption`. But I would certainly like to have useful fresh names and not the stuff spit out by `mk_fresh_name`. (I'm now using `get_unused_name`, but that doesn't seem much better.) Since multiple fresh names may be created, I think the option of specifying one name is not enough. I thought about doing something like adding a suffix to the name of `h`. How do I get the name of the hypothesis from the `expr`?  What do you think?

```quote
Second question: is there a reason that your rule wouldn't be desirable if you had a pi type where the bound variable occurs in the term?
```

Perhaps not. Are you suggesting I use `is_pi` instead of `is_arrow`?

```quote
Third question:  could it not be useful to repeat the process a certain number of times (if the user provides a list of names for the new assumptions, repeat until you run out of names; otherwise, repeat as many times as you can).
```

Repeating is indeed my intention. Is it not doing that? I haven't yet tested. But, looking again at `any_hyp_aux`, it looks like it does stop at the first success. Is there an existing function for iterating over all of the local context or `list expr`, or should I write one?

#### [Sean Leather (May 04 2018 at 08:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tactic for applying at appropriate assumptions/near/126083607):
```quote
Is there an existing function for iterating over all of the local context or `list expr`, or should I write one?
```

Answering my own question: `list.mfoldl`/`list.mfoldr`

#### [Sean Leather (May 04 2018 at 10:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tactic for applying at appropriate assumptions/near/126085893):
The latest version with `expr.is_pi` and `list.mfoldl`:

```lean
meta def apply_matching (p : parse texpr) : tactic unit :=
  do e ← to_expr p,
     et ← infer_type e,
     guard et.is_pi <|> fail format!"'apply_matching' expected a function, got '{et}'",
     local_context >>= mfoldl
       (λ a h, do
         ht ← infer_type h,
         tactic.try (do
           unify ht et.binding_domain,
           n ← get_unused_name,
           note n none (expr.mk_app e [h])))
       ()
```

#### [Sean Leather (May 04 2018 at 10:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tactic for applying at appropriate assumptions/near/126085942):
It's funny and annoying that I keep forgetting the commas in Lean `do`-notation.

#### [Sean Leather (May 04 2018 at 11:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tactic for applying at appropriate assumptions/near/126088409):
Now with a `'` appended to the name of the source hypothesis:

```lean
meta def name.update_suffix : name → (string → string) → name
| name.anonymous        _ := name.anonymous
| (name.mk_string s p)  f := name.mk_string (f s) p
| (name.mk_numeral n p) _ := name.mk_numeral n p

meta def apply_matching (p : parse texpr) : tactic unit :=
  do e ← to_expr p,
     et ← infer_type e,
     guard et.is_pi <|> fail format!"'apply_matching' expected a function, got '{et}'",
     local_context >>= mfoldl
       (λ a h, do
         ht ← infer_type h,
         tactic.try $ do
           unify ht et.binding_domain,
           note (h.local_pp_name.update_suffix (flip append "'")) none (expr.mk_app e [h]))
       ()
```

#### [Sean Leather (May 04 2018 at 11:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tactic for applying at appropriate assumptions/near/126088722):
Hmm. I thought perhaps I could remove `ht ← infer_type h` and `unify ht et.binding_domain` because `note` would type check the expression `expr.mk_app e [h])`, but I ended up generating a new hypothesis for every existing hypothesis. `note` is defined with `assertv_core`, but it didn't do what I would expect from a cursory reading.

#### [Simon Hudon (May 04 2018 at 14:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tactic for applying at appropriate assumptions/near/126093166):
Sorry I missed the first question. At least, you didn't miss it

#### [Simon Hudon (May 04 2018 at 14:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tactic for applying at appropriate assumptions/near/126093228):
I would change:

```
 et ← infer_type e,
 guard et.is_pi <|> fail format!"'apply_matching' expected a function, got '{et}'",
```

to

```
 (expr.pi _ _ ed _) <- infer_type | fail format!"'apply_matching' expected a function, got '{et}'",
```

#### [Simon Hudon (May 04 2018 at 14:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tactic for applying at appropriate assumptions/near/126093239):
and `.local_pp_name.update_suffix (flip append "'")` to `.local_pp_name.update_suffix (++ "'")`

#### [Simon Hudon (May 04 2018 at 14:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tactic for applying at appropriate assumptions/near/126093335):
```quote
`note` is defined with `assertv_core`, but it didn't do what I would expect from a cursory reading.
```

Care to elaborate?

#### [Sean Leather (May 04 2018 at 14:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tactic for applying at appropriate assumptions/near/126093336):
```quote
```lean
 (expr.pi _ _ ed _) <- infer_type | fail format!"'apply_matching' expected a function, got '{et}'",
```
```

What is `|` here? Is this equivalent to the following bracketing (assuming said bracketing is valid)?

```lean
((expr.pi _ _ ed _) <- infer_type) | (fail format!"'apply_matching' expected a function, got '{et}'"),
```

#### [Sean Leather (May 04 2018 at 14:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tactic for applying at appropriate assumptions/near/126093350):
```quote
and `.local_pp_name.update_suffix (flip append "'")` to `.local_pp_name.update_suffix (++ "'")`
```
Ah, sections are supported. I wasn't sure and didn't try.

#### [Simon Hudon (May 04 2018 at 14:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tactic for applying at appropriate assumptions/near/126093403):
No, I don't think that's syntactically valid. It's because `(expr.pi _ _ ed _) <- infer_type` is an incomplete pattern matching statement. `|` comes in to say "here's what you do if it doesn't match ..."

#### [Sean Leather (May 04 2018 at 14:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tactic for applying at appropriate assumptions/near/126093486):
```quote
```quote
`note` is defined with `assertv_core`, but it didn't do what I would expect from a cursory reading.
```

Care to elaborate?
```
About? :simple_smile:

#### [Sean Leather (May 04 2018 at 14:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tactic for applying at appropriate assumptions/near/126093504):
```quote
No, I don't think that's syntactically valid. It's because `(expr.pi _ _ ed _) <- infer_type` is an incomplete pattern matching statement. `|` comes in to say "here's what you do if it doesn't match ..."
```
I see. Is this `|` strictly for pattern-matching in `do`-notation? Is it notation defined somewhere, or is it built in?

#### [Simon Hudon (May 04 2018 at 14:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tactic for applying at appropriate assumptions/near/126093554):
And there's a subtle difference with `<|>`. While `do x <- a <|> b, c` means `a <|> b >>= λ x, c`, `do x <- a | b, c` means:

```
a >>= λ x₀, 
match x₀ with
 | x := c 
 | _ := b
end
```

#### [Simon Hudon (May 04 2018 at 14:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tactic for applying at appropriate assumptions/near/126093560):
i.e. when you run `b`, you exit immediately. If `b` is not a fail statement but a statement like `return none`, the whole function returns `non`.

#### [Sean Leather (May 04 2018 at 14:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tactic for applying at appropriate assumptions/near/126093665):
```quote
```lean
 (expr.pi _ _ ed _) <- infer_type | fail format!"'apply_matching' expected a function, got '{et}'",
```
```
Except that, with this, I no longer have `et`. :wink:

#### [Simon Hudon (May 04 2018 at 14:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tactic for applying at appropriate assumptions/near/126093722):
```quote
```quote
```quote
note is defined with assertv_core, but it didn't do what I would expect from a cursory reading.
```
Care to elaborate?
```
About? 
```

Hoping to break records of quotes within quotes, here's my answer. Please, let's make this an Inception of quotes.

What did you expect from `assertv_core` and how did the reality differ?

#### [Simon Hudon (May 04 2018 at 14:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tactic for applying at appropriate assumptions/near/126093796):
```quote
```quote
```lean
 (expr.pi _ _ ed _) <- infer_type | fail format!"'apply_matching' expected a function, got '{et}'",
```
```
Except that, with this, I no longer have `et`. :wink:
```
I missed the occurrence in the error message. What a bummer! I thought we could get rid of it. Let's go with:

```lean
 et <- infer_type,
 (expr.pi _ _ ed _) <- pure et | fail format!"'apply_matching' expected a function, got '{et}'",
```

#### [Sean Leather (May 04 2018 at 14:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tactic for applying at appropriate assumptions/near/126093802):
```quote
What did you expect from `assertv_core` and how did the reality differ?
```
As I said, I expected it to type-check the expression.

#### [Sean Leather (May 04 2018 at 14:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tactic for applying at appropriate assumptions/near/126093848):
```quote
Let's go with:

```lean
 et <- infer_type,
 (expr.pi _ _ ed _) <- pure et | fail format!"'apply_matching' expected a function, got '{et}'",
```
```

Hmm, I'm not convinced that's better. :wink:

#### [Simon Hudon (May 04 2018 at 14:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tactic for applying at appropriate assumptions/near/126093923):
Oh I see. I would think that too. But as the developers keep pointing out, they are very aggressive in their optimization. They try to never type check by default. The whole proof will be type checked at the end so that's not unsafe but it does mean that you have to `unify` or `type_check` when you think you need it.

#### [Sean Leather (May 04 2018 at 14:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tactic for applying at appropriate assumptions/near/126093981):
```quote
Oh I see. I would think that too. But as the developers keep pointing out, they are very aggressive in their optimization. They try to never type check by default. The whole proof will be type checked at the end so that's not unsafe but it does mean that you have to `unify` or `type_check` when you think you need it.
```
Oh, interesting. So, you can introduce badly typed hypotheses?

#### [Sean Leather (May 04 2018 at 14:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tactic for applying at appropriate assumptions/near/126093988):
```quote
Oh, interesting. So, you can introduce badly typed hypotheses?
```
... and goals?

#### [Simon Hudon (May 04 2018 at 14:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tactic for applying at appropriate assumptions/near/126093993):
```quote
```quote
Let's go with:

```lean
 et <- infer_type,
 (expr.pi _ _ ed _) <- pure et | fail format!"'apply_matching' expected a function, got '{et}'",
```
```

Hmm, I'm not convinced that's better. :wink:
```
Yeah, that's less of an improvement

#### [Simon Hudon (May 04 2018 at 14:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tactic for applying at appropriate assumptions/near/126094048):
```quote
```quote
Oh, interesting. So, you can introduce badly typed hypotheses?
```
... and goals?
```
The expressions and goals are still type checked from time to time but you can find a way.

#### [Simon Hudon (May 04 2018 at 14:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tactic for applying at appropriate assumptions/near/126094114):
I think `to_expr` type checks the expression so that already filters out a lot of nonsense

#### [Sean Leather (May 04 2018 at 14:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tactic for applying at appropriate assumptions/near/126094120):
```quote
```quote
```quote
```quote
note is defined with assertv_core, but it didn't do what I would expect from a cursory reading.
```
Care to elaborate?
```
About? 
```

Hoping to break records of quotes within quotes, here's my answer. Please, let's make this an Inception of quotes.
```
I think Zulip needs threads within topics within streams... :house_buildings:

#### [Sean Leather (May 04 2018 at 14:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tactic for applying at appropriate assumptions/near/126094324):
Current version:

```lean
meta def note_all_applied (p : parse texpr) : tactic unit :=
  do e ← to_expr p,
     et ← infer_type e,
     guard et.is_pi <|> fail format!"'note_all_applied' expected a function, got '{et}'",
     local_context >>= mfoldl
       (λ a h, do
         ht ← infer_type h,
         tactic.try $ do
           unify ht et.binding_domain,
           note (h.local_pp_name.update_suffix (++ "'")) none (e.mk_app [h]))
       ()
```

I'm not really sure about a good name. `apply_matching` is certainly not good: too much of a connection to `apply`.

#### [Simon Hudon (May 04 2018 at 14:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tactic for applying at appropriate assumptions/near/126094606):
how about `have_spec` (for specialization)?

#### [Simon Hudon (May 04 2018 at 14:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tactic for applying at appropriate assumptions/near/126094623):
I think you you should check if the domain of `e` is a proposition. If it is, having multiple specializations will only be noisy

#### [Sean Leather (May 04 2018 at 14:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tactic for applying at appropriate assumptions/near/126094786):
```quote
how about `have_spec` (for specialization)?
```

1. My immediate thought is to expand `spec` to `specification`.
2. I would not naturally think of this as specialization. The resulting type depends on the argument.

#### [Johan Commelin (May 04 2018 at 15:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tactic for applying at appropriate assumptions/near/126094897):
and Kevin is defining the `spec`trum of a ring... although that will probably be called `Spec`.

#### [Sean Leather (May 04 2018 at 15:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tactic for applying at appropriate assumptions/near/126095717):
```quote
I think you you should check if the domain of `e` is a proposition. If it is, having multiple specializations will only be noisy
```

I don't follow. If I have this:

```lean
have h : Prop := true,
note_all_applied or_true
```

I see this:

```lean
h : Prop,
h' : h ∨ true ↔ true
```

#### [Simon Hudon (May 04 2018 at 15:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tactic for applying at appropriate assumptions/near/126096992):
*a proposition*

```lean
assume h :  x ≤ y,
assume h' :  x ≤ y,
note_all_applied (not_lt_of_ge x y)
```

The above should only produce one more assumption, not two.

#### [Sean Leather (May 06 2018 at 11:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tactic for applying at appropriate assumptions/near/126170825):
@**Simon Hudon** I'm sorry, but I'm still not getting what you're saying.

What do you mean by a proposition? I used `h : Prop`, but you may be thinking of something else.

I tried to make a working example out of your code, and this is what I have:

```lean
example {x y : ℕ} (h h' : x ≤ y) : Prop := by note_all_applied not_lt_of_ge
```

The state:

```lean
x y : ℕ,
h h' : x ≤ y,
h' h'' : ¬y < x
⊢ ?m_1
```

So, two things are clearly problematic here:

* Output hypotheses (`h'`, `h''`) with the same type (`¬y < x`). However, there are input hypotheses with the same type. I'm not sure this is something the tactic should handle because:
  * Handling duplicate outputs adds complexity when the duplicate inputs already exist, and, consequently, this complexity appears unnecessary.
  * If the tactic did something else, what would it be, and would it still be predictable?
* Duplicate `h'` hypotheses. The output hypothesis naming could certainly be better. It would be nice to have fresh, readable, predictable names, perhaps similar to what `cases` and `induction` do. Do you have any suggestions for this?

That said, I'm not sure what the above has to do with propositions. The same issues can be shown with non-`Prop` types:

```lean
example (x y : ℕ) : Prop := by note_all_applied nat.succ
```

```lean
x y x' y' : ℕ
⊢ Prop
```

#### [Simon Hudon (May 06 2018 at 19:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tactic for applying at appropriate assumptions/near/126183355):
What I was trying to point out is that the types of `h`,`h'`,`h'` and `h''` themselves have type `Prop`. Maybe I should have called them proofs instead of proposition. Sorry for the confusion.

I was saying that using many of them in your tactic would result in repetition because of proof irrelevant.

#### [Simon Hudon (May 06 2018 at 19:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tactic for applying at appropriate assumptions/near/126183363):
As you point out, that might make for a highly redundant tactic code.

#### [Simon Hudon (May 06 2018 at 20:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tactic for applying at appropriate assumptions/near/126183637):
If you decide to adopt that more aggressive simplification, you can replace `mfold` or `for_each` with:

```
meta def for_each_considering_proof_irrelevance {α : Type}
  (irrel : bool) (f : α → tactic unit) (xs : list α) : tactic unit :=
if irrel then
  xs.any_of f
else
  xs.for_each f
```

#### [Sean Leather (May 07 2018 at 08:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tactic for applying at appropriate assumptions/near/126202657):
Thanks for pointing at `for_each` and `any_of`. Funny that they don't seem to be used at all in the Lean core library.

#### [Scott Morrison (Aug 09 2018 at 08:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tactic for applying at appropriate assumptions/near/131154182):
Hi @**Sean Leather**, what happened to this tactic? I think I want it now, and I'm not sure where to look for it.

#### [Sean Leather (Aug 09 2018 at 09:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tactic for applying at appropriate assumptions/near/131155526):
You mean the one and only tactic I ever wrote? It's [here](https://github.com/spl/tts/blob/69893255c64e407f3b3ca6e9ff6242f7120177d8/src/tactics.lean#L15-L24). I think I use it in the same repository, but I'm not convinced it is actually that useful.

