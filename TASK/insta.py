import instaloader

# Prompt the user to enter their Instagram login credentials
username = input("Enter your Instagram username: ")
password = input("Enter your Instagram password: ")

# Initialize Instaloader and login with the provided credentials
insta = instaloader.Instaloader()
insta.login(username, password)

try:
    # Prompt the user to enter the target Instagram profile username
    target_username = input("Enter the Instagram profile username you want to download the profile picture from: ")

    # Load the profile and download the profile picture only
    profile = instaloader.Profile.from_username(insta.context, target_username)
    insta.download_profile(profile, profile_pic_only=True)

    print("Download successful")
except instaloader.exceptions.ProfileNotExistsException:
    print("Profile with the given username does not exist.")
except instaloader.exceptions.QueryReturnedNotFoundException:
    print("The profile is private or does not exist.")
finally:
    # Always logout after using Instaloader with login credentials
    insta.logout()
