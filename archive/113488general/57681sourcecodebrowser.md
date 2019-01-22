---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/57681sourcecodebrowser.html
---

## [general](index.html)
### [source code browser](57681sourcecodebrowser.html)

#### [Johan Commelin (Sep 03 2018 at 09:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/source%20code%20browser/near/133246061):
Is there some way to easily turn a repo of Lean files into a hyperlinked bunch of HTML files? If we want to showcase some code to mathematicians, we should take into account that they have never heard of git or github before. Also, on github you can't click on an imported file, or a token, to go somewhere else. And we can't expect people who want to read some source files to install VScode before they are able to really use it.

#### [Johan Commelin (Sep 03 2018 at 09:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/source%20code%20browser/near/133246070):
So basically, I would like a read-only VScode that can easily be hosted somewhere. Just a bunch of static files.

#### [Kenny Lau (Sep 03 2018 at 09:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/source%20code%20browser/near/133246129):
I mean, for other languages (like Java) the corresponding website is grepcode

#### [Kenny Lau (Sep 03 2018 at 09:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/source%20code%20browser/near/133246132):
so I don't think things like this is very common

#### [Soham Chowdhury (Sep 03 2018 at 09:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/source%20code%20browser/near/133246315):
I think what @**Johan Commelin** has in mind is closer to Javadoc, Haddock, or `agda --html`.

#### [Mario Carneiro (Sep 03 2018 at 09:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/source%20code%20browser/near/133246374):
this has been a dream for some time

#### [Mario Carneiro (Sep 03 2018 at 09:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/source%20code%20browser/near/133246379):
My `#explode` command was actually working toward that goal

#### [Johan Commelin (Sep 03 2018 at 09:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/source%20code%20browser/near/133246384):
So, why is it easy in VScode?

#### [Mario Carneiro (Sep 03 2018 at 09:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/source%20code%20browser/near/133246386):
Currently it's a bit tough to get good data on what exists in a file

#### [Johan Commelin (Sep 03 2018 at 09:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/source%20code%20browser/near/133246428):
If VScode can figure out where to take me, if I `Ctrl-click` on something, can't it export a bunch of html files?

#### [Mario Carneiro (Sep 03 2018 at 09:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/source%20code%20browser/near/133246443):
Actually what you are describing sounds a bit different - the plan has been to show some abbreviated or expandable or indexed form of the file to make browsing easier

#### [Johan Commelin (Sep 03 2018 at 09:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/source%20code%20browser/near/133246446):
Ok, I guess that is harder.

#### [Johan Commelin (Sep 03 2018 at 09:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/source%20code%20browser/near/133246487):
I just figure that if Kevin publishes a paper, then he want to include a URL with a static view of his files that is easy to navigate.

#### [Johan Commelin (Sep 03 2018 at 09:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/source%20code%20browser/near/133246490):
GitHub isn't good enough.

#### [Soham Chowdhury (Sep 03 2018 at 09:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/source%20code%20browser/near/133246495):
It should be possible to dump source code into plain HTML files and then modify or hook into `vscode-lean` (I think) to use its symbol table to turn identifiers into links.

#### [Mario Carneiro (Sep 03 2018 at 09:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/source%20code%20browser/near/133246496):
I think Mizar has a pretty similar display to what you are suggesting, Coq too to some degree

#### [Mario Carneiro (Sep 03 2018 at 09:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/source%20code%20browser/near/133246513):
See, for example: http://www.mizar.org/version/current/html/polynom5.html#T74

#### [Soham Chowdhury (Sep 03 2018 at 09:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/source%20code%20browser/near/133246515):
https://agda.github.io/agda-stdlib/README.html
Just to be clear, @**Johan Commelin**, does this look like what you want?

#### [Soham Chowdhury (Sep 03 2018 at 09:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/source%20code%20browser/near/133246555):
Yeah, or that

#### [Johan Commelin (Sep 03 2018 at 09:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/source%20code%20browser/near/133246571):
Right, those are both good examples.

#### [Johan Commelin (Sep 03 2018 at 09:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/source%20code%20browser/near/133246579):
Althought the Agda one only has a bunch of comments and imports...

#### [Soham Chowdhury (Sep 03 2018 at 09:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/source%20code%20browser/near/133246587):
You can click on the imports to get to more interesting files.

#### [Soham Chowdhury (Sep 03 2018 at 09:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/source%20code%20browser/near/133246588):
Like this: https://agda.github.io/agda-stdlib/Category.Monad.html

#### [Johan Commelin (Sep 03 2018 at 10:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/source%20code%20browser/near/133246652):
I have very little fu in this regard. But it seems to me that it shouldn't be too hard to hack such a thing together, right?

#### [Mario Carneiro (Sep 03 2018 at 10:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/source%20code%20browser/near/133246677):
I really hope there is a more effective way to locate tokens than asking lean at each position what token is at that location (and where is it defined)

#### [Mario Carneiro (Sep 03 2018 at 10:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/source%20code%20browser/near/133246719):
otherwise this could take a really long time

#### [Johan Commelin (Sep 03 2018 at 10:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/source%20code%20browser/near/133246735):
Not longer then `lean --make`, right?

#### [Johan Commelin (Sep 03 2018 at 10:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/source%20code%20browser/near/133246736):
And this is something that you'll run only occasionaly.

#### [Johan Commelin (Sep 03 2018 at 10:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/source%20code%20browser/near/133246744):
So I really don't care about runtime.

#### [Mario Carneiro (Sep 03 2018 at 10:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/source%20code%20browser/near/133246745):
yes longer than lean --make

#### [Johan Commelin (Sep 03 2018 at 10:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/source%20code%20browser/near/133246750):
Ooh, hmmm

#### [Mario Carneiro (Sep 03 2018 at 10:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/source%20code%20browser/near/133246755):
I'm talking about asking lean at each character what is there, basically the software version of clicking everywhere to see what happens

#### [Johan Commelin (Sep 03 2018 at 10:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/source%20code%20browser/near/133246804):
But Lean stores this data already, right? We saw it sitting somewhere in some `expr`.

#### [Johan Commelin (Sep 03 2018 at 10:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/source%20code%20browser/near/133246815):
How does VScode figure this out? Only at runtime, when I click somewhere?

#### [Mario Carneiro (Sep 03 2018 at 10:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/source%20code%20browser/near/133246818):
Through the lean server API

#### [Mario Carneiro (Sep 03 2018 at 10:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/source%20code%20browser/near/133246830):
you click, VSCode sends lean a message asking "what is here", lean responds

#### [Johan Commelin (Sep 03 2018 at 10:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/source%20code%20browser/near/133246833):
I see. And that is going to be slow.

#### [Mario Carneiro (Sep 03 2018 at 10:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/source%20code%20browser/near/133246841):
if that is the only message you can send, then we are in trouble, but maybe there is a saner data structure being sent

#### [Soham Chowdhury (Sep 03 2018 at 10:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/source%20code%20browser/near/133246843):
Hm, isn't there a lexer/parser/AST-generator for Lean that we can hook into?

#### [Mario Carneiro (Sep 03 2018 at 10:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/source%20code%20browser/near/133246844):
see lean 4

#### [Mario Carneiro (Sep 03 2018 at 10:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/source%20code%20browser/near/133246890):
this is why many of the leandoc plans are waiting on lean 4

#### [Johan Commelin (Sep 03 2018 at 10:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/source%20code%20browser/near/133246918):
/me proposes :four_leaf_clover: as the default emoji for marking dreams and wishes that will be trivially realizable when Lean 4 emerges :stuck_out_tongue_wink:

#### [Mario Carneiro (Sep 03 2018 at 10:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/source%20code%20browser/near/133246924):
maybe we should make a list

#### [Johan Commelin (Sep 03 2018 at 10:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/source%20code%20browser/near/133246973):
Voila: https://leanprover.zulipchat.com/#narrow/search/.22lean.204.22

#### [Johannes Hölzl (Sep 03 2018 at 10:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/source%20code%20browser/near/133248804):
Apropos Lean 4: Leo gave a new talk at Galois inc. You find the slides on leanprover.github.io: http://leanprover.github.io/talks/LeanAtGalois.pdf Some new information about Lean4!

#### [Johannes Hölzl (Sep 03 2018 at 10:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/source%20code%20browser/near/133248820):
local constants are now called free variables :)

#### [Patrick Massot (Sep 03 2018 at 10:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/source%20code%20browser/near/133248821):
My [Lean crawler](https://github.com/leanprover-community/leancrawler) does get access to some information. With more work we could maybe get something like what you want.

#### [Johan Commelin (Sep 03 2018 at 10:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/source%20code%20browser/near/133249002):
That would be really nice, Patrick!

#### [Patrick Massot (Sep 03 2018 at 11:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/source%20code%20browser/near/133249148):
I'm not sure it's worth the effort to fight Lean 3 here, but everyone should feel free to try

#### [Reid Barton (Sep 03 2018 at 20:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/source%20code%20browser/near/133273389):
I have a mostly working "API documentation" generator although I'm not sure yet that it is more useful than just reading the source files.

#### [Reid Barton (Sep 03 2018 at 20:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/source%20code%20browser/near/133273545):
I was hoping to look into how the editor integration works to see whether I could also produce hyperlinked source but I haven't gotten that far yet.

#### [Johan Commelin (Sep 03 2018 at 20:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/source%20code%20browser/near/133273678):
Cool! Please let us know if you get hyperlinking working!

#### [Reid Barton (Sep 03 2018 at 20:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/source%20code%20browser/near/133274063):
I do think probably the clearest use of such a tool is to advertise what we are doing in a way which is somewhat more transparent to people who are not already Lean users.

#### [Johan Commelin (Sep 03 2018 at 20:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/source%20code%20browser/near/133274134):
Right, and it might not be unthinkable that demand for such usage will increase in the next months. When the word spreads about the perfectoid project, and when more senior mathematicians hear about the teaching that Kevin and Patrick are doing.

