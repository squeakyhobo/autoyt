
import os
from scrape import scraping_vids,login
from compiling import compile,uploadCompilations,batch_number

#tasks

# look into resolution issues
#a result of compiling or chainging the resolution 
# I dont think its scraping the videos as 




def autoyt():
    # based on look in at files , create a way to see what batch I am on 
    current_batch = batch_number()
    print(current_batch)
    os.chdir("C:/Users/lucas/OneDrive/Desktop/dev/automated yt/batches")
    # create a file for new batch 
    os.makedirs(f"batch{current_batch}")
    L = login()
    #scrape 
    scraping_vids(L,current_batch)
    #compile 
    compile(current_batch)
    #upload
    uploadCompilations(current_batch)
    #ensure playground and compilations folders are clear
#while True:
autoyt()


# the quality of the videos is still iffy , i might scrape one that are only resolution of yt shorts 
