---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/34848notationscoping.html
---

## [general](index.html)
### [notation scoping](34848notationscoping.html)

#### [Sebastian Ullrich (May 28 2018 at 09:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notation scoping/near/127193572):
https://leanprover.zulipchat.com/#narrow/stream/113488-general/subject/local.20notation.20for.20fin.20(n.2B1)/near/127041848
>  This is exactly how lean 2 notation used to work. Why it changed, I don't know, and I'm not clear on whether to expect this to be different in lean 4.
I think that lean 3 notation is not handled very well at all, this is why I avoid all notation overloading in mathlib

Lean 2 used the notion of "metaclasses" to scope notations, coercions, and attributes declared in namespaces. To use them, you had `open` the namespace, either with an explicit list of metaclasses, or with all of them as the default. It was annoying and didn't make any sense for most of the metaclasses - except perhaps for notations and `classical.prop_decidable`. We completely removed metaclasses for Lean 3.
I'm open to proposals for a notation (and macro) scoping system in Lean 4. A survey of designs in other systems would probably be a good first step.

#### [Andrew Ashworth (May 28 2018 at 10:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notation scoping/near/127194432):
Do people like the way Coq does it?

#### [Andrew Ashworth (May 28 2018 at 10:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notation scoping/near/127194473):
for reference:
```quoted
Interpretation scopes
An interpretation scope is a set of notations for terms with their interpretation. Interpretation scopes provide a weak, purely syntactical form of notations overloading: the same notation, for instance the infix symbol + can be used to denote distinct definitions of the additive operator. Depending on which interpretation scopes is currently open, the interpretation is different. Interpretation scopes can include an interpretation for numerals and strings. However, this is only made possible at the Objective Caml level.

See Figure 12.1 for the syntax of notations including the possibility to declare them in a given scope. Here is a typical example which declares the notation for conjunction in the scope type_scope.


Notation “A /\ B” := (and A B) : type_scope.
Note

A notation not defined in a scope is called a lonely notation.

Global interpretation rules for notations
At any time, the interpretation of a notation for term is done within a stack of interpretation scopes and lonely notations. In case a notation has several interpretations, the actual interpretation is the one defined by (or in) the more recently declared (or open) lonely notation (or interpretation scope) which defines this notation. Typically if a given notation is defined in some scope scope but has also an interpretation not assigned to a scope, then, if scope is open before the lonely interpretation is declared, then the lonely interpretation is used (and this is the case even if the interpretation of the notation in scope is given after the lonely interpretation: otherwise said, only the order of lonely interpretations and opening of scopes matters, and not the declaration of interpretations within a scope).

The initial state of Coq declares three interpretation scopes and no lonely notations. These scopes, in opening order, are core_scope, type_scope and nat_scope.
```

#### [Patrick Massot (May 28 2018 at 10:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notation scoping/near/127194784):
I'm a bit confused to see Coq mentioned here. I thought notations were one of the areas where Lean is clearly better than Coq. I can already tell you mathematicians wouldn't be pleased to see `a .+ b` or `%N` everywhere.

#### [Andrew Ashworth (May 28 2018 at 10:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notation scoping/near/127194900):
would be nice since we have leanpkg that there would be some idea of "package-scope". then my notations, type-class instances, &such have precedence when inside my package.

#### [Andrew Ashworth (May 28 2018 at 10:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notation scoping/near/127195085):
```quote
I'm a bit confused to see Coq mentioned here. I thought notations were one of the areas where Lean is clearly better than Coq. I can already tell you mathematicians wouldn't be pleased to see `a .+ b` or `%N` everywhere.
```
It's not quite about `a .+ b`, but more how should lean handle cases where people use notation to mean different things. consider if one person wants `sin^2 x` to be `(sin x)^2`, but another person wants it to mean `sin (sin x)`. They define that notation in their own files and for whatever reason you end up importing both of them.  Which one should win?

#### [Sean Leather (May 28 2018 at 10:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notation scoping/near/127195271):
Or, for another example, about the interpretation of `[n]`: `fin (n+1)` or `list.cons n list.nil`.

#### [Sean Leather (May 28 2018 at 10:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notation scoping/near/127195493):
I'm not intimately familiar with the Coq notation given above, but it sounds complicated and confusing. I would like to see notation and non-notation name scopes be treated similarly and simply by `open`, probably more like of Agda. (But I'm sure my familiarity breeds bias.)

#### [Andrew Ashworth (May 28 2018 at 10:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notation scoping/near/127195725):
i think that would be fine too, but i'd also like restrictions on imported packages polluting the global namespace if that's an approach people like

#### [Sean Leather (May 28 2018 at 10:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notation scoping/near/127195808):
@**Andrew Ashworth** Maybe we're thinking from different sides of the same coin? It sounds you want a given global name-/notation-space with the ability to restrict it. I think I'd rather have an empty-by-default space with the ability to explicitly expand it using `open`.

#### [Sebastian Ullrich (May 28 2018 at 10:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notation scoping/near/127196091):
As a general comment, much of Coq's notation complexity seems to stem from the fact that it does not support notation overloading (i.e. overlapping notation disambiguated at elaboration time). Is that correct?

#### [Sebastian Ullrich (May 28 2018 at 10:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notation scoping/near/127196092):
I don't know what Agda's system is like.

#### [Sean Leather (May 28 2018 at 11:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notation scoping/near/127196345):
There are [Agda syntax declarations](https://agda.readthedocs.io/en/latest/language/syntax-declarations.html), but I was thinking mainly about the power and flexibility of Agda's `open` for modules. Since you can use nearly arbitrary Unicode naming structure (cf. mixfix parsing) in Agda, most of what is notation in Lean are names in Agda. Thus, they are treated by `open` in the same way as ASCII names are.

#### [Sean Leather (May 28 2018 at 11:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notation scoping/near/127196429):
One possibility is to give a `notation` declaration a name and support bringing notation into scope or excluding it from scope via the name.

#### [Sean Leather (May 28 2018 at 11:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notation scoping/near/127196751):
```lean
namespace list
notation square_brackets : `[` l:(foldr `, ` (h t, list.cons h t) list.nil `]`) := l
end list

section list_with_brackets
open list -- brings everything, including notation, into scope
example : list nat := [1, 2, 3]
example : list nat := map nat.succ [1, 2, 3]
end list_with_brackets

section list_without_open
example : list nat := list.cons 1 (list.cons 2 (list.cons 3 list.nil)) -- no brackets in scope
end list_without_open

section list_with_brackets_but_not_whole_namespace
open list (square_brackets) -- brings only notation into scope
example : list nat := [1, 2, 3]
example : list nat := map nat.succ [1, 2, 3] -- error: should be list.map
end list_with_brackets_but_not_whole_namespace
```

#### [Sebastian Ullrich (May 28 2018 at 12:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notation scoping/near/127199647):
> One possibility is to give a notation declaration a name and support bringing notation into scope or excluding it from scope via the name.

I like that. Because we want to translate notations to macros in Lean 4, we have to give them _some_ name anyway.

#### [Sebastian Ullrich (May 28 2018 at 12:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notation scoping/near/127199766):
It's fun to think about what the standard declaration modifiers mean in that case:
* `private` corresponds to `local`
* `protected` is... interesting :smile:  . Something like `persistent local`?
* `export` can be used for Coq's `Global`

#### [Sebastian Ullrich (May 28 2018 at 12:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notation scoping/near/127199785):
And of course `hide` hides any notation, global or not

#### [Mario Carneiro (May 28 2018 at 12:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notation scoping/near/127199792):
I don't understand how to use `hide`

#### [Sebastian Ullrich (May 28 2018 at 12:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notation scoping/near/127199797):
You mean right now?

#### [Mario Carneiro (May 28 2018 at 12:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notation scoping/near/127199805):
when I have overloaded notations it's impossible to specify which to hide

#### [Mario Carneiro (May 28 2018 at 12:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notation scoping/near/127199807):
yes

#### [Sebastian Ullrich (May 28 2018 at 12:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notation scoping/near/127199919):
`hide` currently only works for `open`ed or `export`ed names, I think. Perhaps that could be lifted. For specifying overloaded notations, you'd need to know their macro names. I'm not sure what the autogenerated names would look like, probably similar to `instance`.

#### [Sean Leather (May 28 2018 at 13:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notation scoping/near/127200712):
```quote
Because we want to translate notations to macros in Lean 4, we have to give them _some_ name anyway.
```
Oh, that's good. Can you generalize to make `infixl`/`infixr` a kind of notation and nameable, since it also affects how identifiers are parsed in a given scope?

#### [Sebastian Ullrich (May 28 2018 at 13:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notation scoping/near/127200743):
Sure, they are already implemented via `notation` in Lean 3 anyway

#### [Sean Leather (May 28 2018 at 13:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notation scoping/near/127200794):
Cool! And, while you're at it, point notation? In the same vein as we discussed in the past? :wink:

#### [Sebastian Ullrich (May 28 2018 at 13:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notation scoping/near/127200799):
Uh. Do you have a link? :)

#### [Sean Leather (May 28 2018 at 13:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notation scoping/near/127200806):
The namespace field projection stuff.

#### [Sean Leather (May 28 2018 at 13:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notation scoping/near/127200811):
https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/namespace.20field.20notation

#### [Sean Leather (May 28 2018 at 13:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notation scoping/near/127200862):
Basically, I think you could consider field notation as a special notation that could become more flexible than right now.

#### [Sebastian Ullrich (May 28 2018 at 13:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notation scoping/near/127201356):
I haven't seen a very convincing example for generalizing projection notation outside of the original namespace yet. It may be simple to implement it yourself when the elaborator is implemented in Lean, but currently I'm not anticipating that to happen in the first version of Lean 4. On the other hand, we're definitely planning to rewrite the pretty printer in Lean, so adding dot notation support during that sound good to me.

#### [Sean Leather (May 28 2018 at 13:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notation scoping/near/127201425):
Dot-notation pretty-printing is a good step. But I don't think I'd want everything that could be pretty-printed with that notation to be done in that way. Do you?

#### [Sebastian Ullrich (May 28 2018 at 13:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notation scoping/near/127201875):
No, I think there should be an option with values "none/attributed/all"

#### [Sean Leather (May 28 2018 at 13:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notation scoping/near/127201979):
A global `set_option` option? I was thinking it would be preferable to decide for each identifier. What do each of the values mean?

#### [Sebastian Ullrich (May 28 2018 at 13:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notation scoping/near/127202324):
"none": never pretty-print projection notation
"attributed": use on identifiers attributed with some new attribute
"all": use where possible

#### [Sebastian Ullrich (May 28 2018 at 13:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notation scoping/near/127202410):
So I agree with you that there should be an attribute, but there should also be a quick way to turn it off completely

#### [Sean Leather (May 28 2018 at 13:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notation scoping/near/127202415):
Sure, that sounds reasonable.

