# Pyekyll / Python与Jekyll的简易博客系统

好吧同志们，本项目其实一点也不玄学，不需要NodeJs和NPM，我用了Python的方式最简单的实现了一个比较美观且好做的方案，如果你觉得Jekyll在GithubPage上的主题不错，那么你选对地方了。这里不需要服务器部署，不需要终端知识，只需要一个手即可。

好的，现在我来简单讲解以下运行方式。

## Jekyll方面

首先本实例中使用[cayman](https://github.com/pages-themes/cayman)主题，实际上，不用Jekyll主题也一样可以实现，只不过你需要用HTML与Markdown适配，这需要另外的js库，所以不建议。

## 博客位置

对于博客来说，我们的文章需要储存到某一个特定位置，这时候创建文件夹是一个很好的方式，就像文件里面的example1和example2文件夹

![博客位置](https://i.gyazo.com/d1a338a1c3bec55acfd6208dd370b16d.png "博客位置")

接下来我们只需要将文章使用markdown形式写入这两个文件夹即可，例如在example1内有一个ex.md，那么当你访问这篇文章时，链接就会是https://your-domain.com/example1/ex，就是这个原理。

## Python方面

这个python实现也很简单，首先你需要在本项目目录下运行[这个文件](https://github.com/alltobebetter/Pyekyll/blob/master/deploy.py)，遍历文件夹内容并给出相应markdown内容，我这么说你一定不是很明白，没关系，下面是实际演示。

> 第一步：克隆到本地或您选择的云端，直接下载或者使用Git都可以，我这里用了Git

![克隆](https://i.gyazo.com/7c423ca95afbb7042606dcda9f34c7bc.png "克隆")

> 第二步：运行deploy.py文件

```python
python /work/Pyekyll/deploy.py #请把这里换成您自己的路径，deploy.py里也有路径设置
```

> 第三步：查看同路径下是否出现new.md文件

![new](https://i.gyazo.com/460ae6954180fb3048f9fabd26417fba.png "new")

详细内容如下：

![内容](https://i.gyazo.com/91f90441a13119765700ee9479db32c5.png "内容")

> 最后

我们复制到index.md相应位置中，于是就实现了博客的基本链接归档，其余的您可以根据自己的情况更改，本项目可更新方面十分显著，恳求您可以pull request来使这个项目更加完好！
