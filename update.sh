declare commitWord=$1
declare date=`date '+%T'`

mkdir ${date}_log

declare GIT_COMMIT_LOG=./${date}_log/gitCommit.log

# ステージ追加
git add --all . 

# コミット
git commit -m "${commitWord}" > $GIT_COMMIT_LOG

# プッシュ
git push origin master

