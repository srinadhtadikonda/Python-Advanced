import json 
import facebook 
  
def main(): 
    token = "Please replace this with "me" or your Access Token(for Posting on your wall)\ 
             or with PAGE Access Token(for posting on Page)" 
  
    graph = facebook.GraphAPI(token) 
    message = graph.put_object(parent_object ="me",  
              connection_name ="feed", 
              message ="Hello this is a great website for various Computer Science Topics.", 
              link ="https://www.geeksforgeeks.org") 
  
    print(json.dumps(message, indent = 4)) 
  
if __name__ == '__main__': 
    main() 
