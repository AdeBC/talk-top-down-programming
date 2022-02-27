# Top-down programming for problem solving

Hui Chong

[huichong.me@gmail.com](mailto:huichong.me@gmail.com)

[www.huichong.me](https://www.huichong.me)

---
## Programming for problem solving

**Why programming?**

There are mainly two ways to solve problems.

- Manual operation
  - Flexible: human can adapt to different problems.
  - Error prone: human can make random mistakes.
  - **But, what if you have to solve it over and over again 1000 or even more times?**
- Programming
  - Less flexible: a program is built for only one kind of problems.
  - **Easy to scale up**: it's a series of pre-defined instructions to be executed by computers.

Not all problems can be solved by programming.

---
## Top-down programming

A hard problem often can be split into several simpler problems.

A diagram of top-down problem solving.

You're using "Top-down" thinking every day when you solve problems.
You just didn't realize that you're using it.

---
## Bottom-up debugging

Programming is about both writing code and debugging.

A diagram of bottom-up debugging.

---
## Motif-finding: A classical problem

#### Motif：

- Does not have an independent tertiary structure.
- Has specific biological functions: binding, modification, cell sublocalization, maintenance of structures, etc.
- The length is generally several to several tens of amino acids / base.

Motif finding problem is a classical bioinformatics problem, 
aiming to quickly find a series of motifs on genes with the 
same enzyme (DNA replicase, etc.) binding site.

#### Solution:

Gibbs sampler algorithm.

---
## Gibbs sampler algorithm

Iterative three steps
```text
randomly select motif.
...
...
```
The pseudocode
```text
    Gibbs sampler(Dna, k, t, N)
        randomly select k-mers Motifs = (Motif1, …, Motift) in each string from Dna
        BestMotifs ← Motifs
        for j ← 1 to N
            i ← Random(t)
            Profile ← profile matrix constructed from all strings in Motifs except for Motifi
            Motifi ← profile most(Dnai, k, Profile)
            if Score(Motifs) < Score(BestMotifs)
                BestMotifs ← Motifs
        return BestMotifs
```

---
## Very first implementation
```python
def motif_finder(dnas, k):
  step_1()
  step_2()
  step_3()
  
  
......
  
  
if __name__ == "__main__":
  dnas = [
    'acgta.....',
    'acgta.....',
    'acgta.....',
    'acgta.....',
    'acgta.....',
    'acgta.....',
  ]
  motif_finding(dnas)
```

---
## Debugging

bottom-up debugging.

#### Bug #1
It's in step_2 code but Python interpreter reported error when executing step_3.

#### But #2
It's in step_3 code.

---
## Top-down programming

Do you think it's quite useful?