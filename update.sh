declare commitWord=$1
declare date=`date '+%T'`
declare GIT_COMMIT_LOG=./${date}_gitCommit.log
declare GIT_PUSH_LOG=./${date}_gitPush.log

# ステージ追加
git add --all . 

# コミット
git commit -m '${commitWord}' > $GIT_COMMIT_LOG

# プッシュ
git push origin master > $GIT_PUSH_LOG

echo '完了'