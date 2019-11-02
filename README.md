# rpull
python3 shell trick for recursive git pull

### what is it
if you type "rpull", you can recursive update all rep's in current path  

#### easy install trick

```bash
mkdir -p ~/.bash_tricks && curl https://raw.githubusercontent.com/germanwb/rpull/master/rpull.py --output ~/.bash_tricks/rpull.py && echo 'alias rpull='python3 ~/.bash_tricks/rpull.py --path \$\(pwd\)'' >> ~/.bash_aliases && alias rpull='python3 ~/.bash_tricks/rpull.py --path $(pwd)
```
