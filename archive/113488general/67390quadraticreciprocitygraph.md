---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/67390quadraticreciprocitygraph.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [quadratic reciprocity graph](https://leanprover-community.github.io/archive/113488general/67390quadraticreciprocitygraph.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Kevin Buzzard (Sep 16 2018 at 17:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quadratic%20reciprocity%20graph/near/134058821):
<p>Chris just sent me a text file of all the theorems used in his proof of quadratic reciprocity</p>

#### [ Kevin Buzzard (Sep 16 2018 at 17:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quadratic%20reciprocity%20graph/near/134058869):
<p><a href="/user_uploads/3121/V5O2ze1stMrqhYQNQydKuqvL/quadratic_reciprocity.txt" target="_blank" title="quadratic_reciprocity.txt">quadratic_reciprocity.txt</a></p>

#### [ Kevin Buzzard (Sep 16 2018 at 17:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quadratic%20reciprocity%20graph/near/134058872):
<p>Maybe <span class="user-mention" data-user-id="110044">@Chris Hughes</span>  can explain what this file represents while I spend 5 minutes doing emacs hackery on it</p>

#### [ Kevin Buzzard (Sep 16 2018 at 17:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quadratic%20reciprocity%20graph/near/134058882):
<p>but in 10 minutes' time we're going to have this in GePhi</p>

#### [ Kenny Lau (Sep 16 2018 at 17:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quadratic%20reciprocity%20graph/near/134058932):
<p>who is gephi?</p>

#### [ Patrick Massot (Sep 16 2018 at 17:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quadratic%20reciprocity%20graph/near/134058935):
<p>Chris I'd very interested to know why you duplicate this meta-effort. If you don't like what I wrote in <a href="https://github.com/leanprover-community/leancrawler" target="_blank" title="https://github.com/leanprover-community/leancrawler">https://github.com/leanprover-community/leancrawler</a> you can improve it, or propose a brand new stuff.</p>

#### [ Patrick Massot (Sep 16 2018 at 17:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quadratic%20reciprocity%20graph/near/134058938):
<p><a href="https://gephi.org/" target="_blank" title="https://gephi.org/">https://gephi.org/</a></p>

#### [ Chris Hughes (Sep 16 2018 at 17:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quadratic%20reciprocity%20graph/near/134058947):
<p>It's a <code>list (name × list name)</code>. Each element of the list is a <code>declaration</code> used in the proof and the list of depth one dependencies.</p>

#### [ Patrick Massot (Sep 16 2018 at 17:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quadratic%20reciprocity%20graph/near/134058949):
<p>The same graph visualization format my crawler natively writes</p>

#### [ Chris Hughes (Sep 16 2018 at 17:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quadratic%20reciprocity%20graph/near/134058952):
<p>I duplicated it to learn how to write <code>meta</code> mainly</p>

#### [ Patrick Massot (Sep 16 2018 at 17:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quadratic%20reciprocity%20graph/near/134058959):
<p>Your meta code may be better than mine, you could contribute it</p>

#### [ Patrick Massot (Sep 16 2018 at 17:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quadratic%20reciprocity%20graph/near/134059000):
<p>Learning meta stuff was also one of my main motivations</p>

#### [ Kevin Buzzard (Sep 16 2018 at 17:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quadratic%20reciprocity%20graph/near/134059007):
<p>I've got it working</p>

#### [ Chris Hughes (Sep 16 2018 at 17:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quadratic%20reciprocity%20graph/near/134059012):
<p>It does slightly different things from yours</p>

#### [ Kevin Buzzard (Sep 16 2018 at 17:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quadratic%20reciprocity%20graph/near/134059013):
<p><a href="/user_uploads/3121/N1FVZyB30X5bFl3Tw6A1_EDy/quadratic_reciprocity.csv" target="_blank" title="quadratic_reciprocity.csv">quadratic_reciprocity.csv</a></p>

#### [ Kevin Buzzard (Sep 16 2018 at 17:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quadratic%20reciprocity%20graph/near/134059022):
<p>I've never used gephi before in my life but it's very intuitive. The hard work is done.</p>

#### [ Kevin Buzzard (Sep 16 2018 at 17:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quadratic%20reciprocity%20graph/near/134059064):
<p>open GePhi, click on "open graph file", select that csv file</p>

#### [ Kevin Buzzard (Sep 16 2018 at 17:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quadratic%20reciprocity%20graph/near/134059073):
<p>make sure "separator" is set to semicolon, "import as" is set to "Adjacency List" and "Charset" apparently should be UTF-16LE (blame chris for this)</p>

#### [ Kevin Buzzard (Sep 16 2018 at 17:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quadratic%20reciprocity%20graph/near/134059118):
<p>then Window -&gt; Graph and you have a graph of the proof of quadratic reciprocity in Lean</p>

#### [ Kevin Buzzard (Sep 16 2018 at 17:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quadratic%20reciprocity%20graph/near/134059121):
<p>and 10 gigs less of free ram</p>

#### [ Kevin Buzzard (Sep 16 2018 at 17:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quadratic%20reciprocity%20graph/near/134059189):
<p>In the "statistics" section you can do a bunch of tests and compute things, and those run fine, it's just the visualisation stuff that really hammers the CPU</p>

#### [ Kevin Buzzard (Sep 16 2018 at 17:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quadratic%20reciprocity%20graph/near/134059211):
<p>Diameter is 24, which I guess means that that's the longest chain of dependencies (25 definitions I guess)</p>

#### [ Kevin Buzzard (Sep 16 2018 at 17:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quadratic%20reciprocity%20graph/near/134059251):
<p><a href="/user_uploads/3121/hZZB39E4kv_LHQ8xY8yys-dY/chaos.png" target="_blank" title="chaos.png">chaos.png</a></p>
<div class="message_inline_image"><a href="/user_uploads/3121/hZZB39E4kv_LHQ8xY8yys-dY/chaos.png" target="_blank" title="chaos.png"><img src="/user_uploads/3121/hZZB39E4kv_LHQ8xY8yys-dY/chaos.png"></a></div>

#### [ Kevin Buzzard (Sep 16 2018 at 17:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quadratic%20reciprocity%20graph/near/134059253):
<p>It's still trying to see the wood from the trees</p>

#### [ Patrick Massot (Sep 16 2018 at 17:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quadratic%20reciprocity%20graph/near/134059321):
<p>Did you use the Force 2 layout?</p>

#### [ Patrick Massot (Sep 16 2018 at 17:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quadratic%20reciprocity%20graph/near/134059361):
<p>You need to push the scale parameter</p>

#### [ Patrick Massot (Sep 16 2018 at 17:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quadratic%20reciprocity%20graph/near/134059379):
<p>Most of the very high valence vertices seem to be the usual suspects (eq, eq.rec...)</p>

#### [ Patrick Massot (Sep 16 2018 at 17:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quadratic%20reciprocity%20graph/near/134059413):
<p>has_mem and friends, has_zero...</p>

#### [ Kevin Buzzard (Sep 16 2018 at 18:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quadratic%20reciprocity%20graph/near/134059662):
<p>oh -- force 2 uses all the threads!</p>

#### [ Kevin Buzzard (Sep 16 2018 at 18:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quadratic%20reciprocity%20graph/near/134059663):
<p>Oh that's much better</p>

#### [ Chris Hughes (Sep 16 2018 at 21:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quadratic%20reciprocity%20graph/near/134065462):
<p><a href="/user_uploads/3121/ZIxA3pfZ9pcVlAK1Wd8IaGot/QR.png" target="_blank" title="QR.png">QR.png</a></p>
<div class="message_inline_image"><a href="/user_uploads/3121/ZIxA3pfZ9pcVlAK1Wd8IaGot/QR.png" target="_blank" title="QR.png"><img src="/user_uploads/3121/ZIxA3pfZ9pcVlAK1Wd8IaGot/QR.png"></a></div>

#### [ Kevin Buzzard (Sep 16 2018 at 21:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quadratic%20reciprocity%20graph/near/134065843):
<p>That's a proof of quadratic reciprocity!</p>

#### [ Chris Hughes (Sep 16 2018 at 21:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quadratic%20reciprocity%20graph/near/134065896):
<p>You can spend hours fiddling with all the options on that.</p>

#### [ Kevin Buzzard (Sep 16 2018 at 22:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quadratic%20reciprocity%20graph/near/134066752):
<p><a href="/user_uploads/3121/8Wzwd0qZKOxY52vR2VrHTRh_/qr2.png" target="_blank" title="qr2.png">qr2.png</a></p>
<div class="message_inline_image"><a href="/user_uploads/3121/8Wzwd0qZKOxY52vR2VrHTRh_/qr2.png" target="_blank" title="qr2.png"><img src="/user_uploads/3121/8Wzwd0qZKOxY52vR2VrHTRh_/qr2.png"></a></div>

#### [ Kevin Buzzard (Sep 16 2018 at 22:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quadratic%20reciprocity%20graph/near/134066793):
<p>yeah. Yours is nice and arty :-)</p>

#### [ Mario Carneiro (Sep 16 2018 at 22:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quadratic%20reciprocity%20graph/near/134066801):
<p>lol I guess it doesn't lend itself well to word cloud format</p>

#### [ Kevin Buzzard (Sep 16 2018 at 22:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quadratic%20reciprocity%20graph/near/134066865):
<p><a href="/user_uploads/3121/AjrtdEkiMh0ZVvx2aZkHKhp3/QR3.png" target="_blank" title="QR3.png">QR3.png</a> You can see the words a bit better if you zoom in</p>
<div class="message_inline_image"><a href="/user_uploads/3121/AjrtdEkiMh0ZVvx2aZkHKhp3/QR3.png" target="_blank" title="QR3.png"><img src="/user_uploads/3121/AjrtdEkiMh0ZVvx2aZkHKhp3/QR3.png"></a></div>

#### [ Mario Carneiro (Sep 16 2018 at 22:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quadratic%20reciprocity%20graph/near/134066906):
<p>I notice that all the biggest things are typeclass instances</p>

#### [ Kevin Buzzard (Sep 16 2018 at 22:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quadratic%20reciprocity%20graph/near/134066909):
<p><code>Nice to see polynomial.integral_domain._proof_12</code> there.</p>

#### [ Mario Carneiro (Sep 16 2018 at 22:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quadratic%20reciprocity%20graph/near/134066913):
<p>what am I looking at?</p>

#### [ Kevin Buzzard (Sep 16 2018 at 22:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quadratic%20reciprocity%20graph/near/134066914):
<p>Node size is based on "betweenness centrality"</p>

#### [ Kevin Buzzard (Sep 16 2018 at 22:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quadratic%20reciprocity%20graph/near/134066915):
<p>and font size is proportional to node size</p>

#### [ Mario Carneiro (Sep 16 2018 at 22:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quadratic%20reciprocity%20graph/near/134066956):
<p>I'm afraid I can't guess what that means</p>

#### [ Bryan Gin-ge Chen (Sep 16 2018 at 22:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quadratic%20reciprocity%20graph/near/134066965):
<p>There's apparently a whole <a href="https://en.wikipedia.org/wiki/Betweenness_centrality" target="_blank" title="https://en.wikipedia.org/wiki/Betweenness_centrality">wikipedia page  on it</a>.</p>

#### [ Kevin Buzzard (Sep 16 2018 at 22:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quadratic%20reciprocity%20graph/near/134066977):
<p><a href="/user_uploads/3121/RnxBANmJ2Yoxrv_VVQ-ck_ac/degree.png" target="_blank" title="degree.png">degree.png</a> size now proportional to degree of node</p>
<div class="message_inline_image"><a href="/user_uploads/3121/RnxBANmJ2Yoxrv_VVQ-ck_ac/degree.png" target="_blank" title="degree.png"><img src="/user_uploads/3121/RnxBANmJ2Yoxrv_VVQ-ck_ac/degree.png"></a></div>

#### [ Kevin Buzzard (Sep 16 2018 at 22:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quadratic%20reciprocity%20graph/near/134067075):
<p>OK last one, with size proportional to out-degree -- completely different. <a href="/user_uploads/3121/WBULe2a2A5SozefrvDmtCRc0/QR4.png" target="_blank" title="QR4.png">QR4.png</a> Thanks so much to <span class="user-mention" data-user-id="110031">@Patrick Massot</span> for pointing me to GePhi. It's really easy to use. Patrick's scripts even create a graph in GePhi format -- Chris sent me a list of edges and I had to do some emacs hackery to turn it into an appropriate format.</p>
<div class="message_inline_image"><a href="/user_uploads/3121/WBULe2a2A5SozefrvDmtCRc0/QR4.png" target="_blank" title="QR4.png"><img src="/user_uploads/3121/WBULe2a2A5SozefrvDmtCRc0/QR4.png"></a></div>

#### [ Bryan Gin-ge Chen (Sep 16 2018 at 22:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quadratic%20reciprocity%20graph/near/134067187):
<p>I know very little about quadratic reciprocity and this proof, but for those who do, in your opinion, what should be the biggest nodes in terms of "mathematical importance", i.e. the "key steps"?</p>

#### [ Chris Hughes (Sep 16 2018 at 22:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quadratic%20reciprocity%20graph/near/134067500):
<p>The key steps are polynomials of degree n over an integral domain have at most n roots, Lagrange's theorem in group theory, cyclicness of units of finite field, the fact that integers mod p are a field. After that it's more or less just annoying manipulations of products that have no relevance outside of this proof.</p>

#### [ Patrick Massot (Sep 16 2018 at 22:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quadratic%20reciprocity%20graph/near/134067616):
<blockquote>
<p>it's really easy to use</p>
</blockquote>
<p>Unfortunately it's not quite true. It's really easy to have fun with, like you and I did. But the purpose of this software is to actually get information from the graph, either visually or in tables. And this is much harder.</p>

#### [ Kevin Buzzard (Sep 16 2018 at 23:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quadratic%20reciprocity%20graph/near/134068463):
<p>I think that Gauss knew all of the facts that Chris quoted when he formulated the law, but it took him years to find the proof. Perhaps because in some sense the proof isn't conceptual -- or at least the proofs Gauss found weren't. Now we can deduce it from more general reciprocity laws which do have conceptual proofs, but to formalise those proofs we need some basic algebraic number theory first (factorisation of ideals into prime ideals in the integers of a number field).</p>

#### [ Kenny Lau (Sep 16 2018 at 23:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quadratic%20reciprocity%20graph/near/134068468):
<p><a href="https://github.com/leanprover/mathlib/issues/40" target="_blank" title="https://github.com/leanprover/mathlib/issues/40">https://github.com/leanprover/mathlib/issues/40</a></p>

#### [ Patrick Massot (Sep 16 2018 at 23:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quadratic%20reciprocity%20graph/near/134068516):
<p><a href="/user_uploads/3121/vZjqKnNises6zhwJQRTU1Rte/screenshot_232944.png" target="_blank" title="screenshot_232944.png">screenshot_232944.png</a></p>
<div class="message_inline_image"><a href="/user_uploads/3121/vZjqKnNises6zhwJQRTU1Rte/screenshot_232944.png" target="_blank" title="screenshot_232944.png"><img src="/user_uploads/3121/vZjqKnNises6zhwJQRTU1Rte/screenshot_232944.png"></a></div>

#### [ Kevin Buzzard (Sep 16 2018 at 23:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quadratic%20reciprocity%20graph/near/134068517):
<p>We could do that in 10 minutes flat Kenny if you were interested</p>

#### [ Patrick Massot (Sep 16 2018 at 23:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quadratic%20reciprocity%20graph/near/134068520):
<p>This is probably a more readable graph</p>

#### [ Kevin Buzzard (Sep 16 2018 at 23:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quadratic%20reciprocity%20graph/near/134068526):
<p>However we wouldn't be able to prove anything about them, it would just be a PR stunt</p>

#### [ Kenny Lau (Sep 16 2018 at 23:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quadratic%20reciprocity%20graph/near/134068533):
<p>do what in 10 minutes?</p>

#### [ Kevin Buzzard (Sep 16 2018 at 23:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quadratic%20reciprocity%20graph/near/134068535):
<p>Is the middle dot <code>eq</code>?</p>

#### [ Patrick Massot (Sep 16 2018 at 23:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quadratic%20reciprocity%20graph/near/134068536):
<p>It's limited to mathlib (not core), all declarations used in quadratic reciprocity (big dot in the center) but not recursors or other auto-generated stuff</p>

#### [ Kevin Buzzard (Sep 16 2018 at 23:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quadratic%20reciprocity%20graph/near/134068575):
<p>Oh</p>

#### [ Kevin Buzzard (Sep 16 2018 at 23:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quadratic%20reciprocity%20graph/near/134068577):
<p>Is the middle dot QR then?</p>

#### [ Patrick Massot (Sep 16 2018 at 23:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quadratic%20reciprocity%20graph/near/134068578):
<p>Yes</p>

#### [ Patrick Massot (Sep 16 2018 at 23:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quadratic%20reciprocity%20graph/near/134068581):
<p><a href="/user_uploads/3121/UWID5NbYAEpuHVIMWfhm0fTg/qr.gephi" target="_blank" title="qr.gephi">qr.gephi</a></p>

#### [ Kevin Buzzard (Sep 16 2018 at 23:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quadratic%20reciprocity%20graph/near/134068584):
<p>Define adeles in 10 minutes. Adeles of K are adeles of Q tensor K.</p>

#### [ Kenny Lau (Sep 16 2018 at 23:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quadratic%20reciprocity%20graph/near/134068588):
<p>aha</p>

#### [ Kevin Buzzard (Sep 16 2018 at 23:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quadratic%20reciprocity%20graph/near/134068592):
<p>Adeles of Q are just restricted product of p-adics</p>

#### [ Kevin Buzzard (Sep 16 2018 at 23:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quadratic%20reciprocity%20graph/near/134068593):
<p>And the reals</p>

#### [ Kenny Lau (Sep 16 2018 at 23:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quadratic%20reciprocity%20graph/near/134068594):
<p>and R</p>

#### [ Patrick Massot (Sep 16 2018 at 23:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quadratic%20reciprocity%20graph/near/134068595):
<p>Blue is definition, orange is theorem, green is instance</p>

#### [ Kevin Buzzard (Sep 16 2018 at 23:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quadratic%20reciprocity%20graph/near/134068636):
<p>Can you label some of the nodes?</p>

#### [ Patrick Massot (Sep 16 2018 at 23:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quadratic%20reciprocity%20graph/near/134068637):
<p>Kevin, please download the gephi file. I claim it contains relevant stuff</p>

#### [ Patrick Massot (Sep 16 2018 at 23:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quadratic%20reciprocity%20graph/near/134068646):
<p>Not noise</p>

#### [ Kevin Buzzard (Sep 16 2018 at 23:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quadratic%20reciprocity%20graph/near/134068690):
<p><span class="user-mention" data-user-id="123965">@Bryan Gin-ge Chen</span> quadratic reciprocity does not follow easily from these standard facts that Chris quoted. The hard part is putting everything together in a subtle way. I wonder how long a computer would take to prove it just given the standard facts. I suspect a long time. As Chris said, you end up doing some delicate counting with some intermediate lemmas that you never use again for anything else</p>

#### [ Kevin Buzzard (Sep 16 2018 at 23:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quadratic%20reciprocity%20graph/near/134068793):
<p>The conceptual proof uses the fact that if <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>p</mi><mo>≡</mo><mn>1</mn></mrow><annotation encoding="application/x-tex">p\equiv1</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.64444em;"></span><span class="strut bottom" style="height:0.8388800000000001em;vertical-align:-0.19444em;"></span><span class="base"><span class="mord mathit">p</span><span class="mrel">≡</span><span class="mord mathrm">1</span></span></span></span> mod 4, then <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mrow><mi mathvariant="double-struck">Q</mi></mrow><mo>(</mo><msup><mi>p</mi><mrow><mn>1</mn><mi mathvariant="normal">/</mi><mn>2</mn></mrow></msup><mo>)</mo><mo>⊆</mo><mrow><mi mathvariant="double-struck">Q</mi></mrow><mo>(</mo><msub><mi>ζ</mi><mi>p</mi></msub><mo>)</mo></mrow><annotation encoding="application/x-tex">\mathbb{Q}(p^{1/2})\subseteq\mathbb{Q}(\zeta_p)</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.8879999999999999em;"></span><span class="strut bottom" style="height:1.174108em;vertical-align:-0.286108em;"></span><span class="base"><span class="mord"><span class="mord mathbb">Q</span></span><span class="mopen">(</span><span class="mord"><span class="mord mathit">p</span><span class="msupsub"><span class="vlist-t"><span class="vlist-r"><span class="vlist" style="height:0.8879999999999999em;"><span style="top:-3.063em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight"><span class="mord mathrm mtight">1</span><span class="mord mathrm mtight">/</span><span class="mord mathrm mtight">2</span></span></span></span></span></span></span></span></span><span class="mclose">)</span><span class="mrel">⊆</span><span class="mord"><span class="mord mathbb">Q</span></span><span class="mopen">(</span><span class="mord"><span class="mord mathit" style="margin-right:0.07378em;">ζ</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.15139200000000003em;"><span style="top:-2.5500000000000003em;margin-left:-0.07378em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mathit mtight">p</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.286108em;"></span></span></span></span></span><span class="mclose">)</span></span></span></span> where <span class="katex"><span class="katex-mathml"><math><semantics><mrow><msub><mi>ζ</mi><mi>p</mi></msub><mo>=</mo><msup><mi>e</mi><mrow><mn>2</mn><mi>π</mi><mi>i</mi><mi mathvariant="normal">/</mi><mi>p</mi></mrow></msup></mrow><annotation encoding="application/x-tex">\zeta_p=e^{2\pi i/p}</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.8879999999999999em;"></span><span class="strut bottom" style="height:1.174108em;vertical-align:-0.286108em;"></span><span class="base"><span class="mord"><span class="mord mathit" style="margin-right:0.07378em;">ζ</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.15139200000000003em;"><span style="top:-2.5500000000000003em;margin-left:-0.07378em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mathit mtight">p</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.286108em;"></span></span></span></span></span><span class="mrel">=</span><span class="mord"><span class="mord mathit">e</span><span class="msupsub"><span class="vlist-t"><span class="vlist-r"><span class="vlist" style="height:0.8879999999999999em;"><span style="top:-3.063em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight"><span class="mord mathrm mtight">2</span><span class="mord mathit mtight" style="margin-right:0.03588em;">π</span><span class="mord mathit mtight">i</span><span class="mord mathrm mtight">/</span><span class="mord mathit mtight">p</span></span></span></span></span></span></span></span></span></span></span></span></p>

#### [ Kenny Lau (Sep 16 2018 at 23:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quadratic%20reciprocity%20graph/near/134068801):
<p>and then doing a lot of non-trivial stuff</p>

#### [ Patrick Massot (Sep 16 2018 at 23:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quadratic%20reciprocity%20graph/near/134068802):
<p>Even better: a version removing any declaration whose name contains "coe" or "cast" (which is noise from a mathematical point of view) <a href="/user_uploads/3121/WiWuTI0G5fM74Vd8TIbSO6FY/qr.gephi" target="_blank" title="qr.gephi">qr.gephi</a></p>

#### [ Kevin Buzzard (Sep 16 2018 at 23:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quadratic%20reciprocity%20graph/near/134068803):
<p>The factorization of a prime number <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>q</mi></mrow><annotation encoding="application/x-tex">q</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.43056em;"></span><span class="strut bottom" style="height:0.625em;vertical-align:-0.19444em;"></span><span class="base"><span class="mord mathit" style="margin-right:0.03588em;">q</span></span></span></span> in <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mrow><mi mathvariant="double-struck">Q</mi></mrow><mo>(</mo><msup><mi>p</mi><mrow><mn>1</mn><mi mathvariant="normal">/</mi><mn>2</mn></mrow></msup><mo>)</mo></mrow><annotation encoding="application/x-tex">\mathbb{Q}(p^{1/2})</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.8879999999999999em;"></span><span class="strut bottom" style="height:1.138em;vertical-align:-0.25em;"></span><span class="base"><span class="mord"><span class="mord mathbb">Q</span></span><span class="mopen">(</span><span class="mord"><span class="mord mathit">p</span><span class="msupsub"><span class="vlist-t"><span class="vlist-r"><span class="vlist" style="height:0.8879999999999999em;"><span style="top:-3.063em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight"><span class="mord mathrm mtight">1</span><span class="mord mathrm mtight">/</span><span class="mord mathrm mtight">2</span></span></span></span></span></span></span></span></span><span class="mclose">)</span></span></span></span> is governed by whether <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>p</mi></mrow><annotation encoding="application/x-tex">p</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.43056em;"></span><span class="strut bottom" style="height:0.625em;vertical-align:-0.19444em;"></span><span class="base"><span class="mord mathit">p</span></span></span></span> is a square mod <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>q</mi></mrow><annotation encoding="application/x-tex">q</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.43056em;"></span><span class="strut bottom" style="height:0.625em;vertical-align:-0.19444em;"></span><span class="base"><span class="mord mathit" style="margin-right:0.03588em;">q</span></span></span></span></p>

#### [ Patrick Massot (Sep 16 2018 at 23:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quadratic%20reciprocity%20graph/near/134068804):
<p><a href="/user_uploads/3121/MzakNFD8LM3qNGgIlSgA6br0/screenshot_234141.png" target="_blank" title="screenshot_234141.png">screenshot_234141.png</a></p>
<div class="message_inline_image"><a href="/user_uploads/3121/MzakNFD8LM3qNGgIlSgA6br0/screenshot_234141.png" target="_blank" title="screenshot_234141.png"><img src="/user_uploads/3121/MzakNFD8LM3qNGgIlSgA6br0/screenshot_234141.png"></a></div>

#### [ Kevin Buzzard (Sep 16 2018 at 23:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quadratic%20reciprocity%20graph/near/134068844):
<p>but the factorization in <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mrow><mi mathvariant="double-struck">Q</mi></mrow><mo>(</mo><msub><mi>ζ</mi><mi>p</mi></msub><mo>)</mo></mrow><annotation encoding="application/x-tex">\mathbb{Q}(\zeta_p)</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.75em;"></span><span class="strut bottom" style="height:1.036108em;vertical-align:-0.286108em;"></span><span class="base"><span class="mord"><span class="mord mathbb">Q</span></span><span class="mopen">(</span><span class="mord"><span class="mord mathit" style="margin-right:0.07378em;">ζ</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.15139200000000003em;"><span style="top:-2.5500000000000003em;margin-left:-0.07378em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mathit mtight">p</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.286108em;"></span></span></span></span></span><span class="mclose">)</span></span></span></span> is determined by the behaviour of <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>q</mi></mrow><annotation encoding="application/x-tex">q</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.43056em;"></span><span class="strut bottom" style="height:0.625em;vertical-align:-0.19444em;"></span><span class="base"><span class="mord mathit" style="margin-right:0.03588em;">q</span></span></span></span> mod <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>p</mi></mrow><annotation encoding="application/x-tex">p</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.43056em;"></span><span class="strut bottom" style="height:0.625em;vertical-align:-0.19444em;"></span><span class="base"><span class="mord mathit">p</span></span></span></span> and there's the link.</p>

#### [ Patrick Massot (Sep 16 2018 at 23:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quadratic%20reciprocity%20graph/near/134068855):
<p>In this last version you can actually browse the graph and see what's there</p>

#### [ Kevin Buzzard (Sep 16 2018 at 23:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quadratic%20reciprocity%20graph/near/134068856):
<p>This proof historically came much later though. It then goes on to become Artin reciprocity in the early 1900s, which then gets generalised to Langlands reciprocity, a statement sufficiently vague that nobody knows what it is.</p>

#### [ Kevin Buzzard (Sep 16 2018 at 23:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quadratic%20reciprocity%20graph/near/134068857):
<p>But we know it when we see it.</p>

#### [ Kevin Buzzard (Sep 16 2018 at 23:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quadratic%20reciprocity%20graph/near/134068897):
<p>We just can't state it precisely.</p>

#### [ Kevin Buzzard (Sep 16 2018 at 23:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quadratic%20reciprocity%20graph/near/134068900):
<p>Patrick is it easy to say what the definitions and instances are?</p>

#### [ Kenny Lau (Sep 16 2018 at 23:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quadratic%20reciprocity%20graph/near/134068912):
<p>one should ask</p>

#### [ Patrick Massot (Sep 16 2018 at 23:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quadratic%20reciprocity%20graph/near/134068913):
<p>Do you want lists of definitions, or do you want to know which color is what?</p>

#### [ Kenny Lau (Sep 16 2018 at 23:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quadratic%20reciprocity%20graph/near/134068914):
<p>is Chris's proof a proof?</p>

#### [ Kevin Buzzard (Sep 16 2018 at 23:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quadratic%20reciprocity%20graph/near/134068916):
<p>Not of Langlands reciprocity, but probably of quadratic reciprocity.</p>

#### [ Kenny Lau (Sep 16 2018 at 23:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quadratic%20reciprocity%20graph/near/134068957):
<p>should proofs give us some understanding about <em>why</em> it is true?</p>

#### [ Kevin Buzzard (Sep 16 2018 at 23:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quadratic%20reciprocity%20graph/near/134068958):
<p>I was wondering what the names of the small list of things that weren't theorems were. I can look tomorrow. I'm just off to bed.</p>

#### [ Kevin Buzzard (Sep 16 2018 at 23:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quadratic%20reciprocity%20graph/near/134068959):
<blockquote>
<p>should proofs give us some understanding about <em>why</em> it is true?</p>
</blockquote>
<p>That's so 1900s.</p>

#### [ Kevin Buzzard (Sep 16 2018 at 23:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quadratic%20reciprocity%20graph/near/134068961):
<p>If it happens, it's a bonus. If it doesn't, rotten luck.</p>

#### [ Patrick Massot (Sep 16 2018 at 23:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quadratic%20reciprocity%20graph/near/134068963):
<p>Kevin, in gephi, if you go to tab probably called "data lab" (guessing from my French speaking version), you can sort by type of node</p>

#### [ Kevin Buzzard (Sep 16 2018 at 23:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quadratic%20reciprocity%20graph/near/134068964):
<p>It's like asking if food which is good for you should taste nice.</p>

#### [ Patrick Massot (Sep 16 2018 at 23:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quadratic%20reciprocity%20graph/near/134069014):
<p>But of course I can also ask the python shell. Definitions are:</p>
<div class="codehilite"><pre><span></span>[&#39;finset.univ&#39;,
 &#39;fintype.fintype_prod_right&#39;,
 &#39;nat.modeq&#39;,
 &#39;multiset&#39;,
 &#39;nat.prime&#39;,
 &#39;zmodp&#39;,
 &#39;fintype.fintype_prod_left&#39;,
 &#39;zmod&#39;,
 &#39;fintype.card&#39;,
 &#39;zmodp.legendre_sym&#39;,
 &#39;fintype.of_equiv&#39;,
 &#39;multiset.card&#39;,
 &#39;multiset.map&#39;,
 &#39;set_fintype&#39;,
 &#39;order_of&#39;,
 &#39;nat.decidable_prime_1&#39;]
</pre></div>

#### [ Patrick Massot (Sep 16 2018 at 23:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quadratic%20reciprocity%20graph/near/134069024):
<p>instances:</p>
<div class="codehilite"><pre><span></span>[&#39;zmodp.comm_ring&#39;,
 &#39;list.perm.setoid&#39;,
 &#39;zmod.has_neg&#39;,
 &#39;zmod.add_comm_semigroup&#39;,
 &#39;zmod.has_zero&#39;,
 &#39;zmodp.decidable_eq&#39;,
 &#39;fintype.decidable_exists_fintype&#39;,
 &#39;zmodp.discrete_field&#39;,
 &#39;zmod.has_one&#39;,
 &#39;zmodp.fintype&#39;,
 &#39;fin.fintype&#39;,
 &#39;fintype.decidable_forall_fintype&#39;,
 &#39;decidable_gpowers&#39;,
 &#39;zmod.comm_ring&#39;,
 &#39;fintype.subsingleton&#39;,
 &#39;prod.fintype&#39;,
 &#39;nat.decidable&#39;,
 &#39;zmod.fintype&#39;]
</pre></div>

#### [ Patrick Massot (Sep 16 2018 at 23:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quadratic%20reciprocity%20graph/near/134069071):
<p>and I should also go to bed</p>

#### [ Kenny Lau (Sep 16 2018 at 23:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quadratic%20reciprocity%20graph/near/134069230):
<p>there's something wrong with me if Patrick consistently goes to bed earlier than me</p>

#### [ Kevin Buzzard (Sep 16 2018 at 23:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quadratic%20reciprocity%20graph/near/134069272):
<p>I am not sure that Gauss's proofs of quadratic reciprocity gave us any understanding of why the theorem is true. The arguments are sufficiently elementary to be easily checkable by a third year undergraduate but at the end of the day it's a big motivationless computation of eg the number of dots in a rectangle counted in a weird way</p>

#### [ Kevin Buzzard (Sep 16 2018 at 23:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quadratic%20reciprocity%20graph/near/134069273):
<p>What insight does that give us?</p>

#### [ Kenny Lau (Sep 16 2018 at 23:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quadratic%20reciprocity%20graph/near/134069275):
<p>I can confirm the part about third year undergraduate</p>

#### [ Kenny Lau (Sep 16 2018 at 23:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quadratic%20reciprocity%20graph/near/134069278):
<p>I was in the very course</p>

#### [ Kevin Buzzard (Sep 16 2018 at 23:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quadratic%20reciprocity%20graph/near/134069285):
<p>You went to Toby's lectures?</p>

#### [ Kenny Lau (Sep 16 2018 at 23:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quadratic%20reciprocity%20graph/near/134069287):
<p>yes</p>

#### [ Kevin Buzzard (Sep 17 2018 at 00:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quadratic%20reciprocity%20graph/near/134069345):
<p>And the student was right :-)</p>

#### [ Kevin Buzzard (Sep 17 2018 at 00:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quadratic%20reciprocity%20graph/near/134069346):
<p>I got some of the summer students to formalise his example sheet questions and after a few hours one of them came up to me and told me that the first part of the first question was false :-)</p>

#### [ Kevin Buzzard (Sep 17 2018 at 00:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quadratic%20reciprocity%20graph/near/134069347):
<p>Which proof did he give? The Hardy and Wright one?</p>

#### [ Kenny Lau (Sep 17 2018 at 00:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quadratic%20reciprocity%20graph/near/134069387):
<p>the rectangle one</p>

#### [ Kevin Buzzard (Sep 17 2018 at 10:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quadratic%20reciprocity%20graph/near/134087595):
<blockquote>
<p>there's something wrong with me if Patrick consistently goes to bed earlier than me</p>
</blockquote>
<p>It's called "you are not a parent and don't have a job" -- I'm not sure that this qualifies as something wrong with you, it just means you're young.</p>

#### [ Kevin Buzzard (Sep 17 2018 at 10:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quadratic%20reciprocity%20graph/near/134087882):
<p>But back to the point I've been thinking more about quadratic reciprocity. What insight does that stupid rectangle proof give you? It's of the form "divide the rectangle up into about 6 regions, prove some boring lemmas about the number of points in each region, add everything up, deduce quadratic reciprocity". I am not at all sure that it gives you any insight into why the theorem is true at all. Chris gave an excellent summary of the proof -- "invoke some standard lemmas and then do a completely unmotivated computation about an apparently unrelated rectangle, and it happens to drop out". Kenny -- you probably followed Toby's proof -- can you then give me a succinct one-line summary as to why an odd prime p is a square mod 13 if and only if 13 is a square mod p? That assertion on the face of it looks like the ramblings of a madman -- those statements clearly have nothing to do with each other. The proof is entirely non-constructive as well (of course -- actually computing the square root of 13 mod p is computationally hard if p is huge, whereas computing a square root of p mod 13 is trivial). Is the rectangle proof really a proof? I read it and read it, and I still have no idea "why" the theorem is true.</p>
<p>Looking at it now, that proof of quadratic reciprocity looks pretty much the same as the four colour theorem proof to me -- that proof goes something like: divide the problem up into around 2000 graphs, prove a lemma about each graph, put everything together. And yet people regard quadratic reciprocity as a brilliant thing and the 4 colour proof as something which gives no insight. Are we just being blinded by the fact that 6 is less than 2000?</p>

#### [ Johan Commelin (Sep 17 2018 at 10:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quadratic%20reciprocity%20graph/near/134087952):
<blockquote>
<p>Are we just being blinded by the fact that 6 is less than 2000?</p>
</blockquote>
<p>Yes, we are!</p>

#### [ Reid Barton (Sep 17 2018 at 14:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quadratic%20reciprocity%20graph/near/134097189):
<p>Wasn't there some "one-sentence" proof which showed an equation (maybe writing a prime 1 mod 4 as the sum of two squares?) has a solution by exhibiting an involution on some set of tuples of integers whose fixed points were solutions to the equations, and then exhibiting a second involution on the same set which obviously had a unique fixed point (or maybe an odd number of them)</p>

#### [ Chris Hughes (Sep 17 2018 at 14:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quadratic%20reciprocity%20graph/near/134097214):
<p>Yes. Here it is in lean <a href="https://github.com/dorhinj/leanstuff/blob/master/fermat_sum_two_squares.lean" target="_blank" title="https://github.com/dorhinj/leanstuff/blob/master/fermat_sum_two_squares.lean">https://github.com/dorhinj/leanstuff/blob/master/fermat_sum_two_squares.lean</a></p>

#### [ Kevin Buzzard (Sep 17 2018 at 14:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quadratic%20reciprocity%20graph/near/134098431):
<p>This is Zagier's "one line proof" that a prime which is 1 mod 4 is the sum of two squares. Since then a slightly simpler involution argument has been found: see <a href="https://www.sciencedirect.com/science/article/pii/S0012365X15004355" target="_blank" title="https://www.sciencedirect.com/science/article/pii/S0012365X15004355">https://www.sciencedirect.com/science/article/pii/S0012365X15004355</a> (possibly behind a firewall).</p>

#### [ Kevin Buzzard (Sep 17 2018 at 14:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quadratic%20reciprocity%20graph/near/134098479):
<p>Zagier's proof is here: <a href="https://www.jstor.org/stable/2323918?origin=crossref&amp;seq=1#metadata_info_tab_contents" target="_blank" title="https://www.jstor.org/stable/2323918?origin=crossref&amp;seq=1#metadata_info_tab_contents">https://www.jstor.org/stable/2323918?origin=crossref&amp;seq=1#metadata_info_tab_contents</a></p>

#### [ Reid Barton (Sep 17 2018 at 14:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quadratic%20reciprocity%20graph/near/134098763):
<p>Yes this is the one I was thinking of. Nice!<br>
I wonder how many of these verifications could be done automatically with a tool like Z3. Obviously it wouldn't be able to do the steps which use the fact that p is prime, but those cases could be handled manually and then fed in as additional hypotheses.</p>

#### [ Kevin Buzzard (Sep 17 2018 at 15:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quadratic%20reciprocity%20graph/near/134099135):
<p>I would be very interested in hearing people's opinion on to what extent this is possible.</p>

#### [ Kevin Buzzard (Sep 17 2018 at 15:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quadratic%20reciprocity%20graph/near/134099150):
<p>Any mathematics which is undergraduate level -- I am interested in what state of the art proof verification software can do.</p>

#### [ Reid Barton (Sep 17 2018 at 15:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quadratic%20reciprocity%20graph/near/134099230):
<p>I guess I could try some of these</p>

#### [ Reid Barton (Sep 17 2018 at 15:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quadratic%20reciprocity%20graph/near/134100248):
<p>Here's what I did so far. I didn't put in the assumption that p is prime obviously, I just stated it must be at least 5 in case that was important.</p>
<div class="codehilite"><pre><span></span>(declare-const p Int)
(assert (&gt; p 4))

(declare-datatypes () ((Triple (mk (x Int) (y Int) (z Int)))))

(define-fun S ((t Triple)) Bool
  (= (+ (* (x t) (x t)) (* 4 (y t) (z t))) p))
(define-fun f1 ((t Triple)) Triple
  (mk (x t) (z t) (y t)))
(define-fun f2 ((t Triple)) Triple
  (ite (&lt; (+ (x t) (z t)) (y t))
       (mk (+ (x t) (* 2 (z t))) (z t) (- (y t) (x t) (z t)))
       (ite (&lt; (* 2 (y t)) (x t))
        (mk (- (x t) (* 2 (y t))) (+ (- (x t) (y t)) (z t)) (y t))
        (mk (- (* 2 (y t)) (x t)) (y t) (+ (- (x t) (y t)) (z t))))))

(declare-const t Triple)
(assert (S t))

(push)
(assert (not (S (f1 t))))
(check-sat)             ; unsat
(pop)

(push)
(assert (not (= t (f1 (f1 t)))))    ; unsat
(check-sat)
(pop)

(push)
(assert (not (S (f2 t))))       ; unsat
(check-sat)
(pop)

(push)
(assert (not (= t (f2 (f2 t)))))
(check-sat)             ; sat

(declare-const t1 Triple)
(assert (= t1 (f2 t)))
(declare-const t2 Triple)
(assert (= t2 (f2 t1)))

(check-sat)             ; sat
(get-model)             ; p = 9, t = (3,1,0), t1 = (1,2,1), t2 = (3,2,0)
(pop)
</pre></div>

#### [ Reid Barton (Sep 17 2018 at 15:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quadratic%20reciprocity%20graph/near/134100272):
<p>I learned that to prove f2 is an involution on S I need some further condition--looking at Chris's proof it's these checks that x, y, z have to be positive.</p>

#### [ Reid Barton (Sep 17 2018 at 15:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quadratic%20reciprocity%20graph/near/134100436):
<p>Now I replaced the last section by</p>
<div class="codehilite"><pre><span></span>(push)
(assert (not (= t (f2 (f2 t)))))
(assert (&gt; (x t) 0))
(assert (&gt; (y t) 0))
(assert (&gt; (z t) 0))
(check-sat)                             ; unsat
(pop)
</pre></div>


<p>so x y z positive is enough to prove it.</p>

#### [ Chris Hughes (Sep 17 2018 at 15:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quadratic%20reciprocity%20graph/near/134100519):
<p>You only need that p is not square for x y z positive. Can you weaken the condition to that?</p>

#### [ Reid Barton (Sep 17 2018 at 15:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quadratic%20reciprocity%20graph/near/134100590):
<p>I didn't even say that p is prime or what it is mod 4 yet</p>

#### [ Reid Barton (Sep 17 2018 at 15:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quadratic%20reciprocity%20graph/near/134100594):
<p>Oh, I see.</p>

#### [ Reid Barton (Sep 17 2018 at 15:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quadratic%20reciprocity%20graph/near/134100598):
<p>Hm...</p>

#### [ Reid Barton (Sep 17 2018 at 15:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quadratic%20reciprocity%20graph/near/134100625):
<p>I'm not sure if I can encode "p is not square" in a helpful way</p>

#### [ Reid Barton (Sep 17 2018 at 15:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quadratic%20reciprocity%20graph/near/134100756):
<p>I tried <code>(assert (forall ((n Int)) (not (= p (* n n)))))</code>, but now Z3 seems to be running forever on the fourth check</p>

#### [ Reid Barton (Sep 17 2018 at 15:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quadratic%20reciprocity%20graph/near/134100888):
<p>Oh, I also missed part of the definition of S</p>

#### [ Reid Barton (Sep 17 2018 at 15:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quadratic%20reciprocity%20graph/near/134100944):
<p>okay, now it can actually do the fourth part with <code>(assert (forall ((n Int)) (not (= p (* n n)))))</code> and with the nonnegativity included in the definition of S</p>

#### [ Reid Barton (Sep 17 2018 at 15:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quadratic%20reciprocity%20graph/near/134101038):
<p>For f2 having a unique fixed point, it can prove (if I ask it to) that for a fixed point, we must have x = y</p>

#### [ Reid Barton (Sep 17 2018 at 15:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quadratic%20reciprocity%20graph/near/134101232):
<p>Here's the whole thing <a href="https://gist.github.com/rwbarton/440ef225da3c243c1c03028d5d32f87b" target="_blank" title="https://gist.github.com/rwbarton/440ef225da3c243c1c03028d5d32f87b">https://gist.github.com/rwbarton/440ef225da3c243c1c03028d5d32f87b</a></p>

#### [ Reid Barton (Sep 17 2018 at 15:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quadratic%20reciprocity%20graph/near/134101304):
<p>I guess maybe I can express not prime too, then</p>

#### [ Reid Barton (Sep 17 2018 at 15:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quadratic%20reciprocity%20graph/near/134101319):
<p>Or being prime, rather</p>

#### [ Reid Barton (Sep 17 2018 at 15:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quadratic%20reciprocity%20graph/near/134101785):
<p>Updated: <a href="https://gist.github.com/rwbarton/440ef225da3c243c1c03028d5d32f87b" target="_blank" title="https://gist.github.com/rwbarton/440ef225da3c243c1c03028d5d32f87b">https://gist.github.com/rwbarton/440ef225da3c243c1c03028d5d32f87b</a><br>
If I tell it p is prime, it can check the first four facts and it can still prove that a fixed point of f2 must satisfy x = y but it can't deduce that x = y = 1. I guess it doesn't hit on the idea of using distributivity</p>

#### [ Reid Barton (Sep 17 2018 at 15:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quadratic%20reciprocity%20graph/near/134102026):
<p>I can't get <code>(set-option :produce-proofs true)</code> to do anything, not sure whether I am using it wrong or whether Z3 just doesn't want to produce proofs for the theory of integer arithmetic</p>

#### [ Reid Barton (Sep 17 2018 at 16:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quadratic%20reciprocity%20graph/near/134102470):
<p>oh you have to ask it for the proof explicitly as well</p>

#### [ Reid Barton (Sep 18 2018 at 01:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quadratic%20reciprocity%20graph/near/134134218):
<p>Kevin I would say that the partitions proof no longer has any steps which I would want out to Z3. At least not very large ones.</p>

#### [ Reid Barton (Sep 18 2018 at 01:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quadratic%20reciprocity%20graph/near/134134278):
<p>I think I could explain it to someone at the board and there aren't really any mysterious computations happening.</p>

#### [ Reid Barton (Sep 18 2018 at 01:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quadratic%20reciprocity%20graph/near/134134314):
<p>Whereas the Zagier proof has a couple ring computations to do plus various facts about linear inequalities to check</p>


{% endraw %}
