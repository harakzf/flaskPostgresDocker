declare time=`date '+%T'`
mkdir ./gitLog/${time}

declare commitWord=$1

# ステージ追加
git add --all . 

# コミット
git commit -m "${commitWord}" > ./gitLog/${time}/gitCommit.log

# プッシュ
git push origin master

