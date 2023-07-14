import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import LogLocator as ll


def calcMeanDF(data, index):
    return data.pivot_table(index=index, aggfunc='mean').reset_index()



if __name__=="__main__":
    # Load data
    data = pd.read_csv("experiment1-2023-07-14-154229.csv")

    # Pivot data
    pdata = calcMeanDF(data, ['p', 'sigma_r'])

    # Plot everything
    fig, axs = plt.subplots(2, 2, sharex=True, sharey='row', constrained_layout=True, figsize=(6.4, 3.48))

    for pi, p in enumerate(pdata["p"].unique()):
        subdata = pdata.loc[pdata["p"] == p]

        axs[0, pi].set_title(" $ p = {:.2f} $ ".format(p))

        for erri, err in enumerate(["rerr", "terr"]):
            ax = axs[erri, pi]

            if pi == 0:
                if err == "rerr":
                    ax.set_ylabel("Rotation Error")
                else:
                    ax.set_ylabel("Translation Error")

            if erri == 1:
                ax.set_xlabel("$ \\sigma_{r} $ ")

            for prefix in ["dq", "mat"]:
                ax.semilogy(subdata["sigma_r"], subdata["_".join([prefix, "mean", err])], '-o', markersize=3, \
                        label = prefix.upper() + ",mean", \
                            lw = 0.5)
                ax.fill_between(subdata["sigma_r"], \
                                subdata["_".join([prefix, "min", err])], \
                                subdata["_".join([prefix, "max", err])], \
                                alpha = 0.3, \
                                label = prefix.upper() + ",[min,max]")

                ax.yaxis.set_major_locator(ll(numticks=50))

            ax.grid(which="both", alpha = 0.3)
    axs[-1, -1].legend(fontsize = 6, loc="upper left")

    plt.show(block=False)
    plt.savefig("experiment1_fig.pdf")
