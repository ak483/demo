
# 引入requests和bs
import requests

# 使用headers是一种默认的习惯，默认你已经掌握啦~
# 发起请求，将响应的结果赋值给变量res。
url='https://www.zhihu.com/api/v4/members/yun-ban-gan-huo-jun/articles?'



params = {
    'include': 'data[*].comment_count,suggest_edit,is_normal,thumbnail_extra_info,thumbnail,can_comment,comment_permission,admin_closed_comment,content,voteup_count,created,updated,upvoted_followees,voting,review_info,is_labeled,label_info;data[*].vessay_info;data[*].author.badge[?(type=best_answerer)].topics;data[*].author.vip_info',
    'offset': '10',
    'limit': '10',
    'sort_by': 'created'
}
headers={

    'referer': 'https://www.zhihu.com/org/yun-ban-gan-huo-jun/posts',
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36",
    'cookie': 'SESSIONID=stRIOTk3vybuaHBXujzjNYquTgCzJgXoDfrnIppICD8; JOID=WlsVB0oEajFl4eyBfAiIJ64i8cthSCp_UYuf-hNpV3k0k5HOPT5vKwrj5IZ99L7OaDEsdAzWSTef2emIYVN5uKA=; osd=VF4WB0sKbzJl4OKEfwiJKash8cpvTSl_UIWa-RNoWXw3k5DAOD1vKgTm54Z8-rvNaDAicQ_WSDma2umJb1Z6uKE=; _zap=c3662ac6-08d8-4ab8-b282-8e57abe6d1eb; _xsrf=48732516-0f36-4862-9382-573fc62d1713; d_c0="AAAQx78RSBWPTq5hSCWL1W7Tcbhd_N14TZs=|1658393743"; _9755xjdesxxd_=32; YD00517437729195%3AWM_TID=D0eKvAHny0tBAQVAERKQSFa%2F%2F8E2uvFd; __snaker__id=KtU9HXtjgFgZ15DE; q_c1=13333e54a0a14967b00d187d175712cd|1659936904000|1659936904000; Hm_lvt_98beee57fd2ef70ccdd5ca52b9740c49=1661311366; BAIDU_SSP_lcr=https://www.baidu.com/link?url=ADJweAsk2itQPtQPsB_DeI2vgaMTSQlFJEDvDQj-iS_&wd=&eqid=aa88ef1d000038900000000663106076; tst=r; SESSIONID=GCJ1cxxkd6KUwtDBfyMSiFQQat8rYqMumUJHlBy0Mpe; JOID=UVsQA0P9eyU3eoNxLf6QPfi1kTI-uj5qDhL7D0OSTWhnBfw1aeYKOFdxhXIgCcRotUUR3B8vshgEV2qQziXgfEU=; osd=VV0dAk_5fSg2dod3IP-cOf64kD46vDNrAhb9AkKeSW5qBPAxb-sLNFN3iHMsDcJltEkV2hIuvhwCWmucyiPtfUk=; YD00517437729195%3AWM_NI=6SRCwRJvTpYHtsYBC%2F6UrfLUiE053%2BEjmGA7MQeLvo2E41jLv3UzPDAq0AKDBBhNiV2DCh%2F0zmzfjZf%2ByK4cYZ10VHX32Xnjb7RDLu4iNvfCa%2B4KlFfhrPLRA01YF%2F7naWE%3D; YD00517437729195%3AWM_NIKE=9ca17ae2e6ffcda170e2e6eed1f36096958dd6c77d90928fb6c45e968e9bb1c454acec839aca52ad97818dc12af0fea7c3b92af68d9ea4f65a8aaa9c91dc44b8ad97a3c225f68bbe87cf5fab9b00d6b22187b6a3a8c43d8f8fabadf565f29bfcd2e948b6ed9b9bd35083af00a2ca50829ea8afec5ef29c8d89ae3cbab3b687e952a6f5b7acb7699b86ffd1d5449cedfeb9ed62a2e99ea5cf7ff8b78297e549a3f5fcacef4ea6b8beb1cf5a83f0ffbac525f5b2afb8c837e2a3; gdxidpyhxdE=Rywyk7tXWmcqp4Z1xR%2FW0Xhbv%2F%2ByNHwaUZOc3L1j3w6CA1yf6MveEqN30ypSsOKTRJDIy%2FlUKQPpieeWb%5CCqrBoRn0NvknYi%2Bz%2Fq8kZYTWXNadvC0k9JbWpfiobWAEpHzDMdcWPHaygLpXsMzrIploxqIReSkbflx9f9mbH%2BNTQr1WPs%3A1663050732369; captcha_session_v2=2|1:0|10:1663050305|18:captcha_session_v2|88:Qml5QlFDMVltV1hvVzFnMGNJUnNqT0pkTk5vanpQSVJSWnZMcllNK1J0bktZZVJTTWViT1JFWER1ZmFydUlNaw==|b8edb58c3907914c804cbd43f5d63c90a9a2f2628c8011715bb000ea3db45e02; captcha_ticket_v2=2|1:0|10:1663050316|17:captcha_ticket_v2|704:eyJ2YWxpZGF0ZSI6IkNOMzFfQmVqQXJ6ajUuVzc1LXVZTS5QaENIR1hpa3NOaFQxZ2FSZzdvZm12WEt6N09ISnJNUExRV3BCRUlnbTRsWVF0Q3pOLWUuYnF5YTZ2SHkueUNHQWxkbVdHU1g3bFpoREJQV1UyeHlaVHFKRFdPTE9ZUEZZSjBJY2hFcXhBbmlJZUgtbi5NQmswMnpqN1FfTV9RWFBEUzQycXVTQ293Q3QyN2NwbWxOTVpxSk5mc3dzTUwyYjV1RE1lNHVEZ0pNZmZiVFoyOW1LOFNDbExINnZzbnBJd29US01rVElYOHVhUER0YUVwZHRKS3RaQ0w1TENxWFpvSUdWWjRia1pQLVBOUS1tZDRScTl1U2lZTGJyV0d0RGNodWh3RXhLTkRfRk92Q2N5UTJySjFkQmdRRnlYRVNSbjliOG9xU1VaLmdOYzdUMmRBSUQxZl9vWk5HcU9DS1hQdVVkcGRSYmhNWTBLNldUTzVINlhqaG9xYzktLVJjZ0U3ZFl3Z01NWW1FaVA4NmlVY3JOeVctSmV0OVZaRkpRbU8yTFRvRkh5OGlkRjdvX0U5VHRkWnoyUUFTNFgtRi5IWUZjNUhiN2dmVmNXVkZ3eEJRMGt2SXhNb2RTak1LdlhxOGZ6MlpwSmRfalBfczRxcXpiRmVyQTRyUFhEcnM3LWpjRi01OTFxMyJ9|5880a91e7535ac8990d670684e37059d7e3e6e754a353dd1989599bad6d69517; z_c0=2|1:0|10:1663050338|4:z_c0|92:Mi4xMGJqbEFnQUFBQUFBQUJESHZ4RklGU1lBQUFCZ0FsVk5ZWEFOWkFDbDVPcHpRZkVqYjZvQ0N1dm9Ob05PUDFPaGVn|3123c787ca4496644e15f18cdcc9eda074b57952373f0a92adad60428c8f8122; NOT_UNREGISTER_WAITING=1; Hm_lpvt_98beee57fd2ef70ccdd5ca52b9740c49=1663052421; KLBRSID=3d7feb8a094c905a519e532f6843365f|1663052612|1663033021'

         }

res = requests.get(url, headers=headers,params=params)
# 检查状态码
print(res)
print(res.status_code)