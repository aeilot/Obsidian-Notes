# BitXOR
```cpp
int bitXor(int x, int y) {
  return ~((~(x&~y))&(~((~x)&y)));
}
```

注：

``a|b = ~(~a&~b)``

`a^b = (a&~b) | (~a&b)`

>德摩根定律 (De Morgan's Laws)
>
> **形式一：合取的否定 (Negation of Conjunction)**
>
> > “并非 A 与 B 同时为真” 等价于 “A 为假 或 B 为假”。
> >
> > 逻辑符号： $\neg (A \land B) \iff (\neg A) \lor (\neg B)$
>
> **形式二：析取的否定 (Negation of Disjunction)**
>
> > “并非 A 或 B 中至少一个为真” 等价于 “A 为假 与 B 为假”。
> >
> > 逻辑符号： $\neg (A \lor B) \iff (\neg A) \land (\neg B)$

