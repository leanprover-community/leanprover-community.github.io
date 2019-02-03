---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/17620associationlistsfinmap.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [association lists, finmap](https://leanprover-community.github.io/archive/113488general/17620associationlistsfinmap.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Sean Leather (Sep 20 2018 at 08:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/association%20lists%2C%20finmap/near/134290992):
<p>As some people know, I've been working on association lists and finite maps for mathlib (<a href="https://github.com/spl/lean-finmap" target="_blank" title="https://github.com/spl/lean-finmap">https://github.com/spl/lean-finmap</a>). Mario has decided he wants to get it into mathlib soon, so he has started rewriting it in his own fashion (<a href="https://github.com/leanprover-community/mathlib/tree/finmap" target="_blank" title="https://github.com/leanprover-community/mathlib/tree/finmap">https://github.com/leanprover-community/mathlib/tree/finmap</a>). I wanted to open up the discussion to get feedback from anyone else who might be interested.</p>

#### [ Sean Leather (Sep 20 2018 at 09:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/association%20lists%2C%20finmap/near/134291300):
<p>One question is whether there is  the need for a <code>structure</code> to wrap a list without duplicate keys. Mario thinks it might be useful:</p>
<div class="codehilite"><pre><span></span><span class="kn">structure</span> <span class="n">alist</span> <span class="o">(</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">)</span> <span class="o">(</span><span class="n">β</span> <span class="o">:</span> <span class="n">α</span> <span class="bp">→</span> <span class="kt">Type</span> <span class="n">v</span><span class="o">)</span> <span class="o">:</span> <span class="kt">Type</span> <span class="o">(</span><span class="n">max</span> <span class="n">u</span> <span class="n">v</span><span class="o">)</span> <span class="o">:=</span>
<span class="o">(</span><span class="n">val</span> <span class="o">:</span> <span class="n">list</span> <span class="o">(</span><span class="n">sigma</span> <span class="n">β</span><span class="o">))</span>
<span class="o">(</span><span class="n">nd</span> <span class="o">:</span> <span class="n">val</span><span class="bp">.</span><span class="n">knodup</span><span class="o">)</span>
</pre></div>


<p><a href="https://github.com/leanprover-community/mathlib/blob/e5ddd1d4dca984f6d7a77a87a1608b414296208f/data/list/alist.lean" target="_blank" title="https://github.com/leanprover-community/mathlib/blob/e5ddd1d4dca984f6d7a77a87a1608b414296208f/data/list/alist.lean">https://github.com/leanprover-community/mathlib/blob/e5ddd1d4dca984f6d7a77a87a1608b414296208f/data/list/alist.lean</a></p>
<p>I went down this path and found that, given that (a) there are so many useful definitions and theorems regarding lists and (b) the <code>structure</code> is such a thin wrapper, every definition or proof for the <code>structure</code> is simple, it created a large number of really simple statements. Considering that <code>alist</code> is really a list with a property and I believe it is useful to use other list definitions that don't involve this property, I think the <code>alist</code> structure either (a) makes it more difficult to work with the wrapped list or (b) creates the problem of scaling the number of statements about <code>alist</code> to match those already about <code>list</code>.</p>

#### [ Sean Leather (Sep 20 2018 at 09:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/association%20lists%2C%20finmap/near/134291437):
<p>In another way of putting it, you could look at an <code>alist</code> as something unique on its own or you could look at a list  with a property that it has no duplicate keys. In the process of developing my library, I found the latter view much more useful.</p>

#### [ Simon Hudon (Sep 20 2018 at 09:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/association%20lists%2C%20finmap/near/134291494):
<p>Why is latter more useful?</p>

#### [ Sean Leather (Sep 20 2018 at 09:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/association%20lists%2C%20finmap/near/134291573):
<p>On a related note, that's also how I ended up with the <code>finmap</code> <code>structure</code>:</p>
<div class="codehilite"><pre><span></span><span class="kn">structure</span> <span class="n">finmap</span> <span class="o">(</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">)</span> <span class="o">(</span><span class="n">β</span> <span class="o">:</span> <span class="n">α</span> <span class="bp">→</span> <span class="kt">Type</span> <span class="n">v</span><span class="o">)</span> <span class="o">:</span> <span class="kt">Type</span> <span class="o">(</span><span class="n">max</span> <span class="n">u</span> <span class="n">v</span><span class="o">)</span> <span class="o">:=</span>
<span class="o">(</span><span class="n">val</span> <span class="o">:</span> <span class="n">multiset</span> <span class="o">(</span><span class="n">sigma</span> <span class="n">β</span><span class="o">))</span>
<span class="o">(</span><span class="n">nodupkeys</span> <span class="o">:</span> <span class="n">val</span><span class="bp">.</span><span class="n">nodupkeys</span><span class="o">)</span>
</pre></div>


<p><a href="https://github.com/spl/lean-finmap/blob/035f1faa218e47b9f411c4a243900955f4714a56/src/data/finmap.lean#L8-L10" target="_blank" title="https://github.com/spl/lean-finmap/blob/035f1faa218e47b9f411c4a243900955f4714a56/src/data/finmap.lean#L8-L10">https://github.com/spl/lean-finmap/blob/035f1faa218e47b9f411c4a243900955f4714a56/src/data/finmap.lean#L8-L10</a></p>
<p>You could say that this is a similar situation: a <code>finmap</code> is just a <code>multiset</code> with no duplicate keys. However, I found that it's more useful to look at it as a <code>finmap</code> because I didn't find a lot of the other <code>multiset</code> definitions to be very useful for a <code>finmap</code>.</p>

#### [ Sean Leather (Sep 20 2018 at 09:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/association%20lists%2C%20finmap/near/134291591):
<blockquote>
<p>Why is latter more useful?</p>
</blockquote>
<p>The most important reason for me is that I care about the structure of the internal list: <code>nil</code>, <code>cons</code>, <code>append</code>, etc.</p>

#### [ Sean Leather (Sep 20 2018 at 09:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/association%20lists%2C%20finmap/near/134291598):
<p>Also, regarding <code>finmap</code>, I don't care about the structure of the internal <code>multiset</code>.</p>

#### [ Sean Leather (Sep 20 2018 at 09:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/association%20lists%2C%20finmap/near/134291662):
<p>... which makes sense, since a <code>multiset</code> is a <code>quotient</code>.</p>

#### [ Sean Leather (Sep 20 2018 at 09:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/association%20lists%2C%20finmap/near/134291736):
<p><span class="user-mention" data-user-id="110026">@Simon Hudon</span> Thanks for that question, BTW. It gets to a key reason I don't think <code>alist</code> is useful, a reason that hadn't yet come to mind.</p>

#### [ Sean Leather (Sep 20 2018 at 09:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/association%20lists%2C%20finmap/near/134291871):
<p>That is, I found that it was useful to wrap a <code>quotient</code> like <code>multiset</code> in a <code>structure</code> but not that useful to wrap a <code>list</code> in a <code>structure</code> because the structure of the list is important when working with the <code>structure</code>. I ended up creating definitions to wrap <code>nil</code>, <code>cons</code>, <code>append</code>, etc., and all of that already existed for the <code>list</code>, so I came to ask why it was necessary. I couldn't come up with a good answer.</p>

#### [ Simon Hudon (Sep 20 2018 at 09:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/association%20lists%2C%20finmap/near/134292027):
<blockquote>
<p>You could say that this is a similar situation: a finmap is just a multiset with no duplicate keys. However, I found that it's more useful to look at it as a finmap because I didn't find a lot of the other multiset definitions to be very useful for a finmap.</p>
</blockquote>
<p>I don't get this nuance</p>

#### [ Sean Leather (Sep 20 2018 at 09:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/association%20lists%2C%20finmap/near/134292185):
<blockquote>
<p>I don't get this nuance</p>
</blockquote>
<p>I think it's similar to how you don't see a lot of the <code>multiset</code> definitions used for <code>finset</code>. There's a particular subset (mostly starting with <code>nd</code>) that are used in <code>finset</code>, but many of them are not.</p>

#### [ Sean Leather (Sep 20 2018 at 09:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/association%20lists%2C%20finmap/near/134292261):
<p><code>multiset</code> seems to be useful as a substrate for <code>finset</code> and <code>finmap</code>, but it also has a larger API that is oriented towards counting duplicates.</p>

#### [ Sean Leather (Sep 20 2018 at 09:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/association%20lists%2C%20finmap/near/134292305):
<p>Also, the subset of the <code>multiset</code> API used for <code>finset</code> is not useful for <code>finmap</code>.</p>

#### [ Mario Carneiro (Sep 20 2018 at 15:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/association%20lists%2C%20finmap/near/134308497):
<p>I think the comparison is apt, and applicable to <code>alist</code>. A finset is just a multiset with a property, but the API is different (some basic operations are not applicable, like <code>cons</code>, and others are slightly weird and become more useful on the subtype, like <code>ndinsert</code>).</p>

#### [ Mario Carneiro (Sep 20 2018 at 15:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/association%20lists%2C%20finmap/near/134308618):
<p>In the case of <code>alist</code>, there are some operations that don't work anymore, like <code>cons</code>, and others are slightly weird and have been prefixed with <code>k</code> for lists. <code>cons</code> is just not a valid <code>alist</code> operation, <code>insert</code> is.</p>

#### [ Sean Leather (Sep 20 2018 at 15:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/association%20lists%2C%20finmap/near/134308803):
<blockquote>
<p>I think the comparison is apt, and applicable to <code>alist</code>.</p>
</blockquote>
<p>So does this mean you agree with me, since my comparison is apt, which is to say that <code>alist</code> is not a useful structure?</p>

#### [ Sean Leather (Sep 20 2018 at 15:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/association%20lists%2C%20finmap/near/134308937):
<blockquote>
<p>In the case of <code>alist</code>, there are some operations that don't work anymore, like <code>cons</code>, and others are slightly weird and have been prefixed with <code>k</code> for lists. <code>cons</code> is just not a valid <code>alist</code> operation, <code>insert</code> is.</p>
</blockquote>
<p>This hints of disagreement. My point is that lists are constructed with <code>nil</code> and <code>cons</code>, and it is useful to have that construction, and therefore more useful to have a bare list with no duplicate keys than to have a structure hide that construction.</p>

#### [ Mario Carneiro (Sep 20 2018 at 15:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/association%20lists%2C%20finmap/near/134309076):
<p>In short: I think <code>finset</code> is useful, and I think <code>alist</code> is useful</p>

#### [ Mario Carneiro (Sep 20 2018 at 15:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/association%20lists%2C%20finmap/near/134309171):
<p>I don't see why <code>alist</code> should provide a nil/cons construction. It's not natural. If you want to do such a construction then you should unpack the <code>alist</code> first</p>

#### [ Sean Leather (Sep 20 2018 at 15:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/association%20lists%2C%20finmap/near/134309182):
<p>That's kind of my point. <span class="emoji emoji-1f609" title="wink">:wink:</span></p>

#### [ Mario Carneiro (Sep 20 2018 at 15:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/association%20lists%2C%20finmap/near/134309185):
<p>Instead it has <code>empty</code>/<code>insert</code></p>

#### [ Mario Carneiro (Sep 20 2018 at 15:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/association%20lists%2C%20finmap/near/134309213):
<p>My point is, why are you doing list things on <code>alist</code>s?</p>

#### [ Sean Leather (Sep 20 2018 at 15:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/association%20lists%2C%20finmap/near/134309308):
<p>My point is that I want to construct lists with no duplicate keys as well as use any other existing definitions and theorems on lists.</p>

#### [ Mario Carneiro (Sep 20 2018 at 15:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/association%20lists%2C%20finmap/near/134309416):
<p>then do so, on <code>list</code>. You don't need <code>alist</code> for that</p>

#### [ Sean Leather (Sep 20 2018 at 15:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/association%20lists%2C%20finmap/near/134309434):
<p>Quite right, which is why I don't think <code>alist</code> is necessary.</p>

#### [ Mario Carneiro (Sep 20 2018 at 15:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/association%20lists%2C%20finmap/near/134309458):
<p><code>alist</code> provides a compositional structure for safety-preserving functions on lists</p>

#### [ Mario Carneiro (Sep 20 2018 at 15:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/association%20lists%2C%20finmap/near/134309526):
<blockquote>
<p>as well as use any other existing definitions and theorems on lists.</p>
</blockquote>
<p>Most list operations don't preserve the invariant. What do you do with these?</p>

#### [ Sean Leather (Sep 20 2018 at 15:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/association%20lists%2C%20finmap/near/134309548):
<p>Well, if you want it, add it. I'm only trying to save you work.</p>

#### [ Mario Carneiro (Sep 20 2018 at 15:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/association%20lists%2C%20finmap/near/134309589):
<p>This is an honest question. What is missing from the API of <code>alist</code> that you would want, that requires resorting to <code>list</code>?</p>

#### [ Mario Carneiro (Sep 20 2018 at 15:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/association%20lists%2C%20finmap/near/134309684):
<p>Except for <code>union</code>, there's nothing I've missed that comes to mind</p>

#### [ Sean Leather (Sep 20 2018 at 15:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/association%20lists%2C%20finmap/near/134309698):
<p>I'm not sure about <code>alist</code>, but I defined the minimum necessary to use <code>list</code>s with no duplicate keys. For example, <code>has_mem</code> and <code>append</code> don't need to be redefined. You only need some extra properties to use <code>append</code>, for example.</p>

#### [ Mario Carneiro (Sep 20 2018 at 15:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/association%20lists%2C%20finmap/near/134309747):
<p>To answer your question from earlier, <code>alist</code> should also be available as a tool for programmers. "I need a map, I only have equality" -&gt; use <code>alist</code> or <code>finmap</code></p>

#### [ Mario Carneiro (Sep 20 2018 at 15:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/association%20lists%2C%20finmap/near/134309771):
<p>Note that the <code>has_mem</code> on <code>alist</code> is different from the one on lists</p>

#### [ Mario Carneiro (Sep 20 2018 at 15:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/association%20lists%2C%20finmap/near/134309775):
<p>and <code>append</code> doesn't apply</p>

#### [ Sean Leather (Sep 20 2018 at 15:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/association%20lists%2C%20finmap/near/134309778):
<p>Which I don't think it should be.</p>

#### [ Sean Leather (Sep 20 2018 at 15:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/association%20lists%2C%20finmap/near/134309781):
<p>As you'll see in my library.</p>

#### [ Mario Carneiro (Sep 20 2018 at 15:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/association%20lists%2C%20finmap/near/134309850):
<p>I think in common programming parlance, <code>x \in m</code> where m is a dictionary / map / associative array, means <code>x</code> is a key contained in the map <code>m</code>, not <code>x</code> is a key-value pair in the map</p>

#### [ Mario Carneiro (Sep 20 2018 at 15:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/association%20lists%2C%20finmap/near/134309915):
<p>The idiom for the other interpretation is <code>&lt;x, y&gt; \in m.val</code>, where <code>val</code> is the operation sometimes called <code>entries</code> in other libraries</p>

#### [ Mario Carneiro (Sep 20 2018 at 15:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/association%20lists%2C%20finmap/near/134309930):
<p>(indeed, maybe it should be renamed to that)</p>

#### [ Mario Carneiro (Sep 20 2018 at 15:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/association%20lists%2C%20finmap/near/134310185):
<p>Note also that if it meant membership in the underlying list, then it wouldn't be decidable unless you assume decidability of the values, which is not needed for anything else</p>

#### [ Sean Leather (Sep 20 2018 at 15:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/association%20lists%2C%20finmap/near/134310257):
<p>Fair enough. With <code>a : alist</code>, you can use <code>a.val</code>/<code>a.entries</code>.</p>

#### [ Mario Carneiro (Sep 20 2018 at 15:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/association%20lists%2C%20finmap/near/134310292):
<p>right, I think this helps to view them as different things (a finite map vs a list of pairs)</p>

#### [ Mario Carneiro (Sep 20 2018 at 15:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/association%20lists%2C%20finmap/near/134310375):
<p>You pointed out that it is possible to define operations like <code>append</code> if you assume side conditions (i.e. the key sets are disjoint). Does this come up often?</p>

#### [ Sean Leather (Sep 20 2018 at 15:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/association%20lists%2C%20finmap/near/134310406):
<p>I don't know about “often,” but it has come up.</p>

#### [ Sean Leather (Sep 20 2018 at 15:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/association%20lists%2C%20finmap/near/134310494):
<p>I'm now using <code>finmap</code> instead of association lists directly, and you have the same thing with union there.</p>

#### [ Sean Leather (Sep 20 2018 at 15:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/association%20lists%2C%20finmap/near/134310514):
<p>I'm assuming you'll use <code>has_union</code> for <code>alist</code> instead of <code>has_append</code>?</p>

#### [ Mario Carneiro (Sep 20 2018 at 15:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/association%20lists%2C%20finmap/near/134310519):
<p>yes</p>

#### [ Mario Carneiro (Sep 20 2018 at 15:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/association%20lists%2C%20finmap/near/134310530):
<p>since it's union, not append :P</p>

#### [ Mario Carneiro (Sep 20 2018 at 15:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/association%20lists%2C%20finmap/near/134310581):
<p>it's not even possible to give an <code>append</code> instance that uses <code>list.append</code></p>

#### [ Sean Leather (Sep 20 2018 at 15:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/association%20lists%2C%20finmap/near/134310582):
<p>Well, it's debatable that it's not a form of append.</p>

#### [ Mario Carneiro (Sep 20 2018 at 15:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/association%20lists%2C%20finmap/near/134310612):
<p>I prefer set terminology when duplicates are being dropped</p>

#### [ Sean Leather (Sep 20 2018 at 15:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/association%20lists%2C%20finmap/near/134310633):
<p>It's still appending. <span class="emoji emoji-1f642" title="slight smile">:slight_smile:</span></p>

#### [ Sean Leather (Sep 20 2018 at 15:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/association%20lists%2C%20finmap/near/134310663):
<p>When it comes to the <code>finmap</code>, you can forget that there is any appending. But with <code>alist</code>, you can't.</p>

#### [ Mario Carneiro (Sep 20 2018 at 15:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/association%20lists%2C%20finmap/near/134310727):
<p>Not sure what you mean. The underlying operation is not an append</p>

#### [ Mario Carneiro (Sep 20 2018 at 15:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/association%20lists%2C%20finmap/near/134310750):
<p>It is true that <code>union</code> would be order-respecting on <code>alist</code></p>

#### [ Mario Carneiro (Sep 20 2018 at 15:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/association%20lists%2C%20finmap/near/134310760):
<p>but then again, so is <code>union</code> on <code>list</code></p>

#### [ Sean Leather (Sep 20 2018 at 15:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/association%20lists%2C%20finmap/near/134310795):
<div class="codehilite"><pre><span></span><span class="n">def</span> <span class="n">append</span> <span class="o">:</span> <span class="n">list</span> <span class="n">α</span> <span class="bp">→</span> <span class="n">list</span> <span class="n">α</span> <span class="bp">→</span> <span class="n">list</span> <span class="n">α</span>
<span class="bp">|</span> <span class="o">[]</span>       <span class="n">l</span> <span class="o">:=</span> <span class="n">l</span>
<span class="bp">|</span> <span class="o">(</span><span class="n">h</span> <span class="bp">::</span> <span class="n">s</span><span class="o">)</span> <span class="n">t</span> <span class="o">:=</span> <span class="n">h</span> <span class="bp">::</span> <span class="o">(</span><span class="n">append</span> <span class="n">s</span> <span class="n">t</span><span class="o">)</span>

<span class="n">def</span> <span class="n">kunion</span> <span class="o">:</span> <span class="n">list</span> <span class="o">(</span><span class="n">sigma</span> <span class="n">β</span><span class="o">)</span> <span class="bp">→</span> <span class="n">list</span> <span class="o">(</span><span class="n">sigma</span> <span class="n">β</span><span class="o">)</span> <span class="bp">→</span> <span class="n">list</span> <span class="o">(</span><span class="n">sigma</span> <span class="n">β</span><span class="o">)</span>
<span class="bp">|</span> <span class="o">[]</span>         <span class="n">l</span> <span class="o">:=</span> <span class="n">l</span>
<span class="bp">|</span> <span class="o">(</span><span class="n">hd</span> <span class="bp">::</span> <span class="n">tl</span><span class="o">)</span> <span class="n">l</span> <span class="o">:=</span> <span class="n">hd</span> <span class="bp">::</span> <span class="n">kunion</span> <span class="n">tl</span> <span class="o">(</span><span class="n">kerase</span> <span class="n">hd</span><span class="bp">.</span><span class="mi">1</span> <span class="n">l</span><span class="o">)</span>
</pre></div>

#### [ Sean Leather (Sep 20 2018 at 15:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/association%20lists%2C%20finmap/near/134310838):
<p>Are you doing it differently?</p>

#### [ Mario Carneiro (Sep 20 2018 at 15:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/association%20lists%2C%20finmap/near/134310876):
<p>I think the <code>erase</code> makes that a rather different kind of operation. But also I think we need two functions here - that is <code>unionl</code></p>

#### [ Mario Carneiro (Sep 20 2018 at 15:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/association%20lists%2C%20finmap/near/134310955):
<p><code>unionr</code> would be</p>
<div class="codehilite"><pre><span></span>def kunionr : list (sigma β) → list (sigma β) → list (sigma β)
| []         l := l
| (hd :: tl) l := kinsert hd.1 hd.2 (kunionr tl l)
</pre></div>

#### [ Mario Carneiro (Sep 20 2018 at 15:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/association%20lists%2C%20finmap/near/134310975):
<p>I'm not even sure if it should get a <code>has_union</code> notation</p>

#### [ Sean Leather (Sep 20 2018 at 15:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/association%20lists%2C%20finmap/near/134311002):
<p>I'm not sure if you need it. I don't foresee people asking for it.</p>

#### [ Mario Carneiro (Sep 20 2018 at 16:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/association%20lists%2C%20finmap/near/134311082):
<p>You need left and right preference. For <code>finmap</code> you can ignore it since the order of parameters gives the preference, but on <code>alist</code> you have order and preference separately</p>

#### [ Sean Leather (Sep 20 2018 at 16:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/association%20lists%2C%20finmap/near/134311233):
<p>Why do you need it? Just because it's possible doesn't make it a need.</p>

#### [ Mario Carneiro (Sep 20 2018 at 16:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/association%20lists%2C%20finmap/near/134311266):
<p>I'm okay with just assuming right preference (which is what <code>list.union</code> does), but you want left preference?</p>

#### [ Sean Leather (Sep 20 2018 at 16:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/association%20lists%2C%20finmap/near/134311344):
<p>I stuck with the Haskell <code>Data.Map</code> approach because it seemed to the most intuitive to me.</p>

#### [ Mario Carneiro (Sep 20 2018 at 16:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/association%20lists%2C%20finmap/near/134311402):
<p>Keep in mind that haskell has laziness to contend with, making your definition more natural for them</p>

#### [ Sean Leather (Sep 20 2018 at 16:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/association%20lists%2C%20finmap/near/134311408):
<p>Yep.</p>

#### [ Sean Leather (Sep 20 2018 at 16:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/association%20lists%2C%20finmap/near/134311479):
<p><code>∪</code> is <code>infixl</code>, so could that also indicate left-biased is preferred?</p>

#### [ Mario Carneiro (Sep 20 2018 at 16:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/association%20lists%2C%20finmap/near/134311485):
<p>It seems like the difference between <code>foldl</code> and <code>foldr</code></p>

#### [ Mario Carneiro (Sep 20 2018 at 16:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/association%20lists%2C%20finmap/near/134311497):
<p>and we have both of those</p>

#### [ Mario Carneiro (Sep 20 2018 at 16:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/association%20lists%2C%20finmap/near/134311510):
<p>I'd rather not commit to one camp here</p>

#### [ Mario Carneiro (Sep 20 2018 at 16:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/association%20lists%2C%20finmap/near/134311595):
<p>particularly since there are also performance characteristics to worry about, and the lean 4 compiler may change this as well</p>

#### [ Sean Leather (Sep 20 2018 at 16:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/association%20lists%2C%20finmap/near/134311611):
<p>You have to commit to one for <code>∪</code> at the very least.</p>

#### [ Sean Leather (Sep 20 2018 at 16:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/association%20lists%2C%20finmap/near/134311653):
<p>I guess if you're going with the <code>list.union</code> precedent, you would go with the right-biased option.</p>

#### [ Mario Carneiro (Sep 20 2018 at 16:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/association%20lists%2C%20finmap/near/134311734):
<p>I think <code>alist</code> shouldn't have a notation, <code>finmap</code> can use left preference by default since the API properties take precedence there</p>

#### [ Mario Carneiro (Sep 20 2018 at 16:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/association%20lists%2C%20finmap/near/134311763):
<p>I should look at other languages like java or python and see what preference is preferred</p>

#### [ Sean Leather (Sep 20 2018 at 16:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/association%20lists%2C%20finmap/near/134311849):
<p>I would consider Haskell, ML, OCaml, Coq, Agda, Idris, etc. before looking at Java or Python.</p>

#### [ Mario Carneiro (Sep 20 2018 at 16:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/association%20lists%2C%20finmap/near/134311856):
<p>hm, python has a mutation operation which makes the precedence obvious</p>

#### [ Mario Carneiro (Sep 20 2018 at 16:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/association%20lists%2C%20finmap/near/134311991):
<p>Same with java. OCaml takes a merge function that resolves differences</p>

#### [ Mario Carneiro (Sep 20 2018 at 16:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/association%20lists%2C%20finmap/near/134312238):
<p>Haskell has both union (left bias) and unionWith that takes a merge function</p>

#### [ Mario Carneiro (Sep 20 2018 at 16:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/association%20lists%2C%20finmap/near/134312504):
<p>I couldn't find anything for Coq. Idris uses merge left bias and mergeWith</p>

#### [ Mario Carneiro (Sep 20 2018 at 16:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/association%20lists%2C%20finmap/near/134312515):
<p>ML is roll your own dict</p>

#### [ Sean Leather (Sep 21 2018 at 11:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/association%20lists%2C%20finmap/near/134367053):
<p>I'm coming to realize that what would be better for me than a <code>finmap</code> union that updates by <code>insert</code> or <code>erase</code> is something like an internal disjoint union. At least that's what I've gathered it would be called. [<a href="https://math.stackexchange.com/a/1631405" target="_blank" title="https://math.stackexchange.com/a/1631405">1</a>, <a href="https://ncatlab.org/nlab/show/disjoint+union#internal_version" target="_blank" title="https://ncatlab.org/nlab/show/disjoint+union#internal_version">2</a>] For <code>finmap</code>, perhaps the simplest definition would be:</p>
<div class="codehilite"><pre><span></span><span class="n">def</span> <span class="n">djunion</span> <span class="o">(</span><span class="n">f</span> <span class="n">g</span> <span class="o">:</span> <span class="n">finmap</span> <span class="n">α</span> <span class="n">β</span><span class="o">)</span> <span class="o">:</span> <span class="n">finmap</span> <span class="n">α</span> <span class="n">β</span> <span class="o">:=</span> <span class="k">if</span> <span class="n">disjoint</span> <span class="n">f</span><span class="bp">.</span><span class="n">keys</span> <span class="n">g</span><span class="bp">.</span><span class="n">keys</span> <span class="k">then</span> <span class="n">f</span> <span class="err">∪</span> <span class="n">g</span> <span class="k">else</span> <span class="err">∅</span>
</pre></div>


<p>But a more efficient version would probably use <code>list.append</code> instead of <code>list.kunion</code> as <code>∪</code> does.</p>
<p>I'm only dealing with unions of disjoint <code>finmap</code>s, and it would simplify some things if I didn't have to track all of the <code>disjoint f.keys g.keys</code>.</p>

#### [ Sean Leather (Sep 21 2018 at 11:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/association%20lists%2C%20finmap/near/134368101):
<p>Likewise, a disjoint insert would be good. Conceptually:</p>
<div class="codehilite"><pre><span></span><span class="n">def</span> <span class="n">djinsert</span> <span class="o">(</span><span class="n">a</span> <span class="o">:</span> <span class="n">α</span><span class="o">)</span> <span class="o">(</span><span class="n">b</span> <span class="o">:</span> <span class="n">β</span> <span class="n">a</span><span class="o">)</span> <span class="o">(</span><span class="n">f</span> <span class="o">:</span> <span class="n">finmap</span> <span class="n">α</span> <span class="n">β</span><span class="o">)</span> <span class="o">:</span> <span class="n">finmap</span> <span class="n">α</span> <span class="n">β</span> <span class="o">:=</span> <span class="k">if</span> <span class="n">a</span> <span class="err">∉</span> <span class="n">f</span><span class="bp">.</span><span class="n">keys</span> <span class="k">then</span> <span class="n">insert</span> <span class="n">a</span> <span class="n">b</span> <span class="n">f</span> <span class="k">else</span> <span class="err">∅</span>
</pre></div>


<p>But <code>cons</code> would be better than <code>kinsert</code>.</p>

#### [ Sean Leather (Oct 08 2018 at 16:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/association%20lists%2C%20finmap/near/135406194):
<p><span class="user-mention" data-user-id="110049">@Mario Carneiro</span> What is your plan with <a href="https://github.com/leanprover-community/mathlib/tree/finmap" target="_blank" title="https://github.com/leanprover-community/mathlib/tree/finmap">https://github.com/leanprover-community/mathlib/tree/finmap</a> ? I'd like to see something get into mathlib. However, given the somewhat large difference between your rewrite and <a href="https://github.com/spl/lean-finmap" target="_blank" title="https://github.com/spl/lean-finmap">my library</a>, I'm a bit reluctant at this point to invest the time to port more definitions and theorems over to that branch without knowing what's going to happen to it. Do you plan to continue working on that branch?</p>

#### [ Mario Carneiro (Oct 08 2018 at 16:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/association%20lists%2C%20finmap/near/135406729):
<p>would you like me to merge it?</p>

#### [ Sean Leather (Oct 08 2018 at 16:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/association%20lists%2C%20finmap/near/135406861):
<blockquote>
<p>would you like me to merge it?</p>
</blockquote>
<p>“It” being the <code>leanprover-community/mathlib</code> branch? Sure, if you're happy with it in its current state. I would feel more comfortable extending it at that point.</p>

#### [ Mario Carneiro (Oct 08 2018 at 16:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/association%20lists%2C%20finmap/near/135406969):
<p>I noticed you renamed some things. Not a fan of <code>knodup</code>?</p>

#### [ Sean Leather (Oct 08 2018 at 16:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/association%20lists%2C%20finmap/near/135407006):
<blockquote>
<p>I noticed you renamed some things. Not a fan of <code>knodup</code>?</p>
</blockquote>
<p><span class="emoji emoji-1f642" title="slight smile">:slight_smile:</span> No. I think <code>nodupkeys</code> is better.</p>

#### [ Mario Carneiro (Oct 08 2018 at 16:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/association%20lists%2C%20finmap/near/135407143):
<p>when I look at it I think "nine letters is long for a name segment"</p>

#### [ Mario Carneiro (Oct 08 2018 at 16:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/association%20lists%2C%20finmap/near/135407208):
<p>You could have <code>nodup_keys</code> but then it confuses with <code>nodup</code> of <code>keys</code></p>

#### [ Mario Carneiro (Oct 08 2018 at 16:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/association%20lists%2C%20finmap/near/135407221):
<p>what about <code>nodup_fst</code>?</p>

#### [ Sean Leather (Oct 08 2018 at 16:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/association%20lists%2C%20finmap/near/135407228):
<blockquote>
<p>You could have <code>nodup_keys</code> but then it confuses with <code>nodup</code> of <code>keys</code></p>
</blockquote>
<p>Exactly.</p>

#### [ Sean Leather (Oct 08 2018 at 16:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/association%20lists%2C%20finmap/near/135407279):
<blockquote>
<p>what about <code>nodup_fst</code>?</p>
</blockquote>
<p>How is that better than <code>nodupkeys</code> since <code>nodup</code> and <code>keys</code> already exist?</p>

#### [ Sean Leather (Oct 08 2018 at 16:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/association%20lists%2C%20finmap/near/135407304):
<p>... exist in the association list/finmap API that is.</p>

#### [ Mario Carneiro (Oct 08 2018 at 16:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/association%20lists%2C%20finmap/near/135407323):
<p>I mean for the list version, before the "map" interpretation</p>

#### [ Sean Leather (Oct 08 2018 at 16:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/association%20lists%2C%20finmap/near/135407650):
<p>I'd prefer <code>nodupkeys</code> for both for consistency's sake. I think the name is clear in that it links <code>nodup</code> and <code>keys</code> and as short as it's needed to be.</p>

#### [ Sean Leather (Oct 08 2018 at 16:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/association%20lists%2C%20finmap/near/135407709):
<p>Anyway, I have to go now. If you want to discuss any other issues, I'll pick it up tomorrow.</p>


{% endraw %}
