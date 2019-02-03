---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/35960VariousVMquestions.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [Various VM questions](https://leanprover-community.github.io/archive/113488general/35960VariousVMquestions.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Neil Strickland (Dec 06 2018 at 12:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Various%20VM%20questions/near/150999916):
<p>I have been working on several different approaches to partitions of finite sets and other finite combinatorial structures.  I would like to do things in such a way that the VM can compute with examples that are moderately large.  For this I would like to understand better how the VM works and what it can do.  I have not managed to find any relevant documentation, but I have looked a little bit at the VM-related source code.</p>
<ul>
<li>Is there any documentation that I have not found?</li>
<li>Is there a way to get Lean to print information about what the VM can do with a given definition?</li>
<li>Any comments or corrections on the following?</li>
<li>It seems best to do serious computation with partitions of <code>fin n</code>, and then set things up so that one can deal with partitions of a general fintype by using an equivalence with <code>fin n</code>.</li>
<li>It looks like the VM will deal efficiently with <code>fin n</code> but not with <code>fin2 n</code>.  On the other hand, if you were willing to add stuff to the lean core, it looks like you could easily implement an efficient VM version of fin2.</li>
<li>It looks like it is probably efficient to work with the quotient of a simple type by a complicated equivalence relation,  because the complexity is all hidden in Props which are erased by the VM. </li>
<li>It looks like the VM cannot handle <code>fin n -&gt; X</code> efficiently, but should be happy with <code>list X</code> or <code>array n X</code></li>
<li>The VM has support for <code>rb_map</code>.  It is not clear to me whether this only comes into play if you use <code>rb_map</code> explicitly, or whether it some how gets used for other kinds of structures.</li>
</ul>

#### [ Bryan Gin-ge Chen (Dec 06 2018 at 17:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Various%20VM%20questions/near/151021786):
<p>This doesn't address any of your questions about the VM, but regarding partitions of finite sets, <span class="user-mention" data-user-id="110049">@Mario Carneiro</span>  <a href="#narrow/stream/113488-general/subject/tutorial/near/135302235" title="#narrow/stream/113488-general/subject/tutorial/near/135302235">suggested a more efficient recursive approach to enumeration</a> than the one I took in the tutorial branch. Perhaps this is already something you've done though.</p>

#### [ Mario Carneiro (Dec 06 2018 at 18:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Various%20VM%20questions/near/151022735):
<p>1. There isn't too much documentation about the VM, although for basic use it's quite simple: just use <code>#eval</code> and the VM runs any lean function.<br>
2. Lean can evaluate any definition that is not marked <code>noncomputable</code> (which is a really obvious and required marking on any definition).<br>
3. ...<br>
4. That's debatable. Working over arbitrary types also means working parametrically in the data representation, abstracting away the details like the reason why a type is finite. What representation is "best" depends on the application.<br>
5. This is true. <code>fin2 n</code> will be a linked list of pointers, and <code>fin n</code> will be a number stored as a 32 bit integer if it is small enough. The recommended approach here is to put together VM primitive types to get the data representation you would like - a type describes its data representation, so if you want a different representation you need a different type.<br>
6. This is true. A quotient is represented using the underlying type, with the relation appearing nowhere. It is a zero cost abstraction. However, depending on what you want to do with the relation this may not be a good thing. For example you can't easily enumerate the elements of a quotient type unless you know something about the relation. It is a tool in the box, but its usefulness depends on the application.<br>
7. This is also application dependent. A <code>fin n -&gt; X</code> is a function that takes a number and returns a value in <code>X</code>. A <code>list X</code> is a linked list of values of type <code>X</code>. An <code>array n X</code> is a literal array in memory whose elements have type <code>X</code>. They all have their own performance characteristics, and it isn't too hard to guess what they are, roughly.<br>
8. The VM has support for several <code>meta</code> data structures beyond <code>rb_map</code>, such as <code>tactic_state</code>, <code>expr</code>, <code>environment</code> and so on. There is a non-meta version of <code>rb_map</code>, called <code>rbmap</code>, which has no special support. I think the sense is that it wasn't really necessary to implement <code>rb_map</code> as a C data structure when lean can do it well enough. Not counting <code>meta</code> data structures, the only types/functions with native support are <code>nat</code>, <code>int</code>, <code>array</code> and <code>quot</code> (maybe I'm forgetting something but I'm sure others will point it out).</p>

#### [ Scott Morrison (Dec 06 2018 at 21:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Various%20VM%20questions/near/151041032):
<p>... and perhaps in this context it's worth mentioning that everything will likely be different when Lean 4 arrives <span class="emoji emoji-1f340" title="four leaf clover">:four_leaf_clover:</span> .</p>


{% endraw %}
