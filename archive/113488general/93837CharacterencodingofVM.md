---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/93837CharacterencodingofVM.html
---

## Stream: [general](index.html)
### Topic: [Character encoding of VM](93837CharacterencodingofVM.html)

---

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Keeley Hoek (Aug 13 2018 at 15:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Character%20encoding%20of%20VM/near/132047636):
Does anyone know the internal character encoding of strings after a to_char_buffer? It seems to not be UTF-8.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Aug 13 2018 at 15:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Character%20encoding%20of%20VM/near/132047850):
`init.data.string.basic` says that it is

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sebastian Ullrich (Aug 13 2018 at 18:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Character%20encoding%20of%20VM/near/132056801):
`char` is a Unicode code point, so a `char_buffer` is not encoded at all

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Keeley Hoek (Aug 16 2018 at 18:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Character%20encoding%20of%20VM/near/132250034):
I think there is a serious problem in fs_write() in vm_io.cpp in the frozen final version of Lean 3.

Inside, there is a static_cast to <unsigned char>, which is just wrong when the passed char_buffer has some multibyte unicode characters.

The effect is that nonsense is written by io.fs.write when a char_buffer containing a character such as "𝟙" is passed. e.g. when you execute the following lean program the single byte 0xD9 is written.

````
def write_file (fn : string) (cnts : string) (mode := io.mode.write) : io unit := do
h ← io.mk_file_handle fn io.mode.write,
io.fs.write h cnts.to_char_buffer,
io.fs.close h

def main : io unit := do
  write_file "test.txt" "𝟙" 
````
I'm sure the fix won't be a big deal. Does anyone know of a workaround in the meantime?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sebastian Ullrich (Aug 16 2018 at 18:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Character%20encoding%20of%20VM/near/132250668):
Hmm, perhaps a `char_buffer` is supposed to be encoded in UTF-8 then after all. In that case, the bug is in `buffer.append_string`, which you could reimplement to do proper UTF-8 encoding

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Keeley Hoek (Aug 16 2018 at 18:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Character%20encoding%20of%20VM/near/132251650):
It looks to me like every time the vm needs to turn an honest std::string into a list of chars it does a utf8_decode (on purpose) to make sure a "char" is a single unicode character, so because char_buffer = buffer char I think that would be breaking the rules!

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Keeley Hoek (Aug 16 2018 at 18:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Character%20encoding%20of%20VM/near/132251818):
I would expect that fs_write should call some variant of push_unicode_scalar which pushes char into the temporary buffer it is building. Do you think it'd be okay if I made it do that?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sebastian Ullrich (Aug 16 2018 at 19:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Character%20encoding%20of%20VM/near/132252378):
Do you really want to change the Lean binary instead of fixing the issue in Lean code? This also won't work for `fs_read` since reading a fixed amount of bytes does not necessarily result in a correctly terminated UTF-8 string.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Keeley Hoek (Aug 16 2018 at 19:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Character%20encoding%20of%20VM/near/132252969):
I suppose you are right. But certainly the current behaviour is broken. It seems that there is some confusion as to whether a `char_buffer` should morally be a buffer of characters of text, or of bytes. Much effort is currently gone to to ensure that a `char` is a text-character, so that things like string.length can be the length of the underlying list of chars, etc.

I suppose in an ideal world io.fs.write would produce a `buffer byte`, and io.fs.read should return such a buffer (of course the latter of these actually happens currently, but everything is still called a `char`). And there would be `char_buffer.decode` or something.

One can only dream!

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sebastian Ullrich (Aug 16 2018 at 21:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Character%20encoding%20of%20VM/near/132259214):
Yes, it should look pretty much like this in Lean 4 :)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Keeley Hoek (Nov 23 2018 at 13:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Character%20encoding%20of%20VM/near/148225244):
Hi again @**Sebastian Ullrich**  sorry to resurrect this thread
At the original time of this thread I implemented the UTF-8 decoding you suggested, and we began to use it:
https://github.com/khoek/lean-tidy/blob/1fb088df379285f1d9cd303b129331f60c097fd9/src/tidy/lib/utf8.lean#L17
However we found that the decoder was slowing down the tactic it was part of (part of the visualizer for `rewrite_search`, so we just dropped labels altogether

However, now coming back to caching work for lean I'm having to serialize very large buffers of unicode characters to disk, to preserve the symbols in the names typed in various files, and the slowness has reared its head once again; encoding and saving an 11mb character buffer to disk takes under 1 second if I let lean corrupt it when writing normally, or more than five minutes (I didn't let it finish) if I map the UTF-8 decoder over it. Moreover, it's not the decoder implementation being slow---just asking that each `char` be replaced by its `nat` value as a string via mapping `char.val` over it (and trying to be efficient, appending each resulting `char` one-at-a-time and not doing list joins) takes this long too.

In comparison, parsing such a buffer into the `expr` it represents takes milliseconds.

This makes me very sad---would you at all consider merging a patch to lean which by default transcodes UTF-8 characters when reading and writing, when the file stream was opened in non-binary mode? The patch is under 100 lines. We address your `fs_read` problem above by reading the UTF-8 characters, making the length argument a number of UTF-8 characters, not just bytes (and again, this would only be in non-binary mode).

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sebastian Ullrich (Nov 23 2018 at 13:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Character%20encoding%20of%20VM/near/148226040):
I see. Do you have the patch somewhere?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Keeley Hoek (Nov 23 2018 at 14:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Character%20encoding%20of%20VM/near/148228670):
I'll extract a nice commit for you

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Keeley Hoek (Nov 24 2018 at 08:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Character%20encoding%20of%20VM/near/148267458):
@**Sebastian Ullrich** Sorry about the delay, here you go:
https://github.com/khoek/klean/commit/7d7abf9064297cd34186fad4a043fb7229bed9e8
I've stress-tested the read/write io calls on 100mb of utf8 nonsense, and everything was reproduced correctly without crashing

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Nov 24 2018 at 09:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Character%20encoding%20of%20VM/near/148267991):
Exciting! (especially if you know what comes next :-)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Keeley Hoek (Nov 26 2018 at 12:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Character%20encoding%20of%20VM/near/148362422):
@**Sebastian Ullrich** Sorry to keep bugging you
I have a tiny little puzzle you might be interested in. If you clone https://github.com/khoek/leandemo-for-sebastian and run `lean --make test.lean` (a program which just reads the accompanying file in the repo into memory) lean will finish executing essentially instantly.
On the other hand, try opening up `test.lean` in vscode. I observe a multiple-second pause when lean reads in the file in "interactive mode". Why could this discrepancy be happening?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Keeley Hoek (Nov 26 2018 at 12:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Character%20encoding%20of%20VM/near/148362472):
I measure less than 100ms in the first case

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sebastian Ullrich (Nov 26 2018 at 12:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Character%20encoding%20of%20VM/near/148362685):
Are you sure it's actually rebuilding the file?
```
$ time lean +3.4.1 test.lean
running
done
0.93user 0.58system 0:04.35elapsed 34%CPU (0avgtext+0avgdata 176204maxresident)k
0inputs+200outputs (77major+66430minor)pagefaults 0swaps
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Nov 26 2018 at 13:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Character%20encoding%20of%20VM/near/148362744):
Did you have any olean floating around Keeley?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Keeley Hoek (Nov 26 2018 at 13:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Character%20encoding%20of%20VM/near/148362996):
I got embarrassed for a second, but I don't think its an olean problem
What does "rebuilding" mean Sebastian?
But on my computer at the terminal I get
````
running
/home/khoek/code/lean/leandemo-for-sebastian/test.lean: parsing at line 145803226
done

real	0m0.876s
user	0m0.774s
sys	0m0.100s
````
(I made it print the number of bytes `5803226` read in there)
But in vscode I can comfortably count one-thousand-and-one one-thousand-and-two after I perturb the file
And if you make the file bigger (more MB) then it takes longer, too

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Keeley Hoek (Nov 26 2018 at 13:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Character%20encoding%20of%20VM/near/148363371):
copy-and-pasting the contents of the `test.dat` file a few times to get the file size up to 87mb, at the terminal it takes 1.967seconds to run, while in vscode it is more than 10

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sebastian Ullrich (Nov 26 2018 at 14:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Character%20encoding%20of%20VM/near/148367812):
@**Keeley Hoek** What do you get if you use `--server` like this?
```
echo '{"seq_num": 0, "command": "sync", "file_name": "test.lean"}' | time lean +3.4.1 --server
```
For me, it's about as fast after the first run (i.e. after the file cache is hot, probably)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Keeley Hoek (Nov 26 2018 at 14:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Character%20encoding%20of%20VM/near/148368092):
When I run that it starts/finishes really quick without printing `running` and `done`, so I don't think its actually running
I made sure to delete the olean file

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sebastian Ullrich (Nov 26 2018 at 15:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Character%20encoding%20of%20VM/near/148368796):
Ah, you should probably use `-j0` to force it into serial mode. I don't even remember half of these things.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Keeley Hoek (Nov 26 2018 at 15:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Character%20encoding%20of%20VM/near/148369274):
Yep that worked

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Keeley Hoek (Nov 26 2018 at 15:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Character%20encoding%20of%20VM/near/148369357):
14.14 seconds for the file in my repository (now updated, I made it way bigger)
2.348 from the terminal

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sebastian Ullrich (Dec 09 2018 at 22:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Character%20encoding%20of%20VM/near/151237681):
```quote
@**Sebastian Ullrich** Sorry about the delay, here you go:
https://github.com/khoek/klean/commit/7d7abf9064297cd34186fad4a043fb7229bed9e8
I've stress-tested the read/write io calls on 100mb of utf8 nonsense, and everything was reproduced correctly without crashing
```
 merged

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Dec 10 2018 at 13:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Character%20encoding%20of%20VM/near/151268884):
@**Keeley Hoek** did you see this?

