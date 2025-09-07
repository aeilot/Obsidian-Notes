## What's learning

generalize → predict (predicting the future based on the past)

examples: objects that our algorithm will make predictions about

The goal of inductive machine learning: take some training data and use it to induce a function $f$.

This function $f$ will be evaluated on the test data.

The machine learning algorithm has succeeded if its performance on the test data is high.

## Learning Problems
1. Regression: trying to predict a real value
2. Binary Classification: trying to predict a simple yes/no response
3. Multi-class Classification: trying to put an example into one of a number of classes
4. Ranking: trying to put a set of objects in order of relevance
## Decision Tree

divide & conquer

![[Pasted image 20250907180013.png]]

## Loss Function

A **loss function** is a mathematical function that quantifies the penalty or "cost" associated with an incorrect prediction made by a machine learning model. It serves as the primary measure of error that the model training process seeks to minimize.

$\to$ the measure of error: to tell us how “bad” a system’s prediction is in comparison to the truth

Formally, a loss function, denoted as $\ell$, is a mapping from the true data label and a model's prediction to a non-negative real number. $$\ell: \mathcal{Y} \times \mathcal{Y} \to \mathbb{R}_{\ge 0}$$

- ***Regression:*** **squared loss** $\ell(y, \hat{y}) = (y - \hat{y})^2$ or **absolute loss** $\ell(y, \hat{y}) = |y - \hat{y}|$.

- **_Binary Classification:_** **zero/one loss** $$ \ell(y, \hat{y}) = \begin{cases} 0 & \text{if } y = \hat{y} \\ 1 & \text{otherwise} \end{cases} $$

- ***Multiclass Classification:*** also zero/one loss.
## the Probabilistic Model of Learning

**the Probabilistic Model of Learning**: A probability distribution $D$ over input/output pairs (the **data generating distribution**) $\to \,\,(x,y)$ pairs

**The expected loss**: the weighted average loss over the all $(x, y)$ pairs in $D$, weighted by their probability, $D(x, y)$

If D is a finite discrete distribution, we have:

![[Pasted image 20250907193811.png]]

(1) The expectation of some function $g$ is the weighted average value of $g$, where the weights are given by the underlying probability distribution. 

(2) The expectation of some function $g$ is your best guess of the value of $g$ if you were to draw a single item from the underlying probability distribution.

**We don't know what $D$ is beforehand**: all we get is a random sample from it (our training data)
## Formalized Learning Problem

![[Pasted image 20250907194334.png]]

We're given training data (a random sample of input/output pairs drawn from $D$)

We need to induce a function $f$ that maps new inputs $\hat{x}$ to corresponding prediction $\hat{y}$

it’s expected loss ϵ over D with respect to ℓ should be as small as possible

![[Pasted image 20250907194554.png]]

**We don't know what D is!** 
We only have access to the training error, and we need to generalize beyond the training data.

### Definition of induction machine learning

Given (i) a loss function $\ell$ and (ii) a sample $D$ from some unknown distribution $D$, you must compute a function $f$ that has low expected error $\epsilon$ over $D$ with respect to $\ell$.

Caveat: the distribution $D$ for training data must match the distribution $D$ for the test data