import os

def generate_index():
    """遍历目录并生成新的index.md文件"""

    sections = {
        "example1": "示例类别1：",
        "example2": "示例类别2："#注意最后一行没有逗号
    """这里多加几行就是多几个类别，前面是文件夹名称，后面是显示名称"""
    }

    base_path = "/work/Pyekyll/"  # 请改到您所在的文件路径

    with open("new.md", "w", encoding="utf-8") as new_file:
        for section, title in sections.items():
            folder_path = os.path.join(base_path, section)  # 构造完整路径
            files = [f[:-3] for f in os.listdir(folder_path) if f.endswith(".md")]
            links = [f"[{name}](/" + section + "/" + name + ")" for name in files]
            line = title + ", ".join(links) + "\n\n"
            new_file.write(line)

if __name__ == "__main__":
    generate_index()
