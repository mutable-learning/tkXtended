import tkinter as tk
from tkinter import ttk


class ScrollableList(tk.Listbox):

    def __init__(self, master, **kwargs):
        scroll_h = kwargs.pop("scroll_h", False)
        scroll_v = kwargs.pop("scroll_v", False)
        self.container_frame = ttk.Frame(
            master,
            borderwidth=1,
            relief="groove",
        )
        if scroll_v:
            self.vertical_scroll = ttk.Scrollbar(
                self.container_frame,
                orient=tk.VERTICAL,
                command=self.yview,
            )
        kwargs.setdefault("yscrollcommand", self.vertical_scroll.set)
        self.vertical_scroll.pack(side=tk.RIGHT, fill=tk.Y)
        if scroll_h:
            self.horizontal_scroll = ttk.Scrollbar(
                self.container_frame,
                orient=tk.HORIZONTAL,
                command=self.xview,
            )
        kwargs.setdefault("xscrollcommand", self.horizontal_scroll.set)
        self.horizontal_scroll.pack(side=tk.BOTTOM, fill=tk.X)

        super().__init__(self.container_frame, **kwargs)
        super().pack(side=tk.LEFT, fill=tk.BOTH, expand=1)

    def place(self, *args, **kwargs):
        return self.container_frame.place(*args, **kwargs)

    def pack(self, *args, **kwargs):
        return self.container_frame.pack(*args, **kwargs)

    def grid(self, *args, **kwargs):
        return self.container_frame.grid(*args, **kwargs)


if __name__ == "__main__":
    root = tk.Tk()
    scrolling_listbox = ScrollableList(root, scroll_h=True, scroll_v=True)
    scrolling_listbox.pack(fill=tk.BOTH)

    for i in range(1, 101):
        scrolling_listbox.insert(tk.END, f"A long entry number: {i}")

    root.mainloop()
