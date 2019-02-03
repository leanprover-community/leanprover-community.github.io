---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/66756Concurrentlean.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [Concurrent lean](https://leanprover-community.github.io/archive/113488general/66756Concurrentlean.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Mario Carneiro (Mar 28 2018 at 03:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Concurrent%20lean/near/124299642):
<p>I've been thinking about what appropriate concurrency primitives can be used in pure lean. <span class="user-mention" data-user-id="110043">@Gabriel Ebner</span> Do you see any problems with modeling <code>task</code> in lean (being the same as <code>thunk</code>)? It's not clear why this needs to be <code>meta</code>.</p>
<p>Another possible concurrency primitive is <code>fork : thunk A -&gt; thunk B -&gt; A x B</code> which runs the two thunks on separate threads and then returns the results. There is an obvious generalization here to <code>peval : list (thunk A) -&gt; list A</code>, not sure if this is better or worse than <code>join</code> as a primitive. I'm not sure how to simulate these forking strategies with <code>task</code>.</p>

#### [ Mario Carneiro (Mar 28 2018 at 03:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Concurrent%20lean/near/124299700):
<p>I hoped to get inspiration from ML and Haskell, but ML is too declarative (<code>unit</code> functions everywhere) and Haskell has funny problems with laziness turning the evaluation order inside out. <a href="https://www.microsoft.com/en-us/research/wp-content/uploads/2016/02/parallel_haskell2.pdf" target="_blank" title="https://www.microsoft.com/en-us/research/wp-content/uploads/2016/02/parallel_haskell2.pdf">https://www.microsoft.com/en-us/research/wp-content/uploads/2016/02/parallel_haskell2.pdf</a></p>

#### [ Sebastian Ullrich (Mar 28 2018 at 09:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Concurrent%20lean/near/124308889):
<p><code>fork f g = let tf = task.delay t in let tg = task.delay g in (tf.get, tg.get)</code>?</p>

#### [ Gabriel Ebner (Mar 28 2018 at 09:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Concurrent%20lean/near/124308940):
<p><code>task</code> is perfectly sound, and does not need to be meta.  A possible model for <code>task</code> is <code>id</code>, and you should not be able to observe any differences from <code>id</code> in pure Lean code.</p>

#### [ Sebastian Ullrich (Mar 28 2018 at 09:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Concurrent%20lean/near/124308977):
<p>Or less resource-hungry, <code>fork f g = let tf = task.delay f in let y = g () in (tf.get, y)</code></p>

#### [ Mario Carneiro (Mar 28 2018 at 09:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Concurrent%20lean/near/124309039):
<p>Isn't the evaluation semantics off from <code>id</code> though? You need <code>thunk</code> to avoid evaluating the argument too soon</p>

#### [ Gabriel Ebner (Mar 28 2018 at 09:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Concurrent%20lean/near/124309040):
<p>That's why I said <em>pure</em> Lean code. <span class="emoji emoji-1f604" title="smile">:smile:</span></p>

#### [ Gabriel Ebner (Mar 28 2018 at 09:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Concurrent%20lean/near/124309079):
<p>Of course, <code>task</code> hides nontermination and C++ exceptions.</p>

#### [ Sebastian Ullrich (Mar 28 2018 at 09:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Concurrent%20lean/near/124309080):
<p>One missing ingredient right now is <code>task.delay_io : {α : Type u} (f : io α) : io (task α)</code></p>

#### [ Mario Carneiro (Mar 28 2018 at 09:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Concurrent%20lean/near/124309081):
<p>Neither can happen in non-<code>meta</code> code though, right?</p>

#### [ Mario Carneiro (Mar 28 2018 at 09:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Concurrent%20lean/near/124309083):
<p>How is that different from <code>task.delay</code>?</p>

#### [ Gabriel Ebner (Mar 28 2018 at 09:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Concurrent%20lean/near/124309088):
<p>You can have nontermination without meta if you add <code>axiom large_cardinal : 0 = 1</code></p>

#### [ Mario Carneiro (Mar 28 2018 at 09:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Concurrent%20lean/near/124309090):
<p>lol that's quite a large cardinal</p>

#### [ Sebastian Ullrich (Mar 28 2018 at 09:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Concurrent%20lean/near/124309139):
<p>Okay, I think I fixed the signature</p>

#### [ Gabriel Ebner (Mar 28 2018 at 09:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Concurrent%20lean/near/124309140):
<p>Right now, there is also the <em>slight</em> performance problem that we serialize the thunk passed to <code>task.delay</code>, and then deserialize it on the thread where it executes.  From the last public state of the Lean 4 design document, this should be solved in Lean 4.</p>

#### [ Mario Carneiro (Mar 28 2018 at 09:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Concurrent%20lean/near/124309143):
<p>Well, you can break the VM in many ways using <code>large_cardinal</code>, you don't need <code>task</code></p>

#### [ Mario Carneiro (Mar 28 2018 at 09:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Concurrent%20lean/near/124309182):
<p>in fact you should be able to get nontermination even without <code>task</code></p>

#### [ Gabriel Ebner (Mar 28 2018 at 09:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Concurrent%20lean/near/124309183):
<blockquote>
<p>in fact you should be able to get nontermination even without <code>task</code></p>
</blockquote>
<p>New results from your master thesis?</p>

#### [ Mario Carneiro (Mar 28 2018 at 09:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Concurrent%20lean/near/124309188):
<p>No, maybe it's folklore... But you can just evaluate a false proof of well_founded in the VM</p>

#### [ Gabriel Ebner (Mar 28 2018 at 09:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Concurrent%20lean/near/124309192):
<p>Ok, that's essentially the same thing as <code>large_cardinal</code>, or <code>sorry</code>.</p>

#### [ Mario Carneiro (Mar 28 2018 at 09:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Concurrent%20lean/near/124309232):
<p>right, that's my point - from a false axiom you can fake a wf definition to cause nontermination</p>

#### [ Mario Carneiro (Mar 28 2018 at 09:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Concurrent%20lean/near/124309236):
<p>(in the VM, which doesn't do reduction and so doesn't get stuck like <code>#reduce</code> would)</p>

#### [ Mario Carneiro (Mar 28 2018 at 09:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Concurrent%20lean/near/124309281):
<p>What is the behavior of <code>let f := task.delay f in ()</code>?</p>

#### [ Mario Carneiro (Mar 28 2018 at 09:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Concurrent%20lean/near/124309286):
<p>Does it just drop the thread?</p>

#### [ Mario Carneiro (Mar 28 2018 at 09:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Concurrent%20lean/near/124309287):
<p>What if you call <code>task.get</code> twice?</p>

#### [ Gabriel Ebner (Mar 28 2018 at 09:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Concurrent%20lean/near/124309328):
<blockquote>
<p>What is the behavior of <code>let f := task.delay f in ()</code>?</p>
</blockquote>
<p><code>f</code> continues to execute, you can continue printing trace messages, etc., and they will show up.</p>

#### [ Gabriel Ebner (Mar 28 2018 at 09:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Concurrent%20lean/near/124309339):
<blockquote>
<p>What if you call <code>task.get</code> twice?</p>
</blockquote>
<p>The first time you call <code>task.get</code>, it will wait for the task to finish and return the result.  The second time it will return immediately with the result.  The code in the task is only executed once.</p>

#### [ Mario Carneiro (Mar 28 2018 at 09:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Concurrent%20lean/near/124309340):
<p>Ooh, that sounds like memoization</p>

#### [ Mario Carneiro (Mar 28 2018 at 10:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Concurrent%20lean/near/124309383):
<p>Maybe <code>memoized</code> is definable after all...</p>

#### [ Sebastian Ullrich (Mar 28 2018 at 10:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Concurrent%20lean/near/124309384):
<p>It's what <code>thunk</code> should sound like <span class="emoji emoji-1f606" title="laughing">:laughing:</span></p>

#### [ Mario Carneiro (Mar 28 2018 at 10:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Concurrent%20lean/near/124309391):
<p>I think Leo said something about explicitly wanting <code>thunk</code> to not be memoized, although I think it's a poor name if that's the intent</p>

#### [ Gabriel Ebner (Mar 28 2018 at 10:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Concurrent%20lean/near/124309394):
<p>It's like memoization except that the code starts running immediately, and on another thread.  C++ code has the ability to create tasks that do not start immediately though (in fact, that's even the default behavior).</p>

#### [ Sebastian Ullrich (Mar 28 2018 at 10:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Concurrent%20lean/near/124309397):
<p>Btw, we will most probably move those horrible impure <code>init.util</code> functions into <code>io</code></p>

#### [ Mario Carneiro (Mar 28 2018 at 10:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Concurrent%20lean/near/124309438):
<p>You can create delayed tasks with <code>thunk (task A)</code> I guess</p>

#### [ Gabriel Ebner (Mar 28 2018 at 10:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Concurrent%20lean/near/124309440):
<p>This will create a new task every time you evaluate the thunk, probably not what you want.</p>

#### [ Mario Carneiro (Mar 28 2018 at 10:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Concurrent%20lean/near/124309446):
<p>hm... <code>task (task A)</code>? :)</p>

#### [ Gabriel Ebner (Mar 28 2018 at 10:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Concurrent%20lean/near/124309447):
<p>Immediately creates a task on another thread...</p>

#### [ Mario Carneiro (Mar 28 2018 at 10:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Concurrent%20lean/near/124309494):
<p>but I guess if the real work is in the created task that won't be executed until you <code>flatten</code></p>

#### [ Gabriel Ebner (Mar 28 2018 at 10:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Concurrent%20lean/near/124309501):
<p>If you do <code>task.delay (task.delay ())</code>, you first create task A, which immediately begins executing on thread 2.  This task A then creates task B, which again immediately begins executing <code>()</code> on thread 3.</p>

#### [ Mario Carneiro (Mar 28 2018 at 10:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Concurrent%20lean/near/124309545):
<p>Oh, I see...</p>

#### [ Mario Carneiro (Mar 28 2018 at 10:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Concurrent%20lean/near/124309595):
<p><span class="user-mention" data-user-id="110024">@Sebastian Ullrich</span> I really like those non-io functions. As long as they are observationally pure there is no problem</p>

#### [ Gabriel Ebner (Mar 28 2018 at 10:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Concurrent%20lean/near/124309596):
<p>Do you actually use them?</p>

#### [ Sebastian Ullrich (Mar 28 2018 at 10:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Concurrent%20lean/near/124309599):
<p>:)</p>

#### [ Mario Carneiro (Mar 28 2018 at 10:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Concurrent%20lean/near/124309603):
<p>I use <code>timeit</code> and <code>trace</code> all the time</p>

#### [ Sebastian Ullrich (Mar 28 2018 at 10:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Concurrent%20lean/near/124309614):
<p>Hmm, good to know I guess</p>

#### [ Mario Carneiro (Mar 28 2018 at 10:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Concurrent%20lean/near/124309656):
<p>Actually I've never used <code>io</code> in pure code. It seems like a trap</p>

#### [ Gabriel Ebner (Mar 28 2018 at 10:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Concurrent%20lean/near/124309661):
<p>I just realized that you can't even simulate them via <code>unsafe_perform_io</code>, since that is meta.</p>

#### [ Mario Carneiro (Mar 28 2018 at 10:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Concurrent%20lean/near/124309718):
<p>Here's another missing <code>task</code> primitive: Run <code>f g : thunk A</code>, and return the first one that finishes</p>

#### [ Gabriel Ebner (Mar 28 2018 at 10:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Concurrent%20lean/near/124309720):
<p>That's nondeterministic and hence unsupported by design.</p>

#### [ Mario Carneiro (Mar 28 2018 at 10:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Concurrent%20lean/near/124309721):
<p>The obvious problem is that they might not return the same thing, but <code>cached</code> solves that problem handily</p>

#### [ Mario Carneiro (Mar 28 2018 at 10:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Concurrent%20lean/near/124309726):
<p>I think it should probably be renamed <code>nondet</code></p>

#### [ Sebastian Ullrich (Mar 28 2018 at 10:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Concurrent%20lean/near/124309731):
<p>Did you see my beautiful typeclass for lifting these functions in the extended monad PR? Fortunately I found a more general monad class that subsumes it <a href="https://github.com/Kha/lean/commit/974fee78f75c8861477fba9143a49c8e08101b41#diff-f8e23e5e864df768277396e6f07b2809L67" target="_blank" title="https://github.com/Kha/lean/commit/974fee78f75c8861477fba9143a49c8e08101b41#diff-f8e23e5e864df768277396e6f07b2809L67">https://github.com/Kha/lean/commit/974fee78f75c8861477fba9143a49c8e08101b41#diff-f8e23e5e864df768277396e6f07b2809L67</a></p>

#### [ Gabriel Ebner (Mar 28 2018 at 10:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Concurrent%20lean/near/124309774):
<p><span class="user-mention" data-user-id="110024">@Sebastian Ullrich</span> This does not help you if you want to do printf-style debugging in a pure non-monadic function, right?</p>

#### [ Sebastian Ullrich (Mar 28 2018 at 10:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Concurrent%20lean/near/124309824):
<p>Then you don't need any lifting, no? This is still with the current pure definition instead of in <code>io</code>.</p>

#### [ Mario Carneiro (Mar 28 2018 at 10:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Concurrent%20lean/near/124309831):
<p>Is there a <code>@[noinline]</code> or <code>@[volatile]</code> attribute for these functions?</p>

#### [ Gabriel Ebner (Mar 28 2018 at 10:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Concurrent%20lean/near/124309832):
<p>Right.  You proposed the lifting functions as a replacement for the pure ones, that's what I was responding to.</p>

#### [ Mario Carneiro (Mar 28 2018 at 10:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Concurrent%20lean/near/124309927):
<p>Alternatively, you could accept a proof <code>f () = g ()</code> to eliminate the nondeterminism. This is roughly equivalent to the <code>cached</code> approach without boxing up the result</p>

#### [ Mario Carneiro (Mar 28 2018 at 10:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Concurrent%20lean/near/124309932):
<p>(This is not an unreasonable constraint, if it's not true you can just quotient the output type to make it true)</p>

#### [ Sebastian Ullrich (Mar 28 2018 at 10:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Concurrent%20lean/near/124309997):
<p><span class="user-mention" data-user-id="110043">@Gabriel Ebner</span>  No, that was intended for correctly lifting "pure" scoping functions <code>thunk A -&gt; A</code> into <code>thunk (state S A) -&gt; state S A</code>, etc. But the same approach would be used for lifting <code>io A -&gt; io A</code> scoping functions, yes. The good thing is that with the latter, you can't accidentally forget the lift. Which is the main reason why I think the current definitions are pretty evil.</p>

#### [ Gabriel Ebner (Mar 28 2018 at 10:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Concurrent%20lean/near/124310047):
<p>Ah, I see.</p>

#### [ Mario Carneiro (Mar 28 2018 at 10:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Concurrent%20lean/near/124310061):
<p>I think that using scoping functions to build an <code>io</code> computation is certainly bad practice; the trace output should be expected to be nondeterministic</p>

#### [ Mario Carneiro (Mar 28 2018 at 10:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Concurrent%20lean/near/124310125):
<p>what is <code>unrun</code>? That seems a bit paradoxical</p>

#### [ Sebastian Ullrich (Mar 28 2018 at 10:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Concurrent%20lean/near/124310135):
<p><code>unrun</code> has since been removed :)</p>

#### [ Mario Carneiro (Mar 28 2018 at 10:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Concurrent%20lean/near/124310247):
<p>Now that <code>io_interface</code> is gone, is it impossible to non-meta write <code>io</code> programs?</p>

#### [ Sebastian Ullrich (Mar 28 2018 at 10:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Concurrent%20lean/near/124310250):
<p><code>io</code> is non-meta now :)</p>

#### [ Mario Carneiro (Mar 28 2018 at 10:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Concurrent%20lean/near/124310258):
<p>yeah, but not really, it relies on a meta constant that is not actually meta for some reason</p>

#### [ Sebastian Ullrich (Mar 28 2018 at 10:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Concurrent%20lean/near/124310352):
<p>I think the idea was to not force users to annotate all <code>io</code> functions with <code>meta</code>. You can't prove anything about it, but it's still sound. The replacement for <code>io_interface</code> is <code>monad_io</code>.</p>

#### [ Mario Carneiro (Mar 28 2018 at 10:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Concurrent%20lean/near/124310354):
<p>Oh, I guess the idea is you should replace <code>io_core</code> with your own implementation of <code>monad_io_terminal</code> etc</p>

#### [ Mario Carneiro (Mar 28 2018 at 10:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Concurrent%20lean/near/124310417):
<p>How do you know it's sound? Writing an implementation is not trivial, I think</p>

#### [ Mario Carneiro (Mar 28 2018 at 10:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Concurrent%20lean/near/124310420):
<p>in particular there is a constructor that gives unbounded recursion in the monad</p>

#### [ Sebastian Ullrich (Mar 28 2018 at 10:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Concurrent%20lean/near/124310473):
<p>Which should be okay as long as there's no eliminator, no?</p>

#### [ Mario Carneiro (Mar 28 2018 at 10:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Concurrent%20lean/near/124310576):
<p>hm, I guess you can do some kind of coinductive trace thing if you don't want to have it be trivial</p>

#### [ Mario Carneiro (Mar 28 2018 at 10:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Concurrent%20lean/near/124310584):
<p>Oh cool I just noticed we have a random number generator in lean now</p>

#### [ Gabriel Ebner (Mar 28 2018 at 10:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Concurrent%20lean/near/124310627):
<p>For soundness it should be enough to set <code>io_core := λ _ _, unit</code>.</p>

#### [ Mario Carneiro (Mar 28 2018 at 10:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Concurrent%20lean/near/124310643):
<p>is <code>unit</code> a monad in lean?</p>

#### [ Sebastian Ullrich (Mar 28 2018 at 10:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Concurrent%20lean/near/124310683):
<p>It's not even a type constructor...?</p>

#### [ Mario Carneiro (Mar 28 2018 at 10:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Concurrent%20lean/near/124310685):
<p>or I guess <code>λ _, unit</code></p>

#### [ Sebastian Ullrich (Mar 28 2018 at 10:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Concurrent%20lean/near/124310692):
<p>There's also <a href="https://github.com/leanprover/lean/blob/efa9d7e110ff6389e8863551a4882c84dbcf8236/tests/lean/run/rebind_bind.lean" target="_blank" title="https://github.com/leanprover/lean/blob/efa9d7e110ff6389e8863551a4882c84dbcf8236/tests/lean/run/rebind_bind.lean">https://github.com/leanprover/lean/blob/efa9d7e110ff6389e8863551a4882c84dbcf8236/tests/lean/run/rebind_bind.lean</a></p>

#### [ Mario Carneiro (Mar 28 2018 at 10:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Concurrent%20lean/near/124310741):
<p>interesting. You are using <code>do</code> notation with something that's not <code>monad.bind</code>?</p>

#### [ Sebastian Ullrich (Mar 28 2018 at 10:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Concurrent%20lean/near/124310749):
<p>Yep, that's the main purpose of the test</p>

#### [ Kevin Buzzard (Mar 28 2018 at 12:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Concurrent%20lean/near/124313219):
<p><code>mono_monad</code>? Reminds me of <a href="https://www.youtube.com/watch?v=8N_tupPBtWQ" target="_blank" title="https://www.youtube.com/watch?v=8N_tupPBtWQ">https://www.youtube.com/watch?v=8N_tupPBtWQ</a></p>
<div class="youtube-video message_inline_image"><a data-id="8N_tupPBtWQ" href="https://www.youtube.com/watch?v=8N_tupPBtWQ" target="_blank" title="https://www.youtube.com/watch?v=8N_tupPBtWQ"><img src="https://i.ytimg.com/vi/8N_tupPBtWQ/default.jpg"></a></div>

#### [ Mario Carneiro (Mar 30 2018 at 09:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Concurrent%20lean/near/124402303):
<p>Check it out:</p>
<div class="codehilite"><pre><span></span>meta def list.par_map {α β} (f : α → β) (l : list α) : list β :=
let fs := l.map (λ a, task.delay (λ _, f a)) in
fs.map task.get

#eval timeit &quot;&quot; ((list.range&#39; 50000 10).map (λ n, (eratosthenes n).length))
-- 6.87s
#eval timeit &quot;&quot; ((list.range&#39; 50000 10).par_map (λ n, (eratosthenes n).length))
-- 2.78s
</pre></div>

#### [ Mario Carneiro (Mar 30 2018 at 09:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Concurrent%20lean/near/124402344):
<p>too bad it has to be <code>meta</code></p>

#### [ Adam Kurkiewicz (Mar 30 2018 at 14:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Concurrent%20lean/near/124411857):
<p>impressive! What keeps it in <code>meta</code>?</p>


{% endraw %}
