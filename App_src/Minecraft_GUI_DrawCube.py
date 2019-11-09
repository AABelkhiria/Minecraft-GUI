from Minecraft_GUI_Dependancies import *

def drawButton( ):
	xs, xf = int( x1.get( ) ), int( x2.get( ) )
	ys, yf = int( y1.get( ) ), int( y2.get( ) )
	zs, zf = int( z1.get( ) ), int( z2.get( ) )

	if xs > xf:
		xs, xf = xf, xs
	if ys > yf:
		ys, yf = yf, ys
	if zs > zf:
		zs, zf = zf, zs
	
	ID = int( blkID.get( ) )
	data = int( blkData.get( ) )

	try:
		for xi in range( xs, xf + 1 ):
			for yi in range( ys, yf + 1 ):
				for zi in range( zs, zf + 1 ):
					if GV.mc.getBlock( xi, yi, zi ) != 7:
						GV.mc.setBlock( xi, yi, zi, block.Block( ID, data ) )
	except Exception as e:
		if DEBUG:
			print e

def DrawCubic( main ):
	frame = Frame( main )
	frame.pack( side = LEFT )

	msg = Message( main, 'Draw Cube' )
	msg.place( x = 5, y = -9 )

	btn1, btn2 = Righty( main )
	btn1.configure( command = drawButton )
	btn2.configure( command = lambda : PreviewCube( x1, x2, y1, y2, z1, z2 ) )