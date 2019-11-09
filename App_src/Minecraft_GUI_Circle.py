from Minecraft_GUI_Dependancies import *
from tkinter.ttk import Frame
from mine import *

position = IntVar( )
fillchk = IntVar( )
r = IntVar( )

def SetBlockCircle( x, y, z, ID, data ):
	if GV.mc.getBlock( x, y, z ) != BEDROCK:
		GV.mc.setBlock( x, y, z, block.Block( ID, data ) )

def Set4Blocks( xi, zi ,ID, data ):
	if position.get( ) == 1:
		x = int( x1.get( ) )
		y = int( y1.get( ) )
		z = int( z1.get( ) )
	elif position.get( ) == 2:
		x = int( x2.get( ) )
		y = int( y2.get( ) )
		z = int( z2.get( ) )
	SetBlockCircle( x + xi, y, z + zi, ID, data )
	SetBlockCircle( x + xi, y, z - zi, ID, data )
	SetBlockCircle( x - xi, y, z + zi, ID, data )
	SetBlockCircle( x - xi, y, z - zi, ID, data )

def drawButton( ):
	global r
	global fillchk

	radius = int( r.get( ) )
	ID = int( blkID.get( ) )
	data = int( blkData.get( ) )


	fill = int( fillchk.get( ) )

	if radius >= 0 and ID >= 0 and data >= 0 :
		try:
			if fill == 0:
				x2, z2 = radius, 0
				while x2 > z2:
					Set4Blocks( x2, z2 ,ID, data )
					z2 = z2 + 1
					x2 = int ( sqrt( radius**2 - z2**2 ) )

				x2, z2 = 0, radius
				while z2 > x2:
					Set4Blocks( x2, z2 ,ID, data )
					x2 = x2 + 1
					z2 = int ( sqrt( radius**2 - x2**2 ) )

			else:
				for x2 in range( radius + 1 ):
					for z2 in range( radius + 1 ):
						if ( x2**2 + z2**2 ) <= radius**2:
							Set4Blocks( x2, z2 ,ID, data )

		except Exception as e:
			if DEBUG:
				print e
			tkMessageBox.showerror( "Error", "An error occured !" )
			for button in btn:
				button.configure( state = DISABLED )

def CircleFrame( main ):
	frame = Frame( main )
	frame.pack( side = LEFT )

	msg = Message( main, 'Draw Circle' )
	msg.place( x = 5, y = -9 )

	text = Message( frame, 'Radius' )
	text.grid( column = 0, row = 0, padx = 5, pady = 10, rowspan = 2 )

	ra = Entry( frame )
	ra.grid( column = 1, row = 0, padx = 5, pady = 10, rowspan = 2 )
	ra.configure( textvariable = r )
	ra.configure( width = 6 )

	r.set( 1 )

	pos1 = Radiobutton( frame )
	pos1.grid( column = 3, row = 0, padx = 5, pady = 5 )
	pos1.configure( variable = position )
	pos1.configure( value = 1 )
	pos1.configure( text = "Center Position 1" )

	pos2 = Radiobutton( frame )
	pos2.grid( column = 3, row = 1, padx = 5, pady = 5 )
	pos2.configure( variable = position )
	pos2.configure( value = 2 )
	pos2.configure( text = "Center Position 2" )

	position.set( 1 )

	chk = Checkbutton( frame )
	chk.grid( column = 4, row = 0, rowspan = 2, padx = 5, pady = 10 )
	chk.configure( variable = fillchk )
	chk.configure( text = 'fill' )

	btn1, btn2 = Righty( main )
	btn1.configure( command = drawButton )
	btn2.configure( command = lambda : PreviewCircle( x, y, z, r, fillchk ) )