---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/57481LeanLaTeX.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [Lean + LaTeX?](https://leanprover-community.github.io/archive/113488general/57481LeanLaTeX.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Kevin Buzzard (Jan 23 2019 at 12:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20%2B%20LaTeX%3F/near/156681378):
<p>I've been reading work of Lamport about structured proofs.  Here's an extract from <a href="https://github.com/ImperialCollegeLondon/M1P1-lean/blob/master/src/limits.lean" target="_blank" title="https://github.com/ImperialCollegeLondon/M1P1-lean/blob/master/src/limits.lean">https://github.com/ImperialCollegeLondon/M1P1-lean/blob/master/src/limits.lean</a> :</p>
<div class="codehilite"><pre><span></span><span class="c1">-- We now prove that if aₙ → l and bₙ → m then aₙ + bₙ → l + m.</span>
<span class="kn">theorem</span> <span class="n">tendsto_add</span> <span class="o">(</span><span class="n">a</span> <span class="o">:</span> <span class="bp">ℕ</span> <span class="bp">→</span> <span class="n">ℝ</span><span class="o">)</span> <span class="o">(</span><span class="n">b</span> <span class="o">:</span> <span class="bp">ℕ</span> <span class="bp">→</span> <span class="n">ℝ</span><span class="o">)</span> <span class="o">(</span><span class="n">l</span> <span class="n">m</span> <span class="o">:</span> <span class="n">ℝ</span><span class="o">)</span>
  <span class="o">(</span><span class="n">h1</span> <span class="o">:</span> <span class="n">is_limit</span> <span class="n">a</span> <span class="n">l</span><span class="o">)</span> <span class="o">(</span><span class="n">h2</span> <span class="o">:</span> <span class="n">is_limit</span> <span class="n">b</span> <span class="n">m</span><span class="o">)</span> <span class="o">:</span>
  <span class="n">is_limit</span> <span class="o">(</span><span class="n">a</span> <span class="bp">+</span> <span class="n">b</span><span class="o">)</span> <span class="o">(</span><span class="n">l</span> <span class="bp">+</span> <span class="n">m</span><span class="o">)</span> <span class="o">:=</span>
<span class="k">begin</span>
  <span class="c1">-- let epsilon be a positive real</span>
  <span class="n">intros</span> <span class="n">ε</span> <span class="n">Hε</span><span class="o">,</span>
  <span class="c1">-- We now need to come up with N such that</span>
  <span class="c1">-- n &gt;= N implies |aₙ + bₙ - (l + m)| &lt; ε.</span>
  <span class="c1">-- Well, note first that epsilon / 2 is also positive.</span>
  <span class="k">have</span> <span class="n">Hε2</span> <span class="o">:</span> <span class="n">ε</span> <span class="bp">/</span> <span class="mi">2</span> <span class="bp">&gt;</span> <span class="mi">0</span> <span class="o">:=</span> <span class="k">by</span> <span class="n">linarith</span><span class="o">,</span>
  <span class="c1">-- Choose large M₁ such that n ≥ M₁ implies |a n - l| &lt; ε /2,</span>
  <span class="n">cases</span> <span class="o">(</span><span class="n">h1</span> <span class="o">(</span><span class="n">ε</span> <span class="bp">/</span> <span class="mi">2</span><span class="o">)</span> <span class="n">Hε2</span><span class="o">)</span> <span class="k">with</span> <span class="n">M₁</span> <span class="n">HM₁</span><span class="o">,</span>
  <span class="c1">-- and similarly choose M₂ for the b sequence.</span>
  <span class="n">cases</span> <span class="o">(</span><span class="n">h2</span> <span class="o">(</span><span class="n">ε</span> <span class="bp">/</span> <span class="mi">2</span><span class="o">)</span> <span class="n">Hε2</span><span class="o">)</span> <span class="k">with</span> <span class="n">M₂</span> <span class="n">HM₂</span><span class="o">,</span>
  <span class="c1">-- let N be the max of M1 and M2</span>
  <span class="k">let</span> <span class="n">N</span> <span class="o">:=</span> <span class="n">max</span> <span class="n">M₁</span> <span class="n">M₂</span><span class="o">,</span>
  <span class="c1">-- and let&#39;s use this value of N.</span>
  <span class="n">use</span> <span class="n">N</span><span class="o">,</span>
  <span class="c1">-- Of course N ≥ M₁ and N ≥ M₂.</span>
  <span class="k">have</span> <span class="n">H₁</span> <span class="o">:</span> <span class="n">N</span> <span class="bp">≥</span> <span class="n">M₁</span> <span class="o">:=</span> <span class="n">le_max_left</span> <span class="bp">_</span> <span class="bp">_</span><span class="o">,</span>
  <span class="k">have</span> <span class="n">H₂</span> <span class="o">:</span> <span class="n">N</span> <span class="bp">≥</span> <span class="n">M₂</span> <span class="o">:=</span> <span class="n">le_max_right</span> <span class="bp">_</span> <span class="bp">_</span><span class="o">,</span>
  <span class="c1">-- Now say n ≥ N.</span>
  <span class="n">intros</span> <span class="n">n</span> <span class="n">Hn</span><span class="o">,</span>
  <span class="c1">-- Then obviously n ≥ M₁...</span>
  <span class="k">have</span> <span class="n">Hn₁</span> <span class="o">:</span> <span class="n">n</span> <span class="bp">≥</span> <span class="n">M₁</span> <span class="o">:=</span> <span class="k">by</span> <span class="n">linarith</span><span class="o">,</span>
  <span class="c1">-- ...so |aₙ - l| &lt; ε /2</span>
<span class="k">have</span> <span class="n">H3</span> <span class="o">:</span> <span class="bp">|</span><span class="n">a</span> <span class="n">n</span> <span class="bp">-</span> <span class="n">l</span><span class="bp">|</span> <span class="bp">&lt;</span> <span class="n">ε</span> <span class="bp">/</span> <span class="mi">2</span> <span class="o">:=</span> <span class="n">HM₁</span> <span class="n">n</span> <span class="n">Hn₁</span><span class="o">,</span>
<span class="bp">...</span>
</pre></div>


<p>and so on and so on. The point is that I am spelling out the proof I would tell mathematicians in comments, and writing Lean code, which is sometimes self-evident (<code>intros n Hn</code>) and sometimes much harder for beginners to understand (e.g. using <code>le_max_left</code> -- a student could look up what this did, but it's much harder for them to find this function for themselves, and there are far more contrived lines in other parts of this repo). </p>
<p>I would like to make this look really sexy and I am almost sure that this should be possible with known technology. My dream would be to have what looks like a LaTeX document (perhaps viewed through a web browser) and when you hover over e.g. "Then obviously n &gt;= M_1" you get some transient box which says <code>have Hn₁ : n ≥ M₁ := by linarith,</code>, and if you click on it then you somehow end up viewing a Lean file, or part of a Lean file, where you can look at the goal and change / edit things and play around (and then hit the "reset" button when you've screwed everything up).</p>
<p>In other words, I'd like to have some sort of thing which I can present as a "formally verified, but looks like LaTeX, proof that the limit of the sum is the sum of the limits". </p>
<p>I have no doubt that this sort of thing is possible. I've learnt sphinx but I am not quite sure if it is the tool for the job. Does anyone have any suggestions as to how one might be able to do this? There is no particular time frame and if it involves writing a bunch of code then maybe I can find people who will write this code for me. <span class="user-mention" data-user-id="121918">@Edward Ayers</span> <span class="user-mention" data-user-id="110031">@Patrick Massot</span> do either of you know about this kind of thing? </p>
<p>When it comes to writing Lean code I am 100% convinced that I could write code in the above style which could become "online notes" for a beginning analysis course (such as, let's say, the beginning analysis course in Imperial's new curriculum which starts in October). The notes would have the advantage that they are formally verified. But I do not understand enough about how to build the app I envisage and I would dearly like to hear some suggestions!</p>

#### [ Johan Commelin (Jan 23 2019 at 12:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20%2B%20LaTeX%3F/near/156682310):
<p>Do you remember Neil Stricklands demo? That might be a first approximation of what you want.</p>

#### [ Johan Commelin (Jan 23 2019 at 12:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20%2B%20LaTeX%3F/near/156682399):
<p>I meant this one: <a href="http://neil-strickland.staff.shef.ac.uk/dagstuhl/Systems/Lean_mathlib/Tasks/primes/" target="_blank" title="http://neil-strickland.staff.shef.ac.uk/dagstuhl/Systems/Lean_mathlib/Tasks/primes/">http://neil-strickland.staff.shef.ac.uk/dagstuhl/Systems/Lean_mathlib/Tasks/primes/</a></p>

#### [ Kevin Buzzard (Jan 23 2019 at 12:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20%2B%20LaTeX%3F/near/156683049):
<p>Ooh -- thanks for digging that up! <span class="user-mention" data-user-id="130308">@Neil Strickland</span> how did you make this? My plan would be to hide the Lean completely and just have standard maths proof prose visible initially, but one can somehow open up the Lean to see it if one wants to.</p>

#### [ Joseph Corneli (Jan 23 2019 at 15:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20%2B%20LaTeX%3F/near/156693777):
<p><span class="user-mention" data-user-id="110038">@Kevin Buzzard</span> As a quick mockup in Emacs, I used Outshine mode to achieve the following (I realise this doesn't address the LaTeX side of things at all).  This required changing the comment syntax a little bit.  <a href="/user_uploads/3121/_NxlgyLxGewpsjrAPECKZ-g9/Screen-Shot-2019-01-23-at-14.41.33.png" target="_blank" title="Screen-Shot-2019-01-23-at-14.41.33.png">Screen-Shot-2019-01-23-at-14.41.33.png</a></p>
<div class="message_inline_image"><a href="/user_uploads/3121/_NxlgyLxGewpsjrAPECKZ-g9/Screen-Shot-2019-01-23-at-14.41.33.png" target="_blank" title="Screen-Shot-2019-01-23-at-14.41.33.png"><img src="/user_uploads/3121/_NxlgyLxGewpsjrAPECKZ-g9/Screen-Shot-2019-01-23-at-14.41.33.png"></a></div>

#### [ Joseph Corneli (Jan 23 2019 at 15:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20%2B%20LaTeX%3F/near/156693999):
<p>pressing TAB at the start of the buffer, or on a "headline", cycles between showing or not showing headlines / all content below that level.</p>

#### [ Joseph Corneli (Jan 23 2019 at 15:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20%2B%20LaTeX%3F/near/156694296):
<p>Maybe there's a similar plugin to Outshine for VS Code? </p>
<p>For presentation purposes, a related setup for Jupyter is described here: <br>
<a href="http://chris-said.io/2016/02/13/how-to-make-polished-jupyter-presentations-with-optional-code-visibility/" target="_blank" title="http://chris-said.io/2016/02/13/how-to-make-polished-jupyter-presentations-with-optional-code-visibility/">http://chris-said.io/2016/02/13/how-to-make-polished-jupyter-presentations-with-optional-code-visibility/</a><br>
with a clickable demo here:<br>
<a href="https://nbviewer.jupyter.org/github/csaid/polished_notebooks/blob/master/notebook_polished.ipynb" target="_blank" title="https://nbviewer.jupyter.org/github/csaid/polished_notebooks/blob/master/notebook_polished.ipynb">https://nbviewer.jupyter.org/github/csaid/polished_notebooks/blob/master/notebook_polished.ipynb</a></p>

#### [ Patrick Massot (Jan 23 2019 at 17:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20%2B%20LaTeX%3F/near/156701032):
<p>Indeed this is something we can already mostly do with current technology, although we should be able to do it much better with the Lean 4 parser. Without the possibility to modify the Lean code, we could make something very easily (maybe only after thinking a bit more about the expected output with nested subproofs). In order to get a truly interactive version we could reuse Gabriel's work on the documentation view.</p>

#### [ Kevin Buzzard (Jan 23 2019 at 17:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20%2B%20LaTeX%3F/near/156702191):
<p>Right. Nothing you say surprises me. Now how do I actually _do_ it?</p>

#### [ Patrick Massot (Jan 23 2019 at 17:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20%2B%20LaTeX%3F/near/156705049):
<p>Which version? Interactive or read-only?</p>

#### [ Kevin Buzzard (Jan 23 2019 at 18:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20%2B%20LaTeX%3F/near/156707960):
<p>read-only would be a good start.</p>

#### [ Neil Strickland (Jan 23 2019 at 18:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20%2B%20LaTeX%3F/near/156709620):
<p><span class="user-mention" data-user-id="110038">@Kevin Buzzard</span>  there is a new version of my examples now which you can find by following the links at  <a href="http://bim.shef.ac.uk/lean" target="_blank" title="http://bim.shef.ac.uk/lean">http://bim.shef.ac.uk/lean</a>.<br>
At the moment they are not packaged in a way that makes it super-easy for anyone else to use the same framework, but it is not all that sophisticated either.  The key ingredients are the files <br>
1. <a href="http://bim.shef.ac.uk/lean/viewer.js" target="_blank" title="http://bim.shef.ac.uk/lean/viewer.js">http://bim.shef.ac.uk/lean/viewer.js</a><br>
2. <a href="http://bim.shef.ac.uk/lean/viewer.css" target="_blank" title="http://bim.shef.ac.uk/lean/viewer.css">http://bim.shef.ac.uk/lean/viewer.css</a><br>
3. <a href="http://bim.shef.ac.uk/lean/lean_task_index.html" target="_blank" title="http://bim.shef.ac.uk/lean/lean_task_index.html">http://bim.shef.ac.uk/lean/lean_task_index.html</a> (which is a kind of template)<br>
4. Libraries <a href="http://bim.shef.ac.uk/js/jquery.js" target="_blank" title="http://bim.shef.ac.uk/js/jquery.js">http://bim.shef.ac.uk/js/jquery.js</a> and <a href="http://bim.shef.ac.uk/js/he.js" target="_blank" title="http://bim.shef.ac.uk/js/he.js">http://bim.shef.ac.uk/js/he.js</a><br>
For each example you need <br>
1. A copy of lean_task_index.html with the name, title and description filled in.<br>
2. A lean file with comments delineated by the strings <br>
"/-~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ "<br>
and <br>
"~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~-/"</p>
<p>Let me know if you want further details.</p>

#### [ Patrick Massot (Jan 23 2019 at 18:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20%2B%20LaTeX%3F/near/156709958):
<p>Neil, I just had a look at the very first example and something is not quite correct. <code>apply refl</code> is not using the <code>refl</code> tactic, it's using a lemma called <code>refl</code> (use F12 to see it). Use <code>refl</code> alone if you want the <code>refl</code> tactic.</p>

#### [ Neil Strickland (Jan 23 2019 at 19:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20%2B%20LaTeX%3F/near/156710182):
<p>Thanks, I'll fix that.</p>

#### [ Mohammad Pedramfar (Jan 23 2019 at 19:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20%2B%20LaTeX%3F/near/156712996):
<p>There is an old code here <a href="https://github.com/leanprover/lean.js" target="_blank" title="https://github.com/leanprover/lean.js">https://github.com/leanprover/lean.js</a></p>

#### [ Mohammad Pedramfar (Jan 23 2019 at 19:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20%2B%20LaTeX%3F/near/156713098):
<p>below in the examples. It's using lean interactively in the browser.</p>

#### [ Mohammad Pedramfar (Jan 23 2019 at 19:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20%2B%20LaTeX%3F/near/156713804):
<p>This seems to be exactly what you'd need to have an interactive lean webpage<br>
<a href="https://github.com/leanprover/lean-client-js/" target="_blank" title="https://github.com/leanprover/lean-client-js/">https://github.com/leanprover/lean-client-js/</a></p>

#### [ Patrick Massot (Jan 23 2019 at 22:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20%2B%20LaTeX%3F/near/156728489):
<blockquote>
<p>read-only would be a good start.</p>
</blockquote>
<p>I'll try to find time over the week-end to build some demo</p>

#### [ Mohammad Pedramfar (Jan 24 2019 at 16:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20%2B%20LaTeX%3F/near/156778439):
<p>Using the libraries that I mentioned doesn't seem to be very easy. On the other hand, directly manipulating the online lean website seems to be doable. I'll try to make a small interactive example in a few days.</p>

#### [ Bryan Gin-ge Chen (Jan 24 2019 at 16:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20%2B%20LaTeX%3F/near/156778956):
<p><span class="user-mention" data-user-id="132175">@Mohammad Pedramfar</span> I played around with trying to get a custom version of the web editor working a while back in this thread: <a href="#narrow/stream/113488-general/topic/online.20leanprover" title="#narrow/stream/113488-general/topic/online.20leanprover">https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/online.20leanprover</a> . I didn't get too far though.</p>

#### [ Mohammad Pedramfar (Jan 25 2019 at 11:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20%2B%20LaTeX%3F/near/156841534):
<p><span class="user-mention" data-user-id="123965">@Bryan Gin-ge Chen</span> Thanks. Hopefully this will be easier, since here we only need to play around with the reactjs code to to something in the frontend without touching other parts.</p>

#### [ Mohammad Pedramfar (Jan 27 2019 at 21:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20%2B%20LaTeX%3F/near/156987229):
<p>I changed a few things in the online lean editor and turned it into this : <a href="/user_uploads/3121/SV1PUgOO5U2DB4dzH-LExXak/lean-web-editor-with-latex.tar.gz" target="_blank" title="lean-web-editor-with-latex.tar.gz">lean-web-editor-with-latex.tar.gz</a></p>

#### [ Patrick Massot (Jan 27 2019 at 21:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20%2B%20LaTeX%3F/near/156987368):
<p>do you have a live demo somewhere?</p>

#### [ Mohammad Pedramfar (Jan 27 2019 at 21:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20%2B%20LaTeX%3F/near/156987504):
<p>I'm now running it at <a href="http://192.168.43.31:8080/" target="_blank" title="http://192.168.43.31:8080/">http://192.168.43.31:8080/</a></p>

#### [ Patrick Massot (Jan 27 2019 at 21:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20%2B%20LaTeX%3F/near/156987513):
<p>Firefox can’t establish a connection to the server at 192.168.43.31:8080.</p>

#### [ Wojciech Nawrocki (Jan 27 2019 at 21:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20%2B%20LaTeX%3F/near/156987523):
<p>That's a local-network IP :) It's not publicly accessible</p>

#### [ Patrick Massot (Jan 27 2019 at 21:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20%2B%20LaTeX%3F/near/156987526):
<p>(deleted)</p>

#### [ Mohammad Pedramfar (Jan 27 2019 at 21:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20%2B%20LaTeX%3F/near/156987540):
<p>I don't know why I thought http-server would run it on the web</p>

#### [ Mohammad Pedramfar (Jan 27 2019 at 21:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20%2B%20LaTeX%3F/near/156987594):
<p>is there an easy way to run it locally ?</p>

#### [ Patrick Massot (Jan 27 2019 at 21:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20%2B%20LaTeX%3F/near/156987599):
<p>You may be able to redirect something there</p>

#### [ Mohammad Pedramfar (Jan 27 2019 at 21:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20%2B%20LaTeX%3F/near/156987763):
<p>I don't know how to do that</p>

#### [ Patrick Massot (Jan 27 2019 at 22:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20%2B%20LaTeX%3F/near/156988002):
<p>Maybe you can explain how we could run it locally then, and what there is to see</p>

#### [ Mohammad Pedramfar (Jan 27 2019 at 22:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20%2B%20LaTeX%3F/near/156988077):
<p>sure, you'd need to follow the instructions in the readme. run these first :<br>
npm install<br>
./fetch_lean_js.sh<br>
./node_modules/.bin/webpack</p>

#### [ Mohammad Pedramfar (Jan 27 2019 at 22:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20%2B%20LaTeX%3F/near/156988127):
<p>then you can into the "dist" folder and run "http-server"</p>

#### [ Mohammad Pedramfar (Jan 27 2019 at 22:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20%2B%20LaTeX%3F/near/156988205):
<p>At the moment the content is hardcoded, I have yet to add some kind of editor for the latex part. For any line in the latex, if you click on it, you'll see the corresponding lean code. You can change it and see the goals and warnings etc. but if you click on another line, the changes won't be saved. You can also see all the lean code at the same time, which would be like the normal online editor.</p>

#### [ Patrick Massot (Jan 27 2019 at 22:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20%2B%20LaTeX%3F/near/156988337):
<p>Nice!</p>

#### [ Patrick Massot (Jan 27 2019 at 22:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20%2B%20LaTeX%3F/near/156988449):
<p>People who want to know what we are talking about can go to <a href="http://pat.perso.ens-lyon.org/lean/" target="_blank" title="http://pat.perso.ens-lyon.org/lean/">http://pat.perso.ens-lyon.org/lean/</a> (it probably won't stay there for long)</p>

#### [ Patrick Massot (Jan 27 2019 at 22:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20%2B%20LaTeX%3F/near/156988459):
<p>I can't see any error message when I edit the Lean code</p>

#### [ Patrick Massot (Jan 27 2019 at 22:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20%2B%20LaTeX%3F/near/156988520):
<p>wait, the LaTeX doesn't work there</p>

#### [ Patrick Massot (Jan 27 2019 at 22:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20%2B%20LaTeX%3F/near/156988525):
<p>I used to work when served locally</p>

#### [ Mohammad Pedramfar (Jan 27 2019 at 22:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20%2B%20LaTeX%3F/near/156988646):
<p>The error messages didn't show up at all or were they late ? because the code is probably not the most efficient code possible !</p>

#### [ Mohammad Pedramfar (Jan 27 2019 at 22:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20%2B%20LaTeX%3F/near/156988725):
<p>You're right about the LaTeX. I think it works only if things are loaded in the correct order. It shouldn't be difficult to fix.</p>

#### [ Patrick Massot (Jan 27 2019 at 22:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20%2B%20LaTeX%3F/near/156988739):
<p>I don't have time to play with this (I have lectures to prepare) but it looks like a nice try</p>

#### [ Mohammad Pedramfar (Jan 27 2019 at 22:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20%2B%20LaTeX%3F/near/156988788):
<p>Thanks</p>

#### [ Kevin Buzzard (Jan 27 2019 at 22:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20%2B%20LaTeX%3F/near/156989789):
<p>Hey that's very cool!</p>

#### [ Mohammad Pedramfar (Jan 28 2019 at 01:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20%2B%20LaTeX%3F/near/156994368):
<p>Glad you liked it. I'll make it a bit more usable this week.</p>

#### [ Kevin Buzzard (Jan 28 2019 at 23:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20%2B%20LaTeX%3F/near/157063321):
<p>Could you try something from <a href="https://github.com/ImperialCollegeLondon/M1P1-lean/blob/master/src/limits.lean" target="_blank" title="https://github.com/ImperialCollegeLondon/M1P1-lean/blob/master/src/limits.lean">https://github.com/ImperialCollegeLondon/M1P1-lean/blob/master/src/limits.lean</a>?</p>

#### [ Mohammad Pedramfar (Feb 01 2019 at 22:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20%2B%20LaTeX%3F/near/157389394):
<p>Sure, I'll sort it out this weekend</p>


{% endraw %}
