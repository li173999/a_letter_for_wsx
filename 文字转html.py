import tkinter as tk
from tkinter import filedialog, messagebox

def convert_text_to_html_paragraphs(text):
    """将普通文本转换为HTML段落标签格式"""
    lines = text.strip().split('\n')
    html_lines = []
    
    for line in lines:
        # 跳过空行
        if line.strip():
            html_line = f"<p>{line}</p>"
            html_lines.append(html_line)
    
    return '\n'.join(html_lines)

def convert_button_clicked():
    # 获取输入框的文本
    input_text = input_text_box.get("1.0", "end-1c")
    
    if not input_text.strip():
        messagebox.showwarning("警告", "请输入文本")
        return
    
    # 转换文本
    html_output = convert_text_to_html_paragraphs(input_text)
    
    # 清空输出框并显示结果
    output_text_box.delete("1.0", tk.END)
    output_text_box.insert("1.0", html_output)

def open_file():
    file_path = filedialog.askopenfilename(
        title="选择文本文件",
        filetypes=[("Text files", "*.txt"), ("All files", "*.*")]
    )
    
    if file_path:
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                text = file.read()
                input_text_box.delete("1.0", tk.END)
                input_text_box.insert("1.0", text)
        except Exception as e:
            messagebox.showerror("错误", f"读取文件时出错: {e}")

def save_file():
    if not output_text_box.get("1.0", "end-1c").strip():
        messagebox.showwarning("警告", "没有内容可保存")
        return
        
    file_path = filedialog.asksaveasfilename(
        title="保存为HTML",
        defaultextension=".html",
        filetypes=[("HTML files", "*.html"), ("Text files", "*.txt"), ("All files", "*.*")]
    )
    
    if file_path:
        try:
            with open(file_path, 'w', encoding='utf-8') as file:
                file.write(output_text_box.get("1.0", "end-1c"))
            messagebox.showinfo("成功", f"已保存到 {file_path}")
        except Exception as e:
            messagebox.showerror("错误", f"保存文件时出错: {e}")

def copy_to_clipboard():
    app.clipboard_clear()
    app.clipboard_append(output_text_box.get("1.0", "end-1c"))
    messagebox.showinfo("复制成功", "HTML代码已复制到剪贴板")

# 创建主窗口
app = tk.Tk()
app.title("文本转HTML段落")
app.geometry("800x600")
app.configure(padx=20, pady=20)

# 创建框架
input_frame = tk.Frame(app)
input_frame.pack(fill=tk.BOTH, expand=True)

output_frame = tk.Frame(app)
output_frame.pack(fill=tk.BOTH, expand=True)

button_frame = tk.Frame(app)
button_frame.pack(fill=tk.X, pady=(10, 0))

# 输入区域
tk.Label(input_frame, text="输入文本:").pack(anchor="w")
input_text_box = tk.Text(input_frame, wrap=tk.WORD, height=10)
input_text_box.pack(fill=tk.BOTH, expand=True, pady=(0, 10))

# 添加滚动条到输入区域
input_scrollbar = tk.Scrollbar(input_text_box)
input_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
input_text_box.config(yscrollcommand=input_scrollbar.set)
input_scrollbar.config(command=input_text_box.yview)

# 输出区域
tk.Label(output_frame, text="HTML输出:").pack(anchor="w")
output_text_box = tk.Text(output_frame, wrap=tk.WORD, height=10)
output_text_box.pack(fill=tk.BOTH, expand=True)

# 添加滚动条到输出区域
output_scrollbar = tk.Scrollbar(output_text_box)
output_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
output_text_box.config(yscrollcommand=output_scrollbar.set)
output_scrollbar.config(command=output_text_box.yview)

# 按钮
open_button = tk.Button(button_frame, text="打开文本文件", command=open_file)
open_button.pack(side=tk.LEFT, padx=(0, 10))

convert_button = tk.Button(button_frame, text="转换为HTML", command=convert_button_clicked)
convert_button.pack(side=tk.LEFT, padx=(0, 10))

copy_button = tk.Button(button_frame, text="复制到剪贴板", command=copy_to_clipboard)
copy_button.pack(side=tk.LEFT, padx=(0, 10))

save_button = tk.Button(button_frame, text="保存HTML文件", command=save_file)
save_button.pack(side=tk.LEFT)

# 启动应用
app.mainloop()