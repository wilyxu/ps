# coding=utf-8

from bs4 import BeautifulSoup
html="""
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <link rel="canonical" href="https://blog.csdn.net/zwq912318834/article/details/79571110"/>
    <meta http-equiv="content-type" content="text/html; charset=utf-8">
    <meta name="renderer" content="webkit"/>
    <meta name="force-rendering" content="webkit"/>
    <meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1"/>
    <meta name="viewport" content="width=device-width, initial-scale=1.0, minimum-scale=1.0, maximum-scale=1.0, user-scalable=no">
    <meta name="apple-mobile-web-app-status-bar-style" content="black">
    <meta name="referrer" content="always">
    <meta http-equiv="Cache-Control" content="no-siteapp" /><link rel="alternate" media="handheld" href="#" />
    <meta name="shenma-site-verification" content="5a59773ab8077d4a62bf469ab966a63b_1497598848">
        <meta name="csdn-baidu-search" = content='{"autorun":true,"install":true,"keyword":"python+requests+%E6%A8%A1%E6%8B%9F%E7%99%BB%E5%BD%95"}'>
        <script src="https://csdnimg.cn/release/phoenix/vendor/tingyun/tingyun-rum-blog.js"></script>

    <link href="https://csdnimg.cn/public/favicon.ico" rel="SHORTCUT ICON">
    <title>python3下使用requests实现模拟用户登录 —— 基础篇（马蜂窝） - Kosmoo的博客 - CSDN博客</title>

        
                    <link rel="stylesheet" href="https://csdnimg.cn/release/phoenix/template/css/detail-312775a663.min.css">
            
        
          <link rel="stylesheet" href="https://csdnimg.cn/release/phoenix/themes/skin-yellow/skin-yellow-2eefd34acf.min.css">
        <script type="text/javascript">
        var username = "zwq912318834";
        var blog_address = "https://blog.csdn.net/zwq912318834";
        var static_host = "https://csdnimg.cn/release/phoenix/";
        var currentUserName = "";
        var isShowAds = true;
        var isOwner = false;
        var loginUrl = "http://passport.csdn.net/account/login?from=https://blog.csdn.net/zwq912318834/article/details/79571110"
        var blogUrl = "https://blog.csdn.net/";
        //页面皮肤样式
        var curSkin = "skin-yellow";
        // 第四范式所需数据
        var articleTitles = "python3下使用requests实现模拟用户登录 —— 基础篇（马蜂窝） - Kosmoo的博客";
        var articleID = "79571110";

        var nickName = "Kosmoo";
        var isCorporate = false;
    </script>
    <script type="text/javascript">
        // Traffic Stats of the entire Web site By baidu
        var _hmt = _hmt || [];
        (function() {
            var hm = document.createElement("script");
            hm.src = "https://hm.baidu.com/hm.js?6bcd52f51e9b3dce32bec4a3997715ac";
            var s = document.getElementsByTagName("script")[0];
            s.parentNode.insertBefore(hm, s);
        })();
        // Traffic Stats of the entire Web site By baidu end
    </script>
    <script src="https://csdnimg.cn/public/common/libs/jquery/jquery-1.9.1.min.js" type="text/javascript"></script>
    <script src="https://csdnimg.cn/rabbit/exposure-click/main-1.0.6.js"></script>
    <script src="//g.csdnimg.cn/fixed-sidebar/1.1.3/fixed-sidebar.js" type="text/javascript"></script>
    <!-- 新版上报 -->
    <script src="//g.csdnimg.cn/track/1.2.4/track.js" type="text/javascript"></script>
    <!-- 新版上报end -->
            <link rel="stylesheet" href="https://csdnimg.cn/public/sandalstrap/1.4/css/sandalstrap.min.css">
    <style>
        .MathJax, .MathJax_Message, .MathJax_Preview{
            display: none
        }
    </style>
</head>
<!-- nodata 第三栏接口无数据时样式不变 -->
<body class="nodata " > 
    <link rel="stylesheet" href="https://csdnimg.cn/public/common/toolbar/content_toolbar_css/content_toolbar.css">
    <script id="toolbar-tpl-scriptId" src="https://csdnimg.cn/public/common/toolbar/js/content_toolbar.js" type="text/javascript" domain="https://blog.csdn.net/"></script>
<div id="kp_box_476" data-pid="476" data-track-view='{"mod":"kp_popu_476-794","con":",,"}' data-track-click='{"mod":"kp_popu_476-794","con":",,"}'><script src="//csdnimg.cn/public/common/indexSuperise/1.0.1/indexSuperise.js?20190103190825"></script>
<script>
 window.csdn.indexSuperise({
      smallMoveImg: '//ubmcmm.baidustatic.com/media/v1/0f000ji9GQBTQif4KlS1n6.jpg',
      bigMoveImg: '//ubmcmm.baidustatic.com/media/v1/0f000Dd29O15Im4ZGHXmF0.jpg',
     link:'//bss.csdn.net/m/topic/blog_star2018/index?utm_source=bloghudong',
boxStyle:140,
trackSuperId:476,
smallMove:'notMove',  
trackSId:794
    });
</script></div><link rel="stylesheet" href="https://csdnimg.cn/release/phoenix/template/css/blog_code-c3a0c33d5c.css">
<link rel="stylesheet" href="https://csdnimg.cn/release/phoenix/vendor/pagination/paging.css">
<script type="text/javascript">
	// 容错处理
	var NEWS_FEED = function(){}
</script>
<script type="text/javascript" src="//static.mediav.com/js/mvf_news_feed.js"></script>
<script type="text/javascript" src="//g.csdnimg.cn/copyright/1.0.3/copyright.js"></script>
<div style="display:none;">
	<img src="" onerror='setTimeout(function(){if(!/(csdn.net|iteye.com|baiducontent.com|googleusercontent.com|360webcache.com|sogoucdn.com|bingj.com|baidu.com)$/.test(window.location.hostname)){window.location.href="\x68\x74\x74\x70\x73\x3a\x2f\x2f\x77\x77\x77\x2e\x63\x73\x64\x6e\x2e\x6e\x65\x74"}},3000);'>
</div>
<link rel="stylesheet" href="https://csdnimg.cn/release/phoenix/template/css/chart-3456820cac.css" />
<script src="https://dup.baidustatic.com/js/ds.js"></script>
<div class="container clearfix" id="mainBox">
			<div class="recommend-right">
  <ul class="recommend-fixed-box">
    
  </ul>
</div>	
    <main>
        <div class="blog-content-box">
	<div class="article-header-box">
		<div class="article-header">
			<div class="article-title-box">
				<span class="article-type type-1 float-left">原</span>				<h1 class="title-article">python3下使用requests实现模拟用户登录 —— 基础篇（马蜂窝）</h1>
			</div>
			<div class="article-info-box">
				<div class="article-bar-top">
																				<span class="time">2018年03月15日 17:20:17</span>
					<a class="follow-nickName" href="https://me.csdn.net/zwq912318834" target="_blank">Kosmoo</a>
						<span class="read-count">阅读数：10330</span>
						
																															</div>
				<div class="operating">
														</div>
			</div>
		</div>
	</div>
	<article class="baidu_pl">
		<div id="article_content" class="article_content clearfix csdn-tracking-statistics" data-pid="blog"  data-mod=popu_307  data-dsm = "post" >
								<div class="article-copyright">
                  					<svg class="icon" title="CSDN认证原创" aria-hidden="true" style="width:53px; height: 18px; vertical-align: -4px;">
							<use xlink:href="#CSDN_Cert"></use>
					</svg>
                  					
					版权声明：本文为博主原创文章，未经博主允许不得转载。					https://blog.csdn.net/zwq912318834/article/details/79571110				</div>
								            <div id="content_views" class="markdown_views prism-atom-one-dark">
							<!-- flowchart 箭头图标 勿删 -->
							<svg xmlns="http://www.w3.org/2000/svg" style="display: none;"><path stroke-linecap="round" d="M5,0 0,2.5 5,5z" id="raphael-marker-block" style="-webkit-tap-highlight-color: rgba(0, 0, 0, 0);"></path></svg>
							<h1 id="python3下使用requests实现模拟用户登录-基础篇马蜂窝">python3下使用requests实现模拟用户登录 —— 基础篇（马蜂窝）</h1>

<h2 id="1-了解cookie和session">1. 了解cookie和session</h2>

<ul>
<li>首先一定要先了解到cookie和session是什么，这是后面理解网站交互，模拟用户登录的基础。</li>
</ul>



<h3 id="11-无状态协议http">1.1. 无状态协议：Http</h3>

<p><img src="//img-blog.csdn.net/2018031615455894?watermark/2/text/Ly9ibG9nLmNzZG4ubmV0L3p3cTkxMjMxODgzNA==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70" alt="这里写图片描述" title=""></p>

<ul>
<li>如上图所示，<strong>HTTP协议</strong> 是无状态的协议，用户浏览服务器上的内容，只需要发送页面请求，服务器返回内容。对于服务器来说，并不关心，也并不知道是哪个用户的请求。对于一般浏览性的网页来说，没有任何问题。</li>
<li>但是，现在很多的网站，是需要用户登录的。以淘宝为例：比如说某个用户想购买一个产品，当点击 “ 购买按钮 ” 时，由于<strong>HTTP协议</strong> 是无状态的，那对于淘宝来说，就不知道是哪个用户操作的。</li>
<li>为了实现这种用户标记，服务器就采用了cookie这种机制来识别具体是哪一个用户的访问。</li>
</ul>



<h3 id="12-了解cookie">1.2. 了解cookie</h3>

<p><img src="//img-blog.csdn.net/20180316155341853?watermark/2/text/Ly9ibG9nLmNzZG4ubmV0L3p3cTkxMjMxODgzNA==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70" alt="这里写图片描述" title=""></p>

<ul>
<li><p>如图，为了实现用户标记，在Http无状态请求的基础之上，我们需要在请求中携带一些用户信息（比如用户名之类，<strong>这些信息是服务器发送到本地浏览器的，但是服务器并不存储这些信息</strong>），这就是cookie机制。如下图所示，在登录马蜂窝网站之后，就可以看到浏览器已经保存了一些cookie信息（chrome浏览器为例）： <br>
<img src="//img-blog.csdn.net/20180316155648184?watermark/2/text/Ly9ibG9nLmNzZG4ubmV0L3p3cTkxMjMxODgzNA==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70" alt="这里写图片描述" title=""></p></li>
<li><p><strong>需要注意的是：cookie信息是保存在本地浏览器里面的，服务器上并不存储相关的信息。 在发送请求时，cookie的这些内容是放在 Http协议中的header 字段中进行传输的。</strong> <br>
<img src="//img-blog.csdn.net/20180316160200685?watermark/2/text/Ly9ibG9nLmNzZG4ubmV0L3p3cTkxMjMxODgzNA==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70" alt="这里写图片描述" title=""></p></li>
<li>几乎现在所有的网站都会发送一些 cookie信息过来，当用户请求中携带了cookie信息，服务器就可以知道是哪个用户的访问了，从而不需要再使用账户和密码登录。</li>
<li>但是，<strong>刚才也提到了，cookie信息是直接放在Http协议的header中进行传输的</strong>，看得出来，这是个隐患！一旦别人获取到你的cookie信息（截获请求，或者使用你的电脑），那么他很容易从cookie中分析出你的用户名和密码。为了解决这个隐患，所以有了session机制。</li>
</ul>



<h3 id="13-了解session">1.3. 了解session</h3>

<ul>
<li>刚才提到了cookie不安全，所以有了session机制。简单来说（每个框架都不一样，这只是举一个通用的实现策略），整过过程是这样： <br>
<ul><li>服务器根据用户名和密码，生成一个session ID，存储到服务器的数据库中。</li>
<li>用户登录访问时，服务器会将对应的session ID发送给用户（本地浏览器）。</li>
<li>浏览器会将这个session ID存储到cookie中，作为一个键值项。</li>
<li>以后，浏览器每次请求，就会将含有session ID的cookie信息，一起发送给服务器。</li>
<li>服务器收到请求之后，通过cookie中的session ID，到数据库中去查询，解析出对应的用户名，就知道是哪个用户的请求了。</li></ul></li>
</ul>



<h4 id="131-看一下django是如何实现session机制的来加深对session的了解">1.3.1. 看一下Django是如何实现session机制的，来加深对session的了解</h4>

<ul>
<li>第一步：对用户登录信息进行加密，生成一个sessionID，存储到数据库中。 <br>
<img src="//img-blog.csdn.net/20180316163024242?watermark/2/text/Ly9ibG9nLmNzZG4ubmV0L3p3cTkxMjMxODgzNA==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70" alt="这里写图片描述" title=""> <br>
<img src="//img-blog.csdn.net/20180316163031719?watermark/2/text/Ly9ibG9nLmNzZG4ubmV0L3p3cTkxMjMxODgzNA==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70" alt="这里写图片描述" title=""></li>
</ul>



<pre class="prettyprint"><code class=" hljs ">    Session_key：服务器给用户返回的ID
    Session_data：一段加密的文字。用户名，密码，一些其他的用户信息。把这些信息生成一段字符串，是加密的
    expire_date：django后台会设置过期时间。 主要是担心session被黑客截取，那就一直可以用，盗用数据。</code></pre>

<ul>
<li><p>第二步，当用户登录时，服务器会给本地浏览器返回一些cookie信息，包括session ID。 <br>
<img src="//img-blog.csdn.net/20180316163441237?watermark/2/text/Ly9ibG9nLmNzZG4ubmV0L3p3cTkxMjMxODgzNA==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70" alt="这里写图片描述" title=""></p>

<ul><li>第三步：以后浏览器每次访问时，浏览器都会把 session ID带过来，这样服务器不需要知道你的用户名，就知道是哪个用户的访问了。</li></ul></li>
<li><p>服务器是如何把sessionID转换成用户名的？ <br>
<img src="//img-blog.csdn.net/20180316163812301?watermark/2/text/Ly9ibG9nLmNzZG4ubmV0L3p3cTkxMjMxODgzNA==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70" alt="这里写图片描述" title=""></p>

<ul><li>如上图所示，在Django中，需要对session进行配置。这个<strong>INSTALLED_APPS</strong> 是会对每次request和response进行拦截，拦截到浏览器发送过来的request时，找到其中的session信息，然后到数据库中进行查询，找到session_data，再做解密，就知道所有的用户信息了，取出user信息。新建完Django项目之后，这个sessions信息就配置好了。如果注释掉这一个session配置，自动登录机制就会失效，无法使用。</li></ul></li>
</ul>



<h3 id="14-总结一下">1.4. 总结一下</h3>

<ul>
<li>cookie 在客户端（本地浏览器），session 在服务器端。cookie是一种浏览器本地存储机制。存储在本地浏览器中，和服务器没有关系。每次请求，用户会带上本地cookie的信息。这些cookie信息也是服务器之前发送给浏览器的，或者是用户之前填写的一些信息。</li>
<li>Cookie有不安全机制。 你不能把所有的用户信息都存在本地，一旦被别人窃取，就知道你的用户名和密码，就会很危险。所以引入了session机制。</li>
<li>服务器在发送id时引入了一种session的机制，很简单，就是根据用户名和密码，生成了一段随机的字符串，这段字符串是有过期时间的。 </li>
<li>一定要注意：session是服务器生成的，存储在服务器的数据库或者文件中，然后把sessionID发送给用户，用户存储在本地cookie中。每次请求时，把这个session ID带给服务器，服务器根据session ID到数据库中去查询，找到是哪个用户，就可以对用户进行标记了。</li>
<li>session 的运行依赖 session ID，而 session ID 是存在 cookie 中的，也就是说，如果浏览器禁用了 cookie ，那么同时 session 也会失效（但是可以通过其它方式实现，比如在url中传递 session ID）</li>
<li>用户验证这种场合一般会用 session。 因此，维持一个会话的核心就是客户端的唯一标识，即session ID</li>
</ul>



<h2 id="2-环境">2. 环境</h2>

<ul>
<li>系统：win7</li>
<li>python 3.6.1</li>
<li>requests 2.14.2 （通过pip list查看）</li>
</ul>



<h2 id="3-模拟登录马蜂窝网站">3. 模拟登录马蜂窝网站</h2>

<ul>
<li>马蜂窝：<a href="http://www.mafengwo.cn/" rel="nofollow">http://www.mafengwo.cn/</a></li>
</ul>



<h2 id="31-分析用户登录流程">3.1. 分析用户登录流程</h2>

<ul>
<li>这里会用到两个小技巧 <br>
<ul><li>第一，先使用一个错误的用户名和密码来登录，这样就可以清晰的看到这个登录请求有post哪些数据，post到哪个url。因为如果使用正确的用户名和密码登录，一旦登录成功，就会直接跳转到其他页面，页面和请求都会被刷新。很难找出原始的请求信息。 <br>
<img src="//img-blog.csdn.net/20180316112345512?watermark/2/text/Ly9ibG9nLmNzZG4ubmV0L3p3cTkxMjMxODgzNA==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70" alt="这里写图片描述" title=""></li>
<li>第二，在截取请求的地方，勾选Preserve log，保留跳转前的请求数据。 <br>
<img src="//img-blog.csdn.net/20180316112538885?watermark/2/text/Ly9ibG9nLmNzZG4ubmV0L3p3cTkxMjMxODgzNA==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70" alt="这里写图片描述" title=""></li></ul></li>
<li>截取到的请求如下： <br>
<img src="//img-blog.csdn.net/20180316112844803?watermark/2/text/Ly9ibG9nLmNzZG4ubmV0L3p3cTkxMjMxODgzNA==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70" alt="这里写图片描述" title=""> <br>
<img src="//img-blog.csdn.net/20180316112857322?watermark/2/text/Ly9ibG9nLmNzZG4ubmV0L3p3cTkxMjMxODgzNA==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70" alt="这里写图片描述" title=""></li>
</ul>



<pre class="prettyprint"><code class="language-python 3.6.1 hljs "><span class="hljs-comment">#提取到的请求信息：</span>
Headers：
    Request URL:https://passport.mafengwo.cn/login/
    Request Method:POST 
    origin:https://passport.mafengwo.cn 
    referer:https://passport.mafengwo.cn/   
    User-Agent:Mozilla/<span class="hljs-number">5.0</span> (Windows NT <span class="hljs-number">6.1</span>; WOW64) AppleWebKit/<span class="hljs-number">537.36</span> (KHTML, like Gecko)     Chrome/<span class="hljs-number">63.0</span><span class="hljs-number">.3239</span><span class="hljs-number">.132</span> Safari/<span class="hljs-number">537.36</span>    

Form Data:
    passport:<span class="hljs-number">13725168940</span>
    password:aaa00000000</code></pre>



<h2 id="32-模拟登录">3.2. 模拟登录</h2>



<pre class="prettyprint"><code class=" hljs python"><span class="hljs-comment"># -*- coding: utf-8 -*-</span>

<span class="hljs-keyword">import</span> requests

userAgent = <span class="hljs-string">"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36"</span>
header = {
    <span class="hljs-comment"># "origin": "https://passport.mafengwo.cn",</span>
    <span class="hljs-string">"Referer"</span>: <span class="hljs-string">"https://passport.mafengwo.cn/"</span>,
    <span class="hljs-string">'User-Agent'</span>: userAgent,
}

<span class="hljs-function"><span class="hljs-keyword">def</span> <span class="hljs-title">mafengwoLogin</span><span class="hljs-params">(account, password)</span>:</span>
    <span class="hljs-comment"># 马蜂窝模仿 登录</span>
    <span class="hljs-keyword">print</span> (<span class="hljs-string">"开始模拟登录马蜂窝"</span>)

    postUrl = <span class="hljs-string">"https://passport.mafengwo.cn/login/"</span>
    postData = {
        <span class="hljs-string">"passport"</span>: account,
        <span class="hljs-string">"password"</span>: password,
    }
    responseRes = requests.post(postUrl, data = postData, headers = header)
    <span class="hljs-comment"># 无论是否登录成功，状态码一般都是 statusCode = 200</span>
    print(f<span class="hljs-string">"statusCode = {responseRes.status_code}"</span>)
    print(f<span class="hljs-string">"text = {responseRes.text}"</span>)

<span class="hljs-keyword">if</span> __name__ == <span class="hljs-string">"__main__"</span>:
    <span class="hljs-comment"># 从返回结果来看，有登录成功</span>
    mafengwoLogin(<span class="hljs-string">"13756567832"</span>, <span class="hljs-string">"000000001"</span>)
</code></pre>

<ul>
<li>一般来说，调试期，判断是否登录成功的最简单的方法：<strong>就是直接打印登录之后的text内容，使用错误的用户名登录，和使用正确的用户名登录，对比打印输出的内容。</strong></li>
<li>后面会提出一个更好的判断方式…</li>
</ul>



<h2 id="33-使用cookie访问站点">3.3. 使用cookie访问站点</h2>

<ul>
<li>在上一步，我们已经成功登录到马蜂窝网站了。那么接下来要如何访问站点中其他页面呢。前面提到过，网站是通过cookie和session来标记是哪个用户访问的。所以，在我们登录成功之后，有很重要的一步，就是我们需要把cookie保存下来，下一次请求这个站点的页面时，把这个cookie带过去。</li>
</ul>



<h3 id="331-保存cookie信息">3.3.1. 保存cookie信息</h3>

<ul>
<li>修改代码，<strong>加入cookie保存机制</strong>：</li>
</ul>



<pre class="prettyprint"><code class="language-python 3.6.1 hljs "><span class="hljs-comment"># -*- coding: utf-8 -*-</span>

<span class="hljs-keyword">import</span> requests

<span class="hljs-comment"># python2 和 python3的兼容代码</span>
<span class="hljs-keyword">try</span>:
    <span class="hljs-comment"># python2 中</span>
    <span class="hljs-keyword">import</span> cookielib
    print(f<span class="hljs-string">"user cookielib in python2."</span>)
<span class="hljs-keyword">except</span>:
    <span class="hljs-comment"># python3 中</span>
    <span class="hljs-keyword">import</span> http.cookiejar <span class="hljs-keyword">as</span> cookielib
    print(f<span class="hljs-string">"user cookielib in python3."</span>)

<span class="hljs-comment"># session代表某一次连接</span>
mafengwoSession = requests.session()
<span class="hljs-comment"># 因为原始的session.cookies 没有save()方法，所以需要用到cookielib中的方法LWPCookieJar，这个类实例化的cookie对象，就可以直接调用save方法。</span>
mafengwoSession.cookies = cookielib.LWPCookieJar(filename = <span class="hljs-string">"mafengwoCookies.txt"</span>)

userAgent = <span class="hljs-string">"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36"</span>
header = {
    <span class="hljs-comment"># "origin": "https://passport.mafengwo.cn",</span>
    <span class="hljs-string">"Referer"</span>: <span class="hljs-string">"https://passport.mafengwo.cn/"</span>,
    <span class="hljs-string">'User-Agent'</span>: userAgent,
}

<span class="hljs-function"><span class="hljs-keyword">def</span> <span class="hljs-title">mafengwoLogin</span><span class="hljs-params">(account, password)</span>:</span>
    <span class="hljs-comment"># 马蜂窝模仿 登录</span>
    print(<span class="hljs-string">"开始模拟登录马蜂窝"</span>)

    postUrl = <span class="hljs-string">"https://passport.mafengwo.cn/login/"</span>
    postData = {
        <span class="hljs-string">"passport"</span>: account,
        <span class="hljs-string">"password"</span>: password,
    }
    <span class="hljs-comment"># 使用session直接post请求</span>
    responseRes = mafengwoSession.post(postUrl, data = postData, headers = header)
    <span class="hljs-comment"># 无论是否登录成功，状态码一般都是 statusCode = 200</span>
    print(f<span class="hljs-string">"statusCode = {responseRes.status_code}"</span>)
    print(f<span class="hljs-string">"text = {responseRes.text}"</span>)
    <span class="hljs-comment"># 登录成功之后，将cookie保存在本地文件中，好处是，以后再去获取马蜂窝首页的时候，就不需要再走mafengwoLogin的流程了，因为已经从文件中拿到cookie了</span>
    mafengwoSession.cookies.save()


<span class="hljs-keyword">if</span> __name__ == <span class="hljs-string">"__main__"</span>:
    <span class="hljs-comment"># 从返回结果来看，有登录成功</span>
    <span class="hljs-comment"># mafengwoLogin("13756567832", "000000001")</span></code></pre>

<ul>
<li>cookie保存结果如下：</li>
</ul>



<pre class="prettyprint"><code class=" hljs perl"><span class="hljs-comment"># 文件：mafengwoCookies.txt</span>

<span class="hljs-comment">#LWP-Cookies-2.0</span>
Set-Cookie3: __today_login=<span class="hljs-number">1</span>; path=<span class="hljs-string">"/"</span>; domain=<span class="hljs-string">".mafengwo.cn"</span>; path_spec; domain_dot; expires=<span class="hljs-string">"2018-03-16 15:56:15Z"</span>; httponly=None; version=<span class="hljs-number">0</span>
Set-Cookie3: mafengwo=<span class="hljs-string">"0a60e1a04f6a6f5555f0e285602b5b17_94281374_5aab641fb23d42.37804626_5aab641fb23dc3.28763728"</span>; path=<span class="hljs-string">"/"</span>; domain=<span class="hljs-string">".mafengwo.cn"</span>; path_spec; domain_dot; expires=<span class="hljs-string">"2018-06-13 06:25:03Z"</span>; httponly=None; version=<span class="hljs-number">0</span>
Set-Cookie3: mfw_uuid=<span class="hljs-string">"5aab641f-b789-96ef-736d-48640285f4c0"</span>; path=<span class="hljs-string">"/"</span>; domain=<span class="hljs-string">".mafengwo.cn"</span>; path_spec; domain_dot; expires=<span class="hljs-string">"2019-03-16 06:25:03Z"</span>; version=<span class="hljs-number">0</span>
Set-Cookie3: oad_n=<span class="hljs-string">"a<span class="hljs-variable">%3A3</span><span class="hljs-variable">%3A</span><span class="hljs-variable">%7Bs</span><span class="hljs-variable">%3A3</span><span class="hljs-variable">%3A</span><span class="hljs-variable">%22oid</span><span class="hljs-variable">%22</span><span class="hljs-variable">%3Bi</span><span class="hljs-variable">%3A1029</span><span class="hljs-variable">%3Bs</span><span class="hljs-variable">%3A2</span><span class="hljs-variable">%3A</span><span class="hljs-variable">%22dm</span><span class="hljs-variable">%22</span><span class="hljs-variable">%3Bs</span><span class="hljs-variable">%3A20</span><span class="hljs-variable">%3A</span><span class="hljs-variable">%22passport</span>.mafengwo.cn<span class="hljs-variable">%22</span><span class="hljs-variable">%3Bs</span><span class="hljs-variable">%3A2</span><span class="hljs-variable">%3A</span><span class="hljs-variable">%22ft</span><span class="hljs-variable">%22</span><span class="hljs-variable">%3Bs</span><span class="hljs-variable">%00009</span><span class="hljs-variable">%3A</span><span class="hljs-variable">%222018</span>-03-16+14<span class="hljs-variable">%3A28</span><span class="hljs-variable">%3A47</span><span class="hljs-variable">%22</span><span class="hljs-variable">%3B</span><span class="hljs-variable">%7D</span>"</span>; path=<span class="hljs-string">"/"</span>; domain=<span class="hljs-string">".mafengwo.cn"</span>; path_spec; domain_dot; expires=<span class="hljs-string">"2018-03-23 06:25:03Z"</span>; version=<span class="hljs-number">0</span>
Set-Cookie3: uol_throttle=<span class="hljs-number">94281374</span>; path=<span class="hljs-string">"/"</span>; domain=<span class="hljs-string">".mafengwo.cn"</span>; path_spec; domain_dot; expires=<span class="hljs-string">"2018-03-16 06:35:03Z"</span>; version=<span class="hljs-number">0</span>
</code></pre>



<h3 id="332-使用cookie登录">3.3.2. 使用cookie登录</h3>

<ul>
<li>为了测试访问页面时，是否处于登录状态。有一个比较巧妙的方法：就是直接访问一个需要登录后，才可见的地址。比如说涉及到用户信息的页面。下面以 “我的路线” 页面为例：<a href="http://www.mafengwo.cn/plan/route.php" rel="nofollow">http://www.mafengwo.cn/plan/route.php</a></li>
<li>这是<strong>登录状态</strong>后见到的页面： <br>
<img src="//img-blog.csdn.net/20180316144523581?watermark/2/text/Ly9ibG9nLmNzZG4ubmV0L3p3cTkxMjMxODgzNA==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70" alt="这里写图片描述" title=""> <br>
<img src="//img-blog.csdn.net/20180316144534288?watermark/2/text/Ly9ibG9nLmNzZG4ubmV0L3p3cTkxMjMxODgzNA==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70" alt="这里写图片描述" title=""></li>
<li>如果是 <strong>非登录状态</strong>，会自动跳转（重定向302）到 <strong>用户登录页面</strong>： <br>
<img src="//img-blog.csdn.net/20180316144734916?watermark/2/text/Ly9ibG9nLmNzZG4ubmV0L3p3cTkxMjMxODgzNA==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70" alt="这里写图片描述" title=""></li>
<li>所以，我们可以用这个页面判断cookie登录是否成功，代码如下：</li>
</ul>



<pre class="prettyprint"><code class="language-python 3.6.1 hljs "><span class="hljs-comment"># -*- coding: utf-8 -*-</span>

<span class="hljs-keyword">import</span> requests

<span class="hljs-comment"># python2 和 python3的兼容代码</span>
<span class="hljs-keyword">try</span>:
    <span class="hljs-comment"># python2 中</span>
    <span class="hljs-keyword">import</span> cookielib
    print(f<span class="hljs-string">"user cookielib in python2."</span>)
<span class="hljs-keyword">except</span>:
    <span class="hljs-comment"># python3 中</span>
    <span class="hljs-keyword">import</span> http.cookiejar <span class="hljs-keyword">as</span> cookielib
    print(f<span class="hljs-string">"user cookielib in python3."</span>)

<span class="hljs-comment"># session代表某一次连接</span>
mafengwoSession = requests.session()
<span class="hljs-comment"># 因为原始的session.cookies 没有save()方法，所以需要用到cookielib中的方法LWPCookieJar，这个类实例化的cookie对象，就可以直接调用save方法。</span>
mafengwoSession.cookies = cookielib.LWPCookieJar(filename = <span class="hljs-string">"mafengwoCookies.txt"</span>)

userAgent = <span class="hljs-string">"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36"</span>
header = {
    <span class="hljs-comment"># "origin": "https://passport.mafengwo.cn",</span>
    <span class="hljs-string">"Referer"</span>: <span class="hljs-string">"https://passport.mafengwo.cn/"</span>,
    <span class="hljs-string">'User-Agent'</span>: userAgent,
}

<span class="hljs-function"><span class="hljs-keyword">def</span> <span class="hljs-title">isLoginStatus</span><span class="hljs-params">()</span>:</span>
    <span class="hljs-comment"># 通过访问个人中心页面的返回状态码来判断是否为登录状态</span>

    routeUrl = <span class="hljs-string">"http://www.mafengwo.cn/plan/route.php"</span>
    <span class="hljs-comment"># 下面有两个关键点</span>
        <span class="hljs-comment"># 第一个是header，如果不设置，会返回500的错误</span>
        <span class="hljs-comment"># 第二个是allow_redirects，如果不设置，session访问时，服务器返回302，</span>
        <span class="hljs-comment"># 然后session会自动重定向到登录页面，获取到登录页面之后，变成200的状态码</span>
        <span class="hljs-comment"># allow_redirects = False  就是不允许重定向</span>
    responseRes = mafengwoSession.get(routeUrl, headers = header, allow_redirects = <span class="hljs-keyword">False</span>)
    print(f<span class="hljs-string">"isLoginStatus = {responseRes.status_code}"</span>)
    <span class="hljs-keyword">if</span> responseRes.status_code != <span class="hljs-number">200</span>:
        <span class="hljs-keyword">return</span> <span class="hljs-keyword">False</span>
    <span class="hljs-keyword">else</span>:
        <span class="hljs-keyword">return</span> <span class="hljs-keyword">True</span>


<span class="hljs-keyword">if</span> __name__ == <span class="hljs-string">"__main__"</span>:
    mafengwoSession.cookies.load()
    isLogin = isLoginStatus()
    print(f<span class="hljs-string">"is login mafengwo = {isLogin}"</span>)
    <span class="hljs-string">'''
        # 按照之前保存过的mafengwoCookies.txt登录，属于登录状态：
        user cookielib in python3.
        isLoginStatus = 200
        is login mafengwo = True
    '''</span>

    <span class="hljs-string">'''
        # 如果把mafengwoCookies.txt中的信息修改掉之后，就无法登录了，属于非登录状态了
        user cookielib in python3.
        isLoginStatus = 302
        is login mafengwo = False
    '''</span></code></pre>



<h2 id="34-最终形成的登录模式">3.4. 最终形成的登录模式</h2>

<ul>
<li>因为cookie是有有效期的，所以没法做到一次登录，终生有效。所以，一般的登录模式，就是： <br>
<ul><li>第一步：先尝试cookie登录</li>
<li>第二步：如果cookie无法登录成功，就使用用户名密码登录，将新的cookie保存下来。</li></ul></li>
</ul>



<pre class="prettyprint"><code class="language-python 3.6.1 hljs "><span class="hljs-comment"># -*- coding: utf-8 -*-</span>

<span class="hljs-keyword">import</span> requests

<span class="hljs-comment"># python2 和 python3的兼容代码</span>
<span class="hljs-keyword">try</span>:
    <span class="hljs-comment"># python2 中</span>
    <span class="hljs-keyword">import</span> cookielib
    print(f<span class="hljs-string">"user cookielib in python2."</span>)
<span class="hljs-keyword">except</span>:
    <span class="hljs-comment"># python3 中</span>
    <span class="hljs-keyword">import</span> http.cookiejar <span class="hljs-keyword">as</span> cookielib
    print(f<span class="hljs-string">"user cookielib in python3."</span>)

<span class="hljs-comment"># session代表某一次连接</span>
mafengwoSession = requests.session()
<span class="hljs-comment"># 因为原始的session.cookies 没有save()方法，所以需要用到cookielib中的方法LWPCookieJar，这个类实例化的cookie对象，就可以直接调用save方法。</span>
mafengwoSession.cookies = cookielib.LWPCookieJar(filename = <span class="hljs-string">"mafengwoCookies.txt"</span>)

userAgent = <span class="hljs-string">"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36"</span>
header = {
    <span class="hljs-comment"># "origin": "https://passport.mafengwo.cn",</span>
    <span class="hljs-string">"Referer"</span>: <span class="hljs-string">"https://passport.mafengwo.cn/"</span>,
    <span class="hljs-string">'User-Agent'</span>: userAgent,
}


<span class="hljs-comment"># 马蜂窝模仿 登录</span>
<span class="hljs-function"><span class="hljs-keyword">def</span> <span class="hljs-title">mafengwoLogin</span><span class="hljs-params">(account, password)</span>:</span>
    print(<span class="hljs-string">"开始模拟登录马蜂窝"</span>)
    postUrl = <span class="hljs-string">"https://passport.mafengwo.cn/login/"</span>
    postData = {
        <span class="hljs-string">"passport"</span>: account,
        <span class="hljs-string">"password"</span>: password,
    }
    <span class="hljs-comment"># 使用session直接post请求</span>
    responseRes = mafengwoSession.post(postUrl, data = postData, headers = header)
    <span class="hljs-comment"># 无论是否登录成功，状态码一般都是 statusCode = 200</span>
    print(f<span class="hljs-string">"statusCode = {responseRes.status_code}"</span>)
    print(f<span class="hljs-string">"text = {responseRes.text}"</span>)
    <span class="hljs-comment"># 登录成功之后，将cookie保存在本地文件中，好处是，以后再去获取马蜂窝首页的时候，就不需要再走mafengwoLogin的流程了，因为已经从文件中拿到cookie了</span>
    mafengwoSession.cookies.save()


<span class="hljs-comment"># 通过访问个人中心页面的返回状态码来判断是否为登录状态</span>
<span class="hljs-function"><span class="hljs-keyword">def</span> <span class="hljs-title">isLoginStatus</span><span class="hljs-params">()</span>:</span>
    routeUrl = <span class="hljs-string">"http://www.mafengwo.cn/plan/route.php"</span>
    <span class="hljs-comment"># 下面有两个关键点</span>
        <span class="hljs-comment"># 第一个是header，如果不设置，会返回500的错误</span>
        <span class="hljs-comment"># 第二个是allow_redirects，如果不设置，session访问时，服务器返回302，</span>
        <span class="hljs-comment"># 然后session会自动重定向到登录页面，获取到登录页面之后，变成200的状态码</span>
        <span class="hljs-comment"># allow_redirects = False  就是不允许重定向</span>
    responseRes = mafengwoSession.get(routeUrl, headers = header, allow_redirects = <span class="hljs-keyword">False</span>)
    print(f<span class="hljs-string">"isLoginStatus = {responseRes.status_code}"</span>)
    <span class="hljs-keyword">if</span> responseRes.status_code != <span class="hljs-number">200</span>:
        <span class="hljs-keyword">return</span> <span class="hljs-keyword">False</span>
    <span class="hljs-keyword">else</span>:
        <span class="hljs-keyword">return</span> <span class="hljs-keyword">True</span>


<span class="hljs-keyword">if</span> __name__ == <span class="hljs-string">"__main__"</span>:
    <span class="hljs-comment"># 第一步：尝试使用已有的cookie登录</span>
    mafengwoSession.cookies.load()
    isLogin = isLoginStatus()
    print(f<span class="hljs-string">"is login mafengwo = {isLogin}"</span>)
    <span class="hljs-keyword">if</span> isLogin == <span class="hljs-keyword">False</span>:
        <span class="hljs-comment"># 第二步：如果cookie已经失效了，那就尝试用帐号登录</span>
        print(f<span class="hljs-string">"cookie失效，用户重新登录..."</span>)
        mafengwoLogin(<span class="hljs-string">"13756567832"</span>, <span class="hljs-string">"000000001"</span>)

    resp = mafengwoSession.get(<span class="hljs-string">"http://www.mafengwo.cn/plan/fav_type.php"</span>, headers = header, allow_redirects = <span class="hljs-keyword">False</span>)
    print(f<span class="hljs-string">"resp.status = {resp.status_code}"</span>)
</code></pre>



<pre class="prettyprint"><code class=" hljs r"><span class="hljs-comment"># 第一次运行程序的输出：</span>
<span class="hljs-comment"># 由于第一次还没有生成cookie，所以需要用账户登录一次</span>

user cookielib <span class="hljs-keyword">in</span> python3.
isLoginStatus = <span class="hljs-number">302</span>
is login mafengwo = False
cookie失效，用户重新登录<span class="hljs-keyword">...</span>
开始模拟登录马蜂窝
statusCode = <span class="hljs-number">200</span>
……………………
resp.status = <span class="hljs-number">200</span></code></pre>



<pre class="prettyprint"><code class=" hljs python"><span class="hljs-comment"># 第二次运行程序的输出：</span>
<span class="hljs-comment"># 第二次，就直接使用cookie登录了，不再需要使用帐号登录</span>

user cookielib <span class="hljs-keyword">in</span> python3.
isLoginStatus = <span class="hljs-number">200</span>
<span class="hljs-keyword">is</span> login mafengwo = <span class="hljs-keyword">True</span>
resp.status = <span class="hljs-number">200</span></code></pre>            </div>
						<link href="https://csdnimg.cn/release/phoenix/mdeditor/markdown_views-df60374684.css" rel="stylesheet">
                </div>
	</article>
</div>
  <div class="hide-article-box hide-article-pos text-center">
    <div class="border"></div>
        <a class="btn article-footer-btn" id="btn-readmore" data-track-view='{"mod":"popu_376","con":",https://blog.csdn.net/zwq912318834/article/details/79571110,"}' data-track-click='{"mod":"popu_376","con":",https://blog.csdn.net/zwq912318834/article/details/79571110,"}'>阅读更多</a>
        <a class="btn article-footer-btn article-footer-bookmark-btn" >
      <svg class="icon no-active hover-hide" aria-hidden="true">
        <use xlink:href="#csdnc-bookmark"></use>
      </svg>
      <span>收藏</span>
    </a>
    <div class="btn article-footer-btn  bds_weixin article-footer-share-btn" data-cmd="weixin" title="分享">
      <svg class="icon no-active hover-hide" aria-hidden="true">
        <use xlink:href="#csdnc-share"></use>
      </svg>
      <span>分享</span>
      <div class="bdsharebuttonbox">
        <a href="#"class="bds_weixin clear-share-style-article-footer" data-cmd="weixin" title="分享"></a>
      </div>
    </div>
    
  </div>
  <script>
  (function(){
    function collection(){
      if (currentUserName) {
        if (!$(this).hasClass("liked")) {
          $.ajax({
            url: 'https://my.csdn.net/my/favorite/do_add/2',
            dataType: 'json',
            type: 'get',
            xhrFields: {
              withCredentials: true
            },
            crossDomain: true,
            data: {
              title: articleTit,
              url: curentUrl,
              share: 1,
              map_name: ''
            },
            success: function(data) {
              if (data.succ == 1) {
                $('.btn-bookmark').addClass("liked");
                $('.article-footer-bookmark-btn').addClass("liked").children('span').text('已收藏');
                
                alert('收藏成功,可以在个人中心查看我的收藏');
              } else {
                if (data.msg === "您已经收藏过") {
                  $('.btn-bookmark').addClass("liked");
                  $('.article-footer-bookmark-btn').addClass("liked").children('span').text('已收藏');
                }
                alert(data.msg);
              }
            }
          });
        } else {
          alert('您已经收藏过');
        }
      } else {
        window.csdn.loginBox.show();
      }
    }
    window.csdn = window.csdn ? window.csdn : {};
    window.csdn.articleCollection = collection;
    function setArticleH(btnReadmore,posi){
      var winH = $(window).height();
      var articleBox = $("div.article_content");
      var artH = articleBox.height();
      if(artH > winH*posi){
        articleBox.css({
          'height':winH*posi+'px',
          'overflow':'hidden'
        })
        btnReadmore.click(function(){
          articleBox.removeAttr("style");
          $(this).hide().parent().addClass('hide-article-style');
        })
      }else{
        btnReadmore.hide().parent().addClass('hide-article-style');
      }
    }
    var btnReadmore = $("#btn-readmore");
    $('.article-footer-bookmark-btn').click(window.csdn.articleCollection)
    if(btnReadmore.length>0){
      if(currentUserName){
        setArticleH(btnReadmore,3);
      }else{
        setArticleH(btnReadmore,1.2);
      }
    }else{
      $('.hide-article-box').addClass('hide-article-style');
    }
  })()
</script>
<script>
		$(".MathJax").remove();
		if($('div.markdown_views pre.prettyprint code.hljs').length > 0 ){
				$('div.markdown_views')[0].className = 'markdown_views';
		}
</script>
        <div class="t0 clearfix">
														<div class="content">
															<a href="https://blog.csdn.net/c406495762/article/details/69817490" target="_blank" title="<em>Python3</em>网络爬虫(六)：<em>Python3</em><em>使用</em>Cookie-<em>模拟</em>登陆获取妹子联系方式" data-track-view='{"mod":"popu_642","con": ",https://blog.csdn.net/c406495762/article/details/69817490,"}' data-track-click='{"mod":"popu_642","con": ",https://blog.csdn.net/c406495762/article/details/69817490,"}'>
															<h4 class="text-truncate oneline"><em>Python3</em>网络爬虫(六)：<em>Python3</em><em>使用</em>Cookie-<em>模拟</em>登陆获取妹子联系方式</h4>
															<div class="info-box d-flex align-content-center">
																<p class="date-and-readNum">
																	<span class="date hover-show">04-09</span>
																	<span class="read-num hover-hide"><svg class="icon csdnc-yuedushu" aria-hidden="true"><use xlink:href="#csdnc-m-passwords-visible"></use></svg>6.6万</span>
																</p>
																</div>
															</a>
																<p class="content">
																	<a href="https://blog.csdn.net/c406495762/article/details/69817490" target="_blank" title="<em>Python3</em>网络爬虫(六)：<em>Python3</em><em>使用</em>Cookie-<em>模拟</em>登陆获取妹子联系方式" data-track-click='{"mod":"popu_642","con": ",https://blog.csdn.net/c406495762/article/details/69817490,"}'>
																		<span class="desc oneline">转载请注明作者和出处：http://blog.csdn.net/c406495762
运行平台：WindowsPython
版本：Python3.x
IDE：Sublime text3...</span>
																	</a>
											            <span class="blog_title_box oneline"><a target="_blank" href="https://blog.csdn.net/c406495762">来自：	<span class="blog_title"> c406495762</span></a></span>
											          </p>
														</div>
													</div>        <a id="commentBox"></a>
<div class="comment-box">
	
	<div class="comment-edit-box d-flex">
		<a id="commentsedit"></a>
		<div class="user-img">
			<a href="javascript:void(0);" target="_blank">
				<img class="show_loginbox" src="//g.csdnimg.cn/static/user-img/anonymous-User-img.png">
			</a>
		</div>
		<form id="commentform">
			<input type="hidden" id="comment_replyId">
			<textarea class="comment-content" name="comment_content" id="comment_content" placeholder="想对作者说点什么"></textarea>
			<div class="opt-box"> <!-- d-flex -->
				<div id="ubbtools" class="add_code">
					<a href="#insertcode" code="code" target="_self"><i class="icon iconfont icon-daima"></i></a>
				</div>
				<input type="hidden" id="comment_replyId" name="comment_replyId">
				<input type="hidden" id="comment_userId" name="comment_userId" value="">
				<input type="hidden" id="commentId" name="commentId" value="">
				<div style="display: none;" class="csdn-tracking-statistics tracking-click" data-mod="popu_384"><a href="#" target="_blank" class="comment_area_btn">发表评论</a></div>
				<div class="dropdown" id="myDrap">
					<a class="dropdown-face d-flex align-items-center" data-toggle="dropdown" role="button" aria-haspopup="true" aria-expanded="false">
					<div class="txt-selected text-truncate">添加代码片</div>
					<svg class="icon d-block" aria-hidden="true">
						<use xlink:href="#csdnc-triangledown"></use>
					</svg>
					</a>
					<ul class="dropdown-menu" id="commentCode" aria-labelledby="drop4">
						<li><a data-code="html">HTML/XML</a></li>
						<li><a data-code="objc">objective-c</a></li>
						<li><a data-code="ruby">Ruby</a></li>
						<li><a data-code="php">PHP</a></li>
						<li><a data-code="csharp">C</a></li>
						<li><a data-code="cpp">C++</a></li>
						<li><a data-code="javascript">JavaScript</a></li>
						<li><a data-code="python">Python</a></li>
						<li><a data-code="java">Java</a></li>
						<li><a data-code="css">CSS</a></li>
						<li><a data-code="sql">SQL</a></li>
						<li><a data-code="plain">其它</a></li>
					</ul>
				</div>  
				<div class="right-box">
					<span id="tip_comment" class="tip">还能输入<em>1000</em>个字符</span>
					<input type="submit" class="btn btn-sm btn-red btn-comment" value="发表评论">
				</div>
			</div>
		</form>
	</div>

		<div class="comment-list-container">
		<a id="comments"></a>
		<div class="comment-list-box">
		</div>
		<div id="commentPage" class="pagination-box d-none"></div>
		<div class="opt-box text-center">
			<button class="btn btn-sm btn-link-blue" id="btnMoreComment"></button>
		</div>
	</div>
</div>
        <div class="recommend-box">
            		<div class="recommend-item-box recommend-box-ident type_blog clearfix" data-track-view='{"mod":"popu_614","con":",https://blog.csdn.net/u010895119/article/details/80584842,BlogCommendFromBaidu_1"}' data-track-click='{"mod":"popu_614","con":",https://blog.csdn.net/u010895119/article/details/80584842,BlogCommendFromBaidu_1"}'>
			<div class="content">
				<a href="https://blog.csdn.net/u010895119/article/details/80584842" target="_blank" title="python3 requests 模拟登录状态的两种方式">
				<h4 class="text-truncate oneline">
						<em>python3</em> <em>requests</em> <em>模拟</em>登录状态的两种方式				</h4>
				<div class="info-box d-flex align-content-center">
					<!-- <p class="avatar">
							<img src="https://avatar.csdn.net/3/F/A/3_u010895119.jpg" alt="u010895119" class="avatar-pic">
							<span class="namebox">
								<span class="name">u010895119</span>
								<span class="triangle"></span>
							</span>
					</p> -->
					<p class="date-and-readNum">
						<span class="date hover-show">06-05</span>
						<span class="read-num hover-hide">
							<svg class="icon csdnc-yuedushu" aria-hidden="true">
								<use xlink:href="#csdnc-m-passwords-visible"></use>
							</svg>
							1748</span>
						</p>
					</div>
				</a>
					<p class="content">
						<a href="https://blog.csdn.net/u010895119/article/details/80584842" target="_blank" title="python3 requests 模拟登录状态的两种方式">
							<span class="desc oneline">模拟登录状态，即与cookie和session有关。 
cookie是用户登录后，服务器返回给客户端的，客户端保存cookie后，可以方便的进行登录；session是服务端用以鉴定用户是否处于登录状态...</span>
						</a>
                        						<span class="blog_title_box oneline"><a target="_blank" href="https://blog.csdn.net/u010895119">来自：	<span class="blog_title"> 小桔的博客</span></a></span>
                        					</p>
			</div>
					</div>
	
    
	    
    		<div class="recommend-item-box recommend-box-ident type_blog clearfix" data-track-view='{"mod":"popu_614","con":",https://blog.csdn.net/qq_41305167/article/details/80328135,BlogCommendFromBaidu_2"}' data-track-click='{"mod":"popu_614","con":",https://blog.csdn.net/qq_41305167/article/details/80328135,BlogCommendFromBaidu_2"}'>
			<div class="content">
				<a href="https://blog.csdn.net/qq_41305167/article/details/80328135" target="_blank" title="python3+selenium3 利用cookie实现模拟登陆">
				<h4 class="text-truncate oneline">
						<em>python3</em>+selenium3 利用cookie<em>实现</em><em>模拟</em>登陆				</h4>
				<div class="info-box d-flex align-content-center">
					<!-- <p class="avatar">
							<img src="https://avatar.csdn.net/8/9/4/3_qq_41305167.jpg" alt="qq_41305167" class="avatar-pic">
							<span class="namebox">
								<span class="name">qq_41305167</span>
								<span class="triangle"></span>
							</span>
					</p> -->
					<p class="date-and-readNum">
						<span class="date hover-show">05-15</span>
						<span class="read-num hover-hide">
							<svg class="icon csdnc-yuedushu" aria-hidden="true">
								<use xlink:href="#csdnc-m-passwords-visible"></use>
							</svg>
							618</span>
						</p>
					</div>
				</a>
					<p class="content">
						<a href="https://blog.csdn.net/qq_41305167/article/details/80328135" target="_blank" title="python3+selenium3 利用cookie实现模拟登陆">
							<span class="desc oneline">学习材料来源：https://www.cnblogs.com/fnng/p/6431484.html本文章基于以上教程的操作工具：python3.6.5          selenium3.11.0...</span>
						</a>
                        						<span class="blog_title_box oneline"><a target="_blank" href="https://blog.csdn.net/qq_41305167">来自：	<span class="blog_title"> qq_41305167的博客</span></a></span>
                        					</p>
			</div>
					</div>
	
    
	    
    		<div class="recommend-item-box recommend-box-ident type_blog clearfix" data-track-view='{"mod":"popu_614","con":",https://blog.csdn.net/xc_zhou/article/details/80647166,BlogCommendFromBaidu_3"}' data-track-click='{"mod":"popu_614","con":",https://blog.csdn.net/xc_zhou/article/details/80647166,BlogCommendFromBaidu_3"}'>
			<div class="content">
				<a href="https://blog.csdn.net/xc_zhou/article/details/80647166" target="_blank" title="Python3 模拟登录知乎（requests）">
				<h4 class="text-truncate oneline">
						<em>Python3</em> <em>模拟</em>登录知乎（<em>requests</em>）				</h4>
				<div class="info-box d-flex align-content-center">
					<!-- <p class="avatar">
							<img src="https://avatar.csdn.net/1/D/5/3_xc_zhou.jpg" alt="xc_zhou" class="avatar-pic">
							<span class="namebox">
								<span class="name">xc_zhou</span>
								<span class="triangle"></span>
							</span>
					</p> -->
					<p class="date-and-readNum">
						<span class="date hover-show">06-11</span>
						<span class="read-num hover-hide">
							<svg class="icon csdnc-yuedushu" aria-hidden="true">
								<use xlink:href="#csdnc-m-passwords-visible"></use>
							</svg>
							453</span>
						</p>
					</div>
				</a>
					<p class="content">
						<a href="https://blog.csdn.net/xc_zhou/article/details/80647166" target="_blank" title="Python3 模拟登录知乎（requests）">
							<span class="desc oneline"># -*- coding: utf-8 -*-

&amp;quot;&amp;quot;&amp;quot; 知乎登录分为两种登录
    一是手机登录 API : https://www.zhihu.com/login/...</span>
						</a>
                        						<span class="blog_title_box oneline"><a target="_blank" href="https://blog.csdn.net/xc_zhou">来自：	<span class="blog_title"> 周小董</span></a></span>
                        					</p>
			</div>
					</div>
	
    <div class="recommend-item-box recommend-ad-box"><div id="kp_box_59" data-pid="59" data-track-view='{"mod":"kp_popu_59-517","con":",,"}' data-track-click='{"mod":"kp_popu_59-517","con":",,"}'><div id="three_ad1" class="mediav_ad" ></div>
<script type="text/javascript" src="//static.mediav.com/js/mvf_news_feed.js"></script>
<script>
                                               NEWS_FEED({
                w: 852,
                h : 52,
                showid : 'GNKXx7',
                placeholderId: "three_ad1",
                inject : 'define',
                define : {
                    imagePosition : 'left',
                    imageBorderRadius : 3,
                    imageWidth: 90,
                    imageHeight: 52,
                    imageFill : 'clip',
                    displayImage : true,
                    displayTitle : true,
                    titleFontSize: 18,
                    titleFontColor: '#000',
                    titleFontFamily : 'Lato,-apple-system,SF UI Text,Arial,PingFang SC,Hiragino Sans GB,Microsoft YaHei,WenQuanYi Micro Hei,sans-serif',
                    titleFontWeight: 'bold',
                    titlePaddingTop : 0,
                    titlePaddingRight : 0,
                    titlePaddingBottom : 5,
                    titlePaddingLeft : 16,
                    displayDesc : true,
                    descFontSize: 14,
                    descFontColor: '#8e959a',
                    descFontFamily : 'Microsoft Yahei',
                    paddingTop : 0,
                    paddingRight : 0,
                    paddingBottom : 0,
                    paddingLeft : 0,
                    backgroundColor: '#fff',
                    hoverColor: '#000'
                      }
                  })
                                        </script></div></div>
	    
    		<div class="recommend-item-box recommend-box-ident type_blog clearfix" data-track-view='{"mod":"popu_614","con":",https://blog.csdn.net/qq_31927785/article/details/78341028,BlogCommendFromBaidu_4"}' data-track-click='{"mod":"popu_614","con":",https://blog.csdn.net/qq_31927785/article/details/78341028,BlogCommendFromBaidu_4"}'>
			<div class="content">
				<a href="https://blog.csdn.net/qq_31927785/article/details/78341028" target="_blank" title="Python3网络爬虫(3)：Python3使用Cookie-模拟登陆">
				<h4 class="text-truncate oneline">
						<em>Python3</em>网络爬虫(3)：<em>Python3</em><em>使用</em>Cookie-<em>模拟</em>登陆				</h4>
				<div class="info-box d-flex align-content-center">
					<!-- <p class="avatar">
							<img src="https://avatar.csdn.net/6/4/E/3_qq_31927785.jpg" alt="qq_31927785" class="avatar-pic">
							<span class="namebox">
								<span class="name">qq_31927785</span>
								<span class="triangle"></span>
							</span>
					</p> -->
					<p class="date-and-readNum">
						<span class="date hover-show">10-25</span>
						<span class="read-num hover-hide">
							<svg class="icon csdnc-yuedushu" aria-hidden="true">
								<use xlink:href="#csdnc-m-passwords-visible"></use>
							</svg>
							1793</span>
						</p>
					</div>
				</a>
					<p class="content">
						<a href="https://blog.csdn.net/qq_31927785/article/details/78341028" target="_blank" title="Python3网络爬虫(3)：Python3使用Cookie-模拟登陆">
							<span class="desc oneline">Python版本：Python3.xIDE：Mac ,Pycharm一、为什么要使用CookieCookie，指某些网站为了辨别用户身份、进行session跟踪而储存在用户本地终端上的数据（通常经过加...</span>
						</a>
                        						<span class="blog_title_box oneline"><a target="_blank" href="https://blog.csdn.net/qq_31927785">来自：	<span class="blog_title"> KEELON的博客</span></a></span>
                        					</p>
			</div>
					</div>
	
    
	    
    		<div class="recommend-item-box recommend-box-ident type_blog clearfix" data-track-view='{"mod":"popu_614","con":",https://blog.csdn.net/weixin_39099836/article/details/78388688,BlogCommendFromBaidu_5"}' data-track-click='{"mod":"popu_614","con":",https://blog.csdn.net/weixin_39099836/article/details/78388688,BlogCommendFromBaidu_5"}'>
			<div class="content">
				<a href="https://blog.csdn.net/weixin_39099836/article/details/78388688" target="_blank" title="Python3_模拟登录">
				<h4 class="text-truncate oneline">
						<em>Python3</em>_<em>模拟</em>登录				</h4>
				<div class="info-box d-flex align-content-center">
					<!-- <p class="avatar">
							<img src="https://avatar.csdn.net/E/2/E/3_weixin_39099836.jpg" alt="weixin_39099836" class="avatar-pic">
							<span class="namebox">
								<span class="name">weixin_39099836</span>
								<span class="triangle"></span>
							</span>
					</p> -->
					<p class="date-and-readNum">
						<span class="date hover-show">10-29</span>
						<span class="read-num hover-hide">
							<svg class="icon csdnc-yuedushu" aria-hidden="true">
								<use xlink:href="#csdnc-m-passwords-visible"></use>
							</svg>
							398</span>
						</p>
					</div>
				</a>
					<p class="content">
						<a href="https://blog.csdn.net/weixin_39099836/article/details/78388688" target="_blank" title="Python3_模拟登录">
							<span class="desc oneline">模拟登录_要求：


1. 用户输入账号密码进行登录
2. 用户信息保存在文件内

3. 用户密码输入错误三次后锁定用户


逻辑图：











...</span>
						</a>
                        						<span class="blog_title_box oneline"><a target="_blank" href="https://blog.csdn.net/weixin_39099836">来自：	<span class="blog_title"> weixin_39099836的博客</span></a></span>
                        					</p>
			</div>
					</div>
	
    
	    
    		<div class="recommend-item-box recommend-box-ident type_blog clearfix" data-track-view='{"mod":"popu_614","con":",https://blog.csdn.net/sinat_31211873/article/details/52200220,BlogCommendFromBaidu_6"}' data-track-click='{"mod":"popu_614","con":",https://blog.csdn.net/sinat_31211873/article/details/52200220,BlogCommendFromBaidu_6"}'>
			<div class="content">
				<a href="https://blog.csdn.net/sinat_31211873/article/details/52200220" target="_blank" title="Python3爬虫学习笔记1.2——模拟登录">
				<h4 class="text-truncate oneline">
						<em>Python3</em>爬虫学习笔记1.2——<em>模拟</em>登录				</h4>
				<div class="info-box d-flex align-content-center">
					<!-- <p class="avatar">
							<img src="https://avatar.csdn.net/C/7/A/3_sinat_31211873.jpg" alt="sinat_31211873" class="avatar-pic">
							<span class="namebox">
								<span class="name">sinat_31211873</span>
								<span class="triangle"></span>
							</span>
					</p> -->
					<p class="date-and-readNum">
						<span class="date hover-show">08-13</span>
						<span class="read-num hover-hide">
							<svg class="icon csdnc-yuedushu" aria-hidden="true">
								<use xlink:href="#csdnc-m-passwords-visible"></use>
							</svg>
							4859</span>
						</p>
					</div>
				</a>
					<p class="content">
						<a href="https://blog.csdn.net/sinat_31211873/article/details/52200220" target="_blank" title="Python3爬虫学习笔记1.2——模拟登录">
							<span class="desc oneline">欢迎捧场，上一篇我们学习了urllib官方库的一些使用方法，今天的主要工作内容是利用Python来模拟登录网站，我们选择用知乎做实验。PS：知乎有毒。...</span>
						</a>
                        						<span class="blog_title_box oneline"><a target="_blank" href="https://blog.csdn.net/sinat_31211873">来自：	<span class="blog_title"> 王凯盛的博客</span></a></span>
                        					</p>
			</div>
					</div>
	
    
	    
    		<div class="recommend-item-box recommend-box-ident type_blog clearfix" data-track-view='{"mod":"popu_614","con":",https://blog.csdn.net/pipisorry/article/details/47948065,BlogCommendFromBaidu_7"}' data-track-click='{"mod":"popu_614","con":",https://blog.csdn.net/pipisorry/article/details/47948065,BlogCommendFromBaidu_7"}'>
			<div class="content">
				<a href="https://blog.csdn.net/pipisorry/article/details/47948065" target="_blank" title="python3爬虫 - cookie登录实战">
				<h4 class="text-truncate oneline">
						<em>python3</em>爬虫 - cookie登录实战				</h4>
				<div class="info-box d-flex align-content-center">
					<!-- <p class="avatar">
							<img src="https://avatar.csdn.net/5/5/8/3_pipisorry.jpg" alt="pipisorry" class="avatar-pic">
							<span class="namebox">
								<span class="name">pipisorry</span>
								<span class="triangle"></span>
							</span>
					</p> -->
					<p class="date-and-readNum">
						<span class="date hover-show">08-24</span>
						<span class="read-num hover-hide">
							<svg class="icon csdnc-yuedushu" aria-hidden="true">
								<use xlink:href="#csdnc-m-passwords-visible"></use>
							</svg>
							3.6万</span>
						</p>
					</div>
				</a>
					<p class="content">
						<a href="https://blog.csdn.net/pipisorry/article/details/47948065" target="_blank" title="python3爬虫 - cookie登录实战">
							<span class="desc oneline">http://blog.csdn.net/pipisorry/article/details/47948065

实战1：使用cookie登录哈工大ACM网站
获取网站登录地址
http://acm....</span>
						</a>
                        						<span class="blog_title_box oneline"><a target="_blank" href="https://blog.csdn.net/pipisorry">来自：	<span class="blog_title"> 皮皮blog</span></a></span>
                        					</p>
			</div>
					</div>
	
    
	    
    		<div class="recommend-item-box recommend-box-ident type_blog clearfix" data-track-view='{"mod":"popu_614","con":",https://blog.csdn.net/spynao/article/details/50374291,BlogCommendFromBaidu_8"}' data-track-click='{"mod":"popu_614","con":",https://blog.csdn.net/spynao/article/details/50374291,BlogCommendFromBaidu_8"}'>
			<div class="content">
				<a href="https://blog.csdn.net/spynao/article/details/50374291" target="_blank" title="python--python3爬虫之模拟登录知乎">
				<h4 class="text-truncate oneline">
						python--<em>python3</em>爬虫之<em>模拟</em>登录知乎				</h4>
				<div class="info-box d-flex align-content-center">
					<!-- <p class="avatar">
							<img src="https://avatar.csdn.net/D/D/9/3_spynao.jpg" alt="spynao" class="avatar-pic">
							<span class="namebox">
								<span class="name">spynao</span>
								<span class="triangle"></span>
							</span>
					</p> -->
					<p class="date-and-readNum">
						<span class="date hover-show">12-21</span>
						<span class="read-num hover-hide">
							<svg class="icon csdnc-yuedushu" aria-hidden="true">
								<use xlink:href="#csdnc-m-passwords-visible"></use>
							</svg>
							5150</span>
						</p>
					</div>
				</a>
					<p class="content">
						<a href="https://blog.csdn.net/spynao/article/details/50374291" target="_blank" title="python--python3爬虫之模拟登录知乎">
							<span class="desc oneline">代码在python3环境下测试通过：
from bs4 import BeautifulSoup
import requests


url = 'http://www.zhihu.com'
logi...</span>
						</a>
                        						<span class="blog_title_box oneline"><a target="_blank" href="https://blog.csdn.net/spynao">来自：	<span class="blog_title"> 木天</span></a></span>
                        					</p>
			</div>
					</div>
	
    <div class="recommend-item-box recommend-ad-box"><div id="kp_box_60" data-pid="60" data-track-view='{"mod":"kp_popu_60-43","con":",,"}' data-track-click='{"mod":"kp_popu_60-43","con":",,"}'><div id="three_ad8" class="mediav_ad" ></div>
<script type="text/javascript" src="//static.mediav.com/js/mvf_news_feed.js"></script>
<script>
                                               NEWS_FEED({
                w: 900,
                h : 84,
                showid : 'Afihld',
                placeholderId: "three_ad8",
                inject : 'define',
                define : {
                    imagePosition : 'left',
                    imageBorderRadius : 3,
                    imageWidth: 90,
                    imageHeight: 60,
                    imageFill : 'clip',
                    displayImage : true,
                    displayTitle : true,
                    titleFontSize: 18,
                    titleFontColor: '#000',
                    titleFontFamily : 'Lato,-apple-system,SF UI Text,Arial,PingFang SC,Hiragino Sans GB,Microsoft YaHei,WenQuanYi Micro Hei,sans-serif',
                    titleFontWeight: 'bold',
                    titlePaddingTop : 0,
                    titlePaddingRight : 0,
                    titlePaddingBottom : 5,
                    titlePaddingLeft : 16,
                    displayDesc : true,
                    descFontSize: 14,
                    descFontColor: '#8e959a',
                    descFontFamily : 'Microsoft Yahei',
                    paddingTop : 10,
                    paddingRight : 0,
                    paddingBottom : 0,
                    paddingLeft : 0,
                    backgroundColor: '#fff',
                    hoverColor: '#000'
                      }
                  })
                                        </script></div></div>
	    
    		<div class="recommend-item-box recommend-box-ident type_blog clearfix" data-track-view='{"mod":"popu_614","con":",https://blog.csdn.net/liuyanhuasd/article/details/80148291,BlogCommendFromBaidu_9"}' data-track-click='{"mod":"popu_614","con":",https://blog.csdn.net/liuyanhuasd/article/details/80148291,BlogCommendFromBaidu_9"}'>
			<div class="content">
				<a href="https://blog.csdn.net/liuyanhuasd/article/details/80148291" target="_blank" title="Python模拟登录的几种方法">
				<h4 class="text-truncate oneline">
						Python<em>模拟</em>登录的几种方法				</h4>
				<div class="info-box d-flex align-content-center">
					<!-- <p class="avatar">
							<img src="https://avatar.csdn.net/0/B/2/3_liuyanhuasd.jpg" alt="liuyanhuasd" class="avatar-pic">
							<span class="namebox">
								<span class="name">liuyanhuasd</span>
								<span class="triangle"></span>
							</span>
					</p> -->
					<p class="date-and-readNum">
						<span class="date hover-show">04-30</span>
						<span class="read-num hover-hide">
							<svg class="icon csdnc-yuedushu" aria-hidden="true">
								<use xlink:href="#csdnc-m-passwords-visible"></use>
							</svg>
							638</span>
						</p>
					</div>
				</a>
					<p class="content">
						<a href="https://blog.csdn.net/liuyanhuasd/article/details/80148291" target="_blank" title="Python模拟登录的几种方法">
							<span class="desc oneline">目录方法一：直接使用已知的cookie访问方法二：模拟登录后再携带得到的cookie访问方法三：模拟登录后用session保持登录状态方法四：使用无头浏览器访问 正文方法一：直接使用已知的cookie...</span>
						</a>
                        						<span class="blog_title_box oneline"><a target="_blank" href="https://blog.csdn.net/liuyanhuasd">来自：	<span class="blog_title"> liuyanhuasd的博客</span></a></span>
                        					</p>
			</div>
					</div>
	
    
			<div class="recommend-item-box type_hot_word">
						<div class="content clearfix oneline">
				<h5 class="float-left">文章热词</h5>
				<div class="word float-left">
													<span>
						<a href="https://edu.csdn.net/course/play/5599/109090 " target="_blank">
						双目视觉基础					</a></span>
																	<span>
						<a href="https://edu.csdn.net/courses/o391_s396_k " target="_blank">
						算法基础					</a></span>
																	<span>
						<a href="https://edu.csdn.net/course/play/8562/176218 " target="_blank">
						python基础					</a></span>
																	<span>
						<a href="https://edu.csdn.net/combos/o391_s396_l0_t " target="_blank">
						算法基础学习					</a></span>
																	<span>
						<a href="https://edu.csdn.net/courses/o391_s396_k " target="_blank">
						算法基础课程					</a></span>
												</div>
			</div>
								</div>
	    
    		<div class="recommend-item-box recommend-box-ident type_blog clearfix" data-track-view='{"mod":"popu_614","con":",https://blog.csdn.net/qq_33988065/article/details/80958130,BlogCommendClickRateRank_10"}' data-track-click='{"mod":"popu_614","con":",https://blog.csdn.net/qq_33988065/article/details/80958130,BlogCommendClickRateRank_10"}'>
			<div class="content">
				<a href="https://blog.csdn.net/qq_33988065/article/details/80958130" target="_blank" title="使用request模拟登录开源中国">
				<h4 class="text-truncate oneline">
						<em>使用</em>request<em>模拟</em>登录开源中国				</h4>
				<div class="info-box d-flex align-content-center">
					<!-- <p class="avatar">
							<img src="https://avatar.csdn.net/3/5/7/3_qq_33988065.jpg" alt="qq_33988065" class="avatar-pic">
							<span class="namebox">
								<span class="name">qq_33988065</span>
								<span class="triangle"></span>
							</span>
					</p> -->
					<p class="date-and-readNum">
						<span class="date hover-show">07-08</span>
						<span class="read-num hover-hide">
							<svg class="icon csdnc-yuedushu" aria-hidden="true">
								<use xlink:href="#csdnc-m-passwords-visible"></use>
							</svg>
							195</span>
						</p>
					</div>
				</a>
					<p class="content">
						<a href="https://blog.csdn.net/qq_33988065/article/details/80958130" target="_blank" title="使用request模拟登录开源中国">
							<span class="desc oneline">源码

const CryptoJS = require('crypto-jS');
const request = require('request');
const cheerio = requi...</span>
						</a>
                        						<span class="blog_title_box oneline"><a target="_blank" href="https://blog.csdn.net/qq_33988065">来自：	<span class="blog_title"> 花神的博客</span></a></span>
                        					</p>
			</div>
					</div>
	
    
	          <div class="recommend-item-box blog-expert-recommend-box">
				<div class="d-flex">
					<div class="blog-expert-recommend">
						<div class="blog-expert">
							<div class="blog-expert-flexbox"></div>
						</div>
					</div>
				</div>
      </div>
    
    		<div class="recommend-item-box recommend-box-ident type_blog clearfix" data-track-view='{"mod":"popu_614","con":",https://blog.csdn.net/python_huohuo/article/details/82985980,BlogCommendClickRateRank_11"}' data-track-click='{"mod":"popu_614","con":",https://blog.csdn.net/python_huohuo/article/details/82985980,BlogCommendClickRateRank_11"}'>
			<div class="content">
				<a href="https://blog.csdn.net/python_huohuo/article/details/82985980" target="_blank" title="Python3下模拟登录知乎">
				<h4 class="text-truncate oneline">
						<em>Python3</em>下<em>模拟</em>登录知乎				</h4>
				<div class="info-box d-flex align-content-center">
					<!-- <p class="avatar">
							<img src="https://avatar.csdn.net/3/A/6/3_python_huohuo.jpg" alt="python_huohuo" class="avatar-pic">
							<span class="namebox">
								<span class="name">python_huohuo</span>
								<span class="triangle"></span>
							</span>
					</p> -->
					<p class="date-and-readNum">
						<span class="date hover-show">10-09</span>
						<span class="read-num hover-hide">
							<svg class="icon csdnc-yuedushu" aria-hidden="true">
								<use xlink:href="#csdnc-m-passwords-visible"></use>
							</svg>
							262</span>
						</p>
					</div>
				</a>
					<p class="content">
						<a href="https://blog.csdn.net/python_huohuo/article/details/82985980" target="_blank" title="Python3下模拟登录知乎">
							<span class="desc oneline">代码：


# -*- coding:UTF-8 -*-

import  requests , time
import  hmac ,json
from bs4 import BeautifulSo...</span>
						</a>
                        						<span class="blog_title_box oneline"><a target="_blank" href="https://blog.csdn.net/python_huohuo">来自：	<span class="blog_title"> python_huohuo的博客</span></a></span>
                        					</p>
			</div>
					</div>
	
    
	    
    		<div class="recommend-item-box recommend-box-ident type_blog clearfix" data-track-view='{"mod":"popu_614","con":",https://blog.csdn.net/weixin_39452320/article/details/81124393,BlogCommendESEnWordWeight_12"}' data-track-click='{"mod":"popu_614","con":",https://blog.csdn.net/weixin_39452320/article/details/81124393,BlogCommendESEnWordWeight_12"}'>
			<div class="content">
				<a href="https://blog.csdn.net/weixin_39452320/article/details/81124393" target="_blank" title="webgl第六课-通过鼠标点击绘点">
				<h4 class="text-truncate oneline">
						webgl第六课-通过鼠标点击绘点				</h4>
				<div class="info-box d-flex align-content-center">
					<!-- <p class="avatar">
							<img src="https://avatar.csdn.net/7/2/C/3_weixin_39452320.jpg" alt="weixin_39452320" class="avatar-pic">
							<span class="namebox">
								<span class="name">weixin_39452320</span>
								<span class="triangle"></span>
							</span>
					</p> -->
					<p class="date-and-readNum">
						<span class="date hover-show">07-22</span>
						<span class="read-num hover-hide">
							<svg class="icon csdnc-yuedushu" aria-hidden="true">
								<use xlink:href="#csdnc-m-passwords-visible"></use>
							</svg>
							869</span>
						</p>
					</div>
				</a>
					<p class="content">
						<a href="https://blog.csdn.net/weixin_39452320/article/details/81124393" target="_blank" title="webgl第六课-通过鼠标点击绘点">
							<span class="desc oneline">需要源码可以Q群：828202939 或者点击这里  希望可以和大家一起学习、一起进步！！纯手打！！

首先我们需要知道要绘制一个点，大致需要哪些步骤：

1.初始化着色器

2.获取attribut...</span>
						</a>
                        						<span class="blog_title_box oneline"><a target="_blank" href="https://blog.csdn.net/weixin_39452320">来自：	<span class="blog_title"> 谷子的博客</span></a></span>
                        					</p>
			</div>
					</div>
	
    
	    
    		<div class="recommend-item-box recommend-box-ident type_blog clearfix" data-track-view='{"mod":"popu_614","con":",https://blog.csdn.net/JavaLixy/article/details/78010318,BlogCommendESEnWordWeight_13"}' data-track-click='{"mod":"popu_614","con":",https://blog.csdn.net/JavaLixy/article/details/78010318,BlogCommendESEnWordWeight_13"}'>
			<div class="content">
				<a href="https://blog.csdn.net/JavaLixy/article/details/78010318" target="_blank" title="python3模拟登录知乎">
				<h4 class="text-truncate oneline">
						<em>python3</em><em>模拟</em>登录知乎				</h4>
				<div class="info-box d-flex align-content-center">
					<!-- <p class="avatar">
							<img src="https://avatar.csdn.net/8/1/9/3_javalixy.jpg" alt="JavaLixy" class="avatar-pic">
							<span class="namebox">
								<span class="name">JavaLixy</span>
								<span class="triangle"></span>
							</span>
					</p> -->
					<p class="date-and-readNum">
						<span class="date hover-show">09-17</span>
						<span class="read-num hover-hide">
							<svg class="icon csdnc-yuedushu" aria-hidden="true">
								<use xlink:href="#csdnc-m-passwords-visible"></use>
							</svg>
							5850</span>
						</p>
					</div>
				</a>
					<p class="content">
						<a href="https://blog.csdn.net/JavaLixy/article/details/78010318" target="_blank" title="python3模拟登录知乎">
							<span class="desc oneline">1，前言
  在爬虫的世界里，模拟登录是一项必备的技能，很多网站登录才能有浏览信息的权限，今天就在python来模拟登录知乎


2，获取登录时post的参数
   在网页上输入知乎的url：http...</span>
						</a>
                        						<span class="blog_title_box oneline"><a target="_blank" href="https://blog.csdn.net/JavaLixy">来自：	<span class="blog_title"> oldbig_lin的博客</span></a></span>
                        					</p>
			</div>
					</div>
	
    <div class="recommend-item-box recommend-ad-box"><script type="text/javascript" src="//rabc1.iteye.com/production/res/rxjg.js?pkcgstj=jm"></script></div>
	    
    		<div class="recommend-item-box recommend-box-ident type_blog clearfix" data-track-view='{"mod":"popu_614","con":",https://blog.csdn.net/zwq912318834/article/details/79665863,BlogCommendESEnWordWeight_14"}' data-track-click='{"mod":"popu_614","con":",https://blog.csdn.net/zwq912318834/article/details/79665863,BlogCommendESEnWordWeight_14"}'>
			<div class="content">
				<a href="https://blog.csdn.net/zwq912318834/article/details/79665863" target="_blank" title="python3下使用requests模拟用户登录 —— 中级篇（百度云俱乐部）">
				<h4 class="text-truncate oneline">
						<em>python3</em>下<em>使用</em><em>requests</em><em>模拟</em><em>用户登录</em> —— 中级篇（百度云俱乐部）				</h4>
				<div class="info-box d-flex align-content-center">
					<!-- <p class="avatar">
							<img src="https://avatar.csdn.net/7/4/8/3_zwq912318834.jpg" alt="zwq912318834" class="avatar-pic">
							<span class="namebox">
								<span class="name">zwq912318834</span>
								<span class="triangle"></span>
							</span>
					</p> -->
					<p class="date-and-readNum">
						<span class="date hover-show">03-23</span>
						<span class="read-num hover-hide">
							<svg class="icon csdnc-yuedushu" aria-hidden="true">
								<use xlink:href="#csdnc-m-passwords-visible"></use>
							</svg>
							2341</span>
						</p>
					</div>
				</a>
					<p class="content">
						<a href="https://blog.csdn.net/zwq912318834/article/details/79665863" target="_blank" title="python3下使用requests模拟用户登录 —— 中级篇（百度云俱乐部）">
							<span class="desc oneline">python3下使用requests模拟用户登录 —— 中级篇（百度云俱乐部）



1. 背景


建议先看一下初级篇，了解一些爬虫模拟登录的基本常识： 
python3下使用requests实现模...</span>
						</a>
                        						<span class="blog_title_box oneline"><a target="_blank" href="https://blog.csdn.net/zwq912318834">来自：	<span class="blog_title"> Kosmoo的博客</span></a></span>
                        					</p>
			</div>
					</div>
	
    
	    
    		<div class="recommend-item-box recommend-box-ident type_blog clearfix" data-track-view='{"mod":"popu_614","con":",https://blog.csdn.net/kk185800961/article/details/78739988,BlogCommendESEnWordWeight_15"}' data-track-click='{"mod":"popu_614","con":",https://blog.csdn.net/kk185800961/article/details/78739988,BlogCommendESEnWordWeight_15"}'>
			<div class="content">
				<a href="https://blog.csdn.net/kk185800961/article/details/78739988" target="_blank" title="Python selenium自动化模拟登录操作（一）">
				<h4 class="text-truncate oneline">
						Python selenium自动化<em>模拟</em>登录操作（一）				</h4>
				<div class="info-box d-flex align-content-center">
					<!-- <p class="avatar">
							<img src="https://avatar.csdn.net/6/E/4/3_kk185800961.jpg" alt="kk185800961" class="avatar-pic">
							<span class="namebox">
								<span class="name">kk185800961</span>
								<span class="triangle"></span>
							</span>
					</p> -->
					<p class="date-and-readNum">
						<span class="date hover-show">12-07</span>
						<span class="read-num hover-hide">
							<svg class="icon csdnc-yuedushu" aria-hidden="true">
								<use xlink:href="#csdnc-m-passwords-visible"></use>
							</svg>
							5038</span>
						</p>
					</div>
				</a>
					<p class="content">
						<a href="https://blog.csdn.net/kk185800961/article/details/78739988" target="_blank" title="Python selenium自动化模拟登录操作（一）">
							<span class="desc oneline">Selenium Python 提供了一个简单的API 便于我们使用 Selenium WebDriver编写 功能/验收测试。 通过Selenium Python的API，你可以直观地使用所有的 S...</span>
						</a>
                        						<span class="blog_title_box oneline"><a target="_blank" href="https://blog.csdn.net/kk185800961">来自：	<span class="blog_title"> KK 笔记：专注数据</span></a></span>
                        					</p>
			</div>
					</div>
	
    
	    
    		<div class="recommend-item-box recommend-box-ident type_blog clearfix" data-track-view='{"mod":"popu_614","con":",https://blog.csdn.net/xiajiandong1024/article/details/71038363,BlogCommendFromBaidu_16"}' data-track-click='{"mod":"popu_614","con":",https://blog.csdn.net/xiajiandong1024/article/details/71038363,BlogCommendFromBaidu_16"}'>
			<div class="content">
				<a href="https://blog.csdn.net/xiajiandong1024/article/details/71038363" target="_blank" title="cookie和session">
				<h4 class="text-truncate oneline">
						cookie和session				</h4>
				<div class="info-box d-flex align-content-center">
					<!-- <p class="avatar">
							<img src="https://avatar.csdn.net/1/8/F/3_xiajiandong1024.jpg" alt="xiajiandong1024" class="avatar-pic">
							<span class="namebox">
								<span class="name">xiajiandong1024</span>
								<span class="triangle"></span>
							</span>
					</p> -->
					<p class="date-and-readNum">
						<span class="date hover-show">05-01</span>
						<span class="read-num hover-hide">
							<svg class="icon csdnc-yuedushu" aria-hidden="true">
								<use xlink:href="#csdnc-m-passwords-visible"></use>
							</svg>
							528</span>
						</p>
					</div>
				</a>
					<p class="content">
						<a href="https://blog.csdn.net/xiajiandong1024/article/details/71038363" target="_blank" title="cookie和session">
							<span class="desc oneline">cookie设置设置 cookie,发送一个cookie到客户端 
语法：bool setcookie ( string $name [, string $value [, int $expire =...</span>
						</a>
                        						<span class="blog_title_box oneline"><a target="_blank" href="https://blog.csdn.net/xiajiandong1024">来自：	<span class="blog_title"> x</span></a></span>
                        					</p>
			</div>
					</div>
	
    
	    
    		<div class="recommend-item-box recommend-box-ident type_blog clearfix" data-track-view='{"mod":"popu_614","con":",https://blog.csdn.net/zhu_free/article/details/50563756,BlogCommendFromBaidu_17"}' data-track-click='{"mod":"popu_614","con":",https://blog.csdn.net/zhu_free/article/details/50563756,BlogCommendFromBaidu_17"}'>
			<div class="content">
				<a href="https://blog.csdn.net/zhu_free/article/details/50563756" target="_blank" title="requests有关cookie的使用">
				<h4 class="text-truncate oneline">
						<em>requests</em>有关cookie的<em>使用</em>				</h4>
				<div class="info-box d-flex align-content-center">
					<!-- <p class="avatar">
							<img src="https://avatar.csdn.net/D/7/2/3_zhu_free.jpg" alt="zhu_free" class="avatar-pic">
							<span class="namebox">
								<span class="name">zhu_free</span>
								<span class="triangle"></span>
							</span>
					</p> -->
					<p class="date-and-readNum">
						<span class="date hover-show">01-22</span>
						<span class="read-num hover-hide">
							<svg class="icon csdnc-yuedushu" aria-hidden="true">
								<use xlink:href="#csdnc-m-passwords-visible"></use>
							</svg>
							3.5万</span>
						</p>
					</div>
				</a>
					<p class="content">
						<a href="https://blog.csdn.net/zhu_free/article/details/50563756" target="_blank" title="requests有关cookie的使用">
							<span class="desc oneline">requests有关cookie的使用最近用requests把百度贴吧的脚本重写了一遍，把用urllib模拟登陆的部分全部重写了一遍，算是渗入接触了一下requests，感觉确实方便了很多。...</span>
						</a>
                        						<span class="blog_title_box oneline"><a target="_blank" href="https://blog.csdn.net/zhu_free">来自：	<span class="blog_title"> zhu_free的博客</span></a></span>
                        					</p>
			</div>
					</div>
	
    
	    
    		<div class="recommend-item-box recommend-box-ident type_blog clearfix" data-track-view='{"mod":"popu_614","con":",https://blog.csdn.net/haeasringnar/article/details/81224127,BlogCommendFromBaidu_18"}' data-track-click='{"mod":"popu_614","con":",https://blog.csdn.net/haeasringnar/article/details/81224127,BlogCommendFromBaidu_18"}'>
			<div class="content">
				<a href="https://blog.csdn.net/haeasringnar/article/details/81224127" target="_blank" title="Python3 利用requests 库进行post携带账号密码请求数据">
				<h4 class="text-truncate oneline">
						<em>Python3</em> 利用<em>requests</em> 库进行post携带账号密码请求数据				</h4>
				<div class="info-box d-flex align-content-center">
					<!-- <p class="avatar">
							<img src="https://avatar.csdn.net/B/4/0/3_haeasringnar.jpg" alt="haeasringnar" class="avatar-pic">
							<span class="namebox">
								<span class="name">haeasringnar</span>
								<span class="triangle"></span>
							</span>
					</p> -->
					<p class="date-and-readNum">
						<span class="date hover-show">07-26</span>
						<span class="read-num hover-hide">
							<svg class="icon csdnc-yuedushu" aria-hidden="true">
								<use xlink:href="#csdnc-m-passwords-visible"></use>
							</svg>
							4724</span>
						</p>
					</div>
				</a>
					<p class="content">
						<a href="https://blog.csdn.net/haeasringnar/article/details/81224127" target="_blank" title="Python3 利用requests 库进行post携带账号密码请求数据">
							<span class="desc oneline">import urllib,json,requests
url = 'http://127.0.0.1:8000/account/login'
headers = {}
data = {'userna...</span>
						</a>
                        						<span class="blog_title_box oneline"><a target="_blank" href="https://blog.csdn.net/haeasringnar">来自：	<span class="blog_title"> haeasringnar的博客</span></a></span>
                        					</p>
			</div>
					</div>
	
    <div class="recommend-item-box recommend-ad-box"><div id="kp_box_62" data-pid="62" data-track-view='{"mod":"kp_popu_62-556","con":",,"}' data-track-click='{"mod":"kp_popu_62-556","con":",,"}'><div id="three_ad18" class="mediav_ad" ></div>
<script type="text/javascript" src="//static.mediav.com/js/mvf_news_feed.js"></script>
<script>
                                               NEWS_FEED({
                w: 852,
                h : 60,
                showid : 'Afihld',
                placeholderId: "three_ad18",
                inject : 'define',
                define : {
                    imagePosition : 'left',
                    imageBorderRadius : 3,
                    imageWidth: 90,
                    imageHeight: 60,
                    imageFill : 'clip',
                    displayImage : true,
                    displayTitle : true,
                    titleFontSize: 18,
                    titleFontColor: '#000',
                    titleFontFamily : 'Lato,-apple-system,SF UI Text,Arial,PingFang SC,Hiragino Sans GB,Microsoft YaHei,WenQuanYi Micro Hei,sans-serif',
                    titleFontWeight: 'bold',
                    titlePaddingTop : 0,
                    titlePaddingRight : 0,
                    titlePaddingBottom : 5,
                    titlePaddingLeft : 16,
                    displayDesc : true,
                    descFontSize: 14,
                    descFontColor: '#8e959a',
                    descFontFamily : 'Microsoft Yahei',
                    paddingTop : 0,
                    paddingRight : 0,
                    paddingBottom : 0,
                    paddingLeft : 0,
                    backgroundColor: '#fff',
                    hoverColor: '#000'
                      }
                  })
                                        </script></div></div>
	    
    		<div class="recommend-item-box recommend-box-ident type_blog clearfix" data-track-view='{"mod":"popu_614","con":",https://blog.csdn.net/zhengy1995/article/details/52692969,BlogCommendFromBaidu_19"}' data-track-click='{"mod":"popu_614","con":",https://blog.csdn.net/zhengy1995/article/details/52692969,BlogCommendFromBaidu_19"}'>
			<div class="content">
				<a href="https://blog.csdn.net/zhengy1995/article/details/52692969" target="_blank" title="Python爬取蚂蜂窝教程">
				<h4 class="text-truncate oneline">
						Python爬取蚂蜂窝教程				</h4>
				<div class="info-box d-flex align-content-center">
					<!-- <p class="avatar">
							<img src="https://avatar.csdn.net/3/1/2/3_zhengy1995.jpg" alt="zhengy1995" class="avatar-pic">
							<span class="namebox">
								<span class="name">zhengy1995</span>
								<span class="triangle"></span>
							</span>
					</p> -->
					<p class="date-and-readNum">
						<span class="date hover-show">09-28</span>
						<span class="read-num hover-hide">
							<svg class="icon csdnc-yuedushu" aria-hidden="true">
								<use xlink:href="#csdnc-m-passwords-visible"></use>
							</svg>
							8991</span>
						</p>
					</div>
				</a>
					<p class="content">
						<a href="https://blog.csdn.net/zhengy1995/article/details/52692969" target="_blank" title="Python爬取蚂蜂窝教程">
							<span class="desc oneline">python+Beautiful爬虫抓取蚂蜂窝信息</span>
						</a>
                        						<span class="blog_title_box oneline"><a target="_blank" href="https://blog.csdn.net/zhengy1995">来自：	<span class="blog_title"> 正好儿的博客</span></a></span>
                        					</p>
			</div>
					</div>
	
    
	    
    		<div class="recommend-item-box recommend-box-ident type_blog clearfix" data-track-view='{"mod":"popu_614","con":",https://blog.csdn.net/u013630017/article/details/52434470,BlogCommendFromBaidu_20"}' data-track-click='{"mod":"popu_614","con":",https://blog.csdn.net/u013630017/article/details/52434470,BlogCommendFromBaidu_20"}'>
			<div class="content">
				<a href="https://blog.csdn.net/u013630017/article/details/52434470" target="_blank" title="Python3 Post登录并且保存cookie登录其他页面">
				<h4 class="text-truncate oneline">
						<em>Python3</em> Post登录并且保存cookie登录其他页面				</h4>
				<div class="info-box d-flex align-content-center">
					<!-- <p class="avatar">
							<img src="https://avatar.csdn.net/D/E/5/3_u013630017.jpg" alt="u013630017" class="avatar-pic">
							<span class="namebox">
								<span class="name">u013630017</span>
								<span class="triangle"></span>
							</span>
					</p> -->
					<p class="date-and-readNum">
						<span class="date hover-show">09-04</span>
						<span class="read-num hover-hide">
							<svg class="icon csdnc-yuedushu" aria-hidden="true">
								<use xlink:href="#csdnc-m-passwords-visible"></use>
							</svg>
							1776</span>
						</p>
					</div>
				</a>
					<p class="content">
						<a href="https://blog.csdn.net/u013630017/article/details/52434470" target="_blank" title="Python3 Post登录并且保存cookie登录其他页面">
							<span class="desc oneline">import urllib.request
import sys
import http.cookiejar
import urllib.parse
from bs4 import Beautiful...</span>
						</a>
                        						<span class="blog_title_box oneline"><a target="_blank" href="https://blog.csdn.net/u013630017">来自：	<span class="blog_title"> 队长小楠的博客</span></a></span>
                        					</p>
			</div>
					</div>
	
    
	    
    		<div class="recommend-item-box recommend-box-ident" data-track-view='{"mod":"popu_614","con":",https://download.csdn.net/download/shengzheyu/10627639,searchFromBaidu_21"}' data-track-click='{"mod":"popu_614","con":",https://download.csdn.net/download/shengzheyu/10627639,searchFromBaidu_21"}'>
		<a href="https://download.csdn.net/download/shengzheyu/10627639" target="_blank">
			<h4 class="text-truncate oneline">
					微博<em>模拟</em>登陆（<em>python3</em>-2018年8月最新版本）			</h4>
			<div class="info-box d-flex align-content-center">
				<p>
									<span class="read-num">下载</span>
								</p>
				<p>
					<span class="date">08-26</span>
				</p>
			</div>
			<p class="content oneline">
					也是自己学习python，网上模拟登陆的代码很多都是py2.7版本，最新的py3+版本更改了函数名也摒弃了2.x版本的一些方法，现在根据修改，成功实现py3微博模拟登陆，并加了自己学习注释，希望大家共			</p>
		</a>

	</div>
	
    
	    
    		<div class="recommend-item-box recommend-box-ident type_blog clearfix" data-track-view='{"mod":"popu_614","con":",https://blog.csdn.net/M_WBCG/article/details/70243372,BlogCommendFromGuangxin_22"}' data-track-click='{"mod":"popu_614","con":",https://blog.csdn.net/M_WBCG/article/details/70243372,BlogCommendFromGuangxin_22"}'>
			<div class="content">
				<a href="https://blog.csdn.net/M_WBCG/article/details/70243372" target="_blank" title="Python 网络爬虫--简单的模拟登录">
				<h4 class="text-truncate oneline">
						Python 网络爬虫--简单的<em>模拟</em>登录				</h4>
				<div class="info-box d-flex align-content-center">
					<!-- <p class="avatar">
							<img src="https://avatar.csdn.net/C/C/0/3_m_wbcg.jpg" alt="M_WBCG" class="avatar-pic">
							<span class="namebox">
								<span class="name">M_WBCG</span>
								<span class="triangle"></span>
							</span>
					</p> -->
					<p class="date-and-readNum">
						<span class="date hover-show">04-19</span>
						<span class="read-num hover-hide">
							<svg class="icon csdnc-yuedushu" aria-hidden="true">
								<use xlink:href="#csdnc-m-passwords-visible"></use>
							</svg>
							9837</span>
						</p>
					</div>
				</a>
					<p class="content">
						<a href="https://blog.csdn.net/M_WBCG/article/details/70243372" target="_blank" title="Python 网络爬虫--简单的模拟登录">
							<span class="desc oneline">和获取网页上的信息不同，想要进行模拟登录还需要向服务器发送一些信息，如账号、密码等等。
模拟登录一个网站大致分为这么几步：
1.先将登录网站的隐藏信息找到，并将其内容先进行保存（由于我这里登录的网站并...</span>
						</a>
                        						<span class="blog_title_box oneline"><a target="_blank" href="https://blog.csdn.net/M_WBCG">来自：	<span class="blog_title"> 年华飞逝的博客</span></a></span>
                        					</p>
			</div>
					</div>
	
    
	    
    		<div class="recommend-item-box recommend-box-ident type_blog clearfix" data-track-view='{"mod":"popu_614","con":",https://blog.csdn.net/qq_41376740/article/details/79292953,BlogCommendFromGuangxin_23"}' data-track-click='{"mod":"popu_614","con":",https://blog.csdn.net/qq_41376740/article/details/79292953,BlogCommendFromGuangxin_23"}'>
			<div class="content">
				<a href="https://blog.csdn.net/qq_41376740/article/details/79292953" target="_blank" title="python模拟一个简单的用户登录">
				<h4 class="text-truncate oneline">
						python<em>模拟</em>一个简单的<em>用户登录</em>				</h4>
				<div class="info-box d-flex align-content-center">
					<!-- <p class="avatar">
							<img src="https://avatar.csdn.net/7/E/5/3_qq_41376740.jpg" alt="qq_41376740" class="avatar-pic">
							<span class="namebox">
								<span class="name">qq_41376740</span>
								<span class="triangle"></span>
							</span>
					</p> -->
					<p class="date-and-readNum">
						<span class="date hover-show">02-08</span>
						<span class="read-num hover-hide">
							<svg class="icon csdnc-yuedushu" aria-hidden="true">
								<use xlink:href="#csdnc-m-passwords-visible"></use>
							</svg>
							994</span>
						</p>
					</div>
				</a>
					<p class="content">
						<a href="https://blog.csdn.net/qq_41376740/article/details/79292953" target="_blank" title="python模拟一个简单的用户登录">
							<span class="desc oneline">


前景
思路
主要功能
代码
实验结果
总结






前景

今天学到了一个模块hashlib,通过廖老师的文章，我猛然发现！原来存储在数据库里面的用户名的密码是经过hash算法之后的，而不是...</span>
						</a>
                        						<span class="blog_title_box oneline"><a target="_blank" href="https://blog.csdn.net/qq_41376740">来自：	<span class="blog_title"> 人在江湖</span></a></span>
                        					</p>
			</div>
					</div>
	
    <div class="recommend-item-box recommend-ad-box"><div id="kp_box_63" data-pid="63" data-track-view='{"mod":"kp_popu_63-555","con":",,"}' data-track-click='{"mod":"kp_popu_63-555","con":",,"}'><div id="three_ad23" class="mediav_ad" ></div>
<script type="text/javascript" src="//static.mediav.com/js/mvf_news_feed.js"></script>
<script>
                                               NEWS_FEED({
                w: 852,
                h : 60,
                showid : 'GNKXx7',
                placeholderId: "three_ad23",
                inject : 'define',
                define : {
                    imagePosition : 'left',
                    imageBorderRadius : 3,
                    imageWidth: 90,
                    imageHeight: 60,
                    imageFill : 'clip',
                    displayImage : true,
                    displayTitle : true,
                    titleFontSize: 18,
                    titleFontColor: '#000',
                    titleFontFamily : 'Lato,-apple-system,SF UI Text,Arial,PingFang SC,Hiragino Sans GB,Microsoft YaHei,WenQuanYi Micro Hei,sans-serif',
                    titleFontWeight: 'bold',
                    titlePaddingTop : 0,
                    titlePaddingRight : 0,
                    titlePaddingBottom : 5,
                    titlePaddingLeft : 16,
                    displayDesc : true,
                    descFontSize: 14,
                    descFontColor: '#8e959a',
                    descFontFamily : 'Microsoft Yahei',
                    paddingTop : 0,
                    paddingRight : 0,
                    paddingBottom : 0,
                    paddingLeft : 0,
                    backgroundColor: '#fff',
                    hoverColor: '#000'
                      }
                  })
                                        </script></div></div>
	    
    		<div class="recommend-item-box recommend-box-ident type_blog clearfix" data-track-view='{"mod":"popu_614","con":",https://blog.csdn.net/churximi/article/details/50917322,BlogCommendFromGuangxin_24"}' data-track-click='{"mod":"popu_614","con":",https://blog.csdn.net/churximi/article/details/50917322,BlogCommendFromGuangxin_24"}'>
			<div class="content">
				<a href="https://blog.csdn.net/churximi/article/details/50917322" target="_blank" title="Python爬虫之模拟登录总结">
				<h4 class="text-truncate oneline">
						Python爬虫之<em>模拟</em>登录总结				</h4>
				<div class="info-box d-flex align-content-center">
					<!-- <p class="avatar">
							<img src="https://avatar.csdn.net/F/B/1/3_churximi.jpg" alt="churximi" class="avatar-pic">
							<span class="namebox">
								<span class="name">churximi</span>
								<span class="triangle"></span>
							</span>
					</p> -->
					<p class="date-and-readNum">
						<span class="date hover-show">03-17</span>
						<span class="read-num hover-hide">
							<svg class="icon csdnc-yuedushu" aria-hidden="true">
								<use xlink:href="#csdnc-m-passwords-visible"></use>
							</svg>
							3.3万</span>
						</p>
					</div>
				</a>
					<p class="content">
						<a href="https://blog.csdn.net/churximi/article/details/50917322" target="_blank" title="Python爬虫之模拟登录总结">
							<span class="desc oneline">备注：python 2.7.9，32位


有些网站需要登录后才能爬取所需要的信息，此时可以设计爬虫进行模拟登录，原理是利用浏览器cookie。
一、浏览器访问服务器的过程：
    （1）浏览器（客...</span>
						</a>
                        						<span class="blog_title_box oneline"><a target="_blank" href="https://blog.csdn.net/churximi">来自：	<span class="blog_title"> 竹聿Simon的专栏</span></a></span>
                        					</p>
			</div>
					</div>
	
    
	    
    		<div class="recommend-item-box recommend-box-ident type_blog clearfix" data-track-view='{"mod":"popu_614","con":",https://blog.csdn.net/ygc123189/article/details/79088772,BlogCommendFromGuangxin_25"}' data-track-click='{"mod":"popu_614","con":",https://blog.csdn.net/ygc123189/article/details/79088772,BlogCommendFromGuangxin_25"}'>
			<div class="content">
				<a href="https://blog.csdn.net/ygc123189/article/details/79088772" target="_blank" title="Python模拟登录多种实现方式">
				<h4 class="text-truncate oneline">
						Python<em>模拟</em>登录多种<em>实现</em>方式				</h4>
				<div class="info-box d-flex align-content-center">
					<!-- <p class="avatar">
							<img src="https://avatar.csdn.net/0/9/C/3_ygc123189.jpg" alt="ygc123189" class="avatar-pic">
							<span class="namebox">
								<span class="name">ygc123189</span>
								<span class="triangle"></span>
							</span>
					</p> -->
					<p class="date-and-readNum">
						<span class="date hover-show">01-17</span>
						<span class="read-num hover-hide">
							<svg class="icon csdnc-yuedushu" aria-hidden="true">
								<use xlink:href="#csdnc-m-passwords-visible"></use>
							</svg>
							1822</span>
						</p>
					</div>
				</a>
					<p class="content">
						<a href="https://blog.csdn.net/ygc123189/article/details/79088772" target="_blank" title="Python模拟登录多种实现方式">
							<span class="desc oneline">Python模拟登录多种实现方式
基于Python 3.6



#coding:utf-8
import sys
import io
import urllib.request
impor...</span>
						</a>
                        						<span class="blog_title_box oneline"><a target="_blank" href="https://blog.csdn.net/ygc123189">来自：	<span class="blog_title"> kocor的博客</span></a></span>
                        					</p>
			</div>
					</div>
	
    
	    
    		<div class="recommend-item-box recommend-box-ident type_blog clearfix" data-track-view='{"mod":"popu_614","con":",https://blog.csdn.net/HeatDeath/article/details/62423963,BlogCommendFromGuangxin_26"}' data-track-click='{"mod":"popu_614","con":",https://blog.csdn.net/HeatDeath/article/details/62423963,BlogCommendFromGuangxin_26"}'>
			<div class="content">
				<a href="https://blog.csdn.net/HeatDeath/article/details/62423963" target="_blank" title="基于How To Tango With Django 1.9的重新实践（10）——Cookies and Sessions">
				<h4 class="text-truncate oneline">
						基于How To Tango With Django 1.9的重新实践（10）——Cookies and Sessions				</h4>
				<div class="info-box d-flex align-content-center">
					<!-- <p class="avatar">
							<img src="https://avatar.csdn.net/B/5/0/3_heatdeath.jpg" alt="HeatDeath" class="avatar-pic">
							<span class="namebox">
								<span class="name">HeatDeath</span>
								<span class="triangle"></span>
							</span>
					</p> -->
					<p class="date-and-readNum">
						<span class="date hover-show">03-16</span>
						<span class="read-num hover-hide">
							<svg class="icon csdnc-yuedushu" aria-hidden="true">
								<use xlink:href="#csdnc-m-passwords-visible"></use>
							</svg>
							1065</span>
						</p>
					</div>
				</a>
					<p class="content">
						<a href="https://blog.csdn.net/HeatDeath/article/details/62423963" target="_blank" title="基于How To Tango With Django 1.9的重新实践（10）——Cookies and Sessions">
							<span class="desc oneline">在本章中我们将要介绍sessions和cookies,它们两个在现代wen应用中有着至关重要的作用.在上一章,Django框架使用sessions和cookies来处理用户登录和注销功能(都在背后运行...</span>
						</a>
                        						<span class="blog_title_box oneline"><a target="_blank" href="https://blog.csdn.net/HeatDeath">来自：	<span class="blog_title"> HeatDeath的博客</span></a></span>
                        					</p>
			</div>
					</div>
	
    
	    
    		<div class="recommend-item-box recommend-box-ident type_blog clearfix" data-track-view='{"mod":"popu_614","con":",https://blog.csdn.net/u014483914/article/details/80689718,BlogCommendFromQuerySearch_27"}' data-track-click='{"mod":"popu_614","con":",https://blog.csdn.net/u014483914/article/details/80689718,BlogCommendFromQuerySearch_27"}'>
			<div class="content">
				<a href="https://blog.csdn.net/u014483914/article/details/80689718" target="_blank" title="基于python3.6的马蜂窝旅行模拟登陆">
				<h4 class="text-truncate oneline">
						基于<em>python3</em>.6的<em>马蜂窝</em>旅行<em>模拟</em>登陆				</h4>
				<div class="info-box d-flex align-content-center">
					<!-- <p class="avatar">
							<img src="https://avatar.csdn.net/6/6/8/3_u014483914.jpg" alt="u014483914" class="avatar-pic">
							<span class="namebox">
								<span class="name">u014483914</span>
								<span class="triangle"></span>
							</span>
					</p> -->
					<p class="date-and-readNum">
						<span class="date hover-show">06-14</span>
						<span class="read-num hover-hide">
							<svg class="icon csdnc-yuedushu" aria-hidden="true">
								<use xlink:href="#csdnc-m-passwords-visible"></use>
							</svg>
							1430</span>
						</p>
					</div>
				</a>
					<p class="content">
						<a href="https://blog.csdn.net/u014483914/article/details/80689718" target="_blank" title="基于python3.6的马蜂窝旅行模拟登陆">
							<span class="desc oneline">这段时间在爬马蜂窝的用户信息，之前搞的是注册用户的粉丝和关注的人，这个稍后再整理，内容比较多；在爬用户的社交圈时需要登陆权限，那就搞一下模拟登陆吧~~进入马蜂窝旅行的登陆界面，按F12查看源码，输入用...</span>
						</a>
                        						<span class="blog_title_box oneline"><a target="_blank" href="https://blog.csdn.net/u014483914">来自：	<span class="blog_title"> 想不出一个好的标题，就用这个吧</span></a></span>
                        					</p>
			</div>
					</div>
	
    
	    
    		<div class="recommend-item-box recommend-box-ident type_blog clearfix" data-track-view='{"mod":"popu_614","con":",https://blog.csdn.net/qq_41888542/article/details/81190670,BlogCommendFromQuerySearch_28"}' data-track-click='{"mod":"popu_614","con":",https://blog.csdn.net/qq_41888542/article/details/81190670,BlogCommendFromQuerySearch_28"}'>
			<div class="content">
				<a href="https://blog.csdn.net/qq_41888542/article/details/81190670" target="_blank" title="使用Selenium与Requests模拟登陆">
				<h4 class="text-truncate oneline">
						<em>使用</em>Selenium与<em>Requests</em><em>模拟</em>登陆				</h4>
				<div class="info-box d-flex align-content-center">
					<!-- <p class="avatar">
							<img src="https://avatar.csdn.net/A/D/8/3_qq_41888542.jpg" alt="qq_41888542" class="avatar-pic">
							<span class="namebox">
								<span class="name">qq_41888542</span>
								<span class="triangle"></span>
							</span>
					</p> -->
					<p class="date-and-readNum">
						<span class="date hover-show">07-24</span>
						<span class="read-num hover-hide">
							<svg class="icon csdnc-yuedushu" aria-hidden="true">
								<use xlink:href="#csdnc-m-passwords-visible"></use>
							</svg>
							128</span>
						</p>
					</div>
				</a>
					<p class="content">
						<a href="https://blog.csdn.net/qq_41888542/article/details/81190670" target="_blank" title="使用Selenium与Requests模拟登陆">
							<span class="desc oneline">


这是崔斯特的第五十九篇原创文章


模拟登陆的两种方式，你喜欢哪种 (๑• . •๑)



本期讲一讲模拟登录相关的东西，目标网站是Github



简单的Selnium

想说说简单的方法...</span>
						</a>
                        						<span class="blog_title_box oneline"><a target="_blank" href="https://blog.csdn.net/qq_41888542">来自：	<span class="blog_title"> qq_41888542的博客</span></a></span>
                        					</p>
			</div>
					</div>
	
    <div class="recommend-item-box recommend-ad-box"><div id="kp_box_64" data-pid="64" data-track-view='{"mod":"kp_popu_64-81","con":",,"}' data-track-click='{"mod":"kp_popu_64-81","con":",,"}'><div id="three_ad28" class="mediav_ad" ></div>
<script type="text/javascript" src="//static.mediav.com/js/mvf_news_feed.js"></script>
<script>
                                               NEWS_FEED({
                w: 852,
                h : 60,
                showid : 'Afihld',
                placeholderId: "three_ad28",
                inject : 'define',
                define : {
                    imagePosition : 'left',
                    imageBorderRadius : 3,
                    imageWidth: 90,
                    imageHeight: 60,
                    imageFill : 'clip',
                    displayImage : true,
                    displayTitle : true,
                    titleFontSize: 18,
                    titleFontColor: '#000',
                    titleFontFamily : 'Lato,-apple-system,SF UI Text,Arial,PingFang SC,Hiragino Sans GB,Microsoft YaHei,WenQuanYi Micro Hei,sans-serif',
                    titleFontWeight: 'bold',
                    titlePaddingTop : 0,
                    titlePaddingRight : 0,
                    titlePaddingBottom : 5,
                    titlePaddingLeft : 16,
                    displayDesc : true,
                    descFontSize: 14,
                    descFontColor: '#8e959a',
                    descFontFamily : 'Microsoft Yahei',
                    paddingTop : 0,
                    paddingRight : 0,
                    paddingBottom : 0,
                    paddingLeft : 0,
                    backgroundColor: '#fff',
                    hoverColor: '#000'
                      }
                  })
                                        </script></div></div>
	    
    		<div class="recommend-item-box recommend-box-ident type_blog clearfix" data-track-view='{"mod":"popu_614","con":",https://blog.csdn.net/zwq912318834/article/details/79614372,BlogCommendFromQuerySearch_29"}' data-track-click='{"mod":"popu_614","con":",https://blog.csdn.net/zwq912318834/article/details/79614372,BlogCommendFromQuerySearch_29"}'>
			<div class="content">
				<a href="https://blog.csdn.net/zwq912318834/article/details/79614372" target="_blank" title="python3下使用scrapy实现模拟用户登录与cookie存储 —— 基础篇（马蜂窝）">
				<h4 class="text-truncate oneline">
						<em>python3</em>下<em>使用</em>scrapy<em>实现</em><em>模拟</em><em>用户登录</em>与cookie存储 —— <em>基础</em>篇（<em>马蜂窝</em>）				</h4>
				<div class="info-box d-flex align-content-center">
					<!-- <p class="avatar">
							<img src="https://avatar.csdn.net/7/4/8/3_zwq912318834.jpg" alt="zwq912318834" class="avatar-pic">
							<span class="namebox">
								<span class="name">zwq912318834</span>
								<span class="triangle"></span>
							</span>
					</p> -->
					<p class="date-and-readNum">
						<span class="date hover-show">03-19</span>
						<span class="read-num hover-hide">
							<svg class="icon csdnc-yuedushu" aria-hidden="true">
								<use xlink:href="#csdnc-m-passwords-visible"></use>
							</svg>
							3367</span>
						</p>
					</div>
				</a>
					<p class="content">
						<a href="https://blog.csdn.net/zwq912318834/article/details/79614372" target="_blank" title="python3下使用scrapy实现模拟用户登录与cookie存储 —— 基础篇（马蜂窝）">
							<span class="desc oneline">python3下使用scrapy实现模拟用户登录与cookie存储 —— 基础篇（马蜂窝）

1. 背景


相关基础知识点回顾： 
python3下使用requests实现模拟用户登录（马蜂窝）： ...</span>
						</a>
                        						<span class="blog_title_box oneline"><a target="_blank" href="https://blog.csdn.net/zwq912318834">来自：	<span class="blog_title"> Kosmoo的博客</span></a></span>
                        					</p>
			</div>
					</div>
	
    
	    
    		<div class="recommend-item-box recommend-box-ident type_blog clearfix" data-track-view='{"mod":"popu_614","con":",https://blog.csdn.net/Cooler_max/article/details/79193386,BlogCommendFromQuerySearch_30"}' data-track-click='{"mod":"popu_614","con":",https://blog.csdn.net/Cooler_max/article/details/79193386,BlogCommendFromQuerySearch_30"}'>
			<div class="content">
				<a href="https://blog.csdn.net/Cooler_max/article/details/79193386" target="_blank" title="python3使用requests模块的get方法做爬虫（伪装浏览器）">
				<h4 class="text-truncate oneline">
						<em>python3</em><em>使用</em><em>requests</em>模块的get方法做爬虫（伪装浏览器）				</h4>
				<div class="info-box d-flex align-content-center">
					<!-- <p class="avatar">
							<img src="https://avatar.csdn.net/1/E/4/3_cooler_max.jpg" alt="Cooler_max" class="avatar-pic">
							<span class="namebox">
								<span class="name">Cooler_max</span>
								<span class="triangle"></span>
							</span>
					</p> -->
					<p class="date-and-readNum">
						<span class="date hover-show">01-29</span>
						<span class="read-num hover-hide">
							<svg class="icon csdnc-yuedushu" aria-hidden="true">
								<use xlink:href="#csdnc-m-passwords-visible"></use>
							</svg>
							3414</span>
						</p>
					</div>
				</a>
					<p class="content">
						<a href="https://blog.csdn.net/Cooler_max/article/details/79193386" target="_blank" title="python3使用requests模块的get方法做爬虫（伪装浏览器）">
							<span class="desc oneline">获取网页对象可以使用两种方法：
使用urllib模块的urlopen方法：

import urllib

reponse=urllib.urlopen(&quot;http://www.itcast...</span>
						</a>
                        						<span class="blog_title_box oneline"><a target="_blank" href="https://blog.csdn.net/Cooler_max">来自：	<span class="blog_title"> Cooler_max的博客</span></a></span>
                        					</p>
			</div>
					</div>
	
    
	    
    		<div class="recommend-item-box recommend-box-ident type_blog clearfix" data-track-view='{"mod":"popu_614","con":",https://blog.csdn.net/sinat_33487968/article/details/62437265,BlogCommendFromQuerySearch_31"}' data-track-click='{"mod":"popu_614","con":",https://blog.csdn.net/sinat_33487968/article/details/62437265,BlogCommendFromQuerySearch_31"}'>
			<div class="content">
				<a href="https://blog.csdn.net/sinat_33487968/article/details/62437265" target="_blank" title="[python 爬虫]Python爬虫抓取马蜂窝游记的照片 基于xpath">
				<h4 class="text-truncate oneline">
						[python 爬虫]Python爬虫抓取<em>马蜂窝</em>游记的照片 基于xpath				</h4>
				<div class="info-box d-flex align-content-center">
					<!-- <p class="avatar">
							<img src="https://avatar.csdn.net/A/2/0/3_sinat_33487968.jpg" alt="sinat_33487968" class="avatar-pic">
							<span class="namebox">
								<span class="name">sinat_33487968</span>
								<span class="triangle"></span>
							</span>
					</p> -->
					<p class="date-and-readNum">
						<span class="date hover-show">03-16</span>
						<span class="read-num hover-hide">
							<svg class="icon csdnc-yuedushu" aria-hidden="true">
								<use xlink:href="#csdnc-m-passwords-visible"></use>
							</svg>
							2469</span>
						</p>
					</div>
				</a>
					<p class="content">
						<a href="https://blog.csdn.net/sinat_33487968/article/details/62437265" target="_blank" title="[python 爬虫]Python爬虫抓取马蜂窝游记的照片 基于xpath">
							<span class="desc oneline">之前都只是使用urllib和urllib2这两个类库，接下来要发掘更多好用的工具了，比如这个xpath，对于分析HTML的网页结构实在是太方便。

http://blog.csdn.net/freek...</span>
						</a>
                        						<span class="blog_title_box oneline"><a target="_blank" href="https://blog.csdn.net/sinat_33487968">来自：	<span class="blog_title"> sinat_33487968的博客</span></a></span>
                        					</p>
			</div>
					</div>
	
    
	    
    		<div class="recommend-item-box recommend-box-ident type_blog clearfix" data-track-view='{"mod":"popu_614","con":",https://blog.csdn.net/zhengyikuangge/article/details/72673913,BlogCommendFromBaidu_32"}' data-track-click='{"mod":"popu_614","con":",https://blog.csdn.net/zhengyikuangge/article/details/72673913,BlogCommendFromBaidu_32"}'>
			<div class="content">
				<a href="https://blog.csdn.net/zhengyikuangge/article/details/72673913" target="_blank" title="python3进阶学习总结——模拟登录">
				<h4 class="text-truncate oneline">
						<em>python3</em>进阶学习总结——<em>模拟</em>登录				</h4>
				<div class="info-box d-flex align-content-center">
					<!-- <p class="avatar">
							<img src="https://avatar.csdn.net/7/2/4/3_zhengyikuangge.jpg" alt="zhengyikuangge" class="avatar-pic">
							<span class="namebox">
								<span class="name">zhengyikuangge</span>
								<span class="triangle"></span>
							</span>
					</p> -->
					<p class="date-and-readNum">
						<span class="date hover-show">05-24</span>
						<span class="read-num hover-hide">
							<svg class="icon csdnc-yuedushu" aria-hidden="true">
								<use xlink:href="#csdnc-m-passwords-visible"></use>
							</svg>
							391</span>
						</p>
					</div>
				</a>
					<p class="content">
						<a href="https://blog.csdn.net/zhengyikuangge/article/details/72673913" target="_blank" title="python3进阶学习总结——模拟登录">
							<span class="desc oneline">一开始跟着学习视频学习的时候发现视频中用的python2.X，而我的是python3.X，所以只能选择性的学习了。在网上找了许多代码但是能用的比较少，因为像一些比较大型的网站，它们的登录需要的条件比较...</span>
						</a>
                        						<span class="blog_title_box oneline"><a target="_blank" href="https://blog.csdn.net/zhengyikuangge">来自：	<span class="blog_title"> zhengyikuangge的博客</span></a></span>
                        					</p>
			</div>
					</div>
	
    
	    
    		<div class="recommend-item-box recommend-box-ident type_blog clearfix" data-track-view='{"mod":"popu_614","con":",https://blog.csdn.net/weixin_41782050/article/details/80571763,BlogCommendFromBaidu_33"}' data-track-click='{"mod":"popu_614","con":",https://blog.csdn.net/weixin_41782050/article/details/80571763,BlogCommendFromBaidu_33"}'>
			<div class="content">
				<a href="https://blog.csdn.net/weixin_41782050/article/details/80571763" target="_blank" title="Python爬虫day5—模拟登录、驱动浏览器及图片处理">
				<h4 class="text-truncate oneline">
						Python爬虫day5—<em>模拟</em>登录、驱动浏览器及图片处理				</h4>
				<div class="info-box d-flex align-content-center">
					<!-- <p class="avatar">
							<img src="https://avatar.csdn.net/6/8/F/3_weixin_41782050.jpg" alt="weixin_41782050" class="avatar-pic">
							<span class="namebox">
								<span class="name">weixin_41782050</span>
								<span class="triangle"></span>
							</span>
					</p> -->
					<p class="date-and-readNum">
						<span class="date hover-show">06-04</span>
						<span class="read-num hover-hide">
							<svg class="icon csdnc-yuedushu" aria-hidden="true">
								<use xlink:href="#csdnc-m-passwords-visible"></use>
							</svg>
							97</span>
						</p>
					</div>
				</a>
					<p class="content">
						<a href="https://blog.csdn.net/weixin_41782050/article/details/80571763" target="_blank" title="Python爬虫day5—模拟登录、驱动浏览器及图片处理">
							<span class="desc oneline">模拟登录

网页登录方法一：

import requests
from bs4 import BeautifulSoup

def main():
    resp = requests.get('...</span>
						</a>
                        						<span class="blog_title_box oneline"><a target="_blank" href="https://blog.csdn.net/weixin_41782050">来自：	<span class="blog_title"> 瞿凯Kai的博客</span></a></span>
                        					</p>
			</div>
					</div>
	
    <div class="recommend-item-box recommend-ad-box"><div id="kp_box_65" data-pid="65" data-track-view='{"mod":"kp_popu_65-84","con":",,"}' data-track-click='{"mod":"kp_popu_65-84","con":",,"}'><div id="three_ad33" class="mediav_ad" ></div>
<script>
                                               NEWS_FEED({
                w: 852,
                h : 60,
                showid : 'GNKXx7',
                placeholderId: "three_ad33",
                inject : 'define',
                define : {
                    imagePosition : 'left',
                    imageBorderRadius : 3,
                    imageWidth: 90,
                    imageHeight: 60,
                    imageFill : 'clip',
                    displayImage : true,
                    displayTitle : true,
                    titleFontSize: 18,
                    titleFontColor: '#000',
                    titleFontFamily : 'Lato,-apple-system,SF UI Text,Arial,PingFang SC,Hiragino Sans GB,Microsoft YaHei,WenQuanYi Micro Hei,sans-serif',
                    titleFontWeight: 'bold',
                    titlePaddingTop : 0,
                    titlePaddingRight : 0,
                    titlePaddingBottom : 5,
                    titlePaddingLeft : 16,
                    displayDesc : true,
                    descFontSize: 14,
                    descFontColor: '#8e959a',
                    descFontFamily : 'Microsoft Yahei',
                    paddingTop : 0,
                    paddingRight : 0,
                    paddingBottom : 0,
                    paddingLeft : 0,
                    backgroundColor: '#fff',
                    hoverColor: '#000'
                      }
                  })
                                        </script></div></div>
	    
    		<div class="recommend-item-box recommend-box-ident type_blog clearfix" data-track-view='{"mod":"popu_614","con":",https://blog.csdn.net/pczjzwok/article/details/39184481,BlogCommendFromBaidu_34"}' data-track-click='{"mod":"popu_614","con":",https://blog.csdn.net/pczjzwok/article/details/39184481,BlogCommendFromBaidu_34"}'>
			<div class="content">
				<a href="https://blog.csdn.net/pczjzwok/article/details/39184481" target="_blank" title="Python3.4 模拟登录校园网 技巧和大坑记录 无验证码">
				<h4 class="text-truncate oneline">
						<em>Python3</em>.4 <em>模拟</em>登录校园网 技巧和大坑记录 无验证码				</h4>
				<div class="info-box d-flex align-content-center">
					<!-- <p class="avatar">
							<img src="https://avatar.csdn.net/F/F/1/3_pczjzwok.jpg" alt="pczjzwok" class="avatar-pic">
							<span class="namebox">
								<span class="name">pczjzwok</span>
								<span class="triangle"></span>
							</span>
					</p> -->
					<p class="date-and-readNum">
						<span class="date hover-show">09-10</span>
						<span class="read-num hover-hide">
							<svg class="icon csdnc-yuedushu" aria-hidden="true">
								<use xlink:href="#csdnc-m-passwords-visible"></use>
							</svg>
							4955</span>
						</p>
					</div>
				</a>
					<p class="content">
						<a href="https://blog.csdn.net/pczjzwok/article/details/39184481" target="_blank" title="Python3.4 模拟登录校园网 技巧和大坑记录 无验证码">
							<span class="desc oneline">先把重要的技巧写出来吧，各种碰壁各种坑，但索性一个个克服过来了
一、辅助工具：wireshark：过滤器那里调到http，然后关闭其他无关的浏览器等等程序，然后再跑python程序，就能很舒服地对py...</span>
						</a>
                        						<span class="blog_title_box oneline"><a target="_blank" href="https://blog.csdn.net/pczjzwok">来自：	<span class="blog_title"> 杂碎记录本</span></a></span>
                        					</p>
			</div>
					</div>
	
    
	    
    		<div class="recommend-item-box recommend-box-ident type_blog clearfix" data-track-view='{"mod":"popu_614","con":",https://blog.csdn.net/hacker2025/article/details/73252600,BlogCommendFromBaidu_35"}' data-track-click='{"mod":"popu_614","con":",https://blog.csdn.net/hacker2025/article/details/73252600,BlogCommendFromBaidu_35"}'>
			<div class="content">
				<a href="https://blog.csdn.net/hacker2025/article/details/73252600" target="_blank" title="Python3处理HTTP请求">
				<h4 class="text-truncate oneline">
						<em>Python3</em>处理HTTP请求				</h4>
				<div class="info-box d-flex align-content-center">
					<!-- <p class="avatar">
							<img src="https://avatar.csdn.net/E/9/6/3_hacker2025.jpg" alt="hacker2025" class="avatar-pic">
							<span class="namebox">
								<span class="name">hacker2025</span>
								<span class="triangle"></span>
							</span>
					</p> -->
					<p class="date-and-readNum">
						<span class="date hover-show">06-14</span>
						<span class="read-num hover-hide">
							<svg class="icon csdnc-yuedushu" aria-hidden="true">
								<use xlink:href="#csdnc-m-passwords-visible"></use>
							</svg>
							6178</span>
						</p>
					</div>
				</a>
					<p class="content">
						<a href="https://blog.csdn.net/hacker2025/article/details/73252600" target="_blank" title="Python3处理HTTP请求">
							<span class="desc oneline">Python3处理HTTP请求的包：http.client，urllib，urllib3，requests
其中，http 比较 low-level，一般不直接使用
urllib更 high-leve...</span>
						</a>
                        						<span class="blog_title_box oneline"><a target="_blank" href="https://blog.csdn.net/hacker2025">来自：	<span class="blog_title"> 南宫米奇</span></a></span>
                        					</p>
			</div>
					</div>
	
    
	    
    		<div class="recommend-item-box recommend-box-ident type_blog clearfix" data-track-view='{"mod":"popu_614","con":",https://blog.csdn.net/lmb1612977696/article/details/78600892,BlogCommendFromBaidu_36"}' data-track-click='{"mod":"popu_614","con":",https://blog.csdn.net/lmb1612977696/article/details/78600892,BlogCommendFromBaidu_36"}'>
			<div class="content">
				<a href="https://blog.csdn.net/lmb1612977696/article/details/78600892" target="_blank" title="python3发起一个http请求">
				<h4 class="text-truncate oneline">
						<em>python3</em>发起一个http请求				</h4>
				<div class="info-box d-flex align-content-center">
					<!-- <p class="avatar">
							<img src="https://avatar.csdn.net/0/9/E/3_lmb1612977696.jpg" alt="lmb1612977696" class="avatar-pic">
							<span class="namebox">
								<span class="name">lmb1612977696</span>
								<span class="triangle"></span>
							</span>
					</p> -->
					<p class="date-and-readNum">
						<span class="date hover-show">11-22</span>
						<span class="read-num hover-hide">
							<svg class="icon csdnc-yuedushu" aria-hidden="true">
								<use xlink:href="#csdnc-m-passwords-visible"></use>
							</svg>
							2318</span>
						</p>
					</div>
				</a>
					<p class="content">
						<a href="https://blog.csdn.net/lmb1612977696/article/details/78600892" target="_blank" title="python3发起一个http请求">
							<span class="desc oneline">python3发起一个http请求例子：import json
from urllib import parse,request

def getOpenRoomList():
    textmod...</span>
						</a>
                        						<span class="blog_title_box oneline"><a target="_blank" href="https://blog.csdn.net/lmb1612977696">来自：	<span class="blog_title"> 幻想之渔</span></a></span>
                        					</p>
			</div>
					</div>
	
    
	    
    		<div class="recommend-item-box recommend-box-ident type_blog clearfix" data-track-view='{"mod":"popu_614","con":",https://blog.csdn.net/chasejava/article/details/79929011,BlogCommendFromBaidu_37"}' data-track-click='{"mod":"popu_614","con":",https://blog.csdn.net/chasejava/article/details/79929011,BlogCommendFromBaidu_37"}'>
			<div class="content">
				<a href="https://blog.csdn.net/chasejava/article/details/79929011" target="_blank" title="使用requests模拟登录知乎">
				<h4 class="text-truncate oneline">
						<em>使用</em><em>requests</em><em>模拟</em>登录知乎				</h4>
				<div class="info-box d-flex align-content-center">
					<!-- <p class="avatar">
							<img src="https://avatar.csdn.net/4/3/7/3_chasejava.jpg" alt="chasejava" class="avatar-pic">
							<span class="namebox">
								<span class="name">chasejava</span>
								<span class="triangle"></span>
							</span>
					</p> -->
					<p class="date-and-readNum">
						<span class="date hover-show">04-13</span>
						<span class="read-num hover-hide">
							<svg class="icon csdnc-yuedushu" aria-hidden="true">
								<use xlink:href="#csdnc-m-passwords-visible"></use>
							</svg>
							179</span>
						</p>
					</div>
				</a>
					<p class="content">
						<a href="https://blog.csdn.net/chasejava/article/details/79929011" target="_blank" title="使用requests模拟登录知乎">
							<span class="desc oneline"># -*- coding:UTF-8 -*-参考 https://github.com/weldon2010/Python/blob/master/login_zhihu.py  import req...</span>
						</a>
                        						<span class="blog_title_box oneline"><a target="_blank" href="https://blog.csdn.net/chasejava">来自：	<span class="blog_title"> chasejava的博客</span></a></span>
                        					</p>
			</div>
					</div>
	
    
	    
    		<div class="recommend-item-box recommend-box-ident type_blog clearfix" data-track-view='{"mod":"popu_614","con":",https://blog.csdn.net/u011798443/article/details/80974166,BlogCommendFromBaidu_38"}' data-track-click='{"mod":"popu_614","con":",https://blog.csdn.net/u011798443/article/details/80974166,BlogCommendFromBaidu_38"}'>
			<div class="content">
				<a href="https://blog.csdn.net/u011798443/article/details/80974166" target="_blank" title="python3远程连接SQL-server">
				<h4 class="text-truncate oneline">
						<em>python3</em>远程连接SQL-server				</h4>
				<div class="info-box d-flex align-content-center">
					<!-- <p class="avatar">
							<img src="https://avatar.csdn.net/9/6/4/3_u011798443.jpg" alt="u011798443" class="avatar-pic">
							<span class="namebox">
								<span class="name">u011798443</span>
								<span class="triangle"></span>
							</span>
					</p> -->
					<p class="date-and-readNum">
						<span class="date hover-show">07-09</span>
						<span class="read-num hover-hide">
							<svg class="icon csdnc-yuedushu" aria-hidden="true">
								<use xlink:href="#csdnc-m-passwords-visible"></use>
							</svg>
							790</span>
						</p>
					</div>
				</a>
					<p class="content">
						<a href="https://blog.csdn.net/u011798443/article/details/80974166" target="_blank" title="python3远程连接SQL-server">
							<span class="desc oneline">首先需要python安装一个模块： pymssql 模块。直接pip安装就好了！我已经安装过了。接下来就是主要代码了：import pymssql
class linkDB():
	def linkd...</span>
						</a>
                        						<span class="blog_title_box oneline"><a target="_blank" href="https://blog.csdn.net/u011798443">来自：	<span class="blog_title"> 菜鸟猿小天</span></a></span>
                        					</p>
			</div>
					</div>
	
    <div class="recommend-item-box recommend-ad-box"><script type="text/javascript" src="//rabc1.iteye.com/production/res/rxjg.js?pkcgstj=jm"></script></div>
	    
    		<div class="recommend-item-box recommend-box-ident type_blog clearfix" data-track-view='{"mod":"popu_614","con":",https://blog.csdn.net/lantiancaiyun/article/details/50983371,BlogCommendFromQuerySearch_39"}' data-track-click='{"mod":"popu_614","con":",https://blog.csdn.net/lantiancaiyun/article/details/50983371,BlogCommendFromQuerySearch_39"}'>
			<div class="content">
				<a href="https://blog.csdn.net/lantiancaiyun/article/details/50983371" target="_blank" title="requests模拟ajax异步请求">
				<h4 class="text-truncate oneline">
						<em>requests</em><em>模拟</em>ajax异步请求				</h4>
				<div class="info-box d-flex align-content-center">
					<!-- <p class="avatar">
							<img src="https://avatar.csdn.net/1/2/7/3_lantiancaiyun.jpg" alt="lantiancaiyun" class="avatar-pic">
							<span class="namebox">
								<span class="name">lantiancaiyun</span>
								<span class="triangle"></span>
							</span>
					</p> -->
					<p class="date-and-readNum">
						<span class="date hover-show">03-25</span>
						<span class="read-num hover-hide">
							<svg class="icon csdnc-yuedushu" aria-hidden="true">
								<use xlink:href="#csdnc-m-passwords-visible"></use>
							</svg>
							4614</span>
						</p>
					</div>
				</a>
					<p class="content">
						<a href="https://blog.csdn.net/lantiancaiyun/article/details/50983371" target="_blank" title="requests模拟ajax异步请求">
							<span class="desc oneline">requests
python
ajax</span>
						</a>
                        					</p>
			</div>
					</div>
	
    
	    
    		<div class="recommend-item-box recommend-box-ident type_blog clearfix" data-track-view='{"mod":"popu_614","con":",https://blog.csdn.net/phplaoniao/article/details/79039772,BlogCommendFromQuerySearch_40"}' data-track-click='{"mod":"popu_614","con":",https://blog.csdn.net/phplaoniao/article/details/79039772,BlogCommendFromQuerySearch_40"}'>
			<div class="content">
				<a href="https://blog.csdn.net/phplaoniao/article/details/79039772" target="_blank" title="python中使用requests 模拟浏览器发送请求数据">
				<h4 class="text-truncate oneline">
						python中<em>使用</em><em>requests</em> <em>模拟</em>浏览器发送请求数据				</h4>
				<div class="info-box d-flex align-content-center">
					<!-- <p class="avatar">
							<img src="https://avatar.csdn.net/7/B/4/3_phplaoniao.jpg" alt="phplaoniao" class="avatar-pic">
							<span class="namebox">
								<span class="name">phplaoniao</span>
								<span class="triangle"></span>
							</span>
					</p> -->
					<p class="date-and-readNum">
						<span class="date hover-show">01-12</span>
						<span class="read-num hover-hide">
							<svg class="icon csdnc-yuedushu" aria-hidden="true">
								<use xlink:href="#csdnc-m-passwords-visible"></use>
							</svg>
							2777</span>
						</p>
					</div>
				</a>
					<p class="content">
						<a href="https://blog.csdn.net/phplaoniao/article/details/79039772" target="_blank" title="python中使用requests 模拟浏览器发送请求数据">
							<span class="desc oneline">import requests

url='http://####'
proxy={'http':'http://####:80'}
headers={
    &quot;Accept&quot;:&quot;text/html...</span>
						</a>
                        						<span class="blog_title_box oneline"><a target="_blank" href="https://blog.csdn.net/phplaoniao">来自：	<span class="blog_title"> phplaoniao的博客</span></a></span>
                        					</p>
			</div>
					</div>
	
    
	    
    		<div class="recommend-item-box recommend-box-ident type_blog clearfix" data-track-view='{"mod":"popu_614","con":",https://blog.csdn.net/qq_32106647/article/details/78248143,BlogCommendFromQuerySearch_41"}' data-track-click='{"mod":"popu_614","con":",https://blog.csdn.net/qq_32106647/article/details/78248143,BlogCommendFromQuerySearch_41"}'>
			<div class="content">
				<a href="https://blog.csdn.net/qq_32106647/article/details/78248143" target="_blank" title="【Java基础Demo】模仿用户登录">
				<h4 class="text-truncate oneline">
						【Java<em>基础</em>Demo】模仿<em>用户登录</em>				</h4>
				<div class="info-box d-flex align-content-center">
					<!-- <p class="avatar">
							<img src="https://avatar.csdn.net/B/C/5/3_qq_32106647.jpg" alt="qq_32106647" class="avatar-pic">
							<span class="namebox">
								<span class="name">qq_32106647</span>
								<span class="triangle"></span>
							</span>
					</p> -->
					<p class="date-and-readNum">
						<span class="date hover-show">10-16</span>
						<span class="read-num hover-hide">
							<svg class="icon csdnc-yuedushu" aria-hidden="true">
								<use xlink:href="#csdnc-m-passwords-visible"></use>
							</svg>
							274</span>
						</p>
					</div>
				</a>
					<p class="content">
						<a href="https://blog.csdn.net/qq_32106647/article/details/78248143" target="_blank" title="【Java基础Demo】模仿用户登录">
							<span class="desc oneline">基于用户从控制台输入模拟的简陋的用户登录验证Demo：
import java.util.Scanner;public class Login {    public static void main...</span>
						</a>
                        						<span class="blog_title_box oneline"><a target="_blank" href="https://blog.csdn.net/qq_32106647">来自：	<span class="blog_title"> qq_32106647的博客</span></a></span>
                        					</p>
			</div>
					</div>
	
    
	    
    		<div class="recommend-item-box recommend-box-ident type_blog clearfix" data-track-view='{"mod":"popu_614","con":",https://blog.csdn.net/explorer9607/article/details/83149408,BlogCommendFromQuerySearch_42"}' data-track-click='{"mod":"popu_614","con":",https://blog.csdn.net/explorer9607/article/details/83149408,BlogCommendFromQuerySearch_42"}'>
			<div class="content">
				<a href="https://blog.csdn.net/explorer9607/article/details/83149408" target="_blank" title="python3.x爬虫 urllib和requests实现模拟登陆的具体步骤详解">
				<h4 class="text-truncate oneline">
						<em>python3</em>.x爬虫 urllib和<em>requests</em><em>实现</em><em>模拟</em>登陆的具体步骤详解				</h4>
				<div class="info-box d-flex align-content-center">
					<!-- <p class="avatar">
							<img src="https://avatar.csdn.net/C/D/C/3_explorer9607.jpg" alt="explorer9607" class="avatar-pic">
							<span class="namebox">
								<span class="name">explorer9607</span>
								<span class="triangle"></span>
							</span>
					</p> -->
					<p class="date-and-readNum">
						<span class="date hover-show">10-18</span>
						<span class="read-num hover-hide">
							<svg class="icon csdnc-yuedushu" aria-hidden="true">
								<use xlink:href="#csdnc-m-passwords-visible"></use>
							</svg>
							55</span>
						</p>
					</div>
				</a>
					<p class="content">
						<a href="https://blog.csdn.net/explorer9607/article/details/83149408" target="_blank" title="python3.x爬虫 urllib和requests实现模拟登陆的具体步骤详解">
							<span class="desc oneline">对于为什么用模拟登陆不用我多说，有些网站只有你登陆进去之后才可以看到内容，而没登录的话爬下来的网页一般只有登陆界面的那一点，所以对于这种网站，就需要能够模拟登陆的状态去爬取页面信息

实现模拟登陆总体...</span>
						</a>
                        						<span class="blog_title_box oneline"><a target="_blank" href="https://blog.csdn.net/explorer9607">来自：	<span class="blog_title"> explorer9607的博客</span></a></span>
                        					</p>
			</div>
					</div>
	
    
	    
    		<div class="recommend-item-box recommend-box-ident type_blog clearfix" data-track-view='{"mod":"popu_614","con":",https://blog.csdn.net/hi_chen_xingwang/article/details/51866781,BlogCommendFromQuerySearch_43"}' data-track-click='{"mod":"popu_614","con":",https://blog.csdn.net/hi_chen_xingwang/article/details/51866781,BlogCommendFromQuerySearch_43"}'>
			<div class="content">
				<a href="https://blog.csdn.net/hi_chen_xingwang/article/details/51866781" target="_blank" title="python 模拟ajax请求">
				<h4 class="text-truncate oneline">
						python <em>模拟</em>ajax请求				</h4>
				<div class="info-box d-flex align-content-center">
					<!-- <p class="avatar">
							<img src="https://avatar.csdn.net/0/A/C/3_hi_chen_xingwang.jpg" alt="hi_chen_xingwang" class="avatar-pic">
							<span class="namebox">
								<span class="name">hi_chen_xingwang</span>
								<span class="triangle"></span>
							</span>
					</p> -->
					<p class="date-and-readNum">
						<span class="date hover-show">07-09</span>
						<span class="read-num hover-hide">
							<svg class="icon csdnc-yuedushu" aria-hidden="true">
								<use xlink:href="#csdnc-m-passwords-visible"></use>
							</svg>
							3383</span>
						</p>
					</div>
				</a>
					<p class="content">
						<a href="https://blog.csdn.net/hi_chen_xingwang/article/details/51866781" target="_blank" title="python 模拟ajax请求">
							<span class="desc oneline">python 模拟ajax请求</span>
						</a>
                        						<span class="blog_title_box oneline"><a target="_blank" href="https://blog.csdn.net/hi_chen_xingwang">来自：	<span class="blog_title"> hi_chen_xingwang的博客</span></a></span>
                        					</p>
			</div>
					</div>
	
    <div class="recommend-item-box recommend-ad-box"><div id="kp_box_67" data-pid="67" data-track-view='{"mod":"kp_popu_67-653","con":",,"}' data-track-click='{"mod":"kp_popu_67-653","con":",,"}'><div id="three_ad43" class="mediav_ad" ></div>
<script>
                                               NEWS_FEED({
                w: 900,
                h : 84,
                showid : '9gAEHz',
                placeholderId: "three_ad43",
                inject : 'define',
                define : {
                    imagePosition : 'left',
                    imageBorderRadius : 3,
                    imageWidth: 90,
                    imageHeight: 60,
                    imageFill : 'clip',
                    displayImage : true,
                    displayTitle : true,
                    titleFontSize: 16,
                    titleFontColor: '#000',
                    titleFontFamily : 'Microsoft Yahei',
                    titleFontWeight: 'bold',
                    titlePaddingTop : 0,
                    titlePaddingRight : 0,
                    titlePaddingBottom : 5,
                    titlePaddingLeft : 16,
                    displayDesc : true,
                    descFontSize: 12,
                    descFontColor: '#8e959a',
                    descFontFamily : 'Microsoft Yahei',
                    paddingTop : 10,
                    paddingRight : 0,
                    paddingBottom : 0,
                    paddingLeft : 0,
                    backgroundColor: '#fff',
                    hoverColor: '#000'
                      }
                  })
                                        </script></div></div>
	    
    		<div class="recommend-item-box recommend-box-ident type_blog clearfix" data-track-view='{"mod":"popu_614","con":",https://blog.csdn.net/Marksinoberg/article/details/69569353,BlogCommendFromBaidu_44"}' data-track-click='{"mod":"popu_614","con":",https://blog.csdn.net/Marksinoberg/article/details/69569353,BlogCommendFromBaidu_44"}'>
			<div class="content">
				<a href="https://blog.csdn.net/Marksinoberg/article/details/69569353" target="_blank" title="Python 模拟登录知乎">
				<h4 class="text-truncate oneline">
						Python <em>模拟</em>登录知乎				</h4>
				<div class="info-box d-flex align-content-center">
					<!-- <p class="avatar">
							<img src="https://avatar.csdn.net/0/8/F/3_marksinoberg.jpg" alt="Marksinoberg" class="avatar-pic">
							<span class="namebox">
								<span class="name">Marksinoberg</span>
								<span class="triangle"></span>
							</span>
					</p> -->
					<p class="date-and-readNum">
						<span class="date hover-show">04-07</span>
						<span class="read-num hover-hide">
							<svg class="icon csdnc-yuedushu" aria-hidden="true">
								<use xlink:href="#csdnc-m-passwords-visible"></use>
							</svg>
							1.2万</span>
						</p>
					</div>
				</a>
					<p class="content">
						<a href="https://blog.csdn.net/Marksinoberg/article/details/69569353" target="_blank" title="Python 模拟登录知乎">
							<span class="desc oneline">前言
必备知识点
headers
Referer
User-Agent
隐藏域
其他
模拟登录
模拟防爬
服务器端
loginphp
loginhtml
浏览器测试
正常提交用户名密码的话如下
用户名...</span>
						</a>
                        						<span class="blog_title_box oneline"><a target="_blank" href="https://blog.csdn.net/Marksinoberg">来自：	<span class="blog_title"> 更上一层楼！</span></a></span>
                        					</p>
			</div>
					</div>
	
    
	    
    		<div class="recommend-item-box recommend-box-ident type_blog clearfix" data-track-view='{"mod":"popu_614","con":",https://blog.csdn.net/phpzhi/article/details/80631650,BlogCommendFromBaidu_45"}' data-track-click='{"mod":"popu_614","con":",https://blog.csdn.net/phpzhi/article/details/80631650,BlogCommendFromBaidu_45"}'>
			<div class="content">
				<a href="https://blog.csdn.net/phpzhi/article/details/80631650" target="_blank" title="Python3实现网站模拟登录">
				<h4 class="text-truncate oneline">
						<em>Python3</em><em>实现</em>网站<em>模拟</em>登录				</h4>
				<div class="info-box d-flex align-content-center">
					<!-- <p class="avatar">
							<img src="https://avatar.csdn.net/F/7/B/3_phpzhi.jpg" alt="phpzhi" class="avatar-pic">
							<span class="namebox">
								<span class="name">phpzhi</span>
								<span class="triangle"></span>
							</span>
					</p> -->
					<p class="date-and-readNum">
						<span class="date hover-show">06-09</span>
						<span class="read-num hover-hide">
							<svg class="icon csdnc-yuedushu" aria-hidden="true">
								<use xlink:href="#csdnc-m-passwords-visible"></use>
							</svg>
							473</span>
						</p>
					</div>
				</a>
					<p class="content">
						<a href="https://blog.csdn.net/phpzhi/article/details/80631650" target="_blank" title="Python3实现网站模拟登录">
							<span class="desc oneline">一、使用selenium和Chrome模拟登录



# -*- coding:utf-8 -*-
# python3.6+selenium3.12+chrome65+Chrome驱动chromedr...</span>
						</a>
                        						<span class="blog_title_box oneline"><a target="_blank" href="https://blog.csdn.net/phpzhi">来自：	<span class="blog_title"> phpzhi的博客</span></a></span>
                        					</p>
			</div>
					</div>
	
    
	    
    		<div class="recommend-item-box recommend-box-ident type_blog clearfix" data-track-view='{"mod":"popu_614","con":",https://blog.csdn.net/qq_27099139/article/details/79851259,BlogCommendFromBaidu_46"}' data-track-click='{"mod":"popu_614","con":",https://blog.csdn.net/qq_27099139/article/details/79851259,BlogCommendFromBaidu_46"}'>
			<div class="content">
				<a href="https://blog.csdn.net/qq_27099139/article/details/79851259" target="_blank" title="python3爬虫学习笔记之模拟淘宝登录">
				<h4 class="text-truncate oneline">
						<em>python3</em>爬虫学习笔记之<em>模拟</em>淘宝登录				</h4>
				<div class="info-box d-flex align-content-center">
					<!-- <p class="avatar">
							<img src="https://avatar.csdn.net/7/C/B/3_qq_27099139.jpg" alt="qq_27099139" class="avatar-pic">
							<span class="namebox">
								<span class="name">qq_27099139</span>
								<span class="triangle"></span>
							</span>
					</p> -->
					<p class="date-and-readNum">
						<span class="date hover-show">04-08</span>
						<span class="read-num hover-hide">
							<svg class="icon csdnc-yuedushu" aria-hidden="true">
								<use xlink:href="#csdnc-m-passwords-visible"></use>
							</svg>
							2225</span>
						</p>
					</div>
				</a>
					<p class="content">
						<a href="https://blog.csdn.net/qq_27099139/article/details/79851259" target="_blank" title="python3爬虫学习笔记之模拟淘宝登录">
							<span class="desc oneline">准备工作使用chrome f12调试模式，抓包查看淘宝登录的整个流程，并查看post请求的数据值得注意的是，淘宝用的是gbk编码说明此版本没有处理验证码，只是单纯的登录具体的流程和实现都在代码注释中代...</span>
						</a>
                        						<span class="blog_title_box oneline"><a target="_blank" href="https://blog.csdn.net/qq_27099139">来自：	<span class="blog_title"> 小小前端大思维</span></a></span>
                        					</p>
			</div>
					</div>
	
    
	    
    		<div class="recommend-item-box recommend-box-ident type_blog clearfix" data-track-view='{"mod":"popu_614","con":",https://blog.csdn.net/u011061889/article/details/72904821,BlogCommendFromBaidu_47"}' data-track-click='{"mod":"popu_614","con":",https://blog.csdn.net/u011061889/article/details/72904821,BlogCommendFromBaidu_47"}'>
			<div class="content">
				<a href="https://blog.csdn.net/u011061889/article/details/72904821" target="_blank" title="使用Python的Requests包模拟登陆">
				<h4 class="text-truncate oneline">
						<em>使用</em>Python的<em>Requests</em>包<em>模拟</em>登陆				</h4>
				<div class="info-box d-flex align-content-center">
					<!-- <p class="avatar">
							<img src="https://avatar.csdn.net/6/4/8/3_u011061889.jpg" alt="u011061889" class="avatar-pic">
							<span class="namebox">
								<span class="name">u011061889</span>
								<span class="triangle"></span>
							</span>
					</p> -->
					<p class="date-and-readNum">
						<span class="date hover-show">06-07</span>
						<span class="read-num hover-hide">
							<svg class="icon csdnc-yuedushu" aria-hidden="true">
								<use xlink:href="#csdnc-m-passwords-visible"></use>
							</svg>
							1.1万</span>
						</p>
					</div>
				</a>
					<p class="content">
						<a href="https://blog.csdn.net/u011061889/article/details/72904821" target="_blank" title="使用Python的Requests包模拟登陆">
							<span class="desc oneline">前段时间喜欢用python去抓一些页面玩，但都基本上都是用get请求一些页面，再通过正则去过滤。 
今天试了一下，模拟登陆个人网站。发现也比较简单。读懂本文需要对http协议和http会话有一定的理解...</span>
						</a>
                        						<span class="blog_title_box oneline"><a target="_blank" href="https://blog.csdn.net/u011061889">来自：	<span class="blog_title"> Richie</span></a></span>
                        					</p>
			</div>
					</div>
	
    
	    
    		<div class="recommend-item-box recommend-box-ident type_blog clearfix" data-track-view='{"mod":"popu_614","con":",https://blog.csdn.net/hui1788/article/details/79944102,BlogCommendFromBaidu_48"}' data-track-click='{"mod":"popu_614","con":",https://blog.csdn.net/hui1788/article/details/79944102,BlogCommendFromBaidu_48"}'>
			<div class="content">
				<a href="https://blog.csdn.net/hui1788/article/details/79944102" target="_blank" title="requests模拟登录的三种方法">
				<h4 class="text-truncate oneline">
						<em>requests</em><em>模拟</em>登录的三种方法				</h4>
				<div class="info-box d-flex align-content-center">
					<!-- <p class="avatar">
							<img src="https://avatar.csdn.net/3/E/9/3_hui1788.jpg" alt="hui1788" class="avatar-pic">
							<span class="namebox">
								<span class="name">hui1788</span>
								<span class="triangle"></span>
							</span>
					</p> -->
					<p class="date-and-readNum">
						<span class="date hover-show">04-14</span>
						<span class="read-num hover-hide">
							<svg class="icon csdnc-yuedushu" aria-hidden="true">
								<use xlink:href="#csdnc-m-passwords-visible"></use>
							</svg>
							2030</span>
						</p>
					</div>
				</a>
					<p class="content">
						<a href="https://blog.csdn.net/hui1788/article/details/79944102" target="_blank" title="requests模拟登录的三种方法">
							<span class="desc oneline"> 1.利用session模拟登陆首先我们看一下requests中session的使用方法我们来爬一下人人网首页的代码，其代码如下：其中post_url是我们点击登陆时，该页面需要跳转的页面url，具体...</span>
						</a>
                        						<span class="blog_title_box oneline"><a target="_blank" href="https://blog.csdn.net/hui1788">来自：	<span class="blog_title"> coolbas的专栏</span></a></span>
                        					</p>
			</div>
					</div>
	
    <div class="recommend-item-box recommend-ad-box"><div id="kp_box_68" data-pid="68" data-track-view='{"mod":"kp_popu_68-654","con":",,"}' data-track-click='{"mod":"kp_popu_68-654","con":",,"}'><div id="three_ad48" class="mediav_ad" ></div>
<script>
                                               NEWS_FEED({
                w: 900,
                h : 84,
                showid : 'Afihld',
                placeholderId: "three_ad48",
                inject : 'define',
                define : {
                    imagePosition : 'left',
                    imageBorderRadius : 3,
                    imageWidth: 90,
                    imageHeight: 60,
                    imageFill : 'clip',
                    displayImage : true,
                    displayTitle : true,
                    titleFontSize: 16,
                    titleFontColor: '#000',
                    titleFontFamily : 'Microsoft Yahei',
                    titleFontWeight: 'bold',
                    titlePaddingTop : 0,
                    titlePaddingRight : 0,
                    titlePaddingBottom : 5,
                    titlePaddingLeft : 16,
                    displayDesc : true,
                    descFontSize: 14,
                    descFontColor: '#8e959a',
                    descFontFamily : 'Microsoft Yahei',
                    paddingTop : 10,
                    paddingRight : 0,
                    paddingBottom : 0,
                    paddingLeft : 0,
                    backgroundColor: '#fff',
                    hoverColor: '#000'
                      }
                  })
                                        </script></div></div>
	    
    		<div class="recommend-item-box recommend-box-ident type_blog clearfix" data-track-view='{"mod":"popu_614","con":",https://blog.csdn.net/kelvinLLL/article/details/59129586,BlogCommendFromBaidu_49"}' data-track-click='{"mod":"popu_614","con":",https://blog.csdn.net/kelvinLLL/article/details/59129586,BlogCommendFromBaidu_49"}'>
			<div class="content">
				<a href="https://blog.csdn.net/kelvinLLL/article/details/59129586" target="_blank" title="Python爬虫实战——蚂蜂窝国内目的地全抓取">
				<h4 class="text-truncate oneline">
						Python爬虫实战——蚂蜂窝国内目的地全抓取				</h4>
				<div class="info-box d-flex align-content-center">
					<!-- <p class="avatar">
							<img src="https://avatar.csdn.net/C/9/E/3_kelvinlll.jpg" alt="kelvinLLL" class="avatar-pic">
							<span class="namebox">
								<span class="name">kelvinLLL</span>
								<span class="triangle"></span>
							</span>
					</p> -->
					<p class="date-and-readNum">
						<span class="date hover-show">03-01</span>
						<span class="read-num hover-hide">
							<svg class="icon csdnc-yuedushu" aria-hidden="true">
								<use xlink:href="#csdnc-m-passwords-visible"></use>
							</svg>
							2985</span>
						</p>
					</div>
				</a>
					<p class="content">
						<a href="https://blog.csdn.net/kelvinLLL/article/details/59129586" target="_blank" title="Python爬虫实战——蚂蜂窝国内目的地全抓取">
							<span class="desc oneline">上一篇文章爬的是豆瓣电影，是属于静态页面的，而且很有规律的，做起来比较容易。这次的蚂蜂窝国内目的主要有三点比较困难的地方
1.不是静态页面，要通过post请求才能获得需要的信息，通过刷新网页可以看到...</span>
						</a>
                        						<span class="blog_title_box oneline"><a target="_blank" href="https://blog.csdn.net/kelvinLLL">来自：	<span class="blog_title"> kelvinLLL的博客</span></a></span>
                        					</p>
			</div>
					</div>
	
    
	    
    		<div class="recommend-item-box recommend-box-ident type_blog clearfix" data-track-view='{"mod":"popu_614","con":",https://blog.csdn.net/diandianxiyu/article/details/53068012,BlogCommendHotData_0"}' data-track-click='{"mod":"popu_614","con":",https://blog.csdn.net/diandianxiyu/article/details/53068012,BlogCommendHotData_0"}'>
			<div class="content">
				<a href="https://blog.csdn.net/diandianxiyu/article/details/53068012" target="_blank" title="【小程序】微信小程序开发实践">
				<h4 class="text-truncate oneline">
						【小程序】微信小程序开发实践				</h4>
				<div class="info-box d-flex align-content-center">
					<!-- <p class="avatar">
							<img src="" alt="diandianxiyu" class="avatar-pic">
							<span class="namebox">
								<span class="name">diandianxiyu</span>
								<span class="triangle"></span>
							</span>
					</p> -->
					<p class="date-and-readNum">
						<span class="date hover-show">11-07</span>
						<span class="read-num hover-hide">
							<svg class="icon csdnc-yuedushu" aria-hidden="true">
								<use xlink:href="#csdnc-m-passwords-visible"></use>
							</svg>
							19531</span>
						</p>
					</div>
				</a>
					<p class="content">
						<a href="https://blog.csdn.net/diandianxiyu/article/details/53068012" target="_blank" title="【小程序】微信小程序开发实践">
							<span class="desc oneline">帐号相关流程注册范围
企业
政府
媒体
其他组织换句话讲就是不让个人开发者注册。 :)填写企业信息不能使用和之前的公众号账户相同的邮箱,也就是说小程序是和微信公众号一个层级的。填写公司机构信息,对公账...</span>
						</a>
                        						<span class="blog_title_box oneline"><a target="_blank" href="https://blog.csdn.net/diandianxiyu">来自：	<span class="blog_title"> 小雨同学的技术博客</span></a></span>
                        					</p>
			</div>
					</div>
	
    
	    
    		<div class="recommend-item-box recommend-box-ident type_blog clearfix" data-track-view='{"mod":"popu_614","con":",https://blog.csdn.net/u012968002/article/details/78958090,BlogCommendHotData_1"}' data-track-click='{"mod":"popu_614","con":",https://blog.csdn.net/u012968002/article/details/78958090,BlogCommendHotData_1"}'>
			<div class="content">
				<a href="https://blog.csdn.net/u012968002/article/details/78958090" target="_blank" title="CAFFE -FCN训练配置过程">
				<h4 class="text-truncate oneline">
						CAFFE -FCN训练配置过程				</h4>
				<div class="info-box d-flex align-content-center">
					<!-- <p class="avatar">
							<img src="" alt="u012968002" class="avatar-pic">
							<span class="namebox">
								<span class="name">u012968002</span>
								<span class="triangle"></span>
							</span>
					</p> -->
					<p class="date-and-readNum">
						<span class="date hover-show">01-03</span>
						<span class="read-num hover-hide">
							<svg class="icon csdnc-yuedushu" aria-hidden="true">
								<use xlink:href="#csdnc-m-passwords-visible"></use>
							</svg>
							2375</span>
						</p>
					</div>
				</a>
					<p class="content">
						<a href="https://blog.csdn.net/u012968002/article/details/78958090" target="_blank" title="CAFFE -FCN训练配置过程">
							<span class="desc oneline">转载自 http://blog.csdn.net/jiongnima/article/details/78549326?locationNum=3&amp;fps=1


   在2015年发表于计算机...</span>
						</a>
                        						<span class="blog_title_box oneline"><a target="_blank" href="https://blog.csdn.net/u012968002">来自：	<span class="blog_title"> JIN JI 2013.12.24</span></a></span>
                        					</p>
			</div>
					</div>
	
    
	    
    		<div class="recommend-item-box recommend-box-ident type_blog clearfix" data-track-view='{"mod":"popu_614","con":",https://blog.csdn.net/aoshilang2249/article/details/46956163,BlogCommendHotData_2"}' data-track-click='{"mod":"popu_614","con":",https://blog.csdn.net/aoshilang2249/article/details/46956163,BlogCommendHotData_2"}'>
			<div class="content">
				<a href="https://blog.csdn.net/aoshilang2249/article/details/46956163" target="_blank" title="PHP jpgraph库的配置及生成统计图表:折线图、柱状图、饼状图等">
				<h4 class="text-truncate oneline">
						PHP jpgraph库的配置及生成统计图表:折线图、柱状图、饼状图等				</h4>
				<div class="info-box d-flex align-content-center">
					<!-- <p class="avatar">
							<img src="" alt="aoshilang2249" class="avatar-pic">
							<span class="namebox">
								<span class="name">aoshilang2249</span>
								<span class="triangle"></span>
							</span>
					</p> -->
					<p class="date-and-readNum">
						<span class="date hover-show">07-19</span>
						<span class="read-num hover-hide">
							<svg class="icon csdnc-yuedushu" aria-hidden="true">
								<use xlink:href="#csdnc-m-passwords-visible"></use>
							</svg>
							17166</span>
						</p>
					</div>
				</a>
					<p class="content">
						<a href="https://blog.csdn.net/aoshilang2249/article/details/46956163" target="_blank" title="PHP jpgraph库的配置及生成统计图表:折线图、柱状图、饼状图等">
							<span class="desc oneline">JpGraph简介

      JpGraph是开源的PHP统计图表生成库，基于PHP的GD2图形库构建，把生成统计图的相关操作封装，隐藏了部分复杂的操作，使在PHP页面上输出统计图表变得更加容...</span>
						</a>
                        						<span class="blog_title_box oneline"><a target="_blank" href="https://blog.csdn.net/aoshilang2249">来自：	<span class="blog_title"> 郎涯工作室</span></a></span>
                        					</p>
			</div>
					</div>
	
    
	    
    		<div class="recommend-item-box recommend-box-ident type_blog clearfix" data-track-view='{"mod":"popu_614","con":",https://blog.csdn.net/bestone0213/article/details/44307267,BlogCommendHotData_3"}' data-track-click='{"mod":"popu_614","con":",https://blog.csdn.net/bestone0213/article/details/44307267,BlogCommendHotData_3"}'>
			<div class="content">
				<a href="https://blog.csdn.net/bestone0213/article/details/44307267" target="_blank" title="追踪mysql操作记录时间1.">
				<h4 class="text-truncate oneline">
						追踪mysql操作记录时间1.				</h4>
				<div class="info-box d-flex align-content-center">
					<!-- <p class="avatar">
							<img src="" alt="bestone0213" class="avatar-pic">
							<span class="namebox">
								<span class="name">bestone0213</span>
								<span class="triangle"></span>
							</span>
					</p> -->
					<p class="date-and-readNum">
						<span class="date hover-show">03-16</span>
						<span class="read-num hover-hide">
							<svg class="icon csdnc-yuedushu" aria-hidden="true">
								<use xlink:href="#csdnc-m-passwords-visible"></use>
							</svg>
							2504</span>
						</p>
					</div>
				</a>
					<p class="content">
						<a href="https://blog.csdn.net/bestone0213/article/details/44307267" target="_blank" title="追踪mysql操作记录时间1.">
							<span class="desc oneline">测试环境莫名其妙有几条重要数据被删除了，由于在binlog里面只看到是公用账号删除的，无法查询是那个谁在那个时间段登录的，就考虑怎么记录每一个MYSQL账号的登录信息，在MYSQL中，每个连接都会先执...</span>
						</a>
                        						<span class="blog_title_box oneline"><a target="_blank" href="https://blog.csdn.net/bestone0213">来自：	<span class="blog_title"> 路在脚下</span></a></span>
                        					</p>
			</div>
					</div>
	
    
	    
    		<div class="recommend-item-box recommend-box-ident type_blog clearfix" data-track-view='{"mod":"popu_614","con":",https://blog.csdn.net/hj7jay/article/details/51302829,BlogCommendHotData_4"}' data-track-click='{"mod":"popu_614","con":",https://blog.csdn.net/hj7jay/article/details/51302829,BlogCommendHotData_4"}'>
			<div class="content">
				<a href="https://blog.csdn.net/hj7jay/article/details/51302829" target="_blank" title="Activiti数据库表结构(表详细版)">
				<h4 class="text-truncate oneline">
						Activiti数据库表结构(表详细版)				</h4>
				<div class="info-box d-flex align-content-center">
					<!-- <p class="avatar">
							<img src="" alt="hj7jay" class="avatar-pic">
							<span class="namebox">
								<span class="name">hj7jay</span>
								<span class="triangle"></span>
							</span>
					</p> -->
					<p class="date-and-readNum">
						<span class="date hover-show">05-03</span>
						<span class="read-num hover-hide">
							<svg class="icon csdnc-yuedushu" aria-hidden="true">
								<use xlink:href="#csdnc-m-passwords-visible"></use>
							</svg>
							68636</span>
						</p>
					</div>
				</a>
					<p class="content">
						<a href="https://blog.csdn.net/hj7jay/article/details/51302829" target="_blank" title="Activiti数据库表结构(表详细版)">
							<span class="desc oneline">版权声明：本文为博主原创文章，未经博主允许不得转载。不经过允许copy,讲追究法律责任，欢迎加入我们的学习提升群466355109，可以相互交流...</span>
						</a>
                        						<span class="blog_title_box oneline"><a target="_blank" href="https://blog.csdn.net/hj7jay">来自：	<span class="blog_title"> 程序猿开发日志【学习永无止境】</span></a></span>
                        					</p>
			</div>
					</div>
	
    
	    
    		<div class="recommend-item-box recommend-box-ident type_blog clearfix" data-track-view='{"mod":"popu_614","con":",https://blog.csdn.net/wuchengzeng/article/details/50037611,BlogCommendHotData_5"}' data-track-click='{"mod":"popu_614","con":",https://blog.csdn.net/wuchengzeng/article/details/50037611,BlogCommendHotData_5"}'>
			<div class="content">
				<a href="https://blog.csdn.net/wuchengzeng/article/details/50037611" target="_blank" title="jquery/js实现一个网页同时调用多个倒计时(最新的)">
				<h4 class="text-truncate oneline">
						jquery/js实现一个网页同时调用多个倒计时(最新的)				</h4>
				<div class="info-box d-flex align-content-center">
					<!-- <p class="avatar">
							<img src="" alt="wuchengzeng" class="avatar-pic">
							<span class="namebox">
								<span class="name">wuchengzeng</span>
								<span class="triangle"></span>
							</span>
					</p> -->
					<p class="date-and-readNum">
						<span class="date hover-show">11-25</span>
						<span class="read-num hover-hide">
							<svg class="icon csdnc-yuedushu" aria-hidden="true">
								<use xlink:href="#csdnc-m-passwords-visible"></use>
							</svg>
							4836</span>
						</p>
					</div>
				</a>
					<p class="content">
						<a href="https://blog.csdn.net/wuchengzeng/article/details/50037611" target="_blank" title="jquery/js实现一个网页同时调用多个倒计时(最新的)">
							<span class="desc oneline">jquery/js实现一个网页同时调用多个倒计时(最新的)
最近需要网页添加多个倒计时. 查阅网络,基本上都是千遍一律的不好用. 自己按需写了个.希望对大家有用. 有用请赞一个哦!...</span>
						</a>
                        						<span class="blog_title_box oneline"><a target="_blank" href="https://blog.csdn.net/wuchengzeng">来自：	<span class="blog_title"> websites</span></a></span>
                        					</p>
			</div>
					</div>
	
    
	    
    		<div class="recommend-item-box recommend-box-ident type_blog clearfix" data-track-view='{"mod":"popu_614","con":",https://blog.csdn.net/yu_xiaofei/article/details/13287899,BlogCommendHotData_6"}' data-track-click='{"mod":"popu_614","con":",https://blog.csdn.net/yu_xiaofei/article/details/13287899,BlogCommendHotData_6"}'>
			<div class="content">
				<a href="https://blog.csdn.net/yu_xiaofei/article/details/13287899" target="_blank" title="SNMP协议详解&lt;二&gt;">
				<h4 class="text-truncate oneline">
						SNMP协议详解&lt;二&gt;				</h4>
				<div class="info-box d-flex align-content-center">
					<!-- <p class="avatar">
							<img src="" alt="yu_xiaofei" class="avatar-pic">
							<span class="namebox">
								<span class="name">yu_xiaofei</span>
								<span class="triangle"></span>
							</span>
					</p> -->
					<p class="date-and-readNum">
						<span class="date hover-show">10-29</span>
						<span class="read-num hover-hide">
							<svg class="icon csdnc-yuedushu" aria-hidden="true">
								<use xlink:href="#csdnc-m-passwords-visible"></use>
							</svg>
							7270</span>
						</p>
					</div>
				</a>
					<p class="content">
						<a href="https://blog.csdn.net/yu_xiaofei/article/details/13287899" target="_blank" title="SNMP协议详解&lt;二&gt;">
							<span class="desc oneline">上一篇文章讲解了SNMP的基本架构，本篇文章将重点分析SNMP报文，并对不同版本（SNMPv1、v2c、v3）进行区别！

四、SNMP协议数据单元

在SNMP管理中，管理站（NMS）和代理（Age...</span>
						</a>
                        						<span class="blog_title_box oneline"><a target="_blank" href="https://blog.csdn.net/yu_xiaofei">来自：	<span class="blog_title"> 假装在纽约</span></a></span>
                        					</p>
			</div>
					</div>
	
    
	    
    		<div class="recommend-item-box recommend-box-ident type_blog clearfix" data-track-view='{"mod":"popu_614","con":",https://blog.csdn.net/stillit/article/details/26500847,BlogCommendHotData_7"}' data-track-click='{"mod":"popu_614","con":",https://blog.csdn.net/stillit/article/details/26500847,BlogCommendHotData_7"}'>
			<div class="content">
				<a href="https://blog.csdn.net/stillit/article/details/26500847" target="_blank" title="ORA-12518 TNS:监听程序无法分发客户机连接 解决办法">
				<h4 class="text-truncate oneline">
						ORA-12518 TNS:监听程序无法分发客户机连接 解决办法				</h4>
				<div class="info-box d-flex align-content-center">
					<!-- <p class="avatar">
							<img src="" alt="stillit" class="avatar-pic">
							<span class="namebox">
								<span class="name">stillit</span>
								<span class="triangle"></span>
							</span>
					</p> -->
					<p class="date-and-readNum">
						<span class="date hover-show">05-21</span>
						<span class="read-num hover-hide">
							<svg class="icon csdnc-yuedushu" aria-hidden="true">
								<use xlink:href="#csdnc-m-passwords-visible"></use>
							</svg>
							6432</span>
						</p>
					</div>
				</a>
					<p class="content">
						<a href="https://blog.csdn.net/stillit/article/details/26500847" target="_blank" title="ORA-12518 TNS:监听程序无法分发客户机连接 解决办法">
							<span class="desc oneline">环境 windows  server 2003 EP

专有服务器模式下processes值设的过小。可通过以下方法解决：

    1.cmd

    2.sqlplus

   ...</span>
						</a>
                        						<span class="blog_title_box oneline"><a target="_blank" href="https://blog.csdn.net/stillit">来自：	<span class="blog_title"> 薄刀刀_薄海_的技术博客</span></a></span>
                        					</p>
			</div>
					</div>
	
    
	    
    		<div class="recommend-item-box recommend-box-ident type_blog clearfix" data-track-view='{"mod":"popu_614","con":",https://blog.csdn.net/yuqinying112/article/details/7244281,BlogCommendHotData_8"}' data-track-click='{"mod":"popu_614","con":",https://blog.csdn.net/yuqinying112/article/details/7244281,BlogCommendHotData_8"}'>
			<div class="content">
				<a href="https://blog.csdn.net/yuqinying112/article/details/7244281" target="_blank" title="使用Spring进行面向切面编程">
				<h4 class="text-truncate oneline">
						使用Spring进行面向切面编程				</h4>
				<div class="info-box d-flex align-content-center">
					<!-- <p class="avatar">
							<img src="" alt="yuqinying112" class="avatar-pic">
							<span class="namebox">
								<span class="name">yuqinying112</span>
								<span class="triangle"></span>
							</span>
					</p> -->
					<p class="date-and-readNum">
						<span class="date hover-show">02-09</span>
						<span class="read-num hover-hide">
							<svg class="icon csdnc-yuedushu" aria-hidden="true">
								<use xlink:href="#csdnc-m-passwords-visible"></use>
							</svg>
							6524</span>
						</p>
					</div>
				</a>
					<p class="content">
						<a href="https://blog.csdn.net/yuqinying112/article/details/7244281" target="_blank" title="使用Spring进行面向切面编程">
							<span class="desc oneline">Chapter 6. 使用Spring进行面向切面编程（AOP）




6.1. 简介



面向切面编程（AOP）通过提供另外一种思考程序结构的途经来弥补面向对象编程（OOP）的...</span>
						</a>
                        					</p>
			</div>
					</div>
	
    
	    
    		<div class="recommend-item-box recommend-box-ident type_blog clearfix" data-track-view='{"mod":"popu_614","con":",https://blog.csdn.net/xu__cg/article/details/53190763,BlogCommendHotData_9"}' data-track-click='{"mod":"popu_614","con":",https://blog.csdn.net/xu__cg/article/details/53190763,BlogCommendHotData_9"}'>
			<div class="content">
				<a href="https://blog.csdn.net/xu__cg/article/details/53190763" target="_blank" title="Java设计模式18——状态模式">
				<h4 class="text-truncate oneline">
						Java设计模式18——状态模式				</h4>
				<div class="info-box d-flex align-content-center">
					<!-- <p class="avatar">
							<img src="" alt="xu__cg" class="avatar-pic">
							<span class="namebox">
								<span class="name">xu__cg</span>
								<span class="triangle"></span>
							</span>
					</p> -->
					<p class="date-and-readNum">
						<span class="date hover-show">11-16</span>
						<span class="read-num hover-hide">
							<svg class="icon csdnc-yuedushu" aria-hidden="true">
								<use xlink:href="#csdnc-m-passwords-visible"></use>
							</svg>
							1403</span>
						</p>
					</div>
				</a>
					<p class="content">
						<a href="https://blog.csdn.net/xu__cg/article/details/53190763" target="_blank" title="Java设计模式18——状态模式">
							<span class="desc oneline">一、定义状态(State)模式又称为状态对象模式(Pattern of Objects for State),状态模式是对象的行为模式。状态模式允许一个对象在其内部状态改变时改变其行为，用于解决系统中...</span>
						</a>
                        						<span class="blog_title_box oneline"><a target="_blank" href="https://blog.csdn.net/xu__cg">来自：	<span class="blog_title"> 小小本科生成长之路</span></a></span>
                        					</p>
			</div>
					</div>
	
    
	    
    		<div class="recommend-item-box recommend-box-ident type_blog clearfix" data-track-view='{"mod":"popu_614","con":",https://blog.csdn.net/qq_36892341/article/details/73918672,BlogCommendHotData_10"}' data-track-click='{"mod":"popu_614","con":",https://blog.csdn.net/qq_36892341/article/details/73918672,BlogCommendHotData_10"}'>
			<div class="content">
				<a href="https://blog.csdn.net/qq_36892341/article/details/73918672" target="_blank" title="linux上安装Docker(非常简单的安装方法)">
				<h4 class="text-truncate oneline">
						linux上安装Docker(非常简单的安装方法)				</h4>
				<div class="info-box d-flex align-content-center">
					<!-- <p class="avatar">
							<img src="" alt="qq_36892341" class="avatar-pic">
							<span class="namebox">
								<span class="name">qq_36892341</span>
								<span class="triangle"></span>
							</span>
					</p> -->
					<p class="date-and-readNum">
						<span class="date hover-show">06-29</span>
						<span class="read-num hover-hide">
							<svg class="icon csdnc-yuedushu" aria-hidden="true">
								<use xlink:href="#csdnc-m-passwords-visible"></use>
							</svg>
							77798</span>
						</p>
					</div>
				</a>
					<p class="content">
						<a href="https://blog.csdn.net/qq_36892341/article/details/73918672" target="_blank" title="linux上安装Docker(非常简单的安装方法)">
							<span class="desc oneline">最近比较有空，大四出来实习几个月了，作为实习狗的我，被叫去研究Docker了，汗汗！

Docker的三大核心概念：镜像、容器、仓库
镜像：类似虚拟机的镜像、用俗话说就是安装文件。
容器：类似一个轻量...</span>
						</a>
                        						<span class="blog_title_box oneline"><a target="_blank" href="https://blog.csdn.net/qq_36892341">来自：	<span class="blog_title"> 我走小路的博客</span></a></span>
                        					</p>
			</div>
					</div>
	
    
	    
    		<div class="recommend-item-box recommend-box-ident type_blog clearfix" data-track-view='{"mod":"popu_614","con":",https://blog.csdn.net/q383965374/article/details/41948467,BlogCommendHotData_11"}' data-track-click='{"mod":"popu_614","con":",https://blog.csdn.net/q383965374/article/details/41948467,BlogCommendHotData_11"}'>
			<div class="content">
				<a href="https://blog.csdn.net/q383965374/article/details/41948467" target="_blank" title="java通过struts实现web中的文件上传">
				<h4 class="text-truncate oneline">
						java通过struts实现web中的文件上传				</h4>
				<div class="info-box d-flex align-content-center">
					<!-- <p class="avatar">
							<img src="" alt="q383965374" class="avatar-pic">
							<span class="namebox">
								<span class="name">q383965374</span>
								<span class="triangle"></span>
							</span>
					</p> -->
					<p class="date-and-readNum">
						<span class="date hover-show">12-16</span>
						<span class="read-num hover-hide">
							<svg class="icon csdnc-yuedushu" aria-hidden="true">
								<use xlink:href="#csdnc-m-passwords-visible"></use>
							</svg>
							1342</span>
						</p>
					</div>
				</a>
					<p class="content">
						<a href="https://blog.csdn.net/q383965374/article/details/41948467" target="_blank" title="java通过struts实现web中的文件上传">
							<span class="desc oneline">单文件上传
fileupload.jsp




  
    &quot;&gt;
    
    My</span>
						</a>
                        						<span class="blog_title_box oneline"><a target="_blank" href="https://blog.csdn.net/q383965374">来自：	<span class="blog_title"> 直到世界的尽头</span></a></span>
                        					</p>
			</div>
					</div>
	
    
	    
    		<div class="recommend-item-box recommend-box-ident type_blog clearfix" data-track-view='{"mod":"popu_614","con":",https://blog.csdn.net/hayixia606/article/details/79237220,BlogCommendHotData_12"}' data-track-click='{"mod":"popu_614","con":",https://blog.csdn.net/hayixia606/article/details/79237220,BlogCommendHotData_12"}'>
			<div class="content">
				<a href="https://blog.csdn.net/hayixia606/article/details/79237220" target="_blank" title="微信支付V3微信公众号支付PHP教程(thinkPHP5公众号支付)/JSSDK的使用">
				<h4 class="text-truncate oneline">
						微信支付V3微信公众号支付PHP教程(thinkPHP5公众号支付)/JSSDK的使用				</h4>
				<div class="info-box d-flex align-content-center">
					<!-- <p class="avatar">
							<img src="" alt="hayixia606" class="avatar-pic">
							<span class="namebox">
								<span class="name">hayixia606</span>
								<span class="triangle"></span>
							</span>
					</p> -->
					<p class="date-and-readNum">
						<span class="date hover-show">02-02</span>
						<span class="read-num hover-hide">
							<svg class="icon csdnc-yuedushu" aria-hidden="true">
								<use xlink:href="#csdnc-m-passwords-visible"></use>
							</svg>
							1547</span>
						</p>
					</div>
				</a>
					<p class="content">
						<a href="https://blog.csdn.net/hayixia606/article/details/79237220" target="_blank" title="微信支付V3微信公众号支付PHP教程(thinkPHP5公众号支付)/JSSDK的使用">
							<span class="desc oneline">扫二维码关注，获取更多技术分享


  本文承接之前发布的博客《 微信支付V3微信公众号支付PHP教程/thinkPHP5公众号支付》必须阅读上篇文章后才可以阅读这篇文章。由于最近一段时间工作比较忙，...</span>
						</a>
                        						<span class="blog_title_box oneline"><a target="_blank" href="https://blog.csdn.net/hayixia606">来自：	<span class="blog_title"> Marswill</span></a></span>
                        					</p>
			</div>
					</div>
	
    
	    
    		<div class="recommend-item-box recommend-box-ident type_blog clearfix" data-track-view='{"mod":"popu_614","con":",https://blog.csdn.net/wyx100/article/details/73080969,BlogCommendHotData_13"}' data-track-click='{"mod":"popu_614","con":",https://blog.csdn.net/wyx100/article/details/73080969,BlogCommendHotData_13"}'>
			<div class="content">
				<a href="https://blog.csdn.net/wyx100/article/details/73080969" target="_blank" title="人脸检测和识别 源代码 下载-opencv3+python3.6完整实战项目源代码 识别视频《欢乐颂》中人物">
				<h4 class="text-truncate oneline">
						人脸检测和识别 源代码 下载-opencv3+python3.6完整实战项目源代码 识别视频《欢乐颂》中人物				</h4>
				<div class="info-box d-flex align-content-center">
					<!-- <p class="avatar">
							<img src="" alt="wyx100" class="avatar-pic">
							<span class="namebox">
								<span class="name">wyx100</span>
								<span class="triangle"></span>
							</span>
					</p> -->
					<p class="date-and-readNum">
						<span class="date hover-show">06-12</span>
						<span class="read-num hover-hide">
							<svg class="icon csdnc-yuedushu" aria-hidden="true">
								<use xlink:href="#csdnc-m-passwords-visible"></use>
							</svg>
							5841</span>
						</p>
					</div>
				</a>
					<p class="content">
						<a href="https://blog.csdn.net/wyx100/article/details/73080969" target="_blank" title="人脸检测和识别 源代码 下载-opencv3+python3.6完整实战项目源代码 识别视频《欢乐颂》中人物">
							<span class="desc oneline">人脸检测和识别- opencv3+python3完整实战项目源代码 识别视频《欢乐颂》中人物
python
opecv3人脸检测和识别
项目源代码
识别视频《欢乐颂》中人物...</span>
						</a>
                        						<span class="blog_title_box oneline"><a target="_blank" href="https://blog.csdn.net/wyx100">来自：	<span class="blog_title"> wyx100的专栏</span></a></span>
                        					</p>
			</div>
					</div>
	
    
	    
    		<div class="recommend-item-box recommend-box-ident type_blog clearfix" data-track-view='{"mod":"popu_614","con":",https://blog.csdn.net/roguesir/article/details/77104246,BlogCommendHotData_14"}' data-track-click='{"mod":"popu_614","con":",https://blog.csdn.net/roguesir/article/details/77104246,BlogCommendHotData_14"}'>
			<div class="content">
				<a href="https://blog.csdn.net/roguesir/article/details/77104246" target="_blank" title="人脸检测工具face_recognition的安装与应用">
				<h4 class="text-truncate oneline">
						人脸检测工具face_recognition的安装与应用				</h4>
				<div class="info-box d-flex align-content-center">
					<!-- <p class="avatar">
							<img src="" alt="roguesir" class="avatar-pic">
							<span class="namebox">
								<span class="name">roguesir</span>
								<span class="triangle"></span>
							</span>
					</p> -->
					<p class="date-and-readNum">
						<span class="date hover-show">08-11</span>
						<span class="read-num hover-hide">
							<svg class="icon csdnc-yuedushu" aria-hidden="true">
								<use xlink:href="#csdnc-m-passwords-visible"></use>
							</svg>
							7682</span>
						</p>
					</div>
				</a>
					<p class="content">
						<a href="https://blog.csdn.net/roguesir/article/details/77104246" target="_blank" title="人脸检测工具face_recognition的安装与应用">
							<span class="desc oneline">人脸检测工具face_recognition的安装与应用</span>
						</a>
                        						<span class="blog_title_box oneline"><a target="_blank" href="https://blog.csdn.net/roguesir">来自：	<span class="blog_title"> roguesir的博客</span></a></span>
                        					</p>
			</div>
					</div>
	
    
	    
    		<div class="recommend-item-box recommend-box-ident type_blog clearfix" data-track-view='{"mod":"popu_614","con":",https://blog.csdn.net/gefangshuai/article/details/50328451,BlogCommendHotData_15"}' data-track-click='{"mod":"popu_614","con":",https://blog.csdn.net/gefangshuai/article/details/50328451,BlogCommendHotData_15"}'>
			<div class="content">
				<a href="https://blog.csdn.net/gefangshuai/article/details/50328451" target="_blank" title="关于SpringBoot bean无法注入的问题（与文件包位置有关）">
				<h4 class="text-truncate oneline">
						关于SpringBoot bean无法注入的问题（与文件包位置有关）				</h4>
				<div class="info-box d-flex align-content-center">
					<!-- <p class="avatar">
							<img src="" alt="gefangshuai" class="avatar-pic">
							<span class="namebox">
								<span class="name">gefangshuai</span>
								<span class="triangle"></span>
							</span>
					</p> -->
					<p class="date-and-readNum">
						<span class="date hover-show">12-16</span>
						<span class="read-num hover-hide">
							<svg class="icon csdnc-yuedushu" aria-hidden="true">
								<use xlink:href="#csdnc-m-passwords-visible"></use>
							</svg>
							27668</span>
						</p>
					</div>
				</a>
					<p class="content">
						<a href="https://blog.csdn.net/gefangshuai/article/details/50328451" target="_blank" title="关于SpringBoot bean无法注入的问题（与文件包位置有关）">
							<span class="desc oneline">问题场景描述整个项目通过Maven构建，大致结构如下：
核心Spring框架一个module spring-boot-base
service和dao一个module server-core
提供系统...</span>
						</a>
                        						<span class="blog_title_box oneline"><a target="_blank" href="https://blog.csdn.net/gefangshuai">来自：	<span class="blog_title"> 开发随笔</span></a></span>
                        					</p>
			</div>
					</div>
	
    
	    
    		<div class="recommend-item-box recommend-box-ident type_blog clearfix" data-track-view='{"mod":"popu_614","con":",https://blog.csdn.net/liqfyiyi/article/details/50894004,BlogCommendHotData_16"}' data-track-click='{"mod":"popu_614","con":",https://blog.csdn.net/liqfyiyi/article/details/50894004,BlogCommendHotData_16"}'>
			<div class="content">
				<a href="https://blog.csdn.net/liqfyiyi/article/details/50894004" target="_blank" title="美团在Redis上踩过的一些坑-3.redis内存占用飙升">
				<h4 class="text-truncate oneline">
						美团在Redis上踩过的一些坑-3.redis内存占用飙升				</h4>
				<div class="info-box d-flex align-content-center">
					<!-- <p class="avatar">
							<img src="" alt="liqfyiyi" class="avatar-pic">
							<span class="namebox">
								<span class="name">liqfyiyi</span>
								<span class="triangle"></span>
							</span>
					</p> -->
					<p class="date-and-readNum">
						<span class="date hover-show">03-15</span>
						<span class="read-num hover-hide">
							<svg class="icon csdnc-yuedushu" aria-hidden="true">
								<use xlink:href="#csdnc-m-passwords-visible"></use>
							</svg>
							27420</span>
						</p>
					</div>
				</a>
					<p class="content">
						<a href="https://blog.csdn.net/liqfyiyi/article/details/50894004" target="_blank" title="美团在Redis上踩过的一些坑-3.redis内存占用飙升">
							<span class="desc oneline">转载请注明出处哈:http://carlosfu.iteye.com/blog/2254154


    



 一、现象：
    redis-cluster某个分片内存飙升，明...</span>
						</a>
                        						<span class="blog_title_box oneline"><a target="_blank" href="https://blog.csdn.net/liqfyiyi">来自：	<span class="blog_title"> 欧辰的专栏</span></a></span>
                        					</p>
			</div>
					</div>
	
    
	    
    		<div class="recommend-item-box recommend-box-ident type_blog clearfix" data-track-view='{"mod":"popu_614","con":",https://blog.csdn.net/u012743772/article/details/50517769,BlogCommendHotData_17"}' data-track-click='{"mod":"popu_614","con":",https://blog.csdn.net/u012743772/article/details/50517769,BlogCommendHotData_17"}'>
			<div class="content">
				<a href="https://blog.csdn.net/u012743772/article/details/50517769" target="_blank" title="DataTables 的 实例 《一》">
				<h4 class="text-truncate oneline">
						DataTables 的 实例 《一》				</h4>
				<div class="info-box d-flex align-content-center">
					<!-- <p class="avatar">
							<img src="" alt="u012743772" class="avatar-pic">
							<span class="namebox">
								<span class="name">u012743772</span>
								<span class="triangle"></span>
							</span>
					</p> -->
					<p class="date-and-readNum">
						<span class="date hover-show">01-14</span>
						<span class="read-num hover-hide">
							<svg class="icon csdnc-yuedushu" aria-hidden="true">
								<use xlink:href="#csdnc-m-passwords-visible"></use>
							</svg>
							2843</span>
						</p>
					</div>
				</a>
					<p class="content">
						<a href="https://blog.csdn.net/u012743772/article/details/50517769" target="_blank" title="DataTables 的 实例 《一》">
							<span class="desc oneline">1.加载需要的js/css文件




2.


function del(id){
   alert(id);
}

var table;
$(document).ready(function(...</span>
						</a>
                        						<span class="blog_title_box oneline"><a target="_blank" href="https://blog.csdn.net/u012743772">来自：	<span class="blog_title"> 辛修灿的博客</span></a></span>
                        					</p>
			</div>
					</div>
	
    
	    
    		<div class="recommend-item-box recommend-box-ident type_blog clearfix" data-track-view='{"mod":"popu_614","con":",https://blog.csdn.net/lzpdz/article/details/51863119,BlogCommendHotData_18"}' data-track-click='{"mod":"popu_614","con":",https://blog.csdn.net/lzpdz/article/details/51863119,BlogCommendHotData_18"}'>
			<div class="content">
				<a href="https://blog.csdn.net/lzpdz/article/details/51863119" target="_blank" title="关于Android电池管理系统（一）Linux驱动部分">
				<h4 class="text-truncate oneline">
						关于Android电池管理系统（一）Linux驱动部分				</h4>
				<div class="info-box d-flex align-content-center">
					<!-- <p class="avatar">
							<img src="" alt="lzpdz" class="avatar-pic">
							<span class="namebox">
								<span class="name">lzpdz</span>
								<span class="triangle"></span>
							</span>
					</p> -->
					<p class="date-and-readNum">
						<span class="date hover-show">07-08</span>
						<span class="read-num hover-hide">
							<svg class="icon csdnc-yuedushu" aria-hidden="true">
								<use xlink:href="#csdnc-m-passwords-visible"></use>
							</svg>
							2499</span>
						</p>
					</div>
				</a>
					<p class="content">
						<a href="https://blog.csdn.net/lzpdz/article/details/51863119" target="_blank" title="关于Android电池管理系统（一）Linux驱动部分">
							<span class="desc oneline">一、概述
android系统电池部分的驱动程序，继承了传统linux系统下的Power Supply驱动程序架构，Battery驱动程序通过Power Supply驱动程序生成相应的sys文件系统，从...</span>
						</a>
                        						<span class="blog_title_box oneline"><a target="_blank" href="https://blog.csdn.net/lzpdz">来自：	<span class="blog_title"> lzpdz的博客</span></a></span>
                        					</p>
			</div>
					</div>
	
    
	    
    		<div class="recommend-item-box recommend-box-ident type_blog clearfix" data-track-view='{"mod":"popu_614","con":",https://blog.csdn.net/ycl111/article/details/78227,BlogCommendHotData_19"}' data-track-click='{"mod":"popu_614","con":",https://blog.csdn.net/ycl111/article/details/78227,BlogCommendHotData_19"}'>
			<div class="content">
				<a href="https://blog.csdn.net/ycl111/article/details/78227" target="_blank" title="读核日记(三)">
				<h4 class="text-truncate oneline">
						读核日记(三)				</h4>
				<div class="info-box d-flex align-content-center">
					<!-- <p class="avatar">
							<img src="" alt="ycl111" class="avatar-pic">
							<span class="namebox">
								<span class="name">ycl111</span>
								<span class="triangle"></span>
							</span>
					</p> -->
					<p class="date-and-readNum">
						<span class="date hover-show">08-18</span>
						<span class="read-num hover-hide">
							<svg class="icon csdnc-yuedushu" aria-hidden="true">
								<use xlink:href="#csdnc-m-passwords-visible"></use>
							</svg>
							976</span>
						</p>
					</div>
				</a>
					<p class="content">
						<a href="https://blog.csdn.net/ycl111/article/details/78227" target="_blank" title="读核日记(三)">
							<span class="desc oneline">本文出自:http://os.silversand.net 作者: sunmoon (2001-08-31 15:00:01)在linux 中每一个进程都由task_struct 数据结构来定义. t...</span>
						</a>
                        						<span class="blog_title_box oneline"><a target="_blank" href="https://blog.csdn.net/ycl111">来自：	<span class="blog_title"> 江湖·郎中·路</span></a></span>
                        					</p>
			</div>
					</div>
	
    
	    
    		<div class="recommend-item-box recommend-box-ident type_blog clearfix" data-track-view='{"mod":"popu_614","con":",https://blog.csdn.net/oscar999/article/details/36373183,BlogCommendHotData_20"}' data-track-click='{"mod":"popu_614","con":",https://blog.csdn.net/oscar999/article/details/36373183,BlogCommendHotData_20"}'>
			<div class="content">
				<a href="https://blog.csdn.net/oscar999/article/details/36373183" target="_blank" title="[JS进阶] JS 之Blob 对象类型">
				<h4 class="text-truncate oneline">
						[JS进阶] JS 之Blob 对象类型				</h4>
				<div class="info-box d-flex align-content-center">
					<!-- <p class="avatar">
							<img src="" alt="oscar999" class="avatar-pic">
							<span class="namebox">
								<span class="name">oscar999</span>
								<span class="triangle"></span>
							</span>
					</p> -->
					<p class="date-and-readNum">
						<span class="date hover-show">11-30</span>
						<span class="read-num hover-hide">
							<svg class="icon csdnc-yuedushu" aria-hidden="true">
								<use xlink:href="#csdnc-m-passwords-visible"></use>
							</svg>
							109441</span>
						</p>
					</div>
				</a>
					<p class="content">
						<a href="https://blog.csdn.net/oscar999/article/details/36373183" target="_blank" title="[JS进阶] JS 之Blob 对象类型">
							<span class="desc oneline">Blob 是什么？ 这里说的是一种Javascript的对象类型。

oracle 中也有类似的栏位类型。

在

[JS进阶] HTML5 之文件操作(file)
这一篇中用到了File对象，而实际...</span>
						</a>
                        						<span class="blog_title_box oneline"><a target="_blank" href="https://blog.csdn.net/oscar999">来自：	<span class="blog_title"> oscar999的专栏</span></a></span>
                        					</p>
			</div>
					</div>
	
    
	    
    		<div class="recommend-item-box recommend-box-ident type_blog clearfix" data-track-view='{"mod":"popu_614","con":",https://blog.csdn.net/ROVAST/article/details/24349189,BlogCommendHotData_21"}' data-track-click='{"mod":"popu_614","con":",https://blog.csdn.net/ROVAST/article/details/24349189,BlogCommendHotData_21"}'>
			<div class="content">
				<a href="https://blog.csdn.net/ROVAST/article/details/24349189" target="_blank" title="VB使用RES资源文件技巧">
				<h4 class="text-truncate oneline">
						VB使用RES资源文件技巧				</h4>
				<div class="info-box d-flex align-content-center">
					<!-- <p class="avatar">
							<img src="" alt="ROVAST" class="avatar-pic">
							<span class="namebox">
								<span class="name">ROVAST</span>
								<span class="triangle"></span>
							</span>
					</p> -->
					<p class="date-and-readNum">
						<span class="date hover-show">04-23</span>
						<span class="read-num hover-hide">
							<svg class="icon csdnc-yuedushu" aria-hidden="true">
								<use xlink:href="#csdnc-m-passwords-visible"></use>
							</svg>
							3410</span>
						</p>
					</div>
				</a>
					<p class="content">
						<a href="https://blog.csdn.net/ROVAST/article/details/24349189" target="_blank" title="VB使用RES资源文件技巧">
							<span class="desc oneline">本文介绍了 Visual Basic 中资源文件的多种使用技巧：①开发中英（简、繁）双版本的技巧；②实现“绿色”软件；③直接播放声音文件；④保存各类图标、光标图片等等。


----------...</span>
						</a>
                        						<span class="blog_title_box oneline"><a target="_blank" href="https://blog.csdn.net/ROVAST">来自：	<span class="blog_title"> ROVAST的专栏</span></a></span>
                        					</p>
			</div>
					</div>
	
    
	    
    		<div class="recommend-item-box recommend-box-ident type_blog clearfix" data-track-view='{"mod":"popu_614","con":",https://blog.csdn.net/Tiaaaaa/article/details/58116346,BlogCommendHotData_22"}' data-track-click='{"mod":"popu_614","con":",https://blog.csdn.net/Tiaaaaa/article/details/58116346,BlogCommendHotData_22"}'>
			<div class="content">
				<a href="https://blog.csdn.net/Tiaaaaa/article/details/58116346" target="_blank" title="R语言逻辑回归、ROC曲线和十折交叉验证">
				<h4 class="text-truncate oneline">
						R语言逻辑回归、ROC曲线和十折交叉验证				</h4>
				<div class="info-box d-flex align-content-center">
					<!-- <p class="avatar">
							<img src="" alt="Tiaaaaa" class="avatar-pic">
							<span class="namebox">
								<span class="name">Tiaaaaa</span>
								<span class="triangle"></span>
							</span>
					</p> -->
					<p class="date-and-readNum">
						<span class="date hover-show">02-27</span>
						<span class="read-num hover-hide">
							<svg class="icon csdnc-yuedushu" aria-hidden="true">
								<use xlink:href="#csdnc-m-passwords-visible"></use>
							</svg>
							12715</span>
						</p>
					</div>
				</a>
					<p class="content">
						<a href="https://blog.csdn.net/Tiaaaaa/article/details/58116346" target="_blank" title="R语言逻辑回归、ROC曲线和十折交叉验证">
							<span class="desc oneline">自己整理编写的逻辑回归模板，作为学习笔记记录分享。数据集用的是14个自变量Xi，一个因变量Y的australian数据集。


1. 测试集和训练集3、7分组
australian ...</span>
						</a>
                        						<span class="blog_title_box oneline"><a target="_blank" href="https://blog.csdn.net/Tiaaaaa">来自：	<span class="blog_title"> Tiaaaaa的博客</span></a></span>
                        					</p>
			</div>
					</div>
	
    
	    
    		<div class="recommend-item-box recommend-box-ident type_blog clearfix" data-track-view='{"mod":"popu_614","con":",https://blog.csdn.net/qq574857122/article/details/16361033,BlogCommendHotData_23"}' data-track-click='{"mod":"popu_614","con":",https://blog.csdn.net/qq574857122/article/details/16361033,BlogCommendHotData_23"}'>
			<div class="content">
				<a href="https://blog.csdn.net/qq574857122/article/details/16361033" target="_blank" title="强连通分量及缩点tarjan算法解析">
				<h4 class="text-truncate oneline">
						强连通分量及缩点tarjan算法解析				</h4>
				<div class="info-box d-flex align-content-center">
					<!-- <p class="avatar">
							<img src="" alt="qq574857122" class="avatar-pic">
							<span class="namebox">
								<span class="name">qq574857122</span>
								<span class="triangle"></span>
							</span>
					</p> -->
					<p class="date-and-readNum">
						<span class="date hover-show">11-16</span>
						<span class="read-num hover-hide">
							<svg class="icon csdnc-yuedushu" aria-hidden="true">
								<use xlink:href="#csdnc-m-passwords-visible"></use>
							</svg>
							14216</span>
						</p>
					</div>
				</a>
					<p class="content">
						<a href="https://blog.csdn.net/qq574857122/article/details/16361033" target="_blank" title="强连通分量及缩点tarjan算法解析">
							<span class="desc oneline">强连通分量：
简言之 就是找环（每条边只走一次，两两可达）
孤立的一个点也是一个连通分量 
 
使用tarjan算法 在嵌套的多个环中优先得到最大环( 最小环就是每个孤立点）
 
定义：
int Ti...</span>
						</a>
                        						<span class="blog_title_box oneline"><a target="_blank" href="https://blog.csdn.net/qq574857122">来自：	<span class="blog_title"> 九野的博客</span></a></span>
                        					</p>
			</div>
					</div>
	
    
	    
    		<div class="recommend-item-box recommend-box-ident type_blog clearfix" data-track-view='{"mod":"popu_614","con":",https://blog.csdn.net/a635661820/article/details/45390671,BlogCommendHotData_24"}' data-track-click='{"mod":"popu_614","con":",https://blog.csdn.net/a635661820/article/details/45390671,BlogCommendHotData_24"}'>
			<div class="content">
				<a href="https://blog.csdn.net/a635661820/article/details/45390671" target="_blank" title="LSTM简介以及数学推导(FULL BPTT)">
				<h4 class="text-truncate oneline">
						LSTM简介以及数学推导(FULL BPTT)				</h4>
				<div class="info-box d-flex align-content-center">
					<!-- <p class="avatar">
							<img src="" alt="a635661820" class="avatar-pic">
							<span class="namebox">
								<span class="name">a635661820</span>
								<span class="triangle"></span>
							</span>
					</p> -->
					<p class="date-and-readNum">
						<span class="date hover-show">04-30</span>
						<span class="read-num hover-hide">
							<svg class="icon csdnc-yuedushu" aria-hidden="true">
								<use xlink:href="#csdnc-m-passwords-visible"></use>
							</svg>
							70209</span>
						</p>
					</div>
				</a>
					<p class="content">
						<a href="https://blog.csdn.net/a635661820/article/details/45390671" target="_blank" title="LSTM简介以及数学推导(FULL BPTT)">
							<span class="desc oneline">前段时间看了一些关于LSTM方面的论文，一直准备记录一下学习过程的，因为其他事儿，一直拖到了现在，记忆又快模糊了。现在赶紧补上，本文的组织安排是这样的：先介绍rnn的BPTT所存在的问题，然后介绍最初...</span>
						</a>
                        						<span class="blog_title_box oneline"><a target="_blank" href="https://blog.csdn.net/a635661820">来自：	<span class="blog_title"> 天道酬勤，做一个务实的理想主义者</span></a></span>
                        					</p>
			</div>
					</div>
	
    
	    
    		<div class="recommend-item-box recommend-box-ident type_blog clearfix" data-track-view='{"mod":"popu_614","con":",https://blog.csdn.net/a1b2c3d4123456/article/details/53915056,BlogCommendHotData_25"}' data-track-click='{"mod":"popu_614","con":",https://blog.csdn.net/a1b2c3d4123456/article/details/53915056,BlogCommendHotData_25"}'>
			<div class="content">
				<a href="https://blog.csdn.net/a1b2c3d4123456/article/details/53915056" target="_blank" title="idea配置maven并添加镜像配置">
				<h4 class="text-truncate oneline">
						idea配置maven并添加镜像配置				</h4>
				<div class="info-box d-flex align-content-center">
					<!-- <p class="avatar">
							<img src="" alt="a1b2c3d4123456" class="avatar-pic">
							<span class="namebox">
								<span class="name">a1b2c3d4123456</span>
								<span class="triangle"></span>
							</span>
					</p> -->
					<p class="date-and-readNum">
						<span class="date hover-show">12-28</span>
						<span class="read-num hover-hide">
							<svg class="icon csdnc-yuedushu" aria-hidden="true">
								<use xlink:href="#csdnc-m-passwords-visible"></use>
							</svg>
							9363</span>
						</p>
					</div>
				</a>
					<p class="content">
						<a href="https://blog.csdn.net/a1b2c3d4123456/article/details/53915056" target="_blank" title="idea配置maven并添加镜像配置">
							<span class="desc oneline">前提是安装好maven。1、打开maven存放文件夹找到 conf -&gt;settings.xml 
 
找到节点 
把下面内容写入节点内 配置为阿里云的镜像
      alimaven
      ...</span>
						</a>
                        						<span class="blog_title_box oneline"><a target="_blank" href="https://blog.csdn.net/a1b2c3d4123456">来自：	<span class="blog_title"> 哆啦A梦的博客</span></a></span>
                        					</p>
			</div>
					</div>
	
    
	    
    		<div class="recommend-item-box recommend-box-ident type_blog clearfix" data-track-view='{"mod":"popu_614","con":",https://blog.csdn.net/ymj7150697/article/details/7384126,BlogCommendHotData_26"}' data-track-click='{"mod":"popu_614","con":",https://blog.csdn.net/ymj7150697/article/details/7384126,BlogCommendHotData_26"}'>
			<div class="content">
				<a href="https://blog.csdn.net/ymj7150697/article/details/7384126" target="_blank" title="expat介绍文档翻译">
				<h4 class="text-truncate oneline">
						expat介绍文档翻译				</h4>
				<div class="info-box d-flex align-content-center">
					<!-- <p class="avatar">
							<img src="" alt="ymj7150697" class="avatar-pic">
							<span class="namebox">
								<span class="name">ymj7150697</span>
								<span class="triangle"></span>
							</span>
					</p> -->
					<p class="date-and-readNum">
						<span class="date hover-show">03-22</span>
						<span class="read-num hover-hide">
							<svg class="icon csdnc-yuedushu" aria-hidden="true">
								<use xlink:href="#csdnc-m-passwords-visible"></use>
							</svg>
							1836</span>
						</p>
					</div>
				</a>
					<p class="content">
						<a href="https://blog.csdn.net/ymj7150697/article/details/7384126" target="_blank" title="expat介绍文档翻译">
							<span class="desc oneline">原文地址：http://www.xml.com/pub/a/1999/09/expat/index.html


因为需要用，所以才翻译了这个文档。但总归赖于英语水平很有限，翻译出来的中文有可能...</span>
						</a>
                        						<span class="blog_title_box oneline"><a target="_blank" href="https://blog.csdn.net/ymj7150697">来自：	<span class="blog_title"> ymj7150697的专栏</span></a></span>
                        					</p>
			</div>
					</div>
	
    
	    
    

            <div class="recommend-loading-box">
                <img src='https://csdnimg.cn/release/phoenix/images/feedLoading.gif'>
            </div>
            <div class="recommend-end-box">
                <p class="text-center">没有更多推荐了，<a href="https://blog.csdn.net/" class="c-blue c-blue-hover c-blue-focus">返回首页</a></p>
            </div>
        </div>
    </main>

    <aside>
		    <div id="asideProfile" class="aside-box">
    <!-- <h3 class="aside-title">个人资料</h3> -->
    <div class="profile-intro d-flex">
        <div class="avatar-box d-flex justify-content-center flex-column">
            <a href="https://blog.csdn.net/zwq912318834">
                <img src="https://avatar.csdn.net/7/4/8/3_zwq912318834.jpg" class="avatar_pic">
            </a>
                    </div>
        <div class="user-info d-flex justify-content-center flex-column">
            <p class="name csdn-tracking-statistics tracking-click" data-mod="popu_379">
                <a href="https://blog.csdn.net/zwq912318834" target="_blank" class="" id="uid">Kosmoo</a>
            </p>
                    </div>
                <div class="opt-box d-flex justify-content-center flex-column">
            <span  class="csdn-tracking-statistics tracking-click" data-mod="popu_379">
                <a class="btn btn-sm btn-red-hollow attention" id="btnAttent">关注</a>
            </span>
        </div>
            </div>
    <div class="data-info d-flex item-tiling">
                <dl class="text-center" title="75">
                        <dt><a href="https://blog.csdn.net/zwq912318834?t=1">原创</a></dt>
            <dd><a href="https://blog.csdn.net/zwq912318834?t=1"><span class="count">75</span></a></dd>
                    </dl>
        <dl class="text-center" id="fanBox" title="141">
            <dt>粉丝</dt>
            <dd><span class="count" id="fan">141</span></dd>
        </dl>
        <dl class="text-center" title="70">
            <dt>喜欢</dt>
            <dd><span class="count">70</span></dd>
        </dl>
        <dl class="text-center" title="95">
            <dt>评论</dt>
            <dd><span class="count">95</span></dd>
        </dl>
    </div>
    <div class="grade-box clearfix">
        <dl>
            <dt>等级：</dt>
            <dd>
                <a href="https://blog.csdn.net/home/help.html#level" title="5级,点击查看等级说明" target="_blank">
                    <svg class="icon icon-level" aria-hidden="true">
                        <use xlink:href="#csdnc-bloglevel-5"></use>
                    </svg>
                </a>
            </dd>
        </dl>
        <dl>
            <dt>访问：</dt>
            <dd title="399176">
                39万+            </dd>
        </dl>
        <dl>
            <dt>积分：</dt>
            <dd title="4493">
                4493            </dd>
        </dl>
        <dl title="10245">
            <dt>排名：</dt>
            <dd>1万+</dd>
        </dl>
    </div>
        <div class="badge-box d-flex">
        <span>勋章：</span>
                        <div class="icon-badge" title="持之以恒">
            <div class="mouse-box">
                <svg class="icon" aria-hidden="true">
                    <use xlink:href="#csdnc-m-lasting"></use>
                </svg>
                <div class="icon-arrow"></div>
            </div>
            <div class="grade-detail-box">
                <div class="pos-box">
                    <div class="left-box d-flex justify-content-center align-items-center flex-column">
                        <svg class="icon" aria-hidden="true">
                            <use xlink:href="#csdnc-m-lasting"></use>
                        </svg>
                        <p>持之以恒</p>
                    </div>
                    <div class="right-box d-flex justify-content-center align-items-center">
                        授予每个自然月内发布4篇或4篇以上原创或翻译IT博文的用户。不积跬步无以至千里，不积小流无以成江海，程序人生的精彩需要坚持不懈地积累！
                    </div>
                </div>
            </div>
        </div>
                                                <script>
            (function ($) {
                setTimeout(function(){
                    $('div.icon-badge.show-moment').removeClass('show-moment');
                }, 5000);
            })(window.jQuery)
        </script>
    </div>
    </div>
		    <div class="csdn-tracking-statistics mb8 box-shadow" data-pid="blog" data-mod="popu_4" style="height:250px;">
    <div class="aside-content text-center" id="cpro_u2734133">
      <div id="kp_box_56" data-pid="56" data-track-view='{"mod":"kp_popu_56-76","con":",,"}' data-track-click='{"mod":"kp_popu_56-76","con":",,"}'><script type="text/javascript">
    (function() {
        var s = "_" + Math.random().toString(36).slice(2);
        document.write('<div style="" id="' + s + '"></div>');
        (window.slotbydup = window.slotbydup || []).push({
            id: "u3032528",
            container:  s
        });
    })();
</script>
<!-- 多条广告如下脚本只需引入一次 -->
<script type="text/javascript" src="//cpro.baidustatic.com/cpro/ui/c.js" async="async" defer="defer" ></script></div>    </div>
</div>
		    <div id="asideNewArticle" class="aside-box">
    <h3 class="aside-title">最新文章</h3>
    <div class="aside-content">
        <ul class="inf_list clearfix csdn-tracking-statistics tracking-click" data-mod="popu_382">
                        <li class="clearfix">
                <a href="https://blog.csdn.net/zwq912318834/article/details/81263618" target="_blank">selenium使用chrome进行登录时如何关闭弹出的密码提示框</a>
            </li>
                        <li class="clearfix">
                <a href="https://blog.csdn.net/zwq912318834/article/details/81189422" target="_blank">selenium操作chrome滑动滚动条的几种方法分析</a>
            </li>
                        <li class="clearfix">
                <a href="https://blog.csdn.net/zwq912318834/article/details/80975748" target="_blank">python下selenium如何处理各种日期控件</a>
            </li>
                        <li class="clearfix">
                <a href="https://blog.csdn.net/zwq912318834/article/details/80696639" target="_blank">阿里云ECS服务器环境搭建（6） —— Windows 与 Ubuntu16.04 之间利用 WinSCP 进行文件传输</a>
            </li>
                        <li class="clearfix">
                <a href="https://blog.csdn.net/zwq912318834/article/details/80570998" target="_blank">阿里云ECS服务器环境搭建（5） —— ubuntu 16.04 下为mongodb各个数据库设置用户名和密码</a>
            </li>
                    </ul>
    </div>
</div>
		    		    <div id="asideCategory" class="aside-box flexible-box">
    <h3 class="aside-title">个人分类</h3>
    <div class="aside-content">
        <ul>
                        <li>
                <a class="clearfix" href="https://blog.csdn.net/zwq912318834/article/category/6724759">
                    <span class="title oneline">python基础</span>
                    <span class="count float-right">12篇</span>
                </a>
            </li>
                        <li>
                <a class="clearfix" href="https://blog.csdn.net/zwq912318834/article/category/7106479">
                    <span class="title oneline">python爬虫</span>
                    <span class="count float-right">52篇</span>
                </a>
            </li>
                        <li>
                <a class="clearfix" href="https://blog.csdn.net/zwq912318834/article/category/7136049">
                    <span class="title oneline">数据库</span>
                    <span class="count float-right">9篇</span>
                </a>
            </li>
                        <li>
                <a class="clearfix" href="https://blog.csdn.net/zwq912318834/article/category/7162309">
                    <span class="title oneline">环境搭建</span>
                    <span class="count float-right">4篇</span>
                </a>
            </li>
                        <li>
                <a class="clearfix" href="https://blog.csdn.net/zwq912318834/article/category/7276681">
                    <span class="title oneline">python-数据挖掘</span>
                    <span class="count float-right">2篇</span>
                </a>
            </li>
                        <li>
                <a class="clearfix" href="https://blog.csdn.net/zwq912318834/article/category/7292375">
                    <span class="title oneline">selenium</span>
                    <span class="count float-right">12篇</span>
                </a>
            </li>
                        <li>
                <a class="clearfix" href="https://blog.csdn.net/zwq912318834/article/category/7334101">
                    <span class="title oneline">数据分析</span>
                    <span class="count float-right">1篇</span>
                </a>
            </li>
                        <li>
                <a class="clearfix" href="https://blog.csdn.net/zwq912318834/article/category/7334102">
                    <span class="title oneline">数据获取</span>
                    <span class="count float-right">2篇</span>
                </a>
            </li>
                        <li>
                <a class="clearfix" href="https://blog.csdn.net/zwq912318834/article/category/7704488">
                    <span class="title oneline">阿里云服务器环境搭建</span>
                    <span class="count float-right">6篇</span>
                </a>
            </li>
                    </ul>
    </div>
        <p class="text-center">
        <a class="btn btn-link-blue flexible-btn" data-fbox="aside-archive">展开</a>
    </p>
    </div>
		    <div id="asideArchive" class="aside-box flexible-box">
    <h3 class="aside-title">归档</h3>
    <div class="aside-content">
        <ul class="archive-list">
                        <!--归档统计-->
            <li>
                <a href="https://blog.csdn.net/zwq912318834/article/month/2018/07">
                    2018年7月                    <span class="count float-right">3篇</span>
                </a>
            </li>
                        <!--归档统计-->
            <li>
                <a href="https://blog.csdn.net/zwq912318834/article/month/2018/06">
                    2018年6月                    <span class="count float-right">5篇</span>
                </a>
            </li>
                        <!--归档统计-->
            <li>
                <a href="https://blog.csdn.net/zwq912318834/article/month/2018/05">
                    2018年5月                    <span class="count float-right">8篇</span>
                </a>
            </li>
                        <!--归档统计-->
            <li>
                <a href="https://blog.csdn.net/zwq912318834/article/month/2018/04">
                    2018年4月                    <span class="count float-right">5篇</span>
                </a>
            </li>
                        <!--归档统计-->
            <li>
                <a href="https://blog.csdn.net/zwq912318834/article/month/2018/03">
                    2018年3月                    <span class="count float-right">8篇</span>
                </a>
            </li>
                        <!--归档统计-->
            <li>
                <a href="https://blog.csdn.net/zwq912318834/article/month/2018/02">
                    2018年2月                    <span class="count float-right">4篇</span>
                </a>
            </li>
                        <!--归档统计-->
            <li>
                <a href="https://blog.csdn.net/zwq912318834/article/month/2018/01">
                    2018年1月                    <span class="count float-right">9篇</span>
                </a>
            </li>
                        <!--归档统计-->
            <li>
                <a href="https://blog.csdn.net/zwq912318834/article/month/2017/12">
                    2017年12月                    <span class="count float-right">8篇</span>
                </a>
            </li>
                        <!--归档统计-->
            <li>
                <a href="https://blog.csdn.net/zwq912318834/article/month/2017/11">
                    2017年11月                    <span class="count float-right">11篇</span>
                </a>
            </li>
                        <!--归档统计-->
            <li>
                <a href="https://blog.csdn.net/zwq912318834/article/month/2017/10">
                    2017年10月                    <span class="count float-right">5篇</span>
                </a>
            </li>
                        <!--归档统计-->
            <li>
                <a href="https://blog.csdn.net/zwq912318834/article/month/2017/09">
                    2017年9月                    <span class="count float-right">4篇</span>
                </a>
            </li>
                        <!--归档统计-->
            <li>
                <a href="https://blog.csdn.net/zwq912318834/article/month/2017/08">
                    2017年8月                    <span class="count float-right">3篇</span>
                </a>
            </li>
                        <!--归档统计-->
            <li>
                <a href="https://blog.csdn.net/zwq912318834/article/month/2017/02">
                    2017年2月                    <span class="count float-right">2篇</span>
                </a>
            </li>
                    </ul>
    </div>
        <p class="text-center">
        <a class="btn btn-link-blue flexible-btn" data-fbox="aside-archive">展开</a>
    </p>
    </div>
		    <div id="asideHotArticle" class="aside-box">
	<h3 class="aside-title">热门文章</h3>
	<div class="aside-content">
		<ul class="hotArticle-list csdn-tracking-statistics tracking-click" data-mod="popu_521">
							<li>
					<a href="https://blog.csdn.net/zwq912318834/article/details/78933910">selenium+python配置chrome浏览器的选项</a>
					<p class="read">阅读量：<span>24920</span></p>
				</li>
							<li>
					<a href="https://blog.csdn.net/zwq912318834/article/details/78626739">selenium+python设置爬虫代理IP</a>
					<p class="read">阅读量：<span>18907</span></p>
				</li>
							<li>
					<a href="https://blog.csdn.net/zwq912318834/article/details/77689568">python使用pymongo访问MongoDB的基本操作，以及CSV文件导出</a>
					<p class="read">阅读量：<span>16983</span></p>
				</li>
							<li>
					<a href="https://blog.csdn.net/zwq912318834/article/details/78292536">scrapy爬虫注意点（1）—— scrapy.FormRequest中formdata参数</a>
					<p class="read">阅读量：<span>13633</span></p>
				</li>
							<li>
					<a href="https://blog.csdn.net/zwq912318834/article/details/77806737">python实现scrapy爬虫每天定时抓取数据</a>
					<p class="read">阅读量：<span>10616</span></p>
				</li>
					</ul>
	</div>
</div>
		    <div id="asideNewComments" class="aside-box">
    <h3 class="aside-title">最新评论</h3>
    <div class="aside-content">
        <ul class="newcomment-list">
                        <li>
                <a class="title text-truncate" target="_blank" href="https://blog.csdn.net/zwq912318834/article/details/80528374#comments">阿里云ECS服务器环境搭建（1） ...</a>
                <p class="comment">
                    <a href="https://my.csdn.net/u014231798" class="user-name" target="_blank">u014231798</a>：我也看不到图形界面                </p>
            </li>
                        <li>
                <a class="title text-truncate" target="_blank" href="https://blog.csdn.net/zwq912318834/article/details/80528374#comments">阿里云ECS服务器环境搭建（1） ...</a>
                <p class="comment">
                    <a href="https://my.csdn.net/qq_40393000" class="user-name" target="_blank">qq_40393000</a>：我用xshell远程连接也没有图形界面，不过用阿里云的远程连接就可以显示图形界面了                </p>
            </li>
                        <li>
                <a class="title text-truncate" target="_blank" href="https://blog.csdn.net/zwq912318834/article/details/79571110#comments">python3下使用request...</a>
                <p class="comment">
                    <a href="https://my.csdn.net/Nothing______" class="user-name" target="_blank">Nothing______</a>：为什么不直接用requests.Session()来保持会话呢                </p>
            </li>
                        <li>
                <a class="title text-truncate" target="_blank" href="https://blog.csdn.net/zwq912318834/article/details/79197114#comments">selenium + python...</a>
                <p class="comment">
                    <a href="https://my.csdn.net/zhailunwen" class="user-name" target="_blank">zhailunwen</a>：有获取被selected的选项吗                </p>
            </li>
                        <li>
                <a class="title text-truncate" target="_blank" href="https://blog.csdn.net/zwq912318834/article/details/79571110#comments">python3下使用request...</a>
                <p class="comment">
                    <a href="https://my.csdn.net/weixin_43991560" class="user-name" target="_blank">weixin_43991560</a>：[reply]ofafucarl[/reply]
第一次执行没有创建cookie文件，所以报错，加...                </p>
            </li>
                    </ul>
    </div>
</div>
		<div id="asideFooter">
			
		<div class="aside-box">
			<div id="kp_box_57" data-pid="57" data-track-view='{"mod":"kp_popu_57-77","con":",,"}' data-track-click='{"mod":"kp_popu_57-77","con":",,"}'><script type="text/javascript">
    (function() {
        var s = "_" + Math.random().toString(36).slice(2);
        document.write('<div style="" id="' + s + '"></div>');
        (window.slotbydup = window.slotbydup || []).push({
            id: "u3163270",
            container:  s
        });
    })();
</script>
<!-- 多条广告如下脚本只需引入一次 -->
<script type="text/javascript" src="//cpro.baidustatic.com/cpro/ui/c.js" async="async" defer="defer" ></script></div>		</div>
				<div class="aside-box">
			<div class="persion_article">
			</div>
		</div>
	</div>
</aside>
<script src="https://csdnimg.cn/pubfooter/js/publib_footer-1.0.3.js" data-isfootertrack="false" type="text/javascript"></script>
<script>
	$("a.flexible-btn").click(function(){
		$(this).parents('div.aside-box').removeClass('flexible-box');
		$(this).remove();
	})
</script>
</div>
<div class="mask-dark"></div>
<div class="super-private private-box">
  <div class="private-title">
    <h5 class="title">
      私密
    </h5>
    <div class="private-close">
      <svg class="icon" aria-hidden="true">
        <use xlink:href="#csdnc-times"></use>
      </svg>
    </div>
  </div>
  <div class="private-content">
    <span class="select-name">私密原因:</span>
    <div class="select">
      <div class="input-mod">
        <span class="select-active" data-index="">请选择设置私密原因</span>
        <div class="select-button">
          <svg class="icon" aria-hidden="true">
            <use xlink:href="#csdnc-triangledown"></use>
          </svg>
        </div>
      </div>
      <ul class="select-option">
        <li data-index="1">广告</li>
        <li data-index="2">抄袭</li>
        <li data-index="3">版权</li>
        <li data-index="4">政治</li>
        <li data-index="5">色情</li>
        <li data-index="6">无意义</li>
        <li data-index="7" data-isInput='true'>其他</li>
      </ul>
    </div>
    <div class="other">
      <span class="other-name">其他原因:</span>
      <div class="textarea-box">
        <textarea class="private-input reason"name="name" rows="8" cols="80" placeholder="请填写其他设置私密原因，不超过120个汉字"></textarea>
        <div class="number">120</div>
      </div>
    </div>
  </div>
  <div class="private-footer">
    <div class="private-close">
      取消
    </div>
    <div class="private-send private-form no-active">
      确定
    </div>
  </div>
</div>
<!--  -->
<div class="private-error super-private">
  <div class="private-title">
    <h5 class="title">
      出错啦
    </h5>
    <div class="private-close">
      <svg class="icon" aria-hidden="true">
        <use xlink:href="#csdnc-times"></use>
      </svg>
    </div>
  </div>
  <div class="private-content">
    系统繁忙，请稍后再试
  </div>
  <div class="private-footer">
    <div class="private-close">
      取消
    </div>
    <div class="private-send close-active">
      确定
    </div>
  </div>
</div><div class="pulllog-box" style="display: block;">
	<div class="pulllog clearfix">
		<span class="text float-left">
            <div id="dmp_ad_69"><div id="kp_box_69" data-pid="69" data-track-view='{"mod":"kp_popu_69-796","con":",,"}' data-track-click='{"mod":"kp_popu_69-796","con":",,"}'><div style="float:left;margin-right:5px;border:1px solid #f13d3d;padding:2px 5px 0px 5px;">
<a href="https://edu.csdn.net/topic/ai30?utm_source=ditong" target="_blank" style="color:#f13d3d;font-weight:bold;text-decoration:none;font-size:15px;">2019人工智能薪资趋势</a>
</div>

<div style="float:left;margin-right:5px;border:1px solid #00BFFF;padding:2px 5px 0px 5px;background:#FFF0F5;">
<a href="https://edu.csdn.net/topic/python115?utm_source=ditong" target="_blank" style="color:#00BFFF;font-weight:bold;text-decoration:none;font-size:15px;">Python实战技巧</a>
</div>

<div style="float:left;margin-right:5px;border:1px solid #f13d3d;padding:2px 5px 0px 5px;">
<a href="https://t.csdnimg.cn/mWQl" target="_blank" style="color:#f13d3d;font-weight:bold;text-decoration:none;font-size:15px;">数据库沙龙</a>
</div>

<div style="float:left;margin-right:5px;border:1px solid #00BFFF;padding:2px 5px 0px 5px;background:#FFF0F5;">
<a href="https://gitbook.cn/gitchat/columns?tag=榜单&utm_source=wzl190104" target="_blank" style="color:#00BFFF;font-weight:bold;text-decoration:none;font-size:15px;">2018 年度课程榜单</a>
</div>


<div style="float:left;">
<script type="text/javascript" src="//rabc1.iteye.com/common/js/ndr3h.js?b=wosyvccl"></script>
<!-- 长文字链
<script type="text/javascript" src="//rabc1.iteye.com/common/5klj5.js?kfxbghx=bx"></script>
-->
</div></div></div>            		</span>
		<div class="pulllog-btn float-right clearfix">
            <div class="float-left csdn-tracking-statistics tracking-click" data-mod="popu_557">
                <a class="pulllog-login">登录</a>
            </div>
            <div class="pulllog-sigin float-left csdn-tracking-statistics tracking-click" data-mod="popu_558">
                <a href="https://passport.csdn.net/account/mobileregister" target="_blank">注册</a>
            </div>
            <button class="btn-close">
                <svg class="icon" aria-hidden="true">
                    <use xlink:href="#csdnc-times"></use>
                </svg>
            </button>
		</div>
	</div>
</div>
<div id="loginWrap" style="display:none"></div>
<div class="tool-box">
	<ul class="meau-list">
		<li class="btn-like-box long-width">
			<button class=" long-height hover-box btn-like " title="点赞">
				<svg class="icon active hover-hide" aria-hidden="true">
					<use xlink:href="#csdnc-thumbsup-ok"></use>
				</svg>
				<svg class="icon no-active hover-hide" aria-hidden="true">
					<use xlink:href="#csdnc-thumbsup"></use>
				</svg>
				<span class="hover-show text-box text">
					<span class="no-active">点赞</span>
					<span class="active">取消点赞</span>
				</span>
				<p>7</p>
			</button>
		</li>
		<li class="">
						<a class="btn-comments long-height hover-box" title="写评论" href="#commentBox">
				<svg class="icon hover-hide" aria-hidden="true">
					<use xlink:href="#csdnc-comments"></use>
				</svg>
				<span class="hover-show text">评论</span>
				<p class="">
						8				</p>
			</a>
		</li>
		<li class="toc-container-box" id="liTocBox">
			<button class="btn-toc low-height hover-box" title="目录">
				<svg class="icon hover-hide" aria-hidden="true">
					<use xlink:href="#csdnc-contents"></use>
				</svg>
				<span class="hover-show text">目录</span>
			</button>
			<div class="toc-container">
				<div class="pos-box">
					<div class="icon-arrow"></div>
					<div class="scroll-box">
						<div class="toc-box"></div>
					</div>
				</div>
				<div class="opt-box">
					<button class="btn-opt prev nomore" title="向上">
						<svg class="icon" aria-hidden="true">
							<use xlink:href="#csdnc-chevronup"></use>
						</svg>
					</button>
					<button class="btn-opt next">
						<svg class="icon" aria-hidden="true">
							<use xlink:href="#csdnc-chevrondown"></use>
						</svg>
					</button>
				</div>
			</div>
		</li>
		<li>
			<button class="btn-bookmark low-height hover-box" title="收藏">
				<svg class="icon active hover-hide" aria-hidden="true">
					<use xlink:href="#csdnc-bookmark-ok"></use>
				</svg>
				<svg class="icon no-active hover-hide" aria-hidden="true">
					<use xlink:href="#csdnc-bookmark"></use>
				</svg>
					<span class="hover-show text">收藏</span>
				<!-- <span class="hover-show text-box text">
					<span class="no-active">收藏</span>
					<span class="active">取消收藏</span>
				</span> -->
			</button>
		</li>
		<li class="bdsharebuttonbox">
			<button class="btn-comments low-height hover-box" >
				<a href="#" class="bds_weixin clear-share-style" data-cmd="weixin" title="手机看"></a>
				<svg class="icon hover-hide" aria-hidden="true">
					<use xlink:href="#csdnc-usephone"></use>
				</svg>
				<span class="hover-show text text3">
					手机看
				</span>
			</button>
		</li>
							<li class="widescreen-hide">
				<a class="btn-comments low-height hover-box" href="https://blog.csdn.net/zwq912318834/article/details/79530828" title="如何使用scrapy中的ItemLoader提取数据？">
					<svg class="icon hover-hide" aria-hidden="true">
						<use xlink:href="#csdnc-chevronleft"></use>
					</svg>
					<span class="hover-show text text3">上一篇</span>
				</a>
			</li>
								<li class="widescreen-hide">
			<a class="btn-comments hover-box low-height" href="https://blog.csdn.net/zwq912318834/article/details/79614372" title="python3下使用scrapy实现模拟用户登录与cookie存储 —— 基础篇（马蜂窝）">
				<svg class="icon hover-hide" aria-hidden="true">
					<use xlink:href="#csdnc-chevronright"></use>
				</svg>
				<span class="hover-show text text3">下一篇</span>
			</a>
		</li>
				<li class="bdsharebuttonbox _360_interactive"style="margin-top: 8px;"><div id="kp_box_73" data-pid="73" data-track-view='{"mod":"kp_popu_73-97","con":",,"}' data-track-click='{"mod":"kp_popu_73-97","con":",,"}'><script type="text/javascript" src="//cjhd.mediav.com/js/interactive_plugin.js"></script> 
			<style>
				#_360_interactive > *{
					 margin-left: -8px;
				}
			</style>
			<div id="_360_interactive" > 
				<script> INTERACTIVE_PLUGIN.render({ showid : 'N0ufqn', w: 60, h: 60, type: 'click', placeholderId: '_360_interactive' }); </script> 
			</div>
			<img src="//img-ads.csdn.net/2016/201608021757063065.png" style="margin: 0 auto;display: block;" alt=""></div></li>		<!-- 宽屏更多按钮 -->
		<li class="widescreen-more">
			<a class="btn-comments chat-ask-button low-height hover-box" title="快问" href="#chatqa">
				<svg class="icon hover-hide" aria-hidden="true">
					<use xlink:href="#csdnc-more"></use>
				</svg>
				<span class="hover-show text">更多</span>
				
			</a>
			<ul class="widescreen-more-box">
													<li class="widescreen-more">
						<a class="btn-comments low-height hover-box" href="https://blog.csdn.net/zwq912318834/article/details/79530828" title="如何使用scrapy中的ItemLoader提取数据？">
							<svg class="icon hover-hide" aria-hidden="true">
								<use xlink:href="#csdnc-chevronleft"></use>
							</svg>
							<span class="hover-show text text3">上一篇</span>
						</a>
					</li>
																<li class="widescreen-more">
					<a class="btn-comments hover-box low-height" href="https://blog.csdn.net/zwq912318834/article/details/79614372" title="python3下使用scrapy实现模拟用户登录与cookie存储 —— 基础篇（马蜂窝）">
						<svg class="icon hover-hide" aria-hidden="true">
							<use xlink:href="#csdnc-chevronright"></use>
						</svg>
						<span class="hover-show text text3">下一篇</span>
					</a>
				</li>
							</ul>
		</li>
	</ul>
</div>
<script>window._bd_share_config = { "common": { "bdSnsKey": {}, "bdText": "", "bdMini": "1", "bdMiniList": false, "bdPic": "", "bdStyle": "0", "bdSize": "16" }, "share": {} }; with (document) 0[(getElementsByTagName('head')[0] || body).appendChild(createElement('script')).src = 'https://csdnimg.cn/static/api/js/share.js?v=89860594'];</script>
<script>
    var recommendCount = 76;
    recommendCount = recommendCount > 1 ? (recommendCount + (recommendCount>6 ? 2 : 1)) : recommendCount;
    var articleTit = articleTitles;
    var ChannelId = 33;
    var articleId = "79571110";
    var commentscount = 8;
    var islock = false;
    var curentUrl = "https://blog.csdn.net/zwq912318834/article/details/79571110";
    var myUrl = "https://my.csdn.net/";
    //1禁止评论，2正常
    var commentAuth = 2;
    //百度搜索
    var baiduKey = "python+requests+%E6%A8%A1%E6%8B%9F%E7%99%BB%E5%BD%95";
    var needInsertBaidu = false;
    // 代码段样式
    var codeStyle = '';
		var highlight = ["python3","\u4f7f\u7528","requests","\u5b9e\u73b0","\u6a21\u62df","\u7528\u6237\u767b\u5f55","\u57fa\u7840","\u9a6c\u8702\u7a9d"];//高亮数组
		// 相关推荐博主数据
    var RecommendBlogExpertList = [{"user_name":"qq_32059827","nick_name":"\u6768\u9053\u9f99","avatar":"https:\/\/avatar.csdn.net\/5\/D\/9\/3_qq_32059827.jpg","is_expert":true,"article_count":451,"rank":"2000+"},{"user_name":"u014483914","nick_name":"beyond_LH","avatar":"https:\/\/avatar.csdn.net\/6\/6\/8\/3_u014483914.jpg","is_expert":false,"article_count":130,"rank":"\u5343\u91cc\u4e4b\u5916"},{"user_name":"qq_41888542","nick_name":"\u83dc\u9e1fPython\u7b14\u8bb0","avatar":"https:\/\/avatar.csdn.net\/A\/D\/8\/3_qq_41888542.jpg","is_expert":false,"article_count":152,"rank":"\u5343\u91cc\u4e4b\u5916"},{"user_name":"zwq912318834","nick_name":"Kosmoo","avatar":"https:\/\/avatar.csdn.net\/7\/4\/8\/3_zwq912318834.jpg","is_expert":false,"article_count":75,"rank":"\u5343\u91cc\u4e4b\u5916"},{"user_name":"Cooler_max","nick_name":"Cooler_max","avatar":"https:\/\/avatar.csdn.net\/1\/E\/4\/3_cooler_max.jpg","is_expert":false,"article_count":1,"rank":"\u5343\u91cc\u4e4b\u5916"},{"user_name":"sinat_33487968","nick_name":"Thorrrrrrrrrr","avatar":"https:\/\/avatar.csdn.net\/A\/2\/0\/3_sinat_33487968.jpg","is_expert":false,"article_count":89,"rank":"\u5343\u91cc\u4e4b\u5916"},{"user_name":"lantiancaiyun","nick_name":"pgplayer_upc","avatar":"https:\/\/avatar.csdn.net\/1\/2\/7\/3_lantiancaiyun.jpg","is_expert":false,"article_count":198,"rank":"\u5343\u91cc\u4e4b\u5916"},{"user_name":"phplaoniao","nick_name":"hotProgramming","avatar":"https:\/\/avatar.csdn.net\/7\/B\/4\/3_phplaoniao.jpg","is_expert":false,"article_count":21,"rank":"\u5343\u91cc\u4e4b\u5916"},{"user_name":"qq_32106647","nick_name":"\u5fd8\u4e86\u957f\u53d1\u6a21\u6837","avatar":"https:\/\/avatar.csdn.net\/B\/C\/5\/3_qq_32106647.jpg","is_expert":false,"article_count":71,"rank":"\u5343\u91cc\u4e4b\u5916"},{"user_name":"hi_chen_xingwang","nick_name":"\u6715\u5c31\u662f\u8fd9\u4e48\u5e05","avatar":"https:\/\/avatar.csdn.net\/0\/A\/C\/3_hi_chen_xingwang.jpg","is_expert":false,"article_count":45,"rank":"\u5343\u91cc\u4e4b\u5916"}];

		var articleType = 1;
		var CopyrightContent = '本文为博主原创文章，未经博主允许不得转载。';
</script>
<script src="https://csdnimg.cn/public/sandalstrap/1.4/js/sandalstrap.min.js"></script>
<script src="https://csdnimg.cn/release/phoenix/vendor/pagination/paging.js"></script>
<script src='https://csdnimg.cn/public/common/gotop/js/goTop-v1.0.min.js?v201811201455'></script>
<script>
    GoTop({
        right: 8,
        hasReport: true,
        reportFun: function() {
            showReport(false,articleTit);
        }
    })
</script>

<script src="//g.csdnimg.cn/baidu-search/1.0.0/baidu-search.js"  type="text/javascript"></script>
</body>

<!-- 右侧第四栏 -->
<div class="fourth_column">
	<div class="title-box">
		<b class="title">猿学习</b>
		<span class="fourth_column_close">    
			<svg class="icon" aria-hidden="true">
				<use xlink:href="#csdnc-times"></use>
			</svg>
		</span>
		
	</div>
	<ul class="">
		<li><div id="kp_box_456" data-pid="456" data-track-view='{"mod":"kp_popu_456-721","con":",,"}' data-track-click='{"mod":"kp_popu_456-721","con":",,"}'><a href="https://edu.csdn.net/topic/python115?utm_source=blogright"_blank">  <div class="blogkp1"><img src="http://img-ads.csdn.net/2018/201812181221437658.png"width="100" height="100"></div></li>		<li><div id="kp_box_457" data-pid="457" data-track-view='{"mod":"kp_popu_457-681","con":",,"}' data-track-click='{"mod":"kp_popu_457-681","con":",,"}'><img src="http://img-ads.csdn.net/2019/201901081453403307.jpg"width="100" height="100"></div></li>		<li><div id="kp_box_458" data-pid="458" data-track-view='{"mod":"kp_popu_458-638","con":",,"}' data-track-click='{"mod":"kp_popu_458-638","con":",,"}'><a href="https://edu.csdn.net/topic/ai30?utm_source=blogright" target="_blank">  <div class="blogkp1"><img src="http://img-ads.csdn.net/2018/201812181217034101.png"width="100" height="100"><h6>转行人工智能工程师</h6></div></a></div></li>		<li><div id="kp_box_459" data-pid="459" data-track-view='{"mod":"kp_popu_459-687","con":",,"}' data-track-click='{"mod":"kp_popu_459-687","con":",,"}'><img src="http://img-ads.csdn.net/2018/201811231432284520.jpg"width="100" height="100"></div></li>	</ul>
</div>
<script type="text/javascript">
	$('.fourth_column_close').click(function(){
		$('.fourth_column').remove();
	})
</script>
<!-- 右侧第四栏end -->
<!-- 高亮未与 markdown兼容  -->
	<link rel="stylesheet" href="https://csdnimg.cn/release/blog_editor_html/release1.3.4/ckeditor/plugins/codesnippet/lib/highlight/styles/atom-one-dark.css">
	<script type="text/javascript" src="https://csdnimg.cn/release/phoenix/production/pc_wap_common-98040b5dc6.js" /></script>
	
	<!-- <script type="text/javascript" src="https://csdnimg.cn/release/phoenix/production/markdownCopy-718168246b.js" /></script> -->


<script src="https://g.csdnimg.cn/login-box/1.0.4/??login-box.js,login-auto.js?t=20190103145159"></script>
<script src="https://csdnimg.cn/release/phoenix/template/js/common-c1c7b20e03.min.js"></script>
<script src="https://csdnimg.cn/release/phoenix/template/js/detail-a4e18dfef2.min.js"></script>
	<script src="https://csdnimg.cn/release/phoenix/themes/skin-yellow/skin-yellow-fc7383b956.min.js"></script>


<!-- <script type="text/javascript" src="//g.csdnimg.cn/check-adb/1.0.2/check-adb.js"></script> -->

<script type="text/javascript" src="https://static-blog.csdn.net/mdeditor/public/res/bower-libs/MathJax/MathJax.js?config=TeX-AMS-MML_HTMLorMML"></script>
<script type="text/x-mathjax-config">
    MathJax.Hub.Config({
            "HTML-CSS": {
                    linebreaks: { automatic: true, width: "94%container" },
                    imageFont: null
            },
            tex2jax: {
                preview: "none"
            },
            mml2jax: {
                preview: 'none'
            }
    });
</script>
<script type="text/javascript">
    window.baidu_blueword ={
        di:'24004469_oem_dg',
        id:['content_views'],// 需要飘蓝区域：id要求以数组或，分隔的字符串形式传入
        blueclass:['baidu_pl'],// 需要飘蓝区域：class要求以数组或，分隔的字符串形式传入, 传入值会覆盖默认值
        user:'',
        isMobile:false,
        title: document.title,
        page_url: location.href,
        ignore:'baidu-blue-word-no',// 需要忽略掉的区域1
        frequency:3,// 词频1
        maxword:20// 最大接受飘词个数
    }
</script>
<script src="https://gh.bdstatic.com/static/gh/js/sdk/bword.min.js"></script>
</html>
"""

soup = BeautifulSoup(html,"html.parser")   #使用python的标准库   html.parser

res=soup.select('a [class="hover-show text text3"]')

str=res[0]
print(str.string)

yy=soup.select("h3[id=13-了解session]")

print((yy))

yy=yy[0]

print(yy)

#----------------------------------动脑学院视频------------------------------------------------
import urllib.request
from urllib import request

#1,获取网页源码
def get_html(url):
    user_agent="Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko"
    headers={"User-Agent":user_agent}

    req=request.Request(url=Url,headers=headers)
    response=urllib.request.urlopen(req)    #打开网址
    content=response.read()              #读取源代码   b'开头的内容是字节流
    #print(content)
    return  content

articleUrl="https://www.qiushibaike.com/textnew/page/%d"
page = 0
while True:
    #用户输入操作
    raw=input("来，点击回车查看或输入exit退出，Now make your choice:")
    if raw=="exit":
        break
    page += 1
    Url = articleUrl % page
#for i in range(1,5):
#    page=i
#    Url=articleUrl%page     #格式化，完整链接，格式化有：%s   %d    {}.formate()

    #print(Url)
    #Gethtml=get_html(Url)

    articlePage=get_html(Url)

    #2,解析内容
    soup22 = BeautifulSoup(articlePage,"html.parser")
    #print(soup)
    icount = 1
    for string22 in soup22.find_all(attrs="article block untagged mb15"):
        print("\n")
        print(icount,",",string22.find(attrs="content").get_text().strip())
        icount+=1

    print(Url)
    #yy=soup22.select("div[class=content]")
    #print((yy))


#3、用户输入操作

