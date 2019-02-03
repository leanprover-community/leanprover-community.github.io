---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/39394leanpkgdoesnotwork.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [leanpkg does not work](https://leanprover-community.github.io/archive/113488general/39394leanpkgdoesnotwork.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Blair Shi (Jul 10 2018 at 20:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/leanpkg%20does%20not%20work/near/129424899):
<p>after git clone Xena-UROP-2018 from GitHub, I want to do <code>leanpkg upgrade</code> but it failed and post many error:</p>
<p><code>/usr/local/leanpkg/leanpkg/main.lean:1:0: error: file 'init' not found in the LEAN_PATH
/usr/local/leanpkg/leanpkg/resolve.lean:1:0: error: file 'init' not found in the LEAN_PATH
/usr/local/leanpkg/leanpkg/manifest.lean:1:0: error: file 'init' not found in the LEAN_PATH
/usr/local/leanpkg/leanpkg/toml.lean:1:0: error: file 'init' not found in the LEAN_PATH </code></p>
<p>I don't know how to do.</p>

#### [ Kevin Buzzard (Jul 10 2018 at 22:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/leanpkg%20does%20not%20work/near/129431669):
<p>Which OS?</p>

#### [ Kevin Buzzard (Jul 10 2018 at 22:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/leanpkg%20does%20not%20work/near/129431724):
<p>Are you using the command line? What's the output of <code>lean --version</code>?</p>

#### [ Blair Shi (Jul 11 2018 at 00:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/leanpkg%20does%20not%20work/near/129437075):
<p>it gives me <code>Lean (version 3.4.1, commit 17fe3decaf8a, Release)</code></p>

#### [ Blair Shi (Jul 11 2018 at 00:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/leanpkg%20does%20not%20work/near/129437080):
<p>I run this on Mac</p>

#### [ Sebastian Ullrich (Jul 11 2018 at 09:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/leanpkg%20does%20not%20work/near/129456013):
<p>How did you install Lean?</p>

#### [ Kevin Buzzard (Jul 11 2018 at 09:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/leanpkg%20does%20not%20work/near/129456073):
<p>If you type <code>leanpkg</code>, what is the first line of the output? I have files with the same names as those which are giving you errors, in my unix install, but there is no mention of <code>init</code>. It's certainly possible to get it all working on a mac.</p>

#### [ Sebastian Ullrich (Jul 11 2018 at 11:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/leanpkg%20does%20not%20work/near/129460129):
<p><span class="user-mention" data-user-id="119876">@Blair Shi</span></p>

#### [ Blair Shi (Jul 11 2018 at 11:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/leanpkg%20does%20not%20work/near/129460708):
<p>Macos high Sierra 10.13.2</p>

#### [ Blair Shi (Jul 11 2018 at 11:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/leanpkg%20does%20not%20work/near/129460895):
<p><span class="user-mention" data-user-id="110038">@Kevin Buzzard</span> </p>
<div class="codehilite"><pre><span></span>dyn3159-100:xena-UROP-2018 shifengzheng$ leanpkg
/usr/local/leanpkg/leanpkg/main.lean:1:0: error: file &#39;init&#39; not found in the LEAN_PATH
</pre></div>

#### [ Blair Shi (Jul 11 2018 at 11:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/leanpkg%20does%20not%20work/near/129460969):
<p><span class="user-mention" data-user-id="110024">@Sebastian Ullrich</span> I just downloaded the package <code>lean-3.4.1</code> and then in my vscode I set <br>
<code>    "lean.executablePath": "/Users/shifengzheng/lean-3.4.1-darwin/bin/lean",</code></p>

#### [ Sebastian Ullrich (Jul 11 2018 at 12:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/leanpkg%20does%20not%20work/near/129462153):
<p><span class="user-mention" data-user-id="119876">@Blair Shi</span> Why do you have files in <code>/usr/local/</code> then? Do you have an old Homebrew installation or something like that?</p>

#### [ Kevin Buzzard (Jul 11 2018 at 12:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/leanpkg%20does%20not%20work/near/129462557):
<p><span class="user-mention" data-user-id="119876">@Blair Shi</span> <span class="user-mention" data-user-id="119876">@Blair Shi</span> (wait -- there are two?) the error shows that the version of <code>leanpkg</code> which is running is <em>not</em> the one in <code>Users/shifengzheng/lean-3.4.1-darwin/bin/</code>, it is some other version installed in <code>usr/local</code>. You might want to completely remove the <code>/usr/local/leanpkg</code> directory and add <code>Users/shifengzheng/lean-3.4.1-darwin/bin/</code> to the path on your command line</p>

#### [ Blair Shi (Jul 11 2018 at 12:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/leanpkg%20does%20not%20work/near/129462558):
<p><span class="user-mention" data-user-id="110024">@Sebastian Ullrich</span>  before I did not have <code>leanpkg</code>in my <code>/usr/local/</code> but when I typed <code>leanpkg</code> in terminal, it reported <code>&lt;unknown&gt;:1:1: error: file '/usr/local/leanpkg/leanpkg/main.lean' not found</code>. So I put leanpkg into my <code>/usr/local/</code></p>

#### [ Kevin Buzzard (Jul 11 2018 at 12:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/leanpkg%20does%20not%20work/near/129462561):
<p>I don't think you can just move <code>leanpkg</code> and hope for things to still work</p>

#### [ Kevin Buzzard (Jul 11 2018 at 12:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/leanpkg%20does%20not%20work/near/129462565):
<p>I think you have to move the entire installation</p>

#### [ Kevin Buzzard (Jul 11 2018 at 12:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/leanpkg%20does%20not%20work/near/129462644):
<p>What I'm saying is that you can move the directory <code>/Users/shifengzheng/lean-3.4.1-darwin</code> to anywhere you like</p>

#### [ Kevin Buzzard (Jul 11 2018 at 12:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/leanpkg%20does%20not%20work/near/129462648):
<p>but you should leave the contents intact.</p>

#### [ Kevin Buzzard (Jul 11 2018 at 12:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/leanpkg%20does%20not%20work/near/129462654):
<p>When you've decided where to put it, point VS Code and your command line PATH to it, and then things should be OK.</p>

#### [ Blair Shi (Jul 11 2018 at 14:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/leanpkg%20does%20not%20work/near/129465999):
<p>I moved <code>lean-3.4.1-darwin</code> to <code>/usr/local/</code> and added path to LEAN_PATH and removed the previous <code>leanpkg</code>in <code>local</code></p>
<div class="codehilite"><pre><span></span>dyn3159-100:xena-UROP-2018 shifengzheng$ echo $LEAN_PATH
/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin:/usr/local/lean-3.4.1-darwin/bin/
</pre></div>


<p>But stil not work. </p>
<div class="codehilite"><pre><span></span>dyn3159-100:xena-UROP-2018 shifengzheng$ leanpkg
&lt;unknown&gt;:1:1: error: file &#39;/usr/local/leanpkg/leanpkg/main.lean&#39; not found
</pre></div>


<p>Did I set the wrong path or did I miss to do something?</p>

#### [ Sebastian Ullrich (Jul 11 2018 at 14:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/leanpkg%20does%20not%20work/near/129466184):
<p>Kevin said to modify <code>PATH</code>, not <code>LEAN_PATH</code>. Please <code>unset LEAN_PATH</code>.</p>

#### [ Sebastian Ullrich (Jul 11 2018 at 14:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/leanpkg%20does%20not%20work/near/129466360):
<p>Could you post the output of <code>which leanpkg</code> and <code>bash -x leanpkg</code>?</p>

#### [ Blair Shi (Jul 11 2018 at 14:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/leanpkg%20does%20not%20work/near/129466476):
<p><span class="user-mention" data-user-id="110024">@Sebastian Ullrich</span>  sorry for my misunderstanding. I <code>unset LEAN_PATH</code> and did what you said</p>
<div class="codehilite"><pre><span></span>dyn3159-100:xena-UROP-2018 shifengzheng$ which leanpkg
/usr/local/bin/leanpkg
dyn3159-100:xena-UROP-2018 shifengzheng$ bash -x leanpkg
++ uname
+ unamestr=Darwin
+ [[ Darwin == \D\a\r\w\i\n ]]
+ command -v greadlink
+ READLINK=greadlink
+++ greadlink -f leanpkg
++ dirname /Users/shifengzheng/xena-UROP-2018/leanpkg
+ leandir=/Users/shifengzheng/xena-UROP-2018/..
++ greadlink -f /Users/shifengzheng/xena-UROP-2018/..
+ leandir=/Users/shifengzheng
+ librarydir=/Users/shifengzheng/lib/lean
+ test -d /Users/shifengzheng/lib/lean
+ librarydir=/Users/shifengzheng
+ LEAN_PATH=/Users/shifengzheng/library:/Users/shifengzheng/leanpkg
+ PATH=/Users/shifengzheng/bin:/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin
+ exec lean --run /Users/shifengzheng/leanpkg/leanpkg/main.lean
&lt;unknown&gt;:1:1: error: file &#39;/Users/shifengzheng/leanpkg/leanpkg/main.lean&#39; not found
</pre></div>

#### [ Sebastian Ullrich (Jul 11 2018 at 14:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/leanpkg%20does%20not%20work/near/129466541):
<p>Apparently you still have an old <code>leanpkg</code> at <code>/usr/local/bin</code></p>

#### [ Kevin Buzzard (Jul 11 2018 at 14:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/leanpkg%20does%20not%20work/near/129466576):
<p>Blair -- I'll be at Imperial in about 10 minutes and will try and sort things out. Sorry it's taken so long -- I had other things to do this morning.</p>

#### [ Blair Shi (Jul 11 2018 at 14:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/leanpkg%20does%20not%20work/near/129466958):
<p>I find a solution to deal with this issue. I just put the <code>Xena-UROP-2018</code> to my <code>my_playground</code> which already set up <code>mathlib</code>. Now it works</p>


{% endraw %}
