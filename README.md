Hype
====
The Hype is Real!

With the help of the (typeannotations)[https://github.com/ceronman/typeannotations] you can have types, AND type checking with Hy! 

Work in progress!

```hy
=> (require hype.ann)
=> (ann foo [int :-> str])
=> (defn foo [a] (str a))
=> (foo 1)
'1'
=> (foo "1")
Traceback (most recent call last):
...
TypeError: Incorrect type for "a"
```
