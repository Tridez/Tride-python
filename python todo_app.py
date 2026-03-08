#!/usr/bin/env python3
# todo_app.py
"""
一个简单的待办清单 GUI 小程序（使用 tkinter）。
功能：添加、删除、标记完成/未完成、保存到文件、从文件加载、清空。
注：代码写得偏清晰、易懂，适合初学者阅读与修改。
"""

import tkinter as tk
from tkinter import ttk, messagebox, filedialog

class TodoApp(tk.Tk):
    """把整个应用封装成一个类，便于组织代码与复用。继承 tk.Tk 表示这个类就是主窗口。"""
    def __init__(self):
        super().__init__()  # 初始化父类（tk.Tk）
        self.title("待办清单 - Todo App")
        self.geometry("420x350")  # 窗口大小（宽x高）
        self.resizable(False, False)  # 不允许调整窗口大小（初学者先固定）
        self.tasks = []  # 用一个列表保存任务，每项是 [text, done_bool]

        self.create_widgets()  # 把界面构建提取成一个方法，结构清晰

    def create_widgets(self):
        """创建并布局所有控件（Entry、Listbox、Buttons、Scrollbar 等）"""
        # 顶部：输入框 + 添加按钮
        frame_top = ttk.Frame(self)
        frame_top.pack(padx=10, pady=10, fill="x")

        self.entry_var = tk.StringVar()  # 绑定到 Entry，方便读取和清空输入
        self.entry = ttk.Entry(frame_top, textvariable=self.entry_var)
        self.entry.pack(side="left", expand=True, fill="x")
        # 按回车也能添加任务
        self.entry.bind("<Return>", self.add_task)

        add_btn = ttk.Button(frame_top, text="添加", command=self.add_task)
        add_btn.pack(side="left", padx=5)

        # 中部：任务列表 + 滚动条
        frame_mid = ttk.Frame(self)
        frame_mid.pack(padx=10, pady=(0,10), fill="both", expand=True)

        # tkinter 的 Listbox 用来显示多行文本（任务）
        self.listbox = tk.Listbox(frame_mid, activestyle="none")
        self.listbox.pack(side="left", fill="both", expand=True)
        # 双击列表项时切换“完成/未完成”状态
        self.listbox.bind("<Double-Button-1>", self.toggle_done)

        scrollbar = ttk.Scrollbar(frame_mid, orient="vertical", command=self.listbox.yview)
        scrollbar.pack(side="right", fill="y")
        self.listbox.config(yscrollcommand=scrollbar.set)

        # 底部：操作按钮（删除、标记、保存、加载、清空）
        frame_bot = ttk.Frame(self)
        frame_bot.pack(padx=10, pady=10, fill="x")

        rem_btn = ttk.Button(frame_bot, text="删除", command=self.remove_task)
        done_btn = ttk.Button(frame_bot, text="标记（完成/未完成）", command=self.toggle_done)
        save_btn = ttk.Button(frame_bot, text="保存...", command=self.save_tasks)
        load_btn = ttk.Button(frame_bot, text="加载...", command=self.load_tasks)
        clear_btn = ttk.Button(frame_bot, text="清空", command=self.clear_all)

        # pack 顺序会影响按钮在行内的显示位置
        rem_btn.pack(side="left")
        done_btn.pack(side="left", padx=5)
        # 把保存/加载/清空放到右边，更符合使用习惯
        clear_btn.pack(side="right", padx=5)
        load_btn.pack(side="right", padx=5)
        save_btn.pack(side="right")

    # —— 下面是操作函数（业务逻辑） —— #
    def add_task(self, event=None):
        """把 Entry 中的文字作为新任务加入 self.tasks 并刷新列表显示"""
        text = self.entry_var.get().strip()
        if not text:
            messagebox.showwarning("提示", "请输入任务内容。")
            return
        self.tasks.append([text, False])  # False 表示尚未完成
        self.entry_var.set("")  # 清空输入框
        self.refresh_listbox()

    def remove_task(self):
        """删除当前选中的任务"""
        sel = self.listbox.curselection()
        if not sel:
            messagebox.showinfo("提示", "请选择要删除的任务。")
            return
        idx = sel[0]
        del self.tasks[idx]
        self.refresh_listbox()

    def toggle_done(self, event=None):
        """切换所选任务的完成状态（完成 <-> 未完成）"""
        sel = self.listbox.curselection()
        if not sel:
            messagebox.showinfo("提示", "请选择要标记的任务（双击或先选中）。")
            return
        idx = sel[0]
        self.tasks[idx][1] = not self.tasks[idx][1]
        self.refresh_listbox()

    def clear_all(self):
        """清空所有任务（带确认）"""
        if messagebox.askyesno("确认", "确定要清空所有任务吗？"):
            self.tasks.clear()
            self.refresh_listbox()

    def save_tasks(self):
        """弹出文件保存对话框并把任务保存到文本文件（每行：完成标志(tab)任务文本）"""
        path = filedialog.asksaveasfilename(defaultextension=".txt",
                                            filetypes=[("Text files","*.txt"),("All files","*.*")])
        if not path:
            return
        try:
            # 保存格式：每行 "1\t任务文本" 或 "0\t任务文本"
            with open(path, "w", encoding="utf-8") as f:
                for text, done in self.tasks:
                    flag = "1" if done else "0"
                    f.write(f"{flag}\t{text}\n")
            messagebox.showinfo("保存成功", f"已保存到：\n{path}")
        except Exception as e:
            messagebox.showerror("保存失败", str(e))

    def load_tasks(self):
        """从文件加载任务（与保存格式对应）"""
        path = filedialog.askopenfilename(filetypes=[("Text files","*.txt"),("All files","*.*")])
        if not path:
            return
        try:
            with open(path, "r", encoding="utf-8") as f:
                self.tasks = []
                for line in f:
                    line = line.rstrip("\n")
                    if not line:
                        continue
                    if "\t" in line:
                        flag, text = line.split("\t", 1)
                        done = (flag == "1")
                    else:
                        # 兼容旧格式：没有 flag
                        done = False
                        text = line
                    self.tasks.append([text, done])
            self.refresh_listbox()
            messagebox.showinfo("加载成功", f"已从：\n{path}\n加载 {len(self.tasks)} 条任务。")
        except Exception as e:
            messagebox.showerror("加载失败", str(e))

    def refresh_listbox(self):
        """把 self.tasks 的内容渲染到 listbox 中（显示 ✔️ 表示已完成）"""
        self.listbox.delete(0, tk.END)
        for text, done in self.tasks:
            display = "✔️ " + text if done else text
            self.listbox.insert(tk.END, display)

# 入口：只有直接运行本文件时才启动应用（便于以后把这个模块导入别的脚本）
if __name__ == "__main__":
    app = TodoApp()
    app.mainloop()  # 启动 tkinter 的事件循环（必须）
