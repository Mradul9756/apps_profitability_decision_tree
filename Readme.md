# LM4 Decision Trees 
Class: CS251-1 – Introduction to Data Science 
Last Modified: 3/11/2021
Whitworth University

For this module you are going to build your skills of building decision tree models.

### Grade Break Down
| Part   |                    | Points |
|--------|--------------------|--------| 
| Part 1 | Python & R CART Modeling     | 25 pts |  
| Part 2 | Predict target variable with test data  | 25 pts |
|        |                    |Total: 50|

### Code Requirements
- Submit both .py and .r files, no jupyter notebook files.
- Header comments with your name and data
- Good and proper comments
- Proper spacing and neat coding

-----
## Part 1 & 2 Python and R CART modeling on a data set of your choice

Pick a data set you are interested in. (It can be from the book or online)
Complete the following analysis in both Python and in R. Save your .py and .r in this folder and submit to whitgit. 

1. In the following space provided, describe the data set and why it interests you, also describe where you found this data set.

    ```
        Describe your data here: This data set is about Mobile app statistics from apple IOS app store. I’ve chosen to work on this data as I’ve done some previous analysis on the data. The analysis was simply finding the app category which attracts the most number of users and which category would be profitable for building new applications on app store. 
I’ve found this data here: https://www.kaggle.com/ramamet4/app-store-apple-data-set-10k-apps


    ```
2. Partition the data set into training and test.
2. Do a CART analysis using the training data set for a particular target variable.
3. Look at the graph, and see if the decision nodes make sense. Describe your thoughts about the decision nodes below:

    ```
        Describe your data here: The decision tree contain various nodes. First, it’s dividing the data if size_bytes <= 14742…, then if price <= 1.49, then dividing the data by all of the four target variables plus the entropy. For most the nodes, the class is Entertainment. Making predictions on this data set after looking at the decision is pretty hard. The distributions of the nodes is vague.

    ```

4. Run a prediction on the test data.
5. Describe the results. How well did your model do? Write your answer below.
  
    ```
        Were the predicted target variables accurate? What was the percentage of missed predictions?
        Intentionally, I’ve chosen the predictor variables which wouldn’t provide the appropriate reason for one to download the app from a particular category except for the user_ratings. In my previous analysis, I’ve seen the people give high ratings to the apps under Games category. From both the predictions from R and Python I’ve found that Games is the predicted class with 46% of the missed predictions. 

    ```
