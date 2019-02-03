---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113489newmembers/93037unicodefontsforVScodeonmacOS.html
---

## Stream: [new members](https://leanprover-community.github.io/archive/113489newmembers/index.html)
### Topic: [unicode fonts for VS code on macOS](https://leanprover-community.github.io/archive/113489newmembers/93037unicodefontsforVScodeonmacOS.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Bryan Gin-ge Chen (Aug 15 2018 at 01:00)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/unicode%20fonts%20for%20VS%20code%20on%20macOS/near/132142135):
<p>Does anyone have any recommendations for macOS fonts that include all the unicode symbols in mathlib? On Windows the default fonts seem good so far but there are some missing symbols on macOS like <code>ₘ</code>.</p>

#### [ Edward Ayers (Aug 15 2018 at 01:10)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/unicode%20fonts%20for%20VS%20code%20on%20macOS/near/132142546):
<p>I'm also interested in font recomendations . On my mac <code>\I</code> and <code>i</code> look exactly the same which lead to some head scratching.</p>

#### [ Patrick Massot (Aug 15 2018 at 01:12)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/unicode%20fonts%20for%20VS%20code%20on%20macOS/near/132142574):
<p>Maybe you need OS recommendations <span class="emoji emoji-1f61c" title="stuck out tongue wink">:stuck_out_tongue_wink:</span></p>

#### [ Gabriel Ebner (Aug 15 2018 at 09:05)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/unicode%20fonts%20for%20VS%20code%20on%20macOS/near/132160189):
<p>Have you tried the 𝔘𝔫𝔦𝔠𝔬𝔡𝔢 𝔣𝔬𝔫𝔱 𝔰𝔲𝔤𝔤𝔢𝔰𝔱𝔦𝔬𝔫𝔰 for Linux?  From what I hear, these fonts run on macOS as well.</p>
<blockquote>
<p>Fonts with good unicode support (on Linux): "editor.fontFamily": "Source Code Pro Medium, DejaVu Sans Mono"</p>
</blockquote>

#### [ Sean Leather (Aug 15 2018 at 09:31)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/unicode%20fonts%20for%20VS%20code%20on%20macOS/near/132161106):
<p>Many of the monospace fonts I've tried on the Mac have a problem with <code>↪</code>: it takes more than the usual horizontal space, which leads to overlap with other characters. This includes Source Code Pro. I've been using Menlo, which has a good monospace <code>↪</code>. For some reason, I had not yet tried DejaVu Sans Mono. Now that I have, I see that it's very similar to Menlo. Both also have <code>ₘ</code>.</p>

#### [ Bryan Gin-ge Chen (Aug 15 2018 at 15:06)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/unicode%20fonts%20for%20VS%20code%20on%20macOS/near/132173504):
<p>Thanks, installing <a href="https://dejavu-fonts.github.io/" target="_blank" title="https://dejavu-fonts.github.io/">the DejaVu fonts</a> seems to have done the trick! I think Menlo doesn't actually have the <code>ₘ</code> character, since it's the default font for VS Code on macOS already (the default setting  is <code>"editor.fontFamily": "Menlo, Monaco, 'Courier New', monospace",</code>) and the character wasn't showing up before I installed these fonts. It seems that whenever a font is missing a glyph, the system fills it in from the other installed fonts (if it can).</p>

#### [ Sean Leather (Aug 15 2018 at 15:12)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/unicode%20fonts%20for%20VS%20code%20on%20macOS/near/132173814):
<p>Interesting. It seems you're right. I confirmed with Font Book. The Mac symbol viewer only shows the DejaVu fonts under Font Variation for <code>ₘ</code>. I previously checked in iTerm2, so, yeah, somebody must be filling in <code>ₘ</code> from some other font. I wonder where it's coming from.</p>


{% endraw %}
