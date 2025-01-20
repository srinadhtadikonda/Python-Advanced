
import json 
import facebook 
  
def main(): 
    token = "Please replace this with your PAGE Access Token"
    graph = facebook.GraphAPI(token) 
    posts_25 = graph.get_connections(id ='PAGE_ID', connection_name ='posts', 
                                                  fields ='id, created_time') 
  
    print(json.dumps(posts_25, indent = 4)) 
  
if __name__ == '__main__': 
    main()  
