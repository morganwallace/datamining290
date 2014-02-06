#Homwork: Obtain-Data

##Answers to questions

I am using the [Yelp dataset challenge data](http://www.yelp.com/dataset_challenge/)
####How many records are there:
Data: **yelp_academic_dataset_business.json**

| Command	| Result |
|---|---|
| ``grep "business_id" yelp_academic_dataset_business.json \| wc -l``	| 11537 |

####Finding and interesting record

1. Start by `less yelp_academic_dataset_business.json`
2. Page through data
3. Wanted to find businesses with perfect 5 star reviews with at least 10 reviews:

| Command	| Result |
|---|---|
| ``egrep -o '"review_count": ([0-9]{2,5}).*"stars": 5' yelp_academic_dataset_business.json \| wc -l``	| 94 |

**Properties**: This is the the count of all the businesses that have at least 10 reviews and still have a 5 star rating.
It is **interesting because** one would expect businesses to get a few perfect reviews from the owner and employees but then once real customers give reviews, the rating should have some imperfection. These records don't have imperfections yet, despite having more than 10 reviews. 

Either:

1. They are a rising star, or
2. They have a nefarious effort to artificially boost their yelp rating.

###3 Questions I could answer using my data

1. Are there clusters of well reviewed businesses?
	* Use Lat and Lng coordinates plus rating with clustering algorithm
2. Which category of business gets the highest average rating?
3. Which category of business gets the most reviews?
