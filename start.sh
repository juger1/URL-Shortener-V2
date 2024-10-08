if [ -z $SOURCE_CODE ]
then
  echo "Cloning main Repository"
  git clone https://github.com/juger1/adlinkfly-telegram-bot/ /adlinkfly-telegram-bot
else
  echo "Cloning Custom Repo from $SOURCE_CODE "
  git clone $SOURCE_CODE /adlinkfly-telegram-bot
fi
cd /content
pip3 install -U -r requirements.txt
echo "Starting Bot...."
python3 get_config.py && python3 main.py
