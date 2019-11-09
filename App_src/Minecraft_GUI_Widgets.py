import tkinter.ttk as ttk
import tkinter as tk
from Minecraft_GUI_Global_Variables import btn


def VPackPart( root ):
	frame = ttk.Frame( root )
	frame.configure( relief = tk.GROOVE )
	frame.pack( side = tk.TOP, fill = tk.BOTH, expand = True )
	frame.configure( borderwidth = "2" )
	frame.pack( padx = 7, pady = 7 )
	return frame

def HPackPart( root ):
	frame = ttk.Frame( root )
	frame.pack( side = tk.LEFT, fill = tk.BOTH , expand = True )
	return frame

def Message( root, txt ):
	msg = tk.Message( root )
	msg.configure( background = '#d9d9d9' )
	msg.configure( foreground = '#000000' )
	msg.configure( width = 250 )
	msg.configure( text = txt )
	return msg

def Button( root, txt ):
	btn = ttk.Button( root )
	btn.configure( padding = ( 2, 0, 0, 0 ) )
	btn.configure( text = txt )
	btn.configure( state = tk.DISABLED )
	return btn

def Entry( root ):
	ent = ttk.Entry( root )
	return ent

def Righty( main ):
	righty = tk.Frame( main )
	righty.pack( side = tk.RIGHT )
	righty.configure( background = '#d9d9d9' )

	btn1 = Button( righty, 'Draw Square' )
	btn1.pack( padx = 7, side = tk.RIGHT )
	btn1.configure( width = 15 )

	btn2 = Button( righty, 'Preview' )
	btn2.pack( padx = 5, side = tk.RIGHT )
	btn2.configure( width = 10 )

	btn.append( btn1 )
	btn.append( btn2 )

	return btn1, btn2