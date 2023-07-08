
if [ -z $UPSTREAM_REPO ]
then
  echo "Cloning main Repository"
  git clone https://github.com/maharaja91/DQ-_BULLET.git /DQ-_BULLET
else
  echo "Cloning Custom Repo from $UPSTREAM_REPO "
  git clone $UPSTREAM_REPO /DQ-_BULLET
fi
cd /DQ-_BULLET
pip3 install -U -r requirements.txt
echo "Starting DQ-_BULLET..."
python3 bot.py
