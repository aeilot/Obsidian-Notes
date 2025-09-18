## Data Generating Distributions

Bayes Optimal Classifier:

![[ciml-v0_99-all.pdf#page=19&rect=74,292,214,323|ciml-v0_99-all, p.19]]

任意属于，都返回概率最大的 $(\hat{x},\hat{y})$

![[ciml-v0_99-all.pdf#page=19&rect=67,226,372,262|ciml-v0_99-all, p.19]]

Bayes Error Rate (Bayes Optimal Error Rate): 贝叶斯最优分类器的错误率

If you have access to the Data Generating Distribution, classification would be simple.

## Inductive Bias

 Inductive bias refers to the set of assumptions a learning algorithm uses to predict outputs given inputs it has not encountered during training. It guides the model's generalization behavior beyond the observed data.

## Not Everything is Learnable

Noise in the training data (feature/label)

Insufficient features

No single correct answers (Too Subjective)

Inductive Bias misaligned

## Underfitting & Overfitting

Underfitting is when you had the opportunity to learn something but didn’t.

Overfitting is when you pay too much attention to idiosyncracies of the training data, and aren’t able to generalize well. (fitting noise)

![[ciml-v0_99-all.pdf#page=24&rect=66,458,561,724|ciml-v0_99-all, p.24]]

## Separation of Training and Test Data

 It is crucial to evaluate model performance on unseen data to measure generalization capability rather than simply memorizing training examples. This prevents data leakage and gives a realistic estimate of how the model will perform in real-world scenarios.

Training data & Test data

80/20 split

**The cardinal rule of machine learning is: never touch your test data.** 

## Models, Parameters and Hyperparameters

A **model** represents the learned function that maps inputs to outputs. 

**Parameters** are the internal variables learned during training.

**Hyperparameters** are configurations set before training that control the learning process. (they cannot be naively adjusted using the training data)

the learning algorithm is essentially trying to adjust the parameters of the model so as to minimize training error. 

choosing hyperparameters: choose them so that they minimize training error

1. Tune it with training data
2. Tune it with test data (wrong: Never touch the test data)
3. A new split: **development data** (or **validation data** or **held-out data**)
## Oracle Experiment

An oracle experiment refers to testing model performance under ideal conditions where we simulate perfect knowledge (such as knowing the true data-generating distribution) to understand theoretical upper bounds or limitations of learning algorithms.