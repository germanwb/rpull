# rpull
python3 shell trick for recursive git pull

### what is it
if you type "rpull", you can recursive pull all rep's in current path  , or m_rpull for switch to master and pull repos in curr path  

#### easy install trick

```bash
mkdir -p ~/.bash_tricks && curl https://raw.githubusercontent.com/germanwb/rpull/master/rpull.py --output ~/.bash_tricks/rpull.py; echo "alias rpull='python3 ~/.bash_tricks/rpull.py --path \$\(pwd\)'" >> ~/.bash_aliases; alias rpull='python3 ~/.bash_tricks/rpull.py --path $(pwd)'; echo "alias m_rpull='python3 ~/.bash_tricks/rpull.py --path \$\(pwd\) -switch'" >> ~/.bash_aliases; alias m_rpull='python3 ~/.bash_tricks/rpull.py --path $(pwd) -switch'
```
