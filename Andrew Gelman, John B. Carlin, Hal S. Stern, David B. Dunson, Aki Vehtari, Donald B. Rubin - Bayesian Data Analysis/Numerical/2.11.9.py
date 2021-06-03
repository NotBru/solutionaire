def posterior_mean_and_stddev(prior_stddev):
    prior_var=prior_stddev**2
    alpha=650+0.6*(0.6*0.4/prior_var-1)
    beta=350+0.4*(0.6*0.4/prior_var-1)
    return alpha/(alpha+beta), (alpha*beta/(alpha+beta)**2/(alpha+beta+1))**0.5

prior_stddevs = [ 0.001, 0.005, 0.01, 0.05, 0.1, 0.5, 1 ]
posterior_means_and_stddevs = list(zip(*[ posterior_mean_and_stddev(pdev)
                                          for pdev in prior_stddevs ]))

f = open('2.11.9.out', 'w')
f.write('\\begin{center}\n'
        '\\begin{tabular}{ c | '+'c '*(len(prior_stddevs)+1)+'}\n')
f.write('\tPrior deviation')
for prior in prior_stddevs:
    f.write(' & ${:02}\\%$'.format(prior*100))
f.write(' & Noninformative\\\\\n'
        '\t\hline\n'
        '\tPosterior mean')
for post_mean in posterior_means_and_stddevs[0]:
    f.write(' & ${:.2f}\\%$'.format(post_mean*100))
f.write(' & ${:.2f}\\%$\\\\\n'.format(651/(651+351)*100)+
        '\tPosterior deviation')
for post_dev in posterior_means_and_stddevs[1]:
    f.write(' & ${:.2f}\\%$'.format(post_dev*100))
f.write(' & ${:.2f}\\%$\\\\\n'
            .format((651*351/(651+351)**2/(651+351+1))**0.5*100)+
        '\\end{tabular}\n'
        '\\end{center}\n')
