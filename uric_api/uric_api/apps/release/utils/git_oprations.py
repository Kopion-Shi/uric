import os

# 拉取git仓库并获得分支数据
def get_git_branchs(git_addr, git_code_dir):
    '''
    :param git_addr:  远程仓库的ssh地址
    :return:  该仓库的分支列表数据
    '''

    # 1 检出(git clone)前的动作

    # 2 检出代码

    # 3 检出后动作

    # 后面3步是在点击发布的时候进行的
    # 4 发布前，对目标主机执行的动作

    # 5 发布

    # 6 发布后，对目标主机执行的动作

    # git仓库地址：git_addr = 'git@gitee.com:mooluo_admin/hippo.git'
    # 本地仓库目录：git_pro_name = gitee.com/mooluo_admin
    git_path_name = "/".join(git_addr.split("@")[-1].replace(":", "/")[:-4].split("/")[:-1])

    # 如果确定以后公司只会在某个git平台上存储git版本，则本地仓库目录采用项目名即可：hippo
    # 项目目录名：pro_name = 'hippo'
    pro_name = git_addr.rsplit('/')[-1].split('.')[0]

    # 指定git存储目录，目前的方式是在settings中配置的GIT_CODE_DIR的目录下根据项目名称创建一个目录，然后进入到这个目录里面再执行git clone
    # from django.conf import settings
    # git_code_dir = settings.GIT_CODE_DIR
    git_dir_path = f'{git_code_dir}/{git_path_name}'  # '/home/moluo/Desktop/hippo/hippo_api/projects/gitee.com/mooluo_admin'
    git_pro_path = f'{git_code_dir}/{git_path_name}/{pro_name}'  # '/home/moluo/Desktop/hippo/hippo_api/projects/gitee.com/mooluo_admin/hippo'
    # import os
    if os.path.exists(git_pro_path):
        git_branch_info = os.popen(f'cd {git_pro_path} && git pull {git_addr} && git branch -r').readlines()
        # git_branch_info = ['已经是最新的。\n', '  origin/HEAD -> origin/master\n', '  origin/dev\n', '  origin/master\n']
        git_branch_info_s = git_branch_info[2:]
    else:
        git_branch_info = os.popen(
            f'mkdir -p -m 777 {git_dir_path} && cd {git_dir_path} && git clone {git_addr} && cd {pro_name} && git branch -r').readlines()[
                          1:]
        # git_branch_info = ['  origin/HEAD -> origin/master\n', '  origin/dev\n', '  origin/master\n']
        git_branch_info_s = git_branch_info[1:]

    # 查看提交版本的指令 git log --pretty="%h %an %s" --since="2020" --before="2021"  -10    #-10指的是最近的10次提交记录
    print('git_branch_info>>>', git_branch_info)
    print('git_branch_info_s>>>>', git_branch_info_s)
    # 将查看分支指令的返回结果进行加工，筛选出所有的分支名称
    branch_list = [i.split('/')[-1].replace('\n', '') for i in git_branch_info_s]
    print('>>>>>', branch_list)
    return branch_list


# 获取git 仓库中分支的commit版本信息
def get_git_commits(branchs_name, git_addr, git_code_dir):
    # git仓库代码的存储路径
    git_path_name = "/".join(git_addr.split("@")[-1].replace(":", "/")[:-4].split("/")[:-1])
    # git仓库名称
    pro_name = git_addr.rsplit('/')[-1].split('.')[0]
    git_pro_path = f'{git_code_dir}/{git_path_name}'
    print(git_pro_path)
    print('branchs_name>>', branchs_name)
    result = os.popen(
        f'cd {git_pro_path}/{pro_name} && git checkout {branchs_name} && git log --pretty="%h %an %s"').readlines()[1:]
    print('result>>>>', result)
    res_dict = {}  # {'版本id号'，版本具体信息, }
    for i in result:
        i_list = i.split(' ')
        res_dict[i_list[0]] = i

    return res_dict
