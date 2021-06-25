#### 功能

#### 1. GitPythonCheck.py
从 gitlab 仓库中查询某个关键字
##### 用法
python GitPythonCheck.py [分支] [关键字] [项目列表]<br>
`python GitPythonCheck.py dev '\"tts' lesson,home,onboarding`
##### 结果
```
find regex: tts from projects: ['lesson'] branch: dev
clone lesson dev...
work_path: ./gitPython/lesson
--- find from project lesson ---
TrailClassAuxServiceImpl.java
[186, 232, 233, 390, 465, 466]
LessonAuxServiceImpl.java
[772, 812]
UserUtils.java
[54, 80]
LotteryServiceImpl.java
[85, 86]
```
##### 说明
替换脚本中  `https://gitlab.xxx.com/backend/` 为自己的地址


#### 2. pre-push.sh
git pre push hook, 阻止本地对特殊分支 git push -f 操作

##### 用法
根据需要修改保护分支：PROTECTED_BRANCHS=("master" "rc" "dev")

1. mkdir $HOME/.githooks
2. cd $HOME/.githooks
3. vim pre-push
4. git config --global core.hooksPath $HOME/.githooks
5. chmod +x $HOME/.githooks/pre-push
