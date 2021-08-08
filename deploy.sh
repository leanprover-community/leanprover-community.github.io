set -e
set -x

git clone --branch master "https://$DEPLOY_GITHUB_USER:$DEPLOY_GITHUB_TOKEN@github.com/leanprover-community/leanprover-community.github.io.git" ./build

./make_site.py
cd blog
nikola build
mv output ../build/blog
cd ..

if [ "$github_repo" = "leanprover-community/leanprover-community.github.io" -a "$github_ref" = "refs/heads/newsite" ]; then
  cd build/
  git config user.email "leanprover.community@gmail.com"
  git config user.name "leanprover-community-bot"
  git add -A .
  git diff-index HEAD
  git diff-index --quiet HEAD || { git commit -m "deploy site from $git_hash" && git push; }
fi
