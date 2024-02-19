from instagrapi import Client

def unfollow_all_users(username, password):
    # Create an Instagram client
    client = Client()
    
    # Login to your Instagram account
    client.login(username, password)
    
    # Get the user ID of the authenticated user
    user_id = client.user_id
    
    # Get the list of users you are following
    following_list = client.user_following(user_id)
    
    # Unfollow each user in the list
    for user in following_list:
        client.user_unfollow(user['pk'])
        print(f"Unfollowed user: {user['username']}")
    
    # Logout after the operation
    client.logout()

# Replace <username> and <password> with your Instagram credentials
username = "<your_username>"
password = "<your_password>"

unfollow_all_users(username, password)
