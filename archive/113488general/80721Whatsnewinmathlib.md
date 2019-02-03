---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/80721Whatsnewinmathlib.html
---

## Stream: [general](index.html)
### Topic: [What's new in mathlib](80721Whatsnewinmathlib.html)

---


{% raw %}
#### [ Johan Commelin (Oct 02 2018 at 16:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/What%27s%20new%20in%20mathlib/near/135038239):
<p>There is a thread in the <code>#maths</code> stream: <a href="#narrow/stream/116395-maths/subject/What's.20new.20in.20Lean.20maths.3F" title="#narrow/stream/116395-maths/subject/What's.20new.20in.20Lean.20maths.3F">https://leanprover.zulipchat.com/#narrow/stream/116395-maths/subject/What's.20new.20in.20Lean.20maths.3F</a><br>
It is a place to announce recent merges to mathlib that have clear mathematical relevance.</p>

#### [ Johan Commelin (Oct 02 2018 at 16:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/What%27s%20new%20in%20mathlib/near/135038253):
<p>I propose to announce other general contributions in this thread.</p>

#### [ Johan Commelin (Oct 03 2018 at 09:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/What%27s%20new%20in%20mathlib/near/135086366):
<p>There is now a <code>choice</code> tactic that will help with applying the axiom of choice: <a href="https://github.com/leanprover/mathlib/blob/c2df6b1f3f62575649dbe128a2c5fc9e2de26ffb/docs/tactics.md#choice" target="_blank" title="https://github.com/leanprover/mathlib/blob/c2df6b1f3f62575649dbe128a2c5fc9e2de26ffb/docs/tactics.md#choice">https://github.com/leanprover/mathlib/blob/c2df6b1f3f62575649dbe128a2c5fc9e2de26ffb/docs/tactics.md#choice</a><br>
Kudos to <span class="user-mention" data-user-id="110031">@Patrick Massot</span> <span class="emoji emoji-1f389" title="tada">:tada:</span></p>

#### [ Johannes Hölzl (Oct 03 2018 at 11:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/What%27s%20new%20in%20mathlib/near/135091616):
<p>I changed the syntax to</p>
<div class="codehilite"><pre><span></span><span class="n">choose</span> <span class="n">a</span> <span class="n">b</span> <span class="n">h</span> <span class="kn">using</span> <span class="k">show</span> <span class="bp">∀</span> <span class="o">(</span><span class="n">y</span> <span class="o">:</span> <span class="n">Y</span><span class="o">),</span> <span class="bp">∃</span> <span class="o">(</span><span class="n">a</span> <span class="o">:</span> <span class="n">A</span><span class="o">)</span> <span class="o">(</span><span class="n">b</span> <span class="o">:</span> <span class="n">B</span><span class="o">),</span> <span class="n">f</span> <span class="n">a</span> <span class="n">b</span> <span class="bp">=</span> <span class="n">y</span><span class="o">,</span> <span class="bp">...</span>
</pre></div>


<p>Also it allows a arbitrary prefix of quantifiers and existentials.</p>

#### [ Mario Carneiro (Oct 03 2018 at 11:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/What%27s%20new%20in%20mathlib/near/135091695):
<p>Does that include higher than Pi^2 complexity?</p>

#### [ Mario Carneiro (Oct 03 2018 at 11:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/What%27s%20new%20in%20mathlib/near/135091718):
<p>i.e. after the first <code>choose</code> you might end up with a hypothesis that is again of the form AE and repeat</p>

#### [ Mario Carneiro (Oct 03 2018 at 11:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/What%27s%20new%20in%20mathlib/near/135091734):
<p>(I'm not sure how applicable this is, but it would be nice to say we have full skolemization)</p>

#### [ Kevin Buzzard (Oct 03 2018 at 11:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/What%27s%20new%20in%20mathlib/near/135091910):
<p>"Mathlib: aiming for full skolemization". I think this should be our catch phrase.</p>

#### [ Johannes Hölzl (Oct 03 2018 at 11:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/What%27s%20new%20in%20mathlib/near/135092306):
<p>It should handle quantifiers again. But problem is that it doesn't handle conjunctions currently. </p>
<div class="codehilite"><pre><span></span><span class="kn">example</span> <span class="o">(</span><span class="n">h</span> <span class="o">:</span> <span class="bp">∀</span><span class="n">n</span> <span class="n">m</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">,</span> <span class="bp">∃</span><span class="n">i</span><span class="o">,</span> <span class="bp">∀</span><span class="n">n</span><span class="o">:</span><span class="bp">ℕ</span><span class="o">,</span> <span class="bp">∃</span><span class="n">j</span><span class="o">,</span> <span class="n">m</span> <span class="bp">=</span> <span class="n">n</span> <span class="bp">+</span> <span class="n">i</span> <span class="bp">∨</span> <span class="n">m</span> <span class="bp">+</span> <span class="n">j</span> <span class="bp">=</span> <span class="n">n</span><span class="o">)</span> <span class="o">:</span> <span class="n">true</span> <span class="o">:=</span>
<span class="k">begin</span>
  <span class="n">choose</span> <span class="n">i</span> <span class="n">j</span> <span class="n">h</span> <span class="kn">using</span> <span class="n">h</span><span class="o">,</span>
  <span class="n">guard_hyp</span> <span class="n">i</span> <span class="o">:=</span> <span class="bp">ℕ</span> <span class="bp">→</span> <span class="bp">ℕ</span> <span class="bp">→</span> <span class="bp">ℕ</span><span class="o">,</span>
  <span class="n">guard_hyp</span> <span class="n">j</span> <span class="o">:=</span> <span class="bp">ℕ</span> <span class="bp">→</span> <span class="bp">ℕ</span> <span class="bp">→</span> <span class="bp">ℕ</span> <span class="bp">→</span> <span class="bp">ℕ</span><span class="o">,</span>
  <span class="n">guard_hyp</span> <span class="n">h</span> <span class="o">:=</span> <span class="bp">∀</span> <span class="o">(</span><span class="n">n</span> <span class="n">m</span> <span class="n">n_1</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">),</span> <span class="n">m</span> <span class="bp">=</span> <span class="n">n_1</span> <span class="bp">+</span> <span class="n">i</span> <span class="n">n</span> <span class="n">m</span> <span class="bp">∨</span> <span class="n">m</span> <span class="bp">+</span> <span class="n">j</span> <span class="n">n</span> <span class="n">m</span> <span class="n">n_1</span> <span class="bp">=</span> <span class="n">n_1</span><span class="o">,</span>
  <span class="n">trivial</span>
<span class="kn">end</span>
</pre></div>

#### [ Johannes Hölzl (Oct 03 2018 at 11:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/What%27s%20new%20in%20mathlib/near/135092364):
<p>also, since it doesn't use <code>axiom_of_choice</code> but <code>classical.some</code> it can be used in <code>Type</code> and not only in <code>Prop</code>.</p>

#### [ Patrick Massot (Oct 03 2018 at 15:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/What%27s%20new%20in%20mathlib/near/135104186):
<p>Oh, I just noticed <a href="https://github.com/leanprover/mathlib/pull/383#issuecomment-426571007" target="_blank" title="https://github.com/leanprover/mathlib/pull/383#issuecomment-426571007">https://github.com/leanprover/mathlib/pull/383#issuecomment-426571007</a> it means I don't need <code>set_option pp.beta true</code> in my demo file anymore</p>

#### [ Johan Commelin (Oct 04 2018 at 15:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/What%27s%20new%20in%20mathlib/near/135178667):
<p><span class="emoji emoji-1f514" title="bell">:bell:</span> We have a new pair of tactics: <code>tfae_have</code> and <code>tfae_finish</code>. The help with proving "the following are equivalent".<br>
Take a look at <a href="https://github.com/leanprover/mathlib/blob/b7d314f3f2f4b18a491b359aaeb889b5c83640bc/data/list/basic.lean#L3890" target="_blank" title="https://github.com/leanprover/mathlib/blob/b7d314f3f2f4b18a491b359aaeb889b5c83640bc/data/list/basic.lean#L3890">https://github.com/leanprover/mathlib/blob/b7d314f3f2f4b18a491b359aaeb889b5c83640bc/data/list/basic.lean#L3890</a> and at <a href="https://github.com/leanprover/mathlib/blob/b7d314f3f2f4b18a491b359aaeb889b5c83640bc/docs/tactics.md#tfae" target="_blank" title="https://github.com/leanprover/mathlib/blob/b7d314f3f2f4b18a491b359aaeb889b5c83640bc/docs/tactics.md#tfae">https://github.com/leanprover/mathlib/blob/b7d314f3f2f4b18a491b359aaeb889b5c83640bc/docs/tactics.md#tfae</a></p>

#### [ Johan Commelin (Oct 15 2018 at 18:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/What%27s%20new%20in%20mathlib/near/135843553):
<p>There have been valiant efforts by the community to improve the installation experience: <a href="https://github.com/leanprover/mathlib/commit/4dbe0cdfaee201cc15cd2a74fbe8731f8bd4642a" target="_blank" title="https://github.com/leanprover/mathlib/commit/4dbe0cdfaee201cc15cd2a74fbe8731f8bd4642a">https://github.com/leanprover/mathlib/commit/4dbe0cdfaee201cc15cd2a74fbe8731f8bd4642a</a></p>

#### [ Johan Commelin (Oct 15 2018 at 18:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/What%27s%20new%20in%20mathlib/near/135843730):
<p>In this context I think it is worth pointing once more to Kevin's page: <a href="https://xenaproject.wordpress.com/installing-lean-and-mathlib/" target="_blank" title="https://xenaproject.wordpress.com/installing-lean-and-mathlib/">https://xenaproject.wordpress.com/installing-lean-and-mathlib/</a> which also links to two fantastic installation walkthrough videos by Scott.</p>

#### [ Scott Morrison (Nov 01 2018 at 10:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/What%27s%20new%20in%20mathlib/near/136909599):
<p>New in Lean itself: the patches to deal with spaces in Windows user names have landed, <a href="https://github.com/leanprover/lean-nightly/releases" target="_blank" title="https://github.com/leanprover/lean-nightly/releases">https://github.com/leanprover/lean-nightly/releases</a>.</p>

#### [ Scott Morrison (Nov 01 2018 at 10:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/What%27s%20new%20in%20mathlib/near/136909612):
<p>In mathlib, my <code>fin_cases</code> tactic was merged. Sorry I haven't been paying attention to mathlib much recently; perhaps someone else can give some updates on recent merges?</p>

#### [ Kenny Lau (Nov 01 2018 at 10:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/What%27s%20new%20in%20mathlib/near/136909834):
<div class="codehilite"><pre><span></span>cd /c/lean
git pull
cd build/release
ninja clean-olean
ninja
</pre></div>


<p>:P</p>

#### [ Scott Morrison (Nov 01 2018 at 10:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/What%27s%20new%20in%20mathlib/near/136909849):
<p>?</p>

#### [ Kenny Lau (Nov 01 2018 at 10:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/What%27s%20new%20in%20mathlib/near/136909865):
<p>that's how to manually update lean</p>

#### [ Keeley Hoek (Nov 01 2018 at 10:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/What%27s%20new%20in%20mathlib/near/136909925):
<p>but kenny, this means you are yet to bask in the glorious <code>elan</code> way</p>

#### [ Keeley Hoek (Nov 01 2018 at 10:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/What%27s%20new%20in%20mathlib/near/136909927):
<p>:D</p>

#### [ Kenny Lau (Nov 01 2018 at 10:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/What%27s%20new%20in%20mathlib/near/136909973):
<p>maybe <code>elan</code> is yet to work for windows</p>

#### [ Keeley Hoek (Nov 01 2018 at 10:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/What%27s%20new%20in%20mathlib/near/136909976):
<p>nah it even has a windows binary and everything!</p>

#### [ Keeley Hoek (Nov 01 2018 at 10:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/What%27s%20new%20in%20mathlib/near/136910034):
<p>there is even scope for like a windows installer, but someone will have to be bothered to repair it</p>

#### [ Kenny Lau (Nov 01 2018 at 10:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/What%27s%20new%20in%20mathlib/near/136910643):
<div class="codehilite"><pre><span></span>[...]
Current installation options:

     default toolchain: stable
  modify PATH variable: yes

1) Proceed with installation (default)
2) Customize installation
3) Cancel installation


error: toolchain &#39;stable&#39; is not installed
info: caused by: not a directory: &#39;C:\Users\Kenny Lau\.elan\toolchains\stable&#39;

Press the Enter key to continue.
</pre></div>

#### [ Keeley Hoek (Nov 01 2018 at 10:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/What%27s%20new%20in%20mathlib/near/136910681):
<p>I think the old space in the name strikes again</p>

#### [ Kenny Lau (Nov 01 2018 at 10:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/What%27s%20new%20in%20mathlib/near/136910816):
<p>I think the correct name is <code>stable-x86_64-pc-windows-msvc</code> not <code>stable</code></p>

#### [ Keeley Hoek (Nov 01 2018 at 10:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/What%27s%20new%20in%20mathlib/near/136911316):
<p>Is that because there was a folder created in <code>...\toolchains\</code> which is called that? How did you get that name?<br>
My understanding of the <code>elan</code> toolchain code is that <code>stable</code> is a special keyword, along with <code>nightly</code>. In my testing I tend to get the error <code>
error: toolchain 'stable' is not installed</code> when <code>elan</code> is failing silently because of something.<br>
I suppose I should stop talking about this in this thread... :o</p>

#### [ Reid Barton (Nov 05 2018 at 15:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/What%27s%20new%20in%20mathlib/near/146800725):
<p>Gonna be a lot of stuff this week.</p>

#### [ Kenny Lau (Nov 05 2018 at 16:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/What%27s%20new%20in%20mathlib/near/146801829):
<p>oh man</p>

#### [ Johan Commelin (Nov 05 2018 at 20:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/What%27s%20new%20in%20mathlib/near/146817419):
<p>Keeley's PR's for extending <code>conv</code> mode with <code>ring</code> and <code>erw</code> have been merged.</p>

#### [ Keeley Hoek (Nov 06 2018 at 03:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/What%27s%20new%20in%20mathlib/near/146840826):
<p>Woah, the pull-request list fits onto one page now!</p>

#### [ Kenny Lau (Nov 06 2018 at 21:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/What%27s%20new%20in%20mathlib/near/146891337):
<p><a href="https://math.stackexchange.com/q/2987631/328173" target="_blank" title="https://math.stackexchange.com/q/2987631/328173">https://math.stackexchange.com/q/2987631/328173</a></p>

#### [ Johan Commelin (Dec 17 2018 at 18:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/What%27s%20new%20in%20mathlib/near/152046738):
<p>We just got <code>elide</code>: <a href="https://github.com/leanprover/mathlib/blob/ebf3008ba84fec5363334fa77a947f43bd71a965/docs/tactics.md#elideunelide" target="_blank" title="https://github.com/leanprover/mathlib/blob/ebf3008ba84fec5363334fa77a947f43bd71a965/docs/tactics.md#elideunelide">https://github.com/leanprover/mathlib/blob/ebf3008ba84fec5363334fa77a947f43bd71a965/docs/tactics.md#elideunelide</a><br>
Thanks Mario!</p>

#### [ Kenny Lau (Dec 17 2018 at 19:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/What%27s%20new%20in%20mathlib/near/152047300):
<p>interesting...</p>

#### [ Johan Commelin (Dec 20 2018 at 09:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/What%27s%20new%20in%20mathlib/near/152242473):
<p><a href="https://github.com/leanprover/mathlib/issues/489" target="_blank" title="https://github.com/leanprover/mathlib/issues/489">#489</a> is merged. This adds a new command <code>#where</code>. Kudos to <span class="user-mention" data-user-id="110111">@Keeley Hoek</span> <span class="emoji emoji-1f389" title="tada">:tada:</span> <br>
If you insert <code>#where</code> in a file, Lean will print a message explaining what your current namespace is, and which variables are in use.</p>

#### [ Keeley Hoek (Dec 20 2018 at 09:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/What%27s%20new%20in%20mathlib/near/152242572):
<p>Mario needs a medal (or at least a high-five) for the insane response time after I fixed up his suggestions</p>

#### [ Johan Commelin (Dec 22 2018 at 18:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/What%27s%20new%20in%20mathlib/near/152396140):
<p>34 merged PRs in the past week!<br>
<a href="https://github.com/leanprover/mathlib/pulse" target="_blank" title="https://github.com/leanprover/mathlib/pulse">https://github.com/leanprover/mathlib/pulse</a></p>

#### [ Mario Carneiro (Dec 22 2018 at 18:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/What%27s%20new%20in%20mathlib/near/152396214):
<p>and I'm sure there are more open PRs now than when I started :P</p>

#### [ Kevin Buzzard (Dec 22 2018 at 18:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/What%27s%20new%20in%20mathlib/near/152396943):
<p><a href="https://xkcd.com/2086/" target="_blank" title="https://xkcd.com/2086/">https://xkcd.com/2086/</a></p>

#### [ Patrick Massot (Dec 22 2018 at 19:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/What%27s%20new%20in%20mathlib/near/152397916):
<blockquote>
<p>and I'm sure there are more open PRs now than when I started :P</p>
</blockquote>
<p>You did ask for many small PR everywhere there could be one big...</p>

#### [ Reid Barton (Dec 22 2018 at 19:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/What%27s%20new%20in%20mathlib/near/152398095):
<p>I think most of the remaining PRs are fairly large though</p>

#### [ Patrick Massot (Jan 27 2019 at 12:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/What%27s%20new%20in%20mathlib/near/156968908):
<p>Simon wrote a bunch of long expected hole commands <a href="https://github.com/leanprover/mathlib/commit/84d1c450111d4c576c7aefd3a7901c4aa07d0b6f" target="_blank" title="https://github.com/leanprover/mathlib/commit/84d1c450111d4c576c7aefd3a7901c4aa07d0b6f">https://github.com/leanprover/mathlib/commit/84d1c450111d4c576c7aefd3a7901c4aa07d0b6f</a>!</p>

#### [ Sebastian Ullrich (Jan 27 2019 at 12:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/What%27s%20new%20in%20mathlib/near/156968928):
<p>Nice</p>

#### [ Simon Hudon (Jan 27 2019 at 18:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/What%27s%20new%20in%20mathlib/near/156979900):
<p>I hope you guys enjoy it! There's a lot of room for improvement. Please let me know what the pain points are.</p>


{% endraw %}
