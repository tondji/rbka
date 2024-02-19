import numpy as np
import random

#@title : Randomized Bregman-Kaczmarz with averaging method

def kaczmarz_method(A, b, eta, x_true, W, max_iter, bN, lbda=1, change_proba=True):

  # the randomized  Bregman-Kaczmarz with averaging method
  # for academic purpose; uses x_true to calculate the exact beta needed for the adaptive stepsize
  # A: The given matrix.
  # b: The true right hand size. We never used it and it is only to get a noisy version of itself.
  # eta: The batch size.
  # x_true: The true solution.
  # W: The weight matrix.
  # max_iter: The maximum number of iterations.
  # bN: Correspond to the noisy version of b.
  # lbda: The sparsity parameter.
  # change_proba: Boolean parameter to set the probabilities vector.

  m, n = A.shape

  squared_row_norms = np.linalg.norm(A, axis=1) ** 2

  if change_proba:
    p = squared_row_norms / squared_row_norms.sum()

  else:
    _, max_A, _ = np.linalg.svd(A, full_matrices=True)
    max_W = np.max(np.abs(W))

    p = (eta - 0.5 * max_W) / ((eta - 1) * max_A[0] ** 2) * (squared_row_norms / W)

  P = np.diag(p)

  W_matrix = np.diag(W)
  D = np.diag(1 / squared_row_norms)

  x_star = np.zeros((n, 1))
  x_k = np.zeros((n, 1))

  residuals = []
  errors = []

  for iter in range(max_iter):

    # sample the row index
    tauk = random.choices([i for i in range(m)], weights=p, k=eta)
    Mk = np.zeros((m, m))

    if len(tauk) < 10:
      for row_index in tauk:
        Mk += W[row_index] * np.eye(1, m, row_index).T @ np.eye(1, m, row_index) / squared_row_norms[row_index]
      Mk /= len(tauk)

    else:
      Mk = P @ W_matrix @ D

    x_star += - A.T @ Mk @ (A @ x_k - bN)

    x_k = soft_skrinkage(x_star, lbda)

    residuals.append(np.linalg.norm(A @ x_k - b)/ (np.linalg.norm(b)))
    errors.append(np.linalg.norm(x_k - x_true) / (np.linalg.norm(x_true)))

  return x_k, residuals, errors

# The soft shrinkage function
def soft_skrinkage(x, lbda):
  return np.sign(x) * np.maximum(np.abs(x) - lbda, 0)

# making a vector x sparse with s non zero entries
def sparse(x, s):
  shape = x.shape

  arr = np.zeros(shape)
  arr[:s]  = 1
  np.random.shuffle(arr)
  return x * arr