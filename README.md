在其他程序中调用时，请调用api.py中的类  


- 基类为api.py文件中的Client类与dbapi.py文件中的相关数据库操作的类  
- Client类主要包括从免费代理网站上抓取免费代理，并检查代理可用性，并存入数据库中
- dbapi.py中包含各类数据库的常用方法进行封装，目前只有最简单的sqlite
 