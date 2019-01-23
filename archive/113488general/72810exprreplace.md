---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/72810exprreplace.html
---

## Stream: [general](index.html)
### Topic: [expr.replace](72810exprreplace.html)

---


{% raw %}
#### [ Jakob von Raumer (Mar 19 2018 at 16:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/expr.replace/near/123920774):
Is there a version of expr.replace that performs replacements until a fixed point is reached?

#### [ Mario Carneiro (Mar 19 2018 at 16:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/expr.replace/near/123920832):
I think you need something like `ext_simplify_core` for that kind of fine-grained traversal control

#### [ Mario Carneiro (Mar 19 2018 at 16:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/expr.replace/near/123920891):
If you don't mind that it doesn't actually stop traversal, you can use `option` or other monadic stuff to escape once you find what you wanted

#### [ Mario Carneiro (Mar 19 2018 at 16:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/expr.replace/near/123920898):
Or you could write your own, `expr.replace` is a simple recursive function IFIACT

#### [ Jakob von Raumer (Mar 19 2018 at 16:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/expr.replace/near/123921125):
`ext_simplify_core` is not useful if I really want to modify the expression, right?

#### [ Jakob von Raumer (Mar 19 2018 at 16:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/expr.replace/near/123921150):
Maybe the easiest would just be to calculate how many times I'd have to run `expr.replace`...

#### [ Jakob von Raumer (Mar 19 2018 at 16:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/expr.replace/near/123921405):
To be more explicit: I want to replace all occurences of `(f a b c ...)` where f is a `local_const` by something else, but I struggle with the fact that the `expr.app` with the `f` is the innermost one and not the outermost one...

#### [ Sebastian Ullrich (Mar 19 2018 at 16:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/expr.replace/near/123921494):
Why do you need the number of runs? You're in meta land, so you don't have to worry about proving termination, do you?

#### [ Jakob von Raumer (Mar 19 2018 at 16:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/expr.replace/near/123921509):
True that...

#### [ Jakob von Raumer (Mar 19 2018 at 16:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/expr.replace/near/123921511):
Still have to get used to being that dirty

#### [ Sebastian Ullrich (Mar 19 2018 at 16:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/expr.replace/near/123921551):
:)

#### [ Jakob von Raumer (Mar 19 2018 at 16:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/expr.replace/near/123921723):
But I cannot imagine that there's not a suitable version of `expr.is_app_of` somewhere, such that ``(expr.app (expr.app (expr.const `lt []) (expr.var 1)) (expr.var 0)).is_app_of `lt'``actually evaluates to `tt`...

#### [ Simon Hudon (Mar 19 2018 at 16:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/expr.replace/near/123921731):
@**Sebastian Ullrich** You should be ashamed to corrupt the youth (or user base) like this! Proposing to not think about termination ... Where is the world heading to?

#### [ Sebastian Ullrich (Mar 19 2018 at 16:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/expr.replace/near/123921778):
We'll soon enough introduce a `fuel` type to make the new parser actually implementable in total Lean... :)

#### [ Simon Hudon (Mar 19 2018 at 16:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/expr.replace/near/123921785):
Awesome! How does fuel work?

#### [ Mario Carneiro (Mar 19 2018 at 16:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/expr.replace/near/123921877):
Why isn't it currently implementable?

#### [ Sebastian Ullrich (Mar 19 2018 at 16:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/expr.replace/near/123921882):
It's basically `nat`, but provides an opaque constant that is assumed to be large enough that the code generator can just ignore the type in practice... :)

#### [ Sebastian Ullrich (Mar 19 2018 at 16:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/expr.replace/near/123921929):
So it's just a hint to the code generator

#### [ Mario Carneiro (Mar 19 2018 at 16:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/expr.replace/near/123921930):
Wouldn't it be better to just do a well founded recursion with an omitted proof?

#### [ Jakob von Raumer (Mar 19 2018 at 16:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/expr.replace/near/123921936):
```quote
But I cannot imagine that there's not a suitable version of `expr.is_app_of` somewhere, such that ``(expr.app (expr.app (expr.const `lt []) (expr.var 1)) (expr.var 0)).is_app_of `lt'``actually evaluates to `tt`...
```
God damn it, there's a `'` in the end of that line...

#### [ Moses Schönfinkel (Mar 19 2018 at 16:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/expr.replace/near/123921946):
But you can prove so easily that `fuel` is nicely structurally decreasing! :P

#### [ Mario Carneiro (Mar 19 2018 at 16:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/expr.replace/near/123921958):
The point is it's a lie though

#### [ Mario Carneiro (Mar 19 2018 at 16:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/expr.replace/near/123921968):
the real `fuel` is infinity, which is not well founded, I think we should be honest about that

#### [ Moses Schönfinkel (Mar 19 2018 at 16:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/expr.replace/near/123922021):
I admit nothing, deny everything. It proofchecks, surely it must be correct ;).

#### [ Moses Schönfinkel (Mar 19 2018 at 16:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/expr.replace/near/123922031):
(It's a minor detail that it doesn't model whatever it is I had set out to do.)

#### [ Mario Carneiro (Mar 19 2018 at 16:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/expr.replace/near/123922034):
Alternatively, the VM could support some coinductive type

#### [ Sebastian Ullrich (Mar 19 2018 at 16:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/expr.replace/near/123922044):
@**Mario Carneiro** What does omitted mean, `sorry`? Things like macro expansion will be _provably_ non-wellfounded, as long as we don't restrict the user input.

#### [ Mario Carneiro (Mar 19 2018 at 16:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/expr.replace/near/123922045):
`undefined` actually, but yes

#### [ Mario Carneiro (Mar 19 2018 at 16:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/expr.replace/near/123922095):
I would rather have a sign that says "this is false, but that won't stop me" than a shell game that is false but not obviously so

#### [ Sebastian Ullrich (Mar 19 2018 at 16:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/expr.replace/near/123922097):
We want non-meta definitions to prove partial correctness of them. There is no need for `fuel` in meta.

#### [ Mario Carneiro (Mar 19 2018 at 16:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/expr.replace/near/123922154):
Why not use coinductive types? That's what they are for

#### [ Mario Carneiro (Mar 19 2018 at 16:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/expr.replace/near/123922173):
I don't mean supporting some `coinductive` command mind you, just some specific useful/relevant coinductive type, like mathlib `computation`

#### [ Mario Carneiro (Mar 19 2018 at 16:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/expr.replace/near/123922177):
which is basically "programming with fuel"

#### [ Mario Carneiro (Mar 19 2018 at 17:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/expr.replace/near/123922326):
The problem is that models of coinductive types in CIC are not computationally efficient (i.e. stream as a nat -> A instead of B -> A x B), so they need to be VM reimplemented

#### [ Sebastian Ullrich (Mar 19 2018 at 17:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/expr.replace/near/123922492):
Yeah, I'm not looking forward to that.

#### [ Sebastian Ullrich (Mar 19 2018 at 17:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/expr.replace/near/123923027):
I agree that `computation` may be a more satisfying design (it shouldn't matter for the proofs), but any trampolining will be bad for performance

#### [ Mario Carneiro (Mar 19 2018 at 17:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/expr.replace/near/123923222):
Trampolining how? B  -> A x B is exactly the same as the state monad, and it didn't seem to be a big problem there; I assumed the plan was to optimize the trampoline away once lean compilation gets good

#### [ Mario Carneiro (Mar 19 2018 at 17:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/expr.replace/near/123923312):
Speaking of which, this requires a trivial amount of VM support - "call Y instead of X", and it would solve a huge number of problems if an API for that was exposed

#### [ Mario Carneiro (Mar 19 2018 at 17:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/expr.replace/near/123923485):
Other applications include "VM identity functions", where some nontrivial lean function is the identity in VM representation, while executing it as written will have much worse performance (for example, `list.attach` is O(n) but is a VM identity function)

#### [ Sebastian Ullrich (Mar 19 2018 at 17:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/expr.replace/near/123923549):
It sounds like we would have to specialize the trampoline driver to the specific functional, but I don't expect specialization any time soon

#### [ Sebastian Ullrich (Mar 19 2018 at 17:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/expr.replace/near/123923826):
"call Y instead of X" sounds like trouble if the types of Y and X have different runtime representations like in your first example...?

#### [ Simon Hudon (Mar 19 2018 at 18:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/expr.replace/near/123926097):
I like Mario's thinking. Using `computation` instead of the `fuel` trick has the added benefit that, if you call one of those functions in code where precise knowledge about termination matters, the type tells you exactly what to expect. And a computation + proof of termination gives you a properly well-founded Lean value

#### [ Simon Hudon (Mar 19 2018 at 18:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/expr.replace/near/123926161):
An example where I have seen that separation to be productive is when the proof of termination depends on the shape of a pointer structure

#### [ Simon Hudon (Mar 19 2018 at 18:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/expr.replace/near/123926401):
If that's useful, I have a Lean port of Chlipala general recursion machinery.

#### [ Sebastian Ullrich (Mar 20 2018 at 10:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/expr.replace/near/123955936):
Chlipala appears to list some strong limitations for both of his coinductive definitions

#### [ Mario Carneiro (Mar 20 2018 at 13:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/expr.replace/near/123960430):
> "call Y instead of X" sounds like trouble if the types of Y and X have different runtime representations like in your first example...?

It's okay as long as it's a complete type replacement, i.e., all the functions that access the type are replaced with modified versions. For example, we could VM-replace `nat.add` with`num.add`, and also all the other nat functions, if we wanted to have a lean-based fast nat implementation. Similarly, you could use this to support the quotient encoding: you don't VM-replace `quot A` by `A` because it's a type so it won't be called anyway, but you replace all the `quot` functions with identity functions.

If we ever get the ability to write system F functions for direct use by the VM (although this is a whole separate feature), it would also be useful to use VM replacement here, in case a certain function can't be well-typed in lean but is valid system F.

#### [ Mario Carneiro (Mar 20 2018 at 13:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/expr.replace/near/123961117):
> It sounds like we would have to specialize the trampoline driver to the specific functional, but I don't expect specialization any time soon

Thinking more about how this would actually work with `computation`, we have `computation.run` which calls the corecursor (which has type B -> A + B after VM-replacement), returns A if success, and otherwise calls itself with the new value of B. This function is the "trampoline" in your scenario. On the other side, the coinductive type is being represented by the corecursor itself, so the user wrote this function B -> A + B. You would have to call the B part whenever you need to use some fuel, and otherwise return the output or continue some other well-founded recursion etc.

Part of the problem with programming this way is that B must contain the entire state of the program, everything that changes during the recursion, and it's usually unpleasant to have to explicitly enumerate all this data - this is what the compiler should be doing for you. One really nice way to handle this would be to have a compiler from unbounded recursive definitions to `computation`, or even simpler, a `computation.fix` operator which allows you to write such functions directly. (Apparently there is no computation.fix defined, but it isn't hard to define, with type `(A -> computation A) -> computation A`.)

#### [ Mario Carneiro (Mar 20 2018 at 13:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/expr.replace/near/123961241):
With this latter approach, you could just call `fix f` instead of `computation.run (computation.fix (ret o f))` on the VM side and thus avoid most of the trampolining. There would still be `fix(f) { return f(fix(f)); }` which I guess can be inlined(?) but otherwise seems difficult to improve on

#### [ Sebastian Ullrich (Mar 20 2018 at 13:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/expr.replace/near/123961675):
> It's okay as long as it's a complete type replacement

I see, yes. We're planning to allow `private` fields in structures to hide implementation details like `string`, which could be used here as well

#### [ Sebastian Ullrich (Mar 20 2018 at 14:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/expr.replace/near/123962943):
> One really nice way to handle this would be to have a compiler from unbounded recursive definitions to computation

This would be a nice feature for a future equation compiler defined in Lean. With `fix`, you still have to pack multiple arguments into tuples. Though that could also happen automatically when lifting `computation` through `state_t`.

#### [ Simon Hudon (Mar 20 2018 at 15:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/expr.replace/near/123966262):
I can see a lot of use for a new generation of equation compilers (including some for corecursive functions). For computation specifically, it would be nice if it worked on the basis of a type class. If your return type is a monad that supports unbounded recursion, then its amenable to the treatment of the new equation compiler.

#### [ Sebastian Ullrich (Mar 20 2018 at 15:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/expr.replace/near/123966322):
I will be very happy if all of this works out some day :)

#### [ Sebastian Ullrich (Mar 20 2018 at 15:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/expr.replace/near/123966324):
Still not sure I should use it in the parser :smile:

#### [ Mario Carneiro (Mar 20 2018 at 16:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/expr.replace/near/123967244):
Why not put a limitation on how many nested macros to unfold? Seems like that would be undesirable anyway

#### [ Sebastian Ullrich (Mar 20 2018 at 16:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/expr.replace/near/123967451):
Yes, that's what it currently looks like. There may be better examples, like parsing routines where we don't want to prove wellfoundedness without the tactic framework.

#### [ Simon Hudon (Mar 20 2018 at 16:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/expr.replace/near/123967582):
That is also a problem with unbounded recursion: you need to prove that your functions are monotonic. The tactic framework is useful for that. Maybe we can do it with type classes too though

#### [ Mario Carneiro (Mar 20 2018 at 16:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/expr.replace/near/123967885):
This is part of the reason I want to avoid the `fuel` approach - the functions of interest are not all functions, but functions that have some monotonicity conditions as `fuel` changes, and you have to prove this for all functions you define, even though the proof is always straightforward.

#### [ Simon Hudon (Mar 20 2018 at 16:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/expr.replace/near/123968026):
But I have found the `(H : monotonic f . prove_monotonicity)` notation to be pretty useful to make that invisible

#### [ Simon Hudon (Mar 20 2018 at 16:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/expr.replace/near/123968031):
(in the parameters of `fix` for instance

#### [ Mario Carneiro (Mar 20 2018 at 16:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/expr.replace/near/123968052):
Not sure how much of this is available in the parser stuff though (maybe bootstrapping will help here)

#### [ Chris Hughes (Dec 04 2018 at 03:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/expr.replace/near/150819592):
What does expr.replace do?

#### [ Keeley Hoek (Dec 05 2018 at 18:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/expr.replace/near/150943939):
So because of `expr.app` and other such things an `expr` is a big tree of little-er `expr`s. You can get lean to map over an `expr` in this way with a function which can decide to replace subexpressions or not (the function decides to either a) replace this with something I provide or b) don't replace and descend into it instead). The `nat` argument tells you how deep in the binders you are, so you can correctly emit `expr.var`s.

#### [ Chris Hughes (Dec 05 2018 at 18:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/expr.replace/near/150944046):
Thanks. Sounds like what I wanted.

#### [ Edward Ayers (Dec 05 2018 at 18:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/expr.replace/near/150944777):
added docstring to `https://github.com/EdAyers/lean`

#### [ Chris Hughes (Dec 22 2018 at 07:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/expr.replace/near/152378457):
Struggling to use `expr.replace` slightly. I want to use `infer_type` to fill in the `(expr → ℕ → option expr)` argument, but this returns a `tactic expr` not an `expr` or `option expr`. Is there any way around this?

#### [ Kenny Lau (Dec 22 2018 at 07:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/expr.replace/near/152378832):
so just extract the `expr`?

#### [ Kenny Lau (Dec 22 2018 at 07:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/expr.replace/near/152378834):
`t <- infer_type u`

#### [ Mario Carneiro (Dec 22 2018 at 07:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/expr.replace/near/152378882):
no way around it, I'm afraid. `infer_type` wouldn't even work because it's looking at open terms

#### [ Mario Carneiro (Dec 22 2018 at 07:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/expr.replace/near/152378890):
you have to explicitly traverse the term and `instantiate_local` to go through binders

#### [ Mario Carneiro (Dec 22 2018 at 07:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/expr.replace/near/152378892):
`tactic.hide` is an example

#### [ Chris Hughes (Dec 22 2018 at 08:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/expr.replace/near/152379188):
Okay thanks.


{% endraw %}
