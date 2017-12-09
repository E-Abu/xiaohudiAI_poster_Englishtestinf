import requests
from send_email import send
from about_yesterday_title import save
from about_yesterday_title import look_yesterday_title

def whole():
    yesterday_title = look_yesterday_title()

    header = {'Accept' : 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
              'Accept-Encoding' : 'gzip, deflate',
              'Accept-Language' : 'zh-CN,zh;q=0.9,en;q=0.8',
              'Cache-Control' : 'max-age=0',
              'Cookie' : 'UM_distinctid=15ece42a3ef46e-010f7768739578-31637e01-13c680-15ece42a3f0d68; wsess=2us9sd6l863fmlrho850jh8643; __utmt=1; __utma=128484826.1645100576.1512818817.1512818817.1512818817.1; __utmb=128484826.3.10.1512818817; __utmc=128484826; __utmz=128484826.1512818817.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); _pk_id.2.2d7f=6e4dec36b5705149.1512818817.1.1512818870.1512818817.; _pk_ses.2.2d7f=*',
              'Host' : 'grs.zju.edu.cn',
              'Proxy-Connection' : 'keep-alive',
              'Upgrade-Insecure-Requests' : '1',
              'User-Agent' : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36'}
    r = requests.get('http://grs.zju.edu.cn/search.php?postflag=1&area=10001&kw_qbzc=机考', headers=header)
    r.encoding='utf-8'

    #print(r.text)

    sousuojieguo = r.text.find('搜索结果：共')
    title_start = r.text.find('title="' , sousuojieguo)
    title_end = r.text.find('">' , title_start)
    new_title = r.text[title_start+7:title_end]

    first_href =  r.text.find('href="' , sousuojieguo) #因为搜索结果后第一个href是'教学日常管理'的链接
    link_start = r.text.find('href="' , first_href+6)
    link_end = r.text.find('"' , link_start+6)
    new_link = 'http://grs.zju.edu.cn/'+r.text[link_start+6:link_end]

    #print(new_title)
    #print(new_link)


    if new_title == yesterday_title:
        print('no new information')
    else:
        yesterday_title = new_title
        save(yesterday_title)
        send(new_title , new_link)

