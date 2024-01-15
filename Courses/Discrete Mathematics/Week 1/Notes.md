## PDF: Chapter 2

![[Discrete Mathematics with Applications.pdf#page=60]]


## Section 2.1

### Definitions and Formulas

![[Statement Definition.png]]
![[Negation Definition.png]]
![[Conjunction Definition.png]]
![[Disjunction Definition.png]]
![[Tautology and Contradiction Definition.png]]
![[Logical Equivalence Formulas.png]]

### Personal

#### Under-simplification

A statement composed of multiple propositions can be under-simplified. The expression is no longer reducible however it's not in it's simplest form. Consider the Canvas Problem from Homework 1, Part 1:
$$((\sim p \wedge q)\vee(\sim p \wedge \sim q))\vee(\sim p \wedge q)\equiv \sim p$$
If the *wrong* sequence of logical equivalences were used to simplify the left-handed expression, it would yield the result $\sim p \wedge q$ (I believe, however the technicality doesn't matter here). Notice that the extraneous $q$ can not be removed. 

Again, following the *wrong* sequence of logical equivalences can result in an under-simplified expression
## Section 2.2
### Definitions and Formulas

![[Conditional, Hypothesis, and Conclusion Definition.png]]$$p \rightarrow q \equiv \sim p \vee q$$
The **negation** of “if p then q” is logically equivalent to “p and not q.” $$\sim (p \rightarrow q) \equiv p \ \wedge \sim q$$
![[Contrapositive Definition.png]]
- A conditional statement is logically equivalent to its own **contrapositive**.

![[Converse and Inverse Definition.png]]
- A conditional statement and its **converse** are **not** logically equivalent.
- A conditional statement and its **inverse** are **not** logically equivalent.
- The **converse** of a statement is logically equivalent to the **inverse** of a statement.

![[Only If Definition.png]]
![[Biconditional (Iff) Definition.png]]
$$p \leftrightarrow q \equiv (\sim p \vee q) \wedge (\sim q \vee p)$$


**Order of Operations for Logical Operators**
1. ($\sim$) Evaluate negations first.
2. ($\wedge$, $\vee$) Evaluate $\wedge$ and $\vee$ second. When both are present, parentheses are needed.
3. ($\rightarrow$, $\leftrightarrow$) Evaluate $\rightarrow$ and $\leftrightarrow$ third. When both are present, parentheses are needed.

![[Sufficient and Necessary Conditions Definition.png]]
- "$r$ is a **necessary** condition for $s$" *also* means "if $s$ then $r$"
- "$r$ is a **necessary** and **sufficient** condition for $s$" means "$r$ if, and only if, $s$."
$$(r \rightarrow s) \wedge (s \rightarrow r) \equiv (r \leftrightarrow s)$$

**Other Statement Forms**
- "$r$ **unless** $s$" means "if $\sim s$ then $r$"