import instaloader
loader = instaloader.Instaloader()

user = input('Enter your Id:-\n')

# loader.login("USER", "PASSWORD")   # Needed only for private account to access

loader.download_profile(user, profile_pic_only=True) # To download profile pic of the given user
print("Profile picture has been downloaded successfully")

profile = instaloader.Profile.from_username(loader.context,user)
post_list = []

try:
    for post in profile.get_posts():   # itterate over posts uploaded by the user
        post_list.append(post)         # append each post into a empty list
except:
    print("Facing some eror")
    
try:
    loader.download_post(post_list[0],'posts')  # To download the latest post uploaded by the user.
    print('Downloaded Successfully')
except IndexError:
    print("You have no posts on this username")
