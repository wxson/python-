# 抖音直播间弹幕数据爬取

#### 🌈 介绍

该项目仅供学习爬虫技术验证，禁止用于非学习相关的场景。特别是商业用途。    
**注意：** 当前项目需要手动配置部分信息，后续完善wss_url生成逻辑，当前未实现，需手动获取、替换。即代码中注释的 TODO 项

```python
# 根据url获取直播间websocket连接
def fetch_live_room_wss_url(url):
    # TODO 每次测试最好获取到新的wss地址替换调，当前未实现自动生成wss_url的相关逻辑
    # wss_url = f'wss://webcast5-ws-web-hl.douyin.com/webcast/im/push/v2/?app_name=douyin_web&version_code=180800&webcast_sdk_version=1.0.12&update_version_code=1.0.12&compress=gzip&device_platform=web&cookie_enabled=true&screen_width=1920&screen_height=1080&browser_language=zh-CN&browser_platform=Win32&browser_name=Mozilla&browser_version=5.0%20(Windows%20NT%2010.0;%20Win64;%20x64)%20AppleWebKit/537.36%20(KHTML,%20like%20Gecko)%20Chrome/119.0.0.0%20Safari/537.36&browser_online=true&tz_name=Asia/Shanghai&cursor=t-1701393814196_r-1_d-1_u-1_fh-7307429962804499507&internal_ext=internal_src:dim|wss_push_room_id:{room_id}|wss_push_did:7306691797249164810|dim_log_id:20231201092334DCBFC78CB94AB298B67E|first_req_ms:1701393814106|fetch_time:1701393814196|seq:1|wss_info:0-1701393814197-0-0|wrds_kvs:WebcastRoomStatsMessage-1701393813861541304_WebcastRoomStreamAdaptationMessage-1701393810164658479_WebcastInRoomBannerMessage-GrowthCommonBannerBSubSyncKey-1701390122430825363_WebcastRoomRankMessage-1701393645864474492&host=https://live.douyin.com&aid=6383&live_id=1&did_rule=3&endpoint=live_pc&support_wrds=1&user_unique_id=7306691797249164810&im_path=/webcast/im/fetch/&identity=audience&need_persist_msg_count=15&room_id={room_id}&heartbeatDuration=0&signature=RgTmcCrJHYwssA3+'
    # wss_url = f'wss://webcast5-ws-web-hl.douyin.com/webcast/im/push/v2/?app_name=douyin_web&version_code=180800&webcast_sdk_version=1.0.12&update_version_code=1.0.12&compress=gzip&device_platform=web&cookie_enabled=true&screen_width=1920&screen_height=1080&browser_language=zh-CN&browser_platform=Win32&browser_name=Mozilla&browser_version=5.0%20(Windows%20NT%2010.0;%20Win64;%20x64)%20AppleWebKit/537.36%20(KHTML,%20like%20Gecko)%20Chrome/119.0.0.0%20Safari/537.36&browser_online=true&tz_name=Asia/Shanghai&cursor=t-1701393814196_r-1_d-1_u-1_fh-7307429962804499507&internal_ext=internal_src:dim|wss_push_room_id:{room_id}|wss_push_did:7306691797249164810|dim_log_id:20231201092334DCBFC78CB94AB298B67E|first_req_ms:1701393814106|fetch_time:1701393814196|seq:1|wss_info:0-1701393814197-0-0|wrds_kvs:WebcastRoomStatsMessage-1701393813861541304_WebcastRoomStreamAdaptationMessage-1701393810164658479_WebcastInRoomBannerMessage-GrowthCommonBannerBSubSyncKey-1701390122430825363_WebcastRoomRankMessage-1701393645864474492&host=https://live.douyin.com&aid=6383&live_id=1&did_rule=3&endpoint=live_pc&support_wrds=1&user_unique_id=7306691797249164810&im_path=/webcast/im/fetch/&identity=audience&need_persist_msg_count=15&room_id={room_id}&heartbeatDuration=0&signature=RgTmcCrJHYwssA3+'
    wss_url = f'wss://webcast5-ws-web-lq.douyin.com/webcast/im/push/v2/?app_name=douyin_web&version_code=180800&webcast_sdk_version=1.0.12&update_version_code=1.0.12&compress=gzip&device_platform=web&cookie_enabled=true&screen_width=1920&screen_height=1080&browser_language=zh-CN&browser_platform=Win32&browser_name=Mozilla&browser_version=5.0%20(Windows%20NT%2010.0;%20Win64;%20x64)%20AppleWebKit/537.36%20(KHTML,%20like%20Gecko)%20Chrome/119.0.0.0%20Safari/537.36&browser_online=true&tz_name=Asia/Shanghai&cursor=d-1_u-1_fh-7307541472856249382_t-1701419836713_r-1&internal_ext=internal_src:dim|wss_push_room_id:{room_id}|wss_push_did:7306691797249164810|dim_log_id:20231201163716ECE4517588076709ED06|first_req_ms:1701419836634|fetch_time:1701419836713|seq:1|wss_info:0-1701419836713-0-0|wrds_kvs:WebcastRoomStreamAdaptationMessage-1701419829816573423_WebcastInRoomBannerMessage-GrowthCommonBannerBSubSyncKey-1701390122430825363_WebcastRoomStatsMessage-1701419835818121403_WebcastRoomRankMessage-1701419487962863670&host=https://live.douyin.com&aid=6383&live_id=1&did_rule=3&endpoint=live_pc&support_wrds=1&user_unique_id=7306691797249164810&im_path=/webcast/im/fetch/&identity=audience&need_persist_msg_count=15&room_id={room_id}&heartbeatDuration=0&signature=R4wv2GEPf056Ir7S'
```

#### ⛱️ 预览

![image](preview/preview.gif)

#### 💌 支持作者

如果觉得框架不错，或者已经在使用了，希望你可以去<a target="_blank" href="https://gitee.com/wxson/python-crawler.git">Gitee</a>
帮我点个 ⭐
Star，这将是对我极大的鼓励与支持。

#### _若当前项目存在不合规，请联系作者进行删除_
