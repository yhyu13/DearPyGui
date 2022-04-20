import dearpygui.dearpygui as dpg

dpg.create_context()
dpg.create_viewport(height=200, width=200)
dpg.setup_dearpygui()


def cb_button1a(sender, app_data, user_data):
    print(f"B1a sender: {sender} {app_data} {user_data}")


class myClass(object):

    def __init__(self):
        pass

    def cb_button1b(self, sender, app_data, user_data):
        print(f"B1b sender: {sender} {app_data} {user_data}")

    def cb_button2(*args, **kwargs):
        print(f"B2 args: {args}")
        print(f"B2 kwargs: {kwargs}")


myclass = myClass()


with dpg.window(label="Example"):
    dpg.add_text("Hello world")
    dpg.add_button(tag="b1a", label="Button1a", callback=cb_button1a)
    dpg.add_button(tag="b1b", label="Button1b", callback=myclass.cb_button1b)
    dpg.add_button(tag="b2", label="Button2", callback=myclass.cb_button2)


dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()