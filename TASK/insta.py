import instaloader

name = input("Enter id : ")

insta = instaloader.Instaloader()

insta.download_profile(name,profile_pic_only = True)

print("download succesfull")