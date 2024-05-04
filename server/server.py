from server.constants import USER_AGENTS 
from server.bestbuy import fetch_bestbuy
from server.newegg import fetch_newegg
from server.walmart import fetch_walmart
from fastapi import FastAPI

app = FastAPI()

unused_agents = USER_AGENTS.copy()
i = 0
headers = {}
items = []

def getAgent():
    global i
    agent = unused_agents[i]
    i += 1
    if i == len(USER_AGENTS) - 1:
        i = 0
    return agent

@app.get("/")
def getItems(item):
    try:
        #Walmart
        items.append(fetch_walmart(item, getAgent()))
        #BestBuy
        items.append(fetch_bestbuy(item, getAgent()))
       
        #Newegg
        items.append(fetch_newegg(item, getAgent()))
        
        return items, 200
    
    except:
        return {"error: Unable to scrap"}, 500