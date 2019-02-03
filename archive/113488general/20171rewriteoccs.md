---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/20171rewriteoccs.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [rewrite occs](https://leanprover-community.github.io/archive/113488general/20171rewriteoccs.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Scott Morrison (Mar 10 2018 at 22:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewrite%20occs/near/123546271):
<p>Can anyone help me understand why the 2nd example in the following doesn't work?</p>
<div class="codehilite"><pre><span></span><span class="bp">@</span><span class="o">[</span><span class="n">ematch</span><span class="o">]</span> <span class="kn">lemma</span> <span class="n">baz</span> <span class="o">(</span><span class="n">l</span> <span class="o">:</span> <span class="n">list</span> <span class="bp">ℕ</span><span class="o">)</span> <span class="o">:</span> <span class="mi">1</span> <span class="bp">::</span> <span class="n">l</span> <span class="bp">=</span> <span class="mi">2</span> <span class="bp">::</span> <span class="n">l</span> <span class="o">:=</span> <span class="n">sorry</span>
<span class="kn">example</span> <span class="o">:</span> <span class="o">[</span><span class="mi">1</span><span class="o">,</span> <span class="mi">1</span><span class="o">,</span> <span class="mi">2</span><span class="o">]</span> <span class="bp">=</span> <span class="o">[</span><span class="mi">2</span><span class="o">,</span> <span class="mi">1</span><span class="o">,</span> <span class="mi">2</span><span class="o">]</span> <span class="o">:=</span>
<span class="k">begin</span>
<span class="n">rw</span> <span class="o">[</span><span class="n">baz</span><span class="o">]</span> <span class="o">{</span><span class="n">occs</span><span class="o">:=</span><span class="n">occurrences</span><span class="bp">.</span><span class="n">pos</span> <span class="o">[</span><span class="mi">1</span><span class="o">]},</span>
<span class="kn">end</span>
<span class="kn">example</span> <span class="o">:</span> <span class="o">[</span><span class="mi">1</span><span class="o">,</span> <span class="mi">1</span><span class="o">,</span> <span class="mi">2</span><span class="o">]</span> <span class="bp">=</span> <span class="o">[</span><span class="mi">1</span><span class="o">,</span> <span class="mi">2</span><span class="o">,</span> <span class="mi">2</span><span class="o">]</span> <span class="o">:=</span>
<span class="k">begin</span>
<span class="n">rw</span> <span class="o">[</span><span class="n">baz</span><span class="o">]</span> <span class="o">{</span><span class="n">occs</span><span class="o">:=</span><span class="n">occurrences</span><span class="bp">.</span><span class="n">pos</span> <span class="o">[</span><span class="mi">2</span><span class="o">]},</span>
<span class="kn">end</span>
</pre></div>

#### [ Scott Morrison (Mar 10 2018 at 22:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewrite%20occs/near/123546276):
<p>I have been reading <code>replace_fn.cpp</code> and <code>kabstract.cpp</code>, to no avail: my understanding of what is going on there suggests the second example should still work.</p>

#### [ Scott Morrison (Mar 10 2018 at 22:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewrite%20occs/near/123546372):
<p>A related confusion is why in</p>
<div class="codehilite"><pre><span></span><span class="kn">example</span> <span class="o">:</span> <span class="o">[</span><span class="mi">1</span><span class="o">,</span> <span class="mi">1</span><span class="o">,</span> <span class="mi">2</span><span class="o">]</span> <span class="bp">=</span> <span class="o">[</span><span class="mi">1</span><span class="o">,</span> <span class="mi">2</span><span class="o">,</span> <span class="mi">2</span><span class="o">]</span> <span class="o">:=</span>
<span class="k">begin</span>
<span class="n">rw</span> <span class="o">[</span><span class="n">baz</span><span class="o">],</span>
<span class="kn">end</span>
</pre></div>


<p>the goal has become <code>[2, 1, 2] = [1, 2, 2]</code>, and not <code>[2, 1, 2] = [2, 2, 2]</code>. That is, why did rewrite give up on the rhs?</p>

#### [ Sebastian Ullrich (Mar 10 2018 at 22:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewrite%20occs/near/123546557):
<p><code>kabstract</code> does not backtrack from unification: once <code>l</code> has been assigned <code>[1, 2]</code>, it does not consider other values for it</p>

#### [ Sebastian Ullrich (Mar 10 2018 at 22:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewrite%20occs/near/123546564):
<p>That is, it only finds occurrences of the same instantiation of the lhs</p>

#### [ Sebastian Ullrich (Mar 10 2018 at 22:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewrite%20occs/near/123546609):
<p>(Don't ask me why :) )</p>

#### [ Scott Morrison (Mar 10 2018 at 22:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewrite%20occs/near/123546657):
<p>oh...</p>

#### [ Scott Morrison (Mar 10 2018 at 22:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewrite%20occs/near/123546664):
<p>I see, that <code>ctx.unify</code> call in <code>kabstract</code> is saving information about things it has seen before.</p>

#### [ Scott Morrison (Mar 10 2018 at 22:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewrite%20occs/near/123546667):
<p>It hadn't occurred to me that there were side effects there.</p>

#### [ Scott Morrison (Mar 10 2018 at 22:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewrite%20occs/near/123546697):
<p>That sucks (for my purposes)...</p>

#### [ Scott Morrison (Mar 10 2018 at 22:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewrite%20occs/near/123546756):
<p>So... if I really really wanted be be able to generate a list of all the rewrites of some expression <code>e</code> by some rule <code>r</code> (where we just rewrite in one place), is there any hope?</p>

#### [ Scott Morrison (Mar 10 2018 at 22:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewrite%20occs/near/123546763):
<p>It seems that just calling <code>rw [r] at e {occs := occurrences.pos n}</code> and gradually increasing <code>n</code> until it fails is doomed, because of this "feature" of <code>kabstract</code>.</p>

#### [ Simon Hudon (Mar 10 2018 at 22:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewrite%20occs/near/123547082):
<p>if you want to hack a solution together, you might have to copy / paste the implementation of <code>rw</code> and reimplement <code>kabstract</code>. I think the key is to undo the assignment of meta variable. One way of to that is to traverse your expression and create new meta variables to replace the ones that you find.</p>

#### [ Sebastian Ullrich (Mar 10 2018 at 22:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewrite%20occs/near/123547088):
<p>Yes. It just won't be very fast.</p>

#### [ Simon Hudon (Mar 10 2018 at 22:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewrite%20occs/near/123547146):
<p>I assume with the new focus on Lean 4, that might be the one way to get the fixed tactic sooner than later.</p>

#### [ Scott Morrison (Mar 10 2018 at 22:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewrite%20occs/near/123547154):
<p>I see: reimplement <code>kabstract</code> in Lean?</p>

#### [ Scott Morrison (Mar 10 2018 at 22:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewrite%20occs/near/123547198):
<p>I was just trying to find the definition of <code>type_context_old</code>, and see if there was any hope of hacking on an extra option that would change this behaviour. But I agree it's exceedingly unlikely I could propose such a change.</p>

#### [ Simon Hudon (Mar 10 2018 at 22:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewrite%20occs/near/123547201):
<p>yeah pretty much. Unless <span class="user-mention" data-user-id="110024">@Sebastian Ullrich</span> agrees that the current semantics is wrong and is willing to fix it for you</p>

#### [ Scott Morrison (Mar 10 2018 at 22:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewrite%20occs/near/123547207):
<p><span class="user-mention" data-user-id="110024">@Sebastian Ullrich</span> ? :-)</p>

#### [ Sebastian Ullrich (Mar 10 2018 at 22:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewrite%20occs/near/123547208):
<p>It's been that way since Lean 2, where it was even documented afair :)</p>

#### [ Scott Morrison (Mar 10 2018 at 22:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewrite%20occs/near/123547209):
<p>Okay!</p>

#### [ Scott Morrison (Mar 10 2018 at 22:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewrite%20occs/near/123547210):
<p>Looks like I will think about a really slow version of kabstract!</p>

#### [ Scott Morrison (Mar 10 2018 at 22:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewrite%20occs/near/123547259):
<p>(Context here is that I'm otherwise really happy with my <code>rewrite_search</code> tactic, based on greedily minimising edit distance. I have "real" examples where it successfully finds long (~10) chains of rewrites that complete a proof. Unfortunately sometimes it mysteriously fails, and this seems to be the issue.)</p>

#### [ Sebastian Ullrich (Mar 10 2018 at 22:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewrite%20occs/near/123547262):
<p>It's not even clear to me what a different <code>kabstract</code> would look like. Would it introduce <code>n</code> lambdas and return <code>n</code> instantiated copies of <code>e</code>?</p>

#### [ Sebastian Ullrich (Mar 10 2018 at 22:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewrite%20occs/near/123547305):
<p><span class="user-mention" data-user-id="110524">@Scott Morrison</span> I suppose repeatedly rewriting will not solve your problem? :)</p>

#### [ Scott Morrison (Mar 10 2018 at 22:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewrite%20occs/near/123547311):
<p>No -- I have lots of examples where the rewrite rule needs to be applied "inside" a bigger expression where the rewrite rule also applies.</p>

#### [ Scott Morrison (Mar 10 2018 at 22:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewrite%20occs/near/123547312):
<p>But after you do the outer rewrite the inner rewrite is no longer available.</p>

#### [ Scott Morrison (Mar 10 2018 at 22:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewrite%20occs/near/123547354):
<p>(<code>rewrite_search</code> is already trying repeated rewrites itself: I only discovered this problem because it was mysteriously failing.)</p>

#### [ Kevin Buzzard (Mar 10 2018 at 22:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewrite%20occs/near/123547355):
<p>Scott -- has Mario made any suggestions on how to deal with your issues?</p>

#### [ Scott Morrison (Mar 10 2018 at 22:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewrite%20occs/near/123547357):
<p>Kevin -- I only raised this about 5 minutes ago, perhaps Mario is sleeping. :-)</p>

#### [ Scott Morrison (Mar 10 2018 at 22:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewrite%20occs/near/123547414):
<p><span class="user-mention" data-user-id="110024">@Sebastian Ullrich</span>, I guess I was thinking not actually to reimplement <code>kabstract</code>, but reimplement all of <code>rewrite_core</code>.</p>

#### [ Scott Morrison (Mar 10 2018 at 22:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewrite%20occs/near/123547416):
<p>(Reimplementing <code>kabstract</code> in Lean would not be helpful, because no tactics actually call it from Lean: only things in c++.)</p>

#### [ Sebastian Ullrich (Mar 10 2018 at 22:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewrite%20occs/near/123547458):
<p>I'm not sure how you want to solve your issue with the current kabstract</p>

#### [ Scott Morrison (Mar 10 2018 at 22:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewrite%20occs/near/123547464):
<p>Or rather, to write something called <code>all_rewrites</code>, that takes an expr, and a list of lemmas, and returns <code>list (expr \times expr)</code>, where the pairs are the result of using the lemma in one place, and the proof.</p>

#### [ Scott Morrison (Mar 10 2018 at 22:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewrite%20occs/near/123547505):
<p>It would work by recursively going down into the expr, and repeatedly calling unify ... oh, I see your point.</p>

#### [ Scott Morrison (Mar 10 2018 at 22:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewrite%20occs/near/123547509):
<p>Those calls to unify are _also_ going to be cached. :-(</p>

#### [ Scott Morrison (Mar 10 2018 at 22:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewrite%20occs/near/123547511):
<p>This is terrible. :-)</p>

#### [ Sebastian Ullrich (Mar 10 2018 at 22:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewrite%20occs/near/123547518):
<p>Well, not if you create new mvars like Simon suggested</p>

#### [ Scott Morrison (Mar 10 2018 at 22:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewrite%20occs/near/123547524):
<p>I see; after every time you successfully find a match, you throw out the mvar you were passing to unify and make a new one.</p>

#### [ Scott Morrison (Mar 10 2018 at 22:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewrite%20occs/near/123547566):
<p>(Thanks, Simon, sorry I was slow to understand exactly what you meant.)</p>

#### [ Simon Hudon (Mar 10 2018 at 22:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewrite%20occs/near/123547580):
<p>No worries</p>

#### [ Kevin Buzzard (Mar 10 2018 at 22:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewrite%20occs/near/123547635):
<blockquote>
<p>Kevin -- I only raised this about 5 minutes ago, perhaps Mario is sleeping. :-)</p>
</blockquote>
<p>Oh -- I knew that you had been discussing with Mario about what looked like a major refactoring job on the category theory library and I was just kind of assumed this might be something to do with the refactoring</p>

#### [ Simon Hudon (Mar 10 2018 at 22:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewrite%20occs/near/123547638):
<p>I believe in rewrite, when you use <code>∀ x, f x = g x</code> as your rewrite rule, you generate one mvar to instantiate x and you start matching. What you can do instead is create a unique local constant to instantiate x with (or as many as you have bound variable) and you create a table mapping those constants to mvars every time you attempt a match</p>

#### [ Sebastian Ullrich (Mar 10 2018 at 23:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewrite%20occs/near/123547691):
<p>Btw, it might be easier to build something on top of <code>tactic.ext_simplify_core</code>. You basically get a very configurable term DFS where you can return subterm equality proofs pre or post visit and the tactic takes care of composing them into the complete proof.</p>

#### [ Scott Morrison (Mar 10 2018 at 23:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewrite%20occs/near/123547692):
<p>Hmm... okay, on the 3rd reading I still don't understand that. :-) (Simon's comment about local constants.)</p>

#### [ Mario Carneiro (Mar 10 2018 at 23:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewrite%20occs/near/123547704):
<p>I don't have any good suggestions for your rewrite issue. One possibility is to use <code>conv</code> or <code>ext_simplify_core</code> to recurse into all subterms and try <code>rw</code> on each of them</p>

#### [ Kevin Buzzard (Mar 10 2018 at 23:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewrite%20occs/near/123547744):
<p>How do I do a rw in conv, by the way?</p>

#### [ Scott Morrison (Mar 10 2018 at 23:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewrite%20occs/near/123547745):
<p>I don't actually know how <code>conv</code> is implemented under the hood: is it using <code>ext_simplify_core</code> anyway?</p>

#### [ Kevin Buzzard (Mar 10 2018 at 23:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewrite%20occs/near/123547746):
<p>I don't mean a rw, I mean I want to replace something with something defeq</p>

#### [ Kevin Buzzard (Mar 10 2018 at 23:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewrite%20occs/near/123547750):
<p>do I have to use whnf?</p>

#### [ Scott Morrison (Mar 10 2018 at 23:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewrite%20occs/near/123547756):
<p>I really like these ideas. It hadn't occurred to me that I could think of <code>conv</code> as letting me recurse into all subterms in tactic mode.</p>

#### [ Kevin Buzzard (Mar 10 2018 at 23:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewrite%20occs/near/123547798):
<p>I only just learnt how it worked really, it's all because of this push by Patrick to get some informal docs written.</p>

#### [ Kevin Buzzard (Mar 10 2018 at 23:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewrite%20occs/near/123547799):
<p>I find them really enlightening</p>

#### [ Scott Morrison (Mar 10 2018 at 23:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewrite%20occs/near/123547800):
<p>Is there any hope that I could build a pattern corresponding to the lhs of my rewrite rule, and pass that to <code>conv</code>, and thereby only visit the places where <code>rw</code> would work anyway? Or would this run into exactly the same unification caching problem?</p>

#### [ Scott Morrison (Mar 10 2018 at 23:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewrite%20occs/near/123547916):
<p>Okay, answering my own question: no, you can't pass patterns to conv, it does indeed run into this same problem.</p>

#### [ Scott Morrison (Mar 10 2018 at 23:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewrite%20occs/near/123548005):
<p><span class="user-mention" data-user-id="110038">@Kevin Buzzard</span>, here are two examples of using <code>rw</code> inside <code>conv</code>, solving the problem I started this thread with:</p>
<div class="codehilite"><pre><span></span><span class="kn">example</span> <span class="o">:</span> <span class="o">[</span><span class="mi">1</span><span class="o">,</span> <span class="mi">1</span><span class="o">,</span> <span class="mi">2</span><span class="o">]</span> <span class="bp">=</span> <span class="o">[</span><span class="mi">2</span><span class="o">,</span> <span class="mi">1</span><span class="o">,</span> <span class="mi">2</span><span class="o">]</span> <span class="o">:=</span>
<span class="k">begin</span>
<span class="n">conv</span> <span class="o">{</span> <span class="n">congr</span><span class="o">,</span> <span class="n">rw</span> <span class="o">[</span><span class="n">baz</span><span class="o">]</span> <span class="o">},</span>
<span class="kn">end</span>
<span class="kn">example</span> <span class="o">:</span> <span class="o">[</span><span class="mi">1</span><span class="o">,</span> <span class="mi">1</span><span class="o">,</span> <span class="mi">2</span><span class="o">]</span> <span class="bp">=</span> <span class="o">[</span><span class="mi">1</span><span class="o">,</span> <span class="mi">2</span><span class="o">,</span> <span class="mi">2</span><span class="o">]</span> <span class="o">:=</span>
<span class="k">begin</span>
<span class="n">conv</span> <span class="o">{</span> <span class="n">congr</span><span class="o">,</span> <span class="n">congr</span><span class="o">,</span> <span class="n">skip</span><span class="o">,</span> <span class="n">rw</span> <span class="o">[</span><span class="n">baz</span><span class="o">]</span> <span class="o">},</span>
<span class="kn">end</span>
</pre></div>

#### [ Scott Morrison (Mar 10 2018 at 23:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewrite%20occs/near/123548103):
<p>I think in the end <code>ext_simplify_core</code> is going to be the right solution. Since I want to build up a list of all the possible rewrites, I think it makes sense to build it up during the run of <code>ext_simplify_core</code>, rather than making multiple calls into conv, each one looking at a different piece of the expression.</p>

#### [ Scott Morrison (Mar 10 2018 at 23:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewrite%20occs/near/123548109):
<p>(Please tell me if that doesn't make sense!)</p>

#### [ Scott Morrison (Mar 10 2018 at 23:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewrite%20occs/near/123548158):
<p>Thank you, everyone, for the extremely helpful suggestions, as usual!</p>

#### [ Simon Hudon (Mar 10 2018 at 23:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewrite%20occs/near/123548204):
<p>Thanks for the interesting challenges <span class="emoji emoji-1f604" title="smile">:smile:</span></p>

#### [ Kevin Buzzard (Mar 10 2018 at 23:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewrite%20occs/near/123548272):
<p>I don't even understand what this thread is about. What is ematch? Did someone write some informal docs yet?</p>

#### [ Kevin Buzzard (Mar 10 2018 at 23:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewrite%20occs/near/123548304):
<p>I really find life easier with docs. Then I have to ask fewer questions.</p>

#### [ Mario Carneiro (Mar 10 2018 at 23:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewrite%20occs/near/123548319):
<p>I don't think the ematch attribute is relevant to simon's example</p>

#### [ Andrew Ashworth (Mar 10 2018 at 23:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewrite%20occs/near/123548415):
<p>ematch: you can try reading Leo's paper.... <a href="https://link.springer.com/chapter/10.1007/978-3-540-73595-3_13" target="_blank" title="https://link.springer.com/chapter/10.1007/978-3-540-73595-3_13">https://link.springer.com/chapter/10.1007/978-3-540-73595-3_13</a></p>

#### [ Andrew Ashworth (Mar 10 2018 at 23:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewrite%20occs/near/123548456):
<p>it's a little arcane unless you're really into the theory though</p>

#### [ Andrew Ashworth (Mar 10 2018 at 23:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewrite%20occs/near/123548570):
<p>aha! something better: <a href="http://yices.csl.sri.com/papers/cav2007.pdf" target="_blank" title="http://yices.csl.sri.com/papers/cav2007.pdf">http://yices.csl.sri.com/papers/cav2007.pdf</a></p>

#### [ Andrew Ashworth (Mar 10 2018 at 23:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewrite%20occs/near/123548609):
<p>seems the root paper at the bottom of all this is something from the 80s: <a href="https://people.eecs.berkeley.edu/~necula/Papers/nelson-thesis.pdf" target="_blank" title="https://people.eecs.berkeley.edu/~necula/Papers/nelson-thesis.pdf">https://people.eecs.berkeley.edu/~necula/Papers/nelson-thesis.pdf</a></p>

#### [ Andrew Ashworth (Mar 10 2018 at 23:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewrite%20occs/near/123548657):
<p>that said, i'm not volunteering to read everything, digest it, and then write a simple introduction to ematch :)</p>

#### [ Kevin Buzzard (Mar 11 2018 at 12:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewrite%20occs/near/123567801):
<p>Oh thanks! I honestly behave like a computer. I looked at what Scott had posted, didn't understand the first word (ematch) and then just crashed and stopped reading (I was trying to get three kids to bed as well as reading chat). I see that this thread is well within my grasp now. Sorry for earlier noise.</p>

#### [ Kevin Buzzard (Mar 11 2018 at 12:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewrite%20occs/near/123567891):
<p>So Scott what are you actually trying to do in the long run here? What is the problem with just writing a tactic which tries every possible rw on some term using some set of terms which are equalities but with metavariables? Is that what you want? Isn't that exactly the sort of thing one can write a tactic for? Or is the point that you want to do it without writing a tactic?</p>

#### [ Kevin Buzzard (Mar 11 2018 at 13:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewrite%20occs/near/123568038):
<p>And a related question. Is Sebastian saying "there is something written in C++ which doesn't do what you want, but you could write a version in Lean which does do what you want but it would be slow"? And how does this contrast with Leo's Lean 4 plan -- goal <a href="https://github.com/leanprover/lean/issues/1" target="_blank" title="https://github.com/leanprover/lean/issues/1">#1</a> in fact -- of taking some stuff out of C++ and implementing it in Lean?</p>

#### [ Kevin Buzzard (Mar 11 2018 at 13:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewrite%20occs/near/123568039):
<p>How can this ever be a good idea? I don't understand the ramifications of this idea</p>

#### [ Kevin Buzzard (Mar 11 2018 at 13:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewrite%20occs/near/123568138):
<p>(deleted)</p>

#### [ Gabriel Ebner (Mar 11 2018 at 13:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewrite%20occs/near/123568224):
<p>In Lean 4 it would be fast because you could compile it to C++ that runs as fast as the current kabstract code.</p>

#### [ Simon Hudon (Mar 11 2018 at 20:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewrite%20occs/near/123579238):
<p>How will that work? Will Lean run the definitions of the current file in the VM and at the end compile the whole file to C++ to accelerate the verification of the next files?</p>

#### [ Kevin Buzzard (Mar 11 2018 at 21:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewrite%20occs/near/123580122):
<blockquote>
<p>I don't mean a rw, I mean I want to replace something with something defeq</p>
</blockquote>
<p>ooh I can use change.</p>

#### [ Kevin Buzzard (Mar 11 2018 at 21:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewrite%20occs/near/123580123):
<div class="codehilite"><pre><span></span>theorem H3 : 3 + 2 = 1 + 4 := begin
conv begin
to_lhs,
change 1 + 4,
end
end
</pre></div>

#### [ Patrick Massot (Mar 11 2018 at 21:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewrite%20occs/near/123580178):
<p>Great! Do you have a slightly more realistic example?</p>

#### [ Kevin Buzzard (Mar 11 2018 at 21:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewrite%20occs/near/123580181):
<p>I did have the other day!</p>

#### [ Patrick Massot (Mar 11 2018 at 21:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewrite%20occs/near/123580183):
<p>(not necessarily super realistic, like the ones I put in the conv doc)</p>

#### [ Kevin Buzzard (Mar 11 2018 at 21:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewrite%20occs/near/123580184):
<p>I had a goal of the form <code>X=Y</code> but <code>Y</code> had terms in it of the form <code>\&lt;a,_\&gt;</code></p>

#### [ Kevin Buzzard (Mar 11 2018 at 21:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewrite%20occs/near/123580228):
<p>so I couldn't use show to replace X on LHS with something defeq because cut and paste wouldn't work for RHS. So I used conv and then realised I didn't know how to do show in conv mode and ended proving some auxiliary lemma with rfl and doing a rw. This way is much cooler :-)</p>

#### [ Kevin Buzzard (Mar 11 2018 at 21:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewrite%20occs/near/123580229):
<p>I was going to update the conv doc myself but then I realised you owned it rather than mathlib</p>

#### [ Patrick Massot (Mar 11 2018 at 21:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewrite%20occs/near/123580231):
<p>What?</p>

#### [ Patrick Massot (Mar 11 2018 at 21:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewrite%20occs/near/123580236):
<p>I don't own anything here</p>

#### [ Patrick Massot (Mar 11 2018 at 21:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewrite%20occs/near/123580237):
<p>My PR was merged into mathlib</p>

#### [ Patrick Massot (Mar 11 2018 at 21:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewrite%20occs/near/123580238):
<p>Please feel super free to update it</p>

#### [ Kevin Buzzard (Mar 11 2018 at 21:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewrite%20occs/near/123580277):
<p>wait I can't find it anywhere</p>

#### [ Patrick Massot (Mar 11 2018 at 21:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewrite%20occs/near/123580279):
<p><a href="https://github.com/leanprover/mathlib/blob/master/docs/extras/conv.md" target="_blank" title="https://github.com/leanprover/mathlib/blob/master/docs/extras/conv.md">https://github.com/leanprover/mathlib/blob/master/docs/extras/conv.md</a></p>

#### [ Patrick Massot (Mar 11 2018 at 21:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewrite%20occs/near/123580280):
<p>or follow links from the main README</p>

#### [ Patrick Massot (Mar 11 2018 at 21:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewrite%20occs/near/123580282):
<p>Starting with link "extra Lean documentation"</p>

#### [ Kevin Buzzard (Mar 11 2018 at 21:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewrite%20occs/near/123580283):
<p>maybe I don't understand git. I thought I just pulled</p>

#### [ Kevin Buzzard (Mar 11 2018 at 21:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewrite%20occs/near/123580290):
<p>oh maybe I really don't understand git. I am pulling from my own fork not from mathlib</p>

#### [ Patrick Massot (Mar 11 2018 at 21:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewrite%20occs/near/123580291):
<p>(because it's no about mathlib)</p>

#### [ Patrick Massot (Mar 11 2018 at 21:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewrite%20occs/near/123580294):
<p>Do you have a git remote pointing to the main repo?</p>

#### [ Patrick Massot (Mar 11 2018 at 21:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewrite%20occs/near/123580295):
<p><code>git add remote upstream https://github.com/leanprover/mathlib.git</code></p>

#### [ Kevin Buzzard (Mar 11 2018 at 21:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewrite%20occs/near/123580296):
<div class="codehilite"><pre><span></span>$ git remote -v
leanprover  https://github.com/leanprover/mathlib.git (fetch)
leanprover  https://github.com/leanprover/mathlib.git (push)
origin  git@github.com:kbuzzard/mathlib.git (fetch)
origin  git@github.com:kbuzzard/mathlib.git (push)
</pre></div>

#### [ Kevin Buzzard (Mar 11 2018 at 21:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewrite%20occs/near/123580338):
<p>I need to pull harder somehow</p>

#### [ Kevin Buzzard (Mar 11 2018 at 21:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewrite%20occs/near/123580342):
<p>I am only pulling from origin</p>

#### [ Patrick Massot (Mar 11 2018 at 21:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewrite%20occs/near/123580343):
<p>Then <code>git pull leanprover master</code></p>

#### [ Patrick Massot (Mar 11 2018 at 21:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewrite%20occs/near/123580344):
<p>you called leanprover what is traditionnaly called "upstream"</p>

#### [ Kevin Buzzard (Mar 11 2018 at 21:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewrite%20occs/near/123580347):
<p>great, I now have extras.</p>

#### [ Patrick Massot (Mar 11 2018 at 21:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewrite%20occs/near/123580358):
<p>Now <code>git checkout -b docs-conv-change</code></p>

#### [ Patrick Massot (Mar 11 2018 at 21:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewrite%20occs/near/123580399):
<p>Do your modifications, <code>git commit -a</code>, <code>git push</code>. Then git will complain and tell you what to type instead of <code>git push</code></p>

#### [ Patrick Massot (Mar 11 2018 at 21:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewrite%20occs/near/123580400):
<p>(with <code>git push set-upstream</code> in it)</p>

#### [ Kevin Buzzard (Mar 11 2018 at 21:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewrite%20occs/near/123580401):
<p>why won't it just push to my fork?</p>

#### [ Patrick Massot (Mar 11 2018 at 21:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewrite%20occs/near/123580404):
<p>then go to either upstream mathlib or your fork on Github and you'll be invited to open a PR</p>

#### [ Patrick Massot (Mar 11 2018 at 21:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewrite%20occs/near/123580410):
<p>Because it's a new branch</p>

#### [ Patrick Massot (Mar 11 2018 at 21:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewrite%20occs/near/123580411):
<p>a branch that is not on github yet</p>

#### [ Patrick Massot (Mar 11 2018 at 21:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewrite%20occs/near/123580412):
<p>(yeah, the word upstream is used in a slightly different sense in <code>set-upstream</code>)</p>

#### [ Kevin Buzzard (Mar 11 2018 at 21:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewrite%20occs/near/123580639):
<p>git push just pushed to my fork</p>

#### [ Patrick Massot (Mar 11 2018 at 21:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewrite%20occs/near/123580640):
<p>yes</p>

#### [ Patrick Massot (Mar 11 2018 at 21:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewrite%20occs/near/123580642):
<p>now you can PR</p>

#### [ Patrick Massot (Mar 11 2018 at 21:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewrite%20occs/near/123580648):
<p>except that you skipped creating a new branch...</p>

#### [ Kevin Buzzard (Mar 11 2018 at 21:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewrite%20occs/near/123580649):
<p>yeah :-/</p>

#### [ Patrick Massot (Mar 11 2018 at 21:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewrite%20occs/near/123580650):
<p>This is bad</p>

#### [ Kevin Buzzard (Mar 11 2018 at 21:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewrite%20occs/near/123580651):
<p>oh :-)</p>

#### [ Patrick Massot (Mar 11 2018 at 21:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewrite%20occs/near/123580701):
<p>You can't have several open PR with this non-branching strategy</p>

#### [ Kevin Buzzard (Mar 11 2018 at 21:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewrite%20occs/near/123580702):
<p>I have loads of my own WIPs all with no branch either.</p>

#### [ Kevin Buzzard (Mar 11 2018 at 21:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewrite%20occs/near/123580704):
<p>I will google and sort it out. Let's not spam here.</p>

#### [ Patrick Massot (Mar 11 2018 at 21:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewrite%20occs/near/123580712):
<p>Then you can't even PR since it would PR the WIP at the same time</p>

#### [ Kevin Buzzard (Mar 12 2018 at 08:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewrite%20occs/near/123597942):
<p>Hmm. I can't deal with Mario's comments on my docs because travis hasn't finished building.</p>

#### [ Mario Carneiro (Mar 12 2018 at 08:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewrite%20occs/near/123598291):
<p>I think you can more or less ignore travis builds for a doc change</p>

#### [ Patrick Massot (Mar 12 2018 at 08:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewrite%20occs/near/123598331):
<p>Quoting Mario for <span class="user-mention" data-user-id="110038">@Kevin Buzzard</span> </p>
<blockquote>
<p>Re: PRs, I'm okay with docs of any kind. My recommendation is to try to write them with an authoritative locution style; I will let you know if you say false things. If you don't know something, leave it out, say you don't know in the doc, or ask about it here and then put in whatever you find out.</p>
</blockquote>

#### [ Mario Carneiro (Mar 12 2018 at 08:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewrite%20occs/near/123598341):
<p>(Of course, there is no guarantee that your PR won't (apparently) "break the build", since our current peculiar setup that pulls from a moving target lean nightly means that if Leo decides to break mathlib at the same time your PR will get the blame.)</p>

#### [ Patrick Massot (Mar 12 2018 at 08:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewrite%20occs/near/123598348):
<p>I think you could edit a few sentences to conform to this recommendation</p>

#### [ Mario Carneiro (Mar 12 2018 at 08:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewrite%20occs/near/123598385):
<p>I tried to respond to Kevin's parentheticals in the PR comments, so hopefully they will be addressed in the next revision</p>


{% endraw %}
