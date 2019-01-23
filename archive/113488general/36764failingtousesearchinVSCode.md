---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/36764failingtousesearchinVSCode.html
---

## Stream: [general](index.html)
### Topic: [failing to use search in VS Code](36764failingtousesearchinVSCode.html)

---

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 03 2018 at 12:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/failing%20to%20use%20search%20in%20VS%20Code/near/126038688):
I don't know how to search properly in VS Code. I am just doing something really stupid. I'm writing a new file, I have no imports at all, I type `[group G]` and it works, I type `[is_group_hom f]` and it doesn't. I know that `is_group_hom` is there somewhere. Here's my workflow:

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 03 2018 at 12:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/failing%20to%20use%20search%20in%20VS%20Code/near/126038745):
1) I click on the magnifying class in VS Code (with a project open which has mathlib as an import) and I search for `is_group_hom`. The only results I get are the instance in the file I just wrote, and two other instances in the *comments* in a file I'm not interested in (so in particular I can't go to this other piece of code and right click on is_group_hom)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 03 2018 at 12:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/failing%20to%20use%20search%20in%20VS%20Code/near/126038749):
2) Think "I am rubbish at using VS Code search"

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 03 2018 at 12:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/failing%20to%20use%20search%20in%20VS%20Code/near/126038752):
3) grep the source code and find it in seconds.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 03 2018 at 12:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/failing%20to%20use%20search%20in%20VS%20Code/near/126038757):
in mathlib in `algebra.group`. What am I doing wrong?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (May 03 2018 at 12:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/failing%20to%20use%20search%20in%20VS%20Code/near/126038770):
[2018-05-03-2.png](/user_uploads/3121/JTu5apknT8ioLvVRLi6qQHM4/2018-05-03-2.png)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 03 2018 at 12:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/failing%20to%20use%20search%20in%20VS%20Code/near/126038814):
How do I tell my VS Code to look where yours is looking

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (May 03 2018 at 12:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/failing%20to%20use%20search%20in%20VS%20Code/near/126038817):
what does the search result look like for you?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 03 2018 at 12:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/failing%20to%20use%20search%20in%20VS%20Code/near/126038827):
[is_group_hom.png](/user_uploads/3121/o4I8ufTMQcIiUYh1cfZQfjoA/is_group_hom.png)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (May 03 2018 at 12:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/failing%20to%20use%20search%20in%20VS%20Code/near/126038849):
Do you have mathlib open as a folder?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (May 03 2018 at 12:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/failing%20to%20use%20search%20in%20VS%20Code/near/126038877):
ctrl+shift+e

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (May 03 2018 at 12:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/failing%20to%20use%20search%20in%20VS%20Code/near/126038882):
and screenshot

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (May 03 2018 at 12:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/failing%20to%20use%20search%20in%20VS%20Code/near/126038885):
[2018-05-03-3.png](/user_uploads/3121/2TiT6Be0I94H7YWV1WFKWBlZ/2018-05-03-3.png)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sebastian Ullrich (May 03 2018 at 12:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/failing%20to%20use%20search%20in%20VS%20Code/near/126038889):
"Also note the Use Exclude Settings and Ignore Files toggle button in the files to exclude box. The toggle determines whether to exclude files that are ignored by your .gitignore files [...]"
`_target` is in `.gitignore`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 03 2018 at 12:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/failing%20to%20use%20search%20in%20VS%20Code/near/126038902):
[open_stuff.png](/user_uploads/3121/h7riDfVuoldfp6pyviUn20Io/open_stuff.png)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sebastian Ullrich (May 03 2018 at 12:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/failing%20to%20use%20search%20in%20VS%20Code/near/126038903):
https://code.visualstudio.com/docs/editor/codebasics#_search-across-files

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (May 03 2018 at 12:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/failing%20to%20use%20search%20in%20VS%20Code/near/126038943):
@**Kevin Buzzard** could you contract all your workspace folders

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (May 03 2018 at 12:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/failing%20to%20use%20search%20in%20VS%20Code/near/126038945):
and see if mathlib is open

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (May 03 2018 at 12:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/failing%20to%20use%20search%20in%20VS%20Code/near/126038946):
if not, drag mathlib into your workspace as the bottom folder and things should work fine

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 03 2018 at 12:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/failing%20to%20use%20search%20in%20VS%20Code/near/126038947):
I have `_target` and mathlib is in there I promise

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 03 2018 at 12:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/failing%20to%20use%20search%20in%20VS%20Code/near/126038953):
I don't understand the advanced options for file include/exclude: it just says "files to include/exclude" and then lets me type in a list of files without explaining how to ensure they are either included or excluded

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (May 03 2018 at 12:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/failing%20to%20use%20search%20in%20VS%20Code/near/126038956):
hmm

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 03 2018 at 12:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/failing%20to%20use%20search%20in%20VS%20Code/near/126038996):
So I've not needed to play with included/excluded

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 03 2018 at 12:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/failing%20to%20use%20search%20in%20VS%20Code/near/126038997):
I have just randomly clicked around and opened some directories in the ctrl-shift-E view

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 03 2018 at 12:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/failing%20to%20use%20search%20in%20VS%20Code/near/126038998):
and now it works

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (May 03 2018 at 12:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/failing%20to%20use%20search%20in%20VS%20Code/near/126038999):
what?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 03 2018 at 12:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/failing%20to%20use%20search%20in%20VS%20Code/near/126039007):
now everything is closed and it works

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 03 2018 at 12:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/failing%20to%20use%20search%20in%20VS%20Code/near/126039008):
It is completely hit-and-miss for me

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (May 03 2018 at 12:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/failing%20to%20use%20search%20in%20VS%20Code/near/126039009):
!scratch.lean excludes the file scratch.lean includes it

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (May 03 2018 at 12:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/failing%20to%20use%20search%20in%20VS%20Code/near/126039010):
this is very interesting

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 03 2018 at 12:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/failing%20to%20use%20search%20in%20VS%20Code/near/126039013):
I now have what looks to me like exactly the same set-up, with no obvious parameters having been changed, and search works find

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 03 2018 at 12:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/failing%20to%20use%20search%20in%20VS%20Code/near/126039014):
fine

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 03 2018 at 12:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/failing%20to%20use%20search%20in%20VS%20Code/near/126039053):
There is some basic thing which I am constantly running into and not spotting.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sebastian Ullrich (May 03 2018 at 12:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/failing%20to%20use%20search%20in%20VS%20Code/near/126039056):
"Also note the Use Exclude Settings and Ignore Files **toggle button** in the files to exclude box." :)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 03 2018 at 12:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/failing%20to%20use%20search%20in%20VS%20Code/near/126039103):
IT'S THE TOGGLE BUTTON

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (May 03 2018 at 12:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/failing%20to%20use%20search%20in%20VS%20Code/near/126039106):
lmao

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 03 2018 at 12:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/failing%20to%20use%20search%20in%20VS%20Code/near/126039107):
I can search!

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 03 2018 at 12:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/failing%20to%20use%20search%20in%20VS%20Code/near/126039110):
I thought that was a settings button opening an empty menu. I hadn't noticed it was changing colour

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 03 2018 at 12:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/failing%20to%20use%20search%20in%20VS%20Code/near/126039116):
the nightmare is over

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 03 2018 at 12:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/failing%20to%20use%20search%20in%20VS%20Code/near/126039117):
Thanks both of you :-)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 03 2018 at 12:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/failing%20to%20use%20search%20in%20VS%20Code/near/126039183):
I need to start wearing my glasses when I'm doing this stuff :-/

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 03 2018 at 12:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/failing%20to%20use%20search%20in%20VS%20Code/near/126039223):
I didn't even see the `!` in the greyed out text. Thanks Chris.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 03 2018 at 12:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/failing%20to%20use%20search%20in%20VS%20Code/near/126039431):
And here's another thing I fail at. If I open `algebra/group.lean` in mathlib

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 03 2018 at 12:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/failing%20to%20use%20search%20in%20VS%20Code/near/126039441):
I see on line 497 that there's a theorem called `mul`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 03 2018 at 12:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/failing%20to%20use%20search%20in%20VS%20Code/near/126039446):
but that `mul` won't be in the root namespace, I'm pretty sure. How do I find out the full name of that function?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 03 2018 at 12:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/failing%20to%20use%20search%20in%20VS%20Code/near/126039449):
The problem is that I might be in a namespace

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 03 2018 at 12:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/failing%20to%20use%20search%20in%20VS%20Code/near/126039452):
What I do currently is I simply edit `algebra/group.lean`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (May 03 2018 at 12:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/failing%20to%20use%20search%20in%20VS%20Code/near/126039453):
search for `namespace` on the file lol

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 03 2018 at 12:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/failing%20to%20use%20search%20in%20VS%20Code/near/126039456):
which is something I don't really like doing

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 03 2018 at 12:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/failing%20to%20use%20search%20in%20VS%20Code/near/126039459):
I don't want to start searching

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 03 2018 at 12:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/failing%20to%20use%20search%20in%20VS%20Code/near/126039460):
I just want to know the answer

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 03 2018 at 12:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/failing%20to%20use%20search%20in%20VS%20Code/near/126039461):
say the file uses 10 namespaces, some within others

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 03 2018 at 12:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/failing%20to%20use%20search%20in%20VS%20Code/near/126039463):
I have to check all their names and when they're closed

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 03 2018 at 12:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/failing%20to%20use%20search%20in%20VS%20Code/near/126039465):
I might have to move around a large file

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 03 2018 at 12:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/failing%20to%20use%20search%20in%20VS%20Code/near/126039466):
What I currently do is under the definition of `mul` in the file I just write `#print mul`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 03 2018 at 12:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/failing%20to%20use%20search%20in%20VS%20Code/near/126039504):
This gives me the prefix

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 03 2018 at 12:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/failing%20to%20use%20search%20in%20VS%20Code/near/126039507):
then I ctrl-Z to get rid of my edits

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 03 2018 at 12:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/failing%20to%20use%20search%20in%20VS%20Code/near/126039508):
It strikes me as an amateurish approach

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (May 03 2018 at 12:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/failing%20to%20use%20search%20in%20VS%20Code/near/126039510):
@**Sebastian Ullrich**

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 03 2018 at 12:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/failing%20to%20use%20search%20in%20VS%20Code/near/126039511):
but mouse hover over mul doesn't do anything

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 03 2018 at 12:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/failing%20to%20use%20search%20in%20VS%20Code/near/126039512):
and right click on mul doesn't work

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 03 2018 at 12:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/failing%20to%20use%20search%20in%20VS%20Code/near/126039516):
"no definition found for mul"

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (May 03 2018 at 12:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/failing%20to%20use%20search%20in%20VS%20Code/near/126039521):
I mean, I'll just import that file in a sandbox and type `#check mul` and ctrl+space

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (May 03 2018 at 12:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/failing%20to%20use%20search%20in%20VS%20Code/near/126039523):
ctrl+space works quite well

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 03 2018 at 12:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/failing%20to%20use%20search%20in%20VS%20Code/near/126039524):
My method has the advantage that I never lose sight of the theorem I want

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 03 2018 at 12:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/failing%20to%20use%20search%20in%20VS%20Code/near/126039529):
aah that's an idea which will probably work well in many situations

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sebastian Ullrich (May 03 2018 at 12:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/failing%20to%20use%20search%20in%20VS%20Code/near/126039573):
You're right, it would make sense if the definition had the same mouseover as its references

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (May 03 2018 at 16:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/failing%20to%20use%20search%20in%20VS%20Code/near/126048674):
I use emacs, but this is something I've wished for too: the ability to see at a keystroke
* which namespaces the current location is inside
* what variables/parameters are in scope at the current location

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (May 03 2018 at 16:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/failing%20to%20use%20search%20in%20VS%20Code/near/126048677):
I don't know if this can be implemented without extending lean

