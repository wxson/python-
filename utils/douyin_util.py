import gzip
import re

import requests

from protobuf.douyin_pb2 import PushFrame, Response


# 根据url获取直播间信息
def fetch_live_room_info(url):
    res = requests.get(
        url=url,
        headers={
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36'
        },
        cookies={
            '__ac_nonce': '063abcffaoed8507d599'
        }
    )
    match_text = res.text
    match_text = match_text.replace("\\", "")
    script = match_text.replace("\\", "")
    pattern = r'"roomId":"(.*?)"'
    room_ids = re.findall(pattern, script)
    if len(room_ids) == 0:
        return
    room_id = room_ids[0]
    ttwid = res.cookies.get_dict()['ttwid']
    return room_id, ttwid


# 根据url获取直播间websocket连接
def fetch_live_room_wss_url(url):
    room_id, ttwid = fetch_live_room_info(url)
    # wss_url = f'wss://webcast5-ws-web-lf.douyin.com/webcast/im/push/v2/?app_name=douyin_web&version_code=180800&webcast_sdk_version=1.0.12&update_version_code=1.0.12&compress=gzip&device_platform=web&cookie_enabled=true&screen_width=1920&screen_height=1080&browser_language=zh-CN&browser_platform=Win32&browser_name=Mozilla&browser_version=5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36&browser_online=true&tz_name=Asia/Shanghai&cursor=t-1701322985497_r-1_d-1_u-1_h-7307126435105346572&internal_ext=internal_src:dim|wss_push_room_id:{room_id}|wss_push_did:7306691797249164810|dim_log_id:20231130134305D098722867DFC505B3E0|first_req_ms:1701322985404|fetch_time:1701322985497|seq:1|wss_info:0-1701322985497-0-0|wrds_kvs:WebcastInRoomBannerMessage-GrowthCommonBannerASubSyncKey-1701320426322145268_WebcastInRoomBannerMessage-GrowthCommonBannerBSubSyncKey-1701320426398077666_WebcastRoomRankMessage-1701322452354816378_WebcastRoomStatsMessage-1701322980200406875_LotteryInfoSyncData-1701322019023492961&host=https://live.douyin.com&aid=6383&live_id=1&did_rule=3&endpoint=live_pc&support_wrds=1&user_unique_id=7306691797249164810&im_path=/webcast/im/fetch/&identity=audience&need_persist_msg_count=15&room_id={room_id}&heartbeatDuration=0&signature=WBoflHwAPnamId0c'
    # wss_url = f'wss://webcast5-ws-web-lf.douyin.com/webcast/im/push/v2/?app_name=douyin_web&version_code=180800&webcast_sdk_version=1.0.12&update_version_code=1.0.12&compress=gzip&device_platform=web&cookie_enabled=true&screen_width=1920&screen_height=1080&browser_language=zh-CN&browser_platform=Win32&browser_name=Mozilla&browser_version=5.0%20(Windows%20NT%2010.0;%20Win64;%20x64)%20AppleWebKit/537.36%20(KHTML,%20like%20Gecko)%20Chrome/119.0.0.0%20Safari/537.36&browser_online=true&tz_name=Asia/Shanghai&cursor=t-1701334639545_r-1_d-1_u-1_h-1&internal_ext=internal_src:dim|wss_push_room_id:{room_id}|wss_push_did:7306691797249164810|dim_log_id:202311301657194B72D6D14C0662032141|first_req_ms:1701334639493|fetch_time:1701334639545|seq:1|wss_info:0-1701334639545-0-0|wrds_kvs:WebcastInRoomBannerMessage-GrowthCommonBannerBSubSyncKey-1701317013121953700_WebcastRoomRankMessage-1701334444583040109_WebcastRoomStreamAdaptationMessage-1701334633962701102_WebcastRoomStatsMessage-1701334636422936740&host=https://live.douyin.com&aid=6383&live_id=1&did_rule=3&endpoint=live_pc&support_wrds=1&user_unique_id=7306691797249164810&im_path=/webcast/im/fetch/&identity=audience&need_persist_msg_count=15&room_id={room_id}&heartbeatDuration=0&signature=Wd1GlEPcGdgvt0Sg'
    # wss_url = f'wss://webcast5-ws-web-hl.douyin.com/webcast/im/push/v2/?app_name=douyin_web&version_code=180800&webcast_sdk_version=1.0.12&update_version_code=1.0.12&compress=gzip&device_platform=web&cookie_enabled=true&screen_width=1920&screen_height=1080&browser_language=zh-CN&browser_platform=Win32&browser_name=Mozilla&browser_version=5.0%20(Windows%20NT%2010.0;%20Win64;%20x64)%20AppleWebKit/537.36%20(KHTML,%20like%20Gecko)%20Chrome/119.0.0.0%20Safari/537.36&browser_online=true&tz_name=Asia/Shanghai&cursor=t-1701393814196_r-1_d-1_u-1_fh-7307429962804499507&internal_ext=internal_src:dim|wss_push_room_id:{room_id}|wss_push_did:7306691797249164810|dim_log_id:20231201092334DCBFC78CB94AB298B67E|first_req_ms:1701393814106|fetch_time:1701393814196|seq:1|wss_info:0-1701393814197-0-0|wrds_kvs:WebcastRoomStatsMessage-1701393813861541304_WebcastRoomStreamAdaptationMessage-1701393810164658479_WebcastInRoomBannerMessage-GrowthCommonBannerBSubSyncKey-1701390122430825363_WebcastRoomRankMessage-1701393645864474492&host=https://live.douyin.com&aid=6383&live_id=1&did_rule=3&endpoint=live_pc&support_wrds=1&user_unique_id=7306691797249164810&im_path=/webcast/im/fetch/&identity=audience&need_persist_msg_count=15&room_id={room_id}&heartbeatDuration=0&signature=RgTmcCrJHYwssA3+'
    wss_url = f'wss://webcast5-ws-web-hl.douyin.com/webcast/im/push/v2/?app_name=douyin_web&version_code=180800&webcast_sdk_version=1.0.12&update_version_code=1.0.12&compress=gzip&device_platform=web&cookie_enabled=true&screen_width=1920&screen_height=1080&browser_language=zh-CN&browser_platform=Win32&browser_name=Mozilla&browser_version=5.0%20(Windows%20NT%2010.0;%20Win64;%20x64)%20AppleWebKit/537.36%20(KHTML,%20like%20Gecko)%20Chrome/119.0.0.0%20Safari/537.36&browser_online=true&tz_name=Asia/Shanghai&cursor=t-1701393814196_r-1_d-1_u-1_fh-7307429962804499507&internal_ext=internal_src:dim|wss_push_room_id:{room_id}|wss_push_did:7306691797249164810|dim_log_id:20231201092334DCBFC78CB94AB298B67E|first_req_ms:1701393814106|fetch_time:1701393814196|seq:1|wss_info:0-1701393814197-0-0|wrds_kvs:WebcastRoomStatsMessage-1701393813861541304_WebcastRoomStreamAdaptationMessage-1701393810164658479_WebcastInRoomBannerMessage-GrowthCommonBannerBSubSyncKey-1701390122430825363_WebcastRoomRankMessage-1701393645864474492&host=https://live.douyin.com&aid=6383&live_id=1&did_rule=3&endpoint=live_pc&support_wrds=1&user_unique_id=7306691797249164810&im_path=/webcast/im/fetch/&identity=audience&need_persist_msg_count=15&room_id={room_id}&heartbeatDuration=0&signature=RgTmcCrJHYwssA3+'
    return wss_url, ttwid


# 解析websocket 推送信息
def parse_response(content):
    # WebcastChatMessage
    # hexStr = "08b70a1082a89abef0cc8fdf5218b84520082a150a0d636f6d70726573735f747970651204677a69702ac1020a0f696d2d696e7465726e616c5f65787412ad02696e7465726e616c5f7372633a707573687365727665727c66697273745f7265715f6d733a313730313235303433303036397c7773735f6d73675f747970653a727c777264735f6b76733a4c6f7474657279496e666f53796e63446174612d313730313235313031333730373732353031375f5072657669657750726f6d6f74696f6e53796e63446174612d313730313235303434393537323338383337345f57656263617374526f6f6d52616e6b4d6573736167652d313730313235303938393730383130353932355f57656263617374526f6f6d53746174734d6573736167652d313730313235313031333634323634373432325f57656263617374526f6f6d53747265616d41646170746174696f6e4d6573736167652d313730313235313030383039303735323635312a400a09696d2d637572736f721233742d313730313235313031343637325f722d373330363831373436373431363930313139375f642d315f752d315f7264632d322a170a06696d2d6e6f77120d313730313235313031343637322a190a0e696d2d6c6976655f637572736f721207642d315f752d31320270623a036d736742d04c1f8b08000000000000ffec7d097c5bf59960fe4f8a2cbf04a2bece745d4f0b1e85dd66b251fceec3fbdbdd48b2e43bbecf35154fd2932c5b9775f80ae926e1a809214981a61012c8181a4208e0982b11210166e94e69292cf4003a2d34b564073a8566cab4ccb4bbfbd3932d1f916d3d1d2494177e3ff2f28eef7beffbbefff7ff6ec17fbe0e2e6e17ac363e18aaf236f97c1e03eff50a813a2118e49d02f2e3eb606eb91b347b8eddb223f2c7179f148ace1dd8fdbfde9838f7a450726be4ed375fc45080dcba7e9bd6e2f7055d2197cfab2dd3e2da4d5a4b68d82f68cbb4847693d615123c16975d5ba6c570822168ed266dd8ebea0f0b963e61585ba61d74057b6a5dc1d0ecad763ec46bcbb4dbbab52e7bb7b62cf1d0a66e6dc815720bdddab26e6df4dc4db19bcf45eff876b77653b7d6e5e19df1f3dbbab5e180dbe2760543dddab2ffd1aded0985fc65a5a57e423798f8b4cd765f78d8e5f5bb6c9b6d3e4fa9cbe32c9db9528a6324815356da4a62148d0a2c4e92b84d601c561ca54894a437fbbdce6f84fcee019dcfdabb7906e5a6391c18f62920a1f385e3fa4d71dab944e24a0124be1d3fe0b4d87c6e5f407c7cbdd164a24c866eedf6f88b0b2e674f9c1b0cbea95b3be8b2877abab56538c9c61fb3c5e5451494389737756b1d01de23cc9e883f200c8502bc08755b77b7280eddf17f75772765267ebc29fe3f3fef145a03eee40d719205cb4a4bdd8e599ae99c015dd0170ed8049bddbbd93a1c129c82adcf2712d067ed2d8d9fd139c301fbcc5d3a672049548fcfeb2beda14ae3684501b358c5f56149f0c1e2b79586048fdfcd8784d2f89b044b5d5ebb30b4b927e471275f31e0f385aa96f984a02de0f2879a03b6cbf311a50121f1cccc1778789777334f515696dedc1b8cbfcef66eed76eda6b9f52aaed1041b671826829e85ca87f8c4aaf4fa062d219747643383623885a11881a2685ce88242c09258e6284da234c7701c1dbfe0743942890b244d6cead6da7c616f68464ee228075ca1e1c4751d368b789e28cdbc43f253e30a61dbcc6d2eafc377c9492fef49e896a987ce4cddf64842c388e2bd18b4f8ef60880f8583ddda32f1ddc28180e00d59fc019f332004e3a7a9b8bee2034e61c1596ed3fc579895ee6df3bf9660702ef9f93691b04beab574d4016b273181a5395cb0113c4d6104efc0714ea0088aa0588623565239e9e8ce6c71a4a53b3342924aafa50328955ed3138c91318a576c3e6f4810c5312edd49c97978e7642472e1c1fb638722dddaeddb67d9384fa1d95dbcc7e7b55b66a579661588b7f16e171f4c0d284f424a622c9d524ef1f89f956535b132d312d574c408a3481bc791b4ddca10362bcfb114cef1569a66385ca00896ca8918658b249d3597118e54a29a0ea054a24ae1244a30cb886a747c5ff4dc4dd17337a590532c859c62970ae942107992500c4d299f34bdb27052349153e9a4080aa76da49560ec0cc1d8059277603c8fe31c4959690761cd8974668b241de9cc08472ae94c07502ae934198c26a36939457ae881a9d193537b1f9dfad678ba8a541489c57a74319c4ba474f2ccc1e8b7ee59424ac9b4a534a59062e8f6eb454bc4d6e70cf8c25e7b30f199bcd7d6e30bcc5a49616f5008652b9b3320c5971569201ea54064c1511cb760b805c77222aff9409c8e0ce70c6f2ab9ce14782a59379bcdd8ac33b4108257185a96ef39a37f1c9104f2e74ade24a2cd15d7d3419b29d353c04ee9001b0d263d31a3b82e5520aea0c51f7079f8c070b7b62c14080b9b56dc3b577278b65fbf7dbb767b11b4f136901f977186007175cdbbe2473dd4acd7b8c8ef0df1c13ed1eddd028a925123f81fb6c3c84c78a9c2e508cdc69dc6b6c33f5e9fea8ae6be630fffe39fde5f1870facde944c0a9ac217a76c764e4f6d8e8fee87df747cfddfad10377ec7de9f44b13e7778ebf743a3abe2f76ffa1e863fb274fdd1ebd63949ada753a7a6647eccec7ca2eecd839f5dcbd93a79e8bddf958093679ea78d284317c4f0bcf4a82851f143c4242068282d76ef1245ec9324020ba6d6859dc63dd5e7261c7cee83723dbb0b26028e0f23ab76fc3cb44e1da5eb28d983d577c355cb8dee170f03601a34af62bb48f5da35e83244eb2368171384af62b8e83ef5c03df7d8dfa8f6fc426f6288aa98c3e6d0282310663718c2028ee22c4d4359383b5bd7a835eafd7eb5add9ebe6a5ba7a3b72348d772a126d2cad575b9c344b37ea4bed6dece7a6a7482153779cd75ef2b9e82e026298a204933bbc7e5b55879bb5348b1e2e066494a2d4da04d5254477a30916b57b8bf4853a2411586abb56b63a3e7a61efffbe8edb74f3d7ae47dc52f20b8530addbcc2a0450c7d3803bc5db0b88501c16d19c02c0497ea4b3ba57ca934d05d9238230936f29fd27bac4853528202c3df147d4dfb1fa6ef7870faf86d538fdd36157998e0a6220fcf123802c16d52081c0c5b83b680cb2a58e2c887053ee01eb61043a948d02685ba12e0b64b226dfa8091f5693c83fe17835aab9aa5de4f21b845d2db38786fd0e60e5b6779455bb05481e3b9859d0e4f24034d87216902454a567a002d30a0706152c5220571dbcd6c361769b445c9b35313b74d9e3a1cbd6f6c96b23f9a47596972b902115a33949e15c0b66426ec2b10f76f577c02c50dd72d41ddb5334ed80c45ff6d9e2a9526abf145206a6a0b465b863cfe54dfdf9191c04a822c496ad3808cfcc7b49e4209e9f2dba48295ab56fd37a46be6eff715bb15b02d331189ab1f4bd0c3bbddf379bf14b56c992d1a6948ec19ae21495810542a00944c772d8c2a603e0b42595dce74c864cd864c69e2e0b310aaf450209ba53d8e52868d4b7001899e7e2a1a393a9f17fb95604c999971fe8ab222618f3778fdfee6a6663fd667e63bca6b750e77cd80e0abb504f5a626b2df417672151653b8b6ca5adf524ef71b43c316aadcd2cff30d549fbd55c0ab7c17951fac86cf436a1522db9b79b537e1ff07a9d722f24e74f976220452add57e550d90453e745761d269d77e02a9d7bd02fe05823f8260477e124d0121e81a11ca48aa8c14cfcee1c96d1ee8123cce3c25b5162342364981b1b160bdd16434990cda2fa5600d348475dc7311bc00a6d59ad7142560034041594c3f13dad07cf8f4c34faa320c709480eaef2be0edb3c12d3fb1881862cca61443d1210c4513ffd2f1037c880f94867c419dcdab73e95016232cbe417dcfd6bade3a93d9a03756f518b91a7a64ab3e20f478f50ebdbec9a9ef0c0e57556deef50bceffee08f83cff9540698666308220e7a1a72f07fa6f24d163d865c08f54e50cfe7120c7993289331d07f2be9fd77dff38902325f989944c802fa8ef59abd9b91a57d02456a6c4281a8d805dabd1af1d042fc8429da5508f8153d05cbc31ad0c9e98e4f0f3c33360f1210b412df1991dd252921220b74bcafea50f18b92e9d878ad696ac45c14be05d047ef6aa7902add11401ede1abe00fe39ed6fb90ec82e7cb054f18fde8faae99bfe1872135848cc92a7845150c3f0aa915c85139f89c56f019fe01a45622df93ddf98cdcf9c5ae39fc0748bd1ab908c981e27c078a67f4e33533faf11a646e8f42dfddf3c22d27f6542063abd50039bc7af1f675d3eaa4d0e74f323f8de574a508fdecd6f499d944f2b389aebc35a510d25d905a03b44ae56ad59a1c55aa8c2b1472b18a5cac72450611e46215b958e54a0cc1c8c52a72b1ca95625ec9c52a9f151f442e56b912226572b18a6c6fcac52a57ea4e8440aab51d2fef3bf4a86ae49335f04f20f8fafcb53dfbbdce39f0b96f468e83ff7a1e1baa33293931eb4d74b9115997e8b949d6ff6c784dc18206d0016e003d6017982b0c1a036a5841e1a8e6ae823150004334ad395030060a61254660a4e60faae340e6518e79546e349366fd7b008c43d3ead7a18fd79e87e618721e52c579271e440f1c8a9d188b1f9cbb29bafbd8794815bbf981e9f1b1c4416ce723f183bb9f88edd9197feacc5db1bd7be267f644269f3f721e524d9fbd6ffaf6a3f13327c6a6cfed3d0fa9a6464f8a900b1390279f3f32a6b82b1f6d70ee61ef5069401810bce199f6303fef15dcb37d7089f6b744a35ce96c1b70b23b6e736f705ca18c28c0aa9714500978457115bc0a295c6f34521c65a4e97714b01a4654d1c7f74c9dddfb8ee26ab50181e9a983375f78f0fee9a79f8d9f380390c2e9a33b63bb4fc6769f7c47f105f5a812593b792a12fffcc8ddb17d4fc5cf4d15206b2fdcf9c0d4e8c9c9c8dec9e78fc41f1c8391c2725f3876cf1393cf1f7943f91634273bb997fc41c1ea9f839f7bd117e15bf228fb71049285df841a5983711428ef0411087e129af387d3a1707cf377f356c16d0908ceb09b0f586c3d7c68d9e04f5a1f9e3edc56290c4b1b2ca25df9918d05eb8d463da1274aaed9a2380878f8ba642c534cdc8702fc70b20133e49be9c745e2ea641bbabd580317ae3710890dbb64bf620bd05eab06c82567e7158d1e077f2a407e0ecdc9503a1cb2f2822060b860c3ac046573e03ce3c0791cb573186ac5083b998aa6162934cd04c10d928421030c73cb209d87e3cbc060c28ca60d002fdc58b09ee5f40463acbe0f82eba5504264b8950f0a16f11d52f56fcf014c8777e9006c9044ca3420225f59eee68d05eb193d8d524407b8e1f575bbc01ab8505c0706939e1805af29c68054252d8dbbd2957406f0a52969e908244b67622cdd34001f01300afd6ee2ed375fc40e425f993f762c399c0c670882c4b8080415ad2e4ab6a2c3efaae02fcdeb556ff38584d94ef6880a2696baa8397ae05bdf3bfcf2c266f629717aa20614ed3ef0c83ffdf2b72f3c2968ff2f243a22d1a307a626ce6afeb4ae38ff566a9ecdc83c5bc19237eac45ca492d7141be7760414b0c0a0c45192d44e41f3d3e8cae2972169d10516c5791ce3059c73700e5ea078ab40d01c61173807cb9056fb42da488a8948032d2d70210936b221ddc744cfaddc68464b1e021b55b1dd072e3cf0a4486c406e988e3bcba8e832b3a028b93ee0ef3627a741d4bafa92abebe66678d7c6545734df3d70e68f3f5b38981405861ffe1dfcd7019fcf6371bbfa048bcde7f1f8bc9690301442be989ce03037bb61764e83f8a764bf42fbf106f59ae3e0c30df06f36a8fff9fbaffff6dfeff818682e7ce7771f09c5eb62f73e7e61c7c1a983374f46225fafff7a09a87e5101df987d69be0d45318b60a5389aa750de6aa348074f718283b75b299ca409dc4eb25ceac6806d59f725e40479a63d199923472a72043d8785f5290d8cdcc4285382ce518c32a515b3728c125b10a3bc76518c125b58589f6dfe15cd47fe3525d0acf3cfa9a02e9bd54597cdeac2cb15d6ff95fa0ea3666c4311c095144691654a966239b1b6feda1cd6d67f6ee53a37b5f5a88548e9c5655f5bbf14e4ac6beb9700bc7c6dfdec43b3b5f52fc0f0c2e24438c7c58968fe8a1397049d75ce6229c8cbe72cd0bc1727fec56bd85415b48757ab0172cf6a5835b5f7bee9bd7b356b8a8076c7ea1cd68c6379cbaaad0c3953095d0af2f2128ae55d4253ee15d94a684aa0594b68caad673909151f4066c4103dfbfa7b3ffccdef5f54ed82564d406b7086205906a3291cbb08d5ceaf9a353777b858ff56a771eb5065e5f0403551855adb9d3a62a8a7cd1c669aab389cc5743d959d75b87f3060e11ca19e709b8b1a09fa6adaa9fa069f532ca595cddfbc9abf6251a3ac9cf360fe8a2578b211918111b164e1c332d45eacd6c542a3c52191b9122243a0a29fa0833d5693ab7668a0b649d7686fac1ca2f5eeeac1fe2e96605a7ad0269ba52b5c1e1ea819ea0cd4102ecb60791b4e946fe51a38772d99871222593fa5d24fc9122279255da69524cebbf9921a742193a7228911b553bb4e4f3f7dff64e4d606300a125355e0a2b33f28dd284725e5a8a4acf6e4a8e4156c96c95149392a2947253f5f66901c9594a3927254528e4aca51c92bc74c90a3927254f2336544c85149593fc951c92b652521906aad01d200abb2e49a2d5051b2d812deb506feab996acc3ac1639dfb25f97761f87665ea6b9a8903632ffdf4925acd5715f05fbb5d0382452cd814bc21216009f9f86008f972b2563376f8bb93915b17556c5ad9b98acd51857a0db2162e58cf1a4d8cd8f5711cfc1e827f07a9cf3cb27ff79f7f3fa9d47cfcccd4bfae2d5645cf3d3a797a7ff5303c987588d0c2a32c8a13828de72882741024873202ebe07882c0059a20c894e1c109a0513f5aa039aac4151485962938828b80552f0118566b55b052bd0a599530aefac2bccb2de03486138b8cabcead06bd3184d676355675b5b975d5c3dc10515e31d0a0b3bb6b3b2ab101f790bfdedbd236323052c37778fbb100d6eec75c7ca8c75161eae12cfcb84221eac81962cca946bc8f37d84d1574dfd686a69616b4dedd5439543384b638fbdda4beb9a97d6460a49c226b469a2c74fd484d5339dfbfb5a7827286ecf52354a5a3c17751b9aa1234808efdff088d02c50b605a8dc82cf8d45950f44a6b03b813c80beb2f8aab0781b204df021525b528fcbbaf2ea1847ff455781c5e4209ef3970f8ee9f5ca2842f16e640561e2bbc5456ee2d840f14aa275f7de8e8af80e64f6fbe0f17aba64fdefae1f3f7974028a8be111ec92647c50f8474288a511606156882e33996a36c1c8bda70967130a803a76c3421d0189d525e8e83ff99234328e59ca1a481a35968e06074d2c0990088fac2d59af7afc69518cbb165f1ff3311f07d806a0e026bfe5f6e0c58b28e216394054b35e06236d4ba78f5a9719c897f26be68f85f8dbec7cef17dcd3d5d1daebe766f9d097386cb5dee469fa7aac1ddd5361468eaeb23bbac94bd4a2fc6062e37ef12eb3c21cbc9755e8f6dc5fa0d9dac99f7e38e6a4b39515dee0be9fadd9d9dad1e5387bdafb79d6c6b65b15a574b55afb98af2773aadfaa0b1ad25a80f768c54596b5b2f2aa7a1a46f91c70fcc8ddfb202e86cfc96d4a3bb56f42d128fa5c13e04a8165b2ab29e92f594aca7643d75a5e9a9a273a2392f9b68b2ea93559facfa3e4faa6fd6e74d3aadf02778ca06f1b770f8832fa76c107fe6c0f8e39736883ffde5ac1ac47f59a45e731cbc5504ffa448fdc2b7c6cf5df8e17b4acd83cf4cff7c1c2afe62ecd0e864e4f18f1ed8736f747cdff4df1f8b1e3d5d0255ff9302de05725490e923f5fac6c69e2a93de395c53e1dbda3ce030ea4386c1ca6a0a2dd7eb832346b3a037a5ae8cdc0972531a99a377c8aa36348b7740ea728ae338784b629a62a9e5c1649fa690045a529a420ae4b934c5b24fcd2882e2a202ed97e62b0266de16fc05f5db0acdab6a5c89612856a620192202fe5589161c046764aa6741f531300e491bfe95c2baa02c2967a74a1a81963e586923d0d2863b37ab6ce94752984baf801fac86df92384d8c2529c6ca59398ea5688a64ac1866a30486b75a5981e6189b35d5674b1bf695090649f3ca32403037ab279d878b0e422507a16299b4f922adf68b4c5c99722c47b3148971188a924c223dc2620c4773044a10dca2f488d7ee1ba9a56bfb0d68bf97614dbe7667b8366040ab074d0ec1cb0c54989bddfae616175d55d3ec6e1ee27d838100d95449094deef26a5d53b94ef40ae48d325f1ba5e8efa4323f93cecf56739360243ab9a6b0810bfbbd559ee156b2c95e4151835455d7d6801e23ac86e66666a8add540d4365a056f0d151ce861591bd1cfd40df08dce8bca5f43f02fe2ce8fccc67cb11101aa953bc156173df883d28db2fb21bb1fb2fb21bb1f9f4daacbee87ec7e5cc936b2ec7ec8ee87acb265f7e3f3c54604a80c4a35108bbef12d5051328102bfd89832f772a411deff7729732f070f4cfcfda5b997773664957bb9491ccefbe7afc1fff635f593ffe7c807b18f376bdefaf6b3bbd714174eefd8193b7cecc3337b4a40f53f43b0231357c3e30bf22e9bce2d3879dbb0856038cc42a10c4a131cc5b0a9fd0967467e5506881c99f82dd2f120b87440e2ac8a1c654353368ee72665b93ce8ac12ad29bbd257ce86920bb2a1572fca8692f2ac8a4f615605a2feb542b31f14015c819164998264097152c5d5e2a40a59aab3926a715245d60325307489cfccba386645c0193aa64b015e765245f2a1596fefe5252655c8b315d2d408f24c8f5ccef44835a9626cb51a2097699c4adee89347a6663b4e252f0be9b3a348321aa7228616d6da87dd0343146e1d18f40517d536d6771a7cfdb56dad0e535d13d1d75b6f0c36b1be5e9c6ed4e1de5a7e90ae68ea6ced6aec6f31f456cd8ea690ed82fc59bbf2680a7934c595b617e66c34c55c9c62ae2a59376868efb05b43cd6c6b8371c4ded01becece79cbd9526d3565f95adc7d954e1eead6ed1f561c35e7f0f4a3b2a2a3ced6d15fd3dfe4e26146e6f4f0ca590e7255c66f6e6ba2e5cde1b52ec0de98dca55890512728c508e117e7e56861c239463849f49a9966384f98811ca912f799aed65d0afd262847254ebca09647f8ea2a9728cf0b36017c831423946786568b0bf9818a11ca1cabf669203b1977b0d2d1a5c9b2c44848fac83bf3c53a9d8e4f3795a8342a059e89f2d65fce3d530bdcc75cd33bb7ef1d6a209b625bf7df6ed375fc490d794c82b4af5e4a1f31f3cbde7c3d5c585e76f7e32367e2ab6f3ceea88224723747896b4db18cac6101c6777e0940de7092b25d08295a0711e5d2220389c45b35396a8e73e1bffb47123a69cc09e00ab16cf104dccf83cae5c3557d65ceeecf3f95b5b2abb86cc7443304c37d60ce1542bd7400d0fb116aac3c635facd4c4f4b5325c384d09e567c4457d56f221a888a7023da610ff68d6dd110044a101447731cc31238cd1601e40d25f2aa527de8a9f70e4f7e3c5d507cd58507f74eddfdc03762e34f4d3ffd6cf569c53cce4a6fa54b528060090745db3802c7ed988033569ea25856b093764cb032a8358f429519eadc085546b8d314aa9560a727548e2a74080ff5d7d875b51de19ee146739da36b40602ac3e1b666d350abadde3518ecac601a705dc8585f53adef309a07abcacde10ab6c213e606f4635b342489e2284750284d12148de14510f2a112795fa9fece4f5ef8f1af3ffe6941b16a6adf91e893e3d5bf50e4ae3313ed339a42945eef2d77f53bf5fa213d66b40a217dad7e6b73671565e51a038e803e356fe7b5a866c0dcdcbf44967db299bf44fafda169e1484be2ea3d3ec370bd5fcf3735b5d85b6ada9d284b3021acaeafad8ea9af15dcf5c3bec1962ea69e69458d81aa4a8af7e85b87598c1aa25c2d6e6f93878c4b1c81e31cce521845e304c550458aa2375ad95dbffca24185a193a7bef99fab5763f1bf9a54d8e6f8415701816f26264f7db3e8995def24b656f8ec52638deffb2afcc052638d8f1ef8d6f4a5b3e57f958b99798752cccc1b2d846f2954ffeccefdef3dfceaa44233f9ab9fbffe16285645ef7b7e7ac7ce6ad7bc749f1439969e863b0e6ecc4d1f0c9ec25e4bf68a400b7b45f079bdb16bd4a8468103a20c22d9087819a0d0417043be5f690c5c9f7583276649e5042c35126f0dc562549ce018462fea4aaba75afd6c43136e132afd346ea03c9db43950ed0a5539fbc3cd7e67afe0088c540cbbeb9de84853b8c2c3b43573756857f340454b391b6aeca4c450d165e5e2ccc872517693daa04e1768c6da6bda9b5b6b8398c3ed1834d3ede6b0adbfbe960cd2366339a6ef09e183437c3b5ddfc677f5350b46d6c0fa4d6dbca0b7b4da7a0383b9efd54af57539ead54a093a27bd5aa920afdcab852fe8d55a92738ba718ffcc88c86a49564bb25a92d5d265564b454f88438b65034cd674b2a69335dd5fb0a69b9d519cf440e16721583b1b43e6bd7d6e573054e90b074cde5080f7da927df3b742b03e9d1b3513c77ef4d17717459d6f3bf3f69b2f6228405e00b011be1646e0aba7ee3d1b3d13993a7182c5a2fbef2801c5620cfd3bcfc48e1e824be02fc0575df8e61dd1c8ad53274e90e275cd823bd6c37f1b07321989c4c6ef8e03611337298a0b13e762470f21345c04af81e79e9a0fa078c19505c091af24ae26012d805a3471ecb5c4f7c1ef52c93902152e476896526729f89335a9ae688e1e1b1ddffb8785a4f9debe438faa5050766d97e075965dd8b173eab97b1365c225f8e4a9e3d1871e8e7efba10bb7dc6938bc069e9dbb63492828a7cb11b20405afdde24920b00c10882eb9535dd8b133facdc8dc4eb50d2f13c5697bc93662f1bc02de2660547cf7bab940bd06499c646d02236e69c7c16f55f0072af5fd53e73fb85f51ac8cbfe90404e32887d21889a3c4a2ca83c1813e5d5bcd40a0a5ad8e7134940fd803acde5d2978fa2adc1d1dd44043a72d840e30d5c3c35da438e124376b72f99f86cf46912c0f399bd59e32b3b7e26a2717ac76e5c2d54e2ed4d322b3e6c2b4ee619b9f626b47065b7421da3dc418867484d14657fa197b07d764446b82c3aec1a11a1d8dda7b2c95a4d94dfacaab282bd5ded7e71a7192a6055a5ae65b5ef8860095f6ab6a802c5a9a5d85495da0fd0452af7b05fc0b047f34d31390b665839356c2666369822171879db4da08bb803a28c2cedb48929d37aa2520045d2342194995919458d0e59456f09a392287a432d58cf1cc0d824a07c6c682f5144ea204a3fd520ad6404378c73d17c10be05e44f3c6ba12b00142a1b22790198da979eedf3f9a2c48e8cdea9714f08d398ad8b3bc80521c69a3719425adac95a37992c7099bc03304c33bf0d409836db9499c6486fcc61c654c32c28e54e408ba38c052d67e79d17e13e02af5bd40538003a64c815189e1954a7178a54cf18c29be7078654e7de0eca74c2e0137db599b4b906db9e195b3345bc2adcf89c93b3bd74f9666d9ea95f9b63039d4f162dc1b1e797a0dfc1308be3e3f866dfcd5e366e6d7f364cfcec2bf3e3f66ec0c78c9d62bcbe909c688fcf5851d3b2723b74e9eda113bfc44d2a1d8f0c63a1634800e7003d4037681394f630c14c010c7694e7ef13890599263965038c110cc7b008c43d3ead7a18fd79e8754d1d313b1c34f9c870aa3a727124c3a0f154e461e8a1dba3dbaeff6f3906a6a6c7ce6860387676f5045cfdd327dd3a1f8c17d6353cfdd35a6b82b5915e476cc7eabce19d0057de1804db0d9bd9badc321c129d8fa7ce287fbacbda5f1333a6738609fb94be70c2489e1f1797da5ee61ef5069401810bce199e0939ff70a6e4b8286a57ede29044badbcd72b044afd019f33200483a521c1e377f32161736f705c01451460d54b0aa804bca2b80a5e8514ae371a298e32d2f43b0a580d23aae8e37ba6ceee7d4771b5da80c0f4d4c19b2f3c78fff4d3cfc64f9c0148e1f4d19db1dd2763bb4fbea3f8827a5489ac9d3c15991a3d198ddc1ddbf754fcdc5401b2f6c29d0f4c8d9e9c8cec9d7cfe48fcc13118292cf78563f73c31f9fc9137946f417372967b311e14acfeb919c679906311c1d7f327c871f89225d96c3619ccec9de071087e18829ba49037be65b879abe016abab07f990ad27d506d624e58bd384d92c894de90145ae5de1fe8d05eb0d6cfcbf926bb6280e021ebe6e61503714e08793f1dc90cfc27b6d3dbe00a2bab063e736747bb1062e5c6f201225e625fb155b80f65a35402e393b2f58741cfca900f939246db0b695170401c3051b6625289b03e71907cee3a89dc3502b46d853da1892868f678240daf0f10c30ccc97d3a0f2735f80680176e2c585fce9a0c4653f57d105c2f851222c3ad7c50b088ef80a5faf206495f9e0ec47a29d2900640e42bcbddbcb160bd8936ebcb8d1de086d7d7ed026be038c1a838f1f4a3e08d756360fef0fa3cb077a1d6ccbd804ad7cad2e14b964e93c184194dd3007c04c028f4d491b7df7c113b08fd0d866104c5e21cce7224c6a0184e612886a114456011082a5a5d944c53c1df275366b88e91f0236b5366b86e3b76e6991796c8707d2d76ea96d8d3b7c49ede193dfdd4c24c173679ea78747c5ff4dc4dd17337195efe54325d275266ba0e14c07715a847f7eddffdc01de7a0e2b5f3df79025a439128c9e2344bb3cca2bcbea7baa68faae5fa5de1be40352af4a075745755906bc21b1afd687f7d7b65457d8fb97f6bfb56677080a932daed0d430ef780c9c00ed436bb8cc15c66c252fe16484e7ccbe52167e35ba6fc9d91157d4b6e816f59b8d0b7e416c60416b0722e36d0ce907e3bddefd3f55afd9583ad56c15dd7e1232de67acad0d218ec74b8306bcf50bf2ee0ee6a1b3237863987b9ab66c020f8f1d660c50019d0e7213620f36f11ff96ce88cdea8ccc33621845da388ea4ed5686b059798ea5708eb7d234c3e10245b054ce32625920929411cb1ccfdc06930e8c8d05eb192367d0134b64c4b06446ec354509d8005050f60324a95935fbfee1d089ef83850ab604544f28e0a1ecd363169e43499cb2711446d84841e05812c705da86913ceb606952489d9d1aca3e3b9521e6c12c3ad4b2418c1873003987e93059f52d527d13e06ab54273ab1a576228819681443eac3087f9b0cf25c973920ffb747f752d4fbf3d97e18fb9cd94b9e6cd1cce6d96ec7329e3b245fc97cbbf44b6ec1fc46cd92762b64c5aee247d23f192dc496e8dea8c523392c14bb66c13b13c645d22b290743336bca698c99381449e6cf6c2182884951881919a3fa8c6801a565038aab9ab404c9fd1b4e64081983e937994531e19cda459bf207d36c790f3902ace3bf1207ae050ecc4989826bb29bafbd8794815bbf981e9f1b1c4416ce723f183bb9f88edd9197feacc5db1bd7be267f644269f3f721e524d9fbd6ffaf6a3f13327c6a6cfed3d0fa9a6464f8a900b1390279f3f72c566dc945746c64d5a6c579aec488fed66033ff7b2bf30b69ba6f053044530fa3b8132df69a4d90575491ae9339be5c97b262c8340bdd96036cfa491cc6693c16490d34869a79168f1cf28784d21a691f29de5f9f4d25457481ac96c36b326c36c1ae9c1b1441aa904235182243096a20986a259762e9544610445d1895c52322104bf3bd71365ece1e7baa5d6c078aa0b9a7dc722175ffdfda219291d3fbb28fe6002724fa1fae1ff7de4f88f7e7f56a1f9f6934fbfaf2e2e8c6f4b771c9c7ceedbd5c3b988a7510ecaee40ad0487931c89b2360ec50882b1da2994e7584120566eb0cdc67b20522c8ea45ba058e816100ba245efd669cede58047080960154ecb1552ce8b1cdcf5b7dfa3db62ade65f505838be20ea1e1e6e19a60b5b1a2970f863b1b7bcbdd1d4ea3c3d768b313765f2be136547123d51d36afbfa2516f0a57d659eb2b06aad92e83a5a5b3295c1d685adc5efbe9f33031503329cc49bfbca1a7abb9a37fc4dde5a8afa8b019dd2e775b39d9d0eb0dd47472ed44efa0c9d7146eb6540bde90dbac6f1868c6460c9d1dcd3e9bcbdfd5d2d5c1bb1a5377d8e6fa0373e396a7849c9b58422ad02bfbe5c402bf7c49e6214055fc8de8779f8fee3ff1e1993d9ffec1af77ecaa76c2fc5c0c525a0956407086dd7c60c9eaa68d05eb89f2f87f25f816302426f68b927a1a6142bae4264052146109e81802a5598c216986c4680ec5308eb1d8759825acc32c3d3acc12b0db7478c9bde7e27bca46bdcb1b12025ede6d09066c65fe70b02728040684c08d0e572018b204847e8b2758964081e2388952ec8d83c1a0c513745a42c37ea12cb0655d25f8ff000000ffff010000fffff1c01ead3e280100"
    # base64Bytes = base64.b64decode(result)
    # base64Text = base64Bytes.decode()
    # 1.将16进制字符串转换为原始字节
    # body_bytes = binascii.unhexlify(base64Text)
    # print("body_bytes：", body_bytes)
    # print("----------------------------------")

    # 2.根据PushFrame结构 + 原始自己，生成数据对象
    frame = PushFrame()
    frame.ParseFromString(content)
    # print("frame：", frame)
    # print("----------------------------------")

    # 3.对PushFrame的 payload 内进行gzip解压
    origin_bytes = gzip.decompress(frame.payload)
    # print("origin_bytes：", origin_bytes)
    # print("----------------------------------")

    # 4.根据Response+gzip解压数据，生成数据对象
    response = Response()
    response.ParseFromString(origin_bytes)
    # print("response：", response)
    # print("----------------------------------")
    return response, frame
