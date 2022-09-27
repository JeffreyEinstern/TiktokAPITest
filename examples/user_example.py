from tiktok import TikTokApi

with TikTokApi() as api:
    user = api.user(username="bianca2849")
    print(user.info_full())
    for video in user.videos():
        print(video.id)

    for liked_video in api.user(username="public_likes").videos():
        print(liked_video.id)
