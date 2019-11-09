from Minecraft_GUI_Dependancies import *
from tkinter.ttk import Frame
from mine import *

x1 = IntVar( )
y1 = IntVar( )
z1 = IntVar( )

x2 = IntVar( )
y2 = IntVar( )
z2 = IntVar( )

blkID = IntVar( )
blkData = IntVar( )

axe = IntVar( )
revchk = IntVar( )
oc = IntVar( )

def Preview( ):
	pass

def duplicButton( ):
	global mc

	xs, xf = int( x1.get( ) ), int( x2.get( ) )
	ys, yf = int( y1.get( ) ), int( y2.get( ) )
	zs, zf = int( z1.get( ) ), int( z2.get( ) )

	if xs > xf:
		xs, xf = xf, xs
	if ys > yf:
		ys, yf = yf, ys
	if zs > zf:
		zs, zf = zf, zs

	#blocks = 

	if revchk == False:
		pass
	else:
		pass
		# taw ba3d

def Duplicate( main ):
	frame = Frame( main )
	frame.pack( side = LEFT )

	msg = Message( main, 'Clone' )
	msg.place( x = 5, y = -9 )

	tx = Message( frame, 'Axe' )
	tx.grid( column = 13, row = 0, pady = 7 )

	xr = Radiobutton( frame )
	xr.grid( column = 14, row = 0 )
	xr.configure( variable = axe )
	xr.configure( value = 0 )
	xr.configure( text = "X" )

	yr = Radiobutton( frame )
	yr.grid( column = 15, row = 0 )
	yr.configure( variable = axe )
	yr.configure( value = 1 )
	yr.configure( text = "Y" )

	zr = Radiobutton( frame )
	zr.grid( column = 16, row = 0 )
	zr.configure( variable = axe )
	zr.configure( value = 2 )
	zr.configure( text = "Z" )

	chk = Checkbutton( frame )
	chk.grid( column = 13, row = 1, columnspan = 4)
	chk.configure( variable = revchk )
	chk.configure( text = 'Revert' )

	occtxt = Message( frame, 'Occurrence' )
	occtxt.grid( column = 0, row = 0, rowspan = 2 )

	occ = Entry( frame )
	occ.grid( column = 1, row = 0, rowspan = 2, padx = 5 )
	occ.configure( textvariable = oc )
	occ.configure( width = 4 )

	btn1, btn2 = Righty( main )
	btn1.configure( command = duplicButton )
	btn2.configure( command = Preview )