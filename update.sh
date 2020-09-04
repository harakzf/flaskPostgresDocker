declare commitWord=$1
declare time=`date '+%H%M%S'`

# ステージ追加
git add --all . 

# コミット
git commit -m "${commitWord}" > ./gitCommitLog/${time}.log

# プッシュ
git push origin master

