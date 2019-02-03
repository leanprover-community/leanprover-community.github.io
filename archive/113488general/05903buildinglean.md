---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/05903buildinglean.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [building lean](https://leanprover-community.github.io/archive/113488general/05903buildinglean.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Scott Morrison (Apr 04 2018 at 06:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/building%20lean/near/124608405):
<p>I've just updated the OS X command line tools, I get a million warnings when trying to build Lean:</p>
<div class="codehilite"><pre><span></span>/Users/scott/projects/lean/lean/src/util/small_object_allocator.h:42:71: warning: &#39;operator delete&#39; has a non-throwing exception specification but can still throw [-Wexceptions]
inline void operator delete(void *, lean::small_object_allocator &amp;) { lean_unreachable(); }
 ^
/Users/scott/projects/lean/lean/src/util/debug.h:23:156: note: expanded from macro &#39;lean_unreachable&#39;
#define lean_unreachable() { DEBUG_CODE({lean::notify_assertion_violation(__FILE__, __LINE__, &quot;UNREACHABLE CODE WAS REACHED.&quot;); lean::invoke_debugger();}) throw lean::unreachable_reached(); }
 ^
/Users/scott/projects/lean/lean/src/util/small_object_allocator.h:42:13: note: deallocator has a implicit non-throwing exception specification
inline void operator delete(void *, lean::small_object_allocator &amp;) { lean_unreachable(); }
 ^
/Users/scott/projects/lean/lean/src/util/small_object_allocator.h:43:73: warning: &#39;operator delete[]&#39; has a non-throwing exception specification but can still throw [-Wexceptions]
inline void operator delete[](void *, lean::small_object_allocator &amp;) { lean_unreachable(); }
 ^
/Users/scott/projects/lean/lean/src/util/debug.h:23:156: note: expanded from macro &#39;lean_unreachable&#39;
#define lean_unreachable() { DEBUG_CODE({lean::notify_assertion_violation(__FILE__, __LINE__, &quot;UNREACHABLE CODE WAS REACHED.&quot;); lean::invoke_debugger();}) throw lean::unreachable_reached(); }
 ^
</pre></div>

#### [ Scott Morrison (Apr 04 2018 at 06:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/building%20lean/near/124608407):
<p>Presumably we want to switch off these warnings?</p>


{% endraw %}
