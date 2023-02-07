import os

global g_path

g_path = "C:\\Users\\geniusShi\\Nutstore\\1\\我的坚果云\A知识库HTML\\技术\\黑马入门资料Markdown"


def d_RemoveDir():
    for v_root, v_dirs, v_files in os.walk(g_path):
        # 通过listdir判断文件夹是否为空.
        if not os.listdir(v_root):
            os.rmdir(v_root)
        # 查看删除后的结果.
        for v_file in v_files:
            v_rf = os.path.join(v_root+r'\\'+v_file)
            print(v_rf)
    return


d_RemoveDir()
