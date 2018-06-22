# 容器部署演示

为了简化部署，让用户开箱即用，我们通过容器来部署 gitlab-analytics + mysql + grafana。

用户通过如下方式启动服务：

	git clone https://github.com/NDHWAlliance/gitlab-analytics.git
	cd gitlab-analytics
	docker-compose up mysql grafana gitlab-analytics

以上的命令执行时发生的动作：

* 启动mysql并初始化DB和数据表。
* 启动grafana，并配置好mysql datasource，并创建好默认的dashboard。
* 启动gitlab-analytics web server。

假设用户执行以上命令的服务器IP是`172.16.154.5`，那么通过以下方式访问各个服务：

1. gitlab-analytics管理界面

	* 访问地址：http://172.16.154.5:8080/admin
	* 用户可以在管理界面配置GitLab API URL & ACCESS TOKEN
	* gitlab-analytics会自动给gitlab里所有的project配置好webhook

1. gitlab-analytics webhook handler

	* 访问地址：http://172.16.154.5:8080/webhook
	* 这个地址会被gitlab-analytics自动添加到gitlab的所有project里。
	* 后续gitlab里发生的任何event，都会发送至这个地址。
	* webhook handler里会处理event数据，存入mysql表。

1. grafana

	* 访问地址：http://172.16.154.5:3000/
	* 容器启动时会自动配置好datasource & dashboard，开箱即用。

```
.
├── docker-compose.yml
├── gitlab-analytics
│   ├── Dockerfile
│   ├── gitlab_analytics_models.py
│   ├── requirements.txt
│   └── web.py
├── grafana
│   ├── dashboards
│   │   └── mydashboard.json
│   ├── grafana.ini
│   └── provisioning
│       ├── dashboards
│       │   └── gitlab_analytics.yaml
│       └── datasources
│           └── gitlab_analytics.yaml
├── mysql
│   ├── 1.add_readonly_user.sql
│   ├── 2.create_table.sql
│   └── 3.sample_data.sql
└── readme.md
```