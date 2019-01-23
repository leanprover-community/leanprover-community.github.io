---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/31824vscodelean0110.html
---

## Stream: [general](index.html)
### Topic: [vscode-lean 0.11.0](31824vscodelean0110.html)

---

#### [Gabriel Ebner (Apr 21 2018 at 19:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vscode-lean%200.11.0/near/125499751):
{% raw %}
I just pushed a new update for the vscode extension.  A few bugfixes and features have accumulated over the last few months:
 * The new `visibleRanges` API in vscode is supported now.  Per default, we no longer check the whole file on every keystroke, but only the currently visible lines (and the rest of the file above).  This new API is only present in vscode >=1.22 (released in March), no idea if it works with older vscode versions.  Please complain (or upgrade) if you run into any troubles.
 * You can now input ⦃⦄ using `\{{`
 * Fewer complaints about `leanpkg.path` changes.{% endraw %}

#### [Mario Carneiro (Apr 21 2018 at 22:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vscode-lean%200.11.0/near/125504461):
can you also type ⟦⟧ using `\[[`?

#### [Chris Hughes (Apr 21 2018 at 22:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vscode-lean%200.11.0/near/125504757):
No, it seems.

#### [Patrick Massot (Apr 21 2018 at 22:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vscode-lean%200.11.0/near/125505099):
How do you check what version of the extension is used? How do you upgrade?

#### [Chris Hughes (Apr 21 2018 at 22:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vscode-lean%200.11.0/near/125505255):
{% raw %}
I clicked on extensions on the left pane, and I clicked the reload button. Try typing` \{{` and  if it turns into special brackets, you have the upgrade.{% endraw %}

#### [Patrick Massot (Apr 21 2018 at 22:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vscode-lean%200.11.0/near/125505262):
I didn't see a reload button

#### [Patrick Massot (Apr 21 2018 at 22:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vscode-lean%200.11.0/near/125505263):
I'll search more

#### [Chris Hughes (Apr 21 2018 at 22:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vscode-lean%200.11.0/near/125505271):
I have a feeling it might do it automatically if you restart, so I would try the brackets thing.

#### [Patrick Massot (Apr 21 2018 at 22:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vscode-lean%200.11.0/near/125505313):
Ok, I've found a menu containg "search updates" (or something like this, this part is in French here)

#### [Patrick Massot (Apr 21 2018 at 22:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vscode-lean%200.11.0/near/125505315):
I'm updated

#### [Gabriel Ebner (Apr 22 2018 at 08:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vscode-lean%200.11.0/near/125520061):
```quote
can you also type ⟦⟧ using `\[[`?
```
You can, as of a minute ago.

#### [Patrick Massot (Apr 22 2018 at 11:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vscode-lean%200.11.0/near/125523356):
Thank you!

#### [Patrick Massot (Apr 22 2018 at 11:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vscode-lean%200.11.0/near/125523927):
Very easy suggestion: make a command (usable through Ctrl-p like the Restart server command) that opens up https://github.com/leanprover/vscode-lean/blob/master/translations.json in a new tab (not fetching it from the web, opening the one which is actually used on the current install)

#### [Patrick Massot (Apr 23 2018 at 16:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vscode-lean%200.11.0/near/125571378):
What about having syntax highlighting in the Lean message window? Would that be complicated to do?

#### [Gabriel Ebner (Apr 23 2018 at 16:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vscode-lean%200.11.0/near/125572368):
If "message window" is the info view (with the pause button on the top right), then this is a bit complicated.  Unfortunately we do not have any programmatic access to vscode's syntax highlighter.  AFAIK there is also no pure javascript package that can use these syntax highlighting files.  I'll keep it in mind though.

#### [Patrick Massot (Apr 23 2018 at 16:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vscode-lean%200.11.0/near/125572400):
Yes this is what I meant. We do spend quite some time staring at this window, and it's a bit austere.

#### [Patrick Massot (May 08 2018 at 17:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vscode-lean%200.11.0/near/126270759):
```quote
If "message window" is the info view (with the pause button on the top right), then this is a bit complicated.  Unfortunately we do not have any programmatic access to vscode's syntax highlighter.  AFAIK there is also no pure javascript package that can use these syntax highlighting files.  I'll keep it in mind though.
```
I just played a bit with this. Here is what I currently see in my VScode:

#### [Patrick Massot (May 08 2018 at 17:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vscode-lean%200.11.0/near/126270769):
[colored_tactic_state.png](/user_uploads/3121/nyFVDaVWTFbkyaDebw9CTNRE/colored_tactic_state.png)

#### [Patrick Massot (May 08 2018 at 17:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vscode-lean%200.11.0/near/126270776):
I think it's already useful (to me at least)

#### [Patrick Massot (May 08 2018 at 18:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vscode-lean%200.11.0/near/126270840):
It's super low tech and unreliable, based on:
```javascript
function formatTacticState(s: string): string {
    return s
        .replace(/^(\d+ goals)/g, '<strong style="color:#569cd6;">$1</strong> :')
        .replace(/^([^ ][^:\n⊢]*) :/g, '<strong style="color:#dcdc00;">$1</strong> :')
        .replace(/\n([^ ⊢][^:\n⊢]*) :/g, '\n<strong style="color:#dcdc00;">$1</strong> :')
        .replace(/\n⊢/g, '\n<strong style="color:#569cd6;">⊢</strong>');
}
```

#### [Patrick Massot (May 08 2018 at 18:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vscode-lean%200.11.0/near/126270853):
Which is called in `InfoProvider.renderGoal`

#### [Patrick Massot (May 08 2018 at 18:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vscode-lean%200.11.0/near/126270859):
@**Gabriel Ebner** What do you think about that?

#### [Mario Carneiro (May 08 2018 at 18:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vscode-lean%200.11.0/near/126270862):
I would object to this on purity grounds, but TBH the standard syntax highlighter isn't much better

#### [Patrick Massot (May 08 2018 at 18:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vscode-lean%200.11.0/near/126270911):
Indeed it couldn't be less pure

#### [Patrick Massot (May 08 2018 at 18:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vscode-lean%200.11.0/near/126270920):
And the next Lean file I'll open will probably tell me I missed some edge case

#### [Mario Carneiro (May 08 2018 at 18:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vscode-lean%200.11.0/near/126270925):
You can probably parse a tactic print string pretty reliably by classifying the lines that don't start with whitespace

#### [Patrick Massot (May 08 2018 at 18:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vscode-lean%200.11.0/near/126270940):
But Gabriel told me the syntax highlighter is not available here

#### [Patrick Massot (May 08 2018 at 18:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vscode-lean%200.11.0/near/126270946):
Yes, a classification function would help

#### [Patrick Massot (May 08 2018 at 18:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vscode-lean%200.11.0/near/126270948):
At least make things more modular

#### [Patrick Massot (May 08 2018 at 18:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vscode-lean%200.11.0/near/126270990):
With the above method, trying to catch anything new would likely break things

#### [Gabriel Ebner (May 08 2018 at 18:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vscode-lean%200.11.0/near/126270991):
This looks great!  I'll just make sure it is also readable with a white background.

#### [Mario Carneiro (May 08 2018 at 18:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vscode-lean%200.11.0/near/126270999):
don't forget the `case` line of tactic state

#### [Patrick Massot (May 08 2018 at 18:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vscode-lean%200.11.0/near/126271008):
There should be away to have proper CSS interacting with the selected theme instead of hardcoded colors

#### [Mario Carneiro (May 08 2018 at 18:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vscode-lean%200.11.0/near/126271012):
presumably it's as simple as just `<span class="x">`

#### [Patrick Massot (May 08 2018 at 18:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vscode-lean%200.11.0/near/126271065):
The question is not there: where should we put classes definitions?

#### [Gabriel Ebner (May 08 2018 at 18:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vscode-lean%200.11.0/near/126271069):
@**Patrick Massot** did you just put the `<strong>` inside the `<pre>`?

#### [Gabriel Ebner (May 08 2018 at 18:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vscode-lean%200.11.0/near/126271075):
The CSS is in `infoview.css`

#### [Patrick Massot (May 08 2018 at 18:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vscode-lean%200.11.0/near/126271078):
```javascript
    private renderGoal() {
        if (!this.curGoalState || this.displayMode !== DisplayMode.OnlyState) { return ''; }
        return `<div id="goal"><h1>Tactic State</h1><pre>${formatTacticState(escapeHtml(this.curGoalState))}</pre></div>`;
    }
```

#### [Patrick Massot (May 08 2018 at 18:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vscode-lean%200.11.0/near/126271182):
Reading `infoview.css` is very interesting

#### [Patrick Massot (May 08 2018 at 18:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vscode-lean%200.11.0/near/126271185):
Indeed it should be very easy to use

#### [Gabriel Ebner (May 08 2018 at 18:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vscode-lean%200.11.0/near/126272070):
The colorization has been deployed.  Please complain if the fancy colors distract you too much.

#### [Patrick Massot (May 08 2018 at 18:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vscode-lean%200.11.0/near/126272161):
Wow, you're fast

#### [Patrick Massot (May 08 2018 at 18:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vscode-lean%200.11.0/near/126272166):
I was working on it

#### [Patrick Massot (May 08 2018 at 18:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vscode-lean%200.11.0/near/126272171):
But not fast enough :wink:

#### [Patrick Massot (May 08 2018 at 18:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vscode-lean%200.11.0/near/126272212):
I didn't know about the `m` flag in `replace`

#### [Patrick Massot (May 08 2018 at 18:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vscode-lean%200.11.0/near/126272253):
https://github.com/leanprover/vscode-lean/commit/8a1e35e6495593620fbaacad5ff98929c15c7793#diff-66e057b4386ca2dfc39356a2fbecb4f2R354 is not good

#### [Patrick Massot (May 08 2018 at 18:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vscode-lean%200.11.0/near/126272297):
There can be space before the colon

#### [Patrick Massot (May 08 2018 at 18:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vscode-lean%200.11.0/near/126272300):
when several variables share a common type

#### [Patrick Massot (May 08 2018 at 18:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vscode-lean%200.11.0/near/126272324):
[bug.png](/user_uploads/3121/VUbq6QDeA0f2v-1YIVC0v3Vu/bug.png)

#### [Patrick Massot (May 08 2018 at 18:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vscode-lean%200.11.0/near/126272327):
But I do like this orange

#### [Patrick Massot (May 08 2018 at 18:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vscode-lean%200.11.0/near/126272394):
Also, you forgot the `|` showing current goal in conversion mode

#### [Patrick Massot (May 08 2018 at 18:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vscode-lean%200.11.0/near/126272404):
In my current version I gave it the same formatting as the ⊢

#### [Gabriel Ebner (May 08 2018 at 18:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vscode-lean%200.11.0/near/126272597):
Should be fixed now.

#### [Patrick Massot (May 08 2018 at 18:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vscode-lean%200.11.0/near/126272796):
Nice!

#### [Patrick Massot (May 08 2018 at 18:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vscode-lean%200.11.0/near/126272820):
oh oh...

#### [Patrick Massot (May 08 2018 at 18:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vscode-lean%200.11.0/near/126272857):
New bug

#### [Patrick Massot (May 08 2018 at 18:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vscode-lean%200.11.0/near/126272862):
I also had that one at some point

#### [Patrick Massot (May 08 2018 at 18:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vscode-lean%200.11.0/near/126272887):
[bug2.png](/user_uploads/3121/aLyRDIXg6KqbSFhRTd0_j6AI/bug2.png)

#### [Patrick Massot (May 08 2018 at 18:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vscode-lean%200.11.0/near/126272938):
I can see you are too much used to proved software. In the real world you need to test your software with real world data

#### [Sebastian Ullrich (May 08 2018 at 18:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vscode-lean%200.11.0/near/126272939):
It's spreading!

#### [Sebastian Ullrich (May 08 2018 at 18:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vscode-lean%200.11.0/near/126272963):
In Emacs, all flycheck errors are now highlighted with the Lean syntax highlighter btw

#### [Sebastian Ullrich (May 08 2018 at 18:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vscode-lean%200.11.0/near/126272964):
:)

#### [Patrick Massot (May 08 2018 at 18:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vscode-lean%200.11.0/near/126272967):
For the record, before you told us you 0.11.2 was out, the state of my regexs was:
```javascript
function formatTacticState(s: string): string {
    return s
        .replace(/^(\d+ goals)/g, '<strong class="goals-number">$1</strong> :')
        .replace(/^([^ ][^:\n⊢]*) :/g, '<strong class="context-element">$1</strong> :')
        .replace(/\n([^ ⊢][^:\n⊢]*) :/g, '\n<strong class="context-element">$1</strong> :')
        .replace(/^case ([^\n]*)/g, '<strong class="case">case $1</strong> :')
        .replace(/\ncase ([^\n]*)/g, '\n<strong class="case">case $1</strong> :')
        .replace(/^⊢/g, '<strong class="goal">⊢</strong>')
        .replace(/\n⊢/g, '\n<strong class="goal">⊢</strong>')
        .replace(/^\|/g, '<strong class="goal">|</strong>')
        .replace(/\n\|/g, '\n<strong class="goal">|</strong>')
        .replace(/no goals/g, '🎉 ');
}
```

#### [Patrick Massot (May 08 2018 at 18:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vscode-lean%200.11.0/near/126273026):
I should really try Lean in spacemacs at some point

#### [Patrick Massot (May 08 2018 at 18:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vscode-lean%200.11.0/near/126273030):
I don't why I'm affraid

#### [Sebastian Ullrich (May 08 2018 at 18:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vscode-lean%200.11.0/near/126273041):
I should really write a Lean spacemacs layer at some point

#### [Patrick Massot (May 08 2018 at 19:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vscode-lean%200.11.0/near/126273048):
Sebastian, do you have plans to make more structured tactic state output in Lean 4?

#### [Patrick Massot (May 08 2018 at 19:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vscode-lean%200.11.0/near/126273099):
Like, we wouldn't have to regex the output

#### [Patrick Massot (May 08 2018 at 19:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vscode-lean%200.11.0/near/126273115):
It could be useful also to build more powerful IDEs

#### [Patrick Massot (May 08 2018 at 19:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vscode-lean%200.11.0/near/126273165):
(where we could click on stuff in the tactic state and see cool things happen)

#### [Sebastian Ullrich (May 08 2018 at 19:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vscode-lean%200.11.0/near/126273244):
@**Patrick Massot** https://github.com/leanprover/lean/issues/1693

#### [Patrick Massot (May 08 2018 at 19:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vscode-lean%200.11.0/near/126273395):
Ok, I see you already discussed this quite a bit

#### [Patrick Massot (May 08 2018 at 19:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vscode-lean%200.11.0/near/126273404):
Is this in the Lean 4 TODO list then? I guess the priority is not super high

#### [Sebastian Ullrich (May 08 2018 at 19:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vscode-lean%200.11.0/near/126275103):
We're currently more focused on the structured traces (https://github.com/leanprover/lean/issues/1692) since that influences how we write Lean-in-Lean code. I suspect structured term output will come a bit later.

#### [Patrick Massot (May 08 2018 at 21:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vscode-lean%200.11.0/near/126279875):
Great

#### [Gabriel Ebner (May 09 2018 at 08:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vscode-lean%200.11.0/near/126301917):
```quote
I can see you are too much used to proved software. In the real world you need to test your software with real world data
```
:smile: We don't have a single test in vscode-lean.  But the new bug is fixed now.

#### [Kevin Buzzard (May 09 2018 at 08:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vscode-lean%200.11.0/near/126302503):
Patrick do you test your theorems about manifolds with real world data?

#### [Patrick Massot (May 09 2018 at 09:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vscode-lean%200.11.0/near/126303394):
Of course I do! How else could we get confidence in our theorems until proof assistants are ready for the real battlefield?

#### [Patrick Massot (May 09 2018 at 09:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vscode-lean%200.11.0/near/126303396):
Have a look at my latest preprint for instance

#### [Patrick Massot (May 09 2018 at 09:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vscode-lean%200.11.0/near/126303397):
The main result is checked against the canonical contact structures on spheres and projective spaces

#### [Patrick Massot (May 09 2018 at 09:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vscode-lean%200.11.0/near/126303450):
Conclusions were already known to hold for spheres and known not to hold for projective spaces (with the nice corollary that the hypothesis of the theorem does not hold for projective spaces, something that we have no other way to prove at the moment)

#### [Patrick Massot (May 09 2018 at 09:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vscode-lean%200.11.0/near/126303453):
Oh crap, my VScode doesn't like the tada unicode in the Tactic state window

#### [Patrick Massot (May 09 2018 at 09:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vscode-lean%200.11.0/near/126303456):
I forgot I kept that experiment in the regex I posted

#### [Gabriel Ebner (May 09 2018 at 09:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vscode-lean%200.11.0/near/126303546):
I tried it and the tada emoji works here, but I have a font installed for it.

#### [Gabriel Ebner (May 09 2018 at 09:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vscode-lean%200.11.0/near/126303661):
I have just enabled the highlighting for error messages as well.  It looks a bit weird for `#print` results, but I think it's a definite improvement for failed tactics.

#### [Mario Carneiro (May 09 2018 at 09:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vscode-lean%200.11.0/near/126303925):
I recommend against seriously using the tada emoji in the vscode extension

#### [Mario Carneiro (May 09 2018 at 09:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vscode-lean%200.11.0/near/126303926):
At least put it after the words "no goals"

#### [Gabriel Ebner (May 09 2018 at 09:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vscode-lean%200.11.0/near/126303990):
Yes, it comes right after the two words.  But I'll remove it.

#### [Patrick Massot (May 09 2018 at 17:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vscode-lean%200.11.0/near/126321127):
```quote
[bug2.png](/user_uploads/3121/aLyRDIXg6KqbSFhRTd0_j6AI/bug2.png)
```
This also happen in conversion mode...

#### [Patrick Massot (May 13 2018 at 22:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vscode-lean%200.11.0/near/126508439):
Here is tricky new bug: `#reduce λ x, x`. Maybe we should try to detect `information reduce result` on top

#### [Patrick Massot (May 23 2018 at 21:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vscode-lean%200.11.0/near/126992808):
@**Gabriel Ebner**  Same remark about detecting class instance trace (and probably also other kinds of traces?)

#### [Gabriel Ebner (May 24 2018 at 11:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vscode-lean%200.11.0/near/127021300):
We skip all information messages now.  I kind of liked it that `trace_state` was colorized, but we can't distinguish it from a class trace.

#### [Johan Commelin (May 25 2018 at 11:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vscode-lean%200.11.0/near/127073426):
I have no clue at all if this is possible: can you show matching parens in the goal. (So if I select one, the other gets some highlighting?)

#### [Gabriel Ebner (May 25 2018 at 11:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vscode-lean%200.11.0/near/127073444):
It's possible.  But we'd have to implement the highlight code ourselves (it's just an html page with javascript).

#### [Johan Commelin (May 25 2018 at 12:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vscode-lean%200.11.0/near/127073780):
Ok, but there is probably some js lib doing this already, right?

#### [Gabriel Ebner (May 25 2018 at 12:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vscode-lean%200.11.0/near/127074433):
I didn't find anything off-the-shelf after a quick search.  But it shouldn't be too hard.  Listen to mouse move events, if we're over a (, [, or { inside a `<pre>`, then look for a matching paren and put a `<span class='paren-highlighted'>` around it, and remove previous `.paren-highlighted` spans.

#### [Mario Carneiro (May 25 2018 at 12:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vscode-lean%200.11.0/near/127075431):
@**Gabriel Ebner** I have vscode-lean github downloaded and hooked up to my VSCode install, but I forget how to compile the extension from source. Could you remind me (and possibly put the instructions on the README)?

#### [Gabriel Ebner (May 25 2018 at 12:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vscode-lean%200.11.0/near/127075505):
The easiest way is to open the extension in vscode and press `F5`. This will compile it and start a new vscode window with the development version of the extension.  This is also documented in the README: https://github.com/leanprover/vscode-lean#development

