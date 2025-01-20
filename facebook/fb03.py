import json 
import facebook 
  
def main(): 
    token = "Please replace this line with your access token"
    graph = facebook.GraphAPI(token) 
    post = graph.get_object(id ='USERID_POSTID', fields ='message, attachments{description}') 
    # return desired fields 
    print(json.dumps(post, indent = 4)) 
  
if __name__ == '__main__': 
    main() 
