---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113489newmembers/93037unicodefontsforVScodeonmacOS.html
---

## Stream: [new members](index.html)
### Topic: [unicode fonts for VS code on macOS](93037unicodefontsforVScodeonmacOS.html)

---


{% raw %}
#### [ Bryan Gin-ge Chen (Aug 15 2018 at 01:00)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/unicode%20fonts%20for%20VS%20code%20on%20macOS/near/132142135):
Does anyone have any recommendations for macOS fonts that include all the unicode symbols in mathlib? On Windows the default fonts seem good so far but there are some missing symbols on macOS like `ₘ`.

#### [ Edward Ayers (Aug 15 2018 at 01:10)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/unicode%20fonts%20for%20VS%20code%20on%20macOS/near/132142546):
I'm also interested in font recomendations . On my mac `\I` and `i` look exactly the same which lead to some head scratching.

#### [ Patrick Massot (Aug 15 2018 at 01:12)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/unicode%20fonts%20for%20VS%20code%20on%20macOS/near/132142574):
Maybe you need OS recommendations :stuck_out_tongue_wink:

#### [ Gabriel Ebner (Aug 15 2018 at 09:05)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/unicode%20fonts%20for%20VS%20code%20on%20macOS/near/132160189):
Have you tried the 𝔘𝔫𝔦𝔠𝔬𝔡𝔢 𝔣𝔬𝔫𝔱 𝔰𝔲𝔤𝔤𝔢𝔰𝔱𝔦𝔬𝔫𝔰 for Linux?  From what I hear, these fonts run on macOS as well.
```quote
Fonts with good unicode support (on Linux): "editor.fontFamily": "Source Code Pro Medium, DejaVu Sans Mono"
```

#### [ Sean Leather (Aug 15 2018 at 09:31)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/unicode%20fonts%20for%20VS%20code%20on%20macOS/near/132161106):
Many of the monospace fonts I've tried on the Mac have a problem with `↪`: it takes more than the usual horizontal space, which leads to overlap with other characters. This includes Source Code Pro. I've been using Menlo, which has a good monospace `↪`. For some reason, I had not yet tried DejaVu Sans Mono. Now that I have, I see that it's very similar to Menlo. Both also have `ₘ`.

#### [ Bryan Gin-ge Chen (Aug 15 2018 at 15:06)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/unicode%20fonts%20for%20VS%20code%20on%20macOS/near/132173504):
Thanks, installing [the DejaVu fonts](https://dejavu-fonts.github.io/) seems to have done the trick! I think Menlo doesn't actually have the `ₘ` character, since it's the default font for VS Code on macOS already (the default setting  is `"editor.fontFamily": "Menlo, Monaco, 'Courier New', monospace",`) and the character wasn't showing up before I installed these fonts. It seems that whenever a font is missing a glyph, the system fills it in from the other installed fonts (if it can).

#### [ Sean Leather (Aug 15 2018 at 15:12)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/unicode%20fonts%20for%20VS%20code%20on%20macOS/near/132173814):
Interesting. It seems you're right. I confirmed with Font Book. The Mac symbol viewer only shows the DejaVu fonts under Font Variation for `ₘ`. I previously checked in iTerm2, so, yeah, somebody must be filling in `ₘ` from some other font. I wonder where it's coming from.


{% endraw %}
