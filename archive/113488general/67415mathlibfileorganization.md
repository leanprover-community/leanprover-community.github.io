---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/67415mathlibfileorganization.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [mathlib file organization](https://leanprover-community.github.io/archive/113488general/67415mathlibfileorganization.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Sean Leather (Jun 01 2018 at 10:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20file%20organization/near/127406142):
<p>For those interested in the file organization of mathlib, I've written up a <a href="https://github.com/leanprover/mathlib/issues/148" target="_blank" title="https://github.com/leanprover/mathlib/issues/148">proposal</a> for a small change that, I think, will improve things a bit. Feedback welcome!</p>

#### [ Johan Commelin (Jun 01 2018 at 10:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20file%20organization/near/127406319):
<p>Interesting proposal. I have also noticed myself getting lost in the long files...</p>

#### [ Johan Commelin (Jun 01 2018 at 10:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20file%20organization/near/127406367):
<p>I would also like to separate the "interface lemma's" from the "real beef", although maybe there is not always a clear line between them.</p>

#### [ Sean Leather (Jun 01 2018 at 10:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20file%20organization/near/127406374):
<blockquote>
<p>I have also noticed myself getting lost in the long files...</p>
</blockquote>
<p>I'm glad I'm not the only one. I think this is a first logical step to reducing the size of files. There are other steps that can be taken later, of course.</p>

#### [ Johan Commelin (Jun 01 2018 at 10:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20file%20organization/near/127406415):
<p>Also, I have never read what the purpose of <code>default.lean</code> is. But if I inferred it correctly, then I think we should make more use of it.</p>

#### [ Johan Commelin (Jun 01 2018 at 10:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20file%20organization/near/127406421):
<p>And then using more files will not increase the length of <code>import</code> lines.</p>

#### [ Mario Carneiro (Jun 01 2018 at 10:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20file%20organization/near/127406424):
<p>I've been deliberately avoiding the use of <code>default.lean</code> within mathlib, and I think it's good practice without as well</p>

#### [ Sean Leather (Jun 01 2018 at 10:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20file%20organization/near/127406464):
<p>AFAIK, the file <code>data/list/default.lean</code> allows you to write <code>import data.list</code> instead of <code>import data.list.default</code>. So, the <code>default.lean</code> file generally <code>import</code>s everything in the directory.</p>

#### [ Johan Commelin (Jun 01 2018 at 10:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20file%20organization/near/127406466):
<p>exactly</p>

#### [ Mario Carneiro (Jun 01 2018 at 10:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20file%20organization/near/127406467):
<p>right</p>

#### [ Mario Carneiro (Jun 01 2018 at 10:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20file%20organization/near/127406472):
<p>and that's exactly what I don't want</p>

#### [ Johan Commelin (Jun 01 2018 at 10:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20file%20organization/near/127406479):
<p>Why not?</p>

#### [ Mario Carneiro (Jun 01 2018 at 10:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20file%20organization/near/127406482):
<p>that adds a bunch of spurious dependencies in an already delicate graph</p>

#### [ Mario Carneiro (Jun 01 2018 at 10:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20file%20organization/near/127406493):
<p>remember that circular dependencies are bad but there isn't an obvious linear order of files</p>

#### [ Johan Commelin (Jun 01 2018 at 10:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20file%20organization/near/127406494):
<p>Sure, but there is a partial order, right?</p>

#### [ Johannes Hölzl (Jun 01 2018 at 10:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20file%20organization/near/127406536):
<p>It should be a DAG</p>

#### [ Johan Commelin (Jun 01 2018 at 10:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20file%20organization/near/127406537):
<p>Do we already have a script that generates a graphviz visualisation?</p>

#### [ Mario Carneiro (Jun 01 2018 at 10:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20file%20organization/near/127406586):
<p><a href="/user_uploads/3121/Xpw3mSr_YxZO2VxAF_owodVt/mathlib.gif" target="_blank" title="mathlib.gif">mathlib.gif</a></p>
<div class="message_inline_image"><a href="/user_uploads/3121/Xpw3mSr_YxZO2VxAF_owodVt/mathlib.gif" target="_blank" title="mathlib.gif"><img src="/user_uploads/3121/Xpw3mSr_YxZO2VxAF_owodVt/mathlib.gif"></a></div>

#### [ Johan Commelin (Jun 01 2018 at 10:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20file%20organization/near/127406596):
<p>Right, I had a similar graph on the level of theorems and proofs for my thesis.</p>

#### [ Johan Commelin (Jun 01 2018 at 10:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20file%20organization/near/127406643):
<p>But why are you scared that the graph becomes to delicate for Lean?</p>

#### [ Sean Leather (Jun 01 2018 at 10:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20file%20organization/near/127406644):
<p>I don't quite see the problem with <code>default.lean</code>. Nonetheless, I see it as just an extra and there's no actual need to have one.</p>

#### [ Johan Commelin (Jun 01 2018 at 10:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20file%20organization/near/127406646):
<p>Well, we need it to keep imports manageable.</p>

#### [ Johan Commelin (Jun 01 2018 at 10:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20file%20organization/near/127406647):
<p>Already it is common to have files with &gt;8 imports</p>

#### [ Johan Commelin (Jun 01 2018 at 10:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20file%20organization/near/127406652):
<p>If you want to split a 3000-line file into 5 files</p>

#### [ Mario Carneiro (Jun 01 2018 at 10:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20file%20organization/near/127406653):
<p>Currently, folders are organized by topic, and files are organized by dependency units</p>

#### [ Mario Carneiro (Jun 01 2018 at 10:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20file%20organization/near/127406661):
<p>so if there is no dependency issue and the topic is still the same, it all goes in one file</p>

#### [ Sean Leather (Jun 01 2018 at 10:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20file%20organization/near/127406705):
<p>At least with my proposal, once you split a file into one for definitions and one for theorems, the theorems file imports the definitions file, and you just import the theorems file. The <code>default.lean</code> just allows you to leave off one part of the hierarchy.</p>

#### [ Johan Commelin (Jun 01 2018 at 10:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20file%20organization/near/127406706):
<p>What is a "dependency issue"?</p>

#### [ Mario Carneiro (Jun 01 2018 at 10:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20file%20organization/near/127406712):
<p>A is used by B, which is used by A'</p>

#### [ Mario Carneiro (Jun 01 2018 at 10:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20file%20organization/near/127406718):
<p>and A' wants to be in the same file as A</p>

#### [ Johan Commelin (Jun 01 2018 at 10:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20file%20organization/near/127406727):
<p>Ok, and there is a reason (I guess the topic) that B should not be in that file as well.</p>

#### [ Mario Carneiro (Jun 01 2018 at 10:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20file%20organization/near/127406731):
<p>I've thought many times about separating out definitions. But I'm not sure it's as easy as that</p>

#### [ Mario Carneiro (Jun 01 2018 at 10:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20file%20organization/near/127406774):
<p>in lean, definitions and theorems are all mixed up thanks to curry howard</p>

#### [ Sean Leather (Jun 01 2018 at 10:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20file%20organization/near/127406781):
<p>As I said, there may be exceptions, but I think there are many obvious easy examples.</p>

#### [ Sean Leather (Jun 01 2018 at 10:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20file%20organization/near/127406790):
<p>And I'm happy to give it a try myself.</p>

#### [ Mario Carneiro (Jun 01 2018 at 10:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20file%20organization/near/127406793):
<p>If you are using <code>list</code> as your test bed it's not representative</p>

#### [ Sean Leather (Jun 01 2018 at 10:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20file%20organization/near/127406794):
<p>If other people think this is a good thing.</p>

#### [ Mario Carneiro (Jun 01 2018 at 10:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20file%20organization/near/127406797):
<p>programming stuff in general tends to be less dependent</p>

#### [ Sean Leather (Jun 01 2018 at 10:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20file%20organization/near/127406841):
<p>Perhaps. But there is a lot of programming stuff in mathlib. <span class="emoji emoji-1f642" title="simple smile">:simple_smile:</span></p>

#### [ Sean Leather (Jun 01 2018 at 10:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20file%20organization/near/127406844):
<p>And what's the harm with doing it there?</p>

#### [ Mario Carneiro (Jun 01 2018 at 10:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20file%20organization/near/127406906):
<p>also, how is theorem organization handled? What to do if a definition depends on a theorem?</p>

#### [ Sean Leather (Jun 01 2018 at 10:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20file%20organization/near/127406916):
<p>It probably depends on the example.</p>

#### [ Mario Carneiro (Jun 01 2018 at 11:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20file%20organization/near/127406972):
<p>What about instances? are they definitions or theorems?</p>

#### [ Sean Leather (Jun 01 2018 at 11:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20file%20organization/near/127406983):
<p>To keep the proposal minimal, I don't say anything about that.</p>

#### [ Sean Leather (Jun 01 2018 at 11:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20file%20organization/near/127406990):
<p>This is where concrete examples help.</p>

#### [ Mario Carneiro (Jun 01 2018 at 11:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20file%20organization/near/127407044):
<p><code>rat</code> is a field</p>

#### [ Sean Leather (Jun 01 2018 at 11:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20file%20organization/near/127407045):
<p>What I really want to know is whether people are, <em>in general</em>, in favor of having definitions separated from theorems. From my experience using mathlib, I believe I am. There are certainly wrinkles to be ironed out.</p>

#### [ Mario Carneiro (Jun 01 2018 at 11:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20file%20organization/near/127407050):
<p>I am worried about losing topicality</p>

#### [ Mario Carneiro (Jun 01 2018 at 11:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20file%20organization/near/127407061):
<p>particularly for smaller definitions that are more auxiliary or only used in a few theorems</p>

#### [ Sean Leather (Jun 01 2018 at 11:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20file%20organization/near/127407063):
<p>Isn't <code>rat</code> a <code>structure</code>?</p>

#### [ Mario Carneiro (Jun 01 2018 at 11:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20file%20organization/near/127407070):
<p>I mean a mathematical field</p>

#### [ Mario Carneiro (Jun 01 2018 at 11:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20file%20organization/near/127407078):
<p>That's an instance</p>

#### [ Mario Carneiro (Jun 01 2018 at 11:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20file%20organization/near/127407113):
<p>in rat.lean</p>

#### [ Sean Leather (Jun 01 2018 at 11:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20file%20organization/near/127407115):
<p>You mean <code>instance field_rat : discrete_field ℚ</code>?</p>

#### [ Mario Carneiro (Jun 01 2018 at 11:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20file%20organization/near/127407119):
<p>yeah</p>

#### [ Mario Carneiro (Jun 01 2018 at 11:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20file%20organization/near/127407194):
<p><span class="user-mention" data-user-id="110865">@Jeremy Avigad</span> may want to chip in on this topic</p>

#### [ Sean Leather (Jun 01 2018 at 11:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20file%20organization/near/127407199):
<p>It seems to me that <code>data/rat.lean</code> would also benefit from extracting the <code>def</code>s.</p>
<div class="codehilite"><pre><span></span>$ grep &#39;^def&#39; data/rat.lean | wc -l
       7
$ grep &#39;^theorem&#39; data/rat.lean | wc -l
      44
$ grep &#39;^instance&#39; data/rat.lean | wc -l
      16
</pre></div>


<p>Whether you put instances in with theorems or not is a secondary question. Since I'm not familiar with it, I don't have the answer for you.</p>

#### [ Mario Carneiro (Jun 01 2018 at 11:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20file%20organization/near/127407246):
<p>You can't just count them, theorems will almost always outnumber defs by a large margin</p>

#### [ Sean Leather (Jun 01 2018 at 11:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20file%20organization/near/127407248):
<p>That's kind of the point. <span class="emoji emoji-1f609" title="wink">:wink:</span></p>

#### [ Mario Carneiro (Jun 01 2018 at 11:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20file%20organization/near/127407255):
<p>But there is often def -&gt; theorem -&gt; def -&gt; theorem dependencies that will be messed up with such a reorganization</p>

#### [ Sean Leather (Jun 01 2018 at 11:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20file%20organization/near/127407258):
<p>Indeed! So it needs a concrete attempt.</p>

#### [ Johannes Hölzl (Jun 01 2018 at 11:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20file%20organization/near/127407260):
<p>and the instances and theorems are very interdependent</p>

#### [ Mario Carneiro (Jun 01 2018 at 11:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20file%20organization/near/127407328):
<p>By the way, one downside of the partial order structure of files is that it's not exactly a lattice, so it's not clear where to put cross cutting theorems</p>

#### [ Johan Commelin (Jun 01 2018 at 11:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20file%20organization/near/127407335):
<p>With my current PR on algebraic topology, I split it up in 3 files... in this example, would you have rather had 1 file? (Question is for mathlib maintainers.)</p>

#### [ Mario Carneiro (Jun 01 2018 at 11:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20file%20organization/near/127407344):
<p>like if you have incomparable files A and B and you have a theorem about AB which is used by C</p>

#### [ Sean Leather (Jun 01 2018 at 11:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20file%20organization/near/127407391):
<blockquote>
<p>By the way, one downside of the partial order structure of files is that it's not exactly a lattice, so it's not clear where to put cross cutting theorems</p>
</blockquote>
<p>Which is one of the reasons I left that concern out of the proposal.</p>

#### [ Johan Commelin (Jun 01 2018 at 11:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20file%20organization/near/127407469):
<p>(Mario, in my thesis I had one theorem/def per file -- this is all LaTeX --, and it worked quite nicely. I had some LaTeX macros that hyperlinked all references to theorems and definitions. And then with a bit of bash-fu I got PDF's for every theorem/def. I wanted an HTML realisation, but it never became nice enough...)</p>

#### [ Johan Commelin (Jun 01 2018 at 11:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20file%20organization/near/127407481):
<p>So... that was the other end of the spectrum (-;</p>

#### [ Johan Commelin (Jun 01 2018 at 11:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20file%20organization/near/127407488):
<p>And it was on a smaller scale, and not formalised.</p>

#### [ Sean Leather (Jun 01 2018 at 11:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20file%20organization/near/127407537):
<p>Yeah, that could make sense for a thesis, but it's probably too far for a library. <span class="emoji emoji-1f609" title="wink">:wink:</span></p>

#### [ Mario Carneiro (Jun 01 2018 at 11:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20file%20organization/near/127407608):
<p>By the way, metamath is organized as <a href="http://set.mm" target="_blank" title="http://set.mm">set.mm</a>, a single 20MB text file with lots of ascii headers of various levels to give it a book-like structure</p>

#### [ Mario Carneiro (Jun 01 2018 at 11:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20file%20organization/near/127407619):
<p>so I guess that's the extreme opposite</p>

#### [ Sean Leather (Jun 01 2018 at 11:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20file%20organization/near/127407624):
<p><a href="https://github.com/metamath/set.mm/blob/master/set.mm" target="_blank" title="https://github.com/metamath/set.mm/blob/master/set.mm">OMG</a> <span class="emoji emoji-1f4a3" title="bomb">:bomb:</span></p>

#### [ Mario Carneiro (Jun 01 2018 at 11:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20file%20organization/near/127407674):
<p>One thing that I like about that is it enforces a linear dependency structure, which makes the dependency question trivial</p>

#### [ Mario Carneiro (Jun 01 2018 at 11:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20file%20organization/near/127407738):
<p>the downside is that it (apparently) adds a lot of spurious dependencies, more than are truly needed by the theorems</p>

#### [ Mario Carneiro (Jun 01 2018 at 11:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20file%20organization/near/127407749):
<p>But that's less of a problem when the entire file can be verified in less than 10 seconds</p>

#### [ Mario Carneiro (Jun 01 2018 at 11:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20file%20organization/near/127407823):
<p>Also metamath has a separate html view so you aren't completely reliant on text navigation, you can look at abridged views and high level views of the theorems so that you can skip over the boring stuff... Maybe something like this in lean could be helpful for you</p>

#### [ Sean Leather (Jun 01 2018 at 11:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20file%20organization/near/127407889):
<p>It's still useful to browse code, and I still think good code organization is a worthy goal.</p>

#### [ Jeremy Avigad (Jun 01 2018 at 19:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20file%20organization/near/127427222):
<p>I think it generally makes it easier to read theory files when the definitions are an integral part of theory. The definitions are needed to understand the theorems and the theorems illustrate the intended usage of the definitions. It would be annoying to have to flip back and forth between files.</p>

#### [ Chris Hughes (Jun 01 2018 at 20:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20file%20organization/near/127429035):
<p>How about just listing all the definitions in a comment at the top of the file?</p>

#### [ Kevin Buzzard (Jun 01 2018 at 20:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20file%20organization/near/127429473):
<p>And while we're at it how about listing what goes on in the file in another comment at the top of the file?</p>

#### [ Kevin Buzzard (Jun 01 2018 at 20:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20file%20organization/near/127429501):
<p><span class="user-mention" data-user-id="110049">@Mario Carneiro</span> what would you make of such PRs? Someone adding definitions and comments explaining what is going in various files in mathlib?</p>

#### [ Mario Carneiro (Jun 01 2018 at 20:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20file%20organization/near/127429555):
<p>Absolutely go ahead</p>

#### [ Mario Carneiro (Jun 01 2018 at 20:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20file%20organization/near/127429564):
<p>I do my best but I also have a lot of theorems I want to prove</p>

#### [ Kevin Buzzard (Jun 01 2018 at 20:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20file%20organization/near/127429571):
<p>theorems are overrated</p>

#### [ Scott Morrison (Jun 02 2018 at 00:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20file%20organization/near/127442021):
<p><span class="user-mention" data-user-id="110038">@Kevin Buzzard</span></p>

#### [ Kevin Buzzard (Jun 02 2018 at 00:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20file%20organization/near/127442371):
<p>I'm into definitions</p>

#### [ Johan Commelin (Jun 02 2018 at 21:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20file%20organization/near/127475414):
<blockquote>
<p>theorems are overrated — <span class="user-mention" data-user-id="110038">@Kevin Buzzard</span> </p>
</blockquote>
<p>I just read the following blogpost of M. Harris: <a href="https://mathematicswithoutapologies.wordpress.com/2018/06/02/is-the-tone-appropriate-is-the-mathematics-at-the-right-level/" target="_blank" title="https://mathematicswithoutapologies.wordpress.com/2018/06/02/is-the-tone-appropriate-is-the-mathematics-at-the-right-level/">https://mathematicswithoutapologies.wordpress.com/2018/06/02/is-the-tone-appropriate-is-the-mathematics-at-the-right-level/</a><br>
It contains the following quote of Scholze:</p>
<blockquote>
<p>“What I care most about are definitions. For one thing, humans describe mathematics through language, and, as always, we need sharp words in order to articulate our ideas clearly. (For example, for a long time, I had some idea of the concept of diamonds. But only when I came up with a good name could I really start to think about it, let alone communicate it to others. Finding the name took several months (or even a year?). Then it took another two or three years to finally write down the correct definition (among many close variants). The essential difficulty in writing “Etale cohomology of diamonds” was (by far) not giving the proofs, but finding the definitions.) But even beyond mere language, we perceive mathematical nature through the lenses given by definitions, and it is critical that the definitions put the essential points into focus.</p>
<p>Unfortunately, it is impossible to find the right definitions by pure thought; one needs to detect the correct problems where progress will require the isolation of a new key concept.”</p>
</blockquote>

#### [ Mario Carneiro (Jun 02 2018 at 21:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20file%20organization/near/127475754):
<p>I think this is an over-mature view though; it is only in the context where theorems are commonplace that you can advocate a return to focus on definitions</p>

#### [ Mario Carneiro (Jun 02 2018 at 21:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20file%20organization/near/127475755):
<p>it's too easy to abuse this view to focus only on definitions at the expense of theorems</p>

#### [ Kevin Buzzard (Jun 02 2018 at 21:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20file%20organization/near/127475795):
<p>On the other hand there are some definitions which are much more important than theorems.</p>

#### [ Mario Carneiro (Jun 02 2018 at 21:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20file%20organization/near/127475853):
<p>I don't argue that definitions aren't important, essential even. They are the core of the theory, the things that theorems relate</p>

#### [ Mario Carneiro (Jun 02 2018 at 21:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20file%20organization/near/127475888):
<p>but to take one without the other is to see only half the picture</p>

#### [ Johan Commelin (Jun 02 2018 at 21:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20file%20organization/near/127475898):
<p>Maybe I like the fact that DTT muddles the distinction between the two.</p>

#### [ Kevin Buzzard (Jun 02 2018 at 21:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20file%20organization/near/127476060):
<p>That's right, so we should take the most important of both :-)</p>

#### [ Kevin Buzzard (Jun 02 2018 at 21:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20file%20organization/near/127476065):
<p>and there is surely ample evidence out there now in blogland and mathoverflow and whatever</p>

#### [ Kevin Buzzard (Jun 02 2018 at 21:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20file%20organization/near/127476066):
<p>that perfectoid spaces are a supremely important definition</p>

#### [ Sean Leather (Jun 04 2018 at 10:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20file%20organization/near/127534230):
<blockquote>
<p>I think it generally makes it easier to read theory files when the definitions are an integral part of theory. The definitions are needed to understand the theorems and the theorems illustrate the intended usage of the definitions. It would be annoying to have to flip back and forth between files.</p>
</blockquote>
<p><span class="user-mention" data-user-id="110865">@Jeremy Avigad</span> Thanks for your thoughts.</p>
<p>I agree with you that it is useful to see definitions and theorems together, but I find that most theorems beyond the simplest <code>rfl</code> involve more than one definition. Thus, when the definitions are interleaved with large chunks of theorems, I'm either flipping back and forth or viewing different parts of the same file in a split screen. Whereas with all (or as many as is reasonable) of the definitions in one file, I can view two files side-by-side, one with definitions and one with theorems involving those definitions.</p>
<p>To summarize, while I think it would be nice to have a definition with a nearby associated group of theorems, I think that that is already problematic in mathlib in a very practical sense because the number of theorems generally surpasses the number of definitions and makes it difficult to find them. In addition to that, I think definition discovery is a useful part of learning a theory topic and would be aided by putting the definitions in one place.</p>

#### [ Sean Leather (Jun 04 2018 at 10:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20file%20organization/near/127534547):
<blockquote>
<p>How about just listing all the definitions in a comment at the top of the file?</p>
</blockquote>
<p><span class="user-mention" data-user-id="110044">@Chris Hughes</span>: By “definition,” are you referring to either (a) the entire declaration (i.e. <code>def name := term</code>) or (b) only the name?</p>
<p>(a) While I grant you that we are not engaging in (“full-blown”) software engineering when writing mathlib, this is one of those big no-no's in practice. Duplication in comments is notorious for getting out of sync with code. I would strongly recommend against doing this.</p>
<p>(b) Listing the names may provide a minor benefit for reference. But, since theorems generally use the unfolded definition in some form, this won't be helpful when trying to understand a theorem that uses multiple definitions, because you will end up trying to find the declarations themselves. It won't solve the problem I'm trying to solve.</p>

#### [ Andrew Ashworth (Jun 04 2018 at 11:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20file%20organization/near/127536279):
<p>I think what you really want to do is write a doxygen extension for lean :)</p>

#### [ Andrew Ashworth (Jun 04 2018 at 11:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20file%20organization/near/127536339):
<p>not like other programming files don't have the same problem with separation of data structures / classes and methods...</p>

#### [ Sean Leather (Jun 04 2018 at 11:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20file%20organization/near/127536412):
<blockquote>
<p>not like other programming files don't have the same problem with separation of data structures / classes and methods...</p>
</blockquote>
<p>Certainly! My proposal is actually similar to a common pattern in Haskell package development: putting types in a file of their own.</p>

#### [ Andrew Ashworth (Jun 04 2018 at 11:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20file%20organization/near/127536545):
<p>that's a big pain in lean though since circular dependencies are hard to handle</p>

#### [ Johan Commelin (Jun 04 2018 at 11:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20file%20organization/near/127536546):
<p><a href="https://www.stack.nl/~dimitri/doxygen/manual/faq.html#faq_pgm_X" target="_blank" title="https://www.stack.nl/~dimitri/doxygen/manual/faq.html#faq_pgm_X">https://www.stack.nl/~dimitri/doxygen/manual/faq.html#faq_pgm_X</a><br>
Seems like Lean falls in the 3rd category...</p>

#### [ Andrew Ashworth (Jun 04 2018 at 11:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20file%20organization/near/127536710):
<p>it wouldn't be so bad if you wanted something quick and dirty - you just want to grab things in between def | definition, lemma, theorem, :, :=, and a newline</p>

#### [ Andrew Ashworth (Jun 04 2018 at 11:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20file%20organization/near/127536771):
<p>but I am not volunteering to do this :) however it seems more likely to happen than changing how mathlib is organized</p>

#### [ Andrew Ashworth (Jun 04 2018 at 11:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20file%20organization/near/127536844):
<p>it seems straightfoward - famous last words of every project I've ever estimated ever</p>

#### [ Patrick Massot (Jun 04 2018 at 13:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20file%20organization/near/127540033):
<p>I know I'm always writing the same thing, but I think we shouldn't forget that some people already developed huge libraries in a language very close to Lean, and have a look at how they handle this. For the comments at top of files see <a href="https://github.com/math-comp/math-comp/blob/master/mathcomp/algebra/vector.v" target="_blank" title="https://github.com/math-comp/math-comp/blob/master/mathcomp/algebra/vector.v">https://github.com/math-comp/math-comp/blob/master/mathcomp/algebra/vector.v</a> (this is random file from math-comp, they all look the same)</p>

#### [ Patrick Massot (Jun 04 2018 at 13:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20file%20organization/near/127540045):
<p>It also seems they keep the definitions and lemmas in the same file</p>

#### [ Patrick Massot (Jun 04 2018 at 13:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20file%20organization/near/127540048):
<p><span class="user-mention" data-user-id="110172">@Assia Mahboubi</span> will probably tell us much more</p>

#### [ Assia Mahboubi (Jun 04 2018 at 13:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20file%20organization/near/127540809):
<p>Hi <span class="user-mention" data-user-id="110031">@Patrick Massot</span> . I read the thread briefly, so I might have missed the point of the debate. I do not see the advantage of having definitions and theorems in separated files. Sometimes, the difference between a definition and a theorem is quite thin. Also, what makes me believe that an object in the library is what I am looking for is not only its name (and not even only its definition) but also the companion lemmas, examples, etc.  So it would not ease my inspection. Last, the definition of a list in Lean is probably no going to change, but for more complex objects, definitions often evolve during the course of the development. "Testing" the subsequent impact of the changes on notations, lemmas, theorem, etc. is easier if this content is not too far I would say. However, part of the answer might be of a technological nature. Even if I am flatted that people like <span class="user-mention" data-user-id="110031">@Patrick Massot</span> want to hear from my experience, you Lean people might benefit from tools that change the game.</p>

#### [ Sebastian Ullrich (Jun 04 2018 at 14:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20file%20organization/near/127543190):
<p>One more argument in favor of not separating definitions and lemmas: You can make uninteresting helper definitions <code>private</code>and still prove things about them</p>

#### [ Sean Leather (Jun 04 2018 at 14:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20file%20organization/near/127543249):
<p>That's really only an argument for not separating <em>those</em> definitions. <span class="emoji emoji-1f609" title="wink">:wink:</span> (But it is a fine argument in any case.)</p>


{% endraw %}
