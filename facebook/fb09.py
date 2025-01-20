
import json 
import facebook 
  
def main(): 
    token = "Please replace this with your PAGE Access Token"
    graph = facebook.GraphAPI(token) 
    posts_25 = graph.get_connections(id ='POST_ID', connection_name ='comments',  
                                     include_hidden = True, order ='reverse_chronological', 
                                     filter ='stream', summary ='total_count') 
  
    print(json.dumps(posts_25, indent = 4)) 
  
if __name__ == '__main__': 
    main(
