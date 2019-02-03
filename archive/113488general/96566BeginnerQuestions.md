---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/96566BeginnerQuestions.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [Beginner Questions](https://leanprover-community.github.io/archive/113488general/96566BeginnerQuestions.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Clyde Watson (Jun 28 2018 at 04:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Beginner%20Questions/near/128751244):
<p>I'm really new to LEAN (and anything like it), and I've had some problems that might be considered a little too simple.</p>

#### [ Clyde Watson (Jun 28 2018 at 04:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Beginner%20Questions/near/128751249):
<p>Questions answered so far:</p>
<p>Let's say that I declared a variable a of type int. How do I attribute a value to it (let's say, 3)?</p>
<p>How would I define a function that searches for a given object in a list?</p>
<p>How do I know that I've reached the end of a list? I want to know this in order to compare if two strings have the same characters at the same positions.</p>
<p>Is there a document where I can check all the avaliable commands for Lean?</p>
<p>How would I declare a local variable inside a function?</p>
<p>New Questions:</p>
<p>Do string and list char represent the same type?</p>
<p>That's it, for now. Thank you all for your time and patience :)</p>

#### [ Simon Hudon (Jun 28 2018 at 05:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Beginner%20Questions/near/128751446):
<p>First question: you want a definition. You do it with <code>def my_def : int := 7</code></p>

#### [ Clyde Watson (Jun 28 2018 at 05:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Beginner%20Questions/near/128751738):
<p>Thank you for that, Simon!</p>

#### [ Simon Hudon (Jun 28 2018 at 05:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Beginner%20Questions/near/128751894):
<p>Second question: </p>
<div class="codehilite"><pre><span></span><span class="n">def</span> <span class="n">find</span> <span class="o">(</span><span class="n">x</span> <span class="o">:</span> <span class="n">nat</span><span class="o">)</span> <span class="o">:</span> <span class="n">list</span> <span class="n">nat</span> <span class="bp">-&gt;</span> <span class="n">option</span> <span class="n">nat</span>
<span class="bp">|</span> <span class="o">[]</span> <span class="o">:=</span> <span class="n">none</span>
<span class="bp">|</span> <span class="o">(</span><span class="n">y</span> <span class="bp">::</span> <span class="n">ys</span><span class="o">)</span> <span class="o">:=</span>
<span class="k">if</span> <span class="n">x</span> <span class="bp">=</span> <span class="n">y</span> <span class="k">then</span> <span class="n">some</span> <span class="mi">0</span>
         <span class="k">else</span> <span class="n">do</span> <span class="n">r</span> <span class="bp">&lt;-</span> <span class="n">find</span> <span class="n">ys</span>
                 <span class="n">return</span> <span class="o">(</span><span class="n">r</span> <span class="bp">+</span> <span class="mi">1</span><span class="o">)</span>
</pre></div>

#### [ Clyde Watson (Jun 28 2018 at 05:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Beginner%20Questions/near/128752529):
<p>Thanks again! <span class="emoji emoji-1f642" title="simple smile">:simple_smile:</span> I will try to understand the code.</p>

#### [ Simon Hudon (Jun 28 2018 at 05:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Beginner%20Questions/near/128752644):
<p>Don't hesitate to ask more questions. I tried to put as little mysterious stuff as possible but I think if you're not a Haskell adept, <code>do</code>, <code>&lt;-</code>  and <code>return</code> are not obvious.</p>

#### [ Mario Carneiro (Jun 28 2018 at 07:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Beginner%20Questions/near/128754968):
<blockquote>
<p>First one: Let's say that I declared a variable a of type int. How do I attribute a value to it (let's say, 3)?</p>
</blockquote>
<p>The first thing to understand about lean is that it is a <em>functional programming language</em>. If you are used to a more traditional imperative programming language, like C, Java, Python, etc, then there is a bit of culture shock to be had. The big thing to know is that there are no "variables* in lean in the sense meant by this word in imperative languages. (My professor always said this was a bad name for them and preferred the term "assignable" for C/Java style mutable memory locations.) In lean, variables are things that you can substitute values for, but their values never change from the time they are declared. In an imperative language you would call these immutable variables, but there are no mutable variables in lean.</p>
<p>To declare a variable and give it a value, you can use <code>let</code>:</p>
<div class="codehilite"><pre><span></span>def f (x : nat) : nat :=
let y := 3 in ...
</pre></div>


<p>Here <code>f</code> is a function with an input variable of type <code>nat</code>, and inside the body of the function I've declared a variable <code>y</code> (also of type <code>nat</code>) with value <code>3</code>.</p>

#### [ Mario Carneiro (Jun 28 2018 at 07:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Beginner%20Questions/near/128755050):
<blockquote>
<p>Second one: How would I define a function that searches for a given object in a list?</p>
<p>Third, that's related to the second one: How do I know that I've reached the end of a list? I want to know this in order to compare if two strings have the same characters at the same positions.</p>
</blockquote>
<p>Usually, a function which is defined on lists will be done by pattern matching, as in Simon's code. This is done in the first two lines, with <code>| [] :=</code> and <code>| (y :: ys) :=</code>. This says what to do if the list is empty, and what to do if it is nonempty with head <code>y</code> and tail <code>ys</code>. Defining the function this way automatically takes care of "knowing when I've reached the end of a list", because you can't even get the value from a list unless you are already in the nonempty case - the nonempty check and value retrieval happen at the same time.</p>

#### [ Mario Carneiro (Jun 28 2018 at 07:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Beginner%20Questions/near/128755147):
<p>Here's a function that compares two strings and returns true iff they are equal:</p>
<div class="codehilite"><pre><span></span>def is_equal : list char → list char → bool
| []        []        := tt
| (x :: xs) []        := ff
| []        (y :: ys) := ff
| (x :: xs) (y :: ys) := (x = y) &amp;&amp; is_equal xs ys
</pre></div>

#### [ Mario Carneiro (Jun 28 2018 at 07:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Beginner%20Questions/near/128755265):
<blockquote>
<p>Fourth: Is there a document where I can check all the avaliable commands for Lean?</p>
</blockquote>
<p>This depends on what you mean by "command". There are relatively few actual keywords recognized by the lean language, and you can find a relatively complete list in chapters 4 and 5 of the <a href="https://leanprover.github.io/reference/" target="_blank" title="https://leanprover.github.io/reference/">lean reference manual</a>.</p>

#### [ Mario Carneiro (Jun 28 2018 at 07:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Beginner%20Questions/near/128755374):
<blockquote>
<p>Fifth: How would I declare a local variable inside a function? I tried doing the following:</p>
</blockquote>
<div class="codehilite"><pre><span></span>def example_def (a : int) : int :=
variable k : int
</pre></div>


<blockquote>
<p>I have a feeling that I might have to use let k := int in ..., but I'm not really sure.</p>
</blockquote>
<p>Since as mentioned there is no such thing as a local assignable in lean, the best you can do is to have a <code>let</code> declaration, which also requires that you provide the local variable with a value. This is because unlike most pointer based languages, there is no "universal null" value in all types - the values of a type are all explicitly determined by the type. So if you define a variable of type <code>int</code>, then it must contain an integer value, maybe <code>0</code> or <code>42</code> or something but "unassigned" is not an option. <code>let k := int</code> actually declares <code>k</code> to be a variable of type <code>Type</code> with value <code>int</code>, which is probably not what you want.</p>

#### [ Clyde Watson (Jun 29 2018 at 03:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Beginner%20Questions/near/128804676):
<blockquote>
<p>Don't hesitate to ask more questions. I tried to put as little mysterious stuff as possible but I think if you're not a Haskell adept, <code>do</code>, <code>&lt;-</code>  and <code>return</code> are not obvious.</p>
</blockquote>
<p>You are right, it isn't that obvious. What does "some 0" mean?<br>
I'm having some trouble understand the "do r &lt;- find ys return (r +1)" part.  Isn't find missing one argument, that is, the x that it's searching? Also, for some reason, Lean considers ys to have the type "option nat".</p>

#### [ Clyde Watson (Jun 29 2018 at 03:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Beginner%20Questions/near/128804735):
<p>Thanks a lot for all the explanations, Mario! It really is a shock. It's the first time I'm seeing a functional programming language.</p>

#### [ Clyde Watson (Jun 29 2018 at 03:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Beginner%20Questions/near/128804790):
<blockquote>
<p>Here's a function that compares two strings and returns true iff they are equal:</p>
</blockquote>
<p>def is_equal : list char → list char → bool<br>
| []        []        := tt<br>
| (x :: xs) []        := ff<br>
| []        (y :: ys) := ff<br>
| (x :: xs) (y :: ys) := (x = y) &amp;&amp; is_equal xs ys</p>
<div class="codehilite"><pre><span></span>
</pre></div>


<p>So, according to the piece of code you sent, whenever I want to compare two kinds of lists, I only have to "place them" side by side?</p>

#### [ Clyde Watson (Jun 29 2018 at 03:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Beginner%20Questions/near/128805114):
<p>One new quesion: In Lean, are there any differences between string and list char?</p>

#### [ Simon Hudon (Jun 29 2018 at 03:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Beginner%20Questions/near/128805586):
<blockquote>
<p>You are right, it isn't that obvious. What does "some 0" mean?</p>
</blockquote>
<p><code>some 0</code> could also be written <code>return 0</code>. Both are expressions of type <code>option nat</code>. <code>option nat</code> has two kinds of values <code>none</code> or <code>some n</code> where <code>n</code> is a natural number. That means <code>option nat</code> either contains a single natural number or nothing. <code>return 0</code> comes in handy when you think of <code>option nat</code> as a sequential program that may fail or return a natural number. This leads us to your second question:</p>
<blockquote>
<p>I'm having some trouble understand the "do r &lt;- find ys return (r +1)" part. Isn't find missing one argument, that is, the x that it's searching? Also, for some reason, Lean considers ys to have the type "option nat".</p>
</blockquote>
<p>I apologize, the expression has a syntax error in it. It should be <code>do r &lt;- find ys, return (r +1)</code> (notice the comma in the middle). You can read it as "call <code>find ys</code> then, if it doesn't fail (i.e. produce the value <code>none</code>) take the result (a natural number), call it <code>r</code> and return from the sequence of two instructions with the value of <code>r+1</code>"</p>

#### [ Sean Leather (Jun 29 2018 at 08:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Beginner%20Questions/near/128813110):
<blockquote>
<p>One new quesion: In Lean, are there any differences between string and list char?</p>
</blockquote>
<p>This is extracted from the core library (<a href="https://github.com/leanprover/lean/blob/master/library/init/data/string/basic.lean#L10-L18" target="_blank" title="https://github.com/leanprover/lean/blob/master/library/init/data/string/basic.lean#L10-L18"><code>init/data/string/basic.lean</code></a>):</p>
<div class="codehilite"><pre><span></span><span class="c">/-</span><span class="cm"> In the VM, strings are implemented using a dynamic array and UTF-8 encoding. -/</span>
<span class="kn">structure</span> <span class="n">string_imp</span> <span class="o">:=</span> <span class="o">(</span><span class="n">data</span> <span class="o">:</span> <span class="n">list</span> <span class="n">char</span><span class="o">)</span>
<span class="n">def</span> <span class="n">string</span> <span class="o">:=</span> <span class="n">string_imp</span>
</pre></div>

#### [ Mario Carneiro (Jun 29 2018 at 08:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Beginner%20Questions/near/128814743):
<blockquote>
<p>So, according to the piece of code you sent, whenever I want to compare two kinds of lists, I only have to "place them" side by side?</p>
</blockquote>
<p>That's the way pattern match syntax works. In this case, since the type of the function is <code>is_equal : list char → list char → bool</code>, there are two arguments, both lists of chars, and so each case should include two variables, possibly broken into cases. In my code snippet I broke into all four cases, but you can combine some of them with wildcards <code>_</code>, depending on the function you are defining. You should read the second case <code>| (x :: xs) [] := ff</code> as being shorthand for the partial specification <code>is_equal (x :: xs) [] = ff</code> of the function <code>is_equal</code>.</p>

#### [ Mario Carneiro (Jun 29 2018 at 08:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Beginner%20Questions/near/128814833):
<blockquote>
<p>One new quesion: In Lean, are there any differences between string and list char?</p>
</blockquote>
<p>Just to unpack Sean's answer a bit: In lean, a string is a wrapper around a <code>list char</code>. The wrapper is there because there is a change of underlying data representation - I believe <code>string</code> is stored as an array of bytes, while <code>list char</code> is a linked list, like all <code>list</code> structures.</p>
<p>In fact, the whole function <code>is_equal</code> already exists in lean so you don't need to define it - it's just <code>a = b</code> where <code>a b : string</code>. Pretty much all data types defined in lean have an equality test implemented, and you can write equality tests for your own data structures easily as well.</p>

#### [ Mario Carneiro (Jun 29 2018 at 09:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Beginner%20Questions/near/128815011):
<p>Here's another way to write Simon's <code>find</code> function using pattern matching instead of monad notation:</p>
<div class="codehilite"><pre><span></span>def find (x : nat) : list nat -&gt; option nat
| [] := none
| (y :: ys) :=
  if x = y then some 0 else
  match find ys with
  | none := none
  | some r := some (r + 1)
  end
</pre></div>


<p>The <code>match</code> acts just like the top level pattern match - it takes the result of <code>find ys</code>, which is an <code>option nat</code>, and breaks into cases depending on if it is <code>none</code> or <code>some r</code> for some <code>r</code>. I mentioned before that lean has no "universal null" value, but when you explicitly want to indicate a "null" value, you do it with the <code>option</code> type. Essentially, this function either returns a result, wrapped in <code>some</code>, or it returns failure to find the value, encoded as <code>none</code> here (you might use "null" for this in other languages).</p>

#### [ Kevin Buzzard (Jun 29 2018 at 09:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Beginner%20Questions/near/128816419):
<p><span class="user-mention" data-user-id="120239">@Clyde Watson</span> I started with Lean after very little functional programming experience (I knew some python / java but only as a hobbyist; I am a professional mathematician). I found <a href="http://learnyouahaskell.com/" target="_blank" title="http://learnyouahaskell.com/">http://learnyouahaskell.com/</a> extremely helpful. Your questions about basic pattern matching seem to indicate that you might be able to learn a lot from this resource (or from some other Haskell learning resources, if the informality of this one is not to your taste). Basically the rule is that if you're defining functions on, or proving things about, so-called "inductive types" like the natural numbers or lists, then you use induction (or recursion), and a syntax which is a completely basic part of functional programming with these "|"s.</p>

#### [ Mario Carneiro (Jun 29 2018 at 10:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Beginner%20Questions/near/128816592):
<p>terminology note: In Haskell, what we call "inductive types" are called (generalized) algebraic data types or GADTs</p>

#### [ Sean Leather (Jun 29 2018 at 13:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Beginner%20Questions/near/128823178):
<blockquote>
<p>I started with Lean after very little functional programming experience (I knew some python / java but only as a hobbyist; I am a professional mathematician). I found <a href="http://learnyouahaskell.com/" target="_blank" title="http://learnyouahaskell.com/">http://learnyouahaskell.com/</a> extremely helpful.</p>
</blockquote>
<p><span class="user-mention" data-user-id="110038">@Kevin Buzzard</span> That's pretty cool that you used Learn You a Haskell for Great Good. Did you learn Haskell first and then move to Lean or use it as a tutorial about the related concepts in Lean?</p>

#### [ Kevin Buzzard (Jun 29 2018 at 13:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Beginner%20Questions/near/128823396):
<p>I am not sure I have learnt Haskell in any real sense. The reason I mentioned it was that the website I mentioned showed me how to define functions on lists by recursion using exactly the notation that the OP was originally asking about. Basically my history was: hobbyist programmer (written simple Android apps in java etc), then in 2016 I attempted to read learnyouahaskell just because (a) I knew the people on our joint maths and computing degree had to learn it in their first term and (b) I'd had an undergraduate doing a maths project with me on elliptic curves and they'd used Haskell to write their code, and then later in 2016 I tried reading it again, and then in 2017 I started trying to code in Lean and then I went back to it for a third time and this time it all made sense. But the concept of defining a function on lists by defining it on the constructors was something which dawned on me on the first reading.</p>

#### [ Reid Barton (Jun 29 2018 at 21:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Beginner%20Questions/near/128845444):
<blockquote>
<p>Isn't find missing one argument</p>
</blockquote>
<p>This is a syntactic oddity of lean--when referring to the thing currently being defined (here <code>find</code>) inside its own definition, parameters to the left of the colon (here <code>(x : nat)</code>) are fixed, and you don't even write them.</p>

#### [ Reid Barton (Jun 29 2018 at 21:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Beginner%20Questions/near/128845733):
<p>So <code>find ys</code> inside the definition of <code>find</code> means the same as <code>find x ys</code> outside it</p>

#### [ Kevin Buzzard (Jun 30 2018 at 00:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Beginner%20Questions/near/128853494):
<blockquote>
<p>What does "some 0" mean?</p>
</blockquote>
<p>I'll show you how to figure this out yourself!</p>
<p>One really important thing to learn in Lean is that every question of this form is a question which you can begin to investigate yourself, and the sooner you learn how to do this the sooner you can figure out what you need to learn next; you can ask really targetted questions which in general receive better answers. </p>
<p>Here's how you can use Lean to answer your own question, in VS Code. First open a completely new file called scratch.lean and let's see if we can isolate your question. Make this as the only line:</p>
<p><code>definition X := some 0</code></p>
<p>It works! </p>
<p>[technical note: This isn't always the case -- sometimes the thing you're trying to understand might rely on some file being imported or some namespace being open and you'll have to resort to right-clicking -- see later.]</p>
<p>Now we have <code>X</code> we can see what this <code>some</code> command really is -- it's defined in the root namespace and is in core lean, so it's probably important. </p>
<p>Now we can write stuff like</p>
<p><code>#check X</code></p>
<p>to see that <code>X</code> is a term of type <code>option ℕ</code>. So it looks like <code>option</code> is a function which eats <code>ℕ</code>. What is the type of <code>ℕ</code>? We just check with</p>
<p><code>#check ℕ</code></p>
<p>and we see that <code>ℕ</code> has type <code>Type</code>. So <code>option</code> is a function which eats something of type <code>Type</code>. We can look at what <code>option</code> is with</p>
<p><code>#check option </code></p>
<p>and we see it's a function from <code>Type</code> to <code>Type</code> (just ignore the universes, you can worry about these later). So <code>some 0</code> is a term of type <code>option ℕ</code>which has type <code>Type</code>. So that's where <code>some 0</code> lives in the tree of terms, types and universes.</p>
<p>[Pro tip: always be checking there are no red underlines in your code. Sometimes random typos which you don't bother to fix can have weird consequences later on. Learn how to use <code>sorry</code> to fix red errors in half-written code]</p>
<p>We didn't look at any definitions yet, we just looked at the types of everything in sight. Everything has a type, and <code>#check x</code> tells you the type of <code>x</code>. Here is a simple picture of the entire type theory of Lean. There are six kinds of things. There are two universes, <code>Type</code> and <code>Prop</code>. A type is something of type <code>Type</code>, and a term is something of type <code>α</code> for <code>α</code> a type. A proposition is something of type <code>Prop</code>, and a proof is something of type <code>H</code> for <code>H</code> a proposition. That's it. The <code>Type</code> stuff is where computer programs live. <code>Prop</code> is where theorems and proofs live. So <code>some 0</code> is a computable thing, it's a term of type <code>option ℕ : Type</code>. </p>
<p>Next let's actually unravel the definitions. Right-click on <code>some</code> in VS Code and select <code>Go to definition</code> (or left-click and press F12). A new file will open called <code>core.lean</code> and you'll be taken to about line 279 where you'll see that <code>option α</code> is an inductive type with two constructors: <code>none</code> and <code>some val</code> with <code>val : α</code>. So in abstracta your question is answered -- <code>some</code> is a constructor which takes <code>n : ℕ</code> and returns <code>some n : option ℕ</code>. We can just check that with </p>
<p><code>#check some</code></p>
<p>and the answer...looks a bit messy. It's clearly some kind of function, but there are question marks. If you don't like those <code>?M_1</code> things, you could use the following trick:</p>
<p><code>#check @some</code></p>
<p>which works with functions and which might produce nicer output. Now we see that <code>some</code> is actually a Pi type.</p>
<p>Here's a gist with all those commands in. One of the fiddly little VS Code options on the right is "show the output of all the <code>#check</code>s at once"; that might be the one you want here.</p>
<p><a href="https://gist.github.com/kbuzzard/455709bfd5d8fed57f5e4321481adf5b" target="_blank" title="https://gist.github.com/kbuzzard/455709bfd5d8fed57f5e4321481adf5b">https://gist.github.com/kbuzzard/455709bfd5d8fed57f5e4321481adf5b</a></p>
<p>If you get stuck at some point, send the entire file as a gist (just google for how to do it) or, if it's got quite big, just a minimal working example of your question. It's much easier for experts to answer questions with the full file in front of them. Even experts make silly mistakes sometimes, which others can spot instantly. Actually, sometimes I find my own silly mistakes when I am making the minimal working example. And did I mention to make sure there are no errors in your file?</p>
<p>So that's <code>option</code>, and how to ask if you get stuck along the way. But if you want some more insight as to what the point of this type is, or perhaps want to know more about what an inductive type is or a Pi type, or what the different kinds of brackets all mean (round, squiggly, square), now is the time to go to the docs -- Theorem Proving In Lean is a really good place to look for basic stuff. It's here:</p>
<p><a href="https://leanprover.github.io/theorem_proving_in_lean/" target="_blank" title="https://leanprover.github.io/theorem_proving_in_lean/">https://leanprover.github.io/theorem_proving_in_lean/</a></p>
<p>I find the web search functionality really hard to use though; there's a pdf download and I usually search with my pdf viewer and then maybe switch to the html manual later because it looks nicer, if I want to know more. If you want to know more about <code>option</code> then the fourth occurrence of " option " in the pdf is the one you want; it's on p101. There you can see a brief description of the point of <code>option</code> and examples of other inductive types which have similar structures. I wish I had learnt this method earlier -- it took a while to dawn on me that you could just work everything out by right clicking and figuring out if you were a term or a type, a proof or a proposition.</p>
<p>You also need to learn a kind of filter -- stuff you can just ignore for the time being.  Stuff like typeclasses, <code>opt_param</code>/<code>out_param</code>, <code>[stuff in brackets]</code> and universes, you can start to worry about them later. Universes are to do with subtle set-theoretic issues like avoiding Russell's Paradox, and the other stuff is technical computer science stuff which you can just treat as magic for the time being. [Typeclasses are some crazy computer science generalisation of notation overloading]</p>

#### [ Amin Bandali (Jun 30 2018 at 15:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Beginner%20Questions/near/128879959):
<p>Another beginner question here: Is it possible to "overload" an instance?</p>
<p><code>format</code> has an instance for <code>list α</code>:<br>
<a href="https://github.com/leanprover/lean/blob/e53f8021ec3bd8b6c7c2eb998932ec79cb941b18/library/init/meta/format.lean#L87-L92" target="_blank" title="https://github.com/leanprover/lean/blob/e53f8021ec3bd8b6c7c2eb998932ec79cb941b18/library/init/meta/format.lean#L87-L92">https://github.com/leanprover/lean/blob/e53f8021ec3bd8b6c7c2eb998932ec79cb941b18/library/init/meta/format.lean#L87-L92</a><br>
And I'd like to customize that in various places. For instance, say, I'd want to drop the outer square brackets, or another time make the items semicolon-separated rather than comma-separated</p>

#### [ Simon Hudon (Jun 30 2018 at 17:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Beginner%20Questions/near/128884679):
<p>It is possible but I wouldn't advise using it that way. Instead, you should explicitly invoke the formatting code that you're interested in. Just to be sure, can you show an example where that would be handy?</p>

#### [ Amin Bandali (Jun 30 2018 at 17:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Beginner%20Questions/near/128884895):
<p>I see. The example I was aiming to use that for was a <code>structure</code> with a <code>(exts : list string)</code> field, which I wanted format using <code>format!"EXTENDS {my_struct.exts}"</code></p>

#### [ Simon Hudon (Jun 30 2018 at 17:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Beginner%20Questions/near/128885052):
<p>Yes, that's what I thought. If you replace <code>format!"EXTENDS {my_struct.exts}"</code> with `format!"EXTENDS {my_to_fmt my_struct.exts}" you should get the same result. Unlike in Haskell, Lean doesn't guarantee global uniqueness of instances so you have to be vigilant not to make the instance search more difficult</p>

#### [ Amin Bandali (Jun 30 2018 at 18:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Beginner%20Questions/near/128885421):
<p>Thanks for the explanations <span class="emoji emoji-1f642" title="simple smile">:simple_smile:</span>  makes sense</p>

#### [ Guy Leroy (Jul 03 2018 at 11:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Beginner%20Questions/near/129013476):
<p>Hi, I'm following a simple tutorial for Lean and an exercice is to define a curry function and an uncurry function.<br>
Could anyone help me with this please?</p>
<p>def curry (α β γ : Type) (f : α × β → γ) : α → β → γ := sorry<br>
def uncurry (α β γ : Type) (f : α → β → γ) : α × β → γ := sorry</p>

#### [ Chris Hughes (Jul 03 2018 at 12:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Beginner%20Questions/near/129013840):
<p>If you have <code>a : α</code> and <code>b : β</code> then I can make an element of type <code>α × β</code> by writing <code>⟨a, b⟩</code>. The pointy bracket is written with <code>\&lt;</code>. If I have <code>x : α × β</code>, then <code>x.1</code> is the first element of the pair and <code>x.2</code> is the second element.</p>

#### [ Guy Leroy (Jul 03 2018 at 12:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Beginner%20Questions/near/129014538):
<p>Oh thank you. I am still struggling though, the best I came up with is:</p>
<p>def curry (α β γ : Type) (f : α × β → γ) : α → β → γ := λ f x, f x.1 x.2 <br>
def uncurry (α β γ : Type) (f : α → β → γ) : α × β → γ := λ f a b, f ⟨a, b⟩  </p>
<p>which is obvisouly wrong  as the types don't match but I can't figure out how to make it work</p>

#### [ Guy Leroy (Jul 03 2018 at 12:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Beginner%20Questions/near/129014608):
<p>Any other hint?</p>

#### [ Mario Carneiro (Jul 03 2018 at 12:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Beginner%20Questions/near/129014636):
<p>Your answers are perfect, except they are swapped</p>

#### [ Sean Leather (Jul 03 2018 at 12:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Beginner%20Questions/near/129014639):
<p>To add to Chris's answer, there are a couple of things you can do to learn what you need to do.</p>
<ul>
<li><code>×</code> is notation for <code>prod</code>. How would you know this? You can do <code>#print ×</code> in a file and see <code>_ </code>×<code>:35 _:34 := prod #1 #0</code>.</li>
<li>Want to find out more about <code>prod</code>, use <code>#print prod</code>.</li>
</ul>
<div class="codehilite"><pre><span></span><span class="bp">@</span><span class="o">[</span><span class="n">derive</span> <span class="n">list</span><span class="bp">.</span><span class="n">cons</span><span class="bp">.</span><span class="o">{</span><span class="mi">0</span><span class="o">}</span> <span class="n">pexpr</span> <span class="bp">``</span><span class="o">(</span><span class="n">has_reflect</span><span class="o">)</span> <span class="o">(</span><span class="n">list</span><span class="bp">.</span><span class="n">nil</span><span class="bp">.</span><span class="o">{</span><span class="mi">0</span><span class="o">}</span> <span class="n">pexpr</span><span class="o">)]</span>
<span class="kn">structure</span> <span class="n">prod</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span> <span class="bp">→</span> <span class="kt">Type</span> <span class="n">v</span> <span class="bp">→</span> <span class="kt">Type</span> <span class="o">(</span><span class="n">max</span> <span class="n">u</span> <span class="n">v</span><span class="o">)</span>
<span class="n">fields</span><span class="o">:</span>
<span class="n">prod</span><span class="bp">.</span><span class="n">fst</span> <span class="o">:</span> <span class="bp">Π</span> <span class="o">{</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">}</span> <span class="o">{</span><span class="n">β</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">v</span><span class="o">},</span> <span class="n">α</span> <span class="bp">×</span> <span class="n">β</span> <span class="bp">→</span> <span class="n">α</span>
<span class="n">prod</span><span class="bp">.</span><span class="n">snd</span> <span class="o">:</span> <span class="bp">Π</span> <span class="o">{</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">}</span> <span class="o">{</span><span class="n">β</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">v</span><span class="o">},</span> <span class="n">α</span> <span class="bp">×</span> <span class="n">β</span> <span class="bp">→</span> <span class="n">β</span>
</pre></div>


<ul>
<li><code>structure</code>s have a default constructor <code>mk</code>. Try <code>#print prod.mk</code>.</li>
<li>Lastly, <code>⟨a, ..., z⟩</code> is the anonymous constructor that works for many structures and types.</li>
</ul>

#### [ Chris Hughes (Jul 03 2018 at 12:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Beginner%20Questions/near/129014717):
<p>They're not quite perfect. You need to get rid of the <code>f</code>s in the lambdas. In lean syntax anything before the colon doesn't need to be introduced with a lambda.</p>

#### [ Chris Hughes (Jul 03 2018 at 12:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Beginner%20Questions/near/129014776):
<p>This is correct.</p>
<div class="codehilite"><pre><span></span><span class="n">def</span> <span class="n">curry</span> <span class="o">(</span><span class="n">α</span> <span class="n">β</span> <span class="n">γ</span> <span class="o">:</span> <span class="kt">Type</span><span class="o">)</span> <span class="o">(</span><span class="n">f</span> <span class="o">:</span> <span class="n">α</span> <span class="bp">×</span> <span class="n">β</span> <span class="bp">→</span> <span class="n">γ</span><span class="o">)</span> <span class="o">:</span> <span class="n">α</span> <span class="bp">→</span> <span class="n">β</span> <span class="bp">→</span> <span class="n">γ</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">a</span> <span class="n">b</span><span class="o">,</span> <span class="n">f</span> <span class="bp">⟨</span><span class="n">a</span><span class="o">,</span> <span class="n">b</span><span class="bp">⟩</span>
<span class="n">def</span> <span class="n">uncurry</span> <span class="o">(</span><span class="n">α</span> <span class="n">β</span> <span class="n">γ</span> <span class="o">:</span> <span class="kt">Type</span><span class="o">)</span> <span class="o">(</span><span class="n">f</span> <span class="o">:</span> <span class="n">α</span> <span class="bp">→</span> <span class="n">β</span> <span class="bp">→</span> <span class="n">γ</span><span class="o">)</span> <span class="o">:</span> <span class="n">α</span> <span class="bp">×</span> <span class="n">β</span> <span class="bp">→</span> <span class="n">γ</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">x</span><span class="o">,</span> <span class="n">f</span> <span class="n">x</span><span class="bp">.</span><span class="mi">1</span> <span class="n">x</span><span class="bp">.</span><span class="mi">2</span>
</pre></div>

#### [ Sean Leather (Jul 03 2018 at 12:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Beginner%20Questions/near/129014805):
<p>Just to help you see, these are also possible:</p>
<div class="codehilite"><pre><span></span><span class="n">def</span> <span class="n">curry</span> <span class="o">(</span><span class="n">α</span> <span class="n">β</span> <span class="n">γ</span> <span class="o">:</span> <span class="kt">Type</span><span class="o">)</span> <span class="o">:</span> <span class="o">(</span><span class="n">α</span> <span class="bp">×</span> <span class="n">β</span> <span class="bp">→</span> <span class="n">γ</span><span class="o">)</span> <span class="bp">→</span> <span class="n">α</span> <span class="bp">→</span> <span class="n">β</span> <span class="bp">→</span> <span class="n">γ</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">f</span> <span class="n">a</span> <span class="n">b</span><span class="o">,</span> <span class="n">f</span> <span class="bp">⟨</span><span class="n">a</span><span class="o">,</span> <span class="n">b</span><span class="bp">⟩</span>
<span class="n">def</span> <span class="n">uncurry</span> <span class="o">(</span><span class="n">α</span> <span class="n">β</span> <span class="n">γ</span> <span class="o">:</span> <span class="kt">Type</span><span class="o">)</span> <span class="o">:</span> <span class="o">(</span><span class="n">α</span> <span class="bp">→</span> <span class="n">β</span> <span class="bp">→</span> <span class="n">γ</span><span class="o">)</span> <span class="bp">→</span> <span class="n">α</span> <span class="bp">×</span> <span class="n">β</span> <span class="bp">→</span> <span class="n">γ</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">f</span> <span class="n">x</span><span class="o">,</span> <span class="n">f</span> <span class="n">x</span><span class="bp">.</span><span class="mi">1</span> <span class="n">x</span><span class="bp">.</span><span class="mi">2</span>
</pre></div>

#### [ Guy Leroy (Jul 03 2018 at 12:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Beginner%20Questions/near/129014848):
<p>Thank you all for the detailed answers! Greatly appreciate it</p>

#### [ Kevin Buzzard (Jul 03 2018 at 13:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Beginner%20Questions/near/129015912):
<p><span class="user-mention" data-user-id="111947">@Guy Leroy</span> Everything is completely logical and you have a logical brain; I remember being confused about all of this a year ago. You came to my talk yesterday, right? <code>alpha -&gt; beta -&gt; gamma</code> is a type, and you make terms of that type using <code>lambda</code>. After the <code>lambda</code> you'd better take a term of type alpha and then a term of type beta, and then you need to return a term of type gamma. So now hopefully you can get your terms sorted out. For products however, you need to learn the notation. The type is <code>\alpha \times \beta</code> so now you need to know the constructor and the eliminators, which is a fancy way of saying that you need to know how to get something of type <code>alpha x beta</code> from <code>a : alpha</code> and <code>b : beta</code> (that's the constructor for the product) and then you also need to know how to get the things of type alpha and beta from the thing of type <code>alpha x beta</code> -- those are the eliminators. So that's three different pieces of notation -- one for making the product type (that's \times), one for the constructor (that's pointy brackets) and one for the elminators (that's the <code>.1</code> and <code>.2</code> notation). A year ago all of these were floating around in my head and I'd just try any of them until something worked. But now I realise that if you keep everything straight then it all starts fitting into place. The pointy brackets are often used for constructors, the dots are often used for eliminators (I hope they are called eliminators, I'm no expert) and the notation for the types depends on the type but is something you pick up as you go along.</p>

#### [ Kevin Buzzard (Jul 03 2018 at 13:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Beginner%20Questions/near/129015940):
<p>As for the stuff before or after the colon, I've realised that this trips mathematicians up. I need to write something about functions. There's so much functiony stuff which CS people do which is very cool but which we don't see in maths at all! Even using functions as maps from props to props is new to mathematicians.</p>

#### [ Mario Carneiro (Jul 03 2018 at 13:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Beginner%20Questions/near/129016068):
<p>Actually <code>.1</code> is called a projection</p>

#### [ Mario Carneiro (Jul 03 2018 at 13:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Beginner%20Questions/near/129016073):
<p>an eliminator is <code>prod.rec</code> for example</p>

#### [ Guy Leroy (Jul 03 2018 at 13:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Beginner%20Questions/near/129016118):
<p>Thank you for the explanation. Yes I came yesterday. The syntax is slowly starting to make sense, I'm a bit confused at first as we were taught Haskell in first year and it has some similar features.</p>

#### [ Guy Leroy (Jul 03 2018 at 13:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Beginner%20Questions/near/129016126):
<p>But I understand the curry/uncurry functions and their syntax now I think</p>

#### [ Kevin Buzzard (Jul 03 2018 at 13:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Beginner%20Questions/near/129016361):
<blockquote>
<p>an eliminator is <code>prod.rec</code> for example</p>
</blockquote>
<p>Technical interlude: are the projections defined using <code>prod.rec</code> or are they inbuilt and appear like axioms when the product type is defined? I don't know how to figure this out. I guess they would be easy to define using <code>prod.rec</code>.</p>

#### [ Kevin Buzzard (Jul 03 2018 at 13:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Beginner%20Questions/near/129016391):
<blockquote>
<p>But I understand the curry/uncurry functions and their syntax now I think</p>
</blockquote>
<p>When I did that exercise last year, the first thing I wanted to prove was that if you curried and then uncurried, you got back to where you started! But at that point in TPIL you don't have enough tools to do that.</p>

#### [ Kevin Buzzard (Jul 03 2018 at 13:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Beginner%20Questions/near/129016497):
<p>"The dot operator is how you access the members of an object" I think I once read in a book on Java. Is this not the appropriate language in Lean? It feels like the same sort of thing.</p>

#### [ Mario Carneiro (Jul 03 2018 at 13:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Beginner%20Questions/near/129016598):
<p>It's a bit hard to tell just by looking at the definition, but projections are defined using the recursor/eliminator</p>

#### [ Sean Leather (Jul 03 2018 at 13:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Beginner%20Questions/near/129016607):
<p><a href="https://www.quora.com/In-type-theory-what-is-an-eliminator-and-what-is-its-opposite" target="_blank" title="https://www.quora.com/In-type-theory-what-is-an-eliminator-and-what-is-its-opposite">In type theory, what is an eliminator, and what is its opposite?</a></p>

#### [ Sean Leather (Jul 03 2018 at 13:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Beginner%20Questions/near/129016667):
<p>Conclusion: a projection is an eliminator.</p>

#### [ Mario Carneiro (Jul 03 2018 at 13:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Beginner%20Questions/near/129016806):
<p>In lean, projections are a limited version of the <code>cases_on</code> eliminator</p>

#### [ Mario Carneiro (Jul 03 2018 at 13:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Beginner%20Questions/near/129016815):
<p>They only work when the inductive only has one constructor (which is why they are only generated for <code>structure</code>s)</p>

#### [ Mario Carneiro (Jul 03 2018 at 13:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Beginner%20Questions/near/129016862):
<p>and they are obviously nonrecursive (in programming languages with a fixpoint operator this is not as important as it is in lean)</p>

#### [ Mario Carneiro (Jul 03 2018 at 13:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Beginner%20Questions/near/129017129):
<p>The projections are even harder to unfold than I remember... Even <code>#reduce</code> doesn't unfold them, I have to unfold first to the underlying projection macro (printed as <code>[prod.fst c]</code>), and then force that to expand through a <code>change</code>:</p>
<div class="codehilite"><pre><span></span>#print prod.fst
-- @[reducible]
-- def prod.fst : Π {α : Type u} {β : Type v}, prod α β → α :=
-- λ (α : Type u) (β : Type v) (c : prod α β), [prod.fst c]
example {α β} (a : α × β) : prod.fst.{0 0} a = sorry :=
begin
  delta prod.fst,
  change @prod.cases_on _ _ _ _ _ = _,
  -- prod.cases_on a (λ (fst : α) (snd : β), fst) = sorry
end
</pre></div>

#### [ Sean Leather (Jul 03 2018 at 13:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Beginner%20Questions/near/129017389):
<p>I tend to do <code>cases a, dsimp</code> while writing a proof, though I can usually remove the <code>dsimp</code> before I'm done.</p>

#### [ Kevin Buzzard (Jul 03 2018 at 18:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Beginner%20Questions/near/129033519):
<p>Rohan Mitta has just asked me how to formalise an exercise on the topological spaces example sheet: prove that if T1 and T2 are topologies on X (i.e. T1 and T2 are sets of subsets of X) then their intersection is a topology.</p>

#### [ Mario Carneiro (Jul 03 2018 at 18:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Beginner%20Questions/near/129033547):
<p>this is in lean already</p>

#### [ Kevin Buzzard (Jul 03 2018 at 18:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Beginner%20Questions/near/129033550):
<p>That sounds like a question to me, but somehow when you formalise it in Lean it becomes more like a construction. I figured that he needed some predicate <code>is_open_sets</code> and I just glanced through the topological space lean file and didn't spot it</p>

#### [ Kevin Buzzard (Jul 03 2018 at 18:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Beginner%20Questions/near/129033562):
<p>I'm sure it's in Lean already, they form some complete semilattice or whatever</p>

#### [ Mario Carneiro (Jul 03 2018 at 18:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Beginner%20Questions/near/129033572):
<p>it's part of the construction of the complete lattice</p>

#### [ Kevin Buzzard (Jul 03 2018 at 18:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Beginner%20Questions/near/129033578):
<p>I just saw that. But Rohan is trying to learn how to use Lean so I am happy to encourage him to figure this exercise out himself!</p>

#### [ Kevin Buzzard (Jul 03 2018 at 18:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Beginner%20Questions/near/129033592):
<p>It's in Lean but it doesn't look like a proposition, it looks like a construction</p>

#### [ Kevin Buzzard (Jul 03 2018 at 18:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Beginner%20Questions/near/129033642):
<p>Is <code>is_open_sets</code> in Lean? I couldn't find it</p>

#### [ Mario Carneiro (Jul 03 2018 at 18:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Beginner%20Questions/near/129033644):
<p>it is a construction</p>

#### [ Kevin Buzzard (Jul 03 2018 at 18:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Beginner%20Questions/near/129033659):
<p>It looks like an exercise</p>

#### [ Mario Carneiro (Jul 03 2018 at 18:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Beginner%20Questions/near/129033665):
<p>what does <code>is_open_sets</code> mean?</p>

#### [ Kevin Buzzard (Jul 03 2018 at 18:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Beginner%20Questions/near/129033700):
<p><code>is_open_sets</code> is a map from set (set X) to Prop and it's the conjunction of the axioms saying that the sets are the opens in a topology. Am I not thinking straight?</p>

#### [ Kevin Buzzard (Jul 03 2018 at 18:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Beginner%20Questions/near/129033765):
<p>And he wants to prove is_open_sets A and is_open_sets B implies is_open_sets (A intersect B)</p>

#### [ Kevin Buzzard (Jul 03 2018 at 18:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Beginner%20Questions/near/129033773):
<p>Am I making sense?</p>

#### [ Kevin Buzzard (Jul 03 2018 at 18:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Beginner%20Questions/near/129033890):
<div class="codehilite"><pre><span></span><span class="kn">definition</span> <span class="n">is_open_sets</span> <span class="o">{</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">}</span> <span class="o">(</span><span class="n">is_open</span> <span class="o">:</span> <span class="n">set</span> <span class="n">α</span> <span class="bp">→</span> <span class="kt">Prop</span><span class="o">)</span> <span class="o">:=</span>
  <span class="n">is_open</span> <span class="n">univ</span> <span class="bp">∧</span> <span class="o">(</span><span class="bp">∀</span><span class="n">s</span> <span class="n">t</span><span class="o">,</span> <span class="n">is_open</span> <span class="n">s</span> <span class="bp">→</span> <span class="n">is_open</span> <span class="n">t</span> <span class="bp">→</span> <span class="n">is_open</span> <span class="o">(</span><span class="n">s</span> <span class="err">∩</span> <span class="n">t</span><span class="o">))</span> <span class="bp">∧</span> <span class="o">(</span><span class="bp">∀</span><span class="n">s</span><span class="o">,</span> <span class="o">(</span><span class="bp">∀</span><span class="n">t</span><span class="err">∈</span><span class="n">s</span><span class="o">,</span> <span class="n">is_open</span> <span class="n">t</span><span class="o">)</span> <span class="bp">→</span> <span class="n">is_open</span> <span class="o">(</span><span class="err">⋃₀</span> <span class="n">s</span><span class="o">))</span>
</pre></div>

#### [ Kevin Buzzard (Jul 03 2018 at 18:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Beginner%20Questions/near/129033894):
<p>I think it's that</p>

#### [ Kevin Buzzard (Jul 03 2018 at 18:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Beginner%20Questions/near/129034040):
<p>Now I can make the example sheet question into a proposition.</p>

#### [ Kevin Buzzard (Jul 03 2018 at 18:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Beginner%20Questions/near/129034141):
<p>Is this some equivalent way of formalising the notion of a topological space? Why did we choose the other way?</p>

#### [ Kevin Buzzard (Jul 03 2018 at 18:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Beginner%20Questions/near/129034388):
<div class="codehilite"><pre><span></span><span class="kn">definition</span> <span class="n">is_to_top</span> <span class="o">{</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">}</span> <span class="o">(</span><span class="n">is_open</span> <span class="o">:</span> <span class="n">set</span> <span class="n">α</span> <span class="bp">→</span> <span class="kt">Prop</span><span class="o">)</span> <span class="o">(</span><span class="n">H</span> <span class="o">:</span> <span class="n">is_open_sets</span> <span class="o">(</span><span class="n">is_open</span><span class="o">))</span> <span class="o">:</span> <span class="n">topological_space</span> <span class="n">α</span> <span class="o">:=</span>
<span class="o">{</span> <span class="n">is_open</span> <span class="o">:=</span> <span class="n">is_open</span><span class="o">,</span>
  <span class="n">is_open_univ</span> <span class="o">:=</span> <span class="n">H</span><span class="bp">.</span><span class="n">left</span><span class="o">,</span>
  <span class="n">is_open_inter</span> <span class="o">:=</span> <span class="n">H</span><span class="bp">.</span><span class="n">right</span><span class="bp">.</span><span class="n">left</span><span class="o">,</span>
  <span class="n">is_open_sUnion</span> <span class="o">:=</span> <span class="n">H</span><span class="bp">.</span><span class="n">right</span><span class="bp">.</span><span class="n">right</span>
<span class="o">}</span>

<span class="kn">definition</span> <span class="n">top_to_is</span> <span class="o">{</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">}</span> <span class="o">(</span><span class="n">T</span> <span class="o">:</span> <span class="n">topological_space</span> <span class="n">α</span><span class="o">)</span> <span class="o">:</span> <span class="n">is_open_sets</span> <span class="o">(</span><span class="n">T</span><span class="bp">.</span><span class="n">is_open</span><span class="o">)</span> <span class="o">:=</span>
<span class="bp">⟨</span><span class="n">T</span><span class="bp">.</span><span class="n">is_open_univ</span><span class="o">,</span><span class="n">T</span><span class="bp">.</span><span class="n">is_open_inter</span><span class="o">,</span><span class="n">T</span><span class="bp">.</span><span class="n">is_open_sUnion</span><span class="bp">⟩</span>
</pre></div>

#### [ Kevin Buzzard (Jul 03 2018 at 18:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Beginner%20Questions/near/129034394):
<p>They're kind of the same</p>

#### [ Mario Carneiro (Jul 03 2018 at 18:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Beginner%20Questions/near/129034413):
<p>yes, it is equivalent to unbundling the set (set A) part of topological_space</p>

#### [ Reid Barton (Jul 03 2018 at 18:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Beginner%20Questions/near/129034414):
<p>The difference is just that the mathlib definition does not have the properties split off together into a separate structure/definition</p>

#### [ Kevin Buzzard (Jul 03 2018 at 18:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Beginner%20Questions/near/129035139):
<p>So what I find myself wondering again and again is what the best way is. A year ago there were plenty of things I could formalise in 0 ways; now I find there are plenty of things I can formalise in two ways, and I really struggle to know the right way. What I have now understood is that in some sense it doesn't matter, because if I write a good enough API then probably any one of my choices will be fine. But I am beginning to realise that there's more at stake than this.</p>

#### [ Mario Carneiro (Jul 03 2018 at 19:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Beginner%20Questions/near/129035491):
<p>particularly in view of the complete lattice structure, the intersection theorem is only one part of bigger structure, and using it as such makes  sense of the whole finer/coarser thing in a more disciplined way</p>

#### [ Sjoerd de Vries (Jul 04 2018 at 12:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Beginner%20Questions/near/129076394):
<p>I really am a beginner, so forgive me if I sound incredibly stupid.<br>
I'm trying to define a function which can add vectors with entries in <code>ℕ</code>.<br>
I tried something like this:<br>
<code>namespace vectest
    universe u
    constant vec : Type u → ℕ → Type u
    def vec_add (n : ℕ) : vec (list ℕ) n → vec (list ℕ) n → vec (list ℕ) n := sorry
end vectest </code><br>
I don't see how I could specify the desired function like this - of course I intend my input to be a vector of length <code>n</code> with entries in <code>ℕ</code>, but Lean just sees (as far as I can tell) something of Type <code>list ℕ</code> which happens to depend on <code>n</code>. I can't really expect to be able to extract values from the list and add them, then put them back into a new list of length <code>n</code>, if Lean doesn't know that's what I'm talking about, right?</p>

#### [ Kevin Buzzard (Jul 04 2018 at 12:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Beginner%20Questions/near/129076676):
<p>Hi Sjoerd. I would generally discourage the use of <code>constant</code>. Is the idea that you want to model vectors of length <code>n</code> with entries in <code>nat</code>?</p>

#### [ Sjoerd de Vries (Jul 04 2018 at 12:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Beginner%20Questions/near/129076678):
<p>Yes, that's the idea.</p>

#### [ Chris Hughes (Jul 04 2018 at 12:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Beginner%20Questions/near/129076726):
<p>The best way to do that is a function <code>fin n → nat</code>. <code>fin n</code> is a type with <code>n</code> elements.</p>

#### [ Sjoerd de Vries (Jul 04 2018 at 12:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Beginner%20Questions/near/129076959):
<p>So I can think of <code>fin n</code> as being a discrete set with <code>n</code> elements and of vectors as functions. Is there a pre-defined way of adding functions that I can then use to add vectors? And how would I find out if this thing exists without asking any of you?</p>

#### [ Kevin Buzzard (Jul 04 2018 at 12:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Beginner%20Questions/near/129077522):
<p>I think it's not so hard to write these functions yourself and it would probably be a good exercise.</p>

#### [ Chris Hughes (Jul 04 2018 at 12:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Beginner%20Questions/near/129077578):
<p><code>algebra/pi_instances</code> contains all of these for <code>add</code>, <code>mul</code> etc</p>

#### [ Kevin Buzzard (Jul 04 2018 at 12:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Beginner%20Questions/near/129077664):
<p>Sjoerd -- feel free to send me a private message if you don't want to spam the chat. <code>fin n</code> is a type which has exactly <code>n</code> terms, which you can think of as 0,1,...,n-1.</p>

#### [ Sebastian Ullrich (Jul 04 2018 at 12:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Beginner%20Questions/near/129077943):
<p>Defining <code>vector</code> as a function is quite unusual because of the resulting runtime complexity (which you may not be interested in). The common definitions are as an inductive type (<a href="https://github.com/leanprover/lean/blob/a4aae537fe771ee92d746d4a2be1e73c543e48b9/tests/lean/run/smt_ematch3.lean#L5-L7" target="_blank" title="https://github.com/leanprover/lean/blob/a4aae537fe771ee92d746d4a2be1e73c543e48b9/tests/lean/run/smt_ematch3.lean#L5-L7">e.g.</a>) or as a subtype of <code>list</code> (<a href="https://github.com/leanprover/lean/blob/master/library/data/vector.lean" target="_blank" title="https://github.com/leanprover/lean/blob/master/library/data/vector.lean"><code>data.vector</code></a>).</p>

#### [ Zak (Jul 09 2018 at 01:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Beginner%20Questions/near/129318433):
<p>Hey, would anyone mind explaining how to prove <code>A ∨ B</code> given two propositions <code>A</code> and <code>B</code> and a proof of A?</p>

#### [ Zak (Jul 09 2018 at 01:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Beginner%20Questions/near/129318435):
<p>I think the question looks a bit like this; </p>
<div class="codehilite"><pre><span></span><span class="kn">theorem</span> <span class="n">prove_or</span> <span class="o">(</span><span class="n">A</span> <span class="n">B</span> <span class="o">:</span> <span class="kt">Prop</span><span class="o">)</span> <span class="o">(</span><span class="n">proof_A</span> <span class="o">:</span> <span class="n">A</span><span class="o">)</span> <span class="o">:</span> <span class="n">A</span> <span class="bp">∨</span> <span class="n">B</span>
</pre></div>

#### [ Simon Hudon (Jul 09 2018 at 02:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Beginner%20Questions/near/129318792):
<p>You can prove it as:</p>
<div class="codehilite"><pre><span></span><span class="kn">theorem</span> <span class="n">prove_or</span> <span class="o">(</span><span class="n">A</span> <span class="n">B</span> <span class="o">:</span> <span class="kt">Prop</span><span class="o">)</span> <span class="o">(</span><span class="n">proof_A</span> <span class="o">:</span> <span class="n">A</span><span class="o">)</span> <span class="o">:</span> <span class="n">A</span> <span class="bp">∨</span> <span class="n">B</span> <span class="o">:=</span>
<span class="n">or</span><span class="bp">.</span><span class="n">inl</span> <span class="n">proof_A</span>
</pre></div>


<p>or </p>
<div class="codehilite"><pre><span></span><span class="kn">theorem</span> <span class="n">prove_or</span> <span class="o">(</span><span class="n">A</span> <span class="n">B</span> <span class="o">:</span> <span class="kt">Prop</span><span class="o">)</span> <span class="o">(</span><span class="n">proof_A</span> <span class="o">:</span> <span class="n">A</span><span class="o">)</span> <span class="o">:</span> <span class="n">A</span> <span class="bp">∨</span> <span class="n">B</span> <span class="o">:=</span>
<span class="k">by</span> <span class="o">{</span> <span class="n">left</span><span class="o">,</span> <span class="n">exact</span> <span class="n">proof_A</span> <span class="o">}</span>
</pre></div>

#### [ Zak (Jul 09 2018 at 02:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Beginner%20Questions/near/129318803):
<p>Thank you :D <code>left</code> will be very useful</p>

#### [ Simon Hudon (Jul 09 2018 at 03:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Beginner%20Questions/near/129320318):
<p>Fun fact: <code>left</code> works with any inductive type. It applies the first constructor while <code>right</code> applies the second constructor.</p>

#### [ Patrick Massot (Jul 09 2018 at 07:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Beginner%20Questions/near/129329261):
<p><a href="https://leanprover.github.io/theorem_proving_in_lean/tactics.html#more-tactics" target="_blank" title="https://leanprover.github.io/theorem_proving_in_lean/tactics.html#more-tactics">https://leanprover.github.io/theorem_proving_in_lean/tactics.html#more-tactics</a></p>

#### [ Kevin Buzzard (Jul 09 2018 at 10:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Beginner%20Questions/near/129334456):
<p>I was mulling over <code>∨</code> as a result of this question, thinking how one could explain to a beginner how to work this out, and as a result I ran into something which I myself didn't understand. Is <code>∨</code> left associative or right associative? If you can't remember then I figured that one way of finding out was just checking for yourself:</p>
<div class="codehilite"><pre><span></span><span class="kn">example</span> <span class="o">(</span><span class="n">P</span> <span class="n">Q</span> <span class="n">R</span> <span class="o">:</span> <span class="kt">Prop</span><span class="o">)</span> <span class="o">:</span> <span class="n">P</span> <span class="bp">∨</span> <span class="n">Q</span> <span class="bp">∨</span> <span class="n">R</span> <span class="bp">=</span> <span class="n">P</span> <span class="bp">∨</span> <span class="o">(</span><span class="n">Q</span> <span class="bp">∨</span> <span class="n">R</span><span class="o">)</span> <span class="o">:=</span> <span class="n">rfl</span>
<span class="kn">example</span> <span class="o">(</span><span class="n">P</span> <span class="n">Q</span> <span class="n">R</span> <span class="o">:</span> <span class="kt">Prop</span><span class="o">)</span> <span class="o">:</span> <span class="n">P</span> <span class="bp">∨</span> <span class="n">Q</span> <span class="bp">∨</span> <span class="n">R</span> <span class="bp">=</span> <span class="o">(</span><span class="n">P</span> <span class="bp">∨</span> <span class="n">Q</span><span class="o">)</span> <span class="bp">∨</span> <span class="n">R</span> <span class="o">:=</span> <span class="n">rfl</span>
</pre></div>


<p>I was expecting precisely one of these to work. But neither does! The first one (which is the right answer) gives the error</p>
<div class="codehilite"><pre><span></span>type mismatch, term
  rfl
has type
  ?m_2 = ?m_2
but is expected to have type
  P ∨ Q ∨ R = P ∨ Q ∨ R
</pre></div>

#### [ Kevin Buzzard (Jul 09 2018 at 10:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Beginner%20Questions/near/129334461):
<p>Why does <code>rfl</code> not prove that?</p>

#### [ Kenny Lau (Jul 09 2018 at 10:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Beginner%20Questions/near/129334482):
<p>because <code>=</code> is less important than <code>∨</code></p>

#### [ Kenny Lau (Jul 09 2018 at 10:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Beginner%20Questions/near/129334521):
<p>think about what a = b or c = d means</p>

#### [ Kenny Lau (Jul 09 2018 at 10:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Beginner%20Questions/near/129334533):
<p>(pp.all would have shown you the problem)</p>

#### [ Kenny Lau (Jul 09 2018 at 10:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Beginner%20Questions/near/129334550):
<div class="codehilite"><pre><span></span><span class="kn">example</span> <span class="o">(</span><span class="n">P</span> <span class="n">Q</span> <span class="n">R</span> <span class="o">:</span> <span class="kt">Prop</span><span class="o">)</span> <span class="o">:</span> <span class="o">(</span><span class="n">P</span> <span class="bp">∨</span> <span class="n">Q</span> <span class="bp">∨</span> <span class="n">R</span><span class="o">)</span> <span class="bp">=</span> <span class="o">(</span><span class="n">P</span> <span class="bp">∨</span> <span class="o">(</span><span class="n">Q</span> <span class="bp">∨</span> <span class="n">R</span><span class="o">))</span> <span class="o">:=</span> <span class="n">rfl</span>
<span class="kn">example</span> <span class="o">(</span><span class="n">P</span> <span class="n">Q</span> <span class="n">R</span> <span class="o">:</span> <span class="kt">Prop</span><span class="o">)</span> <span class="o">:</span> <span class="o">(</span><span class="n">P</span> <span class="bp">∨</span> <span class="n">Q</span> <span class="bp">∨</span> <span class="n">R</span><span class="o">)</span> <span class="bp">=</span> <span class="o">((</span><span class="n">P</span> <span class="bp">∨</span> <span class="n">Q</span><span class="o">)</span> <span class="bp">∨</span> <span class="n">R</span><span class="o">)</span> <span class="o">:=</span> <span class="n">rfl</span>
</pre></div>

#### [ Sebastien Gouezel (Jul 09 2018 at 10:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Beginner%20Questions/near/129334753):
<p>Another beginner question: I would like to understand why <code>apply</code> is failing in the following example:</p>
<div class="codehilite"><pre><span></span><span class="kn">import</span> <span class="n">analysis</span><span class="bp">.</span><span class="n">real</span> <span class="n">order</span><span class="bp">.</span><span class="n">filter</span>
<span class="kn">open</span> <span class="n">filter</span>

<span class="kn">lemma</span> <span class="n">test</span> <span class="o">(</span><span class="n">a</span> <span class="n">b</span> <span class="n">c</span> <span class="o">:</span> <span class="n">real</span><span class="o">)</span> <span class="o">:</span> <span class="n">tendsto</span> <span class="o">(</span><span class="bp">λ</span><span class="n">x</span><span class="o">,</span> <span class="n">a</span> <span class="bp">*</span> <span class="n">x</span><span class="o">)</span> <span class="o">(</span><span class="n">nhds</span> <span class="n">c</span><span class="o">)</span> <span class="o">(</span><span class="n">nhds</span> <span class="o">(</span><span class="n">a</span> <span class="bp">*</span> <span class="n">c</span><span class="o">))</span> <span class="o">:=</span>
<span class="k">begin</span>
  <span class="n">apply</span> <span class="n">tendsto_mul</span><span class="o">,</span>   <span class="c1">-- this line fails</span>
  <span class="n">apply_instance</span><span class="o">,</span>
  <span class="n">exact</span> <span class="n">tendsto_const_nhds</span><span class="o">,</span>
  <span class="n">exact</span> <span class="n">tendsto_id</span>
<span class="kn">end</span>
</pre></div>


<p>I know how to work it out with <code>apply tendsto_mul _ _</code> or <code>refine tendsto_mul _ _</code> or a direct term proof, but with the above it fails with the error message</p>
<div class="codehilite"><pre><span></span>invalid apply tactic, failed to unify
  tendsto (λ (x : ℝ), a * x) (nhds c) (nhds (a * c))
with
  tendsto ?m_3 ?m_4 (nhds ?m_6) → tendsto ?m_7 ?m_4 (nhds ?m_8) → tendsto (λ (x : ?m_1), ?m_3 x * ?m_7 x) ?m_4 (nhds (?m_6 * ?m_8))
</pre></div>


<p>What I don't get is why this unification problem is hard. Any hint?</p>

#### [ Patrick Massot (Jul 09 2018 at 10:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Beginner%20Questions/near/129334812):
<p>This is higher order unification</p>

#### [ Patrick Massot (Jul 09 2018 at 10:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Beginner%20Questions/near/129334820):
<p>You want Lean to recognize a product of functions</p>

#### [ Kenny Lau (Jul 09 2018 at 10:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Beginner%20Questions/near/129334825):
<p>no that isn't it</p>

#### [ Patrick Massot (Jul 09 2018 at 10:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Beginner%20Questions/near/129334826):
<p>But it could be a product in many ways, in principle</p>

#### [ Kenny Lau (Jul 09 2018 at 10:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Beginner%20Questions/near/129334884):
<p>I suspect it's <code>apply</code> not knowing which term is the last thing</p>

#### [ Patrick Massot (Jul 09 2018 at 10:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Beginner%20Questions/near/129334905):
<p>Hum, it's weird that <code>apply tendsto_mul _ _</code> works</p>

#### [ Mario Carneiro (Jul 09 2018 at 10:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Beginner%20Questions/near/129334982):
<p>note that <code>tendsto</code> is itself defined as a pi</p>

#### [ Mario Carneiro (Jul 09 2018 at 10:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Beginner%20Questions/near/129334989):
<p>this has been known to confuse <code>apply</code> in the past</p>

#### [ Kevin Buzzard (Jul 09 2018 at 10:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Beginner%20Questions/near/129335071):
<blockquote>
<p>because <code>=</code> is less important than <code>∨</code></p>
</blockquote>
<p>How ironic that the reason the question came up was that the output of <code>#print notation ∨</code> was what inspired me to ask the question, so I already knew that <code>∨</code> was unimportant. Thanks Kenny. It's not the first time I've been done over by binding powers -- I get caught out by <code>∃</code> occasionally too.</p>

#### [ Sebastien Gouezel (Jul 09 2018 at 10:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Beginner%20Questions/near/129335914):
<blockquote>
<p>note that <code>tendsto</code> is itself defined as a pi</p>
</blockquote>
<p>You mean <code>apply</code> unfolds the definition of <code>tendsto</code> all the way up to the filter inclusion, which is indeed a pi? And then I am not surprised it is confused. Is there a way to tell lean that is should never unfold by itself the definition of <code>tendsto</code>, to avoid the problem?</p>

#### [ Mario Carneiro (Jul 09 2018 at 10:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Beginner%20Questions/near/129336027):
<p>these instructions are already in place</p>

#### [ Mario Carneiro (Jul 09 2018 at 10:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Beginner%20Questions/near/129336028):
<p><code>apply</code> is not supposed to look that deep, but it does</p>

#### [ Mario Carneiro (Jul 09 2018 at 10:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Beginner%20Questions/near/129336037):
<p>it will even look through <code>@[irreducible]</code> definitions, unlike almost anything else</p>

#### [ Sebastien Gouezel (Jul 09 2018 at 10:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Beginner%20Questions/near/129336172):
<p>Yes, I can see that the definition of subset is protected... Do you know if this behavior of <code>apply</code>is by design, and for what reason? This is a real pain for what I would like to do.</p>

#### [ Mario Carneiro (Jul 09 2018 at 11:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Beginner%20Questions/near/129336641):
<p>It's certainly a bug, but we've got to live with it until lean 4 comes around. It only concerns the calculation of how many underscores to insert, and only then in limited circumstances (I'm not sure Patrick was that far off the mark with the note about higher order unification)</p>

#### [ Mario Carneiro (Jul 09 2018 at 11:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Beginner%20Questions/near/129336770):
<p>I think, after you unfold EVERYTHING, the tendsto becomes a bunch of pis applied to a metavariable (the unknown target topology set), which may unfold to still more pis but lean can't be sure</p>

#### [ Sebastien Gouezel (Jul 09 2018 at 11:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Beginner%20Questions/near/129338353):
<p>Thanks for your explanations. Indeed, for proofs written by hand, adding some underscores is not a problem. </p>
<p>I wanted to try my hand at automation, adding <code>@[tendsto_rules]</code> before <code>tendsto</code> lemmas. With the aim that writing <code>applys [tendsto_rules]</code> would try to <code>apply</code>successively all the tagged rules, to prove convergence statements. Since <code>apply</code> does not work well in this context, I will have to find another exercise to learn tactics.</p>
<p>For fun, an even "better" example: in my example above, if you try to replace the line <code>exact tendsto_const_nhds</code> with <code>apply tendsto_const_nhds</code> it fails (while the unification looks even easier as there are no premises in <code>tendsto_const_nhds</code>), but it works with <code>apply @tendsto_const_nhds _ _ _ _ _</code> (I agree, it is only a matter of getting the right number of underscores :)</p>

#### [ Kevin Buzzard (Jul 09 2018 at 12:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Beginner%20Questions/near/129339844):
<p>You could write a tactic which is <code>apply</code> but which works the way you want it to ;-) I have no idea how hard that would be!</p>

#### [ Patrick Massot (Jul 09 2018 at 13:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Beginner%20Questions/near/129342154):
<p>It looks like <code>apply</code> is written in C, not Lean</p>

#### [ Sebastien Gouezel (Jul 09 2018 at 13:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Beginner%20Questions/near/129343466):
<p>I probably speak C++ better than lean, but still I will rather find another exercise, this one is not for me!</p>


{% endraw %}
