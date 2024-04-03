from moviepy.editor import *
import os
import cv2 


def compile(batch_counter):
    videos = []
    os.chdir(f"C:/Users/lucas/OneDrive/Desktop/dev/automated yt/batches/batch{batch_counter}")
    for file in os.listdir():
        vid = adding_bg(file)
        
        videos.append(vid)
    
    #compiles the clips together
    big_vid = concatenate_videoclips(videos,method="compose")
    
    # saves the compilation to a file
    big_vid.write_videofile(f"C:/Users/lucas/OneDrive/Desktop/dev/automated yt/compilations/comp{batch_counter}.mp4")


def adding_bg(vid_file):
    # create video object out of videofile 
    #reel_path = f"C:/Users/lucas/OneDrive/Desktop/dev/automated yt/batches/batch{bacth_num}/{vid_file}"
    og_clip = VideoFileClip(vid_file)
    
    newclip = og_clip.set_position("center","center")

    #newclip =  newclip.resize(1.25)

    vid_frame = (og_clip.resize((1080,1920))).get_frame(2)
    
    
    img = cv2.blur(vid_frame,(7,7))

    #make image squence 
    blur_vid = ImageClip(img)
    #blur_vid= blur_vid.resize(1.5)
    video_clip = concatenate_videoclips([blur_vid.set_duration(og_clip.duration)])
    print(video_clip.duration)
    print(og_clip.duration)
    
    
    impove_vid = CompositeVideoClip((video_clip, newclip),use_bgclip=True,)

    return impove_vid
    
   
  

    

    



def uploadCompilations(batch_counter):
    os.chdir(r"C:\Users\lucas\OneDrive\Desktop\dev\automated yt")
    command = f'python upload_video.py --file "C:/Users/lucas/OneDrive/Desktop/dev/automated yt/compilations/comp{batch_counter}.mp4" --title "funny compilation{batch_counter}" --description "This is an automated channel for memes I made inorder to improve my coding skills. Enjoy." '
    os.system(command)
    

#figure out what current batch number is 
def batch_number():
    os.chdir("C:/Users/lucas/OneDrive/Desktop/dev/automated yt/batches")
    batches = len(os.listdir())
    current_batch = batches+1
    return(current_batch)


def res_checker():
    
    for batch in os.listdir("C:/Users/lucas/OneDrive/Desktop/dev/automated yt/batches"):
        for file in os.listdir(f"C:/Users/lucas/OneDrive/Desktop/dev/automated yt/batches/{batch}"):
            
            
            filevid = VideoFileClip(f"C:/Users/lucas/OneDrive/Desktop/dev/automated yt/batches/{batch}/{file}")
            print(filevid.size)


#res_checker()
#adding_bg("2024-03-21_06-44-03_UTC.mp4",2)