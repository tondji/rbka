import numpy as np
import matplotlib.pyplot as plt



def plotRes(residuals, s=40):
    residuals_mean = []
    residuals_std = []
    Residuals_mean = []
    Residuals_std = []
    X = [k for k in range(len(residuals[0][0])) if k % s == 0]

    for i in range(len(residuals)):
        residuals_mean.append(np.mean(residuals[i], axis=0, dtype=np.float64))
        residuals_std.append(np.std(residuals[i], axis=0, dtype=np.float64))

    for i in range(len(residuals)):
        Residuals_mean.append([residuals_mean[i][l] for l in X])
        Residuals_std.append([residuals_std[i][l] for l in X])

    plt.figure(figsize=(6, 6))

    plt.plot(X, Residuals_mean[0], label=r'\textbf{RK}', color='blue')  # ,  marker='^'
    plt.plot(X, Residuals_mean[1], linestyle='dashed', label=r'\textbf{RSK}', color='limegreen')  # , marker='o'
    plt.plot(X, Residuals_mean[2], linestyle='-.', label=r'\textbf{RSKA-v1}', color='black')  # , marker='*'
    plt.plot(X, Residuals_mean[3], linestyle=':', label=r'\textbf{RSKA-v2}', color='black')  # , marker='s'
    plt.plot(X, Residuals_mean[4], label=r'\textbf{RSKA-v3}', color='black')  # , marker='x'
    plt.plot(X, Residuals_mean[5], linestyle='--', label=r'\textbf{RSKA-v4}',
             color='black')  # linestyle='dashdot' , marker='p'

    plt.fill_between(X, np.subtract(Residuals_mean[0], Residuals_std[0]), np.add(Residuals_mean[0], Residuals_std[0]),
                     color='blue', alpha=0.2)
    plt.fill_between(X, np.subtract(Residuals_mean[1], Residuals_std[1]), np.add(Residuals_mean[1], Residuals_std[1]),
                     color='limegreen', alpha=0.2)
    plt.fill_between(X, np.subtract(Residuals_mean[2], Residuals_std[2]), np.add(Residuals_mean[2], Residuals_std[2]),
                     color='black', alpha=0.2)
    plt.fill_between(X, np.subtract(Residuals_mean[3], Residuals_std[3]), np.add(Residuals_mean[3], Residuals_std[3]),
                     color='black', alpha=0.2)
    plt.fill_between(X, np.subtract(Residuals_mean[4], Residuals_std[4]), np.add(Residuals_mean[4], Residuals_std[4]),
                     color='black', alpha=0.2)
    plt.fill_between(X, np.subtract(Residuals_mean[5], Residuals_std[5]), np.add(Residuals_mean[5], Residuals_std[5]),
                     color='black', alpha=0.2)

    plt.xlabel(r'$\mathbf{k}$', fontsize=12)
    plt.yscale('log')
    plt.ylabel(r'$\mathbf{\|Ax - b\|/\|b\|}$', fontsize=16)
    plt.legend()
    plt.grid(True)
    plt.savefig('relative_residual.png', format='png', dpi=200, bbox_inches='tight')
    plt.show()


def plotErr(errors, s=40):
    Errors_mean = []
    Errors_std = []
    errors_mean = []
    errors_std = []
    X = [k for k in range(len(errors[0][0])) if k % s == 0]

    for i in range(len(errors)):
        errors_mean.append(np.mean(errors[i], axis=0, dtype=np.float64))
        errors_std.append(np.std(errors[i], axis=0, dtype=np.float64))

    for i in range(len(errors)):
        Errors_mean.append([errors_mean[i][l] for l in X])
        Errors_std.append([errors_std[i][l] for l in X])

    plt.figure(figsize=(6, 6))

    plt.plot(X, Errors_mean[0], label=r'\textbf{RK}', color='blue')
    plt.plot(X, Errors_mean[1], marker='', linestyle='dashed', label=r'\textbf{RSK}', color='limegreen')
    plt.plot(X, Errors_mean[2], linestyle='-.', label=r'\textbf{RSKA-v1}', color='black')
    plt.plot(X, Errors_mean[3], linestyle=':', label=r'\textbf{RSKA-v2}', color='black')
    plt.plot(X, Errors_mean[4], marker='', label=r'\textbf{RSKA-v3}', color='black')
    plt.plot(X, Errors_mean[5], linestyle='--', label=r'\textbf{RSKA-v4}', color='black')  # linestyle='dashdot'

    plt.fill_between(X, np.subtract(Errors_mean[0], Errors_std[0]), np.add(Errors_mean[0], Errors_std[0]), color='blue',
                     alpha=0.2)
    plt.fill_between(X, np.subtract(Errors_mean[1], Errors_std[1]), np.add(Errors_mean[1], Errors_std[1]),
                     color='limegreen', alpha=0.2)
    plt.fill_between(X, np.subtract(Errors_mean[2], Errors_std[2]), np.add(Errors_mean[2], Errors_std[2]),
                     color='black', alpha=0.2)
    plt.fill_between(X, np.subtract(Errors_mean[3], Errors_std[3]), np.add(Errors_mean[3], Errors_std[3]),
                     color='black', alpha=0.2)
    plt.fill_between(X, np.subtract(Errors_mean[4], Errors_std[4]), np.add(Errors_mean[4], Errors_std[4]),
                     color='black', alpha=0.2)
    plt.fill_between(X, np.subtract(Errors_mean[5], Errors_std[5]), np.add(Errors_mean[5], Errors_std[5]),
                     color='black', alpha=0.2)

    plt.xlabel(r'$\mathbf{k}$', fontsize=12)
    plt.yscale('log')
    plt.ylabel(r'$\mathbf{\|x - \hat x\|/\|\hat x\|}$', fontsize=16)
    plt.legend()
    plt.grid(True)
    plt.savefig('error.png', format='png', dpi=200, bbox_inches='tight')
    plt.show()

def plot_residuals(results, K):
    plt.figure(figsize=(6,6))
    for key in list(results.keys()):
        plt.plot(results[key]['residuals'], label = '{} = {}'.format(K, key))

    plt.xlabel(r'$\mathbf{k}$', fontsize=12)
    plt.yscale('log')
    plt.ylabel(r'$\mathbf{\|Ax - b\|/\|b\|}$', fontsize=16)
    plt.legend()
    plt.grid(True)
    plt.show()

def plot_errors(results, K):
    plt.figure(figsize=(6,6))
    for key in list(results.keys()):
        plt.plot(results[key]['errors'], label = '{} = {}'.format(K,key) )

    plt.xlabel(r'$\mathbf{k}$', fontsize=12)
    plt.yscale('log')
    plt.ylabel(r'$\mathbf{\|x - \hat x\|/\|\hat x\|}$', fontsize=16)
    plt.legend()
    plt.grid(True)
    plt.show()