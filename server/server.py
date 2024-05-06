from constants import USER_AGENTS 
from bestbuy import fetch_bestbuy
from newegg import fetch_newegg
from walmart import fetch_walmart
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origin = ["http://localhost:3000"]

# Apply CORS middleware configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=origin,
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

unused_agents = USER_AGENTS.copy()
i = 0
headers = {}

def getAgent():
    global i
    agent = unused_agents[i]
    i += 1
    if i == len(USER_AGENTS) - 1:
        i = 0
    return agent

@app.get("/")
def getItems(item):
    items = []
    try:
        #Walmart
        #items.append(fetch_walmart(item, getAgent()))
        #BestBuy
        items.append(fetch_bestbuy(item, getAgent()))
        #Newegg
        items.append(fetch_newegg(item, getAgent()))
        
        return items, 200
    
    except:
        return {"error: Unable to scrap"}, 500