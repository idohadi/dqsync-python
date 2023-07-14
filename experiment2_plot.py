import pandas as pd
import matplotlib.pyplot as plt


def calcMeanDF(data, index):
    return data.pivot_table(index=index, aggfunc='mean').reset_index()



if __name__=="__main__":
    # Load data
    data = pd.read_csv("experiment2-2023-07-14-155129.csv")

    # Pivot data
    pdata = calcMeanDF(data, ['p', 'sigma_t'])

    # Plot everything
    fig, axs = plt.subplots(2, 2, sharex=True, sharey='row', constrained_layout=True)

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
                ax.set_xlabel("$ \\sigma_{t} $ ")

            if erri == 0:
                ax.set_ylim(1e-10, 3e0)

            for prefix in ["dq", "mat"]:
                ax.semilogy(subdata["sigma_t"], subdata["_".join([prefix, "mean", err])], '-o', markersize=3, \
                        label = prefix.upper() + ",mean", \
                            lw = 0.5)
                ax.fill_between(subdata["sigma_t"], \
                                subdata["_".join([prefix, "min", err])], \
                                subdata["_".join([prefix, "max", err])], \
                                alpha = 0.3, \
                                label = prefix.upper() + ",[min,max]")

            ax.grid(which="both", alpha = 0.3)
    axs[-1, -1].legend(fontsize = 8)

    plt.show(block=False)
    plt.savefig("experiment2_fig.pdf")

