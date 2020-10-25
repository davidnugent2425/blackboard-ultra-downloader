from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
import urllib.request

def main():
    driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
    collab_ultra_url = input("Enter the link to the lecture below:\n")
    driver.get(collab_ultra_url)
    time.sleep(5)
    player_container = driver.find_element_by_id('playback-video-playback-video_html5_api')
    root_video_url = player_container.get_attribute('src')
    driver.get(root_video_url)
    video = driver.find_element_by_tag_name('source')
    video_src = video.get_attribute('src')
    print("Starting download, may take a few mins. Wait for program to finish...")
    urllib.request.urlretrieve(video_src, 'lecture.mp4')
    print("lecture.mp4 downloaded")
    driver.close()

if __name__ == "__main__":
    main()
