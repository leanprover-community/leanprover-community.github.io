---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/72810exprreplace.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [expr.replace](https://leanprover-community.github.io/archive/113488general/72810exprreplace.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Jakob von Raumer (Mar 19 2018 at 16:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/expr.replace/near/123920774):
<p>Is there a version of expr.replace that performs replacements until a fixed point is reached?</p>

#### [ Mario Carneiro (Mar 19 2018 at 16:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/expr.replace/near/123920832):
<p>I think you need something like <code>ext_simplify_core</code> for that kind of fine-grained traversal control</p>

#### [ Mario Carneiro (Mar 19 2018 at 16:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/expr.replace/near/123920891):
<p>If you don't mind that it doesn't actually stop traversal, you can use <code>option</code> or other monadic stuff to escape once you find what you wanted</p>

#### [ Mario Carneiro (Mar 19 2018 at 16:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/expr.replace/near/123920898):
<p>Or you could write your own, <code>expr.replace</code> is a simple recursive function IFIACT</p>

#### [ Jakob von Raumer (Mar 19 2018 at 16:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/expr.replace/near/123921125):
<p><code>ext_simplify_core</code> is not useful if I really want to modify the expression, right?</p>

#### [ Jakob von Raumer (Mar 19 2018 at 16:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/expr.replace/near/123921150):
<p>Maybe the easiest would just be to calculate how many times I'd have to run <code>expr.replace</code>...</p>

#### [ Jakob von Raumer (Mar 19 2018 at 16:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/expr.replace/near/123921405):
<p>To be more explicit: I want to replace all occurences of <code>(f a b c ...)</code> where f is a <code>local_const</code> by something else, but I struggle with the fact that the <code>expr.app</code> with the <code>f</code> is the innermost one and not the outermost one...</p>

#### [ Sebastian Ullrich (Mar 19 2018 at 16:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/expr.replace/near/123921494):
<p>Why do you need the number of runs? You're in meta land, so you don't have to worry about proving termination, do you?</p>

#### [ Jakob von Raumer (Mar 19 2018 at 16:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/expr.replace/near/123921509):
<p>True that...</p>

#### [ Jakob von Raumer (Mar 19 2018 at 16:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/expr.replace/near/123921511):
<p>Still have to get used to being that dirty</p>

#### [ Sebastian Ullrich (Mar 19 2018 at 16:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/expr.replace/near/123921551):
<p>:)</p>

#### [ Jakob von Raumer (Mar 19 2018 at 16:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/expr.replace/near/123921723):
<p>But I cannot imagine that there's not a suitable version of <code>expr.is_app_of</code> somewhere, such that <code>(expr.app (expr.app (expr.const `lt []) (expr.var 1)) (expr.var 0)).is_app_of `lt'</code>actually evaluates to <code>tt</code>...</p>

#### [ Simon Hudon (Mar 19 2018 at 16:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/expr.replace/near/123921731):
<p><span class="user-mention" data-user-id="110024">@Sebastian Ullrich</span> You should be ashamed to corrupt the youth (or user base) like this! Proposing to not think about termination ... Where is the world heading to?</p>

#### [ Sebastian Ullrich (Mar 19 2018 at 16:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/expr.replace/near/123921778):
<p>We'll soon enough introduce a <code>fuel</code> type to make the new parser actually implementable in total Lean... :)</p>

#### [ Simon Hudon (Mar 19 2018 at 16:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/expr.replace/near/123921785):
<p>Awesome! How does fuel work?</p>

#### [ Mario Carneiro (Mar 19 2018 at 16:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/expr.replace/near/123921877):
<p>Why isn't it currently implementable?</p>

#### [ Sebastian Ullrich (Mar 19 2018 at 16:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/expr.replace/near/123921882):
<p>It's basically <code>nat</code>, but provides an opaque constant that is assumed to be large enough that the code generator can just ignore the type in practice... :)</p>

#### [ Sebastian Ullrich (Mar 19 2018 at 16:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/expr.replace/near/123921929):
<p>So it's just a hint to the code generator</p>

#### [ Mario Carneiro (Mar 19 2018 at 16:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/expr.replace/near/123921930):
<p>Wouldn't it be better to just do a well founded recursion with an omitted proof?</p>

#### [ Jakob von Raumer (Mar 19 2018 at 16:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/expr.replace/near/123921936):
<blockquote>
<p>But I cannot imagine that there's not a suitable version of <code>expr.is_app_of</code> somewhere, such that <code>(expr.app (expr.app (expr.const `lt []) (expr.var 1)) (expr.var 0)).is_app_of `lt'</code>actually evaluates to <code>tt</code>...</p>
</blockquote>
<p>God damn it, there's a <code>'</code> in the end of that line...</p>

#### [ Moses Schönfinkel (Mar 19 2018 at 16:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/expr.replace/near/123921946):
<p>But you can prove so easily that <code>fuel</code> is nicely structurally decreasing! :P</p>

#### [ Mario Carneiro (Mar 19 2018 at 16:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/expr.replace/near/123921958):
<p>The point is it's a lie though</p>

#### [ Mario Carneiro (Mar 19 2018 at 16:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/expr.replace/near/123921968):
<p>the real <code>fuel</code> is infinity, which is not well founded, I think we should be honest about that</p>

#### [ Moses Schönfinkel (Mar 19 2018 at 16:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/expr.replace/near/123922021):
<p>I admit nothing, deny everything. It proofchecks, surely it must be correct ;).</p>

#### [ Moses Schönfinkel (Mar 19 2018 at 16:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/expr.replace/near/123922031):
<p>(It's a minor detail that it doesn't model whatever it is I had set out to do.)</p>

#### [ Mario Carneiro (Mar 19 2018 at 16:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/expr.replace/near/123922034):
<p>Alternatively, the VM could support some coinductive type</p>

#### [ Sebastian Ullrich (Mar 19 2018 at 16:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/expr.replace/near/123922044):
<p><span class="user-mention" data-user-id="110049">@Mario Carneiro</span> What does omitted mean, <code>sorry</code>? Things like macro expansion will be _provably_ non-wellfounded, as long as we don't restrict the user input.</p>

#### [ Mario Carneiro (Mar 19 2018 at 16:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/expr.replace/near/123922045):
<p><code>undefined</code> actually, but yes</p>

#### [ Mario Carneiro (Mar 19 2018 at 16:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/expr.replace/near/123922095):
<p>I would rather have a sign that says "this is false, but that won't stop me" than a shell game that is false but not obviously so</p>

#### [ Sebastian Ullrich (Mar 19 2018 at 16:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/expr.replace/near/123922097):
<p>We want non-meta definitions to prove partial correctness of them. There is no need for <code>fuel</code> in meta.</p>

#### [ Mario Carneiro (Mar 19 2018 at 16:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/expr.replace/near/123922154):
<p>Why not use coinductive types? That's what they are for</p>

#### [ Mario Carneiro (Mar 19 2018 at 16:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/expr.replace/near/123922173):
<p>I don't mean supporting some <code>coinductive</code> command mind you, just some specific useful/relevant coinductive type, like mathlib <code>computation</code></p>

#### [ Mario Carneiro (Mar 19 2018 at 16:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/expr.replace/near/123922177):
<p>which is basically "programming with fuel"</p>

#### [ Mario Carneiro (Mar 19 2018 at 17:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/expr.replace/near/123922326):
<p>The problem is that models of coinductive types in CIC are not computationally efficient (i.e. stream as a nat -&gt; A instead of B -&gt; A x B), so they need to be VM reimplemented</p>

#### [ Sebastian Ullrich (Mar 19 2018 at 17:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/expr.replace/near/123922492):
<p>Yeah, I'm not looking forward to that.</p>

#### [ Sebastian Ullrich (Mar 19 2018 at 17:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/expr.replace/near/123923027):
<p>I agree that <code>computation</code> may be a more satisfying design (it shouldn't matter for the proofs), but any trampolining will be bad for performance</p>

#### [ Mario Carneiro (Mar 19 2018 at 17:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/expr.replace/near/123923222):
<p>Trampolining how? B  -&gt; A x B is exactly the same as the state monad, and it didn't seem to be a big problem there; I assumed the plan was to optimize the trampoline away once lean compilation gets good</p>

#### [ Mario Carneiro (Mar 19 2018 at 17:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/expr.replace/near/123923312):
<p>Speaking of which, this requires a trivial amount of VM support - "call Y instead of X", and it would solve a huge number of problems if an API for that was exposed</p>

#### [ Mario Carneiro (Mar 19 2018 at 17:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/expr.replace/near/123923485):
<p>Other applications include "VM identity functions", where some nontrivial lean function is the identity in VM representation, while executing it as written will have much worse performance (for example, <code>list.attach</code> is O(n) but is a VM identity function)</p>

#### [ Sebastian Ullrich (Mar 19 2018 at 17:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/expr.replace/near/123923549):
<p>It sounds like we would have to specialize the trampoline driver to the specific functional, but I don't expect specialization any time soon</p>

#### [ Sebastian Ullrich (Mar 19 2018 at 17:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/expr.replace/near/123923826):
<p>"call Y instead of X" sounds like trouble if the types of Y and X have different runtime representations like in your first example...?</p>

#### [ Simon Hudon (Mar 19 2018 at 18:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/expr.replace/near/123926097):
<p>I like Mario's thinking. Using <code>computation</code> instead of the <code>fuel</code> trick has the added benefit that, if you call one of those functions in code where precise knowledge about termination matters, the type tells you exactly what to expect. And a computation + proof of termination gives you a properly well-founded Lean value</p>

#### [ Simon Hudon (Mar 19 2018 at 18:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/expr.replace/near/123926161):
<p>An example where I have seen that separation to be productive is when the proof of termination depends on the shape of a pointer structure</p>

#### [ Simon Hudon (Mar 19 2018 at 18:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/expr.replace/near/123926401):
<p>If that's useful, I have a Lean port of Chlipala general recursion machinery.</p>

#### [ Sebastian Ullrich (Mar 20 2018 at 10:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/expr.replace/near/123955936):
<p>Chlipala appears to list some strong limitations for both of his coinductive definitions</p>

#### [ Mario Carneiro (Mar 20 2018 at 13:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/expr.replace/near/123960430):
<blockquote>
<p>"call Y instead of X" sounds like trouble if the types of Y and X have different runtime representations like in your first example...?</p>
</blockquote>
<p>It's okay as long as it's a complete type replacement, i.e., all the functions that access the type are replaced with modified versions. For example, we could VM-replace <code>nat.add</code> with<code>num.add</code>, and also all the other nat functions, if we wanted to have a lean-based fast nat implementation. Similarly, you could use this to support the quotient encoding: you don't VM-replace <code>quot A</code> by <code>A</code> because it's a type so it won't be called anyway, but you replace all the <code>quot</code> functions with identity functions.</p>
<p>If we ever get the ability to write system F functions for direct use by the VM (although this is a whole separate feature), it would also be useful to use VM replacement here, in case a certain function can't be well-typed in lean but is valid system F.</p>

#### [ Mario Carneiro (Mar 20 2018 at 13:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/expr.replace/near/123961117):
<blockquote>
<p>It sounds like we would have to specialize the trampoline driver to the specific functional, but I don't expect specialization any time soon</p>
</blockquote>
<p>Thinking more about how this would actually work with <code>computation</code>, we have <code>computation.run</code> which calls the corecursor (which has type B -&gt; A + B after VM-replacement), returns A if success, and otherwise calls itself with the new value of B. This function is the "trampoline" in your scenario. On the other side, the coinductive type is being represented by the corecursor itself, so the user wrote this function B -&gt; A + B. You would have to call the B part whenever you need to use some fuel, and otherwise return the output or continue some other well-founded recursion etc.</p>
<p>Part of the problem with programming this way is that B must contain the entire state of the program, everything that changes during the recursion, and it's usually unpleasant to have to explicitly enumerate all this data - this is what the compiler should be doing for you. One really nice way to handle this would be to have a compiler from unbounded recursive definitions to <code>computation</code>, or even simpler, a <code>computation.fix</code> operator which allows you to write such functions directly. (Apparently there is no computation.fix defined, but it isn't hard to define, with type <code>(A -&gt; computation A) -&gt; computation A</code>.)</p>

#### [ Mario Carneiro (Mar 20 2018 at 13:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/expr.replace/near/123961241):
<p>With this latter approach, you could just call <code>fix f</code> instead of <code>computation.run (computation.fix (ret o f))</code> on the VM side and thus avoid most of the trampolining. There would still be <code>fix(f) { return f(fix(f)); }</code> which I guess can be inlined(?) but otherwise seems difficult to improve on</p>

#### [ Sebastian Ullrich (Mar 20 2018 at 13:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/expr.replace/near/123961675):
<blockquote>
<p>It's okay as long as it's a complete type replacement</p>
</blockquote>
<p>I see, yes. We're planning to allow <code>private</code> fields in structures to hide implementation details like <code>string</code>, which could be used here as well</p>

#### [ Sebastian Ullrich (Mar 20 2018 at 14:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/expr.replace/near/123962943):
<blockquote>
<p>One really nice way to handle this would be to have a compiler from unbounded recursive definitions to computation</p>
</blockquote>
<p>This would be a nice feature for a future equation compiler defined in Lean. With <code>fix</code>, you still have to pack multiple arguments into tuples. Though that could also happen automatically when lifting <code>computation</code> through <code>state_t</code>.</p>

#### [ Simon Hudon (Mar 20 2018 at 15:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/expr.replace/near/123966262):
<p>I can see a lot of use for a new generation of equation compilers (including some for corecursive functions). For computation specifically, it would be nice if it worked on the basis of a type class. If your return type is a monad that supports unbounded recursion, then its amenable to the treatment of the new equation compiler.</p>

#### [ Sebastian Ullrich (Mar 20 2018 at 15:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/expr.replace/near/123966322):
<p>I will be very happy if all of this works out some day :)</p>

#### [ Sebastian Ullrich (Mar 20 2018 at 15:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/expr.replace/near/123966324):
<p>Still not sure I should use it in the parser <span class="emoji emoji-1f604" title="smile">:smile:</span></p>

#### [ Mario Carneiro (Mar 20 2018 at 16:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/expr.replace/near/123967244):
<p>Why not put a limitation on how many nested macros to unfold? Seems like that would be undesirable anyway</p>

#### [ Sebastian Ullrich (Mar 20 2018 at 16:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/expr.replace/near/123967451):
<p>Yes, that's what it currently looks like. There may be better examples, like parsing routines where we don't want to prove wellfoundedness without the tactic framework.</p>

#### [ Simon Hudon (Mar 20 2018 at 16:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/expr.replace/near/123967582):
<p>That is also a problem with unbounded recursion: you need to prove that your functions are monotonic. The tactic framework is useful for that. Maybe we can do it with type classes too though</p>

#### [ Mario Carneiro (Mar 20 2018 at 16:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/expr.replace/near/123967885):
<p>This is part of the reason I want to avoid the <code>fuel</code> approach - the functions of interest are not all functions, but functions that have some monotonicity conditions as <code>fuel</code> changes, and you have to prove this for all functions you define, even though the proof is always straightforward.</p>

#### [ Simon Hudon (Mar 20 2018 at 16:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/expr.replace/near/123968026):
<p>But I have found the <code>(H : monotonic f . prove_monotonicity)</code> notation to be pretty useful to make that invisible</p>

#### [ Simon Hudon (Mar 20 2018 at 16:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/expr.replace/near/123968031):
<p>(in the parameters of <code>fix</code> for instance</p>

#### [ Mario Carneiro (Mar 20 2018 at 16:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/expr.replace/near/123968052):
<p>Not sure how much of this is available in the parser stuff though (maybe bootstrapping will help here)</p>

#### [ Chris Hughes (Dec 04 2018 at 03:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/expr.replace/near/150819592):
<p>What does expr.replace do?</p>

#### [ Keeley Hoek (Dec 05 2018 at 18:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/expr.replace/near/150943939):
<p>So because of <code>expr.app</code> and other such things an <code>expr</code> is a big tree of little-er <code>expr</code>s. You can get lean to map over an <code>expr</code> in this way with a function which can decide to replace subexpressions or not (the function decides to either a) replace this with something I provide or b) don't replace and descend into it instead). The <code>nat</code> argument tells you how deep in the binders you are, so you can correctly emit <code>expr.var</code>s.</p>

#### [ Chris Hughes (Dec 05 2018 at 18:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/expr.replace/near/150944046):
<p>Thanks. Sounds like what I wanted.</p>

#### [ Edward Ayers (Dec 05 2018 at 18:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/expr.replace/near/150944777):
<p>added docstring to <code>https://github.com/EdAyers/lean</code></p>

#### [ Chris Hughes (Dec 22 2018 at 07:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/expr.replace/near/152378457):
<p>Struggling to use <code>expr.replace</code> slightly. I want to use <code>infer_type</code> to fill in the <code>(expr → ℕ → option expr)</code> argument, but this returns a <code>tactic expr</code> not an <code>expr</code> or <code>option expr</code>. Is there any way around this?</p>

#### [ Kenny Lau (Dec 22 2018 at 07:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/expr.replace/near/152378832):
<p>so just extract the <code>expr</code>?</p>

#### [ Kenny Lau (Dec 22 2018 at 07:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/expr.replace/near/152378834):
<p><code>t &lt;- infer_type u</code></p>

#### [ Mario Carneiro (Dec 22 2018 at 07:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/expr.replace/near/152378882):
<p>no way around it, I'm afraid. <code>infer_type</code> wouldn't even work because it's looking at open terms</p>

#### [ Mario Carneiro (Dec 22 2018 at 07:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/expr.replace/near/152378890):
<p>you have to explicitly traverse the term and <code>instantiate_local</code> to go through binders</p>

#### [ Mario Carneiro (Dec 22 2018 at 07:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/expr.replace/near/152378892):
<p><code>tactic.hide</code> is an example</p>

#### [ Chris Hughes (Dec 22 2018 at 08:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/expr.replace/near/152379188):
<p>Okay thanks.</p>


{% endraw %}
