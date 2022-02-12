playbook will include 3 roles. 
1. nginx - local role with apt installation and conf template tasks and a service handler
2. docker - nothing to configure here, so preferred to use a community role from ansible-galaxy
3. logrotate - local role with config copy and cron task


**untested**
