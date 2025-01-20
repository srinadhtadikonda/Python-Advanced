



import json 
import facebook 
  
def main(): 
    token = "Please replace this with your PAGE ACCESS TOKEN"
    graph = facebook.GraphAPI(token) 
commenttopost = graph.put_object(parent_object ="PAGEID_POSTID", 
                connection_name ="comments", 
                message ="Please share and Like the website for content on Computer Science") 
    print(json.dumps(commenttopost, indent = 4)) 
  
if __name__ == '__main__': 
    main() 
