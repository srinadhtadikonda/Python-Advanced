import json 
import facebook 
from facebook import GraphAPI 
def main(): 
    token = "EAAlZB3bUwW10BQIpWybsWb0OlTZBxUZAsRAVGIkj03HgEWnIsZBGEnRK5DZBZBzlBRjjtVIgYh7Cm5sZBMZBR9M6aFZCgu3YQLD3KpzBI7OF3kurtUm5QSoBetWveOFiExoL3pOM2GeeW8n4JZAbs61OPzGwH7Rpj6NZCrQto9F9r9ZAcsMmXd4A0wqjIp4ToxeJJZAQJNSU4Ap5nPz4d8rxMwjm3dgBR3AnqwP4c"
    graph = facebook.GraphAPI(token) 
    profile = graph.get_object('me', fields ='first_name, gender, birthday, email')  
     
    # return desired fields 
    print(json.dumps(profile, indent = 4)) 
  
if __name__ == '__main__': 
    main() 
