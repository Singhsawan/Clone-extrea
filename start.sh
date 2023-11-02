
if [ -z $UPSTREAM_REPO ]
then
  echo "Cloning main Repository"
  git clone https://github.com/RealZenX/autofilterv4.git /autofilterv4
else
  echo "Cloning Custom Repo from $UPSTREAM_REPO "
  git clone $UPSTREAM_REPO /autofilterv4
fi
cd /autofilterv4
pip3 install -U -r requirements.txt
echo "Starting lucy..."
python3 bot.py
