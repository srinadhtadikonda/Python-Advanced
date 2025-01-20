



import json 
import facebook 
  
def main(): 
    token = "Please replace this line with your access token"
    graph = facebook.GraphAPI(token) 
    post_ids =["USERID_POSTID# 1", "USERID_POSTID# 2"] 
    posts = graph.get_objects(ids = post_ids, fields ='created_time') 
  
    # print creation time of the two posts. 
    print(json.dumps(posts, indent = 4)) 
  
if __name__ == '__main__': 
    main() 
