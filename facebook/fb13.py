



import json 
import facebook 
  
def main(): 
    token = "Please replace this with your PAGE ACCESS TOKEN"
    graph = facebook.GraphAPI(token) 
    putcomment = graph.put_comment(object_id ="PAGEID_POSTID", 
                 message ="This is a very good website for Computer Science Topics") 
  
    print(json.dumps(putcomment, indent = 4)) 
  
if __name__ == '__main__': 
    main() 
