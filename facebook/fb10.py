



import json 
import facebook 
from datetime import datetime 
   
def main(): 
    token = "Please replace this with your PAGE Access Token"
    graph = facebook.GraphAPI(token) 
    posts_all = graph.get_all_connections(id ='PAGE_ID', connection_name ='posts', 
                                           fields ='created_time, id', 
                                           since = datetime(2017, 1, 1, 0, 0, 0)) 
  
    for ind, post in enumerate(posts_all): 
     print(json.dumps(ind, indent = 4)) 
     print(json.dumps(post, indent = 4)) 
      
   
if __name__ == '__main__': 
    main() 
