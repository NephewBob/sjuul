# Data description
* https://www.gemconsortium.org/data/sets

## NES
* National expert survey, questionnaire sent out to relevant experts in each country.
* questions are encoded as NES_A01_MEAN10
  * NES stands for national expert survey
  * A01 is the question identifier, a mapping is available in the variables csv
  * MEAN10 stands for 0 to 10 scale, 0 completely false, 10 completely true.
  * MEAN9 stands for 1 to 9 scale, 0 completely false, 10 completely true.
  * MEAN7 stands for 1 to 7 scale, 1 completely false, 7 completely true.
  * MEAN5 stands for 1 to 5 scale, 1 completely false, 5 completely true.
  * SUM_10 stands for a -4 to 4 scale, -4 completely false, 4 completely true, other SUM_* have no scale, ignore these.

## APS
* Adult population survey, questionnaire to general populace.

# Ideas
* We regress Total Entrepeneurial Activity (TEA) against Perceived Skills.
* Most of the APS data point are percentages. So I am using the logit transformation.\
  Perhaps Beta regression is a good idea. https://towardsdatascience.com/a-guide-to-the-regression-of-rates-and-proportions-bcfe1c35344f
* Perform regression over time.

# Checklist
https://www.learnbymarketing.com/tools/linear-regression-checklist/
Linear Regression is a well-studied and frequently applied tool.  In this checklist, I walk you through the steps you need to take to have a valid, useful model.  If you’re interested in a “in-the-works” R package for this tool, check out lmade.

## Business Understanding
This is the thing no automation software can handle.  You, as an analyst, need to know the background of the model and its importance.

* Do you know what you’re trying to model?
* Do you know why you’re trying to model?
* What is the potential outcomes of your model?

## Data Understanding
Examining your data, you’ll need to find patterns that you can take advantage of in your model.  The majority of insight usually comes from plotting your data and toying with the results.

* Do you know what all of your data means?
* Plot your X and Y variables.
* Examine correlation among your X and Y variables.
* Look for outliers in your data.
* Look for missing data.
* Does that missing data have a pattern or meaning?
* Try simple models, based on business understanding first.

## Data Preparation
With a firm understanding of the attributes of your data, you’ll start applying some modification to your data and potentially creating new variables.

* Create dummy variables (if necessary) and identify your base case.
* Fill in missing data.
* Possibly drop outliers.
* Transform your X variables
* Transform your Y variable (e.g. natural log).
* Extract features (PCA, Clustering).
* Potentially find more data.

## Linear Regression Assumptions
Traditionally, you’ll want to check these assumptions after building your model.  If any of these assumptions aren’t met, you cannot be confident that your model’s coefficients are truly the best.

* Sum and mean of errors are zero.
* Errors are normally distributed.
* Errors are independent of each other.
* Variance of errors are constant.

## Checking Model Assumptions
* Plot residuals on vertical axis and each X variable on horizontal axis.
* Plot residuals on vertical axis and actual Y variable on horizontal axis.
* Check if 5% or more of residuals are outside two standard deviations from zero.
* If some coefficients have unexpected signs, check for multi-collinearity.

### Unequal Variances
* Plot residuals and look for expanding pattern.  Apply log transformation to Y.

### Normality Assumption
* QQ Plot and Histogram
* Jaque-Bera test for normality.

### Influential / Outlier Points
* Standardized Residuals
* Studentized Residuals
* Jacknife
* DBScan

### Detecting Residual Correlation
* Durbin-Watson test

## Model Performance
What’s the point of building a model if it isn’t accurate on new data.  
One of the most important tasks is to create a validation set: a set of data that the model has never seen. 
A validation set lets you report unbiased performance measures.
Many statistical tools will report these measures on your training data automatically.

* Multiple R-Squared and Adjusted R-Squared
* Root Mean Squared Error
* Mean Absolute Error