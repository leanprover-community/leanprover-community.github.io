---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/36764failingtousesearchinVSCode.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [failing to use search in VS Code](https://leanprover-community.github.io/archive/113488general/36764failingtousesearchinVSCode.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Kevin Buzzard (May 03 2018 at 12:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/failing%20to%20use%20search%20in%20VS%20Code/near/126038688):
<p>I don't know how to search properly in VS Code. I am just doing something really stupid. I'm writing a new file, I have no imports at all, I type <code>[group G]</code> and it works, I type <code>[is_group_hom f]</code> and it doesn't. I know that <code>is_group_hom</code> is there somewhere. Here's my workflow:</p>

#### [ Kevin Buzzard (May 03 2018 at 12:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/failing%20to%20use%20search%20in%20VS%20Code/near/126038745):
<p>1) I click on the magnifying class in VS Code (with a project open which has mathlib as an import) and I search for <code>is_group_hom</code>. The only results I get are the instance in the file I just wrote, and two other instances in the <em>comments</em> in a file I'm not interested in (so in particular I can't go to this other piece of code and right click on is_group_hom)</p>

#### [ Kevin Buzzard (May 03 2018 at 12:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/failing%20to%20use%20search%20in%20VS%20Code/near/126038749):
<p>2) Think "I am rubbish at using VS Code search"</p>

#### [ Kevin Buzzard (May 03 2018 at 12:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/failing%20to%20use%20search%20in%20VS%20Code/near/126038752):
<p>3) grep the source code and find it in seconds.</p>

#### [ Kevin Buzzard (May 03 2018 at 12:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/failing%20to%20use%20search%20in%20VS%20Code/near/126038757):
<p>in mathlib in <code>algebra.group</code>. What am I doing wrong?</p>

#### [ Kenny Lau (May 03 2018 at 12:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/failing%20to%20use%20search%20in%20VS%20Code/near/126038770):
<p><a href="/user_uploads/3121/JTu5apknT8ioLvVRLi6qQHM4/2018-05-03-2.png" target="_blank" title="2018-05-03-2.png">2018-05-03-2.png</a></p>
<div class="message_inline_image"><a href="/user_uploads/3121/JTu5apknT8ioLvVRLi6qQHM4/2018-05-03-2.png" target="_blank" title="2018-05-03-2.png"><img src="/user_uploads/3121/JTu5apknT8ioLvVRLi6qQHM4/2018-05-03-2.png"></a></div>

#### [ Kevin Buzzard (May 03 2018 at 12:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/failing%20to%20use%20search%20in%20VS%20Code/near/126038814):
<p>How do I tell my VS Code to look where yours is looking</p>

#### [ Kenny Lau (May 03 2018 at 12:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/failing%20to%20use%20search%20in%20VS%20Code/near/126038817):
<p>what does the search result look like for you?</p>

#### [ Kevin Buzzard (May 03 2018 at 12:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/failing%20to%20use%20search%20in%20VS%20Code/near/126038827):
<p><a href="/user_uploads/3121/o4I8ufTMQcIiUYh1cfZQfjoA/is_group_hom.png" target="_blank" title="is_group_hom.png">is_group_hom.png</a></p>
<div class="message_inline_image"><a href="/user_uploads/3121/o4I8ufTMQcIiUYh1cfZQfjoA/is_group_hom.png" target="_blank" title="is_group_hom.png"><img src="/user_uploads/3121/o4I8ufTMQcIiUYh1cfZQfjoA/is_group_hom.png"></a></div>

#### [ Chris Hughes (May 03 2018 at 12:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/failing%20to%20use%20search%20in%20VS%20Code/near/126038849):
<p>Do you have mathlib open as a folder?</p>

#### [ Kenny Lau (May 03 2018 at 12:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/failing%20to%20use%20search%20in%20VS%20Code/near/126038877):
<p>ctrl+shift+e</p>

#### [ Kenny Lau (May 03 2018 at 12:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/failing%20to%20use%20search%20in%20VS%20Code/near/126038882):
<p>and screenshot</p>

#### [ Kenny Lau (May 03 2018 at 12:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/failing%20to%20use%20search%20in%20VS%20Code/near/126038885):
<p><a href="/user_uploads/3121/2TiT6Be0I94H7YWV1WFKWBlZ/2018-05-03-3.png" target="_blank" title="2018-05-03-3.png">2018-05-03-3.png</a></p>
<div class="message_inline_image"><a href="/user_uploads/3121/2TiT6Be0I94H7YWV1WFKWBlZ/2018-05-03-3.png" target="_blank" title="2018-05-03-3.png"><img src="/user_uploads/3121/2TiT6Be0I94H7YWV1WFKWBlZ/2018-05-03-3.png"></a></div>

#### [ Sebastian Ullrich (May 03 2018 at 12:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/failing%20to%20use%20search%20in%20VS%20Code/near/126038889):
<p>"Also note the Use Exclude Settings and Ignore Files toggle button in the files to exclude box. The toggle determines whether to exclude files that are ignored by your .gitignore files [...]"<br>
<code>_target</code> is in <code>.gitignore</code></p>

#### [ Kevin Buzzard (May 03 2018 at 12:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/failing%20to%20use%20search%20in%20VS%20Code/near/126038902):
<p><a href="/user_uploads/3121/h7riDfVuoldfp6pyviUn20Io/open_stuff.png" target="_blank" title="open_stuff.png">open_stuff.png</a></p>
<div class="message_inline_image"><a href="/user_uploads/3121/h7riDfVuoldfp6pyviUn20Io/open_stuff.png" target="_blank" title="open_stuff.png"><img src="/user_uploads/3121/h7riDfVuoldfp6pyviUn20Io/open_stuff.png"></a></div>

#### [ Sebastian Ullrich (May 03 2018 at 12:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/failing%20to%20use%20search%20in%20VS%20Code/near/126038903):
<p><a href="https://code.visualstudio.com/docs/editor/codebasics#_search-across-files" target="_blank" title="https://code.visualstudio.com/docs/editor/codebasics#_search-across-files">https://code.visualstudio.com/docs/editor/codebasics#_search-across-files</a></p>

#### [ Kenny Lau (May 03 2018 at 12:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/failing%20to%20use%20search%20in%20VS%20Code/near/126038943):
<p><span class="user-mention" data-user-id="110038">@Kevin Buzzard</span> could you contract all your workspace folders</p>

#### [ Kenny Lau (May 03 2018 at 12:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/failing%20to%20use%20search%20in%20VS%20Code/near/126038945):
<p>and see if mathlib is open</p>

#### [ Kenny Lau (May 03 2018 at 12:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/failing%20to%20use%20search%20in%20VS%20Code/near/126038946):
<p>if not, drag mathlib into your workspace as the bottom folder and things should work fine</p>

#### [ Kevin Buzzard (May 03 2018 at 12:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/failing%20to%20use%20search%20in%20VS%20Code/near/126038947):
<p>I have <code>_target</code> and mathlib is in there I promise</p>

#### [ Kevin Buzzard (May 03 2018 at 12:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/failing%20to%20use%20search%20in%20VS%20Code/near/126038953):
<p>I don't understand the advanced options for file include/exclude: it just says "files to include/exclude" and then lets me type in a list of files without explaining how to ensure they are either included or excluded</p>

#### [ Kenny Lau (May 03 2018 at 12:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/failing%20to%20use%20search%20in%20VS%20Code/near/126038956):
<p>hmm</p>

#### [ Kevin Buzzard (May 03 2018 at 12:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/failing%20to%20use%20search%20in%20VS%20Code/near/126038996):
<p>So I've not needed to play with included/excluded</p>

#### [ Kevin Buzzard (May 03 2018 at 12:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/failing%20to%20use%20search%20in%20VS%20Code/near/126038997):
<p>I have just randomly clicked around and opened some directories in the ctrl-shift-E view</p>

#### [ Kevin Buzzard (May 03 2018 at 12:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/failing%20to%20use%20search%20in%20VS%20Code/near/126038998):
<p>and now it works</p>

#### [ Kenny Lau (May 03 2018 at 12:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/failing%20to%20use%20search%20in%20VS%20Code/near/126038999):
<p>what?</p>

#### [ Kevin Buzzard (May 03 2018 at 12:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/failing%20to%20use%20search%20in%20VS%20Code/near/126039007):
<p>now everything is closed and it works</p>

#### [ Kevin Buzzard (May 03 2018 at 12:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/failing%20to%20use%20search%20in%20VS%20Code/near/126039008):
<p>It is completely hit-and-miss for me</p>

#### [ Chris Hughes (May 03 2018 at 12:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/failing%20to%20use%20search%20in%20VS%20Code/near/126039009):
<p>!scratch.lean excludes the file scratch.lean includes it</p>

#### [ Kenny Lau (May 03 2018 at 12:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/failing%20to%20use%20search%20in%20VS%20Code/near/126039010):
<p>this is very interesting</p>

#### [ Kevin Buzzard (May 03 2018 at 12:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/failing%20to%20use%20search%20in%20VS%20Code/near/126039013):
<p>I now have what looks to me like exactly the same set-up, with no obvious parameters having been changed, and search works find</p>

#### [ Kevin Buzzard (May 03 2018 at 12:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/failing%20to%20use%20search%20in%20VS%20Code/near/126039014):
<p>fine</p>

#### [ Kevin Buzzard (May 03 2018 at 12:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/failing%20to%20use%20search%20in%20VS%20Code/near/126039053):
<p>There is some basic thing which I am constantly running into and not spotting.</p>

#### [ Sebastian Ullrich (May 03 2018 at 12:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/failing%20to%20use%20search%20in%20VS%20Code/near/126039056):
<p>"Also note the Use Exclude Settings and Ignore Files <strong>toggle button</strong> in the files to exclude box." :)</p>

#### [ Kevin Buzzard (May 03 2018 at 12:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/failing%20to%20use%20search%20in%20VS%20Code/near/126039103):
<p>IT'S THE TOGGLE BUTTON</p>

#### [ Kenny Lau (May 03 2018 at 12:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/failing%20to%20use%20search%20in%20VS%20Code/near/126039106):
<p>lmao</p>

#### [ Kevin Buzzard (May 03 2018 at 12:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/failing%20to%20use%20search%20in%20VS%20Code/near/126039107):
<p>I can search!</p>

#### [ Kevin Buzzard (May 03 2018 at 12:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/failing%20to%20use%20search%20in%20VS%20Code/near/126039110):
<p>I thought that was a settings button opening an empty menu. I hadn't noticed it was changing colour</p>

#### [ Kevin Buzzard (May 03 2018 at 12:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/failing%20to%20use%20search%20in%20VS%20Code/near/126039116):
<p>the nightmare is over</p>

#### [ Kevin Buzzard (May 03 2018 at 12:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/failing%20to%20use%20search%20in%20VS%20Code/near/126039117):
<p>Thanks both of you :-)</p>

#### [ Kevin Buzzard (May 03 2018 at 12:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/failing%20to%20use%20search%20in%20VS%20Code/near/126039183):
<p>I need to start wearing my glasses when I'm doing this stuff :-/</p>

#### [ Kevin Buzzard (May 03 2018 at 12:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/failing%20to%20use%20search%20in%20VS%20Code/near/126039223):
<p>I didn't even see the <code>!</code> in the greyed out text. Thanks Chris.</p>

#### [ Kevin Buzzard (May 03 2018 at 12:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/failing%20to%20use%20search%20in%20VS%20Code/near/126039431):
<p>And here's another thing I fail at. If I open <code>algebra/group.lean</code> in mathlib</p>

#### [ Kevin Buzzard (May 03 2018 at 12:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/failing%20to%20use%20search%20in%20VS%20Code/near/126039441):
<p>I see on line 497 that there's a theorem called <code>mul</code></p>

#### [ Kevin Buzzard (May 03 2018 at 12:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/failing%20to%20use%20search%20in%20VS%20Code/near/126039446):
<p>but that <code>mul</code> won't be in the root namespace, I'm pretty sure. How do I find out the full name of that function?</p>

#### [ Kevin Buzzard (May 03 2018 at 12:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/failing%20to%20use%20search%20in%20VS%20Code/near/126039449):
<p>The problem is that I might be in a namespace</p>

#### [ Kevin Buzzard (May 03 2018 at 12:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/failing%20to%20use%20search%20in%20VS%20Code/near/126039452):
<p>What I do currently is I simply edit <code>algebra/group.lean</code></p>

#### [ Kenny Lau (May 03 2018 at 12:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/failing%20to%20use%20search%20in%20VS%20Code/near/126039453):
<p>search for <code>namespace</code> on the file lol</p>

#### [ Kevin Buzzard (May 03 2018 at 12:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/failing%20to%20use%20search%20in%20VS%20Code/near/126039456):
<p>which is something I don't really like doing</p>

#### [ Kevin Buzzard (May 03 2018 at 12:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/failing%20to%20use%20search%20in%20VS%20Code/near/126039459):
<p>I don't want to start searching</p>

#### [ Kevin Buzzard (May 03 2018 at 12:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/failing%20to%20use%20search%20in%20VS%20Code/near/126039460):
<p>I just want to know the answer</p>

#### [ Kevin Buzzard (May 03 2018 at 12:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/failing%20to%20use%20search%20in%20VS%20Code/near/126039461):
<p>say the file uses 10 namespaces, some within others</p>

#### [ Kevin Buzzard (May 03 2018 at 12:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/failing%20to%20use%20search%20in%20VS%20Code/near/126039463):
<p>I have to check all their names and when they're closed</p>

#### [ Kevin Buzzard (May 03 2018 at 12:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/failing%20to%20use%20search%20in%20VS%20Code/near/126039465):
<p>I might have to move around a large file</p>

#### [ Kevin Buzzard (May 03 2018 at 12:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/failing%20to%20use%20search%20in%20VS%20Code/near/126039466):
<p>What I currently do is under the definition of <code>mul</code> in the file I just write <code>#print mul</code></p>

#### [ Kevin Buzzard (May 03 2018 at 12:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/failing%20to%20use%20search%20in%20VS%20Code/near/126039504):
<p>This gives me the prefix</p>

#### [ Kevin Buzzard (May 03 2018 at 12:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/failing%20to%20use%20search%20in%20VS%20Code/near/126039507):
<p>then I ctrl-Z to get rid of my edits</p>

#### [ Kevin Buzzard (May 03 2018 at 12:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/failing%20to%20use%20search%20in%20VS%20Code/near/126039508):
<p>It strikes me as an amateurish approach</p>

#### [ Kenny Lau (May 03 2018 at 12:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/failing%20to%20use%20search%20in%20VS%20Code/near/126039510):
<p><span class="user-mention" data-user-id="110024">@Sebastian Ullrich</span></p>

#### [ Kevin Buzzard (May 03 2018 at 12:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/failing%20to%20use%20search%20in%20VS%20Code/near/126039511):
<p>but mouse hover over mul doesn't do anything</p>

#### [ Kevin Buzzard (May 03 2018 at 12:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/failing%20to%20use%20search%20in%20VS%20Code/near/126039512):
<p>and right click on mul doesn't work</p>

#### [ Kevin Buzzard (May 03 2018 at 12:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/failing%20to%20use%20search%20in%20VS%20Code/near/126039516):
<p>"no definition found for mul"</p>

#### [ Kenny Lau (May 03 2018 at 12:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/failing%20to%20use%20search%20in%20VS%20Code/near/126039521):
<p>I mean, I'll just import that file in a sandbox and type <code>#check mul</code> and ctrl+space</p>

#### [ Kenny Lau (May 03 2018 at 12:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/failing%20to%20use%20search%20in%20VS%20Code/near/126039523):
<p>ctrl+space works quite well</p>

#### [ Kevin Buzzard (May 03 2018 at 12:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/failing%20to%20use%20search%20in%20VS%20Code/near/126039524):
<p>My method has the advantage that I never lose sight of the theorem I want</p>

#### [ Kevin Buzzard (May 03 2018 at 12:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/failing%20to%20use%20search%20in%20VS%20Code/near/126039529):
<p>aah that's an idea which will probably work well in many situations</p>

#### [ Sebastian Ullrich (May 03 2018 at 12:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/failing%20to%20use%20search%20in%20VS%20Code/near/126039573):
<p>You're right, it would make sense if the definition had the same mouseover as its references</p>

#### [ Reid Barton (May 03 2018 at 16:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/failing%20to%20use%20search%20in%20VS%20Code/near/126048674):
<p>I use emacs, but this is something I've wished for too: the ability to see at a keystroke</p>
<ul>
<li>which namespaces the current location is inside</li>
<li>what variables/parameters are in scope at the current location</li>
</ul>

#### [ Reid Barton (May 03 2018 at 16:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/failing%20to%20use%20search%20in%20VS%20Code/near/126048677):
<p>I don't know if this can be implemented without extending lean</p>


{% endraw %}
