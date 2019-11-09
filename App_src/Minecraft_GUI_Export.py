from Minecraft_GUI_Dependancies import *
from mine import *

entry = StringVar( )

def ExportButton( ):
	global x1, x2, y1, y2, z1, z2

	xs, xf = int( x1.get( ) ), int( x2.get( ) )
	ys, yf = int( y1.get( ) ), int( y2.get( ) )
	zs, zf = int( z1.get( ) ), int( z2.get( ) )
	f1, f2, f3 = 0, 0, 0

	if xs > xf:
		xs, xf = xf, xs
		f1 = 1
	if ys > yf:
		ys, yf = yf, ys
		f2 = 1
	if zs > zf:
		zs, zf = zf, zs
		f3 = 1

	if entry.get( ) == "":
		name = str( dt.now( ) ).split( " " )[0] + str( dt.now()).split( "." )[1] + ".blk"
	else:
		if entry.get( ).endswith( ".blk" ):
			name = entry.get( )
		else:
			name = entry.get( ) + ".blk"

	with open( name, 'w+' )  as file:
		file.write( "f " + str( f1 ) + " " + str( f2 ) + " " + str( f3 ) + "\n" )
		try:
			for y in range( ys, yf + 1 ):
				for z in range( zs, zf + 1 ):
					for x in range( xs, xf + 1 ):
						blockId = str( GV.mc.getBlockWithData( x, y, z ).id )
						blockData = str( GV.mc.getBlockWithData( x, y, z ).data )
						file.write( blockId + ',' + blockData + ' ' )
					file.write( '\n' )
				file.write( '*\n' )
		except Exception as e:
			if DEBUG:
				print e
			tkMessageBox.showerror( "Error", "Connection lost !" )
			for button in btn:
				button.configure( state = DISABLED )

def ExportFrame( frame ):
	msg = Message( frame, 'Export' )
	msg.place( x = 5, y = -9 )

	text = Message( frame, 'name' )
	text.pack( padx = 5, pady = 10, side = LEFT )

	name = Entry( frame )
	name.pack( padx = 5, side = LEFT )
	name.configure( textvariable = entry )
	name.configure( width = 35 )

	btn3 = Button( frame, 'Export' )
	btn3.pack( padx = 7, side = RIGHT )
	btn3.configure( width = 15 )
	btn3.configure( command = ExportButton )

	btn.append( btn3 )