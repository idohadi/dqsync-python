"""
Experiment 4.
"""

import pathlib

import numpy as np

import dq_sync as dqs



def experiment4(dirpath):
    # Parameters
    TEST_NAME = "experiment4"
    ns = [100]
    sigma_rs = [0]
    sigma_ts = [0]
    ps = [0.2]
    qs = np.linspace(0.5, 1, 11, endpoint=True)
    rep_no = 50

    # Messaging parameter
    trial_no = len(ns) * len(sigma_rs) * len(sigma_ts) * len(ps) * len(qs) * rep_no;

    # Set up CSV file
    fields = ["n", "sigma_r", "sigma_t", "p", "q", "rep_no", "dq_mean_rerr", "dq_min_rerr", "dq_max_rerr", "dq_mean_terr", "dq_min_terr", "dq_max_terr", "mat_mean_rerr", "mat_min_rerr", "mat_max_rerr", "mat_mean_terr", "mat_min_terr", "mat_max_terr"]
    f, dw = dqs.openCSVFile(dirpath, TEST_NAME, fields = fields)

    # Experimental loop
    row = {}
    count = 0
    for n in ns:
        row['n'] = n

        for sigma_r in sigma_rs:
            row['sigma_r'] = sigma_r

            for sigma_t in sigma_ts:
                row['sigma_t'] = sigma_t

                for p in ps:
                    row['p'] = p

                    for q in qs:
                        row['q'] = q

                        for rep in range(rep_no):
                            row['rep_no'] = rep

                            # Increase the coutner
                            count += 1

                            # Generate ground truth
                            ground_truth = dqs.generateGroundTruth(n)

                            # Run experiment
                            rerr_dqmat, terr_dqmat, rerr_mat, terr_mat \
                                = dqs.experiment(ground_truth, \
                                           sigma_r=dqs.angle2radians(sigma_r), sigma_t=sigma_t, \
                                           p=p, q=q)

                            # Process data
                            row["dq_mean_rerr"] = np.mean(rerr_dqmat)
                            row["dq_min_rerr"] = np.min(rerr_dqmat)
                            row["dq_max_rerr"] = np.max(rerr_dqmat)
                            row["dq_mean_terr"] = np.mean(terr_dqmat)
                            row["dq_min_terr"] = np.min(terr_dqmat)
                            row["dq_max_terr"] = np.max(terr_dqmat)

                            row["mat_mean_rerr"] = np.mean(rerr_mat)
                            row["mat_min_rerr"] = np.min(rerr_mat)
                            row["mat_max_rerr"] = np.max(rerr_mat)
                            row["mat_mean_terr"] = np.mean(terr_mat)
                            row["mat_min_terr"] = np.min(terr_mat)
                            row["mat_max_terr"] = np.max(terr_mat)

                            dw.writerow(row)

                            dqs.logmsg("Trial {:d} of {:d} completed.\n\t\tmean rerr\tmean terr\n\tDQ\t{:.3}\t\t{:.3}\n\tMAT\t{:.3}\t\t{:.3}".format(count, trial_no, row["dq_mean_rerr"], row["dq_mean_terr"], row["mat_mean_rerr"], row["mat_mean_terr"]))

    f.close()


if __name__=="__main__":
    dirpath = pathlib.Path(__file__).parent.resolve()
    print("Writing directory: \t", str(dirpath))
    experiment4(dirpath=str(dirpath))
