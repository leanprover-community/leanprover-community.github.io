---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/50044nearlynoconfusion.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [nearly no_confusion](https://leanprover-community.github.io/archive/113488general/50044nearlynoconfusion.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Kevin Buzzard (Mar 24 2018 at 00:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nearly%20no_confusion/near/124130895):
<p>I spent some time with Chris at Xena last night trying to get to the bottom of <code>no_confusion</code>.  I seem to have a slightly simpler approach which gives what looks to me like everything we need for a proof of the idea that two nats are equal iff they were constructed using the same constructors in the same order.</p>

#### [ Kevin Buzzard (Mar 24 2018 at 00:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nearly%20no_confusion/near/124130903):
<div class="codehilite"><pre><span></span>inductive  xnat
| zero : xnat
| succ : xnat → xnat

open xnat

def  xnat_no_confusion_prop (s : xnat) (t : xnat) : Prop  :=
xnat.rec (xnat.rec true (λ _ _,false) t) (λ m _,(xnat.rec false (λ n _,(m=n)) t)) s

variables m n : xnat
#reduce xnat_no_confusion_prop zero zero -- true
#reduce xnat_no_confusion_prop (succ m) zero -- false
#reduce xnat_no_confusion_prop zero (succ n) -- false
#reduce xnat_no_confusion_prop (succ m) (succ n) -- (m = n)

def  xnat_no_confusion&#39; (s t : xnat) (H : s = t) : xnat_no_confusion_prop s t :=
begin
rw H,
cases t with n,
exact trivial, -- t = 0
show (n=n), -- t = succ n
refl,
end

example : succ m = succ n → m = n :=  λ H, xnat_no_confusion&#39; _ _ H
example : ¬ succ m = zero :=  λ H, xnat_no_confusion&#39; _ _ H
 ```
</pre></div>

#### [ Kevin Buzzard (Mar 24 2018 at 00:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nearly%20no_confusion/near/124130959):
<p>Here I prove injectivity of <code>xnat.succ</code> and also that <code>zero</code> is not a <code>succ</code> using an easier variant of the <code>no_confusion</code> / <code>no_confusion_type</code> strategy, where instead of carrying round a general sort <code>P</code> I just use the relevant props.</p>

#### [ Kevin Buzzard (Mar 24 2018 at 00:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nearly%20no_confusion/near/124130970):
<p>Are there other applications of <code>no_confusion_type</code> lemmas which go beyond this sort of "instance of inductive type is uniquely determined by how it was constructed" sort of thing? Or am I missing something else? Why is this sort <code>P</code> used?</p>

#### [ Kevin Buzzard (Mar 24 2018 at 00:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nearly%20no_confusion/near/124131025):
<p>I'm writing a blog post about all this <code>no_confusion</code> stuff and I was somehow expecting for this to come out in the wash but it didn't, so I need to think of something coherent to say about why the general sort P is involved before I post.</p>

#### [ Andrew Ashworth (Mar 24 2018 at 00:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nearly%20no_confusion/near/124131971):
<p>was mcbride's paper on <code>no confusion</code> not helpful?</p>

#### [ Kevin Buzzard (Mar 24 2018 at 00:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nearly%20no_confusion/near/124132023):
<p>I either don't know this paper, or I looked at it before and at the time it was too much for me. Having actually spent some time thinking about no_confusion_type now perhaps I can ask you for a link to this paper in the hope that I can get something from it?</p>

#### [ Andrew Ashworth (Mar 24 2018 at 00:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nearly%20no_confusion/near/124132027):
<p><a href="https://pdfs.semanticscholar.org/d224/e96c59a81a471625faf87118b6299094e1e4.pdf" target="_blank" title="https://pdfs.semanticscholar.org/d224/e96c59a81a471625faf87118b6299094e1e4.pdf">https://pdfs.semanticscholar.org/d224/e96c59a81a471625faf87118b6299094e1e4.pdf</a> section 7.3</p>

#### [ Andrew Ashworth (Mar 24 2018 at 00:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nearly%20no_confusion/near/124132032):
<p><a href="http://strictlypositive.org/thesis.pdf" target="_blank" title="http://strictlypositive.org/thesis.pdf">http://strictlypositive.org/thesis.pdf</a> page 136</p>

#### [ Andrew Ashworth (Mar 24 2018 at 01:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nearly%20no_confusion/near/124132207):
<p>mcbride's phd thesis is definitely hard going</p>

#### [ Andrew Ashworth (Mar 24 2018 at 01:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nearly%20no_confusion/near/124132233):
<p>i had to sit and stare at it for awhile, and i still don't fully understand it <span class="emoji emoji-1f605" title="sweat smile">:sweat_smile:</span></p>

#### [ Kevin Buzzard (Mar 24 2018 at 01:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nearly%20no_confusion/near/124132336):
<p>Well I am not an expert but it seems to me that what McBride is defining on p136ff is what is implemented in Lean.</p>

#### [ Kevin Buzzard (Mar 24 2018 at 01:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nearly%20no_confusion/near/124132337):
<p>Maybe I should just post my blog post. Hang on.</p>

#### [ Mario Carneiro (Mar 24 2018 at 01:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nearly%20no_confusion/near/124132589):
<p>I think the reason <code>no_confusion</code> uses a general sort instead of using the consequent <code>m = n</code> directly is because the number of conclusions varies with the constructors, so that for <code>list</code> it would be something like <code>cons a l = cons a' l' -&gt; a = a' /\ l = l'</code>, which is a bit less natural to define inductively since the 0-ary case gets special consideration, and it also relies on the definition <code>and</code> which may not be available yet. As it is defined normally <code>no_confusion</code> for an arbitrary type needs nothing except the basics of DTT, plus <code>eq</code> and <code>heq</code> (which comes up when there are dependencies, for example <code>sigma.mk a b = sigma.mk a' b' -&gt; a = a' /\ b == b'</code> where the latter equality involves <code>b : B a</code> and <code>b' : B a'</code> which are different types.</p>

#### [ Kevin Buzzard (Mar 24 2018 at 01:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nearly%20no_confusion/near/124132771):
<p><a href="https://xenaproject.wordpress.com/2018/03/24/no-confusion-over-no_confusion/" target="_blank" title="https://xenaproject.wordpress.com/2018/03/24/no-confusion-over-no_confusion/">https://xenaproject.wordpress.com/2018/03/24/no-confusion-over-no_confusion/</a></p>

#### [ Kevin Buzzard (Mar 24 2018 at 01:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nearly%20no_confusion/near/124132788):
<p>I'll perhaps add some comments about what you said above, later.</p>

#### [ Mario Carneiro (Mar 24 2018 at 01:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nearly%20no_confusion/near/124133073):
<p>Here's another interesting story to do with no_confusion:</p>
<div class="codehilite"><pre><span></span>inductive {u} mystery : Sort u
| A : mystery
| B : mystery

def confused : Type := mystery
def confused.A : confused := mystery.A
def confused.B : confused := mystery.B
open confused

theorem A_ne_B_attempt_1 : A ≠ B :=
λ h, mystery.no_confusion h --fails: no_confusion not defined

theorem A_ne_B_attempt_2 : A ≠ B :=
λ h, by cases h -- now I have to prove ⊢ false?

theorem A_ne_B_attempt_3.no_confusion_type : mystery → mystery → Type
| mystery.A mystery.A := _ -- already fails, can&#39;t case on mystery
| mystery.B mystery.A := _
| mystery.A mystery.B := _
| mystery.A mystery.B := _

#print mystery.rec
-- protected eliminator tc.mystery.rec : ∀ {C : mystery → Prop},
-- C mystery.A → C mystery.B → ∀ (n : mystery), C n
--
-- Hm, the recursor only eliminates to Prop, so we can&#39;t
-- define functions like no_confusion_type

-- Maybe we can prove they are equal instead? If it was a Prop
-- they would be equal by proof irrelevance...
theorem A_eq_B_attempt_1 : A = B := rfl --nope
</pre></div>

#### [ Mario Carneiro (Mar 24 2018 at 01:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nearly%20no_confusion/near/124133116):
<p>The punch line is that <code>confused</code> is a type with two elements <code>A</code> and <code>B</code>, for which it is impossible to prove whether they are equal or not</p>

#### [ Mario Carneiro (Mar 24 2018 at 01:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nearly%20no_confusion/near/124133271):
<p>By the way in the blog post you could have defined <code>mytype_equal</code> like so:</p>
<div class="codehilite"><pre><span></span>def  mytype_equal : mytype → mytype →  Prop
| mytype.AA mytype.AA := true
| mytype.AA mytype.ZZ := false
| mytype.ZZ mytype.AA := false
| mytype.ZZ mytype.ZZ := true
</pre></div>


<p>Not sure if you were deliberately showing off other ways to construct it</p>

#### [ Mario Carneiro (Mar 24 2018 at 01:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nearly%20no_confusion/near/124133419):
<p>Re: the one-sided inverse, that approach actually does work in general, as a "partial projection". So for example you could define <code>head l : option A</code> when <code>l : list A</code>, to return <code>none</code> on the empty list and <code>a</code> on <code>a::l</code>. In general, you have an inductive type with several constructors, each of which has several arguments, and you can project each element of each constructor in an <code>option</code>, returning <code>none</code> if the wrong constructor is passed in and <code>some a</code> where <code>a</code> is the appropriate argument to the constructor otherwise. You can reconstruct the <code>cases_on</code> theorem using all these projections.</p>

#### [ Kevin Buzzard (Mar 24 2018 at 02:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nearly%20no_confusion/near/124133808):
<p>Aah excellent, I will beef up the post tomorrow</p>

#### [ Kevin Buzzard (Mar 24 2018 at 02:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nearly%20no_confusion/near/124133809):
<p>Thanks!</p>

#### [ Kevin Buzzard (Mar 24 2018 at 17:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nearly%20no_confusion/near/124155749):
<p>PS Do you think I'm wasting my time trying to get to the bottom of things like this? I am currently thinking about getting to the bottom of something else I've always been confused by -- "using-well-founded" (the error you get when you try and define something by recursion but things are slightly too convoluted for the elaborator(?) to figure out that what you're doing will definitely terminate after a finite time). Currently the only way I know how to figure stuff out is to look at the source code and then work stuff out by experimenting. My plan, like the no-confusion post, would be to work out some simple examples, and basically write some docs and either PR them to mathlib docs or blog about them. But when Lean 4 comes is there every chance that everything I write about these sorts of "obscure" parts of Lean will be no longer relevant?</p>

#### [ Kevin Buzzard (Mar 24 2018 at 17:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nearly%20no_confusion/near/124155850):
<p>I think I'm right in saying that using_well_founded is not mentioned in either the reference manual or TPIL (like no_confusion).</p>

#### [ Kevin Buzzard (Mar 24 2018 at 17:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nearly%20no_confusion/near/124156198):
<p>Re : <code>mystery</code> -- why is it any different to <code>bool</code>? It clearly is:</p>

#### [ Kevin Buzzard (Mar 24 2018 at 17:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nearly%20no_confusion/near/124156199):
<div class="codehilite"><pre><span></span>inductive {u} mystery : Sort u
| A : mystery
| B : mystery

#print  prefix mystery

inductive  bool&#39;
| TT : bool&#39;
| FF : bool&#39;

#print  prefix bool&#39;
</pre></div>

#### [ Kevin Buzzard (Mar 24 2018 at 17:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nearly%20no_confusion/near/124156251):
<p>we get <code>bool'.no_confusion</code> but no <code>mystery.no_confusion</code>; and <code>bool.rec</code> eliminates to any Sort whereas <code>mystery.rec</code> only eliminates to <code>Prop</code>. Why is this?</p>

#### [ Simon Hudon (Mar 24 2018 at 17:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nearly%20no_confusion/near/124156307):
<p>Because <code>mystery</code> can inhabit multiple types including <code>Prop</code> and when it does, it's a bit like <code>or</code>. If you could eliminate to anything other than <code>Prop</code>, you could affect the behavior of a program with just a proof</p>

#### [ Simon Hudon (Mar 24 2018 at 17:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nearly%20no_confusion/near/124156364):
<p>for example:</p>
<div class="codehilite"><pre><span></span>def prog : mystery.{0} -&gt; nat
 | A := 0
 | B := 1
</pre></div>


<p>wouldn't make sense because of proof irrelevance</p>

#### [ Kevin Buzzard (Mar 24 2018 at 18:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nearly%20no_confusion/near/124156746):
<p>I see. The whole point is that mystery is allowed to be a Prop so everything is paranoid. You guys should get classical.</p>

#### [ Andrew Ashworth (Mar 24 2018 at 18:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nearly%20no_confusion/near/124156753):
<p>it's not a waste of time. some version of well-founded recursion will be in lean 4</p>

#### [ Andrew Ashworth (Mar 24 2018 at 18:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nearly%20no_confusion/near/124156755):
<p>what might change is the exact syntax / <code>using_well_founded</code>, so perhaps you could discuss doing it manually using <code>well_founded.fix</code></p>

#### [ Kevin Buzzard (Mar 24 2018 at 18:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nearly%20no_confusion/near/124156804):
<p>I know even less about <code>well_founded.fix</code>.</p>

#### [ Andrew Ashworth (Mar 24 2018 at 18:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nearly%20no_confusion/near/124156818):
<p>i don't know much either about the fixed points of functions, so i would avidly read your blog post :)</p>

#### [ Andrew Ashworth (Mar 24 2018 at 18:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nearly%20no_confusion/near/124156820):
<p>it's a way of expressing well-founded induction</p>

#### [ Kevin Buzzard (Mar 24 2018 at 18:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nearly%20no_confusion/near/124156821):
<p>You should use Coq, everything seems to be defined using Fixpoint there.</p>

#### [ Kevin Buzzard (Mar 24 2018 at 18:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nearly%20no_confusion/near/124156862):
<p>Hey, I now realise I don't even understand Lean's definition of nat.div and I am supposed to be a  professor of number theory :-/</p>

#### [ Kevin Buzzard (Mar 24 2018 at 18:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nearly%20no_confusion/near/124156863):
<p>Maybe this was mentioned in TPIL...</p>

#### [ Kevin Buzzard (Mar 24 2018 at 18:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nearly%20no_confusion/near/124156919):
<p>Maybe it's time I read TPIL Chapter 8 again in fact.</p>

#### [ Moses Schönfinkel (Mar 24 2018 at 18:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nearly%20no_confusion/near/124157073):
<p>Coq just uses the keyword <code>Fixpoint</code> to express <code>Definition</code> that can recurse, there's not much difference from Lean's <code>def</code></p>

#### [ Simon Hudon (Mar 24 2018 at 18:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nearly%20no_confusion/near/124157175):
<p>The big difference is that Lean takes care of well founded recursion for you</p>

#### [ Andrew Ashworth (Mar 24 2018 at 18:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nearly%20no_confusion/near/124157269):
<p>regarding the div example in TPIL, I wish jeremy had pattern matched on y, it would have been clearer then IMO</p>

#### [ Moses Schönfinkel (Mar 24 2018 at 18:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nearly%20no_confusion/near/124157270):
<p>Except for when it doesn't and then you're stuck with quoted tactics and such :(.</p>

#### [ Moses Schönfinkel (Mar 24 2018 at 18:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nearly%20no_confusion/near/124157271):
<p>Coq has a better solution to provin gtermination.</p>

#### [ Moses Schönfinkel (Mar 24 2018 at 18:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nearly%20no_confusion/near/124157332):
<p>Not to mention that Coq can in some cases help you show your relation is well founded. Then you're left with proof of termination only.</p>

#### [ Kevin Buzzard (Mar 24 2018 at 18:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nearly%20no_confusion/near/124157333):
<p>Right -- this is what I see with <code>using_well_founded</code> -- I am having to actually write a tactic (or know about the "`[" trick)</p>

#### [ Kevin Buzzard (Mar 24 2018 at 18:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nearly%20no_confusion/near/124157372):
<p>I don't know whether as a mathematician I should care about this</p>

#### [ Kevin Buzzard (Mar 24 2018 at 18:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nearly%20no_confusion/near/124157373):
<p>The reason I currently care is that I have been reading software foundations</p>

#### [ Kevin Buzzard (Mar 24 2018 at 18:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nearly%20no_confusion/near/124157376):
<p>and I defined a positive integer as an inductive type using binary notation: three constructors <code>one</code>, <code>double x</code> and <code>double_and_then_add_one x</code></p>

#### [ Kevin Buzzard (Mar 24 2018 at 18:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nearly%20no_confusion/near/124157377):
<p>and when I tried to define addition on these things, I have trouble doing (2x+1)+(2y+1)</p>

#### [ Simon Hudon (Mar 24 2018 at 18:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nearly%20no_confusion/near/124157440):
<blockquote>
<p>regarding the div example in TPIL, I wish jeremy had pattern matched on y, it would have been clearer then IMO</p>
</blockquote>
<p>A clearer way to present that definition of division can be found:</p>
<p><a href="https://github.com/leanprover/lean/blob/bb9e3ddae2396b574b8ab62976bd4db9520d525d/tests/lean/run/conv_tac1.lean#L8-L13" target="_blank" title="https://github.com/leanprover/lean/blob/bb9e3ddae2396b574b8ab62976bd4db9520d525d/tests/lean/run/conv_tac1.lean#L8-L13">https://github.com/leanprover/lean/blob/bb9e3ddae2396b574b8ab62976bd4db9520d525d/tests/lean/run/conv_tac1.lean#L8-L13</a></p>
<p>I believe <code>nat</code> has access to very little tactic machinery so they have to be frugal there.</p>

#### [ Andrew Ashworth (Mar 24 2018 at 18:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nearly%20no_confusion/near/124157564):
<p>i think it's worth caring about using <code>well_founded.fix</code> by hand, just like <code>no_confusion</code></p>

#### [ Andrew Ashworth (Mar 24 2018 at 18:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nearly%20no_confusion/near/124157565):
<p>it's applicable whenever you're doing complicated induction</p>

#### [ Moses Schönfinkel (Mar 24 2018 at 18:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nearly%20no_confusion/near/124157664):
<p>Coq just asks for proofs of well foundedness and termination (according some decreasing measure).</p>

#### [ Kevin Buzzard (Mar 24 2018 at 18:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nearly%20no_confusion/near/124157665):
<p>Yes, as an end user I forget all about this "what is the actual state of Lean when this object is being made" stuff. For example with no_confusion I was thinking "why not just return a=a' and L=L'" for <code>list.no_confusion_type (a::L) (a'::L')</code></p>

#### [ Moses Schönfinkel (Mar 24 2018 at 18:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nearly%20no_confusion/near/124157666):
<p>Lean has this weird way of requiring tactics.</p>

#### [ Kevin Buzzard (Mar 24 2018 at 18:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nearly%20no_confusion/near/124157667):
<p>and then Mario points out that <code>and</code> might not be defined at this point. Oops.</p>

#### [ Kevin Buzzard (Mar 24 2018 at 18:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nearly%20no_confusion/near/124157672):
<p><span class="user-mention" data-user-id="110027">@Moses Schönfinkel</span> Is it only weird because you are used to the Coq way? i.e. are you saying "I don't like it because I know Coq and Lean is different", or "I don't like it because I know Coq and Lean is worse for this sort of thing"</p>

#### [ Moses Schönfinkel (Mar 24 2018 at 18:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nearly%20no_confusion/near/124157879):
<p>It's worse because you can barely see the state of what you're proving, given it's in a tactic monad. All your feedback is nested exceptions from within the quoted tactics block.</p>

#### [ Moses Schönfinkel (Mar 24 2018 at 18:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nearly%20no_confusion/near/124157916):
<p>In Coq those are first-class proofs.</p>

#### [ Moses Schönfinkel (Mar 24 2018 at 18:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nearly%20no_confusion/near/124157976):
<p>So instead of a type you need to find a term for, in Lean you're asked to provide tactics.</p>

#### [ Andrew Ashworth (Mar 24 2018 at 19:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nearly%20no_confusion/near/124158146):
<p>yes, i agree, i always end up writing out everything using <code>well_founded.fix</code> just so it's easier to read</p>

#### [ Andrew Ashworth (Mar 24 2018 at 19:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nearly%20no_confusion/near/124158155):
<p>i'm glad it's not just my poor Lean programming skills, haha</p>

#### [ Kevin Buzzard (Mar 24 2018 at 19:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nearly%20no_confusion/near/124158400):
<p>Would defining addition on that binary type I mentioned above be easier in Coq? How hard is it in Lean?</p>

#### [ Kevin Buzzard (Mar 24 2018 at 19:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nearly%20no_confusion/near/124158441):
<p>(the inductive type with constructors one, double and double_then_add_one)</p>

#### [ Andrew Ashworth (Mar 24 2018 at 19:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nearly%20no_confusion/near/124158546):
<p>i remember doing that exercise and trying to solve it by defining a coercion to nat. the trouble is you can have an infinite sequence of <code>doub doub doub doub doub zero</code> and you need to normalize the expression before you can do so</p>

#### [ Kevin Buzzard (Mar 24 2018 at 19:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nearly%20no_confusion/near/124158589):
<p>I decided that zero was a bad thing to have, I started at one</p>

#### [ Kevin Buzzard (Mar 24 2018 at 19:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nearly%20no_confusion/near/124158590):
<p>then every positive integer is uniquely represented</p>

#### [ Kevin Buzzard (Mar 24 2018 at 19:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nearly%20no_confusion/near/124158592):
<p>and there is no confusion</p>

#### [ Andrew Ashworth (Mar 24 2018 at 19:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nearly%20no_confusion/near/124158597):
<p>that's cheating! haha</p>

#### [ Andrew Ashworth (Mar 24 2018 at 19:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nearly%20no_confusion/near/124158659):
<p>the same problem arises in the construction of the integers, where the pair (1,0) is the same as (2,1), but you need some way to say they are equivalent</p>

#### [ Moses Schönfinkel (Mar 24 2018 at 19:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nearly%20no_confusion/near/124158710):
<p>I remember doing it in Coq, I am not sure if it would be at all more difficult to do in Lean.</p>

#### [ Chris Hughes (Mar 24 2018 at 19:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nearly%20no_confusion/near/124159648):
<p>I solved the problem Kevin and Andrew were talking about.</p>
<div class="codehilite"><pre><span></span><span class="kn">lemma</span>  <span class="n">sizeof_pos</span> <span class="o">:</span> <span class="bp">∀</span> <span class="n">n</span> <span class="o">:</span> <span class="n">pint</span><span class="o">,</span> <span class="mi">0</span>  <span class="bp">&lt;</span> <span class="n">pint</span><span class="bp">.</span><span class="n">sizeof</span> <span class="n">n</span>
<span class="bp">|</span> <span class="n">one</span> <span class="o">:=</span> <span class="n">dec_trivial</span>
<span class="bp">|</span> <span class="o">(</span><span class="n">d</span> <span class="n">m</span><span class="o">)</span> <span class="o">:=</span>  <span class="k">by</span> <span class="n">unfold</span> <span class="n">pint</span><span class="bp">.</span><span class="n">sizeof</span><span class="bp">;</span> <span class="n">rw</span> <span class="n">add_comm</span><span class="bp">;</span> <span class="n">exact</span> <span class="n">succ_pos</span> <span class="bp">_</span>
<span class="bp">|</span> <span class="o">(</span><span class="n">da</span> <span class="n">m</span><span class="o">)</span> <span class="o">:=</span>  <span class="k">by</span> <span class="n">unfold</span> <span class="n">pint</span><span class="bp">.</span><span class="n">sizeof</span><span class="bp">;</span> <span class="n">rw</span> <span class="n">add_comm</span><span class="bp">;</span> <span class="n">exact</span> <span class="n">succ_pos</span> <span class="bp">_</span>

<span class="n">def</span>  <span class="n">padd2</span> <span class="o">:</span> <span class="n">pint</span> <span class="bp">→</span> <span class="n">pint</span> <span class="bp">→</span> <span class="n">pint</span>
<span class="bp">|</span> <span class="n">one</span> <span class="n">one</span> <span class="o">:=</span> <span class="n">d</span> <span class="n">one</span>
<span class="bp">|</span> <span class="n">one</span> <span class="o">(</span><span class="n">d</span> <span class="n">m</span><span class="o">)</span> <span class="o">:=</span> <span class="n">da</span> <span class="n">m</span>
<span class="bp">|</span> <span class="n">one</span> <span class="o">(</span><span class="n">da</span> <span class="n">m</span><span class="o">)</span> <span class="o">:=</span> <span class="n">d</span> <span class="o">(</span><span class="n">padd2</span> <span class="n">one</span> <span class="n">m</span><span class="o">)</span>
<span class="bp">|</span> <span class="o">(</span><span class="n">d</span> <span class="n">n</span><span class="o">)</span> <span class="n">one</span> <span class="o">:=</span> <span class="n">da</span> <span class="n">n</span>
<span class="bp">|</span> <span class="o">(</span><span class="n">d</span> <span class="n">n</span><span class="o">)</span> <span class="o">(</span><span class="n">d</span> <span class="n">m</span><span class="o">)</span> <span class="o">:=</span> <span class="n">d</span> <span class="o">(</span><span class="n">padd2</span> <span class="n">n</span> <span class="n">m</span><span class="o">)</span>
<span class="bp">|</span> <span class="o">(</span><span class="n">d</span> <span class="n">n</span><span class="o">)</span> <span class="o">(</span><span class="n">da</span> <span class="n">m</span><span class="o">)</span> <span class="o">:=</span> <span class="n">da</span> <span class="o">(</span><span class="n">padd2</span> <span class="n">n</span> <span class="n">m</span><span class="o">)</span>
<span class="bp">|</span> <span class="o">(</span><span class="n">da</span> <span class="n">n</span><span class="o">)</span> <span class="n">one</span> <span class="o">:=</span> <span class="n">d</span> <span class="o">(</span><span class="n">padd2</span> <span class="n">n</span> <span class="n">one</span><span class="o">)</span>
<span class="bp">|</span> <span class="o">(</span><span class="n">da</span> <span class="n">n</span><span class="o">)</span> <span class="o">(</span><span class="n">d</span> <span class="n">m</span><span class="o">)</span> <span class="o">:=</span> <span class="n">da</span> <span class="o">(</span><span class="n">padd2</span> <span class="n">n</span> <span class="n">m</span><span class="o">)</span>
<span class="bp">|</span> <span class="o">(</span><span class="n">da</span> <span class="n">n</span><span class="o">)</span> <span class="o">(</span><span class="n">da</span> <span class="n">m</span><span class="o">):=</span>  <span class="k">have</span> <span class="n">h</span> <span class="o">:</span> <span class="mi">0</span>  <span class="bp">&lt;</span> <span class="n">pint</span><span class="bp">.</span><span class="n">sizeof</span> <span class="n">n</span><span class="o">,</span> <span class="k">from</span> <span class="n">sizeof_pos</span> <span class="bp">_</span><span class="o">,</span>
<span class="n">d</span> <span class="o">(</span><span class="n">padd2</span> <span class="n">one</span> <span class="o">(</span><span class="n">padd2</span> <span class="n">n</span> <span class="n">m</span><span class="o">))</span>
</pre></div>


<p>The order of arguments in the final case matters, I think because in the default well-founded relation on <code>Σ' p : pint, pint</code> , <code>⟨one, padd2 n m⟩ ≺ ⟨da n, da m⟩</code> , but not necessarily <code>⟨padd2 n m, one⟩ ≺ ⟨da n, da m⟩</code> I'm not sure why it wanted me to prove <code>sizeof n</code> was pos however, but that was the goal that came up in the error message.</p>

#### [ Mario Carneiro (Mar 24 2018 at 21:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nearly%20no_confusion/near/124162751):
<p><span class="user-mention" data-user-id="110038">@Kevin Buzzard</span> You should look at mathlib <code>num</code> type, which is binary naturals just as you are describing. You don't need wf recursion for any of the definitions</p>

#### [ Andrew Ashworth (Mar 24 2018 at 22:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nearly%20no_confusion/near/124163808):
<p>yeah, iirc that exercise asks you to define <code>nat_to_bin</code> and <code>bin_to_nat</code>. Once you've proven there is a bijection between the binary naturals and the"traditional" naturals, you can use nat addition on the binary numbers</p>

#### [ Andrew Ashworth (Mar 24 2018 at 22:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nearly%20no_confusion/near/124163818):
<p>this is hard to do if you don't have zero</p>

#### [ Kevin Buzzard (Mar 24 2018 at 22:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nearly%20no_confusion/near/124163981):
<p>it's harder to do if you do have zero</p>

#### [ Kevin Buzzard (Mar 24 2018 at 22:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nearly%20no_confusion/near/124163982):
<p>because double double double zero is zero</p>

#### [ Kevin Buzzard (Mar 24 2018 at 22:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nearly%20no_confusion/near/124163983):
<p>so bijectivity fails much worse</p>

#### [ Kenny Lau (Mar 24 2018 at 22:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nearly%20no_confusion/near/124163994):
<p>bijective binary to the rescue</p>

#### [ Kenny Lau (Mar 24 2018 at 22:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nearly%20no_confusion/near/124163995):
<p>ok it's literally inside the name</p>

#### [ Andrew Ashworth (Mar 24 2018 at 22:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nearly%20no_confusion/near/124164046):
<p>yeah, handling the <code>doub doub doub zero</code> case is the real trick to the problem</p>

#### [ Kenny Lau (Mar 24 2018 at 22:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nearly%20no_confusion/near/124164057):
<p>or you can just surject to the naturals and quotient</p>

#### [ Andrew Ashworth (Mar 24 2018 at 22:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nearly%20no_confusion/near/124164058):
<p>i solved it a long time ago, let me see if i can find my solution, maybe...</p>

#### [ Kenny Lau (Mar 24 2018 at 22:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nearly%20no_confusion/near/124164060):
<p>literally a~b iff f(a)=f(b)</p>

#### [ Kenny Lau (Mar 24 2018 at 22:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nearly%20no_confusion/near/124164107):
<p>(deleted)</p>

#### [ Kevin Buzzard (Mar 24 2018 at 22:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nearly%20no_confusion/near/124164118):
<p>I only defined the map one way. Did it ask you for the other way later on?</p>

#### [ Andrew Ashworth (Mar 24 2018 at 22:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nearly%20no_confusion/near/124164156):
<p>so, it seems they've made many of the exercises different / a little easier in the new edition</p>

#### [ Andrew Ashworth (Mar 24 2018 at 22:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nearly%20no_confusion/near/124164176):
<p>the original problem was a 4 star advanced take you all day to complete if you're a learner hair-raiser</p>

#### [ Andrew Ashworth (Mar 24 2018 at 22:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nearly%20no_confusion/near/124164179):
<p>at least it was for me</p>

#### [ Andrew Ashworth (Mar 24 2018 at 22:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nearly%20no_confusion/near/124164237):
<p>which is why i remember some of the details about it</p>

#### [ Kevin Buzzard (Mar 24 2018 at 22:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nearly%20no_confusion/near/124164281):
<p>They dumbed down for the kids?</p>

#### [ Andrew Ashworth (Mar 24 2018 at 22:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nearly%20no_confusion/near/124164293):
<p>not too badly! and i agree with dumbing it down, it's an introductory text</p>

#### [ Andrew Ashworth (Mar 24 2018 at 22:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nearly%20no_confusion/near/124164348):
<p>i can't imagine teaching yourself from the original software foundations without guidance or help</p>

#### [ Andrew Ashworth (Mar 24 2018 at 22:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nearly%20no_confusion/near/124164360):
<p>i eventually found somebody's homework solutions online and figured out how to solve it</p>

#### [ Andrew Ashworth (Mar 24 2018 at 22:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nearly%20no_confusion/near/124164557):
<p>ahh, yes</p>

#### [ Andrew Ashworth (Mar 24 2018 at 22:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nearly%20no_confusion/near/124164562):
<p><a href="http://staff.ustc.edu.cn/~bjhua/courses/theory/2012/slides/lec1notes.html" target="_blank" title="http://staff.ustc.edu.cn/~bjhua/courses/theory/2012/slides/lec1notes.html">http://staff.ustc.edu.cn/~bjhua/courses/theory/2012/slides/lec1notes.html</a></p>

#### [ Andrew Ashworth (Mar 24 2018 at 22:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nearly%20no_confusion/near/124164617):
<p>once you've normalized your binary number, then you can create a bijection, and life is good again</p>

#### [ Andrew Ashworth (Mar 25 2018 at 01:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nearly%20no_confusion/near/124169245):
<blockquote>
<p>literally a~b iff f(a)=f(b)</p>
</blockquote>
<p>if only i had known at the time. they didn't talk much about equivalence relations in engineering school</p>

#### [ Andrew Ashworth (Mar 25 2018 at 01:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nearly%20no_confusion/near/124169303):
<p>and if SF had started talking about how <code>bin_to_nat</code> was onto but not one-to-one, I doubt many undergraduates would know what that really meant</p>

#### [ Kevin Buzzard (Mar 25 2018 at 01:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nearly%20no_confusion/near/124169359):
<p>That's funny. I teach that to maths undergraduates in year 1 term 1. And equivalence relations.</p>

#### [ Simon Hudon (Mar 25 2018 at 01:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nearly%20no_confusion/near/124169369):
<p>I remember learning that in first year of university too, in discrete math</p>

#### [ Andrew Ashworth (Mar 25 2018 at 01:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nearly%20no_confusion/near/124169410):
<p>i never had to take discrete math, I was an electrical engineer</p>

#### [ Simon Hudon (Mar 25 2018 at 01:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nearly%20no_confusion/near/124169411):
<p>(I did CS and not engineering though, if that makes a difference)</p>

#### [ Andrew Ashworth (Mar 25 2018 at 01:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nearly%20no_confusion/near/124169412):
<p>instead there was a 2 semester sequence on fourier transforms</p>

#### [ Andrew Ashworth (Mar 25 2018 at 01:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nearly%20no_confusion/near/124169419):
<p>where we basically learned very little theory and a lot of how to compute various integrals</p>

#### [ Andrew Ashworth (Mar 25 2018 at 01:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nearly%20no_confusion/near/124169421):
<p>i may have mentioned this before but i have issues with how they teach math in engineering school :)</p>

#### [ Simon Hudon (Mar 25 2018 at 01:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nearly%20no_confusion/near/124169534):
<p>It seems common that people who like math don't get enough of it in engineering school.</p>

#### [ Andrew Ashworth (Mar 25 2018 at 01:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nearly%20no_confusion/near/124169556):
<p>yes, we get a lot of boring computation instead</p>

#### [ Andrew Ashworth (Mar 25 2018 at 01:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nearly%20no_confusion/near/124169584):
<p>my linear algebra class was basically doing a lot of gauss-jordan elimination and calculating eigenvectors by hand</p>

#### [ Andrew Ashworth (Mar 25 2018 at 01:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nearly%20no_confusion/near/124169601):
<p>which ends up being completely a waste of time since no working engineer would ever do these things without a computer</p>

#### [ Simon Hudon (Mar 25 2018 at 01:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nearly%20no_confusion/near/124169659):
<p>Mine was like that too. I've never missed my calculator more than in that class</p>

#### [ Simon Hudon (Mar 25 2018 at 01:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nearly%20no_confusion/near/124169720):
<p>The follow up class was about numerical methods for linear algebra so I guess I should have been happy to do some implementation. I was not easy to satisfy I guess</p>


{% endraw %}
