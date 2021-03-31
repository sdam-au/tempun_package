# tempun

![](https://zenodo.org/badge/DOI/10.5281/zenodo.4650989.svg)

### Citation
Vojtěch Kaše. (2021, February 19). tempun (Version v0.1). Zenodo. http://doi.org/10.5281/zenodo.4650989

## Description

`tempun` is a Python 3 package to deal with temporal uncertainty in historical & archaeological datasets. Dating of historical artifacts (e.g. inscriptions, books etc.) is typically expressed by means of a **dating interval** during which it is assumed that the artifact was produced. Commonly, the production itself was much shorter than the interval and did not take more than one year. Therefore, the interval rather expresses **uncertainty** concerning the actual date of production. The question is how to analyze temporal trends in data revealing such temporal uncertainty.

A way forward is to use the interval to extract **probability** of production of the artifact. All dates (years) outside of the dating interval have probality *p*=0; all dates within the interval have probability somehow proportional to the duration of the interval, while the sum of  probabilities for all years within the interval has to be equal to 1. This probality has to follow certain **distribution**. The package works with uniform or trapezoidal distribution. With uniform distribution, each year within the interval has an equal probality to be the year of production of the artifact. 

We can use the intervals and the probalities associatiated with them to randomly assign individual dates (years) to each artifact within our dataset. In other words, we can **model** or **simulate** the date.  We can do this repeatedly, i.e. to each artifact assign a certain number of **random dates**.  This is in the core of a **Monte Carlo Simulation** (MCS) approach. In the package, it is is implemented by means of `model_date()` function. 

Having the random dates, we can proceed to do the analysis. For instance, we can recombine these dates into **multiple time series** and to compare between them. The package includes a bunch of functions developed for this purpose.

## Getting started

The package can be installed via `pip`:

```bash
pip install tempun
```

To be sure that you have the latest version, use `pip install tempun --ignore-installed`. To install it directly from Jupyter, use `!pip install tempun`.

In Python, import the package:

```python
import tempun
```

## Documentation (in progress)

### model_date()

This function requires at least two parameters:

* `start`
* `stop`

If both `start` and `stop` are numbers, model_date(start, stop) returns a random number within the range starting with `start` and ending with `stop`.

If `stop` is not a valid number or contains an empty value, `start` is interpreted as defining a NOT BEFORE date (the so called ante quem*)

If `start` is not a valid number or contains an empty value, `stop` is interpreted as defining a NOT AFTER date (the so called *post quem*)

If `start` and `stop` are identical, the function returns the same number as well.

There are three optional parameters:

* `size=1`: how many random numbers you want to get; by default, size=1, i.e. only one number is returned
* `b`: bending point *b* defining shape of the trapezoidal distribution; by default, *b*=0.1; set to 0 to get uniform distribution
* `scale`:  scale of the half-uniform distribution used to model ante quem and post quem; by default scale=25

The function returns an individual number (if size=1; i.e. by default) or a list of numbers of length equal to size

```python
# example 1: only start and stop
>>> tempun.model_date(-340, -330)
-337
# example 2: size specified (returns a list of numbers of given size
>>> tempun.model_date(-340, -330, 10)
[-334, -333, -332, -336, -332, -338, -333, -336, -333, -331]
# example 3: model post quem (with default scale)
>>> tempun.model_date(114, "", 10)
[123, 143, 123, 149, 123, 155, 125, 115, 128, 132]
```



## Version history

* 0.1 - first version
