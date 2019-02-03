---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/08327darraytypechangingupdate.html
---

## Stream: [general](index.html)
### Topic: [`d_array` type changing update](08327darraytypechangingupdate.html)

---


{% raw %}
#### [ Simon Hudon (Apr 26 2018 at 05:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%60d_array%60%20type%20changing%20update/near/125705649):
<p>In <code>data.array.basic</code>, there's an optimized mutation function:</p>
<div class="codehilite"><pre><span></span>def foreach (a : d_array n α) (f : Π i : fin n, α i → α i) : d_array n α :=
...
</pre></div>


<p>Is it possible to change the element type during the update efficiently? I'd like an operation like:</p>
<div class="codehilite"><pre><span></span>def foreach (a : d_array n α) (f : Π i : fin n, α i → β i) : d_array n β :=
...
</pre></div>


<p>Ultimately, I'm trying to implement <code>traversable</code> for array and I'd like it to not be too slow. If the required functions are not available, should I postpone submitting a traversable instance of array to <code>mathlib</code> until it can be done efficiently?</p>

#### [ Mario Carneiro (Apr 26 2018 at 05:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%60d_array%60%20type%20changing%20update/near/125706021):
<p>No, it's an in-place update so the type has to stay fixed.</p>

#### [ Simon Hudon (Apr 26 2018 at 05:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%60d_array%60%20type%20changing%20update/near/125706063):
<p>Because the amount of memory allocated per element?</p>

#### [ Mario Carneiro (Apr 26 2018 at 05:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%60d_array%60%20type%20changing%20update/near/125706064):
<p>It's conceivable that you could use an auxiliary array of sigma types (which would be erased on the vm side)</p>

#### [ Mario Carneiro (Apr 26 2018 at 05:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%60d_array%60%20type%20changing%20update/near/125706075):
<p>It updates like this: [1, 2, 3] -&gt; [f 1, 2, 3] -&gt; [f 1, f 2, 3] -&gt; [f 1, f 2, f 3]</p>

#### [ Mario Carneiro (Apr 26 2018 at 05:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%60d_array%60%20type%20changing%20update/near/125706079):
<p>Each update is performed on the same underlying data structure so that space isn't wasted</p>

#### [ Simon Hudon (Apr 26 2018 at 05:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%60d_array%60%20type%20changing%20update/near/125706080):
<p>Right but now, <code>array</code> is based on <code>d_array</code> where the type of elements depends on indices</p>

#### [ Simon Hudon (Apr 26 2018 at 06:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%60d_array%60%20type%20changing%20update/near/125706126):
<p>So the intermediate arrays are well-typed</p>

#### [ Mario Carneiro (Apr 26 2018 at 06:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%60d_array%60%20type%20changing%20update/near/125706138):
<p>The core function doing the in place write is <code>array.write</code> and this function doesn't change the type of the argument</p>

#### [ Mario Carneiro (Apr 26 2018 at 06:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%60d_array%60%20type%20changing%20update/near/125706181):
<p>oh wait, the comment says that <code>foreach</code> is also given a builtin impl</p>

#### [ Mario Carneiro (Apr 26 2018 at 06:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%60d_array%60%20type%20changing%20update/near/125706239):
<p>Maybe you can get similar performance with <code>iterate</code> to build the new array?</p>

#### [ Simon Hudon (Apr 26 2018 at 06:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%60d_array%60%20type%20changing%20update/near/125706298):
<p>Actually, maybe I'm better off converting to list, traversing the list and converting back to array: if I'm executing within a monad like list that would mean duplicating the array a lot while the list would share its tail so it wouldn't be so bad.</p>

#### [ Mario Carneiro (Apr 26 2018 at 06:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%60d_array%60%20type%20changing%20update/near/125706300):
<p>Actually I think <code>array.mk</code> is the most efficient option</p>

#### [ Mario Carneiro (Apr 26 2018 at 06:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%60d_array%60%20type%20changing%20update/near/125706344):
<p>that will just evaluate the whole function at once to get the new elements</p>

#### [ Simon Hudon (Apr 26 2018 at 06:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%60d_array%60%20type%20changing%20update/near/125706523):
<p>I'm not sure how I could reconcile that with working within an applicative. I would have to store an accumulation of closures which does not sound good</p>

#### [ Mario Carneiro (Apr 26 2018 at 06:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%60d_array%60%20type%20changing%20update/near/125706533):
<div class="codehilite"><pre><span></span>def d_array.map&#39;
  {n : nat} {α β : fin n → Type*}
  (a : d_array n α) (f : Π i : fin n, α i → β i) : d_array n β :=
⟨λ i, f _ (a.read _)⟩

#eval
  let a := d_array.mk (λ a:fin 1000000, a.1) in
  let a&#39; := timeit &quot;map&quot; (a.map&#39; (λ i j, j+1)) in
  a&#39;
</pre></div>


<p>Looks like it takes roughly linear time</p>

#### [ Simon Hudon (Apr 26 2018 at 06:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%60d_array%60%20type%20changing%20update/near/125706583):
<p>That looks good but it doesn't seem to address my comment</p>

#### [ Mario Carneiro (Apr 26 2018 at 06:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%60d_array%60%20type%20changing%20update/near/125706614):
<p>It is important to realize that (unlike most constructors taking a function) <code>array.mk</code> does not store its argument function, it evaluates it and puts the result in an array</p>

#### [ Mario Carneiro (Apr 26 2018 at 06:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%60d_array%60%20type%20changing%20update/near/125706658):
<p><code>array.mk f</code> is O(n), while <code>array'.mk f</code> would be O(1) if you wrote <code>array'</code> identically to <code>array</code></p>

#### [ Mario Carneiro (Apr 26 2018 at 06:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%60d_array%60%20type%20changing%20update/near/125706720):
<p>and conversely, <code>a.read i</code> does not call the underlying function of <code>a</code></p>

#### [ Mario Carneiro (Apr 26 2018 at 06:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%60d_array%60%20type%20changing%20update/near/125706733):
<div class="codehilite"><pre><span></span>#eval
  let f (a:fin 3) := trace (&quot;calling f &quot; ++ to_string a.1) a.1 in
  let a := d_array.mk f in
  a.read ⟨1, dec_trivial⟩

-- calling f 0
-- calling f 1
-- calling f 2
--
-- (note: &quot;calling f 1&quot; does not appear twice)
</pre></div>

#### [ Simon Hudon (Apr 26 2018 at 06:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%60d_array%60%20type%20changing%20update/near/125706833):
<p>Right, that make sense but the reason I was talking about accumulating closures is that I'm thinking of  implementing the mutation by recursion because I have to combine applicative values:</p>
<div class="codehilite"><pre><span></span>def traverse (g : α → f β) : Π n (a : array n α), f (fin n → β)
 | 0 a := -- ...
 | (succ n) a := _ &lt;$&gt; g (a.read ⟨n,_⟩) &lt;*&gt; traverse n a.pop_back
</pre></div>

#### [ Mario Carneiro (Apr 26 2018 at 06:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%60d_array%60%20type%20changing%20update/near/125707001):
<p>So you have a dependency between the different elements of the computation? Like calculating the first element affects the computation of the second</p>

#### [ Simon Hudon (Apr 26 2018 at 06:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%60d_array%60%20type%20changing%20update/near/125707019):
<p>It might. <code>f</code> is actually a parameter of which I only know that it's an applicative functor</p>

#### [ Mario Carneiro (Apr 26 2018 at 06:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%60d_array%60%20type%20changing%20update/near/125707043):
<p>Do you have a default value for the array? This will be easier if you do</p>

#### [ Simon Hudon (Apr 26 2018 at 06:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%60d_array%60%20type%20changing%20update/near/125707057):
<p>Where would be the fun in "easy"? <span class="emoji emoji-1f61d" title="stuck out tongue closed eyes">:stuck_out_tongue_closed_eyes:</span>  I have no assumptions about either <code>α</code> or <code>β</code></p>

#### [ Simon Hudon (Apr 26 2018 at 06:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%60d_array%60%20type%20changing%20update/near/125707105):
<p>Except: they're from the same universe</p>

#### [ Mario Carneiro (Apr 26 2018 at 06:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%60d_array%60%20type%20changing%20update/near/125707117):
<p>I think you should just do it semi-imperatively then, just call <code>read</code> and <code>push_back</code> and make sure you use the array linearly</p>

#### [ Mario Carneiro (Apr 26 2018 at 06:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%60d_array%60%20type%20changing%20update/near/125707160):
<p>Do not do induction over the array size</p>

#### [ Mario Carneiro (Apr 26 2018 at 06:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%60d_array%60%20type%20changing%20update/near/125707165):
<p>and accumulate an array, not a function to fin n</p>

#### [ Simon Hudon (Apr 26 2018 at 06:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%60d_array%60%20type%20changing%20update/near/125707166):
<p>You mean I should do induction on the index <code>i</code> and maintain <code>i &lt; n</code>?</p>

#### [ Mario Carneiro (Apr 26 2018 at 06:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%60d_array%60%20type%20changing%20update/near/125707213):
<p>yes</p>

#### [ Simon Hudon (Apr 26 2018 at 06:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%60d_array%60%20type%20changing%20update/near/125707214):
<p>The fun thing about knowing next to nothing about <code>f</code> is that I can't guarantee that it is a linear computation: if it's a non-deterministic computation, it would screw up that assumption</p>

#### [ Mario Carneiro (Apr 26 2018 at 06:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%60d_array%60%20type%20changing%20update/near/125707217):
<p>I have no mental model for applicative functors except as monads</p>

#### [ Mario Carneiro (Apr 26 2018 at 06:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%60d_array%60%20type%20changing%20update/near/125707232):
<p>When I say linearly I mean in the "linear logic" sense, i.e.  use the variable once</p>

#### [ Simon Hudon (Apr 26 2018 at 06:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%60d_array%60%20type%20changing%20update/near/125707248):
<p>That's good enough. The only thing they add is asynchronous computations. But just think of the list monad. It's basically an unbounded backtracking device</p>

#### [ Simon Hudon (Apr 26 2018 at 06:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%60d_array%60%20type%20changing%20update/near/125707276):
<p>That means that at every branching point, I'd need a copy of the array</p>

#### [ Mario Carneiro (Apr 26 2018 at 06:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%60d_array%60%20type%20changing%20update/near/125707277):
<p>Lean doesn't currently check this but you can test it by setting some option to hear whether an array write is destructive or not</p>

#### [ Simon Hudon (Apr 26 2018 at 06:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%60d_array%60%20type%20changing%20update/near/125707285):
<p>How does that work?</p>

#### [ Mario Carneiro (Apr 26 2018 at 06:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%60d_array%60%20type%20changing%20update/near/125707289):
<p>Whenever you call <code>array.write</code> lean checks the reference counter to determine if it can do an in-place update</p>

#### [ Simon Hudon (Apr 26 2018 at 06:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%60d_array%60%20type%20changing%20update/near/125707344):
<p>But can I use that information to select a different algorithm?</p>

#### [ Simon Hudon (Apr 26 2018 at 06:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%60d_array%60%20type%20changing%20update/near/125707489):
<p>Maybe the best is accept the intermediate list. Maybe in Lean 4 we'll see custom rewrite rules for optimization. Then, maybe I can eliminate that intermediate list when the use is linear (or affine)</p>

#### [ Mario Carneiro (Apr 26 2018 at 06:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%60d_array%60%20type%20changing%20update/near/125707547):
<p>The linear usage thing is a static analysis you can do on your code to try and preserve destructive writes when the use is actually linear, but since the check is done at run time it doesn't matter if you use it in a nonlinear context, it will just make copies and that's the right thing to do</p>

#### [ Mario Carneiro (Apr 26 2018 at 06:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%60d_array%60%20type%20changing%20update/near/125707783):
<p>Does this work?</p>
<div class="codehilite"><pre><span></span>universe u
variables {α β : Type u} {f : Type u → Type u} [applicative f]

def traverse.aux (g : α → f β) (n) (a : array n α) :
  ∀ i ≤ n, f (array i β)
| 0 h := pure array.nil
| (i+1) h :=
  have h&#39; : i ≤ n := nat.le_of_succ_le h,
  array.push_back &lt;$&gt; (traverse.aux _ h&#39;) &lt;*&gt; g (a.read ⟨i, h⟩)

def traverse (g : α → f β) (n) (a : array n α) : f (array n β) :=
traverse.aux g n a n (le_refl _)
</pre></div>

#### [ Simon Hudon (Apr 26 2018 at 06:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%60d_array%60%20type%20changing%20update/near/125707829):
<p>Nice! Thanks!</p>

#### [ Simon Hudon (Apr 26 2018 at 07:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%60d_array%60%20type%20changing%20update/near/125707882):
<p>I believe in backtracking computations, this will be pretty inefficient though. I'm wondering if the rarity of such monads is a good reason to accept that cost or if taking a small hit in the general case would be a worthy price to pay so that backtracking computations wouldn't be too slow</p>

#### [ Mario Carneiro (Apr 26 2018 at 07:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%60d_array%60%20type%20changing%20update/near/125708080):
<p>For backtracking computations, you will end up using more of the <code>p</code> in the <code>p_array</code> data type that actually implements lean's <code>array</code> in C++. It has optimizations for precisely this use case, it's not just a block of memory</p>

#### [ Mario Carneiro (Apr 26 2018 at 07:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%60d_array%60%20type%20changing%20update/near/125708125):
<p>I would argue that the lack of an actual C-like array data structure is a current failing of lean, but having a deluxe array type has its advantages</p>

#### [ Mario Carneiro (Apr 26 2018 at 07:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%60d_array%60%20type%20changing%20update/near/125708128):
<p>(the <code>p</code> stands for <a href="https://en.wikipedia.org/wiki/Persistent_data_structure" target="_blank" title="https://en.wikipedia.org/wiki/Persistent_data_structure">persistent</a> btw)</p>

#### [ Simon Hudon (Apr 26 2018 at 07:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%60d_array%60%20type%20changing%20update/near/125708187):
<p>Oh! Interesting!</p>

#### [ Simon Hudon (Apr 26 2018 at 07:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%60d_array%60%20type%20changing%20update/near/125708231):
<p>I assume the kind of optimization you're talking about is to queue up updates until you get a read and only then do you actually perform them?</p>

#### [ Mario Carneiro (Apr 26 2018 at 07:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%60d_array%60%20type%20changing%20update/near/125708292):
<p>Actually I'm not exactly sure, I haven't studied the implementation in detail. I think the updates are in chunks though, there is a "buffer" aspect to it as well which makes repeated <code>push_back</code> like I've done here not stupidly inefficient</p>


{% endraw %}
