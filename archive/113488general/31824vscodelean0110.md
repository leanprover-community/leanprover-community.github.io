---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/31824vscodelean0110.html
---

## Stream: [general](index.html)
### Topic: [vscode-lean 0.11.0](31824vscodelean0110.html)

---


{% raw %}
#### [ Gabriel Ebner (Apr 21 2018 at 19:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vscode-lean%200.11.0/near/125499751):
<p>I just pushed a new update for the vscode extension.  A few bugfixes and features have accumulated over the last few months:</p>
<ul>
<li>The new <code>visibleRanges</code> API in vscode is supported now.  Per default, we no longer check the whole file on every keystroke, but only the currently visible lines (and the rest of the file above).  This new API is only present in vscode &gt;=1.22 (released in March), no idea if it works with older vscode versions.  Please complain (or upgrade) if you run into any troubles.</li>
<li>You can now input ⦃⦄ using <code>\{{</code></li>
<li>Fewer complaints about <code>leanpkg.path</code> changes.</li>
</ul>

#### [ Mario Carneiro (Apr 21 2018 at 22:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vscode-lean%200.11.0/near/125504461):
<p>can you also type ⟦⟧ using <code>\[[</code>?</p>

#### [ Chris Hughes (Apr 21 2018 at 22:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vscode-lean%200.11.0/near/125504757):
<p>No, it seems.</p>

#### [ Patrick Massot (Apr 21 2018 at 22:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vscode-lean%200.11.0/near/125505099):
<p>How do you check what version of the extension is used? How do you upgrade?</p>

#### [ Chris Hughes (Apr 21 2018 at 22:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vscode-lean%200.11.0/near/125505255):
<p>I clicked on extensions on the left pane, and I clicked the reload button. Try typing<code> \{{</code> and  if it turns into special brackets, you have the upgrade.</p>

#### [ Patrick Massot (Apr 21 2018 at 22:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vscode-lean%200.11.0/near/125505262):
<p>I didn't see a reload button</p>

#### [ Patrick Massot (Apr 21 2018 at 22:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vscode-lean%200.11.0/near/125505263):
<p>I'll search more</p>

#### [ Chris Hughes (Apr 21 2018 at 22:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vscode-lean%200.11.0/near/125505271):
<p>I have a feeling it might do it automatically if you restart, so I would try the brackets thing.</p>

#### [ Patrick Massot (Apr 21 2018 at 22:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vscode-lean%200.11.0/near/125505313):
<p>Ok, I've found a menu containg "search updates" (or something like this, this part is in French here)</p>

#### [ Patrick Massot (Apr 21 2018 at 22:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vscode-lean%200.11.0/near/125505315):
<p>I'm updated</p>

#### [ Gabriel Ebner (Apr 22 2018 at 08:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vscode-lean%200.11.0/near/125520061):
<blockquote>
<p>can you also type ⟦⟧ using <code>\[[</code>?</p>
</blockquote>
<p>You can, as of a minute ago.</p>

#### [ Patrick Massot (Apr 22 2018 at 11:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vscode-lean%200.11.0/near/125523356):
<p>Thank you!</p>

#### [ Patrick Massot (Apr 22 2018 at 11:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vscode-lean%200.11.0/near/125523927):
<p>Very easy suggestion: make a command (usable through Ctrl-p like the Restart server command) that opens up <a href="https://github.com/leanprover/vscode-lean/blob/master/translations.json" target="_blank" title="https://github.com/leanprover/vscode-lean/blob/master/translations.json">https://github.com/leanprover/vscode-lean/blob/master/translations.json</a> in a new tab (not fetching it from the web, opening the one which is actually used on the current install)</p>

#### [ Patrick Massot (Apr 23 2018 at 16:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vscode-lean%200.11.0/near/125571378):
<p>What about having syntax highlighting in the Lean message window? Would that be complicated to do?</p>

#### [ Gabriel Ebner (Apr 23 2018 at 16:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vscode-lean%200.11.0/near/125572368):
<p>If "message window" is the info view (with the pause button on the top right), then this is a bit complicated.  Unfortunately we do not have any programmatic access to vscode's syntax highlighter.  AFAIK there is also no pure javascript package that can use these syntax highlighting files.  I'll keep it in mind though.</p>

#### [ Patrick Massot (Apr 23 2018 at 16:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vscode-lean%200.11.0/near/125572400):
<p>Yes this is what I meant. We do spend quite some time staring at this window, and it's a bit austere.</p>

#### [ Patrick Massot (May 08 2018 at 17:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vscode-lean%200.11.0/near/126270759):
<blockquote>
<p>If "message window" is the info view (with the pause button on the top right), then this is a bit complicated.  Unfortunately we do not have any programmatic access to vscode's syntax highlighter.  AFAIK there is also no pure javascript package that can use these syntax highlighting files.  I'll keep it in mind though.</p>
</blockquote>
<p>I just played a bit with this. Here is what I currently see in my VScode:</p>

#### [ Patrick Massot (May 08 2018 at 17:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vscode-lean%200.11.0/near/126270769):
<p><a href="/user_uploads/3121/nyFVDaVWTFbkyaDebw9CTNRE/colored_tactic_state.png" target="_blank" title="colored_tactic_state.png">colored_tactic_state.png</a></p>
<div class="message_inline_image"><a href="/user_uploads/3121/nyFVDaVWTFbkyaDebw9CTNRE/colored_tactic_state.png" target="_blank" title="colored_tactic_state.png"><img src="/user_uploads/3121/nyFVDaVWTFbkyaDebw9CTNRE/colored_tactic_state.png"></a></div>

#### [ Patrick Massot (May 08 2018 at 17:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vscode-lean%200.11.0/near/126270776):
<p>I think it's already useful (to me at least)</p>

#### [ Patrick Massot (May 08 2018 at 18:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vscode-lean%200.11.0/near/126270840):
<p>It's super low tech and unreliable, based on:</p>
<div class="codehilite"><pre><span></span><span class="kd">function</span> <span class="nx">formatTacticState</span><span class="p">(</span><span class="nx">s</span><span class="o">:</span> <span class="nx">string</span><span class="p">)</span><span class="o">:</span> <span class="nx">string</span> <span class="p">{</span>
    <span class="k">return</span> <span class="nx">s</span>
        <span class="p">.</span><span class="nx">replace</span><span class="p">(</span><span class="sr">/^(\d+ goals)/g</span><span class="p">,</span> <span class="s1">&#39;&lt;strong style=&quot;color:#569cd6;&quot;&gt;$1&lt;/strong&gt; :&#39;</span><span class="p">)</span>
        <span class="p">.</span><span class="nx">replace</span><span class="p">(</span><span class="sr">/^([^ ][^:\n⊢]*) :/g</span><span class="p">,</span> <span class="s1">&#39;&lt;strong style=&quot;color:#dcdc00;&quot;&gt;$1&lt;/strong&gt; :&#39;</span><span class="p">)</span>
        <span class="p">.</span><span class="nx">replace</span><span class="p">(</span><span class="sr">/\n([^ ⊢][^:\n⊢]*) :/g</span><span class="p">,</span> <span class="s1">&#39;\n&lt;strong style=&quot;color:#dcdc00;&quot;&gt;$1&lt;/strong&gt; :&#39;</span><span class="p">)</span>
        <span class="p">.</span><span class="nx">replace</span><span class="p">(</span><span class="sr">/\n⊢/g</span><span class="p">,</span> <span class="s1">&#39;\n&lt;strong style=&quot;color:#569cd6;&quot;&gt;⊢&lt;/strong&gt;&#39;</span><span class="p">);</span>
<span class="p">}</span>
</pre></div>

#### [ Patrick Massot (May 08 2018 at 18:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vscode-lean%200.11.0/near/126270853):
<p>Which is called in <code>InfoProvider.renderGoal</code></p>

#### [ Patrick Massot (May 08 2018 at 18:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vscode-lean%200.11.0/near/126270859):
<p><span class="user-mention" data-user-id="110043">@Gabriel Ebner</span> What do you think about that?</p>

#### [ Mario Carneiro (May 08 2018 at 18:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vscode-lean%200.11.0/near/126270862):
<p>I would object to this on purity grounds, but TBH the standard syntax highlighter isn't much better</p>

#### [ Patrick Massot (May 08 2018 at 18:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vscode-lean%200.11.0/near/126270911):
<p>Indeed it couldn't be less pure</p>

#### [ Patrick Massot (May 08 2018 at 18:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vscode-lean%200.11.0/near/126270920):
<p>And the next Lean file I'll open will probably tell me I missed some edge case</p>

#### [ Mario Carneiro (May 08 2018 at 18:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vscode-lean%200.11.0/near/126270925):
<p>You can probably parse a tactic print string pretty reliably by classifying the lines that don't start with whitespace</p>

#### [ Patrick Massot (May 08 2018 at 18:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vscode-lean%200.11.0/near/126270940):
<p>But Gabriel told me the syntax highlighter is not available here</p>

#### [ Patrick Massot (May 08 2018 at 18:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vscode-lean%200.11.0/near/126270946):
<p>Yes, a classification function would help</p>

#### [ Patrick Massot (May 08 2018 at 18:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vscode-lean%200.11.0/near/126270948):
<p>At least make things more modular</p>

#### [ Patrick Massot (May 08 2018 at 18:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vscode-lean%200.11.0/near/126270990):
<p>With the above method, trying to catch anything new would likely break things</p>

#### [ Gabriel Ebner (May 08 2018 at 18:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vscode-lean%200.11.0/near/126270991):
<p>This looks great!  I'll just make sure it is also readable with a white background.</p>

#### [ Mario Carneiro (May 08 2018 at 18:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vscode-lean%200.11.0/near/126270999):
<p>don't forget the <code>case</code> line of tactic state</p>

#### [ Patrick Massot (May 08 2018 at 18:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vscode-lean%200.11.0/near/126271008):
<p>There should be away to have proper CSS interacting with the selected theme instead of hardcoded colors</p>

#### [ Mario Carneiro (May 08 2018 at 18:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vscode-lean%200.11.0/near/126271012):
<p>presumably it's as simple as just <code>&lt;span class="x"&gt;</code></p>

#### [ Patrick Massot (May 08 2018 at 18:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vscode-lean%200.11.0/near/126271065):
<p>The question is not there: where should we put classes definitions?</p>

#### [ Gabriel Ebner (May 08 2018 at 18:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vscode-lean%200.11.0/near/126271069):
<p><span class="user-mention" data-user-id="110031">@Patrick Massot</span> did you just put the <code>&lt;strong&gt;</code> inside the <code>&lt;pre&gt;</code>?</p>

#### [ Gabriel Ebner (May 08 2018 at 18:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vscode-lean%200.11.0/near/126271075):
<p>The CSS is in <code>infoview.css</code></p>

#### [ Patrick Massot (May 08 2018 at 18:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vscode-lean%200.11.0/near/126271078):
<div class="codehilite"><pre><span></span>    <span class="kr">private</span> <span class="nx">renderGoal</span><span class="p">()</span> <span class="p">{</span>
        <span class="k">if</span> <span class="p">(</span><span class="o">!</span><span class="k">this</span><span class="p">.</span><span class="nx">curGoalState</span> <span class="o">||</span> <span class="k">this</span><span class="p">.</span><span class="nx">displayMode</span> <span class="o">!==</span> <span class="nx">DisplayMode</span><span class="p">.</span><span class="nx">OnlyState</span><span class="p">)</span> <span class="p">{</span> <span class="k">return</span> <span class="s1">&#39;&#39;</span><span class="p">;</span> <span class="p">}</span>
        <span class="k">return</span> <span class="sb">`&lt;div id=&quot;goal&quot;&gt;&lt;h1&gt;Tactic State&lt;/h1&gt;&lt;pre&gt;</span><span class="si">${</span><span class="nx">formatTacticState</span><span class="p">(</span><span class="nx">escapeHtml</span><span class="p">(</span><span class="k">this</span><span class="p">.</span><span class="nx">curGoalState</span><span class="p">))</span><span class="si">}</span><span class="sb">&lt;/pre&gt;&lt;/div&gt;`</span><span class="p">;</span>
    <span class="p">}</span>
</pre></div>

#### [ Patrick Massot (May 08 2018 at 18:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vscode-lean%200.11.0/near/126271182):
<p>Reading <code>infoview.css</code> is very interesting</p>

#### [ Patrick Massot (May 08 2018 at 18:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vscode-lean%200.11.0/near/126271185):
<p>Indeed it should be very easy to use</p>

#### [ Gabriel Ebner (May 08 2018 at 18:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vscode-lean%200.11.0/near/126272070):
<p>The colorization has been deployed.  Please complain if the fancy colors distract you too much.</p>

#### [ Patrick Massot (May 08 2018 at 18:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vscode-lean%200.11.0/near/126272161):
<p>Wow, you're fast</p>

#### [ Patrick Massot (May 08 2018 at 18:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vscode-lean%200.11.0/near/126272166):
<p>I was working on it</p>

#### [ Patrick Massot (May 08 2018 at 18:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vscode-lean%200.11.0/near/126272171):
<p>But not fast enough <span class="emoji emoji-1f609" title="wink">:wink:</span></p>

#### [ Patrick Massot (May 08 2018 at 18:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vscode-lean%200.11.0/near/126272212):
<p>I didn't know about the <code>m</code> flag in <code>replace</code></p>

#### [ Patrick Massot (May 08 2018 at 18:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vscode-lean%200.11.0/near/126272253):
<p><a href="https://github.com/leanprover/vscode-lean/commit/8a1e35e6495593620fbaacad5ff98929c15c7793#diff-66e057b4386ca2dfc39356a2fbecb4f2R354" target="_blank" title="https://github.com/leanprover/vscode-lean/commit/8a1e35e6495593620fbaacad5ff98929c15c7793#diff-66e057b4386ca2dfc39356a2fbecb4f2R354">https://github.com/leanprover/vscode-lean/commit/8a1e35e6495593620fbaacad5ff98929c15c7793#diff-66e057b4386ca2dfc39356a2fbecb4f2R354</a> is not good</p>

#### [ Patrick Massot (May 08 2018 at 18:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vscode-lean%200.11.0/near/126272297):
<p>There can be space before the colon</p>

#### [ Patrick Massot (May 08 2018 at 18:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vscode-lean%200.11.0/near/126272300):
<p>when several variables share a common type</p>

#### [ Patrick Massot (May 08 2018 at 18:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vscode-lean%200.11.0/near/126272324):
<p><a href="/user_uploads/3121/VUbq6QDeA0f2v-1YIVC0v3Vu/bug.png" target="_blank" title="bug.png">bug.png</a></p>
<div class="message_inline_image"><a href="/user_uploads/3121/VUbq6QDeA0f2v-1YIVC0v3Vu/bug.png" target="_blank" title="bug.png"><img src="/user_uploads/3121/VUbq6QDeA0f2v-1YIVC0v3Vu/bug.png"></a></div>

#### [ Patrick Massot (May 08 2018 at 18:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vscode-lean%200.11.0/near/126272327):
<p>But I do like this orange</p>

#### [ Patrick Massot (May 08 2018 at 18:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vscode-lean%200.11.0/near/126272394):
<p>Also, you forgot the <code>|</code> showing current goal in conversion mode</p>

#### [ Patrick Massot (May 08 2018 at 18:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vscode-lean%200.11.0/near/126272404):
<p>In my current version I gave it the same formatting as the ⊢</p>

#### [ Gabriel Ebner (May 08 2018 at 18:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vscode-lean%200.11.0/near/126272597):
<p>Should be fixed now.</p>

#### [ Patrick Massot (May 08 2018 at 18:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vscode-lean%200.11.0/near/126272796):
<p>Nice!</p>

#### [ Patrick Massot (May 08 2018 at 18:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vscode-lean%200.11.0/near/126272820):
<p>oh oh...</p>

#### [ Patrick Massot (May 08 2018 at 18:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vscode-lean%200.11.0/near/126272857):
<p>New bug</p>

#### [ Patrick Massot (May 08 2018 at 18:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vscode-lean%200.11.0/near/126272862):
<p>I also had that one at some point</p>

#### [ Patrick Massot (May 08 2018 at 18:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vscode-lean%200.11.0/near/126272887):
<p><a href="/user_uploads/3121/aLyRDIXg6KqbSFhRTd0_j6AI/bug2.png" target="_blank" title="bug2.png">bug2.png</a></p>
<div class="message_inline_image"><a href="/user_uploads/3121/aLyRDIXg6KqbSFhRTd0_j6AI/bug2.png" target="_blank" title="bug2.png"><img src="/user_uploads/3121/aLyRDIXg6KqbSFhRTd0_j6AI/bug2.png"></a></div>

#### [ Patrick Massot (May 08 2018 at 18:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vscode-lean%200.11.0/near/126272938):
<p>I can see you are too much used to proved software. In the real world you need to test your software with real world data</p>

#### [ Sebastian Ullrich (May 08 2018 at 18:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vscode-lean%200.11.0/near/126272939):
<p>It's spreading!</p>

#### [ Sebastian Ullrich (May 08 2018 at 18:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vscode-lean%200.11.0/near/126272963):
<p>In Emacs, all flycheck errors are now highlighted with the Lean syntax highlighter btw</p>

#### [ Sebastian Ullrich (May 08 2018 at 18:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vscode-lean%200.11.0/near/126272964):
<p>:)</p>

#### [ Patrick Massot (May 08 2018 at 18:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vscode-lean%200.11.0/near/126272967):
<p>For the record, before you told us you 0.11.2 was out, the state of my regexs was:</p>
<div class="codehilite"><pre><span></span><span class="kd">function</span> <span class="nx">formatTacticState</span><span class="p">(</span><span class="nx">s</span><span class="o">:</span> <span class="nx">string</span><span class="p">)</span><span class="o">:</span> <span class="nx">string</span> <span class="p">{</span>
    <span class="k">return</span> <span class="nx">s</span>
        <span class="p">.</span><span class="nx">replace</span><span class="p">(</span><span class="sr">/^(\d+ goals)/g</span><span class="p">,</span> <span class="s1">&#39;&lt;strong class=&quot;goals-number&quot;&gt;$1&lt;/strong&gt; :&#39;</span><span class="p">)</span>
        <span class="p">.</span><span class="nx">replace</span><span class="p">(</span><span class="sr">/^([^ ][^:\n⊢]*) :/g</span><span class="p">,</span> <span class="s1">&#39;&lt;strong class=&quot;context-element&quot;&gt;$1&lt;/strong&gt; :&#39;</span><span class="p">)</span>
        <span class="p">.</span><span class="nx">replace</span><span class="p">(</span><span class="sr">/\n([^ ⊢][^:\n⊢]*) :/g</span><span class="p">,</span> <span class="s1">&#39;\n&lt;strong class=&quot;context-element&quot;&gt;$1&lt;/strong&gt; :&#39;</span><span class="p">)</span>
        <span class="p">.</span><span class="nx">replace</span><span class="p">(</span><span class="sr">/^case ([^\n]*)/g</span><span class="p">,</span> <span class="s1">&#39;&lt;strong class=&quot;case&quot;&gt;case $1&lt;/strong&gt; :&#39;</span><span class="p">)</span>
        <span class="p">.</span><span class="nx">replace</span><span class="p">(</span><span class="sr">/\ncase ([^\n]*)/g</span><span class="p">,</span> <span class="s1">&#39;\n&lt;strong class=&quot;case&quot;&gt;case $1&lt;/strong&gt; :&#39;</span><span class="p">)</span>
        <span class="p">.</span><span class="nx">replace</span><span class="p">(</span><span class="sr">/^⊢/g</span><span class="p">,</span> <span class="s1">&#39;&lt;strong class=&quot;goal&quot;&gt;⊢&lt;/strong&gt;&#39;</span><span class="p">)</span>
        <span class="p">.</span><span class="nx">replace</span><span class="p">(</span><span class="sr">/\n⊢/g</span><span class="p">,</span> <span class="s1">&#39;\n&lt;strong class=&quot;goal&quot;&gt;⊢&lt;/strong&gt;&#39;</span><span class="p">)</span>
        <span class="p">.</span><span class="nx">replace</span><span class="p">(</span><span class="sr">/^\|/g</span><span class="p">,</span> <span class="s1">&#39;&lt;strong class=&quot;goal&quot;&gt;|&lt;/strong&gt;&#39;</span><span class="p">)</span>
        <span class="p">.</span><span class="nx">replace</span><span class="p">(</span><span class="sr">/\n\|/g</span><span class="p">,</span> <span class="s1">&#39;\n&lt;strong class=&quot;goal&quot;&gt;|&lt;/strong&gt;&#39;</span><span class="p">)</span>
        <span class="p">.</span><span class="nx">replace</span><span class="p">(</span><span class="sr">/no goals/g</span><span class="p">,</span> <span class="s1">&#39;🎉 &#39;</span><span class="p">);</span>
<span class="p">}</span>
</pre></div>

#### [ Patrick Massot (May 08 2018 at 18:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vscode-lean%200.11.0/near/126273026):
<p>I should really try Lean in spacemacs at some point</p>

#### [ Patrick Massot (May 08 2018 at 18:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vscode-lean%200.11.0/near/126273030):
<p>I don't why I'm affraid</p>

#### [ Sebastian Ullrich (May 08 2018 at 18:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vscode-lean%200.11.0/near/126273041):
<p>I should really write a Lean spacemacs layer at some point</p>

#### [ Patrick Massot (May 08 2018 at 19:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vscode-lean%200.11.0/near/126273048):
<p>Sebastian, do you have plans to make more structured tactic state output in Lean 4?</p>

#### [ Patrick Massot (May 08 2018 at 19:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vscode-lean%200.11.0/near/126273099):
<p>Like, we wouldn't have to regex the output</p>

#### [ Patrick Massot (May 08 2018 at 19:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vscode-lean%200.11.0/near/126273115):
<p>It could be useful also to build more powerful IDEs</p>

#### [ Patrick Massot (May 08 2018 at 19:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vscode-lean%200.11.0/near/126273165):
<p>(where we could click on stuff in the tactic state and see cool things happen)</p>

#### [ Sebastian Ullrich (May 08 2018 at 19:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vscode-lean%200.11.0/near/126273244):
<p><span class="user-mention" data-user-id="110031">@Patrick Massot</span> <a href="https://github.com/leanprover/lean/issues/1693" target="_blank" title="https://github.com/leanprover/lean/issues/1693">https://github.com/leanprover/lean/issues/1693</a></p>

#### [ Patrick Massot (May 08 2018 at 19:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vscode-lean%200.11.0/near/126273395):
<p>Ok, I see you already discussed this quite a bit</p>

#### [ Patrick Massot (May 08 2018 at 19:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vscode-lean%200.11.0/near/126273404):
<p>Is this in the Lean 4 TODO list then? I guess the priority is not super high</p>

#### [ Sebastian Ullrich (May 08 2018 at 19:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vscode-lean%200.11.0/near/126275103):
<p>We're currently more focused on the structured traces (<a href="https://github.com/leanprover/lean/issues/1692" target="_blank" title="https://github.com/leanprover/lean/issues/1692">https://github.com/leanprover/lean/issues/1692</a>) since that influences how we write Lean-in-Lean code. I suspect structured term output will come a bit later.</p>

#### [ Patrick Massot (May 08 2018 at 21:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vscode-lean%200.11.0/near/126279875):
<p>Great</p>

#### [ Gabriel Ebner (May 09 2018 at 08:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vscode-lean%200.11.0/near/126301917):
<blockquote>
<p>I can see you are too much used to proved software. In the real world you need to test your software with real world data</p>
</blockquote>
<p><span class="emoji emoji-1f604" title="smile">:smile:</span> We don't have a single test in vscode-lean.  But the new bug is fixed now.</p>

#### [ Kevin Buzzard (May 09 2018 at 08:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vscode-lean%200.11.0/near/126302503):
<p>Patrick do you test your theorems about manifolds with real world data?</p>

#### [ Patrick Massot (May 09 2018 at 09:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vscode-lean%200.11.0/near/126303394):
<p>Of course I do! How else could we get confidence in our theorems until proof assistants are ready for the real battlefield?</p>

#### [ Patrick Massot (May 09 2018 at 09:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vscode-lean%200.11.0/near/126303396):
<p>Have a look at my latest preprint for instance</p>

#### [ Patrick Massot (May 09 2018 at 09:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vscode-lean%200.11.0/near/126303397):
<p>The main result is checked against the canonical contact structures on spheres and projective spaces</p>

#### [ Patrick Massot (May 09 2018 at 09:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vscode-lean%200.11.0/near/126303450):
<p>Conclusions were already known to hold for spheres and known not to hold for projective spaces (with the nice corollary that the hypothesis of the theorem does not hold for projective spaces, something that we have no other way to prove at the moment)</p>

#### [ Patrick Massot (May 09 2018 at 09:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vscode-lean%200.11.0/near/126303453):
<p>Oh crap, my VScode doesn't like the tada unicode in the Tactic state window</p>

#### [ Patrick Massot (May 09 2018 at 09:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vscode-lean%200.11.0/near/126303456):
<p>I forgot I kept that experiment in the regex I posted</p>

#### [ Gabriel Ebner (May 09 2018 at 09:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vscode-lean%200.11.0/near/126303546):
<p>I tried it and the tada emoji works here, but I have a font installed for it.</p>

#### [ Gabriel Ebner (May 09 2018 at 09:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vscode-lean%200.11.0/near/126303661):
<p>I have just enabled the highlighting for error messages as well.  It looks a bit weird for <code>#print</code> results, but I think it's a definite improvement for failed tactics.</p>

#### [ Mario Carneiro (May 09 2018 at 09:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vscode-lean%200.11.0/near/126303925):
<p>I recommend against seriously using the tada emoji in the vscode extension</p>

#### [ Mario Carneiro (May 09 2018 at 09:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vscode-lean%200.11.0/near/126303926):
<p>At least put it after the words "no goals"</p>

#### [ Gabriel Ebner (May 09 2018 at 09:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vscode-lean%200.11.0/near/126303990):
<p>Yes, it comes right after the two words.  But I'll remove it.</p>

#### [ Patrick Massot (May 09 2018 at 17:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vscode-lean%200.11.0/near/126321127):
<blockquote>
<p><a href="/user_uploads/3121/aLyRDIXg6KqbSFhRTd0_j6AI/bug2.png" target="_blank" title="bug2.png">bug2.png</a></p>
<div class="message_inline_image"><a href="/user_uploads/3121/aLyRDIXg6KqbSFhRTd0_j6AI/bug2.png" target="_blank" title="bug2.png"><img src="/user_uploads/3121/aLyRDIXg6KqbSFhRTd0_j6AI/bug2.png"></a></div></blockquote>
<p>This also happen in conversion mode...</p>

#### [ Patrick Massot (May 13 2018 at 22:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vscode-lean%200.11.0/near/126508439):
<p>Here is tricky new bug: <code>#reduce λ x, x</code>. Maybe we should try to detect <code>information reduce result</code> on top</p>

#### [ Patrick Massot (May 23 2018 at 21:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vscode-lean%200.11.0/near/126992808):
<p><span class="user-mention" data-user-id="110043">@Gabriel Ebner</span>  Same remark about detecting class instance trace (and probably also other kinds of traces?)</p>

#### [ Gabriel Ebner (May 24 2018 at 11:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vscode-lean%200.11.0/near/127021300):
<p>We skip all information messages now.  I kind of liked it that <code>trace_state</code> was colorized, but we can't distinguish it from a class trace.</p>

#### [ Johan Commelin (May 25 2018 at 11:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vscode-lean%200.11.0/near/127073426):
<p>I have no clue at all if this is possible: can you show matching parens in the goal. (So if I select one, the other gets some highlighting?)</p>

#### [ Gabriel Ebner (May 25 2018 at 11:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vscode-lean%200.11.0/near/127073444):
<p>It's possible.  But we'd have to implement the highlight code ourselves (it's just an html page with javascript).</p>

#### [ Johan Commelin (May 25 2018 at 12:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vscode-lean%200.11.0/near/127073780):
<p>Ok, but there is probably some js lib doing this already, right?</p>

#### [ Gabriel Ebner (May 25 2018 at 12:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vscode-lean%200.11.0/near/127074433):
<p>I didn't find anything off-the-shelf after a quick search.  But it shouldn't be too hard.  Listen to mouse move events, if we're over a (, [, or { inside a <code>&lt;pre&gt;</code>, then look for a matching paren and put a <code>&lt;span class='paren-highlighted'&gt;</code> around it, and remove previous <code>.paren-highlighted</code> spans.</p>

#### [ Mario Carneiro (May 25 2018 at 12:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vscode-lean%200.11.0/near/127075431):
<p><span class="user-mention" data-user-id="110043">@Gabriel Ebner</span> I have vscode-lean github downloaded and hooked up to my VSCode install, but I forget how to compile the extension from source. Could you remind me (and possibly put the instructions on the README)?</p>

#### [ Gabriel Ebner (May 25 2018 at 12:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vscode-lean%200.11.0/near/127075505):
<p>The easiest way is to open the extension in vscode and press <code>F5</code>. This will compile it and start a new vscode window with the development version of the extension.  This is also documented in the README: <a href="https://github.com/leanprover/vscode-lean#development" target="_blank" title="https://github.com/leanprover/vscode-lean#development">https://github.com/leanprover/vscode-lean#development</a></p>


{% endraw %}
