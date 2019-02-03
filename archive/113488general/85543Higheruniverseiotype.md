---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/85543Higheruniverseiotype.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: ["Higher universe" io type](https://leanprover-community.github.io/archive/113488general/85543Higheruniverseiotype.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Keeley Hoek (Aug 10 2018 at 16:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22Higher%20universe%22%20io%20type/near/131240824):
<p>Consider the following silly lean program:</p>
<div class="codehilite"><pre><span></span>import system.io

structure the_structure :=
  (a_type : Type)
  (str : string)

def print_struct : io the_structure := do
  return (the_structure.mk nat &quot;some-text&quot;)
</pre></div>


<p>The program fails to typecheck witht he following error:</p>
<div class="codehilite"><pre><span></span>type mismatch at application
  io the_structure
term
  the_structure
has type
  Type 1 : Type 2
but is expected to have type
  Type : Type 1
</pre></div>


<p>Is there anything that can be done to salvage this code?</p>
<p>I suppose I'm really asking: why am I prevented from doing this?</p>

#### [ Mario Carneiro (Aug 10 2018 at 16:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22Higher%20universe%22%20io%20type/near/131240924):
<p><code>the_structure</code> contains a <code>Type</code>, so it is a member of <code>Type 1</code></p>

#### [ Mario Carneiro (Aug 10 2018 at 16:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22Higher%20universe%22%20io%20type/near/131241013):
<p>On the other hand <code>io</code> is defined to only take <code>Type = Type 0</code> (for some reason...)</p>

#### [ Keeley Hoek (Aug 10 2018 at 16:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22Higher%20universe%22%20io%20type/near/131241027):
<p>Is there any reason why <code>io</code> should only take <code>Type</code>s?</p>

#### [ Keeley Hoek (Aug 10 2018 at 16:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22Higher%20universe%22%20io%20type/near/131241039):
<p>Yes, that is what I was wondering!</p>

#### [ Mario Carneiro (Aug 10 2018 at 16:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22Higher%20universe%22%20io%20type/near/131241078):
<p>not really, I think Leo just didn't think it would get used like that - programming stuff usually lives in Type</p>

#### [ Mario Carneiro (Aug 10 2018 at 16:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22Higher%20universe%22%20io%20type/near/131241202):
<p>Normally everything is universe polymorphic, <code>io</code> seems to be an exception</p>

#### [ Mario Carneiro (Aug 10 2018 at 16:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22Higher%20universe%22%20io%20type/near/131241213):
<p><span class="user-mention" data-user-id="110024">@Sebastian Ullrich</span> Do you know anything about the story here?</p>

#### [ Mario Carneiro (Aug 10 2018 at 16:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22Higher%20universe%22%20io%20type/near/131241299):
<p>Unfortunately even <code>meta</code> doesn't save you from universe checks</p>

#### [ Mario Carneiro (Aug 10 2018 at 16:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22Higher%20universe%22%20io%20type/near/131241455):
<p>Here's a weird meta workaround:</p>
<div class="codehilite"><pre><span></span>meta structure the_structure : Type :=
(a_type : expr)
(str : string)

meta def print_struct : io the_structure := do
return (the_structure.mk `(nat) &quot;some-text&quot;)
</pre></div>

#### [ Keeley Hoek (Aug 10 2018 at 16:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22Higher%20universe%22%20io%20type/near/131241536):
<p>I see. Thanks. I think what I'm doing isn't too ridiculous---I'd like to to have a few modules in a program which are different ways of performing the same "job", each needing their own internal types etc. I wanted to be able to fill a structure with their functions and the types they take so the calling code could be module-independent. I'm just trying to say I don't think I'm doing something toooo arcane</p>
<p>haha indeed, and once something is bumped up somewhere it is a cancer which proliferates through everything! :D</p>

#### [ Mario Carneiro (Aug 10 2018 at 16:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22Higher%20universe%22%20io%20type/near/131241617):
<p>existential types are one of the weak points of dependent type theory over a system F like type system such as Haskell</p>

#### [ Mario Carneiro (Aug 10 2018 at 16:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22Higher%20universe%22%20io%20type/near/131241655):
<p>You can get many of the same benefits of existential types through typeclasses</p>

#### [ Keeley Hoek (Aug 10 2018 at 16:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22Higher%20universe%22%20io%20type/near/131241764):
<p>Thanks for the workaround there---but am I right in thinking that without converting just everything into expressions, that I won't be able declare another member of that structure to be a function which takes something of type <code>a_type</code>?</p>
<p>ok thanks very much for your comments, I think i might resort to that even though there might be a bit more ugliness down the road!</p>

#### [ Mario Carneiro (Aug 10 2018 at 16:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22Higher%20universe%22%20io%20type/near/131241892):
<p>Most of the currently available typeclasses have a mathematical bent, but consider for example <code>group A</code>. This is a typeclass on a type <code>A</code> providing it with a "multiplication" operation, which can be implemented however you like, provided it meets the axioms stated in the structure. This is lean's version of java type interfaces</p>

#### [ Mario Carneiro (Aug 10 2018 at 16:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22Higher%20universe%22%20io%20type/near/131241919):
<p>If you have an operation that can be implemented multiple ways, you define the operation as a typeclass and have multiple instances (implementations) of it</p>

#### [ Mario Carneiro (Aug 10 2018 at 16:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22Higher%20universe%22%20io%20type/near/131242028):
<blockquote>
<p>Thanks for the workaround there---but am I right in thinking that without converting just everything into expressions, that I won't be able declare another member of that structure to be a function which takes something of type a_type?</p>
</blockquote>
<p>You can convert from expressions to objects and back in meta land using <code>eval_expr</code> and <code>reflect</code>, respectively</p>

#### [ Mario Carneiro (Aug 10 2018 at 16:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22Higher%20universe%22%20io%20type/near/131242075):
<p>You lose typechecking though - it's just two <code>expr</code>s and it's up to you to make sure one is a function and the other is a value of the same type</p>

#### [ Keeley Hoek (Aug 10 2018 at 16:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22Higher%20universe%22%20io%20type/near/131242441):
<p>I think I can make it weirder! So, it turns out (because of variable universes being allowed there) changing "io" to "tactic" above <em>does</em> work. But(!) now consider the following slight modification</p>
<div class="codehilite"><pre><span></span>structure the_structure :=
  (a_type : Type)
  (str : string)

#check the_structure

meta def print_struct : tactic the_structure := do
  t ← pure (the_structure.mk nat &quot;some-text&quot;),
  n ← pure &quot;ello&quot;,
  return t
</pre></div>


<p>We now fail to typecheck because:</p>
<div class="codehilite"><pre><span></span>type mismatch at application
  pure &quot;ello&quot;
term
  &quot;ello&quot;
has type
  string : Type
but is expected to have type
  ?m_1 : Type 1
</pre></div>


<p>So <code>string</code> is too <em>low</em> in the universe hierarchy! This seems even weirder to me than the previous case---is there any why this shouldn't be allowed?</p>

#### [ Mario Carneiro (Aug 10 2018 at 16:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22Higher%20universe%22%20io%20type/near/131242565):
<p>This is due to the fact that everything lives in exactly one type - there is no type subsumption in lean</p>

#### [ Mario Carneiro (Aug 10 2018 at 16:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22Higher%20universe%22%20io%20type/near/131242585):
<p>but it's easy to work around in this case  - the <code>ulift</code> function moves things from any universe to a higher one</p>

#### [ Mario Carneiro (Aug 10 2018 at 16:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22Higher%20universe%22%20io%20type/near/131242677):
<p>so you should be able to replace that line with <code>⟨n⟩ ← pure (ulift.up.{1} "ello"),</code></p>

#### [ Mario Carneiro (Aug 10 2018 at 16:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22Higher%20universe%22%20io%20type/near/131242720):
<p>or <code>⟨n⟩ ← pure (⟨"ello"⟩ : ulift string),</code></p>

#### [ Keeley Hoek (Aug 10 2018 at 17:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22Higher%20universe%22%20io%20type/near/131242795):
<p>you're awesome, mario! cheers and thanks again</p>

#### [ Kevin Buzzard (Aug 10 2018 at 17:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22Higher%20universe%22%20io%20type/near/131243075):
<blockquote>
<p>you're awesome, mario! </p>
</blockquote>
<p>Without him, none of this would be happening.</p>

#### [ Sebastian Ullrich (Aug 10 2018 at 18:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22Higher%20universe%22%20io%20type/near/131834807):
<p>I believe a universe-polymorphic <code>io</code> would only make sense if we add a new primitive <code>io.ulift : io a -&gt; io (ulift a)</code>. Otherwise you would not be able to use any io primitives from an <code>io</code> of a higher universe. Monads really seem to be one of the better arguments for universe cumulativity, though so far we haven't run into any unavoidable issues regarding that yet.</p>

#### [ Mario Carneiro (Aug 10 2018 at 19:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22Higher%20universe%22%20io%20type/near/131835355):
<p><code>io.ulift</code> is just <code>map ulift.up</code></p>

#### [ Mario Carneiro (Aug 10 2018 at 19:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22Higher%20universe%22%20io%20type/near/131835390):
<p>oh wait nvm</p>

#### [ Mario Carneiro (Aug 10 2018 at 19:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22Higher%20universe%22%20io%20type/near/131835397):
<p>better yet, <code>io.map</code> should be a primitive</p>

#### [ Simon Hudon (Aug 10 2018 at 21:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22Higher%20universe%22%20io%20type/near/131842156):
<p>I came up with a type class <code>liftable</code> which I like for this kind of problem. With functors, this universe thing infects the types. I think this will help.</p>

#### [ Simon Hudon (Aug 10 2018 at 21:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22Higher%20universe%22%20io%20type/near/131842157):
<p><a href="https://github.com/cipher1024/slim_check/blob/f6c44cc48bc44c108ce88c4b1d5cad7b3f63445d/test/slim_check/liftable.lean" target="_blank" title="https://github.com/cipher1024/slim_check/blob/f6c44cc48bc44c108ce88c4b1d5cad7b3f63445d/test/slim_check/liftable.lean">https://github.com/cipher1024/slim_check/blob/f6c44cc48bc44c108ce88c4b1d5cad7b3f63445d/test/slim_check/liftable.lean</a></p>

#### [ Simon Hudon (Aug 10 2018 at 21:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22Higher%20universe%22%20io%20type/near/131842166):
<p>I can put it in the nursery</p>


{% endraw %}
