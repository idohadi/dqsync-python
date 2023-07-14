import pandas as pd
import matplotlib.pyplot as plt


def calcMeanDF(data, index):
    return data.pivot_table(index=index, aggfunc='mean').reset_index()



if __name__=="__main__":
    # Load data
    data = pd.read_csv("experiment5-2023-07-14-161219.csv")

    # Pivot data
    pdata = calcMeanDF(data, ['q'])

    # Plot everything
    fig, axs = plt.subplots(1, 2, sharex=True, constrained_layout=True)

    for erri, err in enumerate(["rerr", "terr"]):
        ax = axs.flatten()[erri]

        if err == "rerr":
            ax.set_ylabel("Rotation Error")
        else:
            ax.set_ylabel("Translation Error")

        for prefix in ["dq", "mat"]:
            ax.semilogy(pdata["q"][:-1], pdata["_".join([prefix, "mean", err])][:-1], '-o', markersize=3, \
                    label = prefix.upper() + ",mean", \
                        lw = 0.5)
            ax.fill_between(pdata["q"][:-1], \
                            pdata["_".join([prefix, "min", err])][:-1], \
                            pdata["_".join([prefix, "max", err])][:-1], \
                            alpha = 0.3, \
                            label = prefix.upper() + ",[min,max]")

        ax.grid(which="both", alpha = 0.3)
    axs[-1].legend(fontsize = 8, loc = "lower left")

    fig.supxlabel("Percent of non-corrupted entries ($ q $)")

    fig.set_size_inches(7.75, 3.4)
    plt.show(block=False)
    plt.savefig("experiment5_fig.pdf")
