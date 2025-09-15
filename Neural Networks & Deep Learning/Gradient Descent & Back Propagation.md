https://colab.research.google.com/drive/1sydSb31CEVW-cY9oN7Sw-weyXN_VV7Ap#scrollTo=_zTTnqNWap-C

## Perceptrons

![[Pasted image 20250915092648.png]]

## Sigmoid

![[Pasted image 20250915092702.png]]

```py
def sigmoid(z):
	return 1.0/(1.0+np.exp(-z))
```

## Gradient Descent
**Cost Function**:
![[Pasted image 20250915092912.png]]
![[Pasted image 20250915092926.png]]
![[Pasted image 20250915093002.png]]
mini-batch
![[Pasted image 20250915093937.png]]
![[Pasted image 20250915093945.png]]

## Back Propagation

![[Pasted image 20250915094112.png]]