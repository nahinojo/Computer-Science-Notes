## PDF: Chapter 3

![[Discrete Mathematics with Applications.pdf#page=131]]


## Section 3.1

#### Definitions and Formulas

![[Predicate and Domain Definition.png]]
- **Predicates** are essentially the functional equivalent of statements. They aren't true or false until the values of the unknown variables are defined.
- The **Domain** is set of all values that the unknown variable(s) may be.

![[Truth Set Definition.png]]
- The subset of the **domain** where the **predicate** is always true

![[Universal Statement & Counter Example Definition.png]]
- A **Universal Statement** is essentially the **predicate** where the variable is a value of some set $D$.
	- The statement is true if $D$ is some subset of the **truth set**. 
	- The statement is false if $D$ contains a value for $x$ not in the truth set
		- The corresponding $x$ value is called a **counterexample**.

![[Notation.png]]
$$P(x) \Rightarrow Q(x) = \forall x\text{, }P(x) \rightarrow Q(x)$$
$$P(x) \Leftrightarrow Q(x) = \forall x\text{, }P(x) \leftrightarrow Q(x)$$
- These seem to essentially be simplified versions of understandable formulas. It just removes the $\forall x$ notation. 

![[Existential Statement Definition.png]]
- An **Existential Statement** is essentially the **predicate** where the variable is a value of some set $D$.
	- The statement is true if *any value* in $D$ is within the **truth set**. 
	- The statement is false if there's *no value* $D$ that is part of the truth set
- $\exists$ : for any, exists.
## Section 3.2

### Definitions and Formulas

![[Negation of Universal Statement Theorem.png]]
- The negation of a universal statement ("all are") is logically equivalent to an existential statement ("some are not" or "There is at least one that is not").
- *Conceptually*, a universal statement resembles 'this is true for all values in the set'. The negation to this is 'this is not true for at least one value in the set' 

![[Negation of an Existential Statement Theorem.png]]
- The negation of an existential statement ("some are") is logically equivalent to a universal statement ("none are" or "all are not").
- *Conceptually*, an existential statement is 'this is true for at least one value in the set'. The negation would then be 'this is not true for all values in the set'.

![[Negation of a Universal Conditional Statement.png]]

**Variants of Universal Conditional Statements**
In general, a statement of the form:
$$\forall x \text{ in }D\text{, if }P(x)\text{ then }Q(x)$$
is called **vacuously true** or **true by default** if, and only if, $P(X)$ is false for every $x$ in $D$.


![[Contrapositive, Converse, and Inverse Statements Definition.png]]
- $\forall x \in D \text{, if }P(X)\text{ then }Q(x) \equiv \forall x \in D \text{, if } \sim Q(x) \text{ then }\sim P(x)$
- $\forall x \in D \text{, if }P(X)\text{ then }Q(x) \not\equiv \forall x \in D \text{, if } Q(x) \text{ then }P(x)$
- $\forall x \in D \text{, if }P(X)\text{ then }Q(x) \not\equiv \forall x \in D \text{, if } \sim Q(x) \text{ then }\sim P(x)$

![[Universal Conditions Necessary, Sufficient, and Only If Definition.png]]


