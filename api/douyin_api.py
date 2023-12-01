from network import request_mapping


class DouyinAPI:

    def __init__(self, token, host):
        self.host = host.rstrip('/')
        self.token = token

    @request_mapping('/douyin/user/info')
    def get_user_info(self, uid):
        """
        获取用户信息
        :param uid:用户user id
        """
        return {
            'token': self.token,
            'uid': uid
        }

    @request_mapping('/douyin/user/live/info')
    def get_user_live_info(self, uid):
        """
        获取直播用户信息
        :param uid: 用户user id
        """
        return {
            'token': self.token,
            'uid': uid
        }

    @request_mapping('/douyin/user/posts')
    def get_user_posts(self, uid, cursor=0):
        """
        获取用户发布的视频作品
        :param uid: 用户user id
        :param cursor: 翻页游标，根据返回结果的max_cursor进行翻页操作，初始值为0
        """
        return {
            'token': self.token,
            'uid': uid,
            'cursor': cursor,
        }

    @request_mapping('/douyin/user/favourites')
    def get_user_favourites(self, uid, cursor=0):
        """
        获取用户点赞过的视频
        :param uid: 用户user id
        :param cursor: 翻页游标，根据返回结果的max_cursor进行翻页操作，初始值为0
        """
        return {
            'token': self.token,
            'uid': uid,
            'cursor': cursor,
        }

    @request_mapping('/douyin/user/promotions')
    def get_user_promotions(self, uid, cursor=0):
        """
        获取用户商品橱窗
        :param uid:用户user id
        :param cursor:翻页游标，默认0
        """
        return {
            'token': self.token,
            'uid': uid,
            'cursor': cursor,
        }

    @request_mapping('/douyin/video/comments')
    def get_video_comments(self, aweme_id, cursor=0):
        """
        获取视频评论
        :param aweme_id:视频id
        :param cursor:翻页游标，默认0，根据返回结果的cursor进行翻页
        """
        return {
            'token': self.token,
            'aweme_id': aweme_id,
            'cursor': cursor,
        }

    @request_mapping('/douyin/video/detail')
    def get_video_detail(self, aweme_id):
        """
        获取视频详情
        :param aweme_id:视频的id
        """
        return {
            'token': self.token,
            'aweme_id': aweme_id,
        }

    @request_mapping('/douyin/video/promotions')
    def get_video_promotions(self, aweme_id):
        """
        获取某个视频的带货商品信息
        :param aweme_id:视频id
        """
        return {
            'token': self.token,
            'aweme_id': aweme_id,
        }

    @request_mapping('/douyin/video/comment/reply')
    def get_video_comment_replies(self, aweme_id, cid, cursor=0):
        """
        获取视频评论的子评论
        :param aweme_id: 视频id
        :param cid: 评论id
        :param cursor: 子评论列表翻页游标，适用于子评论过多的情况下
        """
        return {
            'token': self.token,
            'aweme_id': aweme_id,
            'cid': cid,
            'cursor': cursor
        }

    @request_mapping('/douyin/challenge/detail')
    def get_challenge_detail(self, challenge_id):
        """
        获取话题（challenge）详情
        :param challenge_id:话题id
        """
        return {
            'token': self.token,
            'cid': challenge_id
        }

    @request_mapping('/douyin/challenge/videos')
    def get_challenge_videos(self, challenge_id, cursor=0):
        """
        获取话题（challenge）下的视频
        :param challenge_id:话题id
        :param cursor:翻页游标，根据结果返回的cursor进行翻页操作，初始值为0
        """
        return {
            'token': self.token,
            'cid': challenge_id,
            'cursor': cursor,
        }

    @request_mapping('/douyin/poi/detail')
    def get_poi_detail(self, poi_id):
        """
        获取地点（poi）详情
        :param poi_id: 地点id
        """
        return {
            'token': self.token,
            'poi_id': poi_id
        }

    @request_mapping('/douyin/poi/videos')
    def get_poi_videos(self, poi_id, cursor=0):
        """
        获取地点（poi）下的视频
        :param poi_id: 地点id
        :param cursor: 翻页游标，根据结果返回的cursor进行翻页操作，初始值为0
        """
        return {
            'token': self.token,
            'poi_id': poi_id,
            'cursor': cursor
        }

    @request_mapping('/douyin/promotion/videos/feed')
    def Get_Promotion_Videos_Feed(self, page=1):
        """
        带货视频推荐流
        :param page:页数索引
        """
        return {
            'token': self.token,
            'page': page,
        }

    @request_mapping('/douyin/promotion/info')
    def get_promotion_info(self, promotion_id):
        """
        获取某样带货商品的信息
        :param promotion_id: 商品id
        """
        return {
            'token': self.token,
            'promotion_id': promotion_id,
        }

    @request_mapping('/douyin/promotion/samevideos')
    def get_promotion_same_videos(self, promotion_id):
        """
        同款商品带货视频推荐
        :param promotion_id:商品id
        """
        return {
            'token': self.token,
            'promotion_id': promotion_id,
        }

    @request_mapping('/douyin/liveroom/chat')
    def get_live_room_chats(self, room_id):
        """
        获取抖音直播间弹幕/进入直播间观众/刷礼物/关注主播 信息
        :param room_id:直播间id
        """
        return {
            'token': self.token,
            'room_id': room_id
        }

    @request_mapping('/douyin/liveroom/promotions')
    def get_live_room_promotions(self, room_id):
        """
        获取抖音直播间带货商品信息
        :param room_id:直播间id
        """
        return {
            'token': self.token,
            'room_id': room_id
        }

    @request_mapping('/douyin/lives/room')
    def get_live_room_info(self, room_id):
        """
        获取抖音直播间信息
        :param room_id:直播间id
        """
        return {
            'token': self.token,
            'room_id': room_id
        }

    @request_mapping('/douyin/lives/check')
    def get_live_room_status(self, room_id):
        """
        查询直播间是否开播
        :param room_id:直播间id
        """
        return {
            'token': self.token,
            'room_ids': room_id
        }

    @request_mapping('/douyin/starboard')
    def real_star_board(self):
        """
        实时明星爱DOU榜
        """
        return {
            'token': self.token,
        }

    @request_mapping('/douyin/hotboard')
    def real_hot_board(self):
        """
        实时热点榜
        """
        return {
            'token': self.token,
        }

    @request_mapping('/douyin/goodsboard')
    def real_goods_board(self):
        """
        实时好物榜
        """
        return {
            'token': self.token,
        }

    @request_mapping('/douyin/hotvideos')
    def real_hot_videos(self):
        """
        最热视频榜单
        """
        return {
            'token': self.token,
        }

    @request_mapping('/douyin/funnytags')
    def real_hot_challenges(self):
        """
        热门话题推荐
        """
        return {
            'token': self.token,
        }

    @request_mapping('/douyin/brand/board')
    def real_brand_board(self, category_id, start_date=None):
        """
        实时品牌榜
        :param category_id: 品牌类别id，可以从品牌类别接口获取，一次即可
        :param start_date:开始日期，可用于抓取历史榜单数据，默认空
        """
        return {
            'token': self.token,
            'category': category_id,
            'start_date': start_date
        }

    @request_mapping('/douyin/brand/categories')
    def brand_categories(self):
        """
        品牌类别接口
        """
        return {
            'token': self.token,
        }

    @request_mapping('/douyin/brand/detail')
    def brand_detail(self, category_id, brand_id):
        """
        热榜品牌详情
        :param category_id:品牌类别id，可以从品牌类别接口获取，一次即可
        :param brand_id:品牌id
        """
        return {
            'token': self.token,
            'category': category_id,
            'brand_id': brand_id
        }

    @request_mapping('/douyin/search/users')
    def search_users(self, keyword, cursor=0):
        """
        关键词搜索用户
        :param keyword:搜索关键词
        :param cursor:翻页游标，初始为0，根据返回的cursor值进行翻页
        """
        return {
            'token': self.token,
            'keyword': keyword,
            'cursor': cursor
        }

    @request_mapping('/douyin/search/videos')
    def search_videos(self, keyword, cursor=0):
        """
        关键词搜索视频
        :param keyword:搜索关键词
        :param cursor:翻页游标，初始为0，根据返回的cursor值进行翻页
        """
        return {
            'token': self.token,
            'keyword': keyword,
            'cursor': cursor
        }
