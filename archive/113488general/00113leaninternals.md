---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/00113leaninternals.html
---

## Stream: [general](index.html)
### Topic: [lean internals](00113leaninternals.html)

---


{% raw %}
#### [ VinothKumar Raman (Mar 13 2018 at 16:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20internals/near/123659092):
<p>Is there any good reference to learn how to elaborate implicit arguments to a coc like core? Like how lean does? I am trying to build a coc like language<br>
<a href="http://godel.yellowflash.in/" target="_blank" title="http://godel.yellowflash.in/">http://godel.yellowflash.in/</a><br>
I want to introduce implicit arguments, I have some idea in my head but I couldn't put it down clearly, Its mostly based on resolution in simple basic types. But I have a feeling that it won't work</p>

#### [ VinothKumar Raman (Mar 13 2018 at 16:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20internals/near/123659153):
<p>The idea is more like completely apply the explicit arguments and run unification of simple basic types to infer the missing arguments.</p>

#### [ Andrew Ashworth (Mar 13 2018 at 17:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20internals/near/123660760):
<p>is godel your effort?</p>

#### [ Gabriel Ebner (Mar 13 2018 at 17:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20internals/near/123661404):
<blockquote>
<p>The idea is more like completely apply the explicit arguments and run unification of simple basic types to infer the missing arguments.</p>
</blockquote>
<p>This is almost exactly how Lean's elaborator works.  Essentially you keep around a unification state ("metavar_context", basically a partial assignment of metavariables to expressions).  Now you go recursively through the pre-expression (abstract syntax tree, without implicit arguments) and convert it to an expression.  For every application you fill in the implicit arguments as metavariables, and solve the appropriate unfication constraints so that the application type-checks.  At the end, hopefully all metavariables are filled in and you can instantiate all metavariables in the produced expression.</p>

#### [ Gabriel Ebner (Mar 13 2018 at 17:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20internals/near/123661424):
<p>Except that <code>unification of simple basic types</code> is more like first-order unification + several pages of heuristics.</p>

#### [ VinothKumar Raman (Mar 14 2018 at 09:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20internals/near/123693401):
<blockquote>
<p>is godel your effort?</p>
</blockquote>
<p>Yea it is my effort. I read a bit about COC and built it</p>

#### [ VinothKumar Raman (Mar 14 2018 at 09:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20internals/near/123693506):
<p>I was reading a bit about the unification on COC. Some claim it <code>might</code> be undecidable. But it seem really possible to have implicit arguments and really decide on it right? I don't understand how it could be undecidable.</p>

#### [ Mario Carneiro (Mar 14 2018 at 09:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20internals/near/123693552):
<p>Higher order unification is undecidable</p>

#### [ VinothKumar Raman (Mar 14 2018 at 09:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20internals/near/123693553):
<p>What kind of heuristics does lean use? Is it in general not decidable? Is there any reference to read about tha?</p>

#### [ Mario Carneiro (Mar 14 2018 at 09:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20internals/near/123693572):
<p>Lean doesn't do full higher order unification, it uses a few simpler strategies and mostly sticks to first order unification</p>

#### [ VinothKumar Raman (Mar 14 2018 at 09:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20internals/near/123693872):
<p>So lean's type checking is guaranteed to terminate? I have a noob question, does making the type checking semi-decidable, affects the soundness in any way?</p>

#### [ Mario Carneiro (Mar 14 2018 at 10:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20internals/near/123694088):
<p>Lean's typechecker is guaranteed to halt, but is not complete - some definitional equalities will not be discovered by the typechecker, and it is impossible for it to do so without becoming undecidable.</p>

#### [ Mario Carneiro (Mar 14 2018 at 10:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20internals/near/123694112):
<p>The guarantee is of soundness only - if lean verifies a type derivation, then it is correct, but it may error on a correct type derivation</p>

#### [ VinothKumar Raman (Mar 14 2018 at 10:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20internals/near/123694184):
<p>So its also possible to take the alternate route to have soundness intact by doing a higher order unification, which might not halt but if it did its correct type derivation.</p>

#### [ VinothKumar Raman (Mar 14 2018 at 10:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20internals/near/123694194):
<p>Thanks, I would read about higher order unification, Is <code>Huet</code> algorithm the only one?</p>

#### [ Mario Carneiro (Mar 14 2018 at 10:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20internals/near/123694261):
<p>Note that unification is irrelevant to type checking; there is no unifier in the kernel</p>

#### [ Mario Carneiro (Mar 14 2018 at 10:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20internals/near/123694309):
<p>it is definitional equality itself that is undecidable, due to some complications with subsingleton elimination and proof irrelevance</p>

#### [ VinothKumar Raman (Mar 14 2018 at 10:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20internals/near/123694328):
<p>If the core language doesnt have the notion of <code>implicit</code> how do you know that certain arguments are marked implicit?</p>

#### [ Mario Carneiro (Mar 14 2018 at 10:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20internals/near/123694381):
<p>The actual type of expressions <code>expr</code> has an annotation field on lambda and pi that marks implicitness, but the kernel ignores it</p>

#### [ Mario Carneiro (Mar 14 2018 at 10:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20internals/near/123694411):
<p>unification and implicit parameters are all the domain of the elaborator, which is a giant untrusted piece of code</p>

#### [ VinothKumar Raman (Mar 14 2018 at 10:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20internals/near/123694416):
<p>Ah it makes sense. I have one more trivial question which I faced <br>
How do you rewrite <code>definition x = y</code> where <code>x</code> is not annotated with type to some <code>(\x:A,Z)y</code>?</p>

#### [ Mario Carneiro (Mar 14 2018 at 10:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20internals/near/123694467):
<p>I don't quite follow your notation</p>

#### [ Mario Carneiro (Mar 14 2018 at 10:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20internals/near/123694478):
<p>are you asking how to infer the type of an expression <code>y</code>?</p>

#### [ VinothKumar Raman (Mar 14 2018 at 10:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20internals/near/123694488):
<p>so any <code>let x = y in z</code> can be rewritten to <code>(\lambda x, z) y</code> so definition is very similar to let right?</p>

#### [ Mario Carneiro (Mar 14 2018 at 10:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20internals/near/123694534):
<p>a definition doesn't have a scope</p>

#### [ Mario Carneiro (Mar 14 2018 at 10:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20internals/near/123694536):
<p>also <code>let</code> is not the same as a lambda application</p>

#### [ VinothKumar Raman (Mar 14 2018 at 10:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20internals/near/123694538):
<p>But how do you rewrite your definitions to core calculus with just lambda abstraction, when you dont have type annotation</p>

#### [ Mario Carneiro (Mar 14 2018 at 10:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20internals/near/123694546):
<p>there is a type annotation</p>

#### [ Mario Carneiro (Mar 14 2018 at 10:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20internals/near/123694555):
<p>the syntax is <code>let x : t := p in e</code></p>

#### [ VinothKumar Raman (Mar 14 2018 at 10:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20internals/near/123694561):
<p><code>definition x = y</code> is allowed right? Not just <code>definition x: z = y</code> right?</p>

#### [ VinothKumar Raman (Mar 14 2018 at 10:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20internals/near/123694572):
<p>That type annotation is not optional?</p>

#### [ Mario Carneiro (Mar 14 2018 at 10:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20internals/near/123694573):
<p>no, it's only <code>def x : t := e</code>. If you leave out the <code>t</code> it is inferred and filled in</p>

#### [ VinothKumar Raman (Mar 14 2018 at 10:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20internals/near/123694617):
<p>So elaborator runs type checking before it turns to core calculus?</p>

#### [ Mario Carneiro (Mar 14 2018 at 10:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20internals/near/123694623):
<p>Many type annotations are "optional" in the sense that you don't have to write them, but they are inserted by the elaborator</p>

#### [ VinothKumar Raman (Mar 14 2018 at 10:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20internals/near/123694640):
<p>I was thinking elaborator writes out a new lambda term in the core calculus and type checking is completely different step.</p>

#### [ Mario Carneiro (Mar 14 2018 at 10:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20internals/near/123694646):
<p>the parser produces a <code>pexpr</code>, this is a representation that roughly follows the AST of the user's input, all missing type information is absent, and the elaborator inserts metavariables in the holes, performs unification, and results an <code>expr</code> that has all type information filled in</p>

#### [ Mario Carneiro (Mar 14 2018 at 10:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20internals/near/123694699):
<p>After this is done, the expr is sent to the kernel where it is typechecked (again, since the elaborator also has a typechecker that does other stuff on the side)</p>

#### [ VinothKumar Raman (Mar 14 2018 at 10:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20internals/near/123694710):
<p>Its not very linear as I imagined it to be.</p>

#### [ VinothKumar Raman (Mar 14 2018 at 10:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20internals/near/123694719):
<p>I think I understand the complexity very well now after trying to implement one :)</p>

#### [ Mario Carneiro (Mar 14 2018 at 10:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20internals/near/123694756):
<p>Writing an elaborator is no joke</p>

#### [ VinothKumar Raman (Mar 14 2018 at 10:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20internals/near/123694770):
<p>There is no concrete theory to it? Like lambda calculus substitution.</p>

#### [ Mario Carneiro (Mar 14 2018 at 10:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20internals/near/123694777):
<p>That's what the kernel does</p>

#### [ VinothKumar Raman (Mar 14 2018 at 10:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20internals/near/123694780):
<p>Its very messy in lot of ways.</p>

#### [ VinothKumar Raman (Mar 14 2018 at 10:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20internals/near/123694789):
<p>I mean the elaborator doesnt have concrete theory?</p>

#### [ Mario Carneiro (Mar 14 2018 at 10:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20internals/near/123694835):
<p>Parts of it do, I'm sure</p>

#### [ Mario Carneiro (Mar 14 2018 at 10:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20internals/near/123694851):
<p>like the first order unification algorithm is pretty well understood at this point</p>

#### [ VinothKumar Raman (Mar 14 2018 at 10:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20internals/near/123694863):
<p>Yea, I tried implementing first order unification on simple basic types with <code>let</code> polymorphism once<br>
<a href="https://github.com/yellowflash/hindley" target="_blank" title="https://github.com/yellowflash/hindley">https://github.com/yellowflash/hindley</a></p>

#### [ Mario Carneiro (Mar 14 2018 at 10:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20internals/near/123694864):
<p>Most of the complication has to do with when to unfold definitions, I think</p>

#### [ VinothKumar Raman (Mar 14 2018 at 10:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20internals/near/123694865):
<p>Its was super clear</p>

#### [ VinothKumar Raman (Mar 14 2018 at 10:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20internals/near/123694915):
<p>But definitions are normalizing right? Which mean you could find normal form and unify them</p>

#### [ Mario Carneiro (Mar 14 2018 at 10:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20internals/near/123694916):
<p>lol sure if you want to wait until the end of the universe</p>

#### [ VinothKumar Raman (Mar 14 2018 at 10:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20internals/near/123694917):
<p>Ah wait, I understand. It could go both directions on beta reduction</p>

#### [ Mario Carneiro (Mar 14 2018 at 10:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20internals/near/123694920):
<p>DTT "terminates", but it's not remotely practical</p>

#### [ Mario Carneiro (Mar 14 2018 at 10:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20internals/near/123694929):
<p>so there are lots of heuristics for when to unfold something</p>

#### [ VinothKumar Raman (Mar 14 2018 at 10:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20internals/near/123695033):
<p>Oh ok</p>


{% endraw %}
