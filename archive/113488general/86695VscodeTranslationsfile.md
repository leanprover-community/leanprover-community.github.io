---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/86695VscodeTranslationsfile.html
---

## Stream: [general](index.html)
### Topic: [Vscode Translations file](86695VscodeTranslationsfile.html)

---


{% raw %}
#### [ Edward Ayers (Jan 10 2019 at 15:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Vscode%20Translations%20file/near/154843392):
<p>Dear all I am cleaning up the vscode translations file. I've removed all of the accents which are rejected by Lean. Are there any shortcuts that people find they mistype frequently or which stop a useful character from being corrected?<br>
Eg I often write "\de" and have it corrected to "\dei" = "ϯ" instead of "\delta". Would people also be interested in having two letter shortcuts for all of the lower case greek letters? Ie "\ta" corrects to tau and so on.</p>

#### [ Chris Hughes (Jan 10 2019 at 16:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Vscode%20Translations%20file/near/154845160):
<p>It would be nice if <code>\C</code> was ℂ</p>

#### [ Mario Carneiro (Jan 10 2019 at 21:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Vscode%20Translations%20file/near/154869375):
<p>lambda should have a one letter command (other than <code>G</code> which makes no sense), any suggestions?</p>

#### [ Mario Carneiro (Jan 10 2019 at 21:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Vscode%20Translations%20file/near/154869466):
<p>maybe <code>\l</code> for lambda and <code>\&lt;-</code> for left arrow</p>

#### [ Mario Carneiro (Jan 10 2019 at 21:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Vscode%20Translations%20file/near/154869539):
<p>I agree that all greek should be one or two letters</p>

#### [ Mario Carneiro (Jan 10 2019 at 21:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Vscode%20Translations%20file/near/154869649):
<p><code>\e</code> should be epsilon not equal</p>

#### [ Mario Carneiro (Jan 10 2019 at 21:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Vscode%20Translations%20file/near/154869706):
<p><code>\q</code> is theta in mathematica, and a black box in lean (not so useful)</p>

#### [ Mario Carneiro (Jan 10 2019 at 21:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Vscode%20Translations%20file/near/154869785):
<p><code>\p</code> could be pi instead of that arrow</p>

#### [ Edward Ayers (Jan 10 2019 at 22:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Vscode%20Translations%20file/near/154872142):
<p>I use <code>\l</code> a lot in do notation.</p>

#### [ Chris Hughes (Jan 10 2019 at 22:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Vscode%20Translations%20file/near/154872276):
<p>I think people in general use lambda more than <code>&lt;-</code></p>

#### [ Reid Barton (Jan 10 2019 at 22:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Vscode%20Translations%20file/near/154872708):
<p>there's also <code>rw \l</code> which might be more common than lambda depending on style</p>

#### [ Reid Barton (Jan 10 2019 at 22:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Vscode%20Translations%20file/near/154872843):
<p>Another consideration though is ending the abbreviation. I'm not sure whether VSCode works the same way but if I want to rewrite with the reverse of a hypothesis with name that happens to start with <code>e</code>, I would like to type <code>rw \le...</code>, but that gets processed as the less-than-or-equal operator</p>

#### [ Reid Barton (Jan 10 2019 at 22:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Vscode%20Translations%20file/near/154872958):
<p>usually I put a space after a lambda but not necessarily after a &lt;-, so switching them would be an improvement in that case</p>

#### [ Mario Carneiro (Jan 10 2019 at 22:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Vscode%20Translations%20file/near/154874267):
<p>mathlib style puts a space between <code>&lt;-</code> and the lemma anyway</p>

#### [ Mario Carneiro (Jan 10 2019 at 22:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Vscode%20Translations%20file/near/154874331):
<p>if left arrow is so important, any votes for <code>\-</code> for left arrow? Currently it looks like it makes a nbsp</p>

#### [ Edward Ayers (Jan 10 2019 at 22:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Vscode%20Translations%20file/near/154875045):
<p><code>\c</code> is currently <code>⌜</code> which is a little useless.</p>

#### [ Edward Ayers (Jan 10 2019 at 22:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Vscode%20Translations%20file/near/154875133):
<p>Also maybe <code>\ss</code> for <code>⊆</code>  instead of <code>ß</code></p>

#### [ Mario Carneiro (Jan 10 2019 at 23:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Vscode%20Translations%20file/near/154875645):
<p><code>\c</code> could be chi</p>

#### [ Edward Ayers (Jan 10 2019 at 23:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Vscode%20Translations%20file/near/154875797):
<p><code>\i</code> for <code>⁻¹</code> instead of <code>∩</code>?</p>

#### [ Mario Carneiro (Jan 10 2019 at 23:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Vscode%20Translations%20file/near/154875916):
<p><code>\n</code> should be <code>¬ </code> not <code>∋</code></p>

#### [ Mario Carneiro (Jan 10 2019 at 23:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Vscode%20Translations%20file/near/154876024):
<p><code>\/</code> could be <code>\or</code>, is that too tricky?</p>

#### [ Edward Ayers (Jan 10 2019 at 23:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Vscode%20Translations%20file/near/154876054):
<p><code>\v</code> doesn't have a translation.</p>

#### [ Mario Carneiro (Jan 10 2019 at 23:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Vscode%20Translations%20file/near/154876077):
<p>down arrow? Then <code>\d</code> can be delta</p>

#### [ Mario Carneiro (Jan 10 2019 at 23:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Vscode%20Translations%20file/near/154876088):
<p>I guess down arrow doesn't really matter</p>

#### [ Edward Ayers (Jan 10 2019 at 23:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Vscode%20Translations%20file/near/154876147):
<p>I don't want to change too many of the ones that are in use but already assigned.</p>

#### [ Mario Carneiro (Jan 10 2019 at 23:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Vscode%20Translations%20file/near/154876173):
<p>\v = nu?</p>

#### [ Mario Carneiro (Jan 10 2019 at 23:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Vscode%20Translations%20file/near/154876185):
<p>kind of abusive but <code>\n</code> is taken</p>

#### [ Edward Ayers (Jan 10 2019 at 23:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Vscode%20Translations%20file/near/154876202):
<p>I've added 2 letter translations for each of the greek letters</p>

#### [ Edward Ayers (Jan 10 2019 at 23:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Vscode%20Translations%20file/near/154876211):
<p>Was thinking <code>\v</code> could be <code>\or</code></p>

#### [ Mario Carneiro (Jan 10 2019 at 23:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Vscode%20Translations%20file/near/154876218):
<p>aha</p>

#### [ Mario Carneiro (Jan 10 2019 at 23:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Vscode%20Translations%20file/near/154876290):
<p>\D and \G are greek capitals?</p>

#### [ Mario Carneiro (Jan 10 2019 at 23:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Vscode%20Translations%20file/near/154876316):
<p>The current <code>\GD</code> and <code>\Gd</code> etc is annoying to type</p>

#### [ Mario Carneiro (Jan 10 2019 at 23:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Vscode%20Translations%20file/near/154876425):
<p>\L = Lambda</p>

#### [ Edward Ayers (Jan 10 2019 at 23:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Vscode%20Translations%20file/near/154876493):
<p>overwriting "Ł" with "Λ"</p>

#### [ Mario Carneiro (Jan 10 2019 at 23:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Vscode%20Translations%20file/near/154876573):
<p>I certainly use big lambda more than polish L in maths</p>

#### [ Mario Carneiro (Jan 10 2019 at 23:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Vscode%20Translations%20file/near/154876644):
<p>I see that's the only abbrev for polish L, maybe it can relocate to <code>\L/</code></p>

#### [ Mario Carneiro (Jan 10 2019 at 23:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Vscode%20Translations%20file/near/154876815):
<p><code>\m</code> = mu, I don't know what that m-eq thing is</p>

#### [ Johan Commelin (Jan 11 2019 at 08:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Vscode%20Translations%20file/near/154899107):
<p>Can we have <code>\ </code> = lambda? Or is <code>\</code>-space impossible to assign in VScode? (It is even sort of mnemonic...)</p>

#### [ Kenny Lau (Jan 11 2019 at 08:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Vscode%20Translations%20file/near/154900307):
<p>well <code>\;</code> is space :p</p>

#### [ Johan Commelin (Jan 11 2019 at 08:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Vscode%20Translations%20file/near/154900384):
<p>I would expect that to be unicode THIN SPACE, if that exists (-; Which I think it does. But that is just my LaTeX intuition ported to VScode. And that port might not be <em>lawful</em></p>

#### [ Gabriel Ebner (Jan 11 2019 at 09:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Vscode%20Translations%20file/near/154901043):
<p>Patrick just vetoed space.  <code>, </code> needs to remain <code>, </code></p>

#### [ Johan Commelin (Jan 11 2019 at 09:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Vscode%20Translations%20file/near/154901100):
<p>Fair enough... but just like others need to fix their OS, he ought to fix his keyboard layout <span class="emoji emoji-1f61c" title="stuck out tongue wink">:stuck_out_tongue_wink:</span></p>

#### [ matt rice (Jan 12 2019 at 23:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Vscode%20Translations%20file/near/155002027):
<p>One thing i found accidentally, was \&lt;&gt; will do the same as: \&lt; \&gt;, but that neither \f&lt;&gt; nor \f&lt;f&gt; will do the same as \f&lt; \f&gt;, I looked a bit through the translations but didn't find where the \&lt;&gt; magic was coming from</p>

#### [ Johan Commelin (Jan 14 2019 at 11:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Vscode%20Translations%20file/near/155075387):
<p>I don't know if this belongs in the translations file... but I wouldn't mind if I could type <code>\copyright</code> and this would expand to the header that goes to the top of every Lean file. (If possible with the correct year filled in.)<br>
Of course I can just copy it from another file... but this would be a nice little feature.<br>
Priority: very low</p>

#### [ Gabriel Ebner (Jan 14 2019 at 11:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Vscode%20Translations%20file/near/155075895):
<p><span class="user-mention" data-user-id="112680">@Johan Commelin</span> Something like this? <a href="https://github.com/leanprover/mathlib/pull/589" target="_blank" title="https://github.com/leanprover/mathlib/pull/589">https://github.com/leanprover/mathlib/pull/589</a></p>

#### [ Johannes Hölzl (Jan 14 2019 at 12:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Vscode%20Translations%20file/near/155076478):
<p>nice</p>

#### [ Johan Commelin (Jan 14 2019 at 12:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Vscode%20Translations%20file/near/155077548):
<p>Awesome!</p>

#### [ Edward Ayers (Jan 14 2019 at 13:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Vscode%20Translations%20file/near/155082207):
<p>Summary  of my proposed changes:<br>
- <code>\L</code> is <code>Λ</code> instead of <code>Ł</code><br>
- <code>\G</code> is <code>Γ</code><br>
- <code>\p</code>is <code>Π</code><br>
- <code>\C</code> is <code>ℂ</code> instead of <code>∁</code><br>
- <code>\c</code> is <code>χ</code><br>
- <code>\v</code> is <code>∨</code><br>
- <code>\-</code> is <code>⁻¹</code> instead of a space.<br>
- <code>\n</code> is <code>¬</code><br>
- <code>\ss</code> is <code>⊆</code><br>
- <code>\m</code> is <code>μ</code><br>
All greek letters have a 2-space shortcut. Eg sigma is <code>\si</code>, omega is <code>\om</code> etc.</p>
<p>All accented characters have been removed except </p>
<div class="codehilite"><pre><span></span>À Á Â Ã Ä Å Æ Ç È É Ê Ë Ì Í Î Ï
Ð Ñ Ò Ó Ô Õ Ö    Ø Ù Ú Û Ü Ý Þ
à á â ã ä å æ ç è é ê ë ì í î ï
ð ñ ò ó ô õ ö   ø ù ú û ü ý þ ÿ
Ł
</pre></div>


<p>(so we can still use important keywords like "Hölzl")</p>

#### [ Patrick Massot (Jan 14 2019 at 16:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Vscode%20Translations%20file/near/155089894):
<p>Did we decide something for \l giving lambda or left arrow?</p>

#### [ Rob Lewis (Jan 14 2019 at 16:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Vscode%20Translations%20file/near/155090148):
<p>I'd prefer not to change it from left arrow, since presumably anyone who writes tactics uses it a lot.</p>

#### [ Patrick Massot (Jan 14 2019 at 16:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Vscode%20Translations%20file/near/155090192):
<p>everybody use left arrow a lot, it's also used in rewrite. If we change we also need a nice shortcut for left arrow</p>

#### [ Edward Ayers (Jan 14 2019 at 16:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Vscode%20Translations%20file/near/155090639):
<p><code>\l</code>for lambda is contentious so I just kept it as is. In this PR I don't want to change the translations file in such a way that could potentially make things worse for some users.</p>

#### [ Thales (Jan 15 2019 at 00:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Vscode%20Translations%20file/near/155130903):
<p>Some unsupported notations I have considered using in the future are<br>
 ˇ caron, ␣ vispace, ˅ down , ˄ up, ⅅ Dd, ⅆ dd, ⅇ ee, ⅈ ii, ⅉ jj.<br>
The intended use is that ⅈ designates the complex number i, ⅇ designates the<br>
base of the natural log, ⅆ is the binder for integration, etc.</p>
<p>I have experimented with using accents as operators.  For example, the U+0304 bar accent is particularly useful.</p>
<p>Will Lean-emacs remain compatible with VSCode for those of us that switch back and forth?</p>

#### [ Mario Carneiro (Jan 15 2019 at 01:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Vscode%20Translations%20file/near/155133461):
<p>The emacs and VSCode lean modes use the same translations file, so any change to translations.json should affect both</p>

#### [ Mario Carneiro (Jan 15 2019 at 01:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Vscode%20Translations%20file/near/155133513):
<p>I'm not sure if the cocalc version uses the same file</p>

#### [ Patrick Massot (Jan 15 2019 at 08:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Vscode%20Translations%20file/near/155152390):
<p>We should also make sure to PR modifications to TPIL and the reference manual (and mathlib doc)</p>

#### [ Gabriel Ebner (Jan 15 2019 at 09:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Vscode%20Translations%20file/near/155153866):
<blockquote>
<p>The emacs and VSCode lean modes use the same translations file, so any change to translations.json should affect both</p>
</blockquote>
<p>Unfortunately this is not at all the case.  The vscode extension, the emacs mode, cocalc, the javascript version, they all use their own <em>copy</em> of the translations.  The <code>translations.json</code> file was originally exported from the emacs mode two years ago.  To my knowledge, none of the improvements in the vscode extension have been propagated to the other editor plugins.</p>

#### [ Sebastian Ullrich (Jan 15 2019 at 09:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Vscode%20Translations%20file/near/155153913):
<p>I still type <code>\lam</code> <span class="emoji emoji-1f937" title="shrug">:shrug:</span></p>

#### [ Sebastian Ullrich (Jan 15 2019 at 09:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Vscode%20Translations%20file/near/155153921):
<p>But I'm definitely open to unifying this</p>

#### [ Johan Commelin (Jan 17 2019 at 18:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Vscode%20Translations%20file/near/155354302):
<p><span class="user-mention" data-user-id="121918">@Edward Ayers</span> Have your changes already been merged?</p>

#### [ Johan Commelin (Jan 17 2019 at 18:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Vscode%20Translations%20file/near/155354343):
<p>If not, could you change the translation of <code>\functor</code> (and prefixes of that) back to the old symbol?</p>

#### [ Johan Commelin (Jan 17 2019 at 18:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Vscode%20Translations%20file/near/155354389):
<p>The old symbol is <code>⇒</code></p>

#### [ Bryan Gin-ge Chen (Jan 17 2019 at 18:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Vscode%20Translations%20file/near/155354418):
<p>His changes have already been merged in <a href="https://github.com/leanprover/vscode-lean/pull/107" target="_blank" title="https://github.com/leanprover/vscode-lean/pull/107">#107</a>, but your suggestion wouldn't be hard to implement.</p>

#### [ Johan Commelin (Jan 17 2019 at 18:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Vscode%20Translations%20file/near/155354511):
<p>Sure, I just wasn't aware what the status was. Otherwise it could go into that PR.</p>

#### [ Johan Commelin (Jan 17 2019 at 18:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Vscode%20Translations%20file/near/155354517):
<p>So now we have to create a new one.</p>

#### [ Bryan Gin-ge Chen (Jan 17 2019 at 18:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Vscode%20Translations%20file/near/155354642):
<p>I'm not seeing anything related to <code>\functor</code> changed in the diff though?</p>

#### [ Bryan Gin-ge Chen (Jan 17 2019 at 18:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Vscode%20Translations%20file/near/155354707):
<p><a href="https://github.com/EdAyers/vscode-lean/commit/842282b9b96e91ddef3b1eeec759bb03c377f6b8#diff-7c2385f0b8db521fe81e3d20489e5f12" target="_blank" title="https://github.com/EdAyers/vscode-lean/commit/842282b9b96e91ddef3b1eeec759bb03c377f6b8#diff-7c2385f0b8db521fe81e3d20489e5f12">Here's the diff</a>. In the current version of the extension, if I complete <code>\functor</code> I get <code>⥤</code>. If I search the diff for that symbol, I see it both in the old version and the new version.</p>

#### [ Bryan Gin-ge Chen (Jan 17 2019 at 18:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Vscode%20Translations%20file/near/155354777):
<p>The symbol you pasted above as the "old symbol" ⇒ is currently <code>\Longrightarrow</code>. </p>
<p>I guess this also used to be under <code>\functor</code> but that was changed by <a href="https://github.com/leanprover/vscode-lean/commit/d3988d9fae1ab4a7e4785486a08c5eddcd33c575" target="_blank" title="https://github.com/leanprover/vscode-lean/commit/d3988d9fae1ab4a7e4785486a08c5eddcd33c575">your commit in August</a>.</p>
<p>OK, so I think I finally understand. You want to revert that change from August, not anything done by Ed.</p>

#### [ Johan Commelin (Jan 17 2019 at 19:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Vscode%20Translations%20file/near/155355703):
<p>Exactly. Sorry if I was confusing.</p>

#### [ Johan Commelin (Jan 17 2019 at 19:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Vscode%20Translations%20file/near/155355731):
<p>Because that symbol was locked into core, but was recently liberated.</p>

#### [ Johan Commelin (Jan 17 2019 at 19:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Vscode%20Translations%20file/near/155356269):
<p>I made a PR with this change. <span class="user-mention" data-user-id="110043">@Gabriel Ebner</span></p>

#### [ Gabriel Ebner (Jan 17 2019 at 19:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Vscode%20Translations%20file/near/155356868):
<p>Should we maybe wait until mathlib works with that Lean version?</p>

#### [ Johan Commelin (Jan 17 2019 at 19:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Vscode%20Translations%20file/near/155356990):
<p>Yes, that is probably a good idea.</p>

#### [ Johan Commelin (Jan 17 2019 at 19:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Vscode%20Translations%20file/near/155357006):
<p>How far are we from that moment?</p>

#### [ Bryan Gin-ge Chen (Jan 17 2019 at 19:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Vscode%20Translations%20file/near/155357102):
<p>As far as I can tell we're just waiting on 3.4.2 to be officially released. Then I'll PR the 3.4.2 branch in community mathlib which currently works with nightly.</p>

#### [ Gabriel Ebner (Jan 17 2019 at 19:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Vscode%20Translations%20file/near/155357123):
<p>We could switch to nightlies earlier, I guess.</p>

#### [ Edward Ayers (Jan 17 2019 at 19:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Vscode%20Translations%20file/near/155358522):
<p>I think so</p>


{% endraw %}
