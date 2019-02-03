---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/39364compiletimestatistics.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [compile time statistics](https://leanprover-community.github.io/archive/113488general/39364compiletimestatistics.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Kenny Lau (Sep 24 2018 at 07:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/134506913):
<p>Can we get some data on how long it takes for <em>each</em> file to compile?</p>

#### [ Kenny Lau (Sep 24 2018 at 07:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/134506915):
<p>in mathlib, that is</p>

#### [ Simon Hudon (Sep 24 2018 at 07:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/134507008):
<p>You can call <code>lean file.lean --profile</code> on each. You can get the list of all the files of <code>mathlib</code> with <code>git ls-files *.lean</code></p>

#### [ Scott Morrison (Sep 24 2018 at 08:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/134508030):
<p>Make sure everything is already compiled before starting this, so it's only recompiling the particular file you've asked about.</p>

#### [ Scott Morrison (Sep 24 2018 at 08:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/134508037):
<p>However I'd guess that even this could give misleading results: lean still has to reparse all the imported <code>.olean</code> files, so at the end of a huge development you'd expect even tiny files to have very large compile times with this technique.</p>

#### [ Kenny Lau (Sep 24 2018 at 08:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/134508409):
<p><span class="user-mention" data-user-id="110087">@Scott Morrison</span> then what should I do?</p>

#### [ Scott Morrison (Sep 24 2018 at 08:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/134508430):
<p>Well, I guess you could measure how bad the effect I pointed out it, by timing compiling an empty olean file that imports everything?</p>

#### [ Scott Morrison (Sep 24 2018 at 08:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/134508454):
<p>Or even fancier, you could time compiling an empty olean file with the exact same imports, and subtract that time off.</p>

#### [ Scott Morrison (Sep 24 2018 at 08:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/134508499):
<p>I really don't have a good sense of whether this is necessary!</p>

#### [ Scott Morrison (Sep 24 2018 at 08:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/134508504):
<p>I can't think of any direct way to get these per-file timings, however.</p>

#### [ Simon Hudon (Sep 24 2018 at 08:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/134508534):
<p>I'm really tempted to neglect that time</p>

#### [ Simon Hudon (Sep 24 2018 at 08:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/134508584):
<p>You can do it once with all the files to get an upper bound on how much time that is but I feel like that must be negligible compared with everything else</p>

#### [ Kenny Lau (Sep 24 2018 at 08:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/134509157):
<p>if I have a file <code>e.lean</code> that imports <code>a</code> and <code>b</code> and <code>c</code> and <code>d</code>, can I look at the time of <code>e</code> and subtract from it the times of the other four files?</p>

#### [ Kenny Lau (Sep 24 2018 at 08:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/134509337):
<p>I've now tracked 57 out of 255 files</p>

#### [ Kenny Lau (Sep 24 2018 at 08:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/134509338):
<p>this is really slow</p>

#### [ Simon Hudon (Sep 24 2018 at 08:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/134509339):
<p>You shouldn't do it that way.</p>

#### [ Simon Hudon (Sep 24 2018 at 08:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/134509342):
<p>Start with <code>lean --make</code>, then build each file</p>

#### [ Kenny Lau (Sep 24 2018 at 08:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/134509348):
<p>I have all the oleans already</p>

#### [ Kenny Lau (Sep 24 2018 at 08:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/134509352):
<p>I'm running this command:<br>
<code> git ls-files *.lean | xargs -n1 /c/lean/bin/lean --profile &gt; junk.txt 2&gt; time.txt</code></p>

#### [ Simon Hudon (Sep 24 2018 at 09:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/134509388):
<p>Ok, in that case, all that is left is wait. The travis build takes more than an hour</p>

#### [ Kenny Lau (Sep 24 2018 at 09:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/134509410):
<p>brilliant</p>

#### [ Simon Hudon (Sep 24 2018 at 09:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/134509424):
<p>Yup</p>

#### [ Kenny Lau (Sep 24 2018 at 09:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/134510040):
<p>117 out of 255 files</p>

#### [ Kenny Lau (Sep 24 2018 at 10:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/134514042):
<p>there are 11 files that did not show any <code>cumulative profiling times:</code></p>

#### [ Kenny Lau (Sep 24 2018 at 10:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/134514044):
<p>which 11 files is that?</p>

#### [ Kenny Lau (Sep 24 2018 at 11:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/134514346):
<p><a href="https://gist.github.com/kckennylau/6ea2ca42e517ad801564a86fe7a1b7bd" target="_blank" title="https://gist.github.com/kckennylau/6ea2ca42e517ad801564a86fe7a1b7bd">https://gist.github.com/kckennylau/6ea2ca42e517ad801564a86fe7a1b7bd</a></p>

#### [ Kenny Lau (Sep 24 2018 at 11:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/134514354):
<p>time in seconds, may have indexing error by at most 11</p>

#### [ Kenny Lau (Sep 24 2018 at 11:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/134514478):
<div class="codehilite"><pre><span></span>commit ca7f118058342a2f077e836e643d26e0ad1f3ca6
Author: Rob Lewis &lt;Rob.y.lewis@gmail.com&gt;
Date:   Fri Sep 21 17:06:34 2018 +0200

    fix(docs/tactics.md): missing backquote, formatting

    I think I never previewed when I updated the `linarith` doc before, sorry.
</pre></div>

#### [ Kenny Lau (Sep 24 2018 at 11:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/134514888):
<p>I guess afterall looking at the file size might be more reliable</p>

#### [ Kenny Lau (Sep 24 2018 at 11:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/134515602):
<p>is it a good idea if I start working on making the files compile faster?</p>

#### [ Kenny Lau (Sep 24 2018 at 11:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/134515606):
<p><span class="user-mention" data-user-id="110049">@Mario Carneiro</span> will you guys accept my PR?</p>

#### [ Patrick Massot (Sep 24 2018 at 11:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/134515948):
<p>I think it's really a huge problem that we are tempted to sacrifice readability for compile time</p>

#### [ Mario Carneiro (Sep 24 2018 at 11:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/134516218):
<p>yes, if you can make a significant improvement on compile times without making the proof much longer, I think I would accept it without issue. I assume you will start from really bad offenders. If you can get at least ~70% reduction in compile time then I would accept a modest increase in proof size</p>

#### [ Mario Carneiro (Sep 24 2018 at 11:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/134516273):
<p>I find that readability is mostly orthogonal to compile time</p>

#### [ Kenny Lau (Sep 24 2018 at 11:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/134516451):
<p>challenge accepted</p>

#### [ Reid Barton (Sep 24 2018 at 15:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/134526934):
<p>I would guess the 11 files which had no profiling information are the <code>.default</code> modules which do nothing but import other modules</p>

#### [ Reid Barton (Sep 24 2018 at 15:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/134526938):
<p>but I don't understand your data yet</p>

#### [ Reid Barton (Sep 24 2018 at 16:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/134528608):
<blockquote>
<p>I think it's really a huge problem that we are tempted to sacrifice readability for compile time</p>
</blockquote>
<p>But <span class="user-mention" data-user-id="110031">@Patrick Massot</span>, it means we can join the programmers <a href="https://xkcd.com/303/" target="_blank" title="https://xkcd.com/303/">https://xkcd.com/303/</a></p>

#### [ Keeley Hoek (Sep 24 2018 at 16:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/134528990):
<p><a href="https://xkcd.com/1205/" target="_blank" title="https://xkcd.com/1205/">https://xkcd.com/1205/</a></p>

#### [ Kenny Lau (Sep 24 2018 at 17:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/134534111):
<blockquote>
<p>but I don't understand your data yet</p>
</blockquote>
<p>just assume that big numbers means bad, no matter how many there are</p>

#### [ Simon Hudon (Sep 24 2018 at 19:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/134541798):
<p>Another approach is to look at the frequent offenders, the tactics that most often eat up most of the run time of proofs. Then we can work on making them faster. If you find such offenders, I wouldn't mind pitching in to improve the tactics.</p>

#### [ Kenny Lau (Sep 24 2018 at 21:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/134552824):
<p>I think <code>simp</code> is like plastic</p>

#### [ Kenny Lau (Sep 24 2018 at 21:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/134552838):
<p>when it was discovered, everyone thought it's the greatest idea in the world, and everyone used it</p>

#### [ Kenny Lau (Sep 24 2018 at 21:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/134552843):
<p>and it's too late when everyone discovered the ramifications it brings</p>

#### [ Kenny Lau (Sep 24 2018 at 21:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/134552865):
<p>Kurzgesagt compares plastic with the story of the king with the golden touch</p>

#### [ Simon Hudon (Sep 24 2018 at 22:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/134553864):
<p>One way to improve the performances of <code>simp</code> is to create specialized list of simp lemmas. You can have a look at <code>functor_norm</code>. Sometimes, <code>simp only with &lt;my-list&gt;</code> can be sufficient and will be faster.</p>

#### [ Patrick Massot (Sep 24 2018 at 22:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/134553952):
<p>Are you really sure that <code>simp</code> is the slow thing? It seems to me elaboration is often very slow</p>

#### [ Simon Hudon (Sep 24 2018 at 22:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/134554391):
<p>Do you know what kind of situation makes elaboration slow? </p>
<p>Aside from that, if we divide a proof into proof search + elaboration + proof check, I think shrinking the proof search side will also shrink the elaboration and proof check side because proof search often uses both to select the right approach.</p>

#### [ Kenny Lau (Sep 24 2018 at 22:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/134554606):
<blockquote>
<p>One way to improve the performances of <code>simp</code> is to create specialized list of simp lemmas. You can have a look at <code>functor_norm</code>. Sometimes, <code>simp only with &lt;my-list&gt;</code> can be sufficient and will be faster.</p>
</blockquote>
<p><a href="#narrow/stream/113488-general/topic/simp_attr" title="#narrow/stream/113488-general/topic/simp_attr">https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simp_attr</a></p>

#### [ Simon Hudon (Sep 24 2018 at 22:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/134554943):
<p>Yes there are pitfalls</p>

#### [ Simon Hudon (Sep 24 2018 at 22:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/134554995):
<p>One thing you can do is create simp attributes local to files or modules and group in that lemma everything useful for its proofs.</p>

#### [ Simon Hudon (Sep 24 2018 at 22:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/134555063):
<p>Then you can merge those lists as a shortcut for just listing all the useful lemmas.</p>

#### [ Simon Hudon (Sep 24 2018 at 22:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/134555156):
<p>The other possibility is to create a command for listing all the simp lemmas used in a file and printing out the way to create the required simp lemma</p>

#### [ Kenny Lau (Sep 25 2018 at 05:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/134572292):
<div class="codehilite"><pre><span></span>$ git checkout master
Switched to branch &#39;master&#39;
Your branch is up-to-date with &#39;origin/master&#39;.

$ /c/lean/bin/lean --profile algebra/big_operators.lean &gt;/dev/null
cumulative profiling times:
        compilation 1.37ms
        decl post-processing 7.92s
        elaboration 47.7s
        elaboration: tactic compilation 676ms
        elaboration: tactic execution 42s
        parsing 1.18s
        type checking 19.5ms

$ git checkout faster
Switched to branch &#39;faster&#39;

$ /c/lean/bin/lean --profile algebra/big_operators.lean &gt;/dev/null
cumulative profiling times:
        compilation 1.53ms
        decl post-processing 6.86s
        elaboration 7.37s
        elaboration: tactic compilation 561ms
        elaboration: tactic execution 3.82s
        parsing 995ms
        type checking 17.9ms
</pre></div>

#### [ Kenny Lau (Sep 25 2018 at 05:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/134572294):
<p><span class="user-mention" data-user-id="110049">@Mario Carneiro</span></p>

#### [ Kenny Lau (Sep 25 2018 at 05:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/134572336):
<p>elaboration 47.7s --&gt; 7.37s<br>
elaboration: tactic execution 42s --&gt; 3.82s</p>

#### [ Simon Hudon (Sep 25 2018 at 05:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/134572344):
<p>Nice! What did you do?</p>

#### [ Kenny Lau (Sep 25 2018 at 05:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/134572391):
<p>I removed the simp</p>

#### [ Kenny Lau (Sep 25 2018 at 05:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/134572396):
<p>and replaced them with either a term proof or <code>rw</code> or <code>simp only</code></p>

#### [ Simon Hudon (Sep 25 2018 at 05:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/134572472):
<p>How long did it take for each proof?</p>

#### [ Kenny Lau (Sep 25 2018 at 06:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/134572668):
<p><a href="https://gist.github.com/kckennylau/6d1e02b8289f24be38416642b5d91142" target="_blank" title="https://gist.github.com/kckennylau/6d1e02b8289f24be38416642b5d91142">https://gist.github.com/kckennylau/6d1e02b8289f24be38416642b5d91142</a></p>

#### [ Kenny Lau (Sep 25 2018 at 06:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/134572694):
<p><a href="https://github.com/leanprover-community/mathlib/commit/c347e9940c773faf79358b0bf320e73247f51023" target="_blank" title="https://github.com/leanprover-community/mathlib/commit/c347e9940c773faf79358b0bf320e73247f51023">https://github.com/leanprover-community/mathlib/commit/c347e9940c773faf79358b0bf320e73247f51023</a></p>

#### [ Keeley Hoek (Sep 25 2018 at 13:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/134590722):
<p>I've got a setup where I can hook-in to <code>begin</code> blocks and take control away from lean when they occur, and do whatever I want to the <code>texpr</code>s in the <code>begin ... end</code> just by importing a file. One use case is replacing <code>simp</code> by what it did last time and seeing if it works---and saving this in a file to be used again later (the idea I mentioned before). You'd enable it by adding <code>import tactic.caching</code> or something at the top of your file.</p>
<p>This would mean you'd be able to get performance benefits like this without obfuscating the code (but as Scott, or someone else mentioned last time stale caches could break a fresh build for someone else, so you'd have to clear before shipping). If I can get everything working robustly, would anyone hacking on mathlib be willing to try it out?</p>

#### [ Kenny Lau (Sep 25 2018 at 15:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/134596822):
<p>I reckon if we removed all the simp, it can compile in under 10 minutes</p>

#### [ Kenny Lau (Sep 26 2018 at 15:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/134672859):
<div class="codehilite"><pre><span></span>git ls-files *.lean | xargs -I % sh -c &#39;&gt;&amp;2 echo %; /c/lean/bin/lean --profile % &gt;/dev/null;&#39; &gt; profile.txt 2&gt;&amp;1
</pre></div>

#### [ Kenny Lau (Sep 26 2018 at 15:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/134672866):
<p><a href="https://gist.github.com/kckennylau/04917450f71db69f29150d64f360dd0f" target="_blank" title="https://gist.github.com/kckennylau/04917450f71db69f29150d64f360dd0f">https://gist.github.com/kckennylau/04917450f71db69f29150d64f360dd0f</a></p>

#### [ Kenny Lau (Sep 26 2018 at 15:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/134672884):
<p>if A imports B and C, do I need to subtract the times of B and C from the time of A to get a more accurate datum?</p>

#### [ Kenny Lau (Sep 26 2018 at 15:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/134672933):
<p>also, I learnt the hard way that you need to <code>lean --make</code> it before doing this</p>

#### [ Scott Morrison (Sep 26 2018 at 15:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/134674307):
<p>as long as you lean --make beforehand subtraction shouldn't be necessary</p>

#### [ Kenny Lau (Sep 26 2018 at 18:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/134687725):
<p><a href="https://gist.github.com/kckennylau/7cd92fe25114061b706d6c86aa8059ea" target="_blank" title="https://gist.github.com/kckennylau/7cd92fe25114061b706d6c86aa8059ea">https://gist.github.com/kckennylau/7cd92fe25114061b706d6c86aa8059ea</a></p>

#### [ Kenny Lau (Sep 26 2018 at 18:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/134687831):
<p>sorted: <a href="https://gist.github.com/kckennylau/f7c6cbfb2aa8bf7e4784e8c65d6c4852" target="_blank" title="https://gist.github.com/kckennylau/f7c6cbfb2aa8bf7e4784e8c65d6c4852">https://gist.github.com/kckennylau/f7c6cbfb2aa8bf7e4784e8c65d6c4852</a></p>

#### [ Kenny Lau (Sep 26 2018 at 18:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/134687841):
<p>all time in seconds</p>

#### [ Mario Carneiro (Sep 26 2018 at 18:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/134687864):
<p>well I can't say that any of the top ten are a surprise</p>

#### [ Mario Carneiro (Sep 26 2018 at 18:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/134687936):
<p>What do you get if you sort by compile time / length in characters?</p>

#### [ Mario Carneiro (Sep 26 2018 at 18:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/134687960):
<p>the longest files are of course going to take a long time to compile</p>

#### [ Mario Carneiro (Sep 26 2018 at 18:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/134687974):
<p>what do the multiple numbers mean in the first gist?</p>

#### [ Kenny Lau (Sep 26 2018 at 18:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/134688034):
<p>so a raw datum looks like:</p>
<div class="codehilite"><pre><span></span>cumulative profiling times:
        compilation 253ms
        decl post-processing 2.84s
        elaboration 114s
        elaboration: tactic compilation 3.57s
        elaboration: tactic execution 86.9s
        parsing 5.23s
        type checking 229ms
</pre></div>

#### [ Kenny Lau (Sep 26 2018 at 18:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/134688037):
<p>I filtered out the <code>ms</code></p>

#### [ Kenny Lau (Sep 26 2018 at 18:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/134688040):
<p>and listed each item</p>

#### [ Kenny Lau (Sep 26 2018 at 18:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/134688045):
<p>and added the numbers together in the last gist</p>

#### [ Kenny Lau (Sep 26 2018 at 18:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/134688450):
<p><a href="https://gist.github.com/kckennylau/7318d851eca2f951e7acdaa6ffbe65b7" target="_blank" title="https://gist.github.com/kckennylau/7318d851eca2f951e7acdaa6ffbe65b7">https://gist.github.com/kckennylau/7318d851eca2f951e7acdaa6ffbe65b7</a></p>

#### [ Kenny Lau (Sep 26 2018 at 18:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/134688451):
<p><span class="user-mention" data-user-id="110049">@Mario Carneiro</span> ^</p>

#### [ Mario Carneiro (Sep 26 2018 at 18:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/134688562):
<p>complex/basic is a surprise</p>

#### [ Kenny Lau (Sep 26 2018 at 18:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/134688753):
<div class="codehilite"><pre><span></span>elaboration: tactic execution took 1.31s
elaboration of ext_iff took 1.45s
elaboration: tactic execution took 1.51s
elaboration of of_real_neg took 1.6s
elaboration of mk_eq_add_mul_I took 1.62s
elaboration: tactic execution took 1.61s
elaboration of of_real_mul took 1.75s
elaboration: tactic execution took 1.26s
elaboration of re_add_im took 1.37s
elaboration: tactic execution took 1.08s
elaboration of conj_of_real took 1.17s
elaboration of conj_I took 1.16s
elaboration: tactic execution took 1.38s
elaboration of conj_add took 1.5s
elaboration: tactic execution took 2.08s
elaboration of conj_neg took 2.22s
elaboration: tactic execution took 1.99s
elaboration of conj_conj took 2.14s
elaboration: tactic execution took 2.22s
elaboration of conj_mul took 2.39s
elaboration: tactic execution took 2s
elaboration of conj_eq_zero took 2.13s
elaboration: tactic execution took 1.32s
elaboration of norm_sq_of_real took 1.45s
elaboration: tactic execution took 1.23s
elaboration of norm_sq_zero took 1.35s
elaboration of norm_sq_one took 1.4s
elaboration: tactic execution took 1.24s
elaboration of norm_sq_I took 1.35s
elaboration: tactic execution took 1.19s
elaboration of norm_sq_pos took 1.27s
elaboration: tactic execution took 1.27s
elaboration of norm_sq_neg took 1.37s
elaboration: tactic execution took 1.23s
elaboration of norm_sq_conj took 1.34s
elaboration: tactic execution took 1.49s
elaboration of norm_sq_mul took 1.6s
elaboration: tactic execution took 1.13s
elaboration of norm_sq_add took 1.22s
elaboration of add_conj took 1.14s
elaboration: tactic execution took 1.17s
elaboration of mul_conj took 1.29s
elaboration: tactic execution took 2.3s
elaboration of comm_ring took 3.35s
elaboration of inv_im took 1.06s
elaboration of inv_re took 1.09s
elaboration: tactic execution took 1.05s
elaboration of sub_conj took 1.14s
elaboration: tactic execution took 1.04s
elaboration of norm_sq_sub took 1.13s
elaboration: tactic execution took 1.29s
elaboration: tactic execution took 1.01s
elaboration of of_real_inv took 1.71s
elaboration of conj_inv took 1.54s
elaboration: tactic execution took 1.3s
elaboration of norm_sq_inv took 1.51s
elaboration: tactic execution took 1.36s
elaboration of of_real_int_cast took 1.9s
elaboration of abs_of_real took 1.01s
elaboration of re_eq_add_conj took 1.06s
elaboration: tactic execution took 1.22s
elaboration of of_real_rat_cast took 1.32s
elaboration of abs_conj took 1.04s
elaboration: tactic execution took 1.05s
elaboration of abs_add took 1.18s
elaboration: tactic execution took 1.02s
elaboration of abs_le_abs_re_add_abs_im took 1.11s
elaboration: tactic execution took 1.1s
elaboration of is_cau_seq_re took 1.24s
elaboration: tactic execution took 1.1s
elaboration of is_cau_seq_im took 1.27s
elaboration: tactic execution took 1.02s
elaboration of equiv_lim took 1.44s
</pre></div>

#### [ Kenny Lau (Sep 26 2018 at 18:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/134688766):
<p>that's <code>grep /\d+(\.\d+)?s/</code></p>

#### [ Kenny Lau (Sep 26 2018 at 18:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/134688816):
<p>(I know, I should have done <code>grep /\d+s/</code></p>

#### [ Kenny Lau (Sep 26 2018 at 18:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/134688835):
<p>also, 47 usages of <code>simp</code></p>

#### [ Kenny Lau (Sep 26 2018 at 18:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/134688842):
<p>that's <code>/^simp|^.simp|[^@].simp/</code> because VScode doesn't have lookbehind</p>

#### [ Kenny Lau (Sep 26 2018 at 19:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/134688935):
<p><span class="user-mention" data-user-id="110049">@Mario Carneiro</span> what do you think?</p>

#### [ Mario Carneiro (Sep 26 2018 at 19:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/134689238):
<p>Here are the top 30 files on the second list that take more than 100 seconds:</p>
<div class="codehilite"><pre><span></span>data/complex/basic.lean                   0.008525  104.10
data/finset.lean                          0.006419  359.15
order/conditionally_complete_lattice.lean 0.005851  152.78
data/polynomial.lean                      0.004392  213.90
data/finsupp.lean                         0.003828  121.20
group_theory/perm.lean                    0.003750  101.33
set_theory/ordinal.lean                   0.003531  397.60
linear_algebra/basic.lean                 0.003494  123.04
analysis/topology/topological_space.lean  0.002850  161.68
</pre></div>


<p>I suggest focusing on these</p>

#### [ Kenny Lau (Sep 26 2018 at 19:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/134689380):
<p>ok</p>

#### [ Mario Carneiro (Sep 26 2018 at 19:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/134689383):
<p>if you can decrease the compile times of all of these by half that will take 15 minutes off the total compile time, or 30%</p>

#### [ Chris Hughes (Sep 26 2018 at 19:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/134690262):
<p>A ton of lemmas in <code>complex.basic</code> are <code>rfl</code>, but were proved with <code>simp</code></p>

#### [ Chris Hughes (Sep 26 2018 at 19:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/134692162):
<blockquote>
<p>A ton of lemmas in <code>complex.basic</code> are <code>rfl</code>, but were proved with <code>simp</code></p>
</blockquote>
<p><span class="user-mention" data-user-id="110064">@Kenny Lau</span> I just pushed some improvements to <code>complex.basic</code></p>

#### [ Kenny Lau (Sep 26 2018 at 19:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/134692189):
<p>thanks!</p>

#### [ Kenny Lau (Sep 28 2018 at 20:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/134841829):
<p>before:</p>
<div class="codehilite"><pre><span></span>data/finset.lean
cumulative profiling times:
    compilation 138ms
    decl post-processing 178ms
    elaboration 173s
    elaboration: tactic compilation 1.83s
    elaboration: tactic execution 182s
    parsing 2.32s
    type checking 125ms
</pre></div>


<p>after:</p>
<div class="codehilite"><pre><span></span>cumulative profiling times:
        compilation 85.2ms
        decl post-processing 130ms
        elaboration 10.2s
        elaboration: tactic compilation 1.06s
        elaboration: tactic execution 4.98s
        parsing 1.48s
        type checking 90ms
</pre></div>

#### [ Kenny Lau (Sep 28 2018 at 20:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/134841841):
<p><span class="user-mention" data-user-id="110049">@Mario Carneiro</span> that's way more than a 70% reduction :P</p>

#### [ Bryan Gin-ge Chen (Sep 28 2018 at 20:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/134841994):
<p>That's awesome! Since I've been working almost exclusively with finset recently, I hope this gets in soon!</p>

#### [ Kevin Buzzard (Sep 28 2018 at 21:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/134844724):
<p>Very impressive Kenny. Is this all changing <code>simp</code> to <code>simp only</code>?</p>

#### [ Simon Hudon (Sep 28 2018 at 21:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/134847149):
<p>I'm going start an experiment to see if my idea for <code>squeeze_simp</code> is worthwhile. Is anybody else working on optimizing <code>conditionally_complete_lattice.lean</code>?</p>

#### [ Kenny Lau (Sep 28 2018 at 22:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/134850447):
<p>I'm going to work on <code>ordinal.lean</code> now</p>

#### [ Johan Commelin (Sep 29 2018 at 07:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/134869784):
<p><span class="user-mention" data-user-id="110026">@Simon Hudon</span> How much improvement did <code>squeeze_simp</code> give in your experiment? Does it approach the magical 70%?</p>

#### [ Simon Hudon (Sep 29 2018 at 08:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/134871081):
<p>Yes, the file initially took 35s process, then, I used <code>squeeze_simp</code> and it went down to 11s.</p>

#### [ Kenny Lau (Sep 29 2018 at 10:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/134873374):
<div class="codehilite"><pre><span></span><span class="kn">theorem</span> <span class="n">mul_le_of_limit</span> <span class="o">{</span><span class="n">a</span> <span class="n">b</span> <span class="n">c</span> <span class="o">:</span> <span class="n">ordinal</span><span class="bp">.</span><span class="o">{</span><span class="n">u</span><span class="o">}}</span>
  <span class="o">(</span><span class="n">h</span> <span class="o">:</span> <span class="n">is_limit</span> <span class="n">b</span><span class="o">)</span> <span class="o">:</span> <span class="n">a</span> <span class="bp">*</span> <span class="n">b</span> <span class="bp">≤</span> <span class="n">c</span> <span class="bp">↔</span> <span class="bp">∀</span> <span class="n">b&#39;</span> <span class="bp">&lt;</span> <span class="n">b</span><span class="o">,</span> <span class="n">a</span> <span class="bp">*</span> <span class="n">b&#39;</span> <span class="bp">≤</span> <span class="n">c</span> <span class="o">:=</span>
<span class="bp">⟨λ</span> <span class="n">h</span> <span class="n">b&#39;</span> <span class="n">l</span><span class="o">,</span> <span class="n">le_trans</span> <span class="o">(</span><span class="n">mul_le_mul_left</span> <span class="bp">_</span> <span class="o">(</span><span class="n">le_of_lt</span> <span class="n">l</span><span class="o">))</span> <span class="n">h</span><span class="o">,</span>
<span class="bp">λ</span> <span class="n">H</span><span class="o">,</span> <span class="n">le_of_not_lt</span> <span class="err">$</span>
<span class="n">induction_on</span> <span class="n">a</span> <span class="o">(</span><span class="bp">λ</span> <span class="n">α</span> <span class="n">r</span> <span class="bp">_</span><span class="o">,</span> <span class="n">induction_on</span> <span class="n">b</span> <span class="err">$</span> <span class="bp">λ</span> <span class="n">β</span> <span class="n">s</span> <span class="bp">_</span> <span class="n">h</span> <span class="n">H</span> <span class="n">l</span><span class="o">,</span> <span class="k">begin</span>
<span class="n">try_for</span> <span class="mi">300</span> <span class="o">{</span>
  <span class="n">resetI</span><span class="o">,</span>
  <span class="n">suffices</span> <span class="o">:</span> <span class="bp">∀</span> <span class="n">a</span> <span class="n">b</span><span class="o">,</span> <span class="n">prod</span><span class="bp">.</span><span class="n">lex</span> <span class="n">s</span> <span class="n">r</span> <span class="o">(</span><span class="n">b</span><span class="o">,</span> <span class="n">a</span><span class="o">)</span> <span class="o">(</span><span class="n">enum</span> <span class="bp">_</span> <span class="bp">_</span> <span class="n">l</span><span class="o">),</span>
  <span class="o">{</span> <span class="n">cases</span> <span class="n">enum</span> <span class="bp">_</span> <span class="bp">_</span> <span class="n">l</span> <span class="k">with</span> <span class="n">b</span> <span class="n">a</span><span class="o">,</span> <span class="n">exact</span> <span class="n">irrefl</span> <span class="bp">_</span> <span class="o">(</span><span class="n">this</span> <span class="bp">_</span> <span class="bp">_</span><span class="o">)</span> <span class="o">},</span>
  <span class="n">intros</span> <span class="n">a</span> <span class="n">b</span><span class="o">,</span>
  <span class="n">rw</span> <span class="o">[</span><span class="err">←</span> <span class="n">typein_lt_typein</span> <span class="o">(</span><span class="n">prod</span><span class="bp">.</span><span class="n">lex</span> <span class="n">s</span> <span class="n">r</span><span class="o">),</span> <span class="n">typein_enum</span><span class="o">],</span>
  <span class="k">have</span> <span class="o">:=</span> <span class="n">H</span> <span class="bp">_</span> <span class="o">(</span><span class="n">h</span><span class="bp">.</span><span class="mi">2</span> <span class="bp">_</span> <span class="o">(</span><span class="n">typein_lt_type</span> <span class="n">s</span> <span class="n">b</span><span class="o">)),</span>
  <span class="n">rw</span> <span class="o">[</span><span class="n">mul_succ</span><span class="o">]</span> <span class="n">at</span> <span class="n">this</span><span class="o">,</span>
  <span class="k">have</span> <span class="o">:=</span> <span class="n">lt_of_lt_of_le</span> <span class="o">((</span><span class="n">add_lt_add_iff_left</span> <span class="bp">_</span><span class="o">)</span><span class="bp">.</span><span class="mi">2</span>
    <span class="o">(</span><span class="n">typein_lt_type</span> <span class="bp">_</span> <span class="n">a</span><span class="o">))</span> <span class="n">this</span><span class="o">,</span>
  <span class="n">refine</span> <span class="n">lt_of_le_of_lt</span> <span class="bp">_</span> <span class="n">this</span><span class="o">,</span>
  <span class="n">refine</span> <span class="o">(</span><span class="n">type_le&#39;</span><span class="bp">.</span><span class="mi">2</span> <span class="bp">_</span><span class="o">),</span>
  <span class="n">constructor</span><span class="o">,</span>
<span class="o">},</span> <span class="n">try_for</span> <span class="mi">800</span> <span class="o">{</span>
  <span class="n">refine</span> <span class="n">order_embedding</span><span class="bp">.</span><span class="n">of_monotone</span> <span class="o">(</span><span class="bp">λ</span> <span class="n">a</span><span class="o">,</span> <span class="bp">_</span><span class="o">)</span> <span class="o">(</span><span class="bp">λ</span> <span class="n">a</span> <span class="n">b</span><span class="o">,</span> <span class="bp">_</span><span class="o">),</span>
<span class="o">},</span>

<span class="c">/-</span><span class="cm">  { rcases a with ⟨⟨b&#39;, a&#39;⟩, h⟩,</span>
<span class="cm">    by_cases e : b = b&#39;,</span>
<span class="cm">    { refine sum.inr ⟨a&#39;, _⟩,</span>
<span class="cm">      subst e, cases h with _ _ _ _ h _ _ _ h,</span>
<span class="cm">      { exact (irrefl _ h).elim },</span>
<span class="cm">      { exact h } },</span>
<span class="cm">    { refine sum.inl (⟨b&#39;, _⟩, a&#39;),</span>
<span class="cm">      cases h with _ _ _ _ h _ _ _ h,</span>
<span class="cm">      { exact h }, { exact (e rfl).elim } } },</span>
<span class="cm">  { rcases a with ⟨⟨b₁, a₁⟩, h₁⟩,</span>
<span class="cm">    rcases b with ⟨⟨b₂, a₂⟩, h₂⟩,</span>
<span class="cm">    intro h, by_cases e₁ : b = b₁; by_cases e₂ : b = b₂,</span>
<span class="cm">    { substs b₁ b₂, simpa only [subrel_val, prod.lex_def, @irrefl _ s _ b, true_and, false_or, eq_self_iff_true, dif_pos, sum.lex_inr_inr] using h },</span>
<span class="cm">    { subst b₁, simp only [subrel_val, prod.lex_def, e₂, prod.lex_def, dif_pos, subrel_val, eq_self_iff_true, or_false, dif_neg, not_false_iff, sum.lex_inr_inl, false_and] at h ⊢,</span>
<span class="cm">      cases h₂; [exact asymm h h₂_h, exact e₂ rfl] },</span>
<span class="cm">    { squeeze_simp [e₁, e₂, dif_pos, eq_self_iff_true, dif_neg, not_false_iff, sum.lex.sep] },</span>
<span class="cm">    { simpa only [dif_neg e₁, dif_neg e₂, prod.lex_def, subrel_val, subtype.mk_eq_mk, sum.lex_inl_inl] using h } }-/</span>
<span class="kn">end</span><span class="o">)</span> <span class="n">h</span> <span class="n">H</span><span class="bp">⟩</span>
</pre></div>

#### [ Kenny Lau (Sep 29 2018 at 10:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/134873377):
<p><span class="user-mention" data-user-id="110049">@Mario Carneiro</span> this is your file</p>

#### [ Kenny Lau (Sep 29 2018 at 10:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/134873382):
<p>I don't know what to do with this</p>

#### [ Mario Carneiro (Sep 29 2018 at 10:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/134873432):
<p>what's the question?</p>

#### [ Kenny Lau (Sep 29 2018 at 10:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/134873433):
<p>that one line takes 800 ms</p>

#### [ Kenny Lau (Sep 29 2018 at 10:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/134873435):
<p>not to mention the lines afterwards</p>

#### [ Kenny Lau (Sep 29 2018 at 10:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/134873436):
<p>somehow <code>order_embedding.of_monotone</code> is an expensive definition</p>

#### [ Kenny Lau (Sep 29 2018 at 10:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/134873437):
<p>(it isn't a thoerem)</p>

#### [ Kenny Lau (Sep 29 2018 at 10:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/134873478):
<p>how can I make it faster?</p>

#### [ Mario Carneiro (Sep 29 2018 at 10:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/134873494):
<p>I will let you know when my lean catches up to that definition :P</p>

#### [ Mario Carneiro (Sep 29 2018 at 10:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/134873495):
<p>if only it compiled faster...</p>

#### [ Kenny Lau (Sep 29 2018 at 10:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/134873534):
<p>right, ironic</p>

#### [ Kenny Lau (Sep 29 2018 at 10:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/134873545):
<p>I wonder if anyone is working on it</p>

#### [ Mario Carneiro (Sep 29 2018 at 10:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/134873548):
<p>Anyway, you can always skip it and return later</p>

#### [ Kenny Lau (Sep 29 2018 at 10:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/134873556):
<p>right</p>

#### [ Mario Carneiro (Sep 29 2018 at 10:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/134873558):
<p>I doubt anyone is working on <code>ordinal</code> other than you right now</p>

#### [ Johan Commelin (Sep 29 2018 at 10:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/134873941):
<p><span class="user-mention" data-user-id="110026">@Simon Hudon</span> Any chance you can register the hole command? After that we could easily distribute the work to everyone who has a couple of spare minutes.</p>

#### [ Simon Hudon (Sep 29 2018 at 10:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/134874557):
<p>The hole command is not trivial to build because I have to come up with a syntax for the expression found in the hole. It has to allow the encoding of information such as <code>simp! [h0,h1] with attr at *</code>. I'm going to postpone that until I have a better idea on how to do it. In the mean time, if you have <code>simp! [h0,h1] with attr at *</code>, simply replace it with <code>squeeze_simp! [h0,h1] with attr at *</code> and it will print out a replacement that you simply have to copy and paste. That same also works for <code>simpa</code></p>

#### [ Johan Commelin (Sep 29 2018 at 10:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/134874570):
<p>Ok, cool!</p>

#### [ Johan Commelin (Sep 29 2018 at 10:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/134874575):
<p>Thanks a lot for this.</p>

#### [ Simon Hudon (Sep 29 2018 at 10:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/134874583):
<p><span class="emoji emoji-1f44d" title="+1">:+1:</span></p>

#### [ Simon Hudon (Sep 29 2018 at 10:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/134874623):
<p>Now I should really get some sleep :) Best of luck</p>

#### [ Johan Commelin (Sep 29 2018 at 10:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/134874839):
<p>Sleep tight <span class="emoji emoji-1f6cc" title="in bed">:in_bed:</span></p>

#### [ Johan Commelin (Sep 29 2018 at 11:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/134875338):
<p>Hmm, I have proofs where <code>by simp</code> works, but <code>by squeeze_simp</code> fails. E.g., line 157 of <code>order/filter.lean</code>.</p>

#### [ Johan Commelin (Sep 29 2018 at 19:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/134889142):
<p>I <code>squeeze_simp</code>ed <code>order/filter.lean</code>. I didn't time carefully but I think I got the compile time down to maybe 25s.</p>

#### [ Kenny Lau (Sep 29 2018 at 21:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/134893202):
<blockquote>
<p>I <code>squeeze_simp</code>ed <code>order/filter.lean</code>. I didn't time carefully but I think I got the compile time down to maybe 25s.</p>
</blockquote>
<p>from what?</p>

#### [ Johan Commelin (Sep 29 2018 at 21:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/134893462):
<p>I think your gist said something like 150s</p>

#### [ Johan Commelin (Sep 29 2018 at 21:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/134893465):
<p>But I don't have good tools to time an entire file</p>

#### [ Johan Commelin (Sep 29 2018 at 21:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/134893468):
<p>I did see pretty nice speed-ups from some of the substitutions</p>

#### [ Kenny Lau (Sep 29 2018 at 21:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/134893517):
<p>the time on my gist is relative to me and my computer</p>

#### [ Simon Hudon (Sep 29 2018 at 21:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/134893916):
<p><span class="user-mention" data-user-id="112680">@Johan Commelin</span> In emacs at least, there's a <code>lean-std-exe</code> command. It will compile the current file, tell you the time at which it starts and the time at which it ends.</p>

#### [ Kenny Lau (Sep 29 2018 at 22:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/134894297):
<div class="codehilite"><pre><span></span><span class="kn">theorem</span> <span class="n">add_le_add_left</span> <span class="o">{</span><span class="n">a</span> <span class="n">b</span> <span class="o">:</span> <span class="n">ordinal</span><span class="o">}</span> <span class="o">:</span> <span class="n">a</span> <span class="bp">≤</span> <span class="n">b</span> <span class="bp">→</span> <span class="bp">∀</span> <span class="n">c</span><span class="o">,</span> <span class="n">c</span> <span class="bp">+</span> <span class="n">a</span> <span class="bp">≤</span> <span class="n">c</span> <span class="bp">+</span> <span class="n">b</span> <span class="o">:=</span>
<span class="n">induction_on</span> <span class="n">a</span> <span class="err">$</span> <span class="bp">λ</span> <span class="n">α₁</span> <span class="n">r₁</span> <span class="bp">_</span><span class="o">,</span> <span class="n">induction_on</span> <span class="n">b</span> <span class="err">$</span> <span class="bp">λ</span> <span class="n">α₂</span> <span class="n">r₂</span> <span class="bp">_</span> <span class="bp">⟨⟨⟨</span><span class="n">f</span><span class="o">,</span> <span class="n">fo</span><span class="bp">⟩</span><span class="o">,</span> <span class="n">fi</span><span class="bp">⟩⟩</span> <span class="n">c</span><span class="o">,</span>
<span class="n">induction_on</span> <span class="n">c</span> <span class="err">$</span> <span class="bp">λ</span> <span class="n">β</span> <span class="n">s</span> <span class="bp">_</span><span class="o">,</span>
<span class="bp">⟨⟨⟨</span><span class="o">(</span><span class="n">embedding</span><span class="bp">.</span><span class="n">refl</span> <span class="bp">_</span><span class="o">)</span><span class="bp">.</span><span class="n">sum_congr</span> <span class="n">f</span><span class="o">,</span>
  <span class="bp">λ</span> <span class="n">a</span> <span class="n">b</span><span class="o">,</span> <span class="k">begin</span> <span class="n">try_for</span> <span class="mi">200</span> <span class="o">{</span> <span class="n">cases</span> <span class="n">a</span> <span class="k">with</span> <span class="n">a</span> <span class="n">a</span><span class="bp">;</span> <span class="n">cases</span> <span class="n">b</span> <span class="k">with</span> <span class="n">b</span> <span class="n">b</span><span class="bp">;</span>
    <span class="n">split</span><span class="bp">;</span> <span class="n">intro</span> <span class="n">H</span><span class="bp">;</span> <span class="n">cases</span> <span class="n">H</span> <span class="k">with</span> <span class="bp">_</span> <span class="bp">_</span> <span class="n">H</span> <span class="bp">_</span> <span class="bp">_</span> <span class="n">H</span> <span class="bp">_</span> <span class="bp">_</span> <span class="n">H</span><span class="bp">;</span> <span class="n">constructor</span><span class="o">,</span>
    <span class="o">{</span> <span class="n">assumption</span> <span class="o">},</span> <span class="o">{</span> <span class="n">assumption</span> <span class="o">},</span>
    <span class="o">{</span> <span class="n">rw</span> <span class="err">←</span> <span class="n">fo</span><span class="o">,</span> <span class="n">assumption</span> <span class="o">},</span> <span class="o">{</span> <span class="n">rw</span> <span class="n">fo</span><span class="o">,</span> <span class="n">assumption</span> <span class="o">}</span> <span class="o">}</span>
  <span class="kn">end</span><span class="bp">⟩</span><span class="o">,</span>
  <span class="bp">λ</span> <span class="n">a</span> <span class="n">b</span> <span class="n">H</span><span class="o">,</span> <span class="k">begin</span> <span class="n">try_for</span> <span class="mi">200</span> <span class="o">{</span> <span class="n">cases</span> <span class="n">b</span> <span class="k">with</span> <span class="n">b</span> <span class="n">b</span><span class="o">,</span> <span class="o">{</span> <span class="n">exact</span> <span class="bp">⟨</span><span class="n">sum</span><span class="bp">.</span><span class="n">inl</span> <span class="n">b</span><span class="o">,</span> <span class="n">rfl</span><span class="bp">⟩</span> <span class="o">},</span>
    <span class="n">cases</span> <span class="n">a</span> <span class="k">with</span> <span class="n">a</span> <span class="n">a</span><span class="o">,</span> <span class="o">{</span><span class="n">cases</span> <span class="n">H</span><span class="o">},</span>
    <span class="n">cases</span> <span class="n">fi</span> <span class="bp">_</span> <span class="bp">_</span> <span class="o">(</span><span class="n">sum</span><span class="bp">.</span><span class="n">lex_inr_inr</span><span class="bp">.</span><span class="mi">1</span> <span class="n">H</span><span class="o">)</span> <span class="k">with</span> <span class="n">w</span> <span class="n">h</span><span class="o">,</span> <span class="n">exact</span> <span class="bp">⟨</span><span class="n">sum</span><span class="bp">.</span><span class="n">inr</span> <span class="n">w</span><span class="o">,</span> <span class="n">congr_arg</span> <span class="n">sum</span><span class="bp">.</span><span class="n">inr</span> <span class="n">h</span><span class="bp">⟩</span> <span class="o">}</span>
  <span class="kn">end</span><span class="bp">⟩⟩</span>
</pre></div>

#### [ Kenny Lau (Sep 29 2018 at 22:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/134894298):
<p>I'm at a bit of a loss here</p>

#### [ Kenny Lau (Sep 29 2018 at 22:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/134894299):
<p>both blocks take &lt; 200 ms</p>

#### [ Kenny Lau (Sep 29 2018 at 22:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/134894303):
<p>but the whole thing takes 5 s</p>

#### [ Chris Hughes (Sep 29 2018 at 22:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/134894935):
<p>Presumably some elaboration is taking ages then? Computing lots of motives.</p>

#### [ Kenny Lau (Sep 29 2018 at 22:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/134894939):
<p>i'm trying to convert it to term mode</p>

#### [ Kenny Lau (Sep 29 2018 at 22:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/134895382):
<p>solved using term mode</p>

#### [ Kenny Lau (Sep 29 2018 at 22:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/134895383):
<div class="codehilite"><pre><span></span><span class="kn">theorem</span> <span class="n">add_le_add_left</span> <span class="o">{</span><span class="n">a</span> <span class="n">b</span> <span class="o">:</span> <span class="n">ordinal</span><span class="o">}</span> <span class="o">:</span> <span class="n">a</span> <span class="bp">≤</span> <span class="n">b</span> <span class="bp">→</span> <span class="bp">∀</span> <span class="n">c</span><span class="o">,</span> <span class="n">c</span> <span class="bp">+</span> <span class="n">a</span> <span class="bp">≤</span> <span class="n">c</span> <span class="bp">+</span> <span class="n">b</span> <span class="o">:=</span>
<span class="n">induction_on</span> <span class="n">a</span> <span class="err">$</span> <span class="bp">λ</span> <span class="n">α₁</span> <span class="n">r₁</span> <span class="bp">_</span><span class="o">,</span> <span class="n">induction_on</span> <span class="n">b</span> <span class="err">$</span> <span class="bp">λ</span> <span class="n">α₂</span> <span class="n">r₂</span> <span class="bp">_</span> <span class="bp">⟨⟨⟨</span><span class="n">f</span><span class="o">,</span> <span class="n">fo</span><span class="bp">⟩</span><span class="o">,</span> <span class="n">fi</span><span class="bp">⟩⟩</span> <span class="n">c</span><span class="o">,</span>
<span class="n">induction_on</span> <span class="n">c</span> <span class="err">$</span> <span class="bp">λ</span> <span class="n">β</span> <span class="n">s</span> <span class="bp">_</span><span class="o">,</span>
<span class="bp">⟨⟨⟨</span><span class="o">(</span><span class="n">embedding</span><span class="bp">.</span><span class="n">refl</span> <span class="bp">_</span><span class="o">)</span><span class="bp">.</span><span class="n">sum_congr</span> <span class="n">f</span><span class="o">,</span>
  <span class="bp">λ</span> <span class="n">a</span> <span class="n">b</span><span class="o">,</span> <span class="bp">⟨λ</span> <span class="n">H</span><span class="o">,</span> <span class="n">sum</span><span class="bp">.</span><span class="n">lex</span><span class="bp">.</span><span class="n">rec_on</span> <span class="n">H</span> <span class="o">(</span><span class="bp">λ</span> <span class="bp">_</span> <span class="bp">_</span><span class="o">,</span> <span class="n">sum</span><span class="bp">.</span><span class="n">lex_inl_inl</span><span class="bp">.</span><span class="mi">2</span><span class="o">)</span>
      <span class="o">(</span><span class="bp">λ</span> <span class="bp">_</span> <span class="bp">_</span> <span class="n">h</span><span class="o">,</span> <span class="n">sum</span><span class="bp">.</span><span class="n">lex_inr_inr</span><span class="bp">.</span><span class="mi">2</span> <span class="err">$</span> <span class="n">fo</span><span class="bp">.</span><span class="mi">1</span> <span class="n">h</span><span class="o">)</span> <span class="o">(</span><span class="bp">λ</span> <span class="bp">_</span> <span class="bp">_</span><span class="o">,</span> <span class="n">sum</span><span class="bp">.</span><span class="n">lex</span><span class="bp">.</span><span class="n">sep</span> <span class="bp">_</span> <span class="bp">_</span> <span class="bp">_</span> <span class="bp">_</span><span class="o">),</span>
    <span class="n">sum</span><span class="bp">.</span><span class="n">rec_on</span> <span class="n">a</span> <span class="o">(</span><span class="bp">λ</span> <span class="n">a</span><span class="o">,</span> <span class="n">sum</span><span class="bp">.</span><span class="n">rec_on</span> <span class="n">b</span> <span class="o">(</span><span class="bp">λ</span> <span class="n">b</span><span class="o">,</span> <span class="n">sum</span><span class="bp">.</span><span class="n">lex_inl_inl</span><span class="bp">.</span><span class="mi">2</span> <span class="err">∘</span> <span class="n">sum</span><span class="bp">.</span><span class="n">lex_inl_inl</span><span class="bp">.</span><span class="mi">1</span><span class="o">)</span>
        <span class="o">(</span><span class="bp">λ</span> <span class="bp">_</span> <span class="bp">_</span><span class="o">,</span> <span class="n">sum</span><span class="bp">.</span><span class="n">lex</span><span class="bp">.</span><span class="n">sep</span> <span class="bp">_</span> <span class="bp">_</span> <span class="bp">_</span> <span class="bp">_</span><span class="o">))</span>
      <span class="o">(</span><span class="bp">λ</span> <span class="n">a</span><span class="o">,</span> <span class="n">sum</span><span class="bp">.</span><span class="n">rec_on</span> <span class="n">b</span> <span class="o">(</span><span class="bp">λ</span> <span class="n">b</span><span class="o">,</span> <span class="n">false</span><span class="bp">.</span><span class="n">elim</span> <span class="err">∘</span> <span class="n">sum</span><span class="bp">.</span><span class="n">lex_inr_inl</span><span class="o">)</span>
        <span class="o">(</span><span class="bp">λ</span> <span class="n">b</span><span class="o">,</span> <span class="n">sum</span><span class="bp">.</span><span class="n">lex_inr_inr</span><span class="bp">.</span><span class="mi">2</span> <span class="err">∘</span> <span class="n">fo</span><span class="bp">.</span><span class="mi">2</span> <span class="err">∘</span> <span class="n">sum</span><span class="bp">.</span><span class="n">lex_inr_inr</span><span class="bp">.</span><span class="mi">1</span><span class="o">))</span><span class="bp">⟩⟩</span><span class="o">,</span>
  <span class="bp">λ</span> <span class="n">a</span> <span class="n">b</span><span class="o">,</span> <span class="n">sum</span><span class="bp">.</span><span class="n">rec_on</span> <span class="n">b</span> <span class="o">(</span><span class="bp">λ</span> <span class="bp">_</span> <span class="bp">_</span><span class="o">,</span> <span class="bp">⟨</span><span class="n">sum</span><span class="bp">.</span><span class="n">inl</span> <span class="bp">_</span><span class="o">,</span> <span class="n">rfl</span><span class="bp">⟩</span><span class="o">)</span>
    <span class="o">(</span><span class="bp">λ</span> <span class="n">b</span><span class="o">,</span> <span class="n">sum</span><span class="bp">.</span><span class="n">rec_on</span> <span class="n">a</span> <span class="o">(</span><span class="bp">λ</span> <span class="n">a</span><span class="o">,</span> <span class="n">false</span><span class="bp">.</span><span class="n">elim</span> <span class="err">∘</span> <span class="n">sum</span><span class="bp">.</span><span class="n">lex_inr_inl</span><span class="o">)</span>
      <span class="o">(</span><span class="bp">λ</span> <span class="n">a</span> <span class="n">H</span><span class="o">,</span> <span class="k">let</span> <span class="bp">⟨</span><span class="n">w</span><span class="o">,</span> <span class="n">h</span><span class="bp">⟩</span> <span class="o">:=</span> <span class="n">fi</span> <span class="bp">_</span> <span class="bp">_</span> <span class="o">(</span><span class="n">sum</span><span class="bp">.</span><span class="n">lex_inr_inr</span><span class="bp">.</span><span class="mi">1</span> <span class="n">H</span><span class="o">)</span> <span class="k">in</span>
        <span class="bp">⟨</span><span class="n">sum</span><span class="bp">.</span><span class="n">inr</span> <span class="n">w</span><span class="o">,</span> <span class="n">congr_arg</span> <span class="n">sum</span><span class="bp">.</span><span class="n">inr</span> <span class="n">h</span><span class="bp">⟩</span><span class="o">))</span><span class="bp">⟩⟩</span>
</pre></div>

#### [ Kenny Lau (Sep 29 2018 at 22:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/134895385):
<p>&lt; 500 ms</p>

#### [ Patrick Massot (Sep 29 2018 at 22:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/134895440):
<p>Is this copy and pasting the proof term built by tactic mode?</p>

#### [ Kenny Lau (Sep 29 2018 at 22:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/134895441):
<p>hardly</p>

#### [ Kenny Lau (Sep 29 2018 at 22:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/134895442):
<p>I built the proof myself</p>

#### [ Reid Barton (Sep 29 2018 at 22:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/134895494):
<p>hand-crafted artisanal proofs</p>

#### [ Kenny Lau (Sep 30 2018 at 00:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/134898707):
<p>set_theory/ordinal.lean<br>
before:</p>
<div class="codehilite"><pre><span></span>cumulative profiling times:
    compilation 75.5ms
    decl post-processing 255ms
    elaboration 208s
    elaboration: tactic compilation 3.75s
    elaboration: tactic execution 179s
    parsing 6.85s
    type checking 155ms
</pre></div>


<p>after:</p>
<div class="codehilite"><pre><span></span>cumulative profiling times:
        compilation 81.1ms
        decl post-processing 286ms
        elaboration 39.8s
        elaboration: tactic compilation 3.67s
        elaboration: tactic execution 16.9s
        parsing 6.22s
        type checking 165ms
</pre></div>

#### [ Kenny Lau (Sep 30 2018 at 00:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/134898752):
<p>I really wish Mario could help me speed up this file</p>

#### [ Kenny Lau (Sep 30 2018 at 00:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/134898756):
<p>there are some parts that I can't speed up</p>

#### [ Kenny Lau (Sep 30 2018 at 00:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/134898873):
<p>also, which one of the number is (closest to) the actual build time?</p>

#### [ Kevin Buzzard (Sep 30 2018 at 01:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/134899347):
<blockquote>
<p>also, which one of the number is (closest to) the actual build time?</p>
</blockquote>
<p>The largest one.</p>

#### [ Kevin Buzzard (Sep 30 2018 at 01:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/134900435):
<blockquote>
<p>I really wish Mario could help me speed up this file</p>
</blockquote>
<p>He's busy with modules, leave him be ;-)</p>

#### [ Kevin Buzzard (Sep 30 2018 at 01:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/134900438):
<p>After he does modules you can do algebraic closure remember!</p>

#### [ Mario Carneiro (Sep 30 2018 at 02:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/134901088):
<blockquote>
<p>i'm trying to convert it to term mode</p>
</blockquote>
<p>Is there a particular reason you are doing this? I don't think that converting to term mode is necessarily an improvement; in particular some tactics like <code>rw</code> and <code>induction</code> can actually be faster than their term mode equivalents because they can fill in the motives in a straightforward way while the elaborator has to deal with other stuff at the same time that can confound the issue</p>

#### [ Mario Carneiro (Sep 30 2018 at 02:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/134901127):
<p>Do you have evidence that a tactic proof that, say, does <code>refine refine rw cases exact</code> is faster than its term mode equivalent?</p>

#### [ Mario Carneiro (Sep 30 2018 at 02:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/134901227):
<p>In particular, if an elaboration is slow, I find that converting to a sequence of <code>refine</code>s often speeds it up, or at least narrows the problem down to a particular term that should be written a different way</p>

#### [ Kenny Lau (Sep 30 2018 at 05:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/134906074):
<p>no I'm not converting every proof to term mode.</p>

#### [ Kenny Lau (Sep 30 2018 at 05:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/134906076):
<p>I'm converting that particular proof to term mode and it turns out that the speed improved a lot.</p>

#### [ Kenny Lau (Sep 30 2018 at 05:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/134906078):
<p>I'm not making a general claim.</p>

#### [ Kenny Lau (Sep 30 2018 at 05:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/134906086):
<p>(although in my experience, pure term mode proofs do compile much faster)</p>

#### [ Kenny Lau (Sep 30 2018 at 05:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/134906088):
<p>I can give you the statistics for that particular theorem if you want.</p>

#### [ Kenny Lau (Sep 30 2018 at 05:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/134906137):
<p>it's not necessarily an improvement but in this case it is.</p>

#### [ Mario Carneiro (Sep 30 2018 at 05:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/134906248):
<p>In this case I would probably take your term proof and reintroduce tactics to recover some of the original structure, while keeping an eye on the compile time and preventing it from growing again</p>

#### [ Kenny Lau (Sep 30 2018 at 05:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/134906366):
<p>fair enough.</p>

#### [ Kenny Lau (Sep 30 2018 at 08:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/134911308):
<p><span class="user-mention" data-user-id="110049">@Mario Carneiro</span> Am I allowed to remove <code>exactI / resetI / letI</code> and use <code>@</code> to provide the typeclass instances whenever doing so would produce a significant speed boost?</p>

#### [ Mario Carneiro (Sep 30 2018 at 08:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/134911324):
<p>oof, I really hope that's a last resort</p>

#### [ Mario Carneiro (Sep 30 2018 at 08:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/134911365):
<p>I don't think it matters whether <code>exactI</code> is used or not, sometimes typeclass inference is slow</p>

#### [ Mario Carneiro (Sep 30 2018 at 08:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/134911366):
<p>It is possible that with better hints you can shortcut the search</p>

#### [ Kenny Lau (Sep 30 2018 at 08:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/134911416):
<p>well without exactI I can tell which typeclasses Lean is struggling to infer</p>

#### [ Kenny Lau (Sep 30 2018 at 08:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/134911424):
<p>and I can provide it explicitly to save Lean's time</p>

#### [ Mario Carneiro (Sep 30 2018 at 08:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/134911468):
<p>I would try to use limited typeclass inference, i.e. write the hard part of the term and have lean figure out the rest</p>

#### [ Mario Carneiro (Sep 30 2018 at 08:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/134911521):
<p>But explicit typeclass parameters are a big loss in readability, especially if you have to say things more than once, so I would try <em>really</em> hard to avoid it</p>

#### [ Kenny Lau (Sep 30 2018 at 08:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/134911522):
<p>I understand</p>

#### [ Kenny Lau (Sep 30 2018 at 08:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/134911834):
<div class="codehilite"><pre><span></span><span class="kn">import</span> <span class="n">set_theory</span><span class="bp">.</span><span class="n">ordinal</span>

<span class="kn">universe</span> <span class="n">u</span>

<span class="kn">set_option</span> <span class="n">trace</span><span class="bp">.</span><span class="n">class_instances</span> <span class="n">true</span>
<span class="bp">#</span><span class="kn">check</span>
<span class="bp">λ</span> <span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">,</span>
<span class="bp">λ</span> <span class="n">r</span> <span class="o">:</span> <span class="n">α</span> <span class="bp">→</span> <span class="n">α</span> <span class="bp">→</span> <span class="kt">Prop</span><span class="o">,</span>
<span class="bp">λ</span> <span class="n">hr</span> <span class="o">:</span> <span class="n">is_well_order</span> <span class="n">α</span> <span class="n">r</span><span class="o">,</span>
<span class="bp">λ</span> <span class="n">β</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">,</span>
<span class="bp">λ</span> <span class="n">s</span> <span class="o">:</span> <span class="n">β</span> <span class="bp">→</span> <span class="n">β</span> <span class="bp">→</span> <span class="kt">Prop</span><span class="o">,</span>
<span class="bp">λ</span> <span class="n">hs</span> <span class="o">:</span> <span class="n">is_well_order</span> <span class="n">β</span> <span class="n">s</span><span class="o">,</span>
<span class="bp">λ</span> <span class="n">x</span> <span class="o">:</span> <span class="n">β</span><span class="o">,</span> <span class="o">(</span><span class="k">by</span> <span class="n">apply_instance</span> <span class="o">:</span> <span class="n">is_asymm</span> <span class="o">(</span><span class="n">α</span> <span class="err">⊕</span> <span class="err">↥</span><span class="o">{</span><span class="n">b</span> <span class="o">:</span> <span class="n">β</span> <span class="bp">|</span> <span class="n">s</span> <span class="n">b</span> <span class="n">x</span><span class="o">})</span> <span class="o">(</span><span class="bp">@</span><span class="n">sum</span><span class="bp">.</span><span class="n">lex</span> <span class="n">α</span> <span class="err">↥</span><span class="o">{</span><span class="n">b</span> <span class="o">:</span> <span class="n">β</span> <span class="bp">|</span> <span class="n">s</span> <span class="n">b</span> <span class="n">x</span><span class="o">}</span> <span class="n">r</span> <span class="o">(</span><span class="bp">@</span><span class="n">subrel</span> <span class="n">β</span> <span class="n">s</span> <span class="o">{</span><span class="n">b</span> <span class="o">:</span> <span class="n">β</span> <span class="bp">|</span> <span class="n">s</span> <span class="n">b</span> <span class="n">x</span><span class="o">})))</span>
</pre></div>

#### [ Kenny Lau (Sep 30 2018 at 08:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/134911839):
<p><span class="user-mention" data-user-id="110049">@Mario Carneiro</span> how to shorten the path for class instance?</p>

#### [ Mario Carneiro (Sep 30 2018 at 08:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/134911953):
<p>it is much faster if I use <code>is_asymm_of_is_trans_of_is_irrefl</code> instead of <code>by apply_instance</code></p>

#### [ Mario Carneiro (Sep 30 2018 at 08:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/134911994):
<p>alternatively, prove and use <code>is_asymm_of_is_well_order</code></p>

#### [ Kenny Lau (Sep 30 2018 at 08:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/134912045):
<p>well I'm not allowed to add / delete any theorem :P</p>

#### [ Kenny Lau (Sep 30 2018 at 09:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/134912452):
<p><span class="user-mention" data-user-id="110049">@Mario Carneiro</span> Could you have a look at <a href="https://github.com/leanprover-community/mathlib/blob/a58bdb5ab50a3cb2d60e89b326e4f4d7afbf6b05/set_theory/ordinal.lean" target="_blank" title="https://github.com/leanprover-community/mathlib/blob/a58bdb5ab50a3cb2d60e89b326e4f4d7afbf6b05/set_theory/ordinal.lean">the 3 theorems I marked with <code>try_for</code></a>?</p>

#### [ Kenny Lau (Sep 30 2018 at 19:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/134929631):
<div class="codehilite"><pre><span></span><span class="bp">@</span><span class="o">[</span><span class="n">simp</span><span class="o">]</span> <span class="kn">lemma</span> <span class="n">forall₂_nil_left_iff</span> <span class="o">{</span><span class="n">l</span><span class="o">}</span> <span class="o">:</span> <span class="n">forall₂</span> <span class="n">r</span> <span class="n">nil</span> <span class="n">l</span> <span class="bp">↔</span> <span class="n">l</span> <span class="bp">=</span> <span class="n">nil</span> <span class="o">:=</span>
<span class="k">by</span> <span class="n">rw</span> <span class="o">[</span><span class="n">forall₂_iff</span><span class="o">]</span><span class="bp">;</span> <span class="n">simp</span> <span class="n">only</span> <span class="o">[</span><span class="n">eq_self_iff_true</span><span class="o">,</span> <span class="n">true_and</span><span class="o">,</span> <span class="n">false_and</span><span class="o">,</span> <span class="n">and_false</span><span class="o">,</span> <span class="n">exists_false</span><span class="o">,</span> <span class="n">or_false</span><span class="o">]</span>

<span class="bp">@</span><span class="o">[</span><span class="n">simp</span><span class="o">]</span> <span class="kn">lemma</span> <span class="n">forall₂_nil_left_iff&#39;</span> <span class="o">{</span><span class="n">l</span><span class="o">}</span> <span class="o">:</span> <span class="n">forall₂</span> <span class="n">r</span> <span class="n">nil</span> <span class="n">l</span> <span class="bp">↔</span> <span class="n">l</span> <span class="bp">=</span> <span class="n">nil</span> <span class="o">:=</span>
<span class="bp">⟨λ</span> <span class="n">H</span><span class="o">,</span> <span class="k">by</span> <span class="n">cases</span> <span class="n">H</span><span class="bp">;</span> <span class="n">refl</span><span class="o">,</span> <span class="k">by</span> <span class="n">rintro</span> <span class="n">rfl</span><span class="bp">;</span> <span class="n">constructor</span><span class="bp">⟩</span>
</pre></div>

#### [ Kenny Lau (Sep 30 2018 at 19:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/134929634):
<p><span class="user-mention" data-user-id="110049">@Mario Carneiro</span> which one do you like more? they take the same time</p>

#### [ Kenny Lau (Sep 30 2018 at 19:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/134929683):
<p>the original proof was <code>by rw [forall₂_iff]; simp</code> so maybe the first one in order to avoid changing too much</p>

#### [ Kenny Lau (Sep 30 2018 at 19:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/134929728):
<p>I would prefer the one below</p>

#### [ Mario Carneiro (Sep 30 2018 at 23:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/134936006):
<p>I would prefer the one below, although I would use <code>exact forall2.nil</code> instead of <code>constructor</code> (which has to search through the constructors to apply one)</p>

#### [ Kenny Lau (Oct 01 2018 at 10:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/134957374):
<p>before:</p>
<div class="codehilite"><pre><span></span>cumulative profiling times:
    compilation 85.7ms
    decl post-processing 1.17s
    elaboration 126s
    elaboration: tactic compilation 4.88s
    elaboration: tactic execution 90.9s
    parsing 7.79s
    type checking 145ms
</pre></div>


<p>after:</p>
<div class="codehilite"><pre><span></span>cumulative profiling times:
        compilation 46.9ms
        decl post-processing 159ms
        elaboration 12.5s
        elaboration: tactic compilation 1.58s
        elaboration: tactic execution 918ms
        parsing 5.4s
        type checking 109ms
</pre></div>

#### [ Kevin Buzzard (Oct 01 2018 at 11:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/134959164):
<p>Is this <code>ordinal.lean</code>?</p>

#### [ Kevin Buzzard (Oct 01 2018 at 11:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/134959180):
<p>Mario, is all of this making you rethink your writing style?</p>

#### [ Mario Carneiro (Oct 01 2018 at 11:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/134959310):
<p>I'm worried about kenny's writing style</p>

#### [ Mario Carneiro (Oct 01 2018 at 11:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/134959318):
<p>I don't want to sacrifice readability here if I can at all help it</p>

#### [ Mario Carneiro (Oct 01 2018 at 11:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/134959332):
<p>but these numbers are hard to argue with</p>

#### [ Mario Carneiro (Oct 01 2018 at 11:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/134959355):
<p>I think in the future we will need to work a post processing step into the workflow, using things like <code>squeeze_simp</code></p>

#### [ Mario Carneiro (Oct 01 2018 at 11:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/134959415):
<p>But I <em>do not</em> want to be thinking about compile time when I am writing a proof</p>

#### [ Mario Carneiro (Oct 01 2018 at 11:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/134959421):
<p>the mindset is completely different, it is a distraction</p>

#### [ Johan Commelin (Oct 01 2018 at 11:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/134959496):
<p><span class="user-mention" data-user-id="110049">@Mario Carneiro</span> You are talking like a mathematician.</p>

#### [ Kenny Lau (Oct 01 2018 at 11:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/134959627):
<p>this is data/list/basic.lean</p>

#### [ Kenny Lau (Oct 03 2018 at 01:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/135070742):
<div class="codehilite"><pre><span></span>$ /c/lean/bin/lean --profile analysis/topology/topological_space.lean &gt;/dev/null
cumulative profiling times:
        compilation 53.6ms
        decl post-processing 52.3ms
        elaboration 6.15s
        elaboration: tactic compilation 929ms
        elaboration: tactic execution 979ms
        parsing 1.24s
        type checking 35.9ms
</pre></div>

#### [ Kenny Lau (Oct 03 2018 at 01:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/135070748):
<p>it was the 7th on my list sorted by time</p>

#### [ Kenny Lau (Oct 03 2018 at 01:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/135070752):
<p>now it's 6.15 s</p>

#### [ Johan Commelin (Oct 03 2018 at 06:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/135079880):
<p><span class="user-mention" data-user-id="110064">@Kenny Lau</span> Do you want to PR <code>faster</code> in one go or in stages?</p>

#### [ Johan Commelin (Oct 03 2018 at 06:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/135079891):
<p>What does your profile list look like now?</p>

#### [ Kenny Lau (Oct 03 2018 at 08:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/135083606):
<p><a href="https://gist.github.com/kckennylau/f7c6cbfb2aa8bf7e4784e8c65d6c4852" target="_blank" title="https://gist.github.com/kckennylau/f7c6cbfb2aa8bf7e4784e8c65d6c4852">https://gist.github.com/kckennylau/f7c6cbfb2aa8bf7e4784e8c65d6c4852</a></p>

#### [ Kevin Buzzard (Oct 03 2018 at 09:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/135085735):
<p>Is it worth PR'ing now? My impression is that Mario will want to check that you didn't do anything he doesn't approve of.</p>

#### [ Patrick Massot (Oct 03 2018 at 09:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/135086194):
<p>I see <code>uniform_space</code> may be the next target. You may want to skip that one since Johannes and I are currently working on it (see completions branch in the community fork). Actually part of the file moved to a <code>completion</code> file</p>

#### [ Kevin Buzzard (Oct 03 2018 at 09:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/135086353):
<p>That's all the more reason to PR now I guess. Kenny did you see if anyone is working on any files you have already changed? This seems like a difficult task -- there are a million branches in community mathlib.</p>

#### [ Johan Commelin (Oct 03 2018 at 09:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/135086430):
<p>The <code>determinants</code> PR is touching like 10 basic files.</p>

#### [ Johan Commelin (Oct 03 2018 at 09:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/135086437):
<p>Hopefully git's merging strategies will be smart enough</p>

#### [ Kenny Lau (Oct 03 2018 at 10:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/135087752):
<blockquote>
<p>I see <code>uniform_space</code> may be the next target. You may want to skip that one since Johannes and I are currently working on it (see completions branch in the community fork). Actually part of the file moved to a <code>completion</code> file</p>
</blockquote>
<p>ah well I almost finished. I'll deal with the merging issues then.</p>

#### [ Kenny Lau (Oct 05 2018 at 11:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/135244802):
<p><span class="user-mention" data-user-id="110049">@Mario Carneiro</span> I still haven't finished, but do you want me to PR them (a) one by one when I finish (so you'll have 100 PRs), (b) one by one now (so you'll have 100 PRs distributed across a month), or (c) all in one go (so you'll have 1 big PR)?</p>

#### [ Kenny Lau (Oct 05 2018 at 11:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/135244846):
<p>and 100 is not a hyperbole</p>

#### [ Johan Commelin (Oct 05 2018 at 13:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/135249251):
<p>I think we shouldn't have one mega-PR. It will only sit and wait and rot and die a silent death.</p>

#### [ Johan Commelin (Oct 05 2018 at 13:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/135249258):
<p>100 PR's on 1 day won't work either.</p>

#### [ Johan Commelin (Oct 05 2018 at 13:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/135249281):
<p>So I think it is best to either have 100 small PR's that appear on a continuous basis. Or chunk them into 20 PR's that take 5 files each.<br>
Just my €0.02</p>

#### [ Sean Leather (Oct 05 2018 at 13:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/135249828):
<p>One issue that might influence the choice is whether the feedback from early changes will influence later changes. That is, from the reviewer's PoV, one doesn't want to make the same suggestion in large numbers. So to avoid this, you might start with a few small PRs and, as you get feedback, get them merged, and roll the feedback into later PRs, the PRs can either become larger or stay the same size but go through more easily. My R0.02.</p>

#### [ Johan Commelin (Oct 05 2018 at 13:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/135249991):
<p>My €0.02 are worth R0.34 <span class="emoji emoji-1f606" title="lol">:lol:</span> <a href="https://duckduckgo.com/?q=0.02EUR+in+ZAR&amp;t=ffab&amp;ia=currency" target="_blank" title="https://duckduckgo.com/?q=0.02EUR+in+ZAR&amp;t=ffab&amp;ia=currency">https://duckduckgo.com/?q=0.02EUR+in+ZAR&amp;t=ffab&amp;ia=currency</a></p>

#### [ Sean Leather (Oct 05 2018 at 14:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/135250336):
<p>Hmm, I should have given my US$0.02 instead. (<a href="https://ddg.gg/?q=0.02USD+in+EUR" target="_blank" title="https://ddg.gg/?q=0.02USD+in+EUR">€ <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mo>≈</mo></mrow><annotation encoding="application/x-tex">\approx</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.48312em;"></span><span class="strut bottom" style="height:0.48312em;vertical-align:0em;"></span><span class="base"><span class="mrel">≈</span></span></span></span> $!</a>)</p>

#### [ Sean Leather (Oct 05 2018 at 14:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/135250366):
<p>Or you could say I'm thrifty...</p>

#### [ Kenny Lau (Oct 05 2018 at 15:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/135253455):
<p>ok, I'll PR after this one</p>

#### [ Kenny Lau (Oct 05 2018 at 15:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/135255097):
<p><code>sum_sum_index</code> and friends™ have poor elaboration and often takes up time</p>

#### [ Kenny Lau (Oct 05 2018 at 15:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/135255398):
<p>and it's worse than <code>simp</code> at friends™ because you can't track elaboration</p>

#### [ Kenny Lau (Oct 05 2018 at 15:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/135255639):
<p>and I even used <code>calc</code></p>

#### [ Kenny Lau (Oct 05 2018 at 15:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/135255642):
<div class="codehilite"><pre><span></span><span class="kn">import</span> <span class="n">data</span><span class="bp">.</span><span class="n">finsupp</span>

<span class="kn">open</span> <span class="n">finsupp</span>

<span class="kn">variables</span> <span class="o">(</span><span class="n">α</span><span class="o">:</span><span class="kt">Type</span><span class="bp">*</span><span class="o">)</span> <span class="o">(</span><span class="n">β</span><span class="o">:</span><span class="kt">Type</span><span class="bp">*</span><span class="o">)</span> <span class="o">(</span><span class="n">γ</span><span class="o">:</span><span class="kt">Type</span><span class="bp">*</span><span class="o">)</span>

<span class="kn">set_option</span> <span class="n">profiler</span> <span class="n">true</span>
<span class="n">def</span> <span class="n">finsupp_prod_equiv</span> <span class="o">[</span><span class="n">add_comm_monoid</span> <span class="n">γ</span><span class="o">]</span> <span class="o">[</span><span class="n">decidable_eq</span> <span class="n">α</span><span class="o">]</span> <span class="o">[</span><span class="n">decidable_eq</span> <span class="n">β</span><span class="o">]</span> <span class="o">[</span><span class="n">decidable_eq</span> <span class="n">γ</span><span class="o">]</span> <span class="o">:</span>
  <span class="o">((</span><span class="n">α</span> <span class="bp">×</span> <span class="n">β</span><span class="o">)</span> <span class="bp">→</span><span class="err">₀</span> <span class="n">γ</span><span class="o">)</span> <span class="err">≃</span> <span class="o">(</span><span class="n">α</span> <span class="bp">→</span><span class="err">₀</span> <span class="o">(</span><span class="n">β</span> <span class="bp">→</span><span class="err">₀</span> <span class="n">γ</span><span class="o">))</span> <span class="o">:=</span>
<span class="bp">⟨</span> <span class="n">finsupp</span><span class="bp">.</span><span class="n">curry</span><span class="o">,</span> <span class="n">finsupp</span><span class="bp">.</span><span class="n">uncurry</span><span class="o">,</span>
  <span class="k">assume</span> <span class="n">f</span> <span class="o">:</span> <span class="n">α</span> <span class="bp">×</span> <span class="n">β</span> <span class="bp">→</span><span class="err">₀</span> <span class="n">γ</span><span class="o">,</span>
  <span class="k">calc</span>  <span class="o">(</span><span class="n">f</span><span class="bp">.</span><span class="n">sum</span> <span class="err">$</span> <span class="bp">λ</span><span class="n">p</span> <span class="n">c</span><span class="o">,</span> <span class="n">single</span> <span class="n">p</span><span class="bp">.</span><span class="mi">1</span> <span class="o">(</span><span class="n">single</span> <span class="n">p</span><span class="bp">.</span><span class="mi">2</span> <span class="n">c</span><span class="o">))</span><span class="bp">.</span><span class="n">sum</span> <span class="o">(</span><span class="bp">λ</span><span class="n">a</span> <span class="n">g</span><span class="o">,</span> <span class="n">g</span><span class="bp">.</span><span class="n">sum</span> <span class="err">$</span> <span class="bp">λ</span><span class="n">b</span> <span class="n">c</span><span class="o">,</span> <span class="n">single</span> <span class="o">(</span><span class="n">a</span><span class="o">,</span> <span class="n">b</span><span class="o">)</span> <span class="n">c</span><span class="o">)</span>
      <span class="bp">=</span> <span class="n">f</span><span class="bp">.</span><span class="n">sum</span> <span class="o">(</span><span class="bp">λ</span> <span class="n">a</span> <span class="n">b</span><span class="o">,</span> <span class="n">sum</span> <span class="o">(</span><span class="n">single</span> <span class="n">a</span><span class="bp">.</span><span class="mi">1</span> <span class="o">(</span><span class="n">single</span> <span class="n">a</span><span class="bp">.</span><span class="mi">2</span> <span class="n">b</span><span class="o">))</span> <span class="o">(</span><span class="bp">λ</span> <span class="n">a</span> <span class="n">g</span><span class="o">,</span> <span class="n">sum</span> <span class="n">g</span> <span class="o">(</span><span class="bp">λ</span> <span class="n">b</span> <span class="n">c</span><span class="o">,</span> <span class="n">single</span> <span class="o">(</span><span class="n">a</span><span class="o">,</span> <span class="n">b</span><span class="o">)</span> <span class="n">c</span><span class="o">)))</span> <span class="o">:</span>
    <span class="n">sum_sum_index</span> <span class="o">(</span><span class="bp">λ</span> <span class="bp">_</span><span class="o">,</span> <span class="n">sum_zero_index</span><span class="o">)</span>
        <span class="o">(</span><span class="bp">λ</span> <span class="bp">_</span> <span class="bp">_</span> <span class="bp">_</span><span class="o">,</span> <span class="n">sum_add_index</span> <span class="o">(</span><span class="bp">λ</span> <span class="bp">_</span><span class="o">,</span> <span class="n">single_zero</span><span class="o">)</span> <span class="o">(</span><span class="bp">λ</span> <span class="bp">_</span> <span class="bp">_</span> <span class="bp">_</span><span class="o">,</span> <span class="n">single_add</span><span class="o">))</span>
  <span class="bp">...</span> <span class="bp">=</span> <span class="n">sum</span> <span class="n">f</span> <span class="o">(</span><span class="bp">λ</span> <span class="n">a</span> <span class="n">b</span><span class="o">,</span> <span class="n">sum</span> <span class="o">(</span><span class="n">single</span> <span class="n">a</span><span class="bp">.</span><span class="mi">2</span> <span class="n">b</span><span class="o">)</span> <span class="o">(</span><span class="bp">λ</span> <span class="n">b</span> <span class="n">c</span><span class="o">,</span> <span class="n">single</span> <span class="o">(</span><span class="n">a</span><span class="bp">.</span><span class="mi">1</span><span class="o">,</span> <span class="n">b</span><span class="o">)</span> <span class="n">c</span><span class="o">))</span> <span class="o">:</span>
    <span class="n">congr_arg</span> <span class="o">(</span><span class="n">sum</span> <span class="n">f</span><span class="o">)</span> <span class="o">(</span><span class="n">funext</span> <span class="err">$</span> <span class="bp">λ</span> <span class="n">a</span><span class="o">,</span> <span class="n">funext</span> <span class="err">$</span> <span class="bp">λ</span> <span class="n">b</span><span class="o">,</span> <span class="n">sum_single_index</span> <span class="n">sum_zero_index</span><span class="o">)</span>
  <span class="bp">...</span> <span class="bp">=</span> <span class="n">sum</span> <span class="n">f</span> <span class="o">(</span><span class="bp">λ</span> <span class="n">a</span> <span class="n">b</span><span class="o">,</span> <span class="n">single</span> <span class="o">(</span><span class="n">a</span><span class="bp">.</span><span class="mi">1</span><span class="o">,</span> <span class="n">a</span><span class="bp">.</span><span class="mi">2</span><span class="o">)</span> <span class="n">b</span><span class="o">)</span> <span class="o">:</span>
    <span class="n">congr_arg</span> <span class="o">(</span><span class="n">sum</span> <span class="n">f</span><span class="o">)</span> <span class="o">(</span><span class="n">funext</span> <span class="err">$</span> <span class="bp">λ</span> <span class="n">a</span><span class="o">,</span> <span class="n">funext</span> <span class="err">$</span> <span class="bp">λ</span> <span class="n">b</span><span class="o">,</span> <span class="n">sum_single_index</span> <span class="n">single_zero</span><span class="o">)</span>
  <span class="bp">...</span> <span class="bp">=</span> <span class="n">sum</span> <span class="n">f</span> <span class="n">single</span> <span class="o">:</span>
    <span class="n">congr_arg</span> <span class="o">(</span><span class="n">sum</span> <span class="n">f</span><span class="o">)</span> <span class="o">(</span><span class="n">funext</span> <span class="err">$</span> <span class="bp">λ</span> <span class="n">a</span><span class="o">,</span> <span class="n">funext</span> <span class="err">$</span> <span class="bp">λ</span> <span class="n">b</span><span class="o">,</span> <span class="n">congr</span> <span class="o">(</span><span class="n">congr_arg</span> <span class="n">single</span> <span class="n">prod</span><span class="bp">.</span><span class="n">mk</span><span class="bp">.</span><span class="n">eta</span><span class="o">)</span> <span class="n">rfl</span><span class="o">)</span>
  <span class="bp">...</span> <span class="bp">=</span> <span class="n">f</span> <span class="o">:</span> <span class="n">sum_single</span><span class="o">,</span>
  <span class="k">assume</span> <span class="n">f</span><span class="o">,</span> <span class="n">sorry</span> <span class="bp">⟩</span>
</pre></div>

#### [ Kenny Lau (Oct 05 2018 at 15:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/135255644):
<p>MWE ^</p>

#### [ Kenny Lau (Oct 05 2018 at 16:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/135259451):
<div class="codehilite"><pre><span></span>$ /c/lean/bin/lean --profile data/finsupp.lean &gt;/dev/null
cumulative profiling times:
        compilation 143ms
        decl post-processing 1.9s
        elaboration 7.22s
        elaboration: tactic compilation 548ms
        elaboration: tactic execution 1.79s
        parsing 643ms
        type checking 110ms
</pre></div>

#### [ Johan Commelin (Oct 05 2018 at 16:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/135259496):
<p>Hurray!</p>

#### [ Johan Commelin (Oct 05 2018 at 16:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/135259677):
<p><span class="user-mention" data-user-id="110064">@Kenny Lau</span> Will you share the total progress after you PR?</p>

#### [ Johan Commelin (Oct 05 2018 at 16:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/135259725):
<p>I know it won't be 70% reduction yet. But I think you took off a massive chunk anyway.</p>

#### [ Kevin Buzzard (Oct 05 2018 at 17:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/135260053):
<p>Kenny the sooner you PR what you've done so far the better. People like Chris will I think already appreciate your achievements.</p>

#### [ Kenny Lau (Oct 05 2018 at 17:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/135261120):
<blockquote>
<p><span class="user-mention" data-user-id="110064">@Kenny Lau</span> Will you share the total progress after you PR?</p>
</blockquote>
<p>it's always the same link</p>

#### [ Kenny Lau (Oct 05 2018 at 17:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/135261122):
<p><a href="https://gist.github.com/kckennylau/f7c6cbfb2aa8bf7e4784e8c65d6c4852" target="_blank" title="https://gist.github.com/kckennylau/f7c6cbfb2aa8bf7e4784e8c65d6c4852">https://gist.github.com/kckennylau/f7c6cbfb2aa8bf7e4784e8c65d6c4852</a></p>

#### [ Kenny Lau (Oct 05 2018 at 17:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/135262720):
<p><a href="https://github.com/leanprover/mathlib/pull/391" target="_blank" title="https://github.com/leanprover/mathlib/pull/391">The PR is live</a></p>

#### [ Johan Commelin (Oct 05 2018 at 18:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/135264898):
<p><span class="user-mention" data-user-id="110064">@Kenny Lau</span> I meant some total stats: So the sum of the "before" column, and the sum of the "after" column.</p>

#### [ Johan Commelin (Oct 05 2018 at 18:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/135264908):
<p>I know I could throw your file through <code>awk</code>, but maybe you had already done that...</p>

#### [ Kenny Lau (Oct 05 2018 at 18:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/135266401):
<p>you see, the before column isnt exactly before, and the after column isnt exactly after</p>

#### [ Johan Commelin (Oct 05 2018 at 18:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/135266463):
<p>I'm asking about <em>statistics</em> anyway... so you're allowed to be off by 10%.</p>

#### [ Kenny Lau (Oct 05 2018 at 22:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/135280222):
<p>Here are the new measurements: <a href="https://gist.github.com/kckennylau/fd94d8c3a1cd2be9953deffd53657185" target="_blank" title="https://gist.github.com/kckennylau/fd94d8c3a1cd2be9953deffd53657185">https://gist.github.com/kckennylau/fd94d8c3a1cd2be9953deffd53657185</a></p>

#### [ Kenny Lau (Oct 05 2018 at 22:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/135280312):
<p>total compile time went from 3219 seconds to 3191 seconds</p>

#### [ Patrick Massot (Oct 05 2018 at 22:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/135280347):
<p>28 seconds improvement!</p>

#### [ Patrick Massot (Oct 05 2018 at 22:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/135280423):
<p>Impressive. No wonder that guy is the only one to get a personal message in Scott's talk</p>

#### [ Kenny Lau (Oct 05 2018 at 22:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/135280480):
<p>which guy?</p>

#### [ Patrick Massot (Oct 05 2018 at 22:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/135280580):
<p>You</p>

#### [ Patrick Massot (Oct 05 2018 at 22:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/135280592):
<p>I guess there is a typo in your numbers</p>

#### [ Patrick Massot (Oct 05 2018 at 22:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/135280641):
<p>Or I don't understand what you mean, and I should go to bed</p>

#### [ Mario Carneiro (Oct 05 2018 at 22:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/135280699):
<p>those numbers indeed seem unreasonably small compared to your earlier quotes. I thought you had trimmed at least 5 minutes off, what happened or am I not understanding your claim?</p>

#### [ Kenny Lau (Oct 05 2018 at 22:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/135280788):
<p>what happened is that the newly added <code>data/zmod/quadratic_reciprocity.lean</code> adds 2 minutes</p>

#### [ Kevin Buzzard (Oct 05 2018 at 22:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/135280815):
<p>ha ha you are swimming against the tide. Oh boy.</p>

#### [ Kenny Lau (Oct 05 2018 at 22:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/135280869):
<p>that's what happens when I'm the only one doing all this</p>

#### [ Kevin Buzzard (Oct 05 2018 at 22:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/135280877):
<p>what happens when we replace you by a computer?</p>

#### [ Kenny Lau (Oct 05 2018 at 22:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/135280913):
<p>and the newly added <code>data/padics/padic_numbers.lean</code> adds 1 minute</p>

#### [ Kenny Lau (Oct 05 2018 at 22:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/135280978):
<p><code>linear_algebra/basic.lean</code> went from 67.3 to 87.1 despite nothing having been changed, so this might just be a statistical noise</p>

#### [ Kenny Lau (Oct 05 2018 at 22:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/135280994):
<p><code>data/rat.lean</code> from 55.4 to 78 despite only having a small change</p>

#### [ Kevin Buzzard (Oct 05 2018 at 22:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/135281021):
<p>Is there a more reliable way to time these things on average or something?</p>

#### [ Kenny Lau (Oct 05 2018 at 22:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/135281097):
<p>I don't know. All of these times are measured on my computer, which is far from being a constant environment</p>

#### [ Kenny Lau (Oct 05 2018 at 22:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/135281141):
<p>there might be some statistical methods to make the results more representative of the situation at hand</p>

#### [ Kenny Lau (Oct 05 2018 at 22:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/135281151):
<p>but I don't study statistics</p>

#### [ Kevin Buzzard (Oct 05 2018 at 22:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/135281254):
<p>did you turn off discord?</p>

#### [ Kenny Lau (Oct 05 2018 at 22:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/135281261):
<p>no</p>

#### [ Kenny Lau (Oct 05 2018 at 22:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/135281333):
<p>one should just look at <a href="https://gist.github.com/kckennylau/f7c6cbfb2aa8bf7e4784e8c65d6c4852" target="_blank" title="https://gist.github.com/kckennylau/f7c6cbfb2aa8bf7e4784e8c65d6c4852">this bunch of data produced 9 days ago</a> and <a href="https://gist.github.com/kckennylau/fd94d8c3a1cd2be9953deffd53657185" target="_blank" title="https://gist.github.com/kckennylau/fd94d8c3a1cd2be9953deffd53657185">this bunch of data produced 1 hour ago</a> and make of them what one wills</p>

#### [ Mario Carneiro (Oct 05 2018 at 23:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/135281384):
<p>It's time consuming, but if you want better data you should just run it multiple times, say 3 times and average</p>

#### [ Kenny Lau (Oct 05 2018 at 23:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/135281467):
<p>that would take me 6 hours, so maybe I'll do this tomorrow</p>

#### [ Mario Carneiro (Oct 05 2018 at 23:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/135281473):
<p>Obviously I wouldn't count any new material in the count. I assume your PR doesn't introduce quadratic reciprocity, you should just compare before/after on the branch</p>

#### [ Kenny Lau (Oct 05 2018 at 23:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/135281492):
<p>I'll actually compare between the origin/master branch and the lean-community/faster branch, both in the current (i.e. tomorrow) state</p>

#### [ Kenny Lau (Oct 05 2018 at 23:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/135281494):
<p>how does this sound?</p>

#### [ Kenny Lau (Oct 05 2018 at 23:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/135281542):
<p>(I rebase the <code>faster</code> branch constantly to make sure that there are no conflicts with the origin/master branch)</p>

#### [ Mario Carneiro (Oct 05 2018 at 23:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/135281561):
<p>that should be fine. For the test you should stop rebasing for a bit, just use master as of the beginning of the test</p>

#### [ Kenny Lau (Oct 05 2018 at 23:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/135281592):
<p>so you mean origin/master as of now?</p>

#### [ Kenny Lau (Oct 05 2018 at 23:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/135281696):
<p>oh, you mean no rebasing in those 6 hours</p>

#### [ Kevin Buzzard (Oct 05 2018 at 23:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/135281723):
<p>Kenny if you send me instructions I can run some timing tests on a faster machine</p>

#### [ Kenny Lau (Oct 05 2018 at 23:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/135281772):
<p>ok</p>

#### [ Tobias Grosser (Oct 06 2018 at 12:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/135306803):
<p>I did some runs: <a href="https://gist.github.com/tobig/86477b42e1cc1d8f8f73666a002edc03" target="_blank" title="https://gist.github.com/tobig/86477b42e1cc1d8f8f73666a002edc03">https://gist.github.com/tobig/86477b42e1cc1d8f8f73666a002edc03</a></p>

#### [ Tobias Grosser (Oct 06 2018 at 12:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/135306849):
<p>faster is at around 7m10s to 7m30s  vs master at 9m30s to 10m00.</p>

#### [ Tobias Grosser (Oct 06 2018 at 12:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/135306852):
<p>On one of our faster servers.</p>

#### [ Kenny Lau (Oct 06 2018 at 12:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/135306914):
<p>thanks</p>

#### [ Tobias Grosser (Oct 06 2018 at 12:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/135306925):
<p>This is around 207m vs 320m single threaded.</p>

#### [ Johan Commelin (Oct 06 2018 at 12:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/135307121):
<p>Well done Kenny! <span class="emoji emoji-1f44d" title="thumbs up">:thumbs_up:</span></p>

#### [ Scott Morrison (Oct 06 2018 at 16:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/135313490):
<p>Hi <span class="user-mention" data-user-id="110064">@Kenny Lau</span>, I just pushed <code>squeeze_simp</code> as a separate branch, as Simon requested.</p>

#### [ Scott Morrison (Oct 06 2018 at 16:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/135313495):
<p>If you'd like, I can rebase your <code>faster</code> branch on to that.</p>

#### [ Johan Commelin (Oct 06 2018 at 16:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/135313500):
<p>I guess the current <code>faster</code> PR doesn't need it, right?</p>

#### [ Scott Morrison (Oct 06 2018 at 16:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/135313545):
<p>Well, the current <code>faster</code> branch includes <code>squeeze_simp</code>.</p>

#### [ Scott Morrison (Oct 06 2018 at 16:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/135313549):
<p>It's a bit of a mess, but Simon wanted the tactic PR'd separately from all the library improvements.</p>

#### [ Johan Commelin (Oct 06 2018 at 16:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/135313551):
<p>Sure</p>

#### [ Scott Morrison (Oct 06 2018 at 16:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/135313552):
<p>Now I should sleep, however.</p>

#### [ Scott Morrison (Oct 07 2018 at 01:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/135330404):
<p><span class="user-mention" data-user-id="110026">@Simon Hudon</span>,  I was  wondering if instead of have <code>squeeze_simp</code> be a <code>tactic unit</code>, we could have it be a <code>tactic string</code>, that also reports the <code>simp only ...</code> invocation it found via the return value.</p>

#### [ Scott Morrison (Oct 07 2018 at 01:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/135330408):
<p>The benefit of doing this is that <code>tidy</code> already produces "proof scripts", showing the sequence of successful tactics it found.</p>

#### [ Scott Morrison (Oct 07 2018 at 01:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/135330416):
<p>If <code>tidy</code> called <code>squeeze_simp</code>, then it would automatically generate <code>simp only ...</code> lines.</p>

#### [ Simon Hudon (Oct 07 2018 at 03:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/135333526):
<p>Nice! I like the idea. Yes it can do that. I just added an option for inhibiting the printout when nothing would change. I assume that would be detrimental to you. I can create a <code>tactic</code> version and an <code>interactive</code> version.</p>

#### [ Kenny Lau (Oct 08 2018 at 21:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/135422821):
<p>So this is what I do to each file:<br>
1. Place <code>set_option profiler true</code> and <code>set_option trace.simplify.rewrite true</code> at the top of the file, and select "checking visible lines and above"<br>
2. Click the name of each theorem to see if it takes too long to compile. (<code>simp</code> and <code>simpa</code> are the most reliable indicator for proofs that take a long time, but I always check the actual time used to be sure)<br>
3. Then I click on each <code>simp</code> to see which simp lemmas are used, and decide what to do:<br>
3a. I can change <code>simp</code> to <code>simp only</code> and insert all the simp lemmas that are used. Usually <code>eq_self_iff_true</code> and <code>iff_self</code> are redundant. Sometimes if the lemmas don't involving rewriting under a lambda, I may change it to <code>rw</code>, but this actually doesn't save a lot of time.<br>
3b. If I see (with the help of the list of simp lemmas used) that the proof can be written to a short proof in term mode, then I may write it in term mode.<br>
3c. If I see that the simp lemmas are all proved using <code>rfl</code>, I will replace the proof with <code>rfl</code> to see if it works (surprise, it is not infrequent to see a <code>rfl</code> proof being proved by <code>simp</code>).<br>
4. And then I make sure that the proof is sped up after my changes.<br>
5. And you can always ask me if you don't know how to deal with a certain theorem.</p>

#### [ Simon Hudon (Oct 08 2018 at 21:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/135422977):
<p>Do you keep a list of the worst offenders?</p>

#### [ Kenny Lau (Oct 08 2018 at 21:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/135423054):
<p>What do you mean?</p>

#### [ Simon Hudon (Oct 08 2018 at 21:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/135423245):
<p>I mean now that you've done all this work, what are the files that eat up most of the compile time</p>

#### [ Kenny Lau (Oct 08 2018 at 21:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/135423247):
<p><a href="https://gist.github.com/kckennylau/fd94d8c3a1cd2be9953deffd53657185" target="_blank" title="https://gist.github.com/kckennylau/fd94d8c3a1cd2be9953deffd53657185">https://gist.github.com/kckennylau/fd94d8c3a1cd2be9953deffd53657185</a></p>

#### [ Kenny Lau (Oct 08 2018 at 21:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/135423256):
<p>this is the data as of Oct 05</p>

#### [ Johan Commelin (Oct 09 2018 at 06:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/135444340):
<p><span class="user-mention" data-user-id="110026">@Simon Hudon</span> You now have experience with git hooks. Can we have a git hook that will disallow commits that import squeeze_simp?</p>

#### [ Simon Hudon (Oct 09 2018 at 07:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/135446493):
<p>Yes, you write a script and you place it in <code>.git/hooks/</code> and call it <code>pre-commit</code> (no extensions). If you look in that directory, you can see a number of samples already present. They have <code>.sample</code> extension</p>

#### [ Johan Commelin (Oct 09 2018 at 08:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/135447691):
<p><span class="user-mention" data-user-id="110049">@Mario Carneiro</span> Do you think it's worth it to PR such a hook into mathlib?</p>

#### [ Johan Commelin (Oct 09 2018 at 08:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/135447694):
<p>Could also have a hook that checks for end-of-line-whitespace</p>

#### [ Mario Carneiro (Oct 09 2018 at 08:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/135447749):
<p>I think there are a variety of style things you could check</p>

#### [ Johan Commelin (Oct 09 2018 at 08:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/135448002):
<p>Sure, but I wouldn't mind to offload the more advanced checks to a proper linter.</p>

#### [ Simon Hudon (Oct 09 2018 at 09:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/135449522):
<p>In terms of performances, I think it might be worthwhile to check the import structure and trim the redundant dependencies. I'm still unsure how to do it well though</p>

#### [ Johan Commelin (Oct 09 2018 at 14:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/135463886):
<p><a href="https://gist.github.com/jcommelin/ab7b99ee1dcd9084e2f73a940e91bb40" target="_blank" title="https://gist.github.com/jcommelin/ab7b99ee1dcd9084e2f73a940e91bb40">https://gist.github.com/jcommelin/ab7b99ee1dcd9084e2f73a940e91bb40</a> is a python script that I hacked together. If we change <code>squeeze_simp</code> enough, maybe we can automate the replacement into batch mode.</p>

#### [ Johan Commelin (Oct 09 2018 at 14:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/135463913):
<p>Problem is that if I change <code>squeeze_simp</code> to</p>
<div class="codehilite"><pre><span></span><span class="n">meta</span> <span class="n">def</span> <span class="n">squeeze_simp</span>
  <span class="o">(</span><span class="n">pbegin</span> <span class="o">:</span> <span class="n">parse</span> <span class="n">cur_pos</span><span class="o">)</span>
  <span class="o">(</span><span class="n">use_iota_eqn</span> <span class="o">:</span> <span class="n">parse</span> <span class="o">(</span><span class="n">tk</span> <span class="s2">&quot;!&quot;</span><span class="o">)</span><span class="err">?</span><span class="o">)</span> <span class="o">(</span><span class="n">no_dflt</span> <span class="o">:</span> <span class="n">parse</span> <span class="n">only_flag</span><span class="o">)</span> <span class="o">(</span><span class="n">hs</span> <span class="o">:</span> <span class="n">parse</span> <span class="n">simp_arg_list</span><span class="o">)</span>
  <span class="o">(</span><span class="n">attr_names</span> <span class="o">:</span> <span class="n">parse</span> <span class="n">with_ident_list</span><span class="o">)</span> <span class="o">(</span><span class="n">locat</span> <span class="o">:</span> <span class="n">parse</span> <span class="n">location</span><span class="o">)</span>
  <span class="o">(</span><span class="n">cfg</span> <span class="o">:</span> <span class="n">parse</span> <span class="n">record_lit</span><span class="err">?</span><span class="o">)</span>
  <span class="o">(</span><span class="n">pend</span> <span class="o">:</span> <span class="n">parse</span> <span class="n">cur_pos</span><span class="o">)</span> <span class="o">:</span> <span class="n">tactic</span> <span class="n">unit</span> <span class="o">:=</span>
<span class="n">do</span> <span class="n">g</span> <span class="err">←</span> <span class="n">main_goal</span><span class="o">,</span>
   <span class="o">(</span><span class="n">cfg&#39;</span><span class="o">,</span><span class="n">c</span><span class="o">)</span> <span class="err">←</span> <span class="n">parse_config</span> <span class="n">cfg</span><span class="o">,</span>
   <span class="n">hs&#39;</span> <span class="err">←</span> <span class="n">hs</span><span class="bp">.</span><span class="n">mmap</span> <span class="n">arg</span><span class="bp">.</span><span class="n">to_tactic_format</span><span class="o">,</span>
   <span class="n">simp</span> <span class="n">use_iota_eqn</span> <span class="n">no_dflt</span> <span class="n">hs</span> <span class="n">attr_names</span> <span class="n">locat</span> <span class="n">cfg&#39;</span><span class="o">,</span>
   <span class="n">g</span> <span class="err">←</span> <span class="n">instantiate_mvars</span> <span class="n">g</span><span class="o">,</span>
   <span class="k">let</span> <span class="n">vs</span> <span class="o">:=</span> <span class="n">g</span><span class="bp">.</span><span class="n">list_constant</span><span class="o">,</span>
   <span class="n">vs</span> <span class="err">←</span> <span class="n">vs</span><span class="bp">.</span><span class="n">mfilter</span> <span class="o">(</span><span class="n">succeeds</span> <span class="err">∘</span> <span class="n">has_attribute</span> <span class="bp">`</span><span class="n">simp</span><span class="o">),</span>
   <span class="k">let</span> <span class="n">use_iota_eqn</span> <span class="o">:=</span> <span class="k">if</span> <span class="n">use_iota_eqn</span><span class="bp">.</span><span class="n">is_some</span> <span class="k">then</span> <span class="s2">&quot;!&quot;</span> <span class="k">else</span> <span class="s2">&quot;&quot;</span><span class="o">,</span>
   <span class="k">let</span> <span class="n">attrs</span> <span class="o">:=</span> <span class="k">if</span> <span class="n">attr_names</span><span class="bp">.</span><span class="n">empty</span> <span class="k">then</span> <span class="s2">&quot;&quot;</span> <span class="k">else</span> <span class="n">string</span><span class="bp">.</span><span class="n">join</span> <span class="o">(</span><span class="n">list</span><span class="bp">.</span><span class="n">intersperse</span> <span class="s2">&quot; &quot;</span> <span class="o">(</span><span class="s2">&quot; with&quot;</span> <span class="bp">::</span> <span class="n">attr_names</span><span class="bp">.</span><span class="n">map</span> <span class="n">to_string</span><span class="o">)),</span>
   <span class="k">let</span> <span class="n">loc</span> <span class="o">:=</span> <span class="n">loc</span><span class="bp">.</span><span class="n">to_string</span> <span class="n">locat</span><span class="o">,</span>
   <span class="k">let</span> <span class="n">args</span> <span class="o">:=</span> <span class="n">hs&#39;</span> <span class="bp">++</span> <span class="n">vs</span><span class="bp">.</span><span class="n">to_list</span><span class="bp">.</span><span class="n">map</span> <span class="n">to_fmt</span><span class="o">,</span>
   <span class="n">trace</span> <span class="n">format</span><span class="bp">!</span><span class="s2">&quot;{pbegin.line}:{pbegin.column}:{pend.line}:{pend.column}:simp{use_iota_eqn} only {args}{attrs}{loc}{c}&quot;</span>
</pre></div>

#### [ Johan Commelin (Oct 09 2018 at 14:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/135463953):
<p>And I test with</p>
<div class="codehilite"><pre><span></span><span class="kn">example</span> <span class="o">:</span> <span class="n">true</span> <span class="o">:=</span>
<span class="k">begin</span>
  <span class="k">have</span> <span class="o">:</span> <span class="mi">2</span> <span class="bp">+</span> <span class="mi">3</span> <span class="bp">=</span> <span class="mi">3</span> <span class="bp">+</span> <span class="mi">2</span> <span class="o">:=</span>
  <span class="k">begin</span>
    <span class="n">squeeze_simp</span> <span class="c1">-- this is line 105</span>
  <span class="kn">end</span><span class="o">,</span>
  <span class="n">trivial</span>
<span class="kn">end</span>
</pre></div>


<p>I get the output:</p>
<div class="codehilite"><pre><span></span><span class="mi">106</span><span class="o">:</span><span class="mi">2</span><span class="o">:</span><span class="mi">106</span><span class="o">:</span><span class="mi">2</span><span class="o">:</span><span class="n">simp</span> <span class="n">only</span> <span class="o">[</span><span class="n">add_comm</span><span class="o">,</span> <span class="n">eq_self_iff_true</span><span class="o">,</span> <span class="n">add_right_inj</span><span class="o">]</span>
</pre></div>

#### [ Johan Commelin (Oct 09 2018 at 14:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/135463971):
<p>So the line:col:line:col coordinates are not very useful atm</p>

#### [ Reid Barton (Oct 09 2018 at 18:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/135480544):
<p>Does it help if you add a comma after squeeze_simp?</p>

#### [ Kenny Lau (Oct 10 2018 at 00:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/135503455):
<p><code>conv _ in _ etc</code> is slow</p>

#### [ Kenny Lau (Oct 10 2018 at 00:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/135503462):
<p>slower than <code>simp</code></p>

#### [ Kenny Lau (Oct 10 2018 at 02:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/135508682):
<p><a href="/user_uploads/3121/WKTRF2rdqUEt60_Qu8goPD5c/2018-10-10.png" target="_blank" title="2018-10-10.png">2018-10-10.png</a></p>
<div class="message_inline_image"><a href="/user_uploads/3121/WKTRF2rdqUEt60_Qu8goPD5c/2018-10-10.png" target="_blank" title="2018-10-10.png"><img src="/user_uploads/3121/WKTRF2rdqUEt60_Qu8goPD5c/2018-10-10.png"></a></div>

#### [ Kenny Lau (Oct 10 2018 at 02:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/135508741):
<p>if you do <code>set_option profiler true</code> and <code>set_option trace.simplify.rewrite true</code> then you can actually see which tactic takes the most time</p>

#### [ Kenny Lau (Oct 10 2018 at 02:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/135508796):
<p>by observing when the green squiggly line comes up</p>

#### [ Kenny Lau (Oct 10 2018 at 02:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/135509069):
<p><a href="/user_uploads/3121/8zf8fXTD-Qbb-p_O1hIZTa2a/2018-10-10-1.png" target="_blank" title="2018-10-10-1.png">2018-10-10-1.png</a></p>
<div class="message_inline_image"><a href="/user_uploads/3121/8zf8fXTD-Qbb-p_O1hIZTa2a/2018-10-10-1.png" target="_blank" title="2018-10-10-1.png"><img src="/user_uploads/3121/8zf8fXTD-Qbb-p_O1hIZTa2a/2018-10-10-1.png"></a></div>

#### [ Kenny Lau (Oct 10 2018 at 02:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/135509074):
<p>so I changed one line and suddenly the proof takes 20s less to compile</p>

#### [ Kenny Lau (Oct 10 2018 at 02:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/135509127):
<p>(ok part of it is due to caching, but whatever)</p>

#### [ Kevin Buzzard (Oct 10 2018 at 08:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/135521322):
<blockquote>
<p>(ok part of it is due to caching, but whatever)</p>
</blockquote>
<p>Can you get a more robust method for timing?</p>

#### [ Johan Commelin (Oct 10 2018 at 09:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/135524641):
<p><span class="user-mention" data-user-id="110087">@Scott Morrison</span> How long does a full compile of mathlib take on your beast?</p>

#### [ Scott Morrison (Oct 10 2018 at 11:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/135528668):
<p><span class="user-mention" data-user-id="112680">@Johan Commelin</span>  7 min 52 s</p>

#### [ Scott Morrison (Oct 10 2018 at 11:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/135528937):
<p>(During which 80m24s of core time is being used --- so it managed to average using 10 cores. I see it peak above 20 cores.)</p>

#### [ Sebastian Ullrich (Oct 10 2018 at 22:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/135566004):
<p><span class="user-mention" data-user-id="112857">@Leonardo de Moura</span> and me just talked a bit about mathlib's performance troubles. Much of this will change in Lean 4 anyway, but it may still be interesting if someone other than us could take a look and profile (using e.g. <code>perf</code>) what parts in the C++ code are so slow. Some time ago, <span class="user-mention" data-user-id="110043">@Gabriel Ebner</span> profiled that most time is spent in creating the simp lemmas cache from scratch, afair. Is this still the case? Does this mean the cache doesn't work at all, i.e. are subsequent <code>simp</code>s still slow even if no simp attributes have been changed in between? If not, might it be worth to e.g. delay and bundle up simp attribute additions where possible, instead of laboriously optimizing the proofs themselves? etc. pp.</p>

#### [ Mario Carneiro (Oct 10 2018 at 22:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/135566074):
<p>I am not sure how much of a problem this is at large scale in mathlib, but I think <code>haveI</code> and friends just turn off caching altogether, which is pretty bad from a performance standpoint</p>

#### [ Mario Carneiro (Oct 10 2018 at 22:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/135566092):
<p>The semantics I wanted them to have was that <code>haveI</code> would clear the cache but not turn it off permanently</p>

#### [ Mario Carneiro (Oct 10 2018 at 22:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/135566171):
<p>there was at least one example of a large proof that had a <code>haveI</code> early on and lots of typeclass problems later and it was super slow. I fixed it by breaking out a lemma, but I would prefer to avoid this in many cases</p>

#### [ Mario Carneiro (Oct 10 2018 at 22:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/135566234):
<p>Is it possible to run simp with a prebuilt cache somehow?</p>

#### [ Sebastian Ullrich (Oct 10 2018 at 22:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/135566338):
<p>I see. I had the impression that most proofs Kenny changed were <code>simp</code> one-liners. The typeclass cache story will probably change in Lean 4, but I don't think we want to touch that part before that</p>

#### [ Mario Carneiro (Oct 10 2018 at 22:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/135566361):
<p>they were about 80% simp and 20% typeclass inference</p>

#### [ Sebastian Ullrich (Oct 10 2018 at 22:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/135566404):
<p>Ok, good to know</p>

#### [ Mario Carneiro (Oct 10 2018 at 22:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/135566434):
<p>But it could also be that we (I) just use <code>simp</code> disproportionately</p>

#### [ Sebastian Ullrich (Oct 10 2018 at 22:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/135566435):
<blockquote>
<p>Is it possible to run simp with a prebuilt cache somehow?</p>
</blockquote>
<p>That should be possible using the tactic primitives, no? E.g. put simp lemma generation in one <code>timeit</code> and <code>simp_core</code> or whatever it was called in another</p>

#### [ Mario Carneiro (Oct 10 2018 at 22:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/135566447):
<p>i.e. <code>ring</code> is slow but I know it is slow and avoid it when possible</p>

#### [ Mario Carneiro (Oct 10 2018 at 22:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/135566500):
<p>If I put two copies of the same theorem one after another, will the second one have a hot simp cache?</p>

#### [ Mario Carneiro (Oct 10 2018 at 22:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/135566519):
<p>I guess multithreaded execution causes problems here</p>

#### [ Sebastian Ullrich (Oct 10 2018 at 22:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/135566530):
<p>Yeah. You should try running it with <code>-j0</code>.</p>

#### [ Mario Carneiro (Oct 10 2018 at 22:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/135566539):
<p>There are a lot of files like <code>multiset</code> where there are lots of simp proofs, but almost every theorem is also a simp lemma so the cache doesn't stay still</p>

#### [ Mario Carneiro (Oct 10 2018 at 22:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/135566626):
<p>What about running some proofs as though the previous lemmas are added to the bracket list rather than adding them to the default simp set? That way you can chunk up additions to the simp set a bit and decrease the number of rebuilds</p>

#### [ Sebastian Ullrich (Oct 10 2018 at 22:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/135566702):
<p>Heh, that's kind of what we want to do in Lean 4. It would definitely be a helpful experiment</p>

#### [ Simon Hudon (Oct 10 2018 at 22:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/135567209):
<p>It could probably be done with a wrapper around <code>simp</code></p>

#### [ Simon Hudon (Oct 10 2018 at 22:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/135567298):
<p>And I'd use an attribute set on one dummy definition to keep track of the lemmas used in a proof.</p>

#### [ Simon Hudon (Oct 10 2018 at 22:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/135567424):
<blockquote>
<p>What about running some proofs as though the previous lemmas are added to the bracket list rather than adding them to the default simp set? That way you can chunk up additions to the simp set a bit and decrease the number of rebuilds</p>
</blockquote>
<p>Btw, do you mean the lemmas previously defined or the lemmas previously used?</p>

#### [ Simon Hudon (Oct 10 2018 at 22:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/135567445):
<p>Also, what's the difference between the lemmas in the <code>simp</code> brackets and those that are simply in the <code>simp</code> list?</p>

#### [ Kenny Lau (Oct 11 2018 at 00:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/135573105):
<p><span class="user-mention" data-user-id="110049">@Mario Carneiro</span> Can I add the following lemma to <a href="https://github.com/leanprover/mathlib/blob/master/data/rat.lean#L196-L203" target="_blank" title="https://github.com/leanprover/mathlib/blob/master/data/rat.lean#L196-L203"><code>data/rat.lean</code></a>?</p>
<div class="codehilite"><pre><span></span><span class="bp">@</span><span class="o">[</span><span class="n">elab_as_eliminator</span><span class="o">]</span> <span class="kn">theorem</span> <span class="o">{</span><span class="n">u</span><span class="o">}</span> <span class="n">num_denom_cases_on&#39;&#39;</span> <span class="o">{</span><span class="n">C</span> <span class="o">:</span> <span class="n">ℚ</span> <span class="bp">→</span> <span class="n">Sort</span> <span class="n">u</span><span class="o">}</span>
   <span class="o">(</span><span class="n">a</span> <span class="o">:</span> <span class="n">ℚ</span><span class="o">)</span> <span class="o">(</span><span class="n">H</span> <span class="o">:</span> <span class="bp">∀</span> <span class="o">(</span><span class="n">n</span><span class="o">:</span><span class="bp">ℤ</span><span class="o">)</span> <span class="o">(</span><span class="n">d</span><span class="o">:</span><span class="bp">ℤ</span><span class="o">),</span> <span class="n">d</span> <span class="bp">≠</span> <span class="mi">0</span> <span class="bp">→</span> <span class="n">C</span> <span class="o">(</span><span class="n">n</span> <span class="bp">/.</span> <span class="n">d</span><span class="o">))</span> <span class="o">:</span> <span class="n">C</span> <span class="n">a</span> <span class="o">:=</span>
<span class="n">num_denom_cases_on&#39;</span> <span class="n">a</span> <span class="err">$</span> <span class="bp">λ</span> <span class="n">n</span> <span class="n">d</span> <span class="n">h</span><span class="o">,</span>
<span class="n">H</span> <span class="n">n</span> <span class="n">d</span> <span class="err">$</span> <span class="n">int</span><span class="bp">.</span><span class="n">coe_nat_ne_zero</span><span class="bp">.</span><span class="mi">2</span> <span class="n">h</span>
</pre></div>

#### [ Mario Carneiro (Oct 11 2018 at 04:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/135580682):
<p>Sure. You sure you don't want <code>d &gt; 0</code> in the assumptions instead?</p>

#### [ Kenny Lau (Oct 11 2018 at 10:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/135593540):
<p><span class="user-mention" data-user-id="110049">@Mario Carneiro</span> yes, because <code>add_def</code> and friends all use <code>n /. d</code> with <code>d \ne 0</code></p>

#### [ Kenny Lau (Oct 11 2018 at 10:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/135594056):
<p>well now <code>mk_nonneg</code> uses <code>n /. d</code> with <code>d &gt; 0</code> so can I get another recursor?</p>

#### [ Kenny Lau (Oct 11 2018 at 10:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/135594135):
<p>actually I need <code>add_def</code> and <code>mk_nonneg</code> at the same time, so maybe I don't need a new recursor, but I would like to have this instead:</p>

#### [ Kenny Lau (Oct 11 2018 at 10:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/135594154):
<div class="codehilite"><pre><span></span><span class="bp">@</span><span class="o">[</span><span class="n">elab_as_eliminator</span><span class="o">]</span> <span class="kn">theorem</span> <span class="o">{</span><span class="n">u</span><span class="o">}</span> <span class="n">num_denom_cases_on&#39;&#39;</span> <span class="o">{</span><span class="n">C</span> <span class="o">:</span> <span class="n">ℚ</span> <span class="bp">→</span> <span class="n">Sort</span> <span class="n">u</span><span class="o">}</span>
   <span class="o">(</span><span class="n">a</span> <span class="o">:</span> <span class="n">ℚ</span><span class="o">)</span> <span class="o">(</span><span class="n">H</span> <span class="o">:</span> <span class="bp">∀</span> <span class="o">(</span><span class="n">n</span><span class="o">:</span><span class="bp">ℤ</span><span class="o">)</span> <span class="o">(</span><span class="n">d</span><span class="o">:</span><span class="bp">ℤ</span><span class="o">),</span> <span class="n">d</span> <span class="bp">≠</span> <span class="mi">0</span> <span class="bp">→</span> <span class="n">d</span> <span class="bp">&gt;</span> <span class="mi">0</span> <span class="bp">→</span> <span class="n">C</span> <span class="o">(</span><span class="n">n</span> <span class="bp">/.</span> <span class="n">d</span><span class="o">))</span> <span class="o">:</span> <span class="n">C</span> <span class="n">a</span> <span class="o">:=</span>
<span class="n">num_denom_cases_on&#39;</span> <span class="n">a</span> <span class="err">$</span> <span class="bp">λ</span> <span class="n">n</span> <span class="n">d</span> <span class="n">h</span><span class="o">,</span>
<span class="n">H</span> <span class="n">n</span> <span class="n">d</span> <span class="o">(</span><span class="n">int</span><span class="bp">.</span><span class="n">coe_nat_ne_zero</span><span class="bp">.</span><span class="mi">2</span> <span class="n">h</span><span class="o">)</span> <span class="o">(</span><span class="n">int</span><span class="bp">.</span><span class="n">coe_nat_pos</span><span class="bp">.</span><span class="mi">2</span> <span class="err">$</span> <span class="n">nat</span><span class="bp">.</span><span class="n">pos_of_ne_zero</span> <span class="n">h</span><span class="o">)</span>
</pre></div>

#### [ Kenny Lau (Oct 12 2018 at 02:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/135645931):
<div class="codehilite"><pre><span></span>git ls-files *.lean | xargs -I % sh -c &#39;&gt;&amp;2 echo %; /c/lean/bin/lean --profile % &gt;/dev/null;&#39; &gt; profile.txt 2&gt;&amp;1
</pre></div>

#### [ Kenny Lau (Oct 12 2018 at 02:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/135645933):
<p>I'm starting to think that this is the wrong thing to type</p>

#### [ Kenny Lau (Oct 12 2018 at 02:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/135645935):
<p>somehow it only uses one thread</p>

#### [ Kenny Lau (Oct 12 2018 at 02:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/135645937):
<p><span class="user-mention" data-user-id="110049">@Mario Carneiro</span> do you know enough bash magic to make it work?</p>

#### [ Kenny Lau (Oct 12 2018 at 02:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/135645949):
<p>or one core. I'm just guessing based on the output</p>

#### [ Mario Carneiro (Oct 12 2018 at 02:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/135646003):
<p>did you try setting the <code>-j</code> option of lean?</p>

#### [ Mario Carneiro (Oct 12 2018 at 02:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/135646023):
<p>also, your latest version of <code>num_denom_cases_on''</code> seems sillier than the last. Is <code>ne_of_gt</code> so expensive?</p>

#### [ Kenny Lau (Oct 12 2018 at 02:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/135646035):
<p>well it's long</p>

#### [ Mario Carneiro (Oct 12 2018 at 02:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/135646084):
<p>you have a strange sense of long</p>

#### [ Kenny Lau (Oct 12 2018 at 02:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/135646095):
<p>you have a strange interpretation of convention</p>

#### [ Mario Carneiro (Oct 12 2018 at 02:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/135646109):
<p>which one?</p>

#### [ Kenny Lau (Oct 12 2018 at 02:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/135646128):
<p>that there can be two conventions</p>

#### [ Kenny Lau (Oct 12 2018 at 02:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/135646133):
<p>maybe we shouldn't have two conventions to start with</p>

#### [ Mario Carneiro (Oct 12 2018 at 02:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/135646176):
<p>I will defend my right to have exceptions to rules, but I still don't know what you are talking about</p>

#### [ Kenny Lau (Oct 12 2018 at 02:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/135646188):
<p>that add_def and friends uses "denom ne zero" and mk_nonneg uses "denom &gt; zero"</p>

#### [ Mario Carneiro (Oct 12 2018 at 02:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/135646197):
<p>um... <code>mk_nonneg</code> is about nonnegative things</p>

#### [ Mario Carneiro (Oct 12 2018 at 02:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/135646211):
<p>of course it needs to know the inputs are nonnegative</p>

#### [ Kenny Lau (Oct 12 2018 at 02:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/135646215):
<p>and who thought the original <code>num_denom_cases_on'</code> is a good idea despite literally every instance of it needing a fix</p>

#### [ Mario Carneiro (Oct 12 2018 at 02:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/135646269):
<p>I don't see it. It gets used like 20 times immediately afterwards and there are no fixes</p>

#### [ Kenny Lau (Oct 12 2018 at 02:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/135646286):
<p>by "fix" I mean, wrapper</p>

#### [ Mario Carneiro (Oct 12 2018 at 02:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/135646297):
<p>The fact that <code>d</code> is referred to in a <code>\u</code> is deliberate</p>

#### [ Mario Carneiro (Oct 12 2018 at 02:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/135646303):
<p>it's a cheap way of saying nonnegative integer without any overhead</p>

#### [ Kenny Lau (Oct 12 2018 at 02:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/135646339):
<p>but matches none of the theorem's hypothesis</p>

#### [ Mario Carneiro (Oct 12 2018 at 02:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/135646403):
<p>Maybe you are right, most of the theorems don't care that it's nonnegative so having it be an integer is just as well. But in that case I would stick to your first proposal</p>

#### [ Kenny Lau (Oct 12 2018 at 02:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compile%20time%20statistics/near/135646438):
<p>ok</p>


{% endraw %}
