---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/20539squeezesimp.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [squeeze_simp](https://leanprover-community.github.io/archive/113488general/20539squeezesimp.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Johan Commelin (Oct 08 2018 at 15:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/squeeze_simp/near/135401004):
<p><span class="user-mention" data-user-id="110026">@Simon Hudon</span> To what extend do you think <code>sed</code> and <code>lean</code> could cooperate to automatically turn every <code>simp</code> into a <code>squeeze_simp</code>, and then every <code>squeeze_simp</code> into a <code>simp only</code>? Can we automate Kenny?</p>

#### [ Simon Hudon (Oct 08 2018 at 16:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/squeeze_simp/near/135406348):
<p>But we like Kenny!</p>

#### [ Simon Hudon (Oct 08 2018 at 16:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/squeeze_simp/near/135406424):
<p>I was thinking along those lines but I was thinking of adding a feature to the emacs Lean mode. I'm not how I would do it for VS code though. Do you know how to script it?</p>

#### [ Johan Commelin (Oct 08 2018 at 16:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/squeeze_simp/near/135406432):
<p>I don't know anything about VScode</p>

#### [ Johan Commelin (Oct 08 2018 at 16:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/squeeze_simp/near/135406440):
<p>But couldn't this just be a CLI-only thing?</p>

#### [ Johan Commelin (Oct 08 2018 at 16:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/squeeze_simp/near/135406455):
<p>For other purposes the output of <code>squeeze_simp</code> is already very useful.</p>

#### [ Patrick Massot (Oct 08 2018 at 16:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/squeeze_simp/near/135406473):
<p>Can't we use a hole command here again?</p>

#### [ Mario Carneiro (Oct 08 2018 at 16:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/squeeze_simp/near/135406490):
<p>you still have to click on a hole command</p>

#### [ Johan Commelin (Oct 08 2018 at 16:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/squeeze_simp/near/135406493):
<p>Exactly</p>

#### [ Mario Carneiro (Oct 08 2018 at 16:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/squeeze_simp/near/135406537):
<p>indeed, you have to manually edit the file to put a hole in in the first place</p>

#### [ Johan Commelin (Oct 08 2018 at 16:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/squeeze_simp/near/135406538):
<p>I want <code>sed</code> to "click" on the hole command.</p>

#### [ Patrick Massot (Oct 08 2018 at 16:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/squeeze_simp/near/135406554):
<p>Oh you mean you want this for batch processing?</p>

#### [ Simon Hudon (Oct 08 2018 at 16:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/squeeze_simp/near/135406562):
<p>The difficult thing about using something like sed is detecting the end of the input <code>squeeze_simp</code></p>

#### [ Simon Hudon (Oct 08 2018 at 16:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/squeeze_simp/near/135406574):
<p>But I guess we could output it in Lean</p>

#### [ Simon Hudon (Oct 08 2018 at 16:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/squeeze_simp/near/135406591):
<p><span class="user-mention" data-user-id="110031">@Patrick Massot</span> exactly</p>

#### [ Patrick Massot (Oct 08 2018 at 16:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/squeeze_simp/near/135406602):
<p>Sorry I read too quickly the beginning of this thread (I'm fighting dependent rw)</p>

#### [ Simon Hudon (Oct 08 2018 at 16:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/squeeze_simp/near/135407907):
<p><span class="user-mention" data-user-id="110049">@Mario Carneiro</span> has shown us how useful awk can be in these situations. Do you think if we output the beginning line and column number of the input, the ending line and column number of the input and the replacement, we can get awk to go in there and do the replacement? You'd probably also have to go from the last to the first if you want to do it in one go so that the line numbers don't get invalidated.</p>

#### [ Johan Commelin (Oct 08 2018 at 16:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/squeeze_simp/near/135408204):
<p>Sure, that should definitely be possible</p>

#### [ Johan Commelin (Oct 08 2018 at 16:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/squeeze_simp/near/135408213):
<p>I guess <code>squeeze_simp</code> can get access to its location in the file via some tactic_state magic, right?</p>

#### [ Johan Commelin (Oct 08 2018 at 16:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/squeeze_simp/near/135408290):
<p>Or you make <code>squeeze_simp</code> output a patch (-;</p>

#### [ Johan Commelin (Oct 08 2018 at 16:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/squeeze_simp/near/135408296):
<p>Then we can just commit it, and git takes care of the rest <span class="emoji emoji-1f606" title="lol">:lol:</span></p>

#### [ Simon Hudon (Oct 08 2018 at 18:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/squeeze_simp/near/135413309):
<p>I just looked into the patch file format. It seems like more work to format than to just do it ourselves</p>

#### [ Johan Commelin (Oct 08 2018 at 18:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/squeeze_simp/near/135414054):
<p>Ok, so how about your suggestion, with line+col numbers</p>

#### [ Simon Hudon (Oct 08 2018 at 18:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/squeeze_simp/near/135415134):
<p>I think the best bet is to use <code>awk</code> but I'll have to learn it</p>

#### [ Simon Hudon (Oct 08 2018 at 18:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/squeeze_simp/near/135415187):
<p>Right now I'm experimenting with emacs to see if I can get a nice first approximation</p>

#### [ Johan Commelin (Oct 08 2018 at 18:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/squeeze_simp/near/135415446):
<p><code>awk</code> is not hard. Also, I wouldn't mind helping you.</p>

#### [ Johan Commelin (Oct 08 2018 at 18:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/squeeze_simp/near/135415506):
<p>We could use <code>sed</code> to squeeze_simpify a <code>.lean</code> file. After that, we run <code>lean --make</code> on the file, and capture the stdout.</p>

#### [ Johan Commelin (Oct 08 2018 at 18:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/squeeze_simp/near/135415521):
<p>If <code>squeeze_simp</code> can produce output of the form <code>line:column:replacement_text</code> I think we can take it from there.</p>

#### [ Simon Hudon (Oct 08 2018 at 18:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/squeeze_simp/near/135415693):
<p>I was thinking of a format like this:</p>
<div class="codehilite"><pre><span></span><span class="mi">84</span><span class="o">:</span><span class="mi">23</span><span class="o">:</span>
<span class="mi">86</span><span class="o">:</span><span class="mi">0</span><span class="o">:</span>
<span class="c1">--- BEGIN ---</span>
<span class="n">simp</span> <span class="n">only</span> <span class="o">[</span><span class="n">perm_cons</span><span class="o">,</span> <span class="n">multiset</span><span class="bp">.</span><span class="n">cons_coe</span><span class="o">,</span> <span class="n">iff_self</span><span class="o">,</span> <span class="n">multiset</span><span class="bp">.</span><span class="n">coe_eq_coe</span><span class="o">,</span> <span class="n">multiset</span><span class="bp">.</span><span class="n">quot_mk_to_coe&#39;&#39;</span><span class="o">]</span>
<span class="c1">--- END ---</span>
</pre></div>

#### [ Johan Commelin (Oct 08 2018 at 18:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/squeeze_simp/near/135415718):
<p>unix prefers to keep everything on 1 line.</p>

#### [ Simon Hudon (Oct 08 2018 at 18:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/squeeze_simp/near/135415785):
<p>In that case, how about <code>line0:col0:line1:col1:replacement_text</code>?</p>

#### [ Johan Commelin (Oct 08 2018 at 18:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/squeeze_simp/near/135415873):
<p>Looks good</p>

#### [ Johan Commelin (Oct 08 2018 at 18:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/squeeze_simp/near/135415884):
<p>Unless we want to anticipate multiline replacement texts</p>

#### [ Simon Hudon (Oct 08 2018 at 18:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/squeeze_simp/near/135415997):
<p>That's what I'm looking at now. The replacement is sometimes multiline but there's no real reason to be. I'll restrict it to one line and let the user reformat if needed</p>

#### [ Johan Commelin (Oct 08 2018 at 18:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/squeeze_simp/near/135416006):
<p>There is no "user" if we run this in batch mode over 25 files.</p>

#### [ Johan Commelin (Oct 08 2018 at 19:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/squeeze_simp/near/135416069):
<p>But we can write a smart awk script</p>

#### [ Johan Commelin (Oct 08 2018 at 19:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/squeeze_simp/near/135416073):
<p>It can try to reformat that line, breaking on suitable <code>,</code></p>

#### [ Simon Hudon (Oct 08 2018 at 19:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/squeeze_simp/near/135416182):
<p>That's tricky because it might not be alone on its line</p>

#### [ Johan Commelin (Oct 08 2018 at 19:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/squeeze_simp/near/135416288):
<p>I can compute the old line length, and the new one, etc...</p>

#### [ Johan Commelin (Oct 08 2018 at 19:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/squeeze_simp/near/135416292):
<p>It definitely makes a trivial thing a lot harder</p>

#### [ Simon Hudon (Oct 08 2018 at 19:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/squeeze_simp/near/135416372):
<p>Let's leave it for the "future work" section</p>

#### [ Simon Hudon (Oct 08 2018 at 19:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/squeeze_simp/near/135416427):
<p>It might become necessary to have a Lean code formatter which would make all of that good work redundant</p>

#### [ Johan Commelin (Oct 08 2018 at 19:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/squeeze_simp/near/135416431):
<p>Yep, sounds good</p>

#### [ Simon Hudon (Oct 08 2018 at 19:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/squeeze_simp/near/135416520):
<p>This proof engineering stuff is so funny. We're tweaking eternal truths :P</p>

#### [ Simon Hudon (Oct 08 2018 at 19:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/squeeze_simp/near/135416567):
<p>As impatient as I get with Lean and mathlib, it's pretty great that it finds my mistakes faster than my supervisor :D</p>

#### [ Bryan Gin-ge Chen (Oct 08 2018 at 19:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/squeeze_simp/near/135416822):
<p>Are there other "tactics with output" where this kind of tooling would also be useful? Maybe <code>tidy</code>?</p>

#### [ Mario Carneiro (Oct 08 2018 at 19:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/squeeze_simp/near/135416879):
<p><code>tidy</code> already makes output</p>

#### [ Johan Commelin (Oct 08 2018 at 19:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/squeeze_simp/near/135416916):
<p>I'll be reading a bit of Milne to my kids... see you guys soon!</p>

#### [ Simon Hudon (Oct 08 2018 at 19:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/squeeze_simp/near/135416940):
<p>Have fun!</p>

#### [ Bryan Gin-ge Chen (Oct 08 2018 at 19:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/squeeze_simp/near/135417013):
<p>Indeed, what I mean is the output format being discussed here something we should also consider for e.g. <code>tidy</code>?</p>

#### [ Simon Hudon (Oct 08 2018 at 19:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/squeeze_simp/near/135417183):
<p>That could be useful. It might be more useful for <code>tidy</code> to have it tied into the IDE because you probably don't use <code>tidy</code><em>en masse</em></p>

#### [ Gabriel Ebner (Oct 08 2018 at 19:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/squeeze_simp/near/135417482):
<p>Where are you printing the replacement text?  Trace messages?</p>

#### [ Simon Hudon (Oct 08 2018 at 19:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/squeeze_simp/near/135417541):
<p>Yes exactly</p>

#### [ Gabriel Ebner (Oct 08 2018 at 19:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/squeeze_simp/near/135417756):
<p>It's pretty easy to hook them up in vscode: in the extension, you just need to <a href="https://github.com/Microsoft/vscode/blob/5b03dcd69d98b6540f789868cf4647b6486ed739/src/vs/vscode.d.ts#L2046-L2106" target="_blank" title="https://github.com/Microsoft/vscode/blob/5b03dcd69d98b6540f789868cf4647b6486ed739/src/vs/vscode.d.ts#L2046-L2106">return a list of code actions</a>.  Then you can execute these replacements with <code>ctrl+.</code> (similar to holes, which are also implemented using code actions in the extension).</p>

#### [ Simon Hudon (Oct 08 2018 at 19:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/squeeze_simp/near/135417850):
<p>Emacs gives the line and column of the command issuing the trace. Does VS code also do the same?</p>

#### [ Gabriel Ebner (Oct 08 2018 at 19:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/squeeze_simp/near/135417859):
<p>A few suggestions for the format: it should not occur by accident (in a simp trace e.g.).  And it would be nice to have a (textual) description for the replacement (vscode shows this in the dropdown).  Ideally also the <a href="https://github.com/Microsoft/vscode/blob/5b03dcd69d98b6540f789868cf4647b6486ed739/src/vs/vscode.d.ts#L1926-L1996" target="_blank" title="https://github.com/Microsoft/vscode/blob/5b03dcd69d98b6540f789868cf4647b6486ed739/src/vs/vscode.d.ts#L1926-L1996">kind of code action</a>, e.g. vscode can apply <em>all</em> quickfixes in a given file automatically.</p>

#### [ Gabriel Ebner (Oct 08 2018 at 19:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/squeeze_simp/near/135417920):
<p>We have access to the same position information, yes.  However it only includes the start position of the tactic unfortunately.</p>

#### [ Simon Hudon (Oct 08 2018 at 19:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/squeeze_simp/near/135417924):
<p>Does it run them backward so that the line numbers remain valid?</p>

#### [ Gabriel Ebner (Oct 08 2018 at 19:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/squeeze_simp/near/135417971):
<p>Good question.  I don't really know.  If we do one-line replacements then it shouldn't matter too much.</p>

#### [ Simon Hudon (Oct 08 2018 at 19:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/squeeze_simp/near/135417976):
<p>In the parser <code>cur_pos</code> can give me an arbitrary position. I'm putting it at the end and it gives me a good approximation</p>

#### [ Mario Carneiro (Oct 08 2018 at 19:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/squeeze_simp/near/135417980):
<p>Ooh, this is nice. Can we just get a generic hook for writing things from lean?</p>


{% endraw %}
