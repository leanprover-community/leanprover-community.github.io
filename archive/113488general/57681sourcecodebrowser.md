---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/57681sourcecodebrowser.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [source code browser](https://leanprover-community.github.io/archive/113488general/57681sourcecodebrowser.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Johan Commelin (Sep 03 2018 at 09:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/source%20code%20browser/near/133246061):
<p>Is there some way to easily turn a repo of Lean files into a hyperlinked bunch of HTML files? If we want to showcase some code to mathematicians, we should take into account that they have never heard of git or github before. Also, on github you can't click on an imported file, or a token, to go somewhere else. And we can't expect people who want to read some source files to install VScode before they are able to really use it.</p>

#### [ Johan Commelin (Sep 03 2018 at 09:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/source%20code%20browser/near/133246070):
<p>So basically, I would like a read-only VScode that can easily be hosted somewhere. Just a bunch of static files.</p>

#### [ Kenny Lau (Sep 03 2018 at 09:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/source%20code%20browser/near/133246129):
<p>I mean, for other languages (like Java) the corresponding website is grepcode</p>

#### [ Kenny Lau (Sep 03 2018 at 09:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/source%20code%20browser/near/133246132):
<p>so I don't think things like this is very common</p>

#### [ Soham Chowdhury (Sep 03 2018 at 09:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/source%20code%20browser/near/133246315):
<p>I think what <span class="user-mention" data-user-id="112680">@Johan Commelin</span> has in mind is closer to Javadoc, Haddock, or <code>agda --html</code>.</p>

#### [ Mario Carneiro (Sep 03 2018 at 09:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/source%20code%20browser/near/133246374):
<p>this has been a dream for some time</p>

#### [ Mario Carneiro (Sep 03 2018 at 09:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/source%20code%20browser/near/133246379):
<p>My <code>#explode</code> command was actually working toward that goal</p>

#### [ Johan Commelin (Sep 03 2018 at 09:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/source%20code%20browser/near/133246384):
<p>So, why is it easy in VScode?</p>

#### [ Mario Carneiro (Sep 03 2018 at 09:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/source%20code%20browser/near/133246386):
<p>Currently it's a bit tough to get good data on what exists in a file</p>

#### [ Johan Commelin (Sep 03 2018 at 09:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/source%20code%20browser/near/133246428):
<p>If VScode can figure out where to take me, if I <code>Ctrl-click</code> on something, can't it export a bunch of html files?</p>

#### [ Mario Carneiro (Sep 03 2018 at 09:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/source%20code%20browser/near/133246443):
<p>Actually what you are describing sounds a bit different - the plan has been to show some abbreviated or expandable or indexed form of the file to make browsing easier</p>

#### [ Johan Commelin (Sep 03 2018 at 09:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/source%20code%20browser/near/133246446):
<p>Ok, I guess that is harder.</p>

#### [ Johan Commelin (Sep 03 2018 at 09:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/source%20code%20browser/near/133246487):
<p>I just figure that if Kevin publishes a paper, then he want to include a URL with a static view of his files that is easy to navigate.</p>

#### [ Johan Commelin (Sep 03 2018 at 09:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/source%20code%20browser/near/133246490):
<p>GitHub isn't good enough.</p>

#### [ Soham Chowdhury (Sep 03 2018 at 09:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/source%20code%20browser/near/133246495):
<p>It should be possible to dump source code into plain HTML files and then modify or hook into <code>vscode-lean</code> (I think) to use its symbol table to turn identifiers into links.</p>

#### [ Mario Carneiro (Sep 03 2018 at 09:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/source%20code%20browser/near/133246496):
<p>I think Mizar has a pretty similar display to what you are suggesting, Coq too to some degree</p>

#### [ Mario Carneiro (Sep 03 2018 at 09:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/source%20code%20browser/near/133246513):
<p>See, for example: <a href="http://www.mizar.org/version/current/html/polynom5.html#T74" target="_blank" title="http://www.mizar.org/version/current/html/polynom5.html#T74">http://www.mizar.org/version/current/html/polynom5.html#T74</a></p>

#### [ Soham Chowdhury (Sep 03 2018 at 09:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/source%20code%20browser/near/133246515):
<p><a href="https://agda.github.io/agda-stdlib/README.html" target="_blank" title="https://agda.github.io/agda-stdlib/README.html">https://agda.github.io/agda-stdlib/README.html</a><br>
Just to be clear, <span class="user-mention" data-user-id="112680">@Johan Commelin</span>, does this look like what you want?</p>

#### [ Soham Chowdhury (Sep 03 2018 at 09:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/source%20code%20browser/near/133246555):
<p>Yeah, or that</p>

#### [ Johan Commelin (Sep 03 2018 at 09:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/source%20code%20browser/near/133246571):
<p>Right, those are both good examples.</p>

#### [ Johan Commelin (Sep 03 2018 at 09:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/source%20code%20browser/near/133246579):
<p>Althought the Agda one only has a bunch of comments and imports...</p>

#### [ Soham Chowdhury (Sep 03 2018 at 09:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/source%20code%20browser/near/133246587):
<p>You can click on the imports to get to more interesting files.</p>

#### [ Soham Chowdhury (Sep 03 2018 at 09:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/source%20code%20browser/near/133246588):
<p>Like this: <a href="https://agda.github.io/agda-stdlib/Category.Monad.html" target="_blank" title="https://agda.github.io/agda-stdlib/Category.Monad.html">https://agda.github.io/agda-stdlib/Category.Monad.html</a></p>

#### [ Johan Commelin (Sep 03 2018 at 10:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/source%20code%20browser/near/133246652):
<p>I have very little fu in this regard. But it seems to me that it shouldn't be too hard to hack such a thing together, right?</p>

#### [ Mario Carneiro (Sep 03 2018 at 10:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/source%20code%20browser/near/133246677):
<p>I really hope there is a more effective way to locate tokens than asking lean at each position what token is at that location (and where is it defined)</p>

#### [ Mario Carneiro (Sep 03 2018 at 10:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/source%20code%20browser/near/133246719):
<p>otherwise this could take a really long time</p>

#### [ Johan Commelin (Sep 03 2018 at 10:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/source%20code%20browser/near/133246735):
<p>Not longer then <code>lean --make</code>, right?</p>

#### [ Johan Commelin (Sep 03 2018 at 10:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/source%20code%20browser/near/133246736):
<p>And this is something that you'll run only occasionaly.</p>

#### [ Johan Commelin (Sep 03 2018 at 10:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/source%20code%20browser/near/133246744):
<p>So I really don't care about runtime.</p>

#### [ Mario Carneiro (Sep 03 2018 at 10:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/source%20code%20browser/near/133246745):
<p>yes longer than lean --make</p>

#### [ Johan Commelin (Sep 03 2018 at 10:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/source%20code%20browser/near/133246750):
<p>Ooh, hmmm</p>

#### [ Mario Carneiro (Sep 03 2018 at 10:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/source%20code%20browser/near/133246755):
<p>I'm talking about asking lean at each character what is there, basically the software version of clicking everywhere to see what happens</p>

#### [ Johan Commelin (Sep 03 2018 at 10:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/source%20code%20browser/near/133246804):
<p>But Lean stores this data already, right? We saw it sitting somewhere in some <code>expr</code>.</p>

#### [ Johan Commelin (Sep 03 2018 at 10:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/source%20code%20browser/near/133246815):
<p>How does VScode figure this out? Only at runtime, when I click somewhere?</p>

#### [ Mario Carneiro (Sep 03 2018 at 10:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/source%20code%20browser/near/133246818):
<p>Through the lean server API</p>

#### [ Mario Carneiro (Sep 03 2018 at 10:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/source%20code%20browser/near/133246830):
<p>you click, VSCode sends lean a message asking "what is here", lean responds</p>

#### [ Johan Commelin (Sep 03 2018 at 10:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/source%20code%20browser/near/133246833):
<p>I see. And that is going to be slow.</p>

#### [ Mario Carneiro (Sep 03 2018 at 10:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/source%20code%20browser/near/133246841):
<p>if that is the only message you can send, then we are in trouble, but maybe there is a saner data structure being sent</p>

#### [ Soham Chowdhury (Sep 03 2018 at 10:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/source%20code%20browser/near/133246843):
<p>Hm, isn't there a lexer/parser/AST-generator for Lean that we can hook into?</p>

#### [ Mario Carneiro (Sep 03 2018 at 10:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/source%20code%20browser/near/133246844):
<p>see lean 4</p>

#### [ Mario Carneiro (Sep 03 2018 at 10:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/source%20code%20browser/near/133246890):
<p>this is why many of the leandoc plans are waiting on lean 4</p>

#### [ Johan Commelin (Sep 03 2018 at 10:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/source%20code%20browser/near/133246918):
<p>/me proposes <span class="emoji emoji-1f340" title="four leaf clover">:four_leaf_clover:</span> as the default emoji for marking dreams and wishes that will be trivially realizable when Lean 4 emerges <span class="emoji emoji-1f61c" title="stuck out tongue wink">:stuck_out_tongue_wink:</span></p>

#### [ Mario Carneiro (Sep 03 2018 at 10:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/source%20code%20browser/near/133246924):
<p>maybe we should make a list</p>

#### [ Johan Commelin (Sep 03 2018 at 10:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/source%20code%20browser/near/133246973):
<p>Voila: <a href="#narrow/search/.22lean.204.22" title="#narrow/search/.22lean.204.22">https://leanprover.zulipchat.com/#narrow/search/.22lean.204.22</a></p>

#### [ Johannes Hölzl (Sep 03 2018 at 10:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/source%20code%20browser/near/133248804):
<p>Apropos Lean 4: Leo gave a new talk at Galois inc. You find the slides on <a href="http://leanprover.github.io" target="_blank" title="http://leanprover.github.io">leanprover.github.io</a>: <a href="http://leanprover.github.io/talks/LeanAtGalois.pdf" target="_blank" title="http://leanprover.github.io/talks/LeanAtGalois.pdf">http://leanprover.github.io/talks/LeanAtGalois.pdf</a> Some new information about Lean4!</p>

#### [ Johannes Hölzl (Sep 03 2018 at 10:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/source%20code%20browser/near/133248820):
<p>local constants are now called free variables :)</p>

#### [ Patrick Massot (Sep 03 2018 at 10:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/source%20code%20browser/near/133248821):
<p>My <a href="https://github.com/leanprover-community/leancrawler" target="_blank" title="https://github.com/leanprover-community/leancrawler">Lean crawler</a> does get access to some information. With more work we could maybe get something like what you want.</p>

#### [ Johan Commelin (Sep 03 2018 at 10:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/source%20code%20browser/near/133249002):
<p>That would be really nice, Patrick!</p>

#### [ Patrick Massot (Sep 03 2018 at 11:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/source%20code%20browser/near/133249148):
<p>I'm not sure it's worth the effort to fight Lean 3 here, but everyone should feel free to try</p>

#### [ Reid Barton (Sep 03 2018 at 20:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/source%20code%20browser/near/133273389):
<p>I have a mostly working "API documentation" generator although I'm not sure yet that it is more useful than just reading the source files.</p>

#### [ Reid Barton (Sep 03 2018 at 20:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/source%20code%20browser/near/133273545):
<p>I was hoping to look into how the editor integration works to see whether I could also produce hyperlinked source but I haven't gotten that far yet.</p>

#### [ Johan Commelin (Sep 03 2018 at 20:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/source%20code%20browser/near/133273678):
<p>Cool! Please let us know if you get hyperlinking working!</p>

#### [ Reid Barton (Sep 03 2018 at 20:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/source%20code%20browser/near/133274063):
<p>I do think probably the clearest use of such a tool is to advertise what we are doing in a way which is somewhat more transparent to people who are not already Lean users.</p>

#### [ Johan Commelin (Sep 03 2018 at 20:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/source%20code%20browser/near/133274134):
<p>Right, and it might not be unthinkable that demand for such usage will increase in the next months. When the word spreads about the perfectoid project, and when more senior mathematicians hear about the teaching that Kevin and Patrick are doing.</p>


{% endraw %}
