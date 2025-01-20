



import json 
import facebook 
  
def main(): 
    token = "Please replace this with your access token"
    graph = facebook.GraphAPI(token) 
    friends = graph.get_connections(id ='me', connection_name ='friends') 
    print(json.dumps(friends, indent = 4)) 
  
if __name__ == '__main__': 
    main() 
