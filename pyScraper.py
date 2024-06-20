# %%
import requests
import pandas as pd


# %%
twitter_data= []


# %%
payload= {
    "api_key":"f0d763215596beae85f33e572973091f",
    "query":"web3 jobs",
    "num":"10" #number of tweets to scrape

    }


# %%
# create the response
response= requests.get(
    "https://api.scraperapi.com/structured/twitter/search", params=payload

    )


# %%
# parsing link to the scraperAPI
# After getting response, lets store the data in json
data= response.json()

print(data)


# %%
print(type(data))
# we see down here that our data is a dictionary


# %%
print(data.keys())
# down here we see that we have 4 keys i.e"'search_information', 'organic_results', 'images', 'pagination'"


# %%
print(data["search_information"])


# %%
print(data["organic_results"])


# %%
print(data["pagination"])
# dow here we see it giives us additinal metadata of our dataframe


# %% [markdown]
# # from above, the most inportant for us is the organic_results

# %%
# check type of organic_results
print(type(data["organic_results"]))


# %%

# found that organic_results is a list
# now lets get some elements of the list
print(data["organic_results"][0])


# %%
# seems each element in the list is a dictionary
# Now let's use keys of the dictionaries to access info
print(data["organic_results"][0].keys())


# %%
# Now we get title for our first tweet
print(data["organic_results"][0]["title"])


# %%
# Now we get snippet for our first tweet
print(data["organic_results"][0]["snippet"])


# %%
# Now let's iterate through the data and put it into a well organized DataFrame



