---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/91947namespacedesignissuesvspedagogy.html
---

## Stream: [general](index.html)
### Topic: [namespace design issues vs. pedagogy](91947namespacedesignissuesvspedagogy.html)

---


{% raw %}
#### [ Kevin Sullivan (Aug 03 2018 at 15:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/namespace%20design%20issues%20vs.%20pedagogy/near/130837483):
<p>The context for the following is an effort to use Lean in teaching a lower-level undergraduate course. Students are easily confused. I'm trying to use namespaces in the usual way so that we can recapitulate the definitions of built-in types, such as bool, without getting name conflicts. It "works", but in the course of figuring out the details, I noted some inconsistencies that I myself found confusing and that students are likely to find confusing, too. I comment the code. The key lines are marked AAA through EEE.</p>
<p>In the outer environment I define a type, bar, with constructors p and q, and open its namespace. This models the built-in type, bool, the namespace of which is open by default. Then I define a namespace, foo. Within foo, I define bar again, in the same way. Everything else occurs within the foo namespace.</p>
<p>Inconsistency <a href="https://github.com/leanprover/lean/issues/1" target="_blank" title="https://github.com/leanprover/lean/issues/1">#1</a>: In the command "#check bar", on the line marked (AAA), bar is interpreted as referring to foo.bar (as the little equality claim proves); but if you issue the command "open bar" (BBB), bar is interpreted as referring to _root_.bar (so the open command has no effect, as the _root_.bar namespace is already open). The same identifier is thus interpreted in two different ways in the same environment. This is kind of confusing and will be hard to explain to new students in CS.</p>
<p>Inconsistency <a href="https://github.com/leanprover/lean/issues/2" target="_blank" title="https://github.com/leanprover/lean/issues/2">#2</a>: If you now open foo.bar, then you end up with two definitions of the constructor p. Not unexpectedly, you get error messages flagging an "ambiguous interpretation" in both the command, "#check p", at line (CCC) and in the statement of a simple theorem on line (DDD). Uncomment those two lines to see the error. And yet, when p is used as an argument to a function (line EEE), no ambiguity is flagged; rather it's resolved in favor of foo.bar.p from the inner namespace. So once again the same<br>
identifier is interpreted inconsistently in the same environment. Again, explaining that is p flagged as erroneous when used in the statement of a theorem or in a #check command but not when used as an argument to a function will tend to confuse my students.</p>
<p>Is there a compelling reason for these behaviors? If so, can you briefly explain? If not, perhaps they can be fixed in some near future version?</p>
<p>== the code ==</p>
<p>inductive bar : Type<br>
| p : bar<br>
| q : bar<br>
open bar</p>
<p>#check bar<br>
#check p</p>
<p>namespace foo</p>
<p>inductive bar : Type<br>
| p : bar<br>
| q : bar</p>
<p>#check bar -- bar here refers to foo.bar (AAA)<br>
theorem t1 : bar = foo.bar := rfl<br>
#check p -- as expected, p still refers to _root_.bar.p<br>
theorem t2 : p = _root_.bar.p := rfl</p>
<p>open bar -- bar here refers to _root_.bar! (BBB)</p>
<p>#check bar -- bar still refers to foo.bar<br>
theorem t3 : bar = foo.bar := rfl<br>
#check p -- p still refers to _root_.bar.p<br>
theorem t4 : p = _root_.bar.p := rfl</p>
<p>open foo.bar -- need to use qualified name to open namespace<br>
#check bar -- bar still refers to foo.bar<br>
theorem t5 : bar = foo.bar := rfl <br>
--#check p     -- p is now ambiguous (CCC)<br>
--theorem t6 : p = _root_.bar.p := rfl    -- p is ambiguous (DDD)</p>
<p>def id(a: bar): bar := a</p>
<p>#check id p -- but in this expression, p is not ambiguous (EEE)</p>
<p>end foo</p>

#### [ Johan Commelin (Aug 03 2018 at 15:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/namespace%20design%20issues%20vs.%20pedagogy/near/130837541):
<p>Kevin, you can use three backticks around your code to create a codeblock. If you write "lean" after the first set of backticks you get syntax highlighting! Like so</p>
<div class="codehilite"><pre><span></span>```lean
&lt;your code&gt;
-- nesting backticks is hard... somehow there are 4 backticks below. There should be only 3.
````
</pre></div>

#### [ Kevin Sullivan (Aug 03 2018 at 15:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/namespace%20design%20issues%20vs.%20pedagogy/near/130837550):
<blockquote>
<p>The context for the following is an effort to use Lean in teaching a lower-level undergraduate course. Students are easily confused. I'm trying to use namespaces in the usual way so that we can recapitulate the definitions of built-in types, such as bool, without getting name conflicts. It "works", but in the course of figuring out the details, I noted some inconsistencies that I myself found confusing and that students are likely to find confusing, too. I comment the code. The key lines are marked AAA through EEE.</p>
<p>In the outer environment I define a type, bar, with constructors p and q, and open its namespace. This models the built-in type, bool, the namespace of which is open by default. Then I define a namespace, foo. Within foo, I define bar again, in the same way. Everything else occurs within the foo namespace.</p>
<p>Inconsistency <a href="https://github.com/leanprover/lean/issues/1" target="_blank" title="https://github.com/leanprover/lean/issues/1">#1</a>: In the command "#check bar", on the line marked (AAA), bar is interpreted as referring to foo.bar (as the little equality claim proves); but if you issue the command "open bar" (BBB), bar is interpreted as referring to _root_.bar (so the open command has no effect, as the _root_.bar namespace is already open). The same identifier is thus interpreted in two different ways in the same environment. This is kind of confusing and will be hard to explain to new students in CS.</p>
<p>Inconsistency <a href="https://github.com/leanprover/lean/issues/2" target="_blank" title="https://github.com/leanprover/lean/issues/2">#2</a>: If you now open foo.bar, then you end up with two definitions of the constructor p. Not unexpectedly, you get error messages flagging an "ambiguous interpretation" in both the command, "#check p", at line (CCC) and in the statement of a simple theorem on line (DDD). Uncomment those two lines to see the error. And yet, when p is used as an argument to a function (line EEE), no ambiguity is flagged; rather it's resolved in favor of foo.bar.p from the inner namespace. So once again the same<br>
identifier is interpreted inconsistently in the same environment. Again, explaining that is p flagged as erroneous when used in the statement of a theorem or in a #check command but not when used as an argument to a function will tend to confuse my students.</p>
<p>Is there a compelling reason for these behaviors? If so, can you briefly explain? If not, perhaps they can be fixed in some near future version?</p>
<p>== the code ==</p>
<p>inductive bar : Type<br>
| p : bar<br>
| q : bar<br>
open bar</p>
<p>#check bar<br>
#check p</p>
<p>namespace foo</p>
<p>inductive bar : Type<br>
| p : bar<br>
| q : bar</p>
<p>#check bar -- bar here refers to foo.bar (AAA)<br>
theorem t1 : bar = foo.bar := rfl<br>
#check p -- as expected, p still refers to _root_.bar.p<br>
theorem t2 : p = _root_.bar.p := rfl</p>
<p>open bar -- bar here refers to _root_.bar! (BBB)</p>
<p>#check bar -- bar still refers to foo.bar<br>
theorem t3 : bar = foo.bar := rfl<br>
#check p -- p still refers to _root_.bar.p<br>
theorem t4 : p = _root_.bar.p := rfl</p>
<p>open foo.bar -- need to use qualified name to open namespace<br>
#check bar -- bar still refers to foo.bar<br>
theorem t5 : bar = foo.bar := rfl <br>
--#check p     -- p is now ambiguous (CCC)<br>
--theorem t6 : p = _root_.bar.p := rfl    -- p is ambiguous (DDD)</p>
<p>def id(a: bar): bar := a</p>
<p>#check id p -- but in this expression, p is not ambiguous (EEE)</p>
<p>end foo</p>
</blockquote>
<p>Ok, I guess in case <a href="https://github.com/leanprover/lean/issues/2" target="_blank" title="https://github.com/leanprover/lean/issues/2">#2</a>, type inference is resolving the type of p. What about the first inconsistency?</p>

#### [ Kevin Sullivan (Aug 03 2018 at 15:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/namespace%20design%20issues%20vs.%20pedagogy/near/130837633):
<blockquote>
<p>Kevin, you can use three backticks around your code to create a codeblock. If you write "lean" after the first set of backticks you get syntax highlighting! Like so</p>
</blockquote>
<div class="codehilite"><pre><span></span><span class="kn">inductive</span> <span class="n">bar</span> <span class="o">:</span> <span class="kt">Type</span>
<span class="bp">|</span> <span class="n">p</span> <span class="o">:</span> <span class="n">bar</span>
<span class="bp">|</span> <span class="n">q</span> <span class="o">:</span> <span class="n">bar</span>
<span class="kn">open</span> <span class="n">bar</span>

<span class="bp">#</span><span class="kn">check</span> <span class="n">bar</span>
<span class="bp">#</span><span class="kn">check</span> <span class="n">p</span>

<span class="kn">namespace</span> <span class="n">foo</span>

<span class="kn">inductive</span> <span class="n">bar</span> <span class="o">:</span> <span class="kt">Type</span>
<span class="bp">|</span> <span class="n">p</span> <span class="o">:</span> <span class="n">bar</span>
<span class="bp">|</span> <span class="n">q</span> <span class="o">:</span> <span class="n">bar</span>

<span class="bp">#</span><span class="kn">check</span> <span class="n">bar</span> <span class="c1">-- bar here refers to foo.bar (AAA)</span>
<span class="kn">theorem</span> <span class="n">t1</span> <span class="o">:</span> <span class="n">bar</span> <span class="bp">=</span> <span class="n">foo</span><span class="bp">.</span><span class="n">bar</span> <span class="o">:=</span> <span class="n">rfl</span>
<span class="bp">#</span><span class="kn">check</span> <span class="n">p</span> <span class="c1">-- as expected, p still refers to _root_.bar.p</span>
<span class="kn">theorem</span> <span class="n">t2</span> <span class="o">:</span> <span class="n">p</span> <span class="bp">=</span> <span class="bp">_</span><span class="n">root_</span><span class="bp">.</span><span class="n">bar</span><span class="bp">.</span><span class="n">p</span> <span class="o">:=</span> <span class="n">rfl</span>

<span class="kn">open</span> <span class="n">bar</span> <span class="c1">-- bar here refers to _root_.bar! (BBB)</span>

<span class="bp">#</span><span class="kn">check</span> <span class="n">bar</span> <span class="c1">-- bar still refers to foo.bar</span>
<span class="kn">theorem</span> <span class="n">t3</span> <span class="o">:</span> <span class="n">bar</span> <span class="bp">=</span> <span class="n">foo</span><span class="bp">.</span><span class="n">bar</span> <span class="o">:=</span> <span class="n">rfl</span>
<span class="bp">#</span><span class="kn">check</span> <span class="n">p</span> <span class="c1">-- p still refers to _root_.bar.p</span>
<span class="kn">theorem</span> <span class="n">t4</span> <span class="o">:</span> <span class="n">p</span> <span class="bp">=</span> <span class="bp">_</span><span class="n">root_</span><span class="bp">.</span><span class="n">bar</span><span class="bp">.</span><span class="n">p</span> <span class="o">:=</span> <span class="n">rfl</span>

<span class="kn">open</span> <span class="n">foo</span><span class="bp">.</span><span class="n">bar</span> <span class="c1">-- need to use qualified name to open namespace</span>
<span class="bp">#</span><span class="kn">check</span> <span class="n">bar</span> <span class="c1">-- bar still refers to foo.bar</span>
<span class="kn">theorem</span> <span class="n">t5</span> <span class="o">:</span> <span class="n">bar</span> <span class="bp">=</span> <span class="n">foo</span><span class="bp">.</span><span class="n">bar</span> <span class="o">:=</span> <span class="n">rfl</span>
<span class="c1">--#check p     -- p is now ambiguous (CCC)</span>
<span class="c1">--theorem t6 : p = _root_.bar.p := rfl    -- p is ambiguous (DDD)</span>

<span class="n">def</span> <span class="n">id</span><span class="o">(</span><span class="n">a</span><span class="o">:</span> <span class="n">bar</span><span class="o">):</span> <span class="n">bar</span> <span class="o">:=</span> <span class="n">a</span>

<span class="bp">#</span><span class="kn">check</span> <span class="n">id</span> <span class="n">p</span> <span class="c1">-- but in this expression, p is not ambiguous (EEE)</span>

<span class="kn">end</span> <span class="n">foo</span>
</pre></div>

#### [ Simon Hudon (Aug 03 2018 at 15:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/namespace%20design%20issues%20vs.%20pedagogy/near/130839743):
<p>I think the take away from AAA through CCC is that when you use <code>open</code> you must fully qualify the name that you use.</p>

#### [ Simon Hudon (Aug 03 2018 at 15:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/namespace%20design%20issues%20vs.%20pedagogy/near/130840086):
<p>This might provide some more helpful details: <a href="https://leanprover.github.io/reference/other_commands.html#namespaces" target="_blank" title="https://leanprover.github.io/reference/other_commands.html#namespaces">https://leanprover.github.io/reference/other_commands.html#namespaces</a></p>

#### [ Kevin Buzzard (Aug 03 2018 at 18:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/namespace%20design%20issues%20vs.%20pedagogy/near/130850440):
<p>I completely agree that this is confusing; I ran into this myself when trying to teach mathematicians how to build <code>nat</code> with its addition etc. I tried to do everything within a namespace but could never get everything to be as straightforward as I wanted. My solution in the end was to simply give up trying to build <code>my_namespace.nat</code> and as you can see at <a href="https://xenaproject.wordpress.com/2017/10/31/building-the-non-negative-integers-from-scratch/" target="_blank" title="https://xenaproject.wordpress.com/2017/10/31/building-the-non-negative-integers-from-scratch/">https://xenaproject.wordpress.com/2017/10/31/building-the-non-negative-integers-from-scratch/</a> I just called them <code>xnat</code> instead (x for xena). I was even super-paranoid and made them in a <code>xena</code> namespace. Now the trick is to make sure nobody opens <code>nat</code> :-) and then I found that my problems had gone away. Within the <code>xena</code> namespace I could define things like <code>add_assoc</code> and because of this pile of preventative measures I could be fairly confident that nobody would be trying to use the default <code>add_assoc</code> later on when proving <code>add_comm</code> or whatever for <code>xnat</code>. You might want to call my solution a workaround, but I took the practical viewpoint that it wasn't my job to teach people about namespaces -- they were mathematicians. You might be in a different situation of course.</p>

#### [ Kevin Buzzard (Aug 03 2018 at 19:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/namespace%20design%20issues%20vs.%20pedagogy/near/130850682):
<p>PS if you start with</p>
<div class="codehilite"><pre><span></span><span class="kn">inductive</span> <span class="n">bar</span> <span class="o">:</span> <span class="kt">Type</span> <span class="mi">7</span>
<span class="bp">|</span> <span class="n">p</span> <span class="o">:</span> <span class="n">bar</span>
<span class="bp">|</span> <span class="n">q</span> <span class="o">:</span> <span class="n">bar</span>
<span class="kn">open</span> <span class="n">bar</span>

<span class="bp">#</span><span class="kn">check</span> <span class="n">bar</span>
<span class="bp">#</span><span class="kn">check</span> <span class="n">p</span>

<span class="kn">namespace</span> <span class="n">foo</span>

<span class="kn">inductive</span> <span class="n">bar</span> <span class="o">:</span> <span class="kt">Type</span> <span class="mi">4</span>
<span class="bp">|</span> <span class="n">p</span> <span class="o">:</span> <span class="n">bar</span>
<span class="bp">|</span> <span class="n">q</span> <span class="o">:</span> <span class="n">bar</span>
</pre></div>


<p>then it's a little easier to figure out which <code>bar</code> is which when you're experimenting ;-)</p>


{% endraw %}
