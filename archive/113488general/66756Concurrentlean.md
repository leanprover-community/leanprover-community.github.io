---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/66756Concurrentlean.html
---

## Stream: [general](index.html)
### Topic: [Concurrent lean](66756Concurrentlean.html)

---


{% raw %}
#### [ Mario Carneiro (Mar 28 2018 at 03:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Concurrent%20lean/near/124299642):
I've been thinking about what appropriate concurrency primitives can be used in pure lean. @**Gabriel Ebner** Do you see any problems with modeling `task` in lean (being the same as `thunk`)? It's not clear why this needs to be `meta`.

Another possible concurrency primitive is `fork : thunk A -> thunk B -> A x B` which runs the two thunks on separate threads and then returns the results. There is an obvious generalization here to `peval : list (thunk A) -> list A`, not sure if this is better or worse than `join` as a primitive. I'm not sure how to simulate these forking strategies with `task`.

#### [ Mario Carneiro (Mar 28 2018 at 03:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Concurrent%20lean/near/124299700):
I hoped to get inspiration from ML and Haskell, but ML is too declarative (`unit` functions everywhere) and Haskell has funny problems with laziness turning the evaluation order inside out. https://www.microsoft.com/en-us/research/wp-content/uploads/2016/02/parallel_haskell2.pdf

#### [ Sebastian Ullrich (Mar 28 2018 at 09:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Concurrent%20lean/near/124308889):
`fork f g = let tf = task.delay t in let tg = task.delay g in (tf.get, tg.get)`?

#### [ Gabriel Ebner (Mar 28 2018 at 09:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Concurrent%20lean/near/124308940):
`task` is perfectly sound, and does not need to be meta.  A possible model for `task` is `id`, and you should not be able to observe any differences from `id` in pure Lean code.

#### [ Sebastian Ullrich (Mar 28 2018 at 09:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Concurrent%20lean/near/124308977):
Or less resource-hungry, `fork f g = let tf = task.delay f in let y = g () in (tf.get, y)`

#### [ Mario Carneiro (Mar 28 2018 at 09:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Concurrent%20lean/near/124309039):
Isn't the evaluation semantics off from `id` though? You need `thunk` to avoid evaluating the argument too soon

#### [ Gabriel Ebner (Mar 28 2018 at 09:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Concurrent%20lean/near/124309040):
That's why I said *pure* Lean code. :smile:

#### [ Gabriel Ebner (Mar 28 2018 at 09:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Concurrent%20lean/near/124309079):
Of course, `task` hides nontermination and C++ exceptions.

#### [ Sebastian Ullrich (Mar 28 2018 at 09:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Concurrent%20lean/near/124309080):
One missing ingredient right now is `task.delay_io : {α : Type u} (f : io α) : io (task α)`

#### [ Mario Carneiro (Mar 28 2018 at 09:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Concurrent%20lean/near/124309081):
Neither can happen in non-`meta` code though, right?

#### [ Mario Carneiro (Mar 28 2018 at 09:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Concurrent%20lean/near/124309083):
How is that different from `task.delay`?

#### [ Gabriel Ebner (Mar 28 2018 at 09:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Concurrent%20lean/near/124309088):
You can have nontermination without meta if you add `axiom large_cardinal : 0 = 1`

#### [ Mario Carneiro (Mar 28 2018 at 09:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Concurrent%20lean/near/124309090):
lol that's quite a large cardinal

#### [ Sebastian Ullrich (Mar 28 2018 at 09:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Concurrent%20lean/near/124309139):
Okay, I think I fixed the signature

#### [ Gabriel Ebner (Mar 28 2018 at 09:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Concurrent%20lean/near/124309140):
Right now, there is also the *slight* performance problem that we serialize the thunk passed to `task.delay`, and then deserialize it on the thread where it executes.  From the last public state of the Lean 4 design document, this should be solved in Lean 4.

#### [ Mario Carneiro (Mar 28 2018 at 09:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Concurrent%20lean/near/124309143):
Well, you can break the VM in many ways using `large_cardinal`, you don't need `task`

#### [ Mario Carneiro (Mar 28 2018 at 09:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Concurrent%20lean/near/124309182):
in fact you should be able to get nontermination even without `task`

#### [ Gabriel Ebner (Mar 28 2018 at 09:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Concurrent%20lean/near/124309183):
```quote
in fact you should be able to get nontermination even without `task`
```
New results from your master thesis?

#### [ Mario Carneiro (Mar 28 2018 at 09:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Concurrent%20lean/near/124309188):
No, maybe it's folklore... But you can just evaluate a false proof of well_founded in the VM

#### [ Gabriel Ebner (Mar 28 2018 at 09:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Concurrent%20lean/near/124309192):
Ok, that's essentially the same thing as `large_cardinal`, or `sorry`.

#### [ Mario Carneiro (Mar 28 2018 at 09:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Concurrent%20lean/near/124309232):
right, that's my point - from a false axiom you can fake a wf definition to cause nontermination

#### [ Mario Carneiro (Mar 28 2018 at 09:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Concurrent%20lean/near/124309236):
(in the VM, which doesn't do reduction and so doesn't get stuck like `#reduce` would)

#### [ Mario Carneiro (Mar 28 2018 at 09:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Concurrent%20lean/near/124309281):
What is the behavior of `let f := task.delay f in ()`?

#### [ Mario Carneiro (Mar 28 2018 at 09:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Concurrent%20lean/near/124309286):
Does it just drop the thread?

#### [ Mario Carneiro (Mar 28 2018 at 09:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Concurrent%20lean/near/124309287):
What if you call `task.get` twice?

#### [ Gabriel Ebner (Mar 28 2018 at 09:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Concurrent%20lean/near/124309328):
```quote
What is the behavior of `let f := task.delay f in ()`?
```
`f` continues to execute, you can continue printing trace messages, etc., and they will show up.

#### [ Gabriel Ebner (Mar 28 2018 at 09:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Concurrent%20lean/near/124309339):
```quote
What if you call `task.get` twice?
```
The first time you call `task.get`, it will wait for the task to finish and return the result.  The second time it will return immediately with the result.  The code in the task is only executed once.

#### [ Mario Carneiro (Mar 28 2018 at 09:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Concurrent%20lean/near/124309340):
Ooh, that sounds like memoization

#### [ Mario Carneiro (Mar 28 2018 at 10:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Concurrent%20lean/near/124309383):
Maybe `memoized` is definable after all...

#### [ Sebastian Ullrich (Mar 28 2018 at 10:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Concurrent%20lean/near/124309384):
It's what `thunk` should sound like :laughing:

#### [ Mario Carneiro (Mar 28 2018 at 10:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Concurrent%20lean/near/124309391):
I think Leo said something about explicitly wanting `thunk` to not be memoized, although I think it's a poor name if that's the intent

#### [ Gabriel Ebner (Mar 28 2018 at 10:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Concurrent%20lean/near/124309394):
It's like memoization except that the code starts running immediately, and on another thread.  C++ code has the ability to create tasks that do not start immediately though (in fact, that's even the default behavior).

#### [ Sebastian Ullrich (Mar 28 2018 at 10:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Concurrent%20lean/near/124309397):
Btw, we will most probably move those horrible impure `init.util` functions into `io`

#### [ Mario Carneiro (Mar 28 2018 at 10:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Concurrent%20lean/near/124309438):
You can create delayed tasks with `thunk (task A)` I guess

#### [ Gabriel Ebner (Mar 28 2018 at 10:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Concurrent%20lean/near/124309440):
This will create a new task every time you evaluate the thunk, probably not what you want.

#### [ Mario Carneiro (Mar 28 2018 at 10:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Concurrent%20lean/near/124309446):
hm... `task (task A)`? :)

#### [ Gabriel Ebner (Mar 28 2018 at 10:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Concurrent%20lean/near/124309447):
Immediately creates a task on another thread...

#### [ Mario Carneiro (Mar 28 2018 at 10:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Concurrent%20lean/near/124309494):
but I guess if the real work is in the created task that won't be executed until you `flatten`

#### [ Gabriel Ebner (Mar 28 2018 at 10:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Concurrent%20lean/near/124309501):
If you do `task.delay (task.delay ())`, you first create task A, which immediately begins executing on thread 2.  This task A then creates task B, which again immediately begins executing `()` on thread 3.

#### [ Mario Carneiro (Mar 28 2018 at 10:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Concurrent%20lean/near/124309545):
Oh, I see...

#### [ Mario Carneiro (Mar 28 2018 at 10:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Concurrent%20lean/near/124309595):
@**Sebastian Ullrich** I really like those non-io functions. As long as they are observationally pure there is no problem

#### [ Gabriel Ebner (Mar 28 2018 at 10:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Concurrent%20lean/near/124309596):
Do you actually use them?

#### [ Sebastian Ullrich (Mar 28 2018 at 10:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Concurrent%20lean/near/124309599):
:)

#### [ Mario Carneiro (Mar 28 2018 at 10:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Concurrent%20lean/near/124309603):
I use `timeit` and `trace` all the time

#### [ Sebastian Ullrich (Mar 28 2018 at 10:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Concurrent%20lean/near/124309614):
Hmm, good to know I guess

#### [ Mario Carneiro (Mar 28 2018 at 10:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Concurrent%20lean/near/124309656):
Actually I've never used `io` in pure code. It seems like a trap

#### [ Gabriel Ebner (Mar 28 2018 at 10:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Concurrent%20lean/near/124309661):
I just realized that you can't even simulate them via `unsafe_perform_io`, since that is meta.

#### [ Mario Carneiro (Mar 28 2018 at 10:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Concurrent%20lean/near/124309718):
Here's another missing `task` primitive: Run `f g : thunk A`, and return the first one that finishes

#### [ Gabriel Ebner (Mar 28 2018 at 10:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Concurrent%20lean/near/124309720):
That's nondeterministic and hence unsupported by design.

#### [ Mario Carneiro (Mar 28 2018 at 10:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Concurrent%20lean/near/124309721):
The obvious problem is that they might not return the same thing, but `cached` solves that problem handily

#### [ Mario Carneiro (Mar 28 2018 at 10:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Concurrent%20lean/near/124309726):
I think it should probably be renamed `nondet`

#### [ Sebastian Ullrich (Mar 28 2018 at 10:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Concurrent%20lean/near/124309731):
Did you see my beautiful typeclass for lifting these functions in the extended monad PR? Fortunately I found a more general monad class that subsumes it https://github.com/Kha/lean/commit/974fee78f75c8861477fba9143a49c8e08101b41#diff-f8e23e5e864df768277396e6f07b2809L67

#### [ Gabriel Ebner (Mar 28 2018 at 10:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Concurrent%20lean/near/124309774):
@**Sebastian Ullrich** This does not help you if you want to do printf-style debugging in a pure non-monadic function, right?

#### [ Sebastian Ullrich (Mar 28 2018 at 10:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Concurrent%20lean/near/124309824):
Then you don't need any lifting, no? This is still with the current pure definition instead of in `io`.

#### [ Mario Carneiro (Mar 28 2018 at 10:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Concurrent%20lean/near/124309831):
Is there a `@[noinline]` or `@[volatile]` attribute for these functions?

#### [ Gabriel Ebner (Mar 28 2018 at 10:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Concurrent%20lean/near/124309832):
Right.  You proposed the lifting functions as a replacement for the pure ones, that's what I was responding to.

#### [ Mario Carneiro (Mar 28 2018 at 10:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Concurrent%20lean/near/124309927):
Alternatively, you could accept a proof `f () = g ()` to eliminate the nondeterminism. This is roughly equivalent to the `cached` approach without boxing up the result

#### [ Mario Carneiro (Mar 28 2018 at 10:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Concurrent%20lean/near/124309932):
(This is not an unreasonable constraint, if it's not true you can just quotient the output type to make it true)

#### [ Sebastian Ullrich (Mar 28 2018 at 10:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Concurrent%20lean/near/124309997):
@**Gabriel Ebner**  No, that was intended for correctly lifting "pure" scoping functions `thunk A -> A` into `thunk (state S A) -> state S A`, etc. But the same approach would be used for lifting `io A -> io A` scoping functions, yes. The good thing is that with the latter, you can't accidentally forget the lift. Which is the main reason why I think the current definitions are pretty evil.

#### [ Gabriel Ebner (Mar 28 2018 at 10:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Concurrent%20lean/near/124310047):
Ah, I see.

#### [ Mario Carneiro (Mar 28 2018 at 10:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Concurrent%20lean/near/124310061):
I think that using scoping functions to build an `io` computation is certainly bad practice; the trace output should be expected to be nondeterministic

#### [ Mario Carneiro (Mar 28 2018 at 10:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Concurrent%20lean/near/124310125):
what is `unrun`? That seems a bit paradoxical

#### [ Sebastian Ullrich (Mar 28 2018 at 10:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Concurrent%20lean/near/124310135):
`unrun` has since been removed :)

#### [ Mario Carneiro (Mar 28 2018 at 10:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Concurrent%20lean/near/124310247):
Now that `io_interface` is gone, is it impossible to non-meta write `io` programs?

#### [ Sebastian Ullrich (Mar 28 2018 at 10:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Concurrent%20lean/near/124310250):
`io` is non-meta now :)

#### [ Mario Carneiro (Mar 28 2018 at 10:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Concurrent%20lean/near/124310258):
yeah, but not really, it relies on a meta constant that is not actually meta for some reason

#### [ Sebastian Ullrich (Mar 28 2018 at 10:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Concurrent%20lean/near/124310352):
I think the idea was to not force users to annotate all `io` functions with `meta`. You can't prove anything about it, but it's still sound. The replacement for `io_interface` is `monad_io`.

#### [ Mario Carneiro (Mar 28 2018 at 10:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Concurrent%20lean/near/124310354):
Oh, I guess the idea is you should replace `io_core` with your own implementation of `monad_io_terminal` etc

#### [ Mario Carneiro (Mar 28 2018 at 10:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Concurrent%20lean/near/124310417):
How do you know it's sound? Writing an implementation is not trivial, I think

#### [ Mario Carneiro (Mar 28 2018 at 10:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Concurrent%20lean/near/124310420):
in particular there is a constructor that gives unbounded recursion in the monad

#### [ Sebastian Ullrich (Mar 28 2018 at 10:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Concurrent%20lean/near/124310473):
Which should be okay as long as there's no eliminator, no?

#### [ Mario Carneiro (Mar 28 2018 at 10:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Concurrent%20lean/near/124310576):
hm, I guess you can do some kind of coinductive trace thing if you don't want to have it be trivial

#### [ Mario Carneiro (Mar 28 2018 at 10:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Concurrent%20lean/near/124310584):
Oh cool I just noticed we have a random number generator in lean now

#### [ Gabriel Ebner (Mar 28 2018 at 10:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Concurrent%20lean/near/124310627):
For soundness it should be enough to set `io_core := λ _ _, unit`.

#### [ Mario Carneiro (Mar 28 2018 at 10:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Concurrent%20lean/near/124310643):
is `unit` a monad in lean?

#### [ Sebastian Ullrich (Mar 28 2018 at 10:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Concurrent%20lean/near/124310683):
It's not even a type constructor...?

#### [ Mario Carneiro (Mar 28 2018 at 10:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Concurrent%20lean/near/124310685):
or I guess `λ _, unit`

#### [ Sebastian Ullrich (Mar 28 2018 at 10:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Concurrent%20lean/near/124310692):
There's also https://github.com/leanprover/lean/blob/efa9d7e110ff6389e8863551a4882c84dbcf8236/tests/lean/run/rebind_bind.lean

#### [ Mario Carneiro (Mar 28 2018 at 10:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Concurrent%20lean/near/124310741):
interesting. You are using `do` notation with something that's not `monad.bind`?

#### [ Sebastian Ullrich (Mar 28 2018 at 10:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Concurrent%20lean/near/124310749):
Yep, that's the main purpose of the test

#### [ Kevin Buzzard (Mar 28 2018 at 12:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Concurrent%20lean/near/124313219):
`mono_monad`? Reminds me of https://www.youtube.com/watch?v=8N_tupPBtWQ

#### [ Mario Carneiro (Mar 30 2018 at 09:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Concurrent%20lean/near/124402303):
Check it out:
```
meta def list.par_map {α β} (f : α → β) (l : list α) : list β :=
let fs := l.map (λ a, task.delay (λ _, f a)) in
fs.map task.get

#eval timeit "" ((list.range' 50000 10).map (λ n, (eratosthenes n).length))
-- 6.87s
#eval timeit "" ((list.range' 50000 10).par_map (λ n, (eratosthenes n).length))
-- 2.78s
```

#### [ Mario Carneiro (Mar 30 2018 at 09:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Concurrent%20lean/near/124402344):
too bad it has to be `meta`

#### [ Adam Kurkiewicz (Mar 30 2018 at 14:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Concurrent%20lean/near/124411857):
impressive! What keeps it in `meta`?


{% endraw %}
