# Continuation of elemantary data analysis project on apps profitability

### Dataset description

This data set is about Mobile app statistics from apple IOS app store. I’ve chosen to work on this data as I’ve done some previous
analysis on the data. The analysis was simply finding the app category which attracts the most number of users and which category would be profitable for
building new applications on app store. I’ve found this data here: https://www.kaggle.com/ramamet4/app-store-apple-data-set-10k-apps

### Decision nodes

The decision tree contain various nodes. First, it’s dividing the data if size_bytes <= 14742…, then if price <= 1.49, then dividing the data by all of the
four target variables plus the entropy. For most the nodes, the class is Entertainment. Making predictions on this data set after looking at the decision
is pretty hard. The distributions of the nodes is vague.

### Modeling discussions

Intentionally, I’ve chosen the predictor variables which wouldn’t provide the appropriate reason for one to download the app from a particular category
except for the user_ratings. In my previous analysis, I’ve seen the people give high ratings to the apps under Games category. From both the predictions
from R and Python I’ve found that Games is the predicted class with 46% of the missed predictions. 

### Decision tree

<img width="1068" alt="Decision_tree" src="https://user-images.githubusercontent.com/63217569/219815780-ef7d0247-bccf-4f32-aefe-24029f5dea05.png">
