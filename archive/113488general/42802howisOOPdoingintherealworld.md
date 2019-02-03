---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/42802howisOOPdoingintherealworld.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [how is OOP doing in the "real world"](https://leanprover-community.github.io/archive/113488general/42802howisOOPdoingintherealworld.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Adam Kurkiewicz (Apr 06 2018 at 16:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20is%20OOP%20doing%20in%20the%20%22real%20world%22/near/124721653):
<p><span class="user-mention" data-user-id="110027">@Moses Schönfinkel</span>  <span class="user-mention" data-user-id="110031">@Patrick Massot</span> <span class="user-mention" data-user-id="110038">@Kevin Buzzard</span> </p>
<p>I've had a reality check in the "real world" (Skyscanner, a tech company, ~1000 software engineers, customer-facing money-making product).</p>
<p>Here are the results:</p>
<p><a href="/user_uploads/3121/oK3TnPBrE_YOK6kzMEc3UCez/Screen-Shot-2018-04-06-at-3.02.37-PM.png" target="_blank" title="Screen-Shot-2018-04-06-at-3.02.37-PM.png">Screen-Shot-2018-04-06-at-3.02.37-PM.png</a></p>
<div class="message_inline_image"><a href="/user_uploads/3121/oK3TnPBrE_YOK6kzMEc3UCez/Screen-Shot-2018-04-06-at-3.02.37-PM.png" target="_blank" title="Screen-Shot-2018-04-06-at-3.02.37-PM.png"><img src="/user_uploads/3121/oK3TnPBrE_YOK6kzMEc3UCez/Screen-Shot-2018-04-06-at-3.02.37-PM.png"></a></div><p>There was an interesting discussion in the thread, some highlights:</p>
<blockquote>
<p>Basically the whole “tom is a type of cat is a type of animal”-style OO has (rightfully) disappeared</p>
<p>If you look at a sensible java/python codebase it doesn’t look so different from the structure of a c/rust/go program</p>
<p>I agree it's a change of mindset. I don't think OO is necessarily less used - but I think it's less often considered The Way to program. More people recognize that it's a tool that has its pros and cons.</p>
</blockquote>
<p>Code-wise there's of course a lot of C#/python/java in the company (Skyscanner is historically a .net shop, there is still some ancient VB code running in production), and sadly not very much FP, although I know a few data scientists writing scala code (not sure if that counts as "real" FP), and certainly one python code base makes heavy use of <code>functools</code>. I don't think we have any Haskell whatsoever (could be wrong though, it's a big company!), but I could see it happening in a couple of years.</p>

#### [ Adam Kurkiewicz (Apr 06 2018 at 16:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20is%20OOP%20doing%20in%20the%20%22real%20world%22/near/124722331):
<p>Incidentally, the only person who said that OOP is growing in popularity is an agile coach, not a software engineer...</p>

#### [ Kevin Buzzard (Apr 06 2018 at 16:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20is%20OOP%20doing%20in%20the%20%22real%20world%22/near/124722412):
<p>Thank you <em>very much</em> for this. My remit on this committee is to decide which programming languages that my university should be teaching mathematics undergraduates, and we want to be strongly influenced by what people who hire mathematicians want to see. I am going to teach them Lean but only as an option; the issue is what we force them to learn.</p>

#### [ Kevin Buzzard (Apr 06 2018 at 16:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20is%20OOP%20doing%20in%20the%20%22real%20world%22/near/124722465):
<p>I am pretty sure, however, that suggesting that they learn functional programming will not go down well. I suspect that many of our graduates end up working for banks / hedge funds rather than tech companies.</p>

#### [ Sebastian Ullrich (Apr 06 2018 at 16:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20is%20OOP%20doing%20in%20the%20%22real%20world%22/near/124722573):
<p>Which may be the only sector with a significant amount of Haskell programmers... :)</p>

#### [ Simon Hudon (Apr 06 2018 at 16:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20is%20OOP%20doing%20in%20the%20%22real%20world%22/near/124722625):
<p>I always find this debate a bit odd. Once you know a few languages, learning one more is not a big deal. Learning how to think about your programs though is not easy and is made much harder once you acquired bad thinking habits. Ideally, you'd like to teach a language that promotes good thinking so that you don't have to spend the whole semester making apologies for the language that you chose.</p>

#### [ Kevin Buzzard (Apr 06 2018 at 16:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20is%20OOP%20doing%20in%20the%20%22real%20world%22/near/124722651):
<p>So you're saying I should choose...what? Erlang? ;-)</p>

#### [ Simon Hudon (Apr 06 2018 at 16:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20is%20OOP%20doing%20in%20the%20%22real%20world%22/near/124722657):
<p>In short, is your goal to teach how to use a specific programming language or how to build a certain class of programs or how to program in general?</p>

#### [ Simon Hudon (Apr 06 2018 at 16:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20is%20OOP%20doing%20in%20the%20%22real%20world%22/near/124722723):
<p>I think a case can be made for Erlang. Especially if you teach distributed systems. My personal number one choice is of course Haskell but it also has drawbacks in educational contexts</p>

#### [ Simon Hudon (Apr 06 2018 at 16:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20is%20OOP%20doing%20in%20the%20%22real%20world%22/near/124722777):
<p>Maybe I should switch my <a href="https://github.com/leanprover/lean/issues/1" target="_blank" title="https://github.com/leanprover/lean/issues/1">#1</a> choice to Lean. I don't know if I want to do the paper work though <span class="emoji emoji-1f61c" title="stuck out tongue winking eye">:stuck_out_tongue_winking_eye:</span></p>

#### [ Simon Hudon (Apr 06 2018 at 16:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20is%20OOP%20doing%20in%20the%20%22real%20world%22/near/124722804):
<p>I think OCaml can be a good choice. If you have to teach object oriented programming, I like Eiffel a lot. The tools are not the best though</p>

#### [ Simon Hudon (Apr 06 2018 at 17:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20is%20OOP%20doing%20in%20the%20%22real%20world%22/near/124722815):
<p><span class="user-mention" data-user-id="110024">@Sebastian Ullrich</span> For imperative programming, would you recommend teaching Rust?</p>

#### [ Sebastian Ullrich (Apr 06 2018 at 17:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20is%20OOP%20doing%20in%20the%20%22real%20world%22/near/124722886):
<p>No, I really don't think that would be a good idea. The learning curve is way too steep.</p>

#### [ Simon Hudon (Apr 06 2018 at 17:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20is%20OOP%20doing%20in%20the%20%22real%20world%22/near/124722909):
<p>What would you recommend?</p>

#### [ Simon Hudon (Apr 06 2018 at 17:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20is%20OOP%20doing%20in%20the%20%22real%20world%22/near/124722968):
<p>Also, is it steeper than Haskell?</p>

#### [ Sebastian Ullrich (Apr 06 2018 at 17:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20is%20OOP%20doing%20in%20the%20%22real%20world%22/near/124722987):
<p>I don't know. We're teaching... Java, still. Well, our group is teaching Haskell and Prolog, but that's at the end of the bachelor's program</p>

#### [ Simon Hudon (Apr 06 2018 at 17:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20is%20OOP%20doing%20in%20the%20%22real%20world%22/near/124723047):
<p>The big problem with teaching Haskell early is that the execution model is hard to grasp so you'd have to wait a few semesters to understand why your programs are slow</p>

#### [ Sebastian Ullrich (Apr 06 2018 at 17:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20is%20OOP%20doing%20in%20the%20%22real%20world%22/near/124723141):
<p>Yes, I'd say it's steeper than Haskell. I feel like with Haskell you can start by using it as "executable math" and worry about things like laziness and monads later. In Rust, you can't do anything useful without understanding references and lifetimes first.</p>

#### [ Sebastian Ullrich (Apr 06 2018 at 17:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20is%20OOP%20doing%20in%20the%20%22real%20world%22/near/124723155):
<p>You also really need the background of knowing other languages to appreciate the things Rust does differently</p>

#### [ Simon Hudon (Apr 06 2018 at 17:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20is%20OOP%20doing%20in%20the%20%22real%20world%22/near/124723362):
<p>I was thinking about that recently, especially with regards to types. I was wondering if you should learn JavaScript before learning Haskell to appreciate how amazing the types are. And then I started wondering, should we do that for every useful invention in the history of programming languages?</p>

#### [ Adam Kurkiewicz (Apr 06 2018 at 17:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20is%20OOP%20doing%20in%20the%20%22real%20world%22/near/124723374):
<p>I very much agree with this:</p>
<blockquote>
<p>I always find this debate a bit odd. Once you know a few languages, learning one more is not a big deal. Learning how to think about your programs though is not easy and is made much harder once you acquired bad thinking habits </p>
</blockquote>
<p>And that's precisely the reason why I think teaching "java OOP" or "python OOP" to novices is a bad idea. You can spend <strong>ages</strong> going through language-specific minutiae (mixins, multiple inheritance, generics, type erasure, etc.) without teaching things, which are more important (problem-solving, structuring programs, unit-testing, correctness).</p>

#### [ Adam Kurkiewicz (Apr 06 2018 at 17:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20is%20OOP%20doing%20in%20the%20%22real%20world%22/near/124723941):
<p>I was listening to Simon Peyton Jones' talk in Canterbury last week, which was on high school CS education, and he said something along the lines (I'm paraphrasing): "It's good that the government recognises that we should teach programming in high schools, but what I'm afraid is going to happen is that we will just teach Python". His point was, again, that there is much more to computer science than programming in any specific language (<code>sorted([2, 3, 1])</code> for example sorts a list in Python, but that fact is entirely educationally useless).</p>
<p>At UoG we cover Python in the first year, but without going too deep into the language, focusing mostly on problem-solving and applications. We do cover all the minutiae of java OOP in the second year, just because we're training future software engineers (and because we have 4 years to produce a graduate in Scotland). But we never cover all the minutiae of Python OOP, since that wouldn't be very educational (students can learn themselves if/when they need it).</p>

#### [ Moses Schönfinkel (Apr 06 2018 at 17:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20is%20OOP%20doing%20in%20the%20%22real%20world%22/near/124724294):
<p>We teach C to the first years, sadly :). Then Java and then Haskell.</p>

#### [ Simon Hudon (Apr 06 2018 at 17:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20is%20OOP%20doing%20in%20the%20%22real%20world%22/near/124724351):
<blockquote>
<p>Just because we're training future software engineers </p>
</blockquote>
<p>Do you mean by that that you want your graduates to know one common language in depth by the time they graduate so that they're ready to start their likely first job?</p>

#### [ Adam Kurkiewicz (Apr 06 2018 at 17:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20is%20OOP%20doing%20in%20the%20%22real%20world%22/near/124724370):
<p>My specific advise for <span class="user-mention" data-user-id="110038">@Kevin Buzzard</span> on language choice would be: "don't". Jump through any political fences you'll have to jump through and put together a course with your CS department, following their lead on language choice, and working together on curriculum specifics.</p>
<p>The benefits would be enormous:<br>
1. You don't get an outsider to teach the subject. For a student nothing feels worse than a lecturer who doesn't really understand/ like the subject they're teaching.<br>
2. You pave way for increased collaboration with the CS department. CS and maths really need one another. Don't know what the situation is at ICL, but in Glasgow we definitely don't have enough maths-CS collaboration, and it's not just my view, I've discussed this a few times with Muffy Calder for example.</p>

#### [ Adam Kurkiewicz (Apr 06 2018 at 17:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20is%20OOP%20doing%20in%20the%20%22real%20world%22/near/124724585):
<p><span class="user-mention" data-user-id="110026">@Simon Hudon</span> I think that's more or less it. The pressure from the top is that our graduates should be "industry-ready" by 3rd year (Glasgow is <strong>very</strong> industry-focused, unlike for example Edinburgh, who get away with teaching Haskell to first years and Coq later in the course), and I imagine knowing one language in-depth is considered part of that "readiness". We do some cool stuff in the 4th year (FP, Constraints Programming, AI), and it's much more "bottom-up" with 4th year modules.</p>

#### [ Simon Hudon (Apr 06 2018 at 17:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20is%20OOP%20doing%20in%20the%20%22real%20world%22/near/124724692):
<p>That's interesting, I didn't know about Edinburgh. Do you have any comparison about how well their graduates do on the job market? Or whether more of their students go to grad school?</p>

#### [ Simon Hudon (Apr 06 2018 at 17:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20is%20OOP%20doing%20in%20the%20%22real%20world%22/near/124724978):
<p>At YorkU, our engineering school is pretty young and we're only now getting started with a software engineering degree. My supervisor was the one  behind the push and we caught some flak when the time came for accreditation because too much attention was paid to formal specification. One of the guys doing the accreditation was an agile methodologist</p>

#### [ Simon Hudon (Apr 06 2018 at 17:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20is%20OOP%20doing%20in%20the%20%22real%20world%22/near/124724997):
<p>The funny thing is that I think less and less that the two are in opposition. I feel like the way I use Haskell and Lean is pretty agile / hacker-ish</p>

#### [ Adam Kurkiewicz (Apr 06 2018 at 18:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20is%20OOP%20doing%20in%20the%20%22real%20world%22/near/124725983):
<p>Sure, there is this website called UNISTATS, it uses data from "Destination of Leavers from Higher Education (DLHE)". Not sure if the links will work, but you should be able to search for Computing Science degrees from multiple universities:</p>
<p>1. <a href="https://unistats.ac.uk/subjects/employment/10007794FT-G400-2208/ReturnTo/Search" target="_blank" title="https://unistats.ac.uk/subjects/employment/10007794FT-G400-2208/ReturnTo/Search">https://unistats.ac.uk/subjects/employment/10007794FT-G400-2208/ReturnTo/Search</a><br>
2. <a href="https://unistats.ac.uk/subjects/employment/10007790FT-UTCMPSIBENGH/ReturnTo/Search" target="_blank" title="https://unistats.ac.uk/subjects/employment/10007790FT-UTCMPSIBENGH/ReturnTo/Search">https://unistats.ac.uk/subjects/employment/10007790FT-UTCMPSIBENGH/ReturnTo/Search</a></p>
<p>The results are quite counter-intuitive. It appears that Edinburgh has slightly higher employment rate, and actually more industry employment and less further study.</p>
<p>Maybe students from Edinburgh are like "Enough of this theoretical nonsense, I want to do something real for a change" :D.</p>
<p>Also, the data is almost certainly skewed by JPMorgan. It's the biggest CS employer in Glasgow, easily 30-40% of our graduates go into JP, and they get a good starting salary of 32k or so, which I think is the reason why Glasgow graduates earn better money than Edinburgh.</p>

#### [ Simon Hudon (Apr 06 2018 at 18:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20is%20OOP%20doing%20in%20the%20%22real%20world%22/near/124726089):
<p>Yeah, it's certainly hard to attribute a cause when the cities are not identical. I'd be tempted to say that students from Edinburgh are better equipped for understanding their programs.</p>

#### [ Simon Hudon (Apr 06 2018 at 18:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20is%20OOP%20doing%20in%20the%20%22real%20world%22/near/124726091):
<p>Thanks for the stats</p>

#### [ Simon Hudon (Apr 06 2018 at 18:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20is%20OOP%20doing%20in%20the%20%22real%20world%22/near/124726171):
<p>I was organizing a CS competition to pit various North American universities against each other. I personally studied in Sherbrooke QC which is more industry focused and Montreal (UdeM to be exact) has a lot of theory and math. As I recall, Montreal beat the pants off of everybody there</p>

#### [ Simon Hudon (Apr 06 2018 at 18:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20is%20OOP%20doing%20in%20the%20%22real%20world%22/near/124726182):
<p>Lucky for me, I went in not wearing pants</p>

#### [ Adam Kurkiewicz (Apr 06 2018 at 18:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20is%20OOP%20doing%20in%20the%20%22real%20world%22/near/124726921):
<p><span class="user-mention" data-user-id="110038">@Kevin Buzzard</span> sadly, the DLHE data can't settle the "hedge fund" vs "tech company" question. The data is not fine-grained enough, with only a very broad category of "Business and public service associate professionals", which is where 65% Mathematics ICL undergraduates land 6-months after their degree: <a href="https://unistats.ac.uk/subjects/employment/10003270FT-G100/ReturnTo/Search" target="_blank" title="https://unistats.ac.uk/subjects/employment/10003270FT-G100/ReturnTo/Search">https://unistats.ac.uk/subjects/employment/10003270FT-G100/ReturnTo/Search</a></p>
<p>Also, the data is 6 months post-graduation, what would be also nice to see is data ~5 years post-graduation, but I'm not sure if it exists.</p>
<p>Anecdotally I know of 1 mathematician in Skyscanner, doing great, and 2 mathematicians at UoG CS, both doing great, but that's not too scientific I'm afraid :/</p>

#### [ Simon Hudon (Apr 06 2018 at 19:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20is%20OOP%20doing%20in%20the%20%22real%20world%22/near/124727742):
<p>That's still interesting. Anecdotally, my supervisor and I get a lot criticism about the way we run our software design class both by the faculty and the students taking but he has the experience that, 5  years down the line, students come back to thank him because it has finally made sense to them and they find our material useful</p>

#### [ Adam Kurkiewicz (Apr 06 2018 at 19:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20is%20OOP%20doing%20in%20the%20%22real%20world%22/near/124729026):
<p>Personally, if I could go back 10 years in time, I would have advised my young and foolish self to consider going to Edinburgh. Although I did switch my main degree to JH in maths + CS at Glasgow, which worked quite well in the end.  A fun fact: my wife got unconditional from Edinburgh, but she didn't go because none of her friends went. So I would have to find her too and advise her the same, or we wouldn't have met otherwise :D</p>

#### [ Patrick Massot (Apr 08 2018 at 09:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20is%20OOP%20doing%20in%20the%20%22real%20world%22/near/124790875):
<blockquote>
<p>My specific advise for <span class="user-mention" data-user-id="110038">@Kevin Buzzard</span> on language choice would be: "don't". Jump through any political fences you'll have to jump through and put together a course with your CS department, following their lead on language choice, and working together on curriculum specifics.</p>
</blockquote>
<p>I'm back from Köln (where I learned interesting stuff about Kevin's youth) and I can only contribute the following advice to Kevin: read the above quote thinking about what you would get if you ask a hardcore (∞, 1)-category theorist what should be taught in mathematics for biology course. And then do the reasonable thing.</p>

#### [ Patrick Massot (Apr 08 2018 at 09:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20is%20OOP%20doing%20in%20the%20%22real%20world%22/near/124790919):
<p>That being said, I don't think you should teach python MRO in first year. There much to learn before that and, by the time you really need this, you can learn alone</p>

#### [ Patrick Massot (Apr 08 2018 at 09:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20is%20OOP%20doing%20in%20the%20%22real%20world%22/near/124790925):
<p>I don't believe in teaching programming without using a programming language (like I don't believe in teaching category theory before linear algebra and elementary group theory)</p>

#### [ Patrick Massot (Apr 08 2018 at 09:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20is%20OOP%20doing%20in%20the%20%22real%20world%22/near/124790926):
<p>So you need to choose a language. Why not going with something fun and actually used?</p>

#### [ Patrick Massot (Apr 08 2018 at 09:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20is%20OOP%20doing%20in%20the%20%22real%20world%22/near/124790927):
<p>This only reason would be duck typing can encourage confused reasonning</p>

#### [ Patrick Massot (Apr 08 2018 at 09:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20is%20OOP%20doing%20in%20the%20%22real%20world%22/near/124790966):
<p>But then you also have your Lean course</p>

#### [ Patrick Massot (Apr 08 2018 at 09:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20is%20OOP%20doing%20in%20the%20%22real%20world%22/near/124790967):
<p>Teaching rigorous thinking</p>

#### [ Patrick Massot (Apr 08 2018 at 09:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20is%20OOP%20doing%20in%20the%20%22real%20world%22/near/124791063):
<p>Also I really have a hard time imagining functional programming scaling to real world programming but I'd love to learn I'm wrong (I read a book on Haskell recently and it only seemed to be about solving problems created by the functional paradigm). My experience in real world is that you quickly get tired of adding millions of arguments to functions in order to get flexibility. Compare with the beginning of <a href="https://docs.djangoproject.com/fr/2.0/topics/class-based-views/intro/" target="_blank" title="https://docs.djangoproject.com/fr/2.0/topics/class-based-views/intro/">https://docs.djangoproject.com/fr/2.0/topics/class-based-views/intro/</a> for instance. But again this is only my amateur end-user view-point, I'm neither a computer scientist nor a professional programmer.</p>

#### [ Adam Kurkiewicz (Apr 08 2018 at 13:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20is%20OOP%20doing%20in%20the%20%22real%20world%22/near/124796204):
<p>Re "real world" haskell usage: <a href="https://code.facebook.com/posts/745068642270222/fighting-spam-with-haskell/" target="_blank" title="https://code.facebook.com/posts/745068642270222/fighting-spam-with-haskell/">https://code.facebook.com/posts/745068642270222/fighting-spam-with-haskell/</a></p>
<p>Re (∞, 1)-category theorist -- not sure what ICL compsi looks like, but at Glasgow we have plenty of down-to-earth engineering-type people I would trust to do a decent job with co-teaching such course. That being said we have of course a fair share of "(∞, 1)-category theorists", so it's definitely something to be wary of.</p>

#### [ Moses Schönfinkel (Apr 08 2018 at 13:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20is%20OOP%20doing%20in%20the%20%22real%20world%22/near/124796349):
<p>There are definitely examples of people using Haskell for real world stuff but OOP is in overwhelming majority. (Disclaimer: I hate OOP and I write functional exclusively except for when I teach where I am coerced to do Java :(.)</p>

#### [ Adam Kurkiewicz (Apr 08 2018 at 13:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20is%20OOP%20doing%20in%20the%20%22real%20world%22/near/124796704):
<p>No disagreement that popularity(OOP) &gt; popularity(FP).</p>
<p>But if we look at the derivative...</p>
<p>The sentiment in industry (or certainly the slice of industry I'm a part of) is that there is a swing from "rich OOP" (Tom is a Cat is an Animal or SimpleBeanFactoryAwareAspectInstanceFactory), back to more readable procedural/ imperative style. FP is still a bit in the shadows unfortunately, but pace of change in software engineering is very quick. I wouldn't be surprised if we saw internal Haskell products popping up in  major tech companies few years down the line.</p>

#### [ Kevin Buzzard (Apr 08 2018 at 13:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20is%20OOP%20doing%20in%20the%20%22real%20world%22/near/124796750):
<p>I guess I am interested in these derivatives as well as popularity, but I guess I am only interested in the industries that are hiring mathematicians.</p>

#### [ Kevin Buzzard (Apr 08 2018 at 13:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20is%20OOP%20doing%20in%20the%20%22real%20world%22/near/124796751):
<p>(and then I am only interested in what they want the mathematicians to do)</p>

#### [ Adam Kurkiewicz (Apr 08 2018 at 14:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20is%20OOP%20doing%20in%20the%20%22real%20world%22/near/124797318):
<p>I'm afraid you'll have to search more then. I have only 5 mathematicians doing non-mathematics in my professional network, 2.5 of them all seem to be doing what everybody else is doing (writing software, teaching web-dev, writing Integer Programming models, managing software developers), 2.5 of them work at the edge of pure maths/CS (i.e. proving theorems, not writing code).</p>

#### [ Kevin Buzzard (Apr 08 2018 at 14:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20is%20OOP%20doing%20in%20the%20%22real%20world%22/near/124797731):
<p>What languages are the 2.5 writing software using?</p>

#### [ Kevin Buzzard (Apr 08 2018 at 14:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20is%20OOP%20doing%20in%20the%20%22real%20world%22/near/124797732):
<p>Maybe that's not the right question.</p>

#### [ Kevin Buzzard (Apr 08 2018 at 14:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20is%20OOP%20doing%20in%20the%20%22real%20world%22/near/124797734):
<p>Maybe I should just note that they are writing software</p>

#### [ Adam Kurkiewicz (Apr 08 2018 at 14:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20is%20OOP%20doing%20in%20the%20%22real%20world%22/near/124797780):
<p>python, python, java. Certainly not. I will have  a lot people writing python in my professional network :)</p>

#### [ Adam Kurkiewicz (Apr 08 2018 at 14:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20is%20OOP%20doing%20in%20the%20%22real%20world%22/near/124797894):
<p>Likewise, I will have  a lot of people writing software in my professional network. I think this is called Prosecutor's Fallacy or something like that.</p>

#### [ Adam Kurkiewicz (Apr 08 2018 at 14:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20is%20OOP%20doing%20in%20the%20%22real%20world%22/near/124797942):
<p>What you need is better DLHE data. As it is DLHE is just too coarse: <a href="https://unistats.ac.uk/subjects/employment/10003270FT-G100/ReturnTo/Search" target="_blank" title="https://unistats.ac.uk/subjects/employment/10003270FT-G100/ReturnTo/Search">https://unistats.ac.uk/subjects/employment/10003270FT-G100/ReturnTo/Search</a></p>


{% endraw %}
