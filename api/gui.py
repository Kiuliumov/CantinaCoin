import customtkinter as ctk
from tkinter import messagebox
from threading import Thread
import subprocess
import sys


class BlockchainGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Blockchain Server Control")
        self.root.geometry("400x250")

        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")

        self.port_label = ctk.CTkLabel(root, text="Enter Port:")
        self.port_label.pack(pady=10)

        self.port_entry = ctk.CTkEntry(root, width=200)
        self.port_entry.insert(0, "5000")  # Default port
        self.port_entry.pack(pady=5)

        self.start_button = ctk.CTkButton(root, text="Start Server", command=self.start_server, width=150, height=40)
        self.start_button.pack(pady=10)

        self.stop_button = ctk.CTkButton(root, text="Stop Server", command=self.stop_server, width=150, height=40,
                                         state=ctk.DISABLED)
        self.stop_button.pack(pady=5)

        self.process = None

    def start_server(self):
        port = self.port_entry.get()

        if not port.isdigit():
            messagebox.showerror("Invalid Port", "Please enter a valid port number.")
            return

        self.start_button.configure(state=ctk.DISABLED)
        self.stop_button.configure(state=ctk.NORMAL)

        self.process = Thread(target=self.run_server, args=(port,))
        self.process.start()

    def run_server(self, port):
        """ Runs the Flask server with the specified port. """
        try:
            subprocess.run([sys.executable, "app.py", "-p", port])
        except Exception as e:
            messagebox.showerror("Server Error", f"Error starting server: {e}")
        finally:
            self.start_button.configure(state=ctk.NORMAL)
            self.stop_button.configure(state=ctk.DISABLED)

    def stop_server(self):
        """ Stops the Flask server by terminating the process. """
        if self.process:
            self.process.join()
            self.start_button.configure(state=ctk.NORMAL)
            self.stop_button.configure(state=ctk.DISABLED)
            messagebox.showinfo("Server Stopped", "The server has been stopped.")


if __name__ == "__main__":
    root = ctk.CTk()

    gui = BlockchainGUI(root)

    root.mainloop()
