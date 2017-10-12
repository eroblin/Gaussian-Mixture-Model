In statistics, a mixture model is a probabilistic model for representing the presence of subpopulations 
within an overall population, without requiring that an observed data set should identify the sub-population
to which an individual observation belongs. 

Here we analyse the case of a mixture model of gaussians. For instance, in biology, observations obtained using different experiments
can have a gaussian distribution. However, some observations can let a second gaussian curve appear, different from
the first one. The purpose is to work on each group of observations seperatly: this is a gaussian mixture model. 

This type of model is based on a mix of densities. It enables to estimate the distribution of a random variable using a sum of different
gaussian variables. Here, we use a varaible of 1. We want to find the expectancy. Here are our simulated data: 

![alt text](https://github.com/eroblin/Gaussian-Mixture-Model/blob/master/data_distribution.png)

A way to estimate the a posteriori expectancy in this case is to use MCMC methods, based on the simulation of the a posteriori law.
 
First, we use a Gibbs Sampler algorithm. It uses the principle of data augmentation. The idea is to construct iterative algorithms for sampling based on the introduction of unobserved data. We compare two different cases: one with 10 000 iterations and one with 100 000. Here are the resutls:  

![alt text](https://github.com/eroblin/Gaussian-Mixture-Model/blob/master/table_10000.png)

![alt text](https://github.com/eroblin/Gaussian-Mixture-Model/blob/master/estimation_10000.png)

![alt text](https://github.com/eroblin/Gaussian-Mixture-Model/blob/master/table_100000.png)

![alt text](https://github.com/eroblin/Gaussian-Mixture-Model/blob/master/estimation_100000.png) 

With this algorithm, we are confronted with the problem of "label switching". The Metropolis Hasting algorithm is a way to overcome this issue.


