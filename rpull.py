import argparse
import os


def check_it(root_path: str):
    list_of_dir = os.listdir(root_path)
    checked_dirs = []
    for p in list_of_dir:
        full_path = os.path.join(root_path, p)
        if not os.path.isdir(full_path):
            continue
        elif not os.path.isdir(os.path.join(full_path, '.git')):
            continue
        else:
            checked_dirs.append(p)
    return checked_dirs


def recursive_pull(list_of_repo: list, root_dir: str, switch: bool):
    for repo in list_of_repo:
        print('%+50s' % f'\n\n\n=====_update {repo}_=====')
        if switch:
            bash = f'cd {os.path.join(root_dir, repo)}&& git checkout master && git pull'
        else:
            bash = f'cd {os.path.join(root_dir, repo)}&& git pull'
        os.system(bash)


def main():
    parser = argparse.ArgumentParser(description='pls set path to root of recurse')
    parser.add_argument('--path', type=str, help='root path')
    parser.add_argument('-switch', action='store_true')
    args = parser.parse_args()
    path = args.path
    if not os.path.isdir(path) or path is None:
        print('error path')
        exit(-1)
    gits = check_it(root_path=path)
    print(f'start recursive pull in {path} ')
    master_switch = args.switch
    if master_switch:
        print('and switch to master')
    if len(gits) == 0:
        print("no git dir's")
    else:
        print(f'list of repos {gits}, press ENTER to start (or ctl+C for canceling)')
        input()
    recursive_pull(list_of_repo=gits, root_dir=path, switch=master_switch)
    print('Done')


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("Canceling")
        exit(0)
