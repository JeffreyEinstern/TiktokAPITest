# TiktokAPITest

#### 打包
* pip freeze >  packages.txt
#### 安装依赖包
* pip install -r  packages.txt

1.HashTag


with TikTokApi() as api:
    file_name = f"{hashtag}_{timestamp}"
    tag = api.hashtag(name=hashtag)
    # print(tag.info())
    tag_video_sorted = sorted(tag.videos(count=1999), key=lambda x: x.create_time, reverse=True)
    time.sleep(2)
    if tag_video_sorted:
        tag_video_sort_data = [info.as_dict for info in tag_video_sorted]
        with open(f"./data/{file_name}.json", 'w') as outfile:
            FileNameQueue.put(file_name)
            json.dump(tag_video_sort_data, outfile)
            print(f"good~~  crawler {hashtag} tiktok hash finished")
            
 2.User
 
 with TikTokApi() as api:
 
    user = api.user(username="bianca2849")
    print(user.info_full())
