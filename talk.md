# Top-down programming for problem solving

Hui Chong

[huichong.me@gmail.com](mailto:huichong.me@gmail.com)

[www.huichong.me](https://www.huichong.me)

---
## Programming for problem solving

### Why programming?

There are generally two ways to solve problems.

#### Manual operation

- Flexible: human can adapt to different problems.
- Error prone: human can make random mistakes.
- **But, what if you have to execute your solution over and over again in the future?**
- Human effort are for those repetitive works.

#### Programming

- Less flexible: a program is built for only one kind of problems.
- **Easy to scale up**: it's a series of pre-defined instructions to be executed by computers.

Not all problems can be solved by programming.

---
## Top-down programming & bottom-up testing

### What are the benefits?
- Clear code structure that is easy to understand by others.
- Coding is also a kind of commuication (e.g., collaborative developing).
- Easier to debug.
- Develop and test more efficiently without almost any extra cost.
- Top-down programming is independent of programming language. 


### How it works? 

- Split large problem into multiple smaller problems.
- Solve each smaller problem using a function/module.
- Test small functions before testing those larger and depends on the small functions.

---


## Function call graph

Function call graph can clearly show the structure of you program.

![](example/complex.png)

The example was generated based on the [PyCallGraph](https://pycallgraph.readthedocs.io/en/master/index.html) package.

---
## How to apply top-down programming?

Think about the structure while/before you write code.

Tips to write a script.
- The main function goes on the top so that any new comer can see the structure of the script (like a table of content).
- Run `main()` inside `if __name__ == '__main__'` statement for easier test.

```python
def main():
    A(xxx)
    B(xxx)
    C(xxx)

def A(xxx):
    D(xxx)
    E(xxx)

......

def I(xxx):
  ......

if __name__ == '__main__':  
    main()
```

---
## Bottom-up testing and error analysis

Tips to test the script.
- Test small functions first.
- **Error analysis**: If a module cannot work but all its submodules work well, then the bug should be in the module.

![](example/complex.png)


---
## Example: Finding proximate squared root by gradient descent

