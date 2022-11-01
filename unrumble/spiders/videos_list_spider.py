import scrapy


class VideosListSpider(scrapy.Spider):
    name = "videos_list"
    start_urls = ["https://rumble.com/videos"]

    def parse(self, response):
        videos_in_current_page = response.css("li.video-listing-entry")
        
        #print(videos_in_current_page.getall())
        for video in videos_in_current_page:
            video_title = video.css("h3.video-item--title::text").get().strip()
            video_links = video.css("a.video-item--a").get()
            video_url = video_links[video_links.find('href="') + len('href="') : video_links.find('">')].strip()
            video_image_src = video_links[video_links.find('src="') + len('src="'):(video_links.find(' alt'))].strip()
            
            print(f"url-> {video_url}")
            print(f"src-> {video_image_src}")

    def parse_category(self, response): 
        pass
