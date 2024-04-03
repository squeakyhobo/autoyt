import instaloader
import os
from moviepy.editor import *
import random
import shutil
#task 
#fix scraping funtion 

def mp4():
    print(os.getcwd())
    os.chdir("playground")
    files = os.listdir()
    for file in files:
        if file.endswith("mp4") == False:
            os.remove(file)



# check if video is already in batches 
# I think this is slightly bugged
def vid_inbatches(reel_file):
    
    
    reel_filename = filename(reel_file)
    
   
    os.chdir(r"C:\Users\lucas\OneDrive\Desktop\dev\automated yt\batches")
    print("checking if reel has been used before...")
    for batch in os.listdir():
        print(batch)
        #get a way to go through files 
        for file in os.listdir(batch):
           print(file)
           
           
           batchpath = os.path.abspath(file)
           namefile = filename(batchpath)
           
           if reel_filename == namefile :
                print("Reel has been used before...")
                print("This will not be used...")
                os.remove(reel_file)
                

                return False
    return True
            
        


def filename(path):
    fileName =os.path.basename(path)
    return(fileName)

def durationChecker(bacth_counter):
    totalDuration = 0
    #get file form current bacth 
    os.chdir(f"C:/Users/lucas/OneDrive/Desktop/dev/automated yt/batches/batch{bacth_counter}")
    
    for file in os.listdir():
        vid = VideoFileClip(file)
        totalDuration = totalDuration +(vid.duration)
    vid.close()
    return totalDuration
        
def isRight_res():
    #check the files in playground (Threre will only be one there at a time)
    os.chdir("C:/Users/lucas/OneDrive/Desktop/dev/automated yt/playground")
    for file in os.listdir():
        vid = VideoFileClip(file)
        vid_res = vid.size
        print(vid_res)
        if vid_res == [1080,1920]:
            vid.close()
            return True
        else:
            #remove file from playground
            vid.close()
            os.remove(file)
            return False
#sorts the reels by resolution 
def res_sort():
    L = login()
    profile = instaloader.Profile.from_username(L.context,"dudewithcoolusername")
     
    posts = profile.get_posts()
    os.chdir(r"C:\Users\lucas\OneDrive\Desktop\dev\automated yt")
    for post in posts:
        if post.is_video:
            L.download_post(post=post,target="playground")
            
            mp4()
            for file in os.listdir(r"C:\Users\lucas\OneDrive\Desktop\dev\automated yt\playground"):
                clip = VideoFileClip(file)
                print(clip.size)
                clip.close()
                os.remove(file)
            

             

def login():
    username = "cheetoez40"
    password = "vkv296%)P(Y+?Et"
    L = instaloader.Instaloader(max_connection_attempts=1)
    #L.load_session_from_file(username="cheetoez40",filename=r"C:\Users\lucas\AppData\Local\Instaloader\session-cheetoez40",)
    L.login(username,password)
    print("Logging in...")
    return L 


def scraping_vids(L,batch_counter):
   
    username = "cheetoez40"
    password = "vkv296%)P(Y+?Et"
    autoyt_path = "C:/Users/lucas/OneDrive/Desktop/dev/automated yt"

    # do memes have to be random

    

    #scrape higest viewed reels from people I follow 
    profile = instaloader.Profile.from_username(L.context,username)
    
    following= profile.get_followees()
    following = list(following)
    
    while True:
        os.chdir(autoyt_path)
        #pick a random meme account in following list
        
        memeProfile = random.choice(following)
        print(f"scraping {memeProfile.username}...")
        
        #get most viral posts - this may take too long to do 
        #posts = sorted(memeProfile.get_posts(),key= lambda post:post.likes,reverse=True)


        posts = memeProfile.get_posts()
        #keep digging for one reel that I have not used before
        for post in posts:
            print(f"seacrhing for new reel from{memeProfile.username}")
            if post.is_video :
                # download reels in playgroundand then compare it to videos in batches
                os.chdir(r"C:\Users\lucas\OneDrive\Desktop\dev\automated yt")
                L.download_post(post,f"playground")
                L.close()
                mp4()

                #checks playgrounds files to see if in bacthes(normally it is only one file in there at a time)
                for file in os.listdir():
                    filepath = os.path.abspath(file)
                    new_reel = vid_inbatches(filepath)
                    #check the resolution of the scraped reels
                    #is_1080_1920 = isRight_res()
                    #delete playground folder as either way it is not needed 
                    
                    
                    #if reel is not new then keep scraping post 
                    if new_reel == False:
                        print("file has been used before...")
                        # need to scrape another reel if this ahs been used before from the same person
                        print("scraping a new reel from same acount")

                        
                        
                    

                    # if new res I want to keep scraping the same person 
                    #if is_1080_1920 == False:
                        
                       # break



                    # if reel is indeed new then move it to current batch
                    if new_reel == True :
                    #and is_1080_1920 == True:
                        print("found a new reel that has the right resolution")
                        basefilename = os.path.basename(filepath)
                        #moving file to the current batch
                        os.rename(filepath,f"C:/Users/lucas/OneDrive/Desktop/dev/automated yt/batches/batch{batch_counter}/{basefilename}")
                        
                        #check current duration of batch to see if greater than 30 seconds
                        duration = durationChecker(batch_counter)
                        #if the duration is less than 30 secnds pick new random mempage to scrapte
                        if duration <= 30:
                            print("duation is less then 30 , continuing to scrape...")
                            print("scraping a new meme page")
                            scraping_vids(L,batch_counter)
                            duration = durationChecker(batch_counter)
                            
                            #break out of the playground for loop
                            
                        #if the duration is greater than 30 but less than 60 then stop the scraping
                        if duration >= 30 and duration <= 60:
                            print("scraping done")
                            return duration
                        #if the duration is greater then 60 , then remove last vid from batches and stop the scrape
                        if duration >= 60:
                            print("duration is greater than 60 seconds")
                            print("cutting it down")
                        
                            # create a list of the file 
                            batch = os.listdir(f"C:/Users/lucas/OneDrive/Desktop/dev/automated yt/batches/batch{batch_counter}")
                            # removes the last file in the batch
                            os.remove(f"C:/Users/lucas/OneDrive/Desktop/dev/automated yt/batches/batch{batch_counter}/{batch[-1]}")
                            #stops the whole function 
                            print("scraping done")
                            return duration 
                        #need to make one if duration is greater than 60 and len 1
                #break out of the the post in posts loop
                     
                        
                

            

                #only videos 
                #check if video is already there in other batches

#res_sort()

                 
        
            






        


