from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title('Dumb Ass Title')
root.iconbitmap('alien.ico')

#image location using PIL
my_img1 = ImageTk.PhotoImage(Image.open("images/aspen.png"))
my_img2 = ImageTk.PhotoImage(Image.open("images/aspen2.png"))
my_img3 = ImageTk.PhotoImage(Image.open("images/me1.png"))
my_img4 = ImageTk.PhotoImage(Image.open("images/me2.png"))
my_img5 = ImageTk.PhotoImage(Image.open("images/me3.png"))

#create a list of all images
image_list = [my_img1, my_img2, my_img3, my_img4, my_img5]

#start view of status bar at bottom
status = Label(root, text="Image 1 of " + str(len(image_list)), bd=1, relief=SUNKEN, anchor=E)

#creating the label for the status bar
my_label = Label(image = my_img1)
my_label.grid(row=0, column=0, columnspan=3)

#forward button function created with known image_number inside the function
def forward(imgage_number):
	global my_label
	global button_forward
	global button_back

	my_label.grid_forget()
	my_label = Label(image = image_list[imgage_number-1])
	button_forward  = Button(root, text=">>", command=lambda: forward(imgage_number + 1))
	button_back = Button(root, text="<<", command=lambda: back(imgage_number - 1))
		#disables the foward button on the last picture
	if imgage_number == 5:
		button_forward = Button(root, text=">>", state=DISABLED)
		#places label and both buttons using grid instead of pack
	my_label.grid(row=0, column=0, columnspan=3)
	button_forward.grid(row=1, column=2)
	button_back.grid(row=1, column=0)
		#updates the status with current image_number and length of list of images
	status = Label(root, text="Image " + str(imgage_number) + " of " + str(len(image_list)), bd=1, relief=SUNKEN, anchor=E)
	status.grid(row=2, column=0, columnspan=3, sticky=W+E)

#back button
def back(imgage_number):
	global my_label
	global button_forward
	global button_back

	my_label.grid_forget()
	my_label = Label(image = image_list[imgage_number-1])
	button_forward  = Button(root, text=">>", command=lambda: forward(imgage_number + 1))
	button_back = Button(root, text="<<", command=lambda: back(imgage_number - 1))
		#disables back button if image_number is 1
	if imgage_number == 1:
		button_back = Button(root, text="<<", state=DISABLED)
		#places labels in grid
	my_label.grid(row=0, column=0, columnspan=3)
	button_forward.grid(row=1, column=2)
	button_back.grid(row=1, column=0)
		#update status with current image number and length of list of images
	status = Label(root, text="Image " + str(imgage_number) + " of " + str(len(image_list)), bd=1, relief=SUNKEN, anchor=E)
	status.grid(row=2, column=0, columnspan=3, sticky=W+E)

button_back = Button(root, text="<<", command=back, state=DISABLED)
button_exit = Button(root, text="Exit Program", command=root.quit)
button_forward = Button(root, text=">>",command=lambda: forward(2))

button_back.grid(row=1, column=0)
button_exit.grid(row=1, column=1)
button_forward.grid(row=1, column=2, pady=10)
status.grid(row=2, column=0, columnspan=3, sticky=W+E)


root.mainloop()