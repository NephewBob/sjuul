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