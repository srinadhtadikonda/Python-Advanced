



import json 
import facebook 
  
def main(): 
    token = "Please replace this line with your access token"
    graph = facebook.GraphAPI(token) 
    photo_ids =["USERID_PHOTOID# 1", "USERID_PHOTOID# 2"] 
    photos = graph.get_objects(ids = photo_ids, fields ='comments.summary(true)') 
  
    # print total comment count for each photo 
    print(json.dumps(photos, indent = 4)) 
  
if __name__ == '__main__': 
    main() 
