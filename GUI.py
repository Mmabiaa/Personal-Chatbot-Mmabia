import tkinter as tk
from Chatbot import get_response
import logging

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

#Using OOP
class ChatApp:
    def __init__(self,root):
        self.root = root
        self.root.title("'Personal Assistant Chatbot -Mmabia ")
        self.root.geometry("400x500")
        self.chat_log = tk.Text(root, bg="grey",state="disabled", wrap=tk.WORD )

        self.chat_log.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

        self.entry_box = tk.Entry(root, bg= "white")
        self.entry_box.pack(padx=10, pady=(0,10), fill=tk.X, expand=True )
        self.entry_box.bind("<Return>", self.send_message)

    def send_message(self, event):
        user_input = self.entry_box.get()
        self.chat_log.config(state="normal")
        self.chat_log.insert(tk.END, "You:" + user_input + "\n")

        self.chat_log.config(state="disabled")

        logging.debug(f'User Input: {user_input}')
        response = get_response(user_input)
        logging.debug(f'Bot response: {response}')
        

        self.chat_log.config(state="normal")
        self.chat_log.insert(tk.END, "Bot: " + response + "\n")

        self.chat_log.config(state="disabled")
    def on_closing(self):
        logging.debug('CLosing Application.'), self.root.destroy()


if __name__ == "__main__":
    try: 
        root=tk.Tk()
        app = ChatApp(root)
        root.mainloop()
    except:
        logging.debug('Error in main loop.')