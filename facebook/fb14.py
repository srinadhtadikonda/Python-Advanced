import json 
import facebook 
  
def main(): 
    token = "Please replace this with your PAGE ACCESS TOKEN"
    graph = facebook.GraphAPI(token) 
    putlike = graph.put_like(object_id ="PAGEID_POSTID") 
    print(json.dumps(putlike, indent = 4)) 
  
if __name__ == '__main__': 
    main() 
