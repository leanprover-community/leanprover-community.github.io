---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/86695VscodeTranslationsfile.html
---

## [general](index.html)
### [Vscode Translations file](86695VscodeTranslationsfile.html)

#### [Edward Ayers (Jan 10 2019 at 15:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Vscode Translations file/near/154843392):
Dear all I am cleaning up the vscode translations file. I've removed all of the accents which are rejected by Lean. Are there any shortcuts that people find they mistype frequently or which stop a useful character from being corrected?
Eg I often write "\de" and have it corrected to "\dei" = "ϯ" instead of "\delta". Would people also be interested in having two letter shortcuts for all of the lower case greek letters? Ie "\ta" corrects to tau and so on.

#### [Chris Hughes (Jan 10 2019 at 16:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Vscode Translations file/near/154845160):
It would be nice if `\C` was ℂ

#### [Mario Carneiro (Jan 10 2019 at 21:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Vscode Translations file/near/154869375):
lambda should have a one letter command (other than `G` which makes no sense), any suggestions?

#### [Mario Carneiro (Jan 10 2019 at 21:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Vscode Translations file/near/154869466):
maybe `\l` for lambda and `\<-` for left arrow

#### [Mario Carneiro (Jan 10 2019 at 21:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Vscode Translations file/near/154869539):
I agree that all greek should be one or two letters

#### [Mario Carneiro (Jan 10 2019 at 21:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Vscode Translations file/near/154869649):
`\e` should be epsilon not equal

#### [Mario Carneiro (Jan 10 2019 at 21:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Vscode Translations file/near/154869706):
`\q` is theta in mathematica, and a black box in lean (not so useful)

#### [Mario Carneiro (Jan 10 2019 at 21:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Vscode Translations file/near/154869785):
`\p` could be pi instead of that arrow

#### [Edward Ayers (Jan 10 2019 at 22:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Vscode Translations file/near/154872142):
I use `\l` a lot in do notation.

#### [Chris Hughes (Jan 10 2019 at 22:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Vscode Translations file/near/154872276):
I think people in general use lambda more than `<-`

#### [Reid Barton (Jan 10 2019 at 22:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Vscode Translations file/near/154872708):
there's also `rw \l` which might be more common than lambda depending on style

#### [Reid Barton (Jan 10 2019 at 22:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Vscode Translations file/near/154872843):
Another consideration though is ending the abbreviation. I'm not sure whether VSCode works the same way but if I want to rewrite with the reverse of a hypothesis with name that happens to start with `e`, I would like to type `rw \le...`, but that gets processed as the less-than-or-equal operator

#### [Reid Barton (Jan 10 2019 at 22:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Vscode Translations file/near/154872958):
usually I put a space after a lambda but not necessarily after a <-, so switching them would be an improvement in that case

#### [Mario Carneiro (Jan 10 2019 at 22:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Vscode Translations file/near/154874267):
mathlib style puts a space between `<-` and the lemma anyway

#### [Mario Carneiro (Jan 10 2019 at 22:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Vscode Translations file/near/154874331):
if left arrow is so important, any votes for `\-` for left arrow? Currently it looks like it makes a nbsp

#### [Edward Ayers (Jan 10 2019 at 22:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Vscode Translations file/near/154875045):
`\c` is currently `⌜` which is a little useless.

#### [Edward Ayers (Jan 10 2019 at 22:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Vscode Translations file/near/154875133):
Also maybe `\ss` for `⊆`  instead of `ß`

#### [Mario Carneiro (Jan 10 2019 at 23:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Vscode Translations file/near/154875645):
`\c` could be chi

#### [Edward Ayers (Jan 10 2019 at 23:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Vscode Translations file/near/154875797):
`\i` for `⁻¹` instead of `∩`?

#### [Mario Carneiro (Jan 10 2019 at 23:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Vscode Translations file/near/154875916):
`\n` should be `¬ ` not `∋`

#### [Mario Carneiro (Jan 10 2019 at 23:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Vscode Translations file/near/154876024):
`\/` could be `\or`, is that too tricky?

#### [Edward Ayers (Jan 10 2019 at 23:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Vscode Translations file/near/154876054):
`\v` doesn't have a translation.

#### [Mario Carneiro (Jan 10 2019 at 23:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Vscode Translations file/near/154876077):
down arrow? Then `\d` can be delta

#### [Mario Carneiro (Jan 10 2019 at 23:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Vscode Translations file/near/154876088):
I guess down arrow doesn't really matter

#### [Edward Ayers (Jan 10 2019 at 23:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Vscode Translations file/near/154876147):
I don't want to change too many of the ones that are in use but already assigned.

#### [Mario Carneiro (Jan 10 2019 at 23:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Vscode Translations file/near/154876173):
\v = nu?

#### [Mario Carneiro (Jan 10 2019 at 23:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Vscode Translations file/near/154876185):
kind of abusive but `\n` is taken

#### [Edward Ayers (Jan 10 2019 at 23:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Vscode Translations file/near/154876202):
I've added 2 letter translations for each of the greek letters

#### [Edward Ayers (Jan 10 2019 at 23:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Vscode Translations file/near/154876211):
Was thinking `\v` could be `\or`

#### [Mario Carneiro (Jan 10 2019 at 23:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Vscode Translations file/near/154876218):
aha

#### [Mario Carneiro (Jan 10 2019 at 23:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Vscode Translations file/near/154876290):
\D and \G are greek capitals?

#### [Mario Carneiro (Jan 10 2019 at 23:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Vscode Translations file/near/154876316):
The current `\GD` and `\Gd` etc is annoying to type

#### [Mario Carneiro (Jan 10 2019 at 23:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Vscode Translations file/near/154876425):
\L = Lambda

#### [Edward Ayers (Jan 10 2019 at 23:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Vscode Translations file/near/154876493):
overwriting "Ł" with "Λ"

#### [Mario Carneiro (Jan 10 2019 at 23:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Vscode Translations file/near/154876573):
I certainly use big lambda more than polish L in maths

#### [Mario Carneiro (Jan 10 2019 at 23:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Vscode Translations file/near/154876644):
I see that's the only abbrev for polish L, maybe it can relocate to `\L/`

#### [Mario Carneiro (Jan 10 2019 at 23:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Vscode Translations file/near/154876815):
`\m` = mu, I don't know what that m-eq thing is

#### [Johan Commelin (Jan 11 2019 at 08:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Vscode Translations file/near/154899107):
Can we have `\ ` = lambda? Or is `\`-space impossible to assign in VScode? (It is even sort of mnemonic...)

#### [Kenny Lau (Jan 11 2019 at 08:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Vscode Translations file/near/154900307):
well `\;` is space :p

#### [Johan Commelin (Jan 11 2019 at 08:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Vscode Translations file/near/154900384):
I would expect that to be unicode THIN SPACE, if that exists (-; Which I think it does. But that is just my LaTeX intuition ported to VScode. And that port might not be *lawful*

#### [Gabriel Ebner (Jan 11 2019 at 09:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Vscode Translations file/near/154901043):
Patrick just vetoed space.  `, ` needs to remain `, `

#### [Johan Commelin (Jan 11 2019 at 09:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Vscode Translations file/near/154901100):
Fair enough... but just like others need to fix their OS, he ought to fix his keyboard layout :stuck_out_tongue_wink:

#### [matt rice (Jan 12 2019 at 23:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Vscode Translations file/near/155002027):
One thing i found accidentally, was \<> will do the same as: \< \>, but that neither \f<> nor \f<f> will do the same as \f< \f>, I looked a bit through the translations but didn't find where the \<> magic was coming from

#### [Johan Commelin (Jan 14 2019 at 11:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Vscode Translations file/near/155075387):
I don't know if this belongs in the translations file... but I wouldn't mind if I could type `\copyright` and this would expand to the header that goes to the top of every Lean file. (If possible with the correct year filled in.)
Of course I can just copy it from another file... but this would be a nice little feature.
Priority: very low

#### [Gabriel Ebner (Jan 14 2019 at 11:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Vscode Translations file/near/155075895):
@**Johan Commelin** Something like this? https://github.com/leanprover/mathlib/pull/589

#### [Johannes Hölzl (Jan 14 2019 at 12:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Vscode Translations file/near/155076478):
nice

#### [Johan Commelin (Jan 14 2019 at 12:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Vscode Translations file/near/155077548):
Awesome!

#### [Edward Ayers (Jan 14 2019 at 13:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Vscode Translations file/near/155082207):
Summary  of my proposed changes:
- `\L` is `Λ` instead of `Ł`
- `\G` is `Γ`
- `\p`is `Π`
- `\C` is `ℂ` instead of `∁`
- `\c` is `χ`
- `\v` is `∨`
- `\-` is `⁻¹` instead of a space.
- `\n` is `¬`
- `\ss` is `⊆`
- `\m` is `μ`
All greek letters have a 2-space shortcut. Eg sigma is `\si`, omega is `\om` etc.

All accented characters have been removed except 
```
À Á Â Ã Ä Å Æ Ç È É Ê Ë Ì Í Î Ï
Ð Ñ Ò Ó Ô Õ Ö    Ø Ù Ú Û Ü Ý Þ 
à á â ã ä å æ ç è é ê ë ì í î ï
ð ñ ò ó ô õ ö   ø ù ú û ü ý þ ÿ
Ł
```
(so we can still use important keywords like "Hölzl")

#### [Patrick Massot (Jan 14 2019 at 16:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Vscode Translations file/near/155089894):
Did we decide something for \l giving lambda or left arrow?

#### [Rob Lewis (Jan 14 2019 at 16:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Vscode Translations file/near/155090148):
I'd prefer not to change it from left arrow, since presumably anyone who writes tactics uses it a lot.

#### [Patrick Massot (Jan 14 2019 at 16:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Vscode Translations file/near/155090192):
everybody use left arrow a lot, it's also used in rewrite. If we change we also need a nice shortcut for left arrow

#### [Edward Ayers (Jan 14 2019 at 16:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Vscode Translations file/near/155090639):
`\l`for lambda is contentious so I just kept it as is. In this PR I don't want to change the translations file in such a way that could potentially make things worse for some users.

#### [Thales (Jan 15 2019 at 00:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Vscode Translations file/near/155130903):
Some unsupported notations I have considered using in the future are
 ˇ caron, ␣ vispace, ˅ down , ˄ up, ⅅ Dd, ⅆ dd, ⅇ ee, ⅈ ii, ⅉ jj.
The intended use is that ⅈ designates the complex number i, ⅇ designates the
base of the natural log, ⅆ is the binder for integration, etc.

I have experimented with using accents as operators.  For example, the U+0304 bar accent is particularly useful.

Will Lean-emacs remain compatible with VSCode for those of us that switch back and forth?

#### [Mario Carneiro (Jan 15 2019 at 01:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Vscode Translations file/near/155133461):
The emacs and VSCode lean modes use the same translations file, so any change to translations.json should affect both

#### [Mario Carneiro (Jan 15 2019 at 01:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Vscode Translations file/near/155133513):
I'm not sure if the cocalc version uses the same file

#### [Patrick Massot (Jan 15 2019 at 08:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Vscode Translations file/near/155152390):
We should also make sure to PR modifications to TPIL and the reference manual (and mathlib doc)

#### [Gabriel Ebner (Jan 15 2019 at 09:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Vscode Translations file/near/155153866):
```quote
The emacs and VSCode lean modes use the same translations file, so any change to translations.json should affect both
```
 Unfortunately this is not at all the case.  The vscode extension, the emacs mode, cocalc, the javascript version, they all use their own *copy* of the translations.  The `translations.json` file was originally exported from the emacs mode two years ago.  To my knowledge, none of the improvements in the vscode extension have been propagated to the other editor plugins.

#### [Sebastian Ullrich (Jan 15 2019 at 09:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Vscode Translations file/near/155153913):
I still type `\lam` :shrug:

#### [Sebastian Ullrich (Jan 15 2019 at 09:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Vscode Translations file/near/155153921):
But I'm definitely open to unifying this

#### [Johan Commelin (Jan 17 2019 at 18:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Vscode Translations file/near/155354302):
@**Edward Ayers** Have your changes already been merged?

#### [Johan Commelin (Jan 17 2019 at 18:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Vscode Translations file/near/155354343):
If not, could you change the translation of `\functor` (and prefixes of that) back to the old symbol?

#### [Johan Commelin (Jan 17 2019 at 18:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Vscode Translations file/near/155354389):
The old symbol is `⇒`

#### [Bryan Gin-ge Chen (Jan 17 2019 at 18:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Vscode Translations file/near/155354418):
His changes have already been merged in [#107](https://github.com/leanprover/vscode-lean/pull/107), but your suggestion wouldn't be hard to implement.

#### [Johan Commelin (Jan 17 2019 at 18:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Vscode Translations file/near/155354511):
Sure, I just wasn't aware what the status was. Otherwise it could go into that PR.

#### [Johan Commelin (Jan 17 2019 at 18:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Vscode Translations file/near/155354517):
So now we have to create a new one.

#### [Bryan Gin-ge Chen (Jan 17 2019 at 18:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Vscode Translations file/near/155354642):
I'm not seeing anything related to `\functor` changed in the diff though?

#### [Bryan Gin-ge Chen (Jan 17 2019 at 18:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Vscode Translations file/near/155354707):
[Here's the diff](https://github.com/EdAyers/vscode-lean/commit/842282b9b96e91ddef3b1eeec759bb03c377f6b8#diff-7c2385f0b8db521fe81e3d20489e5f12). In the current version of the extension, if I complete `\functor` I get `⥤`. If I search the diff for that symbol, I see it both in the old version and the new version.

#### [Bryan Gin-ge Chen (Jan 17 2019 at 18:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Vscode Translations file/near/155354777):
The symbol you pasted above as the "old symbol" ⇒ is currently `\Longrightarrow`. 

I guess this also used to be under `\functor` but that was changed by [your commit in August](https://github.com/leanprover/vscode-lean/commit/d3988d9fae1ab4a7e4785486a08c5eddcd33c575).

OK, so I think I finally understand. You want to revert that change from August, not anything done by Ed.

#### [Johan Commelin (Jan 17 2019 at 19:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Vscode Translations file/near/155355703):
Exactly. Sorry if I was confusing.

#### [Johan Commelin (Jan 17 2019 at 19:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Vscode Translations file/near/155355731):
Because that symbol was locked into core, but was recently liberated.

#### [Johan Commelin (Jan 17 2019 at 19:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Vscode Translations file/near/155356269):
I made a PR with this change. @**Gabriel Ebner**

#### [Gabriel Ebner (Jan 17 2019 at 19:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Vscode Translations file/near/155356868):
Should we maybe wait until mathlib works with that Lean version?

#### [Johan Commelin (Jan 17 2019 at 19:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Vscode Translations file/near/155356990):
Yes, that is probably a good idea.

#### [Johan Commelin (Jan 17 2019 at 19:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Vscode Translations file/near/155357006):
How far are we from that moment?

#### [Bryan Gin-ge Chen (Jan 17 2019 at 19:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Vscode Translations file/near/155357102):
As far as I can tell we're just waiting on 3.4.2 to be officially released. Then I'll PR the 3.4.2 branch in community mathlib which currently works with nightly.

#### [Gabriel Ebner (Jan 17 2019 at 19:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Vscode Translations file/near/155357123):
We could switch to nightlies earlier, I guess.

#### [Edward Ayers (Jan 17 2019 at 19:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Vscode Translations file/near/155358522):
I think so

