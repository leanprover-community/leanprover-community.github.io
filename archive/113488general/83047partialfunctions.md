---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/83047partialfunctions.html
---

## [general](index.html)
### [partial functions](83047partialfunctions.html)

#### [Victor Porton (Jul 07 2018 at 17:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/partial functions/near/129261641):
Why this does not work?

-- Switch from a function on a subset to a function to option monad
def subfunc_to_option {α β: Type} {c: α → Prop} (f: {x:α // c x} → β) : α → option β :=
λ y: α, if c y then some (f (subtype.mk y (arbitrary (c y) [true_inhabited (c y)]))) else none

#### [Kenny Lau (Jul 07 2018 at 17:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/partial functions/near/129261658):
put [decidable_pred c] in the list of assumptions (before the colon)

#### [Victor Porton (Jul 07 2018 at 17:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/partial functions/near/129261720):
Kenny, I did what you say. Moreover `open classical` is already in effect. But it does not work now too

#### [Chris Hughes (Jul 07 2018 at 17:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/partial functions/near/129262022):
```lean
def subfunc_to_option {α β: Type} {c: α → Prop} [decidable_pred c] 
(f: {x:α // c x} → β) : α → option β :=
λ y: α, if h : c y then some (f (subtype.mk y h)) else none
```

#### [Chris Hughes (Jul 07 2018 at 17:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/partial functions/near/129262116):
`if h : c y` instead of `if c y` gives you access to the proof.

#### [Victor Porton (Jul 07 2018 at 17:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/partial functions/near/129262182):
Chris, Thanks it works now. But I am curious why my old code (with `arbitrary`) didn't work.

#### [Chris Hughes (Jul 07 2018 at 17:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/partial functions/near/129262210):
Because there was no way of telling that the type `c y` was inhabited.

#### [Chris Hughes (Jul 07 2018 at 17:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/partial functions/near/129262269):
It's actually very unusual to use `inhabited` on Props.

#### [Chris Hughes (Jul 07 2018 at 18:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/partial functions/near/129262352):
Also `open classical` only opens the classical namespace, it doesn't give you decidability. You need `local attribute [instance] classical.prop_decidable` for that.

#### [Victor Porton (Jul 07 2018 at 18:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/partial functions/near/129262806):
I tried to synthesize the function in another direction. Now I know where is my error but don't know how to fix it:

-- Switch from function to option monad to a function on a subset
def option_to_subfunc {α β: Type} (f: α → (option β)) :=
λ y: {x:α // f x ≠ none},
match f y with
| some x := y
| none   := sorry

#### [Chris Hughes (Jul 07 2018 at 18:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/partial functions/near/129262898):
You needed to give the type, and write `end` at the end of your `match`
```lean
def option_to_subfunc {α β: Type} (f: α → (option β)) : 
  {x : α // f x ≠ none} → {x:α // f x ≠ none} :=
λ y: {x:α // f x ≠ none},
match f y with
| some x := y
| none := sorry
end
```

#### [Johan Commelin (Jul 07 2018 at 18:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/partial functions/near/129262906):
@**Victor Porton** If you surround your code between three backticks, then it will be typeset in a codeblock. If you append "lean" to the first 3 backticks, then it will get highlighting!

#### [Kevin Buzzard (Jul 07 2018 at 18:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/partial functions/near/129262950):
Again `f y` does not make sense because alpha is not equal to the subtype you are using. f wants an input of type alpha and you are feeding it `y`. Did you read about subtypes in Theorem in Lean?

#### [Victor Porton (Jul 07 2018 at 18:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/partial functions/near/129262952):
@**Chris Hughes** Your code does not validate. What I really wanted to ask is what to do instead of `sorry`. I am lost about this

#### [Chris Hughes (Jul 07 2018 at 18:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/partial functions/near/129262957):
It does make sense because there's a coercion

#### [Victor Porton (Jul 07 2018 at 18:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/partial functions/near/129262963):
Yes, I knew that here there is a coercion

#### [Kevin Buzzard (Jul 07 2018 at 18:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/partial functions/near/129262965):
Oh -- it does make sense in this context because there's a coercion!

#### [Kevin Buzzard (Jul 07 2018 at 18:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/partial functions/near/129262967):
:-)

#### [Chris Hughes (Jul 07 2018 at 18:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/partial functions/near/129263099):
In response to a question in (no topic) that should have been here.
```lean
def option_to_subfunc {α β: Type} (f: α → (option β)) : 
  {x : α // f x ≠ none} → {x:α // f x ≠ none} :=
λ y: {x:α // f x ≠ none},
have hfy : f y ≠ none := y.2,
match f y, hfy with
| some x := λ hfy, y
| none := λ hfy, (hfy rfl).elim
end
```

#### [Victor Porton (Jul 07 2018 at 18:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/partial functions/near/129263253):
@**Chris Hughes**  1.  The values type of your `option_to_subfunc` is wrong; it should be `\beta` not `{x:α // f x ≠ none}`. 2. Do I understand correctly that the values in `have` are "ignored" (not included into the result) when building the value of the defined object? 3. What this elimination do? (I am a very novice and understand your code partially.)

#### [Victor Porton (Jul 07 2018 at 18:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/partial functions/near/129263319):
@**Chris Hughes** Sorry for a stupid question but I do not understand what `:=` after `have` means

#### [Chris Hughes (Jul 07 2018 at 18:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/partial functions/near/129263329):
It's the same as `from`

#### [Victor Porton (Jul 07 2018 at 18:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/partial functions/near/129263344):
I am trying to read your code

#### [Victor Porton (Jul 07 2018 at 18:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/partial functions/near/129263411):
Sorry, what is `λ hfy, y`?

#### [Chris Hughes (Jul 07 2018 at 18:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/partial functions/near/129263412):
I put `hfy` after the `match` so I would have access to the fact that `f y ≠ none`. In the `none` cases `hfy` has type `none ≠ none` which is obviously false, so I can use `false.elim` to define the function

#### [Chris Hughes (Jul 07 2018 at 18:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/partial functions/near/129263460):
`hfy` is just a proof that `f y = none` or in the `some` case that `some ≠ none`

#### [Chris Hughes (Jul 07 2018 at 18:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/partial functions/near/129263520):
I think this is the function you want
```lean
def option_to_subfunc {α β: Type} (f: α → (option β)) : 
  {x : α // f x ≠ none} → β :=
λ y: {x:α // f x ≠ none},
have hfy : f y ≠ none := y.2,
match f y, hfy with
| some x := λ hfy, x
| none := λ hfy, (hfy rfl).elim
end
```

#### [Victor Porton (Jul 07 2018 at 18:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/partial functions/near/129263532):
what is `(hfy rfl).elim`?

#### [Chris Hughes (Jul 07 2018 at 18:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/partial functions/near/129263533):
`match f y, hfy with` means I now have to define a function with type `Π x : option β, x ≠ none → β `

#### [Chris Hughes (Jul 07 2018 at 18:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/partial functions/near/129263572):
`hfy rfl` is a proof of `false`

#### [Chris Hughes (Jul 07 2018 at 18:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/partial functions/near/129263574):
`(hfy rfl).elim` is another way of writing `false.elim (hfy rfl)`.

#### [Victor Porton (Jul 07 2018 at 18:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/partial functions/near/129263581):
I need to time to review all you wrote

#### [Chris Hughes (Jul 07 2018 at 18:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/partial functions/near/129263582):
`false.elim` is a function that gives you a term of any type given a proof of `false`

#### [Victor Porton (Jul 07 2018 at 18:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/partial functions/near/129263706):
What I don't understand: Why is it `| some x := λ hfy, x` not `| some x := x`. It should be a value in `\b`, right? But `λ hfy, x` is a function and so it looks for me that it can't be in `\b`

#### [Victor Porton (Jul 07 2018 at 18:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/partial functions/near/129263710):
err.. wrong

#### [Chris Hughes (Jul 07 2018 at 18:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/partial functions/near/129263833):
`match f y, hfy` with means I now have to define a function with type `Π x : option β, x ≠ none → β`, not `option β → β` any more.  Even though I'm not using the fact that `x  ≠ none` in the `some` case, I still have access to it.

#### [Victor Porton (Jul 07 2018 at 18:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/partial functions/near/129263923):
Hm, it is harder than I expected, I yet do not understand the details of this simple construct. I initially started to learn Lean to rewrite my English book in Lean. Now I suspect that it would take me too much time to master Lean. What is your advice: learn Lean or just to keep writing math in English?

#### [Chris Hughes (Jul 07 2018 at 18:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/partial functions/near/129263975):
What field of maths is your book on?

#### [Chris Hughes (Jul 07 2018 at 18:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/partial functions/near/129264037):
I think maybe a good way to think about the function is that the output of type `β` is the function of type `Π x : option β, x ≠ none → β` applied to `f y` and `hfy`

#### [Victor Porton (Jul 07 2018 at 18:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/partial functions/near/129264039):
@**Chris Hughes** I discovered a new subfield of general topology (though some man expressed that he does not consider it a subfield of general topology). For example the formula $f\circ\mu \leq \nu\circ f$ means that $f$ is a continuous morphisms from $\mu$ to $\nu$.

#### [Chris Hughes (Jul 07 2018 at 18:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/partial functions/near/129264095):
I don't really know much about topology (I'm a first year undergraduate). I think @**Patrick Massot** and @**Johannes Hölzl**  know about topology in lean.

#### [Victor Porton (Jul 07 2018 at 18:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/partial functions/near/129264096):
Honestly, I am somehow lost in your Lean discussion. I may re-read it again

#### [Victor Porton (Jul 07 2018 at 18:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/partial functions/near/129264123):
@**Chris Hughes** This does not matter, as I build my version of topology from scratch, without using the classical GT

#### [Victor Porton (Jul 07 2018 at 18:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/partial functions/near/129264230):
Is `match f y, hfy` the same as `match \<f y, hfy\>`?

#### [Chris Hughes (Jul 07 2018 at 19:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/partial functions/near/129264474):
more or less
```lean
def option_to_subfunc {α β: Type} (f: α → (option β)) : 
  {x : α // f x ≠ none} → β :=
λ y: {x:α // f x ≠ none},
have hfy : f y ≠ none := y.2,
match (⟨f y, hfy⟩ : Σ' x : option β, x ≠ none) with
| ⟨some x, hfy⟩ := x
| ⟨none, hfy⟩ := (hfy rfl).elim
end
```

#### [Chris Hughes (Jul 07 2018 at 19:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/partial functions/near/129264557):
I think that might be more confusing though.

#### [Victor Porton (Jul 07 2018 at 19:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/partial functions/near/129264689):
It seems that I do (or almost do) understand your last ("more confusing") code. But why the "less confusing" code (which I don't understand) uses `some x := λ hfy, x` not `some x := x`?

#### [Victor Porton (Jul 07 2018 at 19:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/partial functions/near/129264699):
oh, it seems I got the idea

#### [Victor Porton (Jul 07 2018 at 19:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/partial functions/near/129264809):
I have yet a question. How does the following work?
```lean
match f y, hfy with
| some x := λ hfy, x
| none := λ hfy, (hfy rfl).elim
end
```
We have two expressions in `match` arguments and just one in the math conditions. How do they match?

#### [Chris Hughes (Jul 07 2018 at 19:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/partial functions/near/129265113):
I don't really understand enough about the equation compiler to answer the question properly.

#### [Victor Porton (Jul 07 2018 at 19:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/partial functions/near/129265139):
@**Chris Hughes** Anyway much thanks for your support. Also what does $\Sigma'$ mean? It has added apostrophe

#### [Victor Porton (Jul 07 2018 at 19:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/partial functions/near/129265189):
Now I "almost" understand. Thanks

#### [Chris Hughes (Jul 07 2018 at 19:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/partial functions/near/129265206):
It's just like Sigma, except the constructors can be either proofs or data, whereas Sigma only takes data.

#### [Chris Hughes (Jul 07 2018 at 19:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/partial functions/near/129265352):
This is perhaps a better way of writing the function
```lean
def option_to_subfunc {α β: Type} (f: α → (option β)) : 
  {x : α // f x ≠ none} → β :=
λ y : {x:α // f x ≠ none},
let g : Π x : option β, x ≠ none → β :=
  λ x, match x with
  | (some x) := λ h, x
  | none := λ h, (h rfl).elim
  end in
g (f y) y.property
```

#### [Victor Porton (Jul 07 2018 at 19:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/partial functions/near/129265357):
@**Chris Hughes** It gets better as I rewrote it more understandably
```lean
def option_to_subfunc {α β: Type} (f: α → (option β)) :
  {x : α // f x ≠ none} → β :=
λ y: {x:α // f x ≠ none},
have hfy : f y ≠ none := y.2,
match f y, hfy with
| some x, hfy := x
| none  , hfy := (hfy rfl).elim
end
```

#### [Victor Porton (Jul 07 2018 at 19:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/partial functions/near/129265405):
I don't understand your last code. For example, what is `property`?

#### [Chris Hughes (Jul 07 2018 at 19:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/partial functions/near/129265438):
Another way of writing `y.2`

#### [Victor Porton (Jul 07 2018 at 19:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/partial functions/near/129265498):
Why do you think the the second way is better?

#### [Chris Hughes (Jul 07 2018 at 19:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/partial functions/near/129265655):
I had to try out a few things to get the first way to work. For example this didn't work. I don't really have a good reason why the second way is better other than that. 
```lean
def option_to_subfunc {α β: Type} (f: α → (option β)) :
  {x : α // f x ≠ none} → β :=
λ y: {x:α // f x ≠ none},
match f y, y.2 with
| some x, hfy := x
| none  , hfy := (hfy rfl).elim
end
```

#### [Chris Hughes (Jul 07 2018 at 19:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/partial functions/near/129265731):
It's clearer what's going on, because in the first method, it's not obvious that hfy will have type `some x ≠ none` or `none ≠ none`, and not `f y ≠ none` in the match expression.

#### [Mario Carneiro (Jul 07 2018 at 20:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/partial functions/near/129266827):
In that last one, `y.2` has the type `f y.1 ≠ none`, so it is important that you write `f y.1` instead of `f (\u y)`

#### [Patrick Massot (Jul 07 2018 at 20:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/partial functions/near/129267274):
What about 
```lean
def option_to_subfunc {α β: Type} (f: α → (option β)) :
  {x : α // option.is_some (f x)} → β | ⟨x, h⟩ := option.get h
```

#### [Chris Hughes (Jul 07 2018 at 20:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/partial functions/near/129267284):
I thought the function probably already existed, but I couldn't find it.

#### [Patrick Massot (Jul 07 2018 at 20:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/partial functions/near/129267287):
`option.is_some` is directly about what you care about instead of its negation

#### [Patrick Massot (Jul 07 2018 at 20:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/partial functions/near/129267327):
I don't know if it already exists

#### [Chris Hughes (Jul 07 2018 at 20:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/partial functions/near/129267409):
I think I saw it before, but I was thrown off by the fact `is_some` is `bool` rather than `Prop`

#### [Patrick Massot (Jul 07 2018 at 20:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/partial functions/near/129267412):
Oh, you mean `is_some` already existed.

#### [Patrick Massot (Jul 07 2018 at 20:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/partial functions/near/129267418):
I thought you were referring to `option_to_subfunc`

#### [Chris Hughes (Jul 07 2018 at 20:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/partial functions/near/129267469):
I was referring to `option_to_subfunc` or things like it, and I saw `option.get` but I didn't like it because `is_some` is `bool`

#### [Victor Porton (Jul 07 2018 at 22:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/partial functions/near/129270457):
@**Patrick Massot** What is this `|`?

#### [Victor Porton (Jul 07 2018 at 22:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/partial functions/near/129270466):
@**Patrick Massot** Oh, it is pattern matching, I got

#### [Victor Porton (Jul 07 2018 at 22:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/partial functions/near/129270785):
weird, I can't find `def option` in Lean library

#### [Victor Porton (Jul 07 2018 at 22:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/partial functions/near/129270788):
got: `inductive option`

#### [Victor Porton (Jul 07 2018 at 22:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/partial functions/near/129270836):
@**Patrick Massot** Where is `option.get` defined?

#### [Victor Porton (Jul 07 2018 at 22:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/partial functions/near/129270857):
found: `basic.lean`

#### [Victor Porton (Jul 07 2018 at 22:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/partial functions/near/129271074):
I also don't understand `(hfy rfl).elim`. Does it contain `hfy` applied to `rfl`? I would be not surprised if `rfl` were applied to an equality, but I see inequality applied to `rfl` what looks for me the "opposite" of what can be done. What is it?

#### [Chris Hughes (Jul 07 2018 at 22:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/partial functions/near/129271212):
`hfy` has type `none ≠ none` which is definitionally equal to `none = none → false`. `rfl` is a proof that `none = none` so `hfy rfl` has type `false`

#### [Victor Porton (Jul 07 2018 at 23:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/partial functions/near/129273495):
How having a function `f` determine its domain?

#### [Kenny Lau (Jul 07 2018 at 23:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/partial functions/near/129273497):
it's in the type of the function

#### [Victor Porton (Jul 07 2018 at 23:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/partial functions/near/129273512):
@**Kenny Lau** So use `match`?

#### [Victor Porton (Jul 07 2018 at 23:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/partial functions/near/129273518):
I have `f: (Σ c:α → Prop, {x:α // c x})` and want to get the `c`

#### [Kenny Lau (Jul 07 2018 at 23:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/partial functions/near/129273519):
I... don't think that's how this works

#### [Victor Porton (Jul 07 2018 at 23:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/partial functions/near/129273563):
What I try is like:
```lean
noncomputable def subfunc_to_option2 {α β: Type} --[decidable_pred c]
(f: (Σ c:α → Prop, {x:α // c x}) → β) : α → option β :=
λ y: α, if h : f.1 y then some (f (subtype.mk y h)) else none
```

#### [Victor Porton (Jul 07 2018 at 23:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/partial functions/near/129273670):
is this possible?

#### [Victor Porton (Jul 08 2018 at 00:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/partial functions/near/129274227):
This does not compile (types of sides equality in `inv1` do not match). How to fix the error?
```lean
local attribute [instance] classical.prop_decidable

-- Switch from a function on a subset to a function to option monad
noncomputable def subfunc_to_option {α β: Type} {c: α → Prop} --[decidable_pred c]
(f: {x:α // c x} → β) : α → option β :=
λ y: α, if h : c y then some (f (subtype.mk y h)) else none

-- Switch from function to option monad to a function on a subset
def option_to_subfunc {α β: Type} (f: α → (option β)) :
  {x : α // option.is_some (f x)} → β | ⟨x, h⟩ := option.get h

theorem inv1 {α β: Type} {c: α → Prop} (f) : option_to_subfunc (@subfunc_to_option α β c f) = f := sorry
```

#### [Chris Hughes (Jul 08 2018 at 00:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/partial functions/near/129274270):
I'm not sure what you're trying to do. I don't think the type of `f` is what you want it to be. You cannot do `f.1` because `f` is not a sigma type.

#### [Victor Porton (Jul 08 2018 at 00:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/partial functions/near/129274320):
@**Chris Hughes** I tried to eliminate `{c: α → Prop}` from my definition. I tried it for completeness, but probably the proper way to do it is using an implicit argument (as in your code) instead

#### [Victor Porton (Jul 08 2018 at 00:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/partial functions/near/129274321):
@**Chris Hughes** Note that the issue in my very last question was different

#### [Victor Porton (Jul 08 2018 at 00:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/partial functions/near/129274440):
Side question: I subscribed to desktop notifications for this chat, but I get no notifications. Will I receive the notifications, if I close the browser window?

#### [Chris Hughes (Jul 08 2018 at 00:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/partial functions/near/129274488):
One way to fix the error is to use `==` instead of `=` which allows you to state equality when the types are different (your types are different, but they should be equal). This can be unwieldy however. Another way would be to prove that they are equal when applied to an argument, something like this
```lean
theorem inv1 {α β: Type} {c: α → Prop} (f: {x:α // c x} → β) [decidable_pred c] : 
∀ y : {x // c x}, option_to_subfunc (@subfunc_to_option α β c _ f) ⟨y.1, sorry⟩ = f y := sorry
```

#### [Victor Porton (Jul 08 2018 at 00:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/partial functions/near/129274550):
@**Chris Hughes** "unwieldy"? What is particularly bad with `==`? the second way (to write `y` explicitly) seems even worse for me.

#### [Victor Porton (Jul 08 2018 at 00:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/partial functions/near/129274878):
Can the following be proved?
```lean
theorem eq_xxx (t: Type) (a b: t) := (a==b -> a=b)
```
(that is if values of the same type are `==` then they are `=`)

#### [Chris Hughes (Jul 08 2018 at 00:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/partial functions/near/129275360):
`eq_of_heq`

#### [Mario Carneiro (Jul 08 2018 at 00:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/partial functions/near/129275452):
@**Victor Porton** You should receive notifications if you are directly addressed, like this

#### [Victor Porton (Jul 08 2018 at 01:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/partial functions/near/129275513):
hm, it looks now I am really stalled to fill the `sorry`ies in my source:
```lean
local attribute [instance] classical.prop_decidable

-- Switch from a function on a subset to a function to option monad
noncomputable def subfunc_to_option {α β: Type} {c: α → Prop} --[decidable_pred c]
(f: {x:α // c x} → β) : α → option β :=
λ y: α, if h : c y then some (f (subtype.mk y h)) else none

-- Switch from function to option monad to a function on a subset
def option_to_subfunc {α β: Type} (f: α → (option β)) :
  {x : α // option.is_some (f x)} → β | ⟨x, h⟩ := option.get h

theorem inv1 {α β: Type} {c: α → Prop} (f) : option_to_subfunc (@subfunc_to_option α β c f) == f := sorry

theorem inv2 {α β: Type} {c: α → Prop} (f): subfunc_to_option (@option_to_subfunc β α f) = f := sorry
```
How to learn to use `==`? Maybe I should read Coq docs on this?

#### [Mario Carneiro (Jul 08 2018 at 01:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/partial functions/near/129275523):
To address the larger goal of the definitions you are making, I think you want to use `roption` (in `data.pfun`) and the isomorphism theorems between `roption` and `option`. A function `A -> roption B` is the same as a partial function (from a subset of `A` to `B`)

#### [Victor Porton (Jul 08 2018 at 15:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/partial functions/near/129299190):
@**Mario Carneiro** First, how `roption` would be better for my purposes than `option`? My project uses classical logic. (However someone suggested me to mark which theorems need axiom of choice explicitly.) Now we have three isomorphic objects (and thus three isomorphisms): a partial function, `A->option B` and `A->roption B`. I do not see how it could be better than my initial idea.

#### [Mario Carneiro (Jul 08 2018 at 19:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/partial functions/near/129307057):
Because a function `A -> roption B` *is* a "subfunc" as you call it. It is literally a pair of a domain and a partial function on that domain

#### [Mario Carneiro (Jul 08 2018 at 19:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/partial functions/near/129307117):
so you can leverage the proofs of isomorphism there to obtain an isomorphism from `A -> option B` to a partial function

#### [Victor Porton (Jul 08 2018 at 19:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/partial functions/near/129307187):
@**Mario Carneiro** Either you don't understand me, or I do not understand you. The "subfunc" by definition is a function on a _subtype_ of `A`. But `A -> roption B` is a function on the type `A`, not on its arbitrary subtype as I want. It may be isomorphic, but they are _not_ the same.

#### [Mario Carneiro (Jul 08 2018 at 19:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/partial functions/near/129307195):
The isomorphism is almost trivial though, unlike the one from option

#### [Mario Carneiro (Jul 08 2018 at 19:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/partial functions/near/129307237):
And furthermore there is already a definition which gives this isomorphism, `as_subtype`

#### [Victor Porton (Jul 08 2018 at 19:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/partial functions/near/129307448):
@**Mario Carneiro** Thanks. As there is undocumented things like `==` which I may need for my Lean-related project, I prefer to lay it aside for an indefinite future. Moreover, I am going to lay aside abstract math research and get busy myself writing a free Python program (for an applied computer science, not abstract mathematics) now

#### [Mario Carneiro (Jul 08 2018 at 19:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/partial functions/near/129307457):
It's not undocumented, but it's a pain to work with

