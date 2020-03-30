from  bs4 import BeautifulSoup
import urllib.request

doc = '''
<div class="headingNews qiehuan1_c" style="display: none;">      
      <div class="hdNews clearfix">
        <div class="on">
        <h5><a href="/n1/2020/0320/c1004-31641040.html" target="_blank">天津港开通海上丝绸之路新航线</a></h5>
        
        <em>　　<a href="/n1/2020/0320/c1004-31641040.html" target="_blank">本报天津3月19日电&nbsp;&nbsp;（记者朱虹）3月19日，“天津—胡志明”集装箱班轮新航线开通。这是天津港集团今年开发的首条“21世纪海上丝绸之路”新航线。</a></em></div>
        <h6><em class="gray"><img src="/img/MAIN/2016/10/116825/images/icon4.gif" width="24" height="21"><a href="/GB/index.html" target="_blank">财经</a>|<a href="/GB/70846/index.html" target="_blank">滚动</a></em>
        <span><a href="/n1/2020/0320/c1004-31641040.html#liuyan" target="_blank"><img src="/img/MAIN/2016/10/116825/images/icon2b.gif" class="ly"></a>
        <div class="bshare-custom fr"><div class="bsPromo bsPromo2"></div>
            <div class="bsPromo bsPromo2"></div>
            <a title="更多平台" class="bshare-more bshare-more-icon more-style-addthis"></a></div>
        </span></h6>
      </div>
<div class="hdNews clearfix">
        <div class="on">
        <h5><a href="/n1/2020/0320/c1004-31641039.html" target="_blank">重点工程复工加油干</a></h5>
        
        <em>　　<a href="/n1/2020/0320/c1004-31641039.html" target="_blank">项目部工人正在指挥架设T梁。孔祥文&nbsp;&nbsp;王智海摄影报道&nbsp;项目部工人正在进行T梁张拉作业。</a></em></div>
        <h6><em class="gray"><img src="/img/MAIN/2016/10/116825/images/icon4.gif" width="24" height="21"><a href="/GB/70846/index.html" target="_blank">滚动</a>|<a href="/GB/index.html" target="_blank">财经</a></em>
        <span><a href="/n1/2020/0320/c1004-31641039.html#liuyan" target="_blank"><img src="/img/MAIN/2016/10/116825/images/icon2b.gif" class="ly"></a>
        <div class="bshare-custom fr"><div class="bsPromo bsPromo2"></div>
            <div class="bsPromo bsPromo2"></div>
            <a title="更多平台" class="bshare-more bshare-more-icon more-style-addthis"></a></div>
        </span></h6>
      </div>
<div class="hdNews clearfix">
        <div class="on">
        <h5><a href="/n1/2020/0320/c1004-31641038.html" target="_blank">中国经济供需循环愈加畅通（锐财经·一手抓防疫  一手促发展(29)）</a></h5>
        
        <em>　　<a href="/n1/2020/0320/c1004-31641038.html" target="_blank">近来，河北省多地根据市场供需动态，在做好疫情防控的同时，积极协调当地畜禽养殖企业饲料供应，保障运输畅通，有序引导畜禽企业复工复产，保障肉、蛋、奶等产品市场供应。图为在河北省成安县一家农业科技有限公司，工人将鸡蛋装箱。</a></em></div>
        <h6><em class="gray"><img src="/img/MAIN/2016/10/116825/images/icon4.gif" width="24" height="21"><a href="/GB/index.html" target="_blank">财经</a>|<a href="/GB/70846/index.html" target="_blank">滚动</a></em>
        <span><a href="/n1/2020/0320/c1004-31641038.html#liuyan" target="_blank"><img src="/img/MAIN/2016/10/116825/images/icon2b.gif" class="ly"></a>
        <div class="bshare-custom fr"><div class="bsPromo bsPromo2"></div>
            <div class="bsPromo bsPromo2"></div>
            <a title="更多平台" class="bshare-more bshare-more-icon more-style-addthis"></a></div>
        </span></h6>
      </div>
<div class="hdNews clearfix">
        <div class="on">
        <h5><a href="/n1/2020/0320/c1004-31640976.html" target="_blank">看这条产业链上下游怎样打通（人民眼·产业链协同复工复产）</a></h5>
        
        <em>　　<a href="/n1/2020/0320/c1004-31640976.html" target="_blank">引&nbsp;子正月初六，张玉清准时从山东老家赶回位于江苏苏州高新区的莱克电气公司。作为这家拥有8500多名员工公司的执行总裁，张玉清这个年过得忐忑不安：疫情当前，延迟开工，2月份的90万台订单能完成多少？莱克电气是一家以生产吸尘器、空气净化器、净水机等家用电器为主的电器制造企业，直接相关的上游配套企业就有600多家。</a></em></div>
        <h6><em class="gray"><img src="/img/MAIN/2016/10/116825/images/icon4.gif" width="24" height="21"><a href="/GB/70846/index.html" target="_blank">滚动</a>|<a href="/GB/index.html" target="_blank">财经</a></em>
        <span><a href="/n1/2020/0320/c1004-31640976.html#liuyan" target="_blank"><img src="/img/MAIN/2016/10/116825/images/icon2b.gif" class="ly"></a>
        <div class="bshare-custom fr"><div class="bsPromo bsPromo2"></div>
            <div class="bsPromo bsPromo2"></div>
            <a title="更多平台" class="bshare-more bshare-more-icon more-style-addthis"></a></div>
        </span></h6>
      </div>
<div class="hdNews clearfix">
        <div class="on">
        <h5><a href="/n1/2020/0320/c1004-31640975.html" target="_blank">重庆江津 工业企业全部复工复产</a></h5>
        
        <em>　　<a href="/n1/2020/0320/c1004-31640975.html" target="_blank">“长兴机械能否尽快复工？园区龙头企业潍柴动力就差它配套了。”“刚去现场看了，企业缺防疫物资，无口罩、无酒精，负责人还在隔离中。</a></em></div>
        <h6><em class="gray"><img src="/img/MAIN/2016/10/116825/images/icon4.gif" width="24" height="21"><a href="/GB/70846/index.html" target="_blank">滚动</a>|<a href="/GB/index.html" target="_blank">财经</a></em>
        <span><a href="/n1/2020/0320/c1004-31640975.html#liuyan" target="_blank"><img src="/img/MAIN/2016/10/116825/images/icon2b.gif" class="ly"></a>
        <div class="bshare-custom fr"><div class="bsPromo bsPromo2"></div>
            <div class="bsPromo bsPromo2"></div>
            <a title="更多平台" class="bshare-more bshare-more-icon more-style-addthis"></a></div>
        </span></h6>
      </div>
<div class="page_n clearfix"><a href="index1.html#fy01">上一页</a>&nbsp;<a href="index1.html#fy01">1</a>&nbsp;<a class="common_current_page">2</a>&nbsp;<a href="index3.html#fy01">3</a>&nbsp;<a href="index4.html#fy01">4</a>&nbsp;<a href="index5.html#fy01">5</a>&nbsp;<a href="index6.html#fy01">6</a>&nbsp;&nbsp;<a href="index3.html#fy01">下一页</a></div><!--all page--><!--PageNo=12-->

     </div>
<div class="headingNews qiehuan1_c" style="display: none;">      
      <div class="hdNews clearfix">
        <div class="on">
        <h5><a href="http://money.people.com.cn/n1/2020/0320/c42877-31641996.html" target="_blank">“青春战疫 希望同行” 上海农商银行捐赠100万元关爱青少年成长</a></h5>
        
        <em>　　<a href="http://money.people.com.cn/n1/2020/0320/c42877-31641996.html" target="_blank">人民网北京3月20日电&nbsp;近日，上海农商银行向上海市青少年发展基金会捐赠100万元，用于帮扶、资助本市家庭困难的6-18岁青少年。这也是该行积极响应共青团上海市委员会、上海市青年联合会、上海市青少年服务和权益保护办公室、少先队上海市工作委员会、上海市青少年发展基金会联合发起的“青春战疫&nbsp;希望同行”万名困难青少年帮扶行动的号召，助力打赢疫情攻坚战的又一举措。</a></em></div>
        <h6><em class="gray"><img src="/img/MAIN/2016/10/116825/images/icon4.gif" width="24" height="21"><a href="http://money.people.com.cn/bank/" target="_blank">银行频道</a>|<a href="http://money.people.com.cn/" target="_blank">金融</a>|<a href="http://money.people.com.cn/GB/400619/index.html" target="_blank">金融·广角</a></em>
        <span><a href="http://money.people.com.cn/n1/2020/0320/c42877-31641996.html#liuyan" target="_blank"><img src="/img/MAIN/2016/10/116825/images/icon2b.gif" class="ly"></a>
        <div class="bshare-custom fr"><div class="bsPromo bsPromo2"></div>
            <div class="bsPromo bsPromo2"></div>
            <a title="更多平台" class="bshare-more bshare-more-icon more-style-addthis"></a></div>
        </span></h6>
      </div>
<div class="hdNews clearfix">
        <div class="on">
        <h5><a href="http://money.people.com.cn/n1/2020/0320/c42877-31641479.html" target="_blank">3月1年期LPR报4.05% 与上月保持不变</a></h5>
        
        <em>　　<a href="http://money.people.com.cn/n1/2020/0320/c42877-31641479.html" target="_blank">人民网北京3月20日电（王仁宏）据全国银行间同业拆借中心公布，2020年3月20日贷款市场报价利率（LPR）为：1年期LPR为4.05%，5年期以上LPR为4.75%。	中国民生银行首席研究员温彬表示，当前货币政策和金融工作的核心是保持流动性合理充裕并进一步降低实体经济融资成本。</a></em></div>
        <h6><em class="gray"><img src="/img/MAIN/2016/10/116825/images/icon4.gif" width="24" height="21"><a href="http://money.people.com.cn/" target="_blank">金融</a>|<a href="http://money.people.com.cn/bank/" target="_blank">银行频道</a>|<a href="http://money.people.com.cn/GB/399292/index.html" target="_blank">原创新闻</a></em>
        <span><a href="http://money.people.com.cn/n1/2020/0320/c42877-31641479.html#liuyan" target="_blank"><img src="/img/MAIN/2016/10/116825/images/icon2b.gif" class="ly"></a>
        <div class="bshare-custom fr"><div class="bsPromo bsPromo2"></div>
            <div class="bsPromo bsPromo2"></div>
            <a title="更多平台" class="bshare-more bshare-more-icon more-style-addthis"></a></div>
        </span></h6>
      </div>
<div class="hdNews clearfix">
        <div class="on">
        <h5><a href="http://money.people.com.cn/n1/2020/0320/c42877-31641405.html" target="_blank">美联储联手九大央行救市：美股巨震翻红 油价猛涨</a></h5>
        <a href="http://money.people.com.cn/n1/2020/0320/c42877-31641405.html" target="_blank"><img src="http://www.people.com.cn/mediafile/pic/20200320/23/10150355655344021363.jpg" width="250"></a>
        <em>　　<a href="http://money.people.com.cn/n1/2020/0320/c42877-31641405.html" target="_blank">全球股市总算是该缓口气了。	经历大幅震荡后，隔夜美股三大股指集体收涨。</a></em></div>
        <h6><em class="gray"><img src="/img/MAIN/2016/10/116825/images/icon4.gif" width="24" height="21"><a href="http://money.people.com.cn/" target="_blank">金融</a>|<a href="http://money.people.com.cn/stock/" target="_blank">股票频道</a>|<a href="http://money.people.com.cn/GB/400619/index.html" target="_blank">金融·广角</a></em>
        <span><a href="http://money.people.com.cn/n1/2020/0320/c42877-31641405.html#liuyan" target="_blank"><img src="/img/MAIN/2016/10/116825/images/icon2b.gif" class="ly"></a>
        <div class="bshare-custom fr"><div class="bsPromo bsPromo2"></div>
            <div class="bsPromo bsPromo2"></div>
            <a title="更多平台" class="bshare-more bshare-more-icon more-style-addthis"></a></div>
        </span></h6>
      </div>
<div class="hdNews clearfix">
        <div class="on">
        <h5><a href="http://money.people.com.cn/n1/2020/0320/c42877-31641390.html" target="_blank">一日5张罚单 券商违规行为被“点名”</a></h5>
        
        <em>　　<a href="http://money.people.com.cn/n1/2020/0320/c42877-31641390.html" target="_blank">新《证券法》压实“看门人”职责	一日5张罚单&nbsp;券商违规行为被“点名”	新《证券法》落地以来，监管部门加强对券商违规行为的查处。日前，深圳证监局一天之内对5家券商下发罚单，对其存在的诸多违规行为予以监管。</a></em></div>
        <h6><em class="gray"><img src="/img/MAIN/2016/10/116825/images/icon4.gif" width="24" height="21"><a href="http://money.people.com.cn/GB/218900/index.html" target="_blank">滚动</a>|<a href="http://money.people.com.cn/GB/400619/index.html" target="_blank">金融·广角</a>|<a href="http://money.people.com.cn/" target="_blank">金融</a></em>
        <span><a href="http://money.people.com.cn/n1/2020/0320/c42877-31641390.html#liuyan" target="_blank"><img src="/img/MAIN/2016/10/116825/images/icon2b.gif" class="ly"></a>
        <div class="bshare-custom fr"><div class="bsPromo bsPromo2"></div>
            <div class="bsPromo bsPromo2"></div>
            <a title="更多平台" class="bshare-more bshare-more-icon more-style-addthis"></a></div>
        </span></h6>
      </div>
<div class="hdNews clearfix">
        <div class="on">
        <h5><a href="http://money.people.com.cn/n1/2020/0320/c42877-31641376.html" target="_blank">三天抄底逾百亿元 保险资金出手布局两条主线</a></h5>
        
        <em>　　<a href="http://money.people.com.cn/n1/2020/0320/c42877-31641376.html" target="_blank">海外市场大跌波及A股市场，沪指接连击穿关键点位。正当部分投资者对下一步走势和操作踌躇不定，甚至信心动摇时，一直追求价值投资的保险资金再度出手。</a></em></div>
        <h6><em class="gray"><img src="/img/MAIN/2016/10/116825/images/icon4.gif" width="24" height="21"><a href="http://money.people.com.cn/" target="_blank">金融</a>|<a href="http://money.people.com.cn/GB/218900/index.html" target="_blank">滚动</a>|<a href="http://money.people.com.cn/GB/400619/index.html" target="_blank">金融·广角</a></em>
        <span><a href="http://money.people.com.cn/n1/2020/0320/c42877-31641376.html#liuyan" target="_blank"><img src="/img/MAIN/2016/10/116825/images/icon2b.gif" class="ly"></a>
        <div class="bshare-custom fr"><div class="bsPromo bsPromo2"></div>
            <div class="bsPromo bsPromo2"></div>
            <a title="更多平台" class="bshare-more bshare-more-icon more-style-addthis"></a></div>
        </span></h6>
      </div>
<div class="page_n clearfix"><a href="index1.html#fy01">上一页</a>&nbsp;<a href="index1.html#fy01">1</a>&nbsp;<a class="common_current_page">2</a>&nbsp;<a href="index3.html#fy01">3</a>&nbsp;<a href="index4.html#fy01">4</a>&nbsp;<a href="index5.html#fy01">5</a>&nbsp;<a href="index6.html#fy01">6</a>&nbsp;&nbsp;<a href="index3.html#fy01">下一页</a></div><!--all page--><!--PageNo=12-->

     </div>




'''
def getAllText(url):
    req = urllib.request.urlopen(url)
    data = req.read().decode()
    soup = BeautifulSoup(data,"html.parser")
    pText = soup.select("div[class='box_con'] p")
    print(pText)


soup = BeautifulSoup(doc, "html.parser")
hds = soup.select("div[class='headingNews qiehuan1_c'] div[class='hdNews clearfix']")
for hd in hds:
    title = hd.select("h5")[0].text
    cText = hd.select("em")[0].text
    cAtext = hd.select("h5 a")[0]["href"]

hdl = soup.select("div[class='headingNews qiehuan1_c']")[-1]
next_page = hdl.select("div[class='page_n clearfix'] a")[-1]


if next_page.text == "下一页":
    url = urllib.request.urljoin(start_url,next_page)
    spider(url)






