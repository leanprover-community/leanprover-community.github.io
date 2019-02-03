---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113489newmembers/00534BasiclogicinLean.html
---

## Stream: [new members](index.html)
### Topic: [Basic logic in Lean.](00534BasiclogicinLean.html)

---


{% raw %}
#### [ Kevin Buzzard (Oct 08 2018 at 15:50)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Basic%20logic%20in%20Lean./near/135404145):
<p>There has been some discussion about Q4 of my first M1F example sheet. The question and my solution are <a href="https://github.com/kbuzzard/xena/tree/master/M1F/problem_bank/PB0104" target="_blank" title="https://github.com/kbuzzard/xena/tree/master/M1F/problem_bank/PB0104">here</a> . My solution from this time last year is <a href="https://github.com/kbuzzard/xena/blob/a61d6db673ae8ab2672cbf6522894f743b08a6e6/M1F/2017-18/Example_Sheet_01/Questions_02_to_4/M1F_sheet01_solutions02_to_04.lean#L60" target="_blank" title="https://github.com/kbuzzard/xena/blob/a61d6db673ae8ab2672cbf6522894f743b08a6e6/M1F/2017-18/Example_Sheet_01/Questions_02_to_4/M1F_sheet01_solutions02_to_04.lean#L60">here</a> and is completely different. <span class="user-mention" data-user-id="110044">@Chris Hughes</span> and <span class="user-mention" data-user-id="110064">@Kenny Lau</span>  -- did you ever attempt to do M1F sheet 1 Q4 in Lean this time last year?</p>

#### [ Kevin Buzzard (Oct 08 2018 at 15:51)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Basic%20logic%20in%20Lean./near/135404266):
<p><span class="user-mention" data-user-id="130500">@Abhimanyu Pallavi Sudhir</span> 's solution is here: <a href="https://github.com/abhimanyupallavisudhir/lean/blob/master/m1f_sols/exsht01.lean" target="_blank" title="https://github.com/abhimanyupallavisudhir/lean/blob/master/m1f_sols/exsht01.lean">https://github.com/abhimanyupallavisudhir/lean/blob/master/m1f_sols/exsht01.lean</a></p>

#### [ Kevin Buzzard (Oct 08 2018 at 15:52)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Basic%20logic%20in%20Lean./near/135404326):
<p>Part of me feels like this would be a lot more fun in <code>bool</code>.</p>

#### [ Johan Commelin (Oct 08 2018 at 15:54)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Basic%20logic%20in%20Lean./near/135404440):
<p>You didn't teach them <code>ring</code>?</p>

#### [ Mario Carneiro (Oct 08 2018 at 15:56)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Basic%20logic%20in%20Lean./near/135404664):
<p>By the way, <span class="user-mention" data-user-id="110087">@Scott Morrison</span> this is a good example of where <code>fin_cases</code> on things other than <code>fin</code> would help</p>

#### [ Mario Carneiro (Oct 08 2018 at 15:57)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Basic%20logic%20in%20Lean./near/135404733):
<p>we have a fintype instance for <code>Prop</code>, which would substitute for <code>classical.cases</code> in this case</p>

#### [ Mario Carneiro (Oct 08 2018 at 16:03)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Basic%20logic%20in%20Lean./near/135405066):
<p>It would do basically the same thing as this:</p>
<div class="codehilite"><pre><span></span><span class="kn">variables</span> <span class="n">P</span> <span class="n">Q</span> <span class="n">R</span> <span class="n">S</span> <span class="o">:</span> <span class="kt">Prop</span>

<span class="kn">theorem</span> <span class="n">m1f_sheet01_q04</span> <span class="o">:</span> <span class="o">(</span><span class="n">P</span> <span class="bp">→</span> <span class="o">(</span><span class="n">Q</span> <span class="bp">∨</span> <span class="n">R</span><span class="o">))</span> <span class="bp">∧</span> <span class="o">(</span><span class="bp">¬</span> <span class="n">Q</span> <span class="bp">→</span> <span class="o">(</span><span class="n">R</span> <span class="bp">∨</span> <span class="bp">¬</span> <span class="n">P</span><span class="o">))</span> <span class="bp">∧</span> <span class="o">((</span><span class="n">Q</span> <span class="bp">∧</span> <span class="n">R</span><span class="o">)</span> <span class="bp">→</span> <span class="bp">¬</span> <span class="n">P</span><span class="o">)</span> <span class="bp">↔</span>
  <span class="o">(</span><span class="bp">¬</span> <span class="n">P</span><span class="o">)</span> <span class="bp">∨</span> <span class="o">(</span><span class="n">P</span> <span class="bp">∧</span> <span class="n">Q</span> <span class="bp">∧</span> <span class="bp">¬</span> <span class="n">R</span><span class="o">)</span> <span class="bp">∨</span> <span class="o">(</span><span class="n">P</span> <span class="bp">∧</span> <span class="bp">¬</span> <span class="n">Q</span> <span class="bp">∧</span> <span class="n">R</span><span class="o">)</span> <span class="o">:=</span>
<span class="k">by</span> <span class="n">refine</span> <span class="n">classical</span><span class="bp">.</span><span class="n">cases_true_false</span> <span class="bp">_</span> <span class="bp">_</span> <span class="bp">_</span> <span class="n">P</span><span class="bp">;</span>
   <span class="n">refine</span> <span class="n">classical</span><span class="bp">.</span><span class="n">cases_true_false</span> <span class="bp">_</span> <span class="bp">_</span> <span class="bp">_</span> <span class="n">Q</span><span class="bp">;</span>
   <span class="n">refine</span> <span class="n">classical</span><span class="bp">.</span><span class="n">cases_true_false</span> <span class="bp">_</span> <span class="bp">_</span> <span class="bp">_</span> <span class="n">R</span><span class="bp">;</span> <span class="n">simp</span>
</pre></div>

#### [ Patrick Massot (Oct 08 2018 at 16:14)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Basic%20logic%20in%20Lean./near/135405999):
<div class="codehilite"><pre><span></span><span class="kn">theorem</span> <span class="n">m1f_sheet01_q04</span> <span class="o">:</span> <span class="o">(</span><span class="n">P</span> <span class="bp">→</span> <span class="o">(</span><span class="n">Q</span> <span class="bp">∨</span> <span class="n">R</span><span class="o">))</span> <span class="bp">∧</span> <span class="o">(</span><span class="bp">¬</span> <span class="n">Q</span> <span class="bp">→</span> <span class="o">(</span><span class="n">R</span> <span class="bp">∨</span> <span class="bp">¬</span> <span class="n">P</span><span class="o">))</span> <span class="bp">∧</span> <span class="o">((</span><span class="n">Q</span> <span class="bp">∧</span> <span class="n">R</span><span class="o">)</span> <span class="bp">→</span> <span class="bp">¬</span> <span class="n">P</span><span class="o">)</span> <span class="bp">↔</span>
  <span class="o">(</span><span class="bp">¬</span> <span class="n">P</span><span class="o">)</span> <span class="bp">∨</span> <span class="o">(</span><span class="n">P</span> <span class="bp">∧</span> <span class="n">Q</span> <span class="bp">∧</span> <span class="bp">¬</span> <span class="n">R</span><span class="o">)</span> <span class="bp">∨</span> <span class="o">(</span><span class="n">P</span> <span class="bp">∧</span> <span class="bp">¬</span> <span class="n">Q</span> <span class="bp">∧</span> <span class="n">R</span><span class="o">)</span> <span class="o">:=</span>
<span class="k">by</span>  <span class="n">split</span> <span class="bp">;</span> <span class="n">finish</span>
</pre></div>


<p><span class="emoji emoji-1f61b" title="mischievous">:mischievous:</span></p>

#### [ Kevin Buzzard (Oct 08 2018 at 16:34)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Basic%20logic%20in%20Lean./near/135407445):
<blockquote>
<p>You didn't teach them <code>ring</code>?</p>
</blockquote>
<p>I wrote and am writing docs randomly and students are reading them randomly.</p>

#### [ Kevin Buzzard (Oct 08 2018 at 16:35)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Basic%20logic%20in%20Lean./near/135407480):
<p><a href="http://wwwf.imperial.ac.uk/~buzzard/xena/" target="_blank" title="http://wwwf.imperial.ac.uk/~buzzard/xena/">http://wwwf.imperial.ac.uk/~buzzard/xena/</a></p>

#### [ Kevin Buzzard (Oct 08 2018 at 16:35)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Basic%20logic%20in%20Lean./near/135407537):
<p>yeah, I haven't pushed the stuff I wrote about <code>ring</code>. My bad.</p>

#### [ Kevin Buzzard (Oct 08 2018 at 16:36)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Basic%20logic%20in%20Lean./near/135407586):
<p>I'm currently trying to get all the questions up for sheet 1.</p>

#### [ Johan Commelin (Oct 08 2018 at 16:36)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Basic%20logic%20in%20Lean./near/135407613):
<p>It's just that I felt sorry when I saw that 10-line <code>calc</code>ulation.</p>

#### [ Kevin Buzzard (Oct 08 2018 at 16:47)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Basic%20logic%20in%20Lean./near/135408370):
<p>Ah nonono, wait, I gave the students the axiom that <code>x^2-3x+2=0 iff x = 1 or x = 2</code></p>

#### [ Kevin Buzzard (Oct 08 2018 at 16:53)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Basic%20logic%20in%20Lean./near/135408792):
<p>But here's the problem -- giving them stuff is hard. It's hard to make a global import work for something which is not in mathlib on the systems my students use (cocalc, local lean set-up in our computer room, their Lean laptops). Can one pull a github dependency to a local machine easily using VS Code? Even that will not solve most of the problems. Both cocalc and my local ICT people have not given me a robust way of being able to add a growing library, and I didn't get this library written over the summer so I am having to write it now in real time.  However I do have a "homework" option with cocalc which I think should work. </p>
<p>The vast majority of students use my Xena.zip set-up on a computer in our computer room, where Lean is installed on all machines by magic via my cheap instructions, and I forgot to put a back door in the zip file and they wrote the script and now it's difficult for me to get the set-up changed. [ Hmm. I wonder if their script downloads Xena.zip or uses a local copy? Surely the latter.]</p>

#### [ Kevin Buzzard (Oct 08 2018 at 16:53)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Basic%20logic%20in%20Lean./near/135408822):
<p>I guess my mistake here is that I did not completely write the library before I was forced to make decisions which could not be easily reversed.</p>

#### [ Kevin Buzzard (Oct 08 2018 at 16:55)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Basic%20logic%20in%20Lean./near/135408915):
<p>Basically my solutions from last year need heavy editing, because I don't want the students to have to struggle through easy-in-maths less-easy-in-lean stuff, it will just get in their way. So all the stuff like x^2-3x+2=0 iff x=1 or x=2 is being moved into a different library; they just cluttered up my solutions last year. I can't figure out how to deliver this library to them easily though in our computer room. Hmm.</p>
<p>I might go for making it all work out of the box on cocalc and then making public github repos for the problem sheets; I won't need to worry about .olean files because the libraries will be very small and easy to compile. Is it easy for a complete git beginner to clone a github repo and open it completely within VS Code? Oh -- you can link to a zip file or something and tell them to unzip and open folder maybe?</p>

#### [ Patrick Massot (Oct 08 2018 at 17:02)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Basic%20logic%20in%20Lean./near/135409410):
<p>You can put olean in the zip only if you know their OS</p>

#### [ Kevin Buzzard (Oct 08 2018 at 17:08)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Basic%20logic%20in%20Lean./near/135409724):
<p>Right. I think I will have to skip olean files. Patrick's position is not even the official one, I believe: didn't Sebastian say they were not even guaranteed to run on a different machine with the same OS?</p>

#### [ Gabriel Ebner (Oct 08 2018 at 17:16)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Basic%20logic%20in%20Lean./near/135410223):
<p>The olean files should be machine- and OS-independent (but they definitely depend on the Lean version).  However you need to be really careful with the file modification times.  They need to be 1) after the olean files for lean itself, 2) after the lean files, and 3) in the correct order (i.e. logic/function.olean should be older than analysis/real.olean)</p>

#### [ Scott Morrison (Oct 08 2018 at 23:05)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Basic%20logic%20in%20Lean./near/135427947):
<p><span class="user-mention" data-user-id="110043">@Gabriel Ebner</span>  --- presumably condition 3) is satisfied if they all have exactly the same timestamp?</p>

#### [ Scott Morrison (Oct 08 2018 at 23:07)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Basic%20logic%20in%20Lean./near/135428020):
<p>Cloning a repo from VS Code consists of opening a terminal inside VS Code and doing it on the command line there...</p>

#### [ Scott Morrison (Oct 08 2018 at 23:09)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Basic%20logic%20in%20Lean./near/135428096):
<p>The fact that you need to make updates really suggests you should be using <code>leanpkg</code>. There's no need to interact with the command line --- in VS Code there is a command to run <code>leanpkg upgrade</code>.</p>

#### [ Gabriel Ebner (Oct 09 2018 at 09:41)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Basic%20logic%20in%20Lean./near/135450329):
<p>Yes, apparently the check is less-than-or-equals.</p>

#### [ Mario Carneiro (Oct 09 2018 at 09:43)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Basic%20logic%20in%20Lean./near/135450407):
<p>I sometimes use <code>find . -name "*.olean" -exec touch {} +</code> for this</p>

#### [ Kevin Buzzard (Oct 09 2018 at 15:57)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Basic%20logic%20in%20Lean./near/135471295):
<p>Does this ensure that <code>logic/function.olean</code> has a timestamp which is less than or equal to that of <code>analysis/real.olean</code>?</p>

#### [ Gabriel Ebner (Oct 09 2018 at 16:18)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Basic%20logic%20in%20Lean./near/135472635):
<p>If you run <code>touch a b c d</code>, then <code>touch</code> will assign the same timestamp to all four files.  <code>find -exec touch {} +</code> calls <code>touch</code> a single time with all files as arguments.</p>

#### [ Kevin Buzzard (Oct 09 2018 at 18:22)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Basic%20logic%20in%20Lean./near/135481231):
<p>Oh that's pretty cool. I had just assumed it was running the command on each successful find.</p>


{% endraw %}
